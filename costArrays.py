import trees 
import numpy as np 

def initialize_arrays(tree):
    n = tree.size() 
    #return U and A
    return (np.zeros((n,n)), np.zeros((n,n)))



#have to put an index per node then /or dictionary
def upStep(tree, U, M, node):
    if tree.get_parent() != None:
        b = node.size
        for r in range(round(tree.nb_vertices_subtree(node)/2)):
            curmin = 100000
            for j in range(b):
                if M[u.index][r-j] < curmin:
                    curmin = M[u.index][r-j]
            U[node.index][r] = curmin
    
