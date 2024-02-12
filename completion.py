import bfs 
import update 
import trees
import qnodes
import update

def algo(tree):
    print(tree.size)
    M, U, W = update.initialize_arrays(tree)
    bfs.create_indices(tree)
    i=0
    while i < len(bfs.bfs(tree)):
        n = bfs.bfs(tree)[i]
        n.print_node()
        #n = bfs.bfs(tree)[0]
        if not n.is_leave() and n.name == "p":
            W = update.updateW(W, U, tree, n) 
            print("W:")
            print(W) 
        if n.name == "p" or n.name == "l":
            M = update.updateM(W, M, tree, n)
            U = update.updateU(M,U, tree, n)
        elif n.name== "q": 
            M = qnodes.computeqM(M, tree, n)
        print("M")
        print(M)
        
        #print("U")
        #print(U)
        i += 1
    return U 
#actually, return the r that minimizes? and the u 

print(algo(trees.test_tree))
#M,U,W = update.initialize_arrays(trees.testq)
#print(qnodes.computeqM(M,trees.testq, trees.q1))
#print(algo(trees.testq))