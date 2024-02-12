import numpy as np 

def size_subtrees(tree, added):
    sum = 0
    for node in added:
         sum += tree.nb_vertices_subtree(node)
    return sum 

def add_to_smallest(tree,W, split, already_added, subtree, r):
    tb = tree.nb_vertices_subtree(subtree)
    cost = 100000
    if tb-r >= 0:
        #print(tb-r)
        cost = W[split.index][r-tb] + (r-tb)*tb
        #print(W[split.index][r-tb])
    return cost


def add_to_biggest(tree, W,split, already_added, subtree, r):
    cost = 1000000
    if size_subtrees(tree, already_added)-r >= 0:
        #print(size_subtrees(tree,already_added)-r)
        cost= W[split.index][r] + (size_subtrees(tree, already_added)-r)*tree.nb_vertices_subtree(subtree)
        #print(W[split.index][r])
    return cost 

#print(add_to_smallest(test_tree, W0, [], ))