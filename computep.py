import math
import numpy as np 

def updateLeaf(node, state):
    for r in range(node.nbr_vertices() +1):
        state.updateM(node, r, 0)

def updatePnode(node, state):
    #create pnode state initializing W (n*r) and M*
    # for i in range(nb_childr) -> updateW
    finalW(node, state)
    for r in range(math.floor(node.nbr_vertices_descendants()/2) +1):
        cost = min(state.accessW(n, r) for n in node.children)
        state.updateU(node, r, cost)
    v = node.nbr_vertices() +1
    for r in range(math.floor(node.nbr_vertices_subtree()/2) +1): 
        cost = min(state.accessU(node, r-i) for i in range(v) if (r-i) >= 0) 
        state.updateM(node, r, cost )


def initializeW(node, state):
    r = math.floor(node.nbr_vertices_descendants()/2) +1
    for c in node.children :
        for e in range(r):
            state.updateW(c, e, state.accessM(c, e))
            #print(state.W)

def finalW(node, state):
    initializeW(node, state)
    for u in node.children:
        queue = [ x for x in node.children if x != u]
        added = [u] 
        rmax =math.floor(node.nbr_vertices_descendants()/2) +1
        Wprov = np.ones(rmax)
        while queue:
            toadd = queue.pop()
            for r in range(math.floor(node.nbr_vertices_descendants()/2) +1):
                cost = min(costLargest(state, u, r, added, toadd), costSmallest(state, u, r, toadd))
                #can't update W until i finish with every r
                Wprov[r] = cost 
                if False:
                    print(f"cost largest{costLargest(state, u, r, added, toadd)} and cost small{costSmallest(state, u, r, toadd)}")
                print(state.W)
            added.append(toadd)
            for r  in range(rmax):
                state.updateW(u, r, Wprov[r])
        

 

def nb_vertices_subtrees(list_nodes):
    return sum(n.nbr_vertices_subtree() for n in list_nodes)

def costLargest(state, u, r, added, toadd):
    #addel list of nodes, u and toadd are nodes
    if nb_vertices_subtrees(added) -r >= 0:
        cost = state.accessW(u, r) + (nb_vertices_subtrees(added) -r)* toadd.nbr_vertices_subtree() + state.accessM(toadd, 0) 
    else: 
        cost = math.inf 
    return cost 

def costSmallest(state, u, r, toadd):
    tb= toadd.nbr_vertices_subtree()
    if r- tb >= 0:
        cost = state.accessW(u, r- tb) + (r- tb) * tb + state.accessM(toadd, 0)
    else :
        cost = math.inf
    return cost 
