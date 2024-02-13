import trees 
import math 
#left costs 
def cost_qsubtree(tree, subtree):
    p = tree.get_parent(subtree)
    brothers= p.children 
    i = brothers.index(subtree)
    j = 0
    cost = 0 
    added=[]

    while j<i:
        cost += tree.nb_vertices_subtree(brothers[j])
        for vert in p.vertices[j]:
            if vert not in p.vertices[i] and vert not in added:
                cost +=1
                added.append(vert)
        j+=1
    return cost

def cost_qvert(tree, node, vertex):
    #find the section it belongs to
    i= 0
    brothers= node.children 
    while i < len(node.vertices):
        if vertex in node.vertices[i]:
            break 
        else: 
            i +=1
    #i think i could just call cost_qsubtree(tree, brothers[i])
    j = 0
    cost = 0 
    while j<i:
        cost += tree.nb_vertices_subtree(brothers[j])
        for vert in node.vertices[j]:
            if vert not in node.vertices[i]:
                cost +=1
        j+=1
    return cost

def rcost_qsubtree(tree, subtree):
    p = tree.get_parent(subtree)
    brothers= p.children 
    i = brothers.index(subtree)
    j = i+1
    cost = 0 
    added = []
    while j>i and j < len(brothers):
        cost += tree.nb_vertices_subtree(brothers[j])
        for vert in p.vertices[j]:
            if vert not in p.vertices[i] and vert not in added:
                cost +=1
                added.append(vert)
        j+=1
    return cost

def rcost_qvert(tree, node, vertex):
    #find the section it belongs to
    i= len(node.vertices)-1
    brothers= node.children 
    while i >=0: # len(node.vertices):
        if vertex in node.vertices[i]:
            break 
        else:
            i = i -1
    #i think i could just call cost_qsubtree(tree, brothers[i])
    j = i+1
    cost = 0 
    while j>i and j< len(brothers):
        cost += tree.nb_vertices_subtree(brothers[j])
        for vert in node.vertices[j]:
            if vert not in node.vertices[i]:
                cost +=1
        j+=1
    return cost

#the costs above are well define, to check below

def initialize_cost_subtree(state, tree, subtree):
    print("subtree")
    subtree.print_node()
    if tree.nb_vertices_subtree(subtree) == 1:
        cost = state.U[subtree.index][0]+ rcost_qsubtree(tree, subtree)-cost_qsubtree(tree, subtree)
    else: 
        
        cost= state.U[subtree.index][1]-state.U[subtree.index][0]+ rcost_qsubtree(tree, subtree)-cost_qsubtree(tree, subtree)

    #return M[subtree.index][1]-M[subtree.index][0]+ rcost_qsubtree(tree, subtree)-cost_qsubtree(tree, subtree)
    #when k is greater than the size of the subtree, we eliminate the cost from the list.
    #when the subtree has size 1, this cost is actually just state.U[0] + etc
    return cost 

def update_cost_subtree(state, tree, subtree, k):
    #if k > rmax, then k= rmax -k 
    rmax = math.floor(tree.nb_vertices_subtree(subtree)/2)
    if k > rmax :
        k = tree.nb_verices_subtree(subtree)-k 
    cost=state.U[subtree.index][k]-state.U[subtree.index][k-1]+ cost_qsubtree(tree,subtree)-rcost_qsubtree(tree, subtree)
    #even worse! since we only have the costs for half of the table, if we are in the other half we need to infer it 
    #return M[subtree.index][k]-M[subtree.index][k-1]+ rcost_qsubtree(tree,subtree)-cost_qsubtree(tree, subtree)
    return cost 

def initialize_costs(state, tree, node): 
    print("node in ")
    node.print_node()
    lsubtrees = node.children 
    lsections= node.vertices 
    lcosts = [] 
    #make this a dictionary
    for s in lsubtrees:
        lcosts.append([s,0, initialize_cost_subtree(state, tree, s)])
    #I'm adding the vertices twice, because they can appear in multiple sections, i should have 
    # in the class a function to get set of vertices (unique)  
    added = []
    for i in range(len(lsections)):    
        for j in lsections[i]:
            if j not in added:
                lcosts.append([j, cost_qvert(tree, node, j) - rcost_qvert(tree, node, j)])
                added.append(j)
    return lcosts 

def update_costs(state, tree, lcosts, chosen):
    if type(chosen[0])== int:
        lcosts.remove(chosen) #[c for c in lcosts if c[0]!= chosen]
    else: 
        for c in range(len(lcosts)):
            if lcosts[c] == chosen:
                lcosts[c][2]= update_cost_subtree(state, tree, chosen[0], chosen[1])
                if chosen[1] == tree.nb_vertices_subtree(chosen[0]):
                    lcosts.remove(chosen)
    return lcosts 

#do this with a dictionary
def select_min(lcosts):
    curmin = 1000000
    pos = None 
    for c in lcosts:
        if c[-1] < curmin:
            curmin = c[-1]
            pos = c 
    return pos 
#compute costs for r 



def initial_rcost(state, tree, node):
    total = 0
    added = []
    for sect in node.vertices:
        for vertex in sect:
            if vertex not in added:
                total += rcost_qvert(tree, node, vertex)
                added.append(vertex)
    for t in node.children:
        total += rcost_qsubtree(tree, t )
        total += state.U[t.index][0]
    return total

def computeqU(state, tree, node):
    print("node")
    node.print_node()
    list_costs= initialize_costs(state, tree, node)
    #define the initial cost with everything right
    icost=initial_rcost(state, tree, node)
    r= 0
    m = tree.nb_vertices_subtree(node)
    W=[]
    while r <= m:
        #the list of costs cannot be empty
        W.append(icost +select_min(list_costs)[-1])
        #W[node.index][r] = icost +select_min(list_costs)[-1]
        list_costs = update_costs(state, tree, list_costs, select_min(list_costs))
        r +=1 
    rmax = math.floor(tree.nb_vertices_subtree(node)/2)
    for r in range(rmax):
        state.U[node.index][r] = min(W[r], W[m-r])
        print("min")
        print(min(W[r], W[m-r]))
        #min(state.M[node.index][r], state.M[node.index][m-r])
    return state