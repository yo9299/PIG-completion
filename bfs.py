#import trees 

def expand_node(node):
    return node.children 

def bfs(tree):
    r = tree.get_root()
    sol= [r] + expand_node(r)
    to_be_expanded = [n for n in expand_node(r) if not n.is_leave()]
    #print([n.print_node() for n in to_be_expanded])
    while to_be_expanded != []:
        e= to_be_expanded.pop()
        #print(e.print_node())
        sol = sol + expand_node(e)
        to_be_expanded = to_be_expanded + [n for n in expand_node(e) if not n.is_leave()]
        #print([n.print_node() for n in to_be_expanded])

    sol.reverse()
    return sol


def get_order(tree):
    r = tree.get_root()
    sol = dfs(r, [], [] )
    return sol 
    
        
def exploreNum(graphe, i, pref, suff, p, s):
    pref[i] = p
    p = p+1
    for j in i.children:
        if pref[j]==-1:
        #A <- A + (i,j)
            pref, suff, p, s = exploreNum(graphe, j, pref, suff, p, s)
    suff[i] = s
    s = s+1
    return pref, suff, p, s
    
    
def dfs(tree):
    pref = dict.fromkeys(tree.nodes)
    suf = dict.fromkeys(tree.nodes)
    for i in tree.nodes:
        pref[i] = -1
        suf[i] = -1
    p = 0
    s = 0
    for i in tree.nodes:
        if pref[i] ==-1:
            pref, suff, p, s = exploreNum(tree, i, pref, suf, p, s)
    return suf 


def create_indices(tree):
    sol =dfs(tree)
    for node in tree.nodes:
        node.index = sol[node]

