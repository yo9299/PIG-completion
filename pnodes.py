import numpy as np 
import math
import copy 
import trees
     
#p nodes fail for trees of height greater than 1
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
    state.U[node.index][0] = 0
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
                #print("rmax" + str(rmax))
                W1[r] = min(add_to_smallest(state, brothers[0:i], brothers[i], u, r), add_to_largest(state,brothers[0:i], brothers[i], u, r))
                #print(W1[r])
            state.W[u.index]= W1 
            #print("W1")
            #print(W1)
            i +=1 
    for r in range(rmax +1):
        state.M[node.index][r] = min([state.W[u.index][r] for u in node.children])
    return state 
        
def update_U(state, node):
    #print(state.tree.nb_vertices_subtree(node))
    node.print_node()
    print(state.tree.nb_vertices_subtree(node))
    for r in range(math.floor(state.tree.nb_vertices_subtree(node)/2)+1):
        print("r")
        print(r)
        state.U[node.index][r] = min([state.M[node.index][r-i] for i in range(node.size+1) if (r-i) >= 0])
    return state 
    
    
def add_to_smallest(state, added, tobeadded, u, r):
    tb = state.tree.nb_vertices_subtree(tobeadded)# tobeadded.size
    #print(" tb " +str(tb) + " r: "+ str(r))
    if r- tb >= 0:
        cost = state.W[u.index][r-tb] + (r-tb)*tb + state.U[tobeadded.index][0]
        #print("cost " + str(cost))
    else: 
        #print("r-tb <0")
        cost = math.inf 

    return cost 

def add_to_largest(state, added, tobeadded, u, r):
    tb= state.tree.nb_vertices_subtree(tobeadded) #tobeadded.size 
    added.append(u)
    tB = state.tree.size_set_subtrees(added) 
    #print(" tB " +str(tB) + " r: "+ str(r))
    if tB -r >= 0:
        print("tobeadded")
        print(state.W[u.index][r])
        print(state.U[tobeadded.index][0])
        cost = state.W[u.index][r] + (tB -r)*tb + state.U[tobeadded.index][0]
        #when i add a subtree there is also the cost of making the subtree a clique
    else: 
        #print("tB-r<0")
        cost = math.inf
    return cost 
    
        
    
    




