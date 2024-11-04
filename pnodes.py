import numpy as np 
import math
import copy 
import trees
     
def initialize_arrays(tree):
    n = tree.size 
    r = math.floor(tree.nb_vertices/2) +1
    M = np.array(np.ones((n,r))*np.inf)
    U = np.array(np.ones((n,r))*np.inf)
    W = np.array(np.ones((n,r))*np.inf)
    return M,U,W

def create_initial_state(tree):
    M,U,W = initialize_arrays(tree)
    tree.initialize_indices()
    return trees.State(W, M, U, tree)

def update_leaves(state, node):
    #not only 0 but every index until leaf.nbr_vertices()?
    for r in range(node.nbr_of_vertices()):
        state.U[node.index][r] = 0
    return state 
    
def update_M(state, node):
    rmax = math.floor(state.tree.size_set_subtrees(node.children)/2) 
    for u in node.children:
        u.print_node()
        state.W[u.index] = copy.copy(state.U[u.index])
        brothers = [b for b in node.children if b != u]
        i = 0
        W1= copy.copy(state.U[u.index])
        while i < len(brothers):
            for r in range(rmax+1):
                W1[r] = min(add_to_smallest(state, brothers[0:i], brothers[i], u, r), add_to_largest(state,brothers[0:i], brothers[i], u, r))
            state.W[u.index]= W1 
            i +=1 
    for r in range(rmax +1):
        state.M[node.index][r] = min([state.W[u.index][r] for u in node.children])
    return state 
        
def update_U(state, node):
    for r in range(math.floor(state.tree.nb_vertices_subtree(node)/2)+1):
        state.U[node.index][r] = min([state.M[node.index][r-i] for i in range(node.size+1) if (r-i) >= 0])
    return state 
    
    
def add_to_smallest(state, added, tobeadded, u, r):
    tb = state.tree.nb_vertices_subtree(tobeadded)
    if r- tb >= 0:
        cost = state.W[u.index][r-tb] + (r-tb)*tb + state.U[tobeadded.index][0]
    else: 
        cost = math.inf 

    return cost 

def add_to_largest(state, added, tobeadded, u, r):
    tb= state.tree.nb_vertices_subtree(tobeadded) 
    added.append(u)
    tB = state.tree.size_set_subtrees(added) 
    if tB -r >= 0:
        cost = state.W[u.index][r] + (tB -r)*tb + state.U[tobeadded.index][0]
    else: 
        cost = math.inf
    return cost 
    
        
    
    




