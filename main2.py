from dfs import create_indices
import math 
from classes import State, q, Leaf, Pnode, Qnode, Node
import computep as putils
import computeq as qutils 

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
        elif isinstance(node, Qnode):
            
            qutils.updateQnode(node, state)
            
            print(state.M)


    return state

l1 = Leaf([7,9])
l2 = Leaf([2])
l3 = Leaf([6])
l4 = Leaf([4])
l5 = Leaf([5])


p = Pnode([3,4], [l1, l2, l3])
q = Qnode([[1],[1,2], [2,3], [3]], [l1, l2,l3,l4])
p1 = Pnode([7], [p, l4, l5])

if __name__=="__main__":
    main(q)
    #print(1)

l11 =Leaf([11])
l12 = Leaf([12])
l9 = Leaf([9])
l10 = Leaf([10])
pe = Pnode([13], [l9,l10])
pe2=Pnode([6,7], [l5,l11, l12])


q1 = Qnode([[1],[1,3],[3]], [pe, l2, pe2])
r = Pnode( [8], [l4, q1])