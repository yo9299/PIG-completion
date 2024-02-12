import trees as T 
import numpy as np 
import math 
import auxiliarycosts as costs
import copy 

#make a class update of self, tree, W, U Z and the functions update node
def updateUbis(M, U, tree, node):
    if tree.get_parent(node) != None:
        s = tree.get_parent(node).size 
        for r in range(round(tree.nb_vertices_subtree(node)/2)+1):
            U[node.index][r] = min([(M[node.index][r-i] ) for i in range(s) if r-i >=0])
    else: 
        for r in range(round(tree.nb_vertices_subtree(node)/2)+1):
            U[node.index][r] = M[node.index][r]
    return U 

def updateU(M, U, tree, node):
    for r in range(round(tree.nb_vertices_subtree(node)/2)+1):
        U[node.index][r] = min([(M[node.index][r-i] ) for i in range(node.size +1) if r-i >=0])
    return U 
        
def updateW(W,U, tree, node):
    children = node.children

    for u in children: 
        B = u 
        W[u.index] = copy.copy(U[u.index]) #make hard copy so that we don't change U
        #print(W)
        brothers= [c for c in children if c != u  ]   
        i=0
        W1 = copy.copy(U[u.index])     
        while i < len(brothers):
            for r in range(round(tree.nb_vertices_subtree(node)/2)+1):
                #compute optimal way of adding the brothers
                cost1 = costs.add_to_smallest(tree,W,u, brothers[0:i]+[u], brothers[i], r)
                cost2 = costs.add_to_biggest(tree,W,u, brothers[0:i]+[u], brothers[i], r)
                W1[r] = min(cost1, cost2)
            i += 1
        W[u.index] = W1 
        print(W1)
    return W 

def updateM(W,M,tree, node):
    children = node.children
    if children == []:
        M[node.index][0]=0
    else:
        for r in range(round((tree.nb_vertices_subtree(node)-node.size)/2)+1): 
            #remove -node.size for orginial algo?
            M[node.index][r] = min([W[u.index][r] for u in children])
    return M 
    

    
def initialize_arrays(tree):
    n = tree.size 
    M = np.array(np.ones((n,n))*np.inf)
    U = np.array(np.ones((n,n))*np.inf)
    W = np.array(np.ones((n,n))*np.inf)
    return M,U,W







        
