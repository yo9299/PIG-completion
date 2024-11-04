from dfs import create_indices
import math 
from classes import State, q, Leaf, Pnode, Qnode
import computep as putils

def main(tree):
    create_indices(tree)
    n = tree.size()
    r = math.floor(tree.nbr_vertices_subtree()/2) +1
    state = State(n, r)
    queue = sorted([tree] + tree.get_descendants(), key= lambda x:x.index, reverse=True)
    print(queue)
    while queue: 
        node = queue.pop()
        print(node)
        if isinstance(node, Leaf):
            putils.updateLeaf(node, state)
            print(state.M)
        elif isinstance(node, Pnode):
            putils.updatePnode(node, state)
            print(state.W)
            print(state.U)
            print(state.M)

    return state

l1 = Leaf([1,2])
l2 = Leaf([5])
l3 = Leaf([6])

p = Pnode([3,4], [l1, l2, l3])

if __name__=="__main__":
    main(p)