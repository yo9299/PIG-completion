#start from the root: is there a maximal center? if p-node and yes(i.e. non empty), call main with node. If q-node, consider all the subtrees induced by vertices contained in the sections and check if they have more than three leaves (non empty, leaves from a section can be empty)m -> call main with the node restricted to the corresponding senctions? 

import numpy as np 
from computeq import computeW0, update, rightCost, leftCost, getLastSection, getFirstSection
import math 
from classes import Node, Leaf, State, Pnode, Qnode 
import computep as putils 
import computeq as qutils 
from dfs import create_indices

class StateQsplit:
    def __init__(self,  qnode):
        #n is the nbr
        self.r = qnode.nbr_vertices_subtree() 
        self.vertices = qnode.get_vertices() + qnode.children #qnode.get_vertices_subtree()
        self.C = {x: np.zeros(self.r +1) for x in qnode.get_vertices() + qnode.children }
        self.C2 = { x: np.zeros((self.r+1, self.r+1)) for x in qnode.get_vertices() + qnode.children }
        #initialize with infinity
        self.W = np.ones((self.r +1, self.r +1))*math.inf
        self.U = {x: np.zeros((self.r+1, self.r+1)) for x in qnode.get_vertices() + qnode.children }
        #create lrx and modify update so that it calls a dictionay instead of function
        self.L = {x: np.zeros(self.r+1) for x in qnode.get_vertices() + qnode.children }

    def accessL(self, vertex, r):
        return self.L[vertex][r]
    
    def accessC(self, vertex, r):
        return self.C[vertex][r]
    
    def accessC2(self, vertex, r, s):
        return self.C2[vertex][r][s]
    
    def accessU(self, vertex, r,s):
        return self.U[vertex][r][s]
    
    def accessW(self, r,s):
        return self.W[r][s]
    
    def updateL(self, vertex, r,value):
        self.L[vertex][r] = value 

    def updateC(self, vertex, r, value):
        self.C[vertex][r] = value 
    
    def updateC2(self, vertex, r,s, value):
        self.C2[vertex][r][s] = value 

    def updateU(self, vertex, r,s, value ):
        self.U[vertex][r][s] = value 

    def updateW(self, r, s, value):
        self.W[r][s] = value


def main(tree):
    create_indices(tree)
    n = tree.size()
    r = math.floor(tree.nbr_vertices_subtree()/2) +1
    state = State(n, r)
    queue = sorted([tree] + tree.get_descendants(), key= lambda x:x.index, reverse=True)
    while queue: 
        node = queue.pop()
        if not queue:
            break
            W = finalS(node, state)
        elif isinstance(node, Leaf):
            putils.updateLeaf(node, state)
        elif isinstance(node, Pnode):
            putils.updatePnode(node, state)
        elif isinstance(node, Qnode):
            #break
            qutils.updateQnode(node, state)
    print(state.M)
    """sol = math.inf
    for x in range(r):
        sol = min(sol,state.accessM(tree, x))
    """
    return state #W #sol

def finalS(qnode, state):
    #perfect the bounds, otherwise we will reach errors
    stateq = finalR(qnode, state)
    for r in range( qnode.nbr_vertices_subtree()+1):
        for s in range(1, qnode.nbr_vertices_subtree()+1):
            if isFeasible(qnode,r,s):
                stepS(qnode, state, stateq, r, s)
    return stateq.W  

def initialize(qnode, state):
    w = computeW0(qnode, state)
    stateq = StateQsplit(qnode)
    stateq.updateW(0,0, w)
    for v in stateq.C.keys(): #qnode.get_vertices_subtree():
        stateq.updateC(v, 0, update(qnode, state, v, 0))
        stateq.updateC2(v, 0,0, update(qnode, state, v, 0) )
    return stateq

def stepR(qnode, state, stateq, r):
    #stateq = initialize(qnode, state)
    vertex = min(stateq.C, key= lambda x: stateq.accessC(x,r-1))
    stateq.updateW(r, 0,stateq.accessW( r-1, 0)+ stateq.accessC(vertex, r-1) )
    stateq.updateU(vertex, r,0, stateq.accessU(vertex,r-1, 0)+1)
    stateq.updateC(vertex, r, update(qnode,state,vertex, stateq.accessU(vertex, r, 0)))
    stateq.updateC2(vertex, r, 0, math.inf)
    for y in stateq.vertices:
        if y != vertex:
            stateq.updateU(y, r, 0, stateq.accessU(y,r-1,0))
            stateq.updateC(y, r, stateq.accessC(y, r-1))
            #is this correct?
            stateq.updateC2(y, r,0, stateq.accessC2(y, r-1,0))

#this one is correct
def finalR(qnode, state):
    stateq = initialize(qnode, state)
    for r in range(1, qnode.nbr_vertices_subtree()+1):
        stepR(qnode, state,stateq, r)
    return stateq

def findSplitSubtree(stateq, r):
    split = None
    for x in stateq.C.keys():
        if isinstance(x, Node) and stateq.accessC2(x,r,0) == math.inf and stateq.accessU(x,r,0)< x.nbr_vertices_subtree():
            split = x 
            break 
    return split 

#the s is wrong
def initialSnonsplit(qnode, state, stateq, r):
    print(stateq.C2.keys())
    for x in stateq.C2.keys():
        #print(f"for {x} stateq.accessC2(x,r,0)")
        #continue
        if stateq.accessC2(x,r,0) != math.inf:
            stateq.updateL(x, r, leftCost(qnode, x) - verticesToLeft(qnode, x, stateq, None, r))
            stateq.updateC2(x,r,0, updatel(qnode,state, x, 0, stateq.accessL(x,r)))
        else: 
            stateq.updateC2(x,r,0, updatel(qnode,state, x, 0, math.inf))

def initialS(qnode, state, stateq, r):
    #separate cases where tree is split and not.
    split = findSplitSubtree(stateq, r)
    if split: 
        s = int(split.nbr_vertices_subtree() - stateq.accessU(split,r,0))
        print(s)
        stateq.updateW(r,s,stateq.accessW(r,0) - rightCost(qnode, split))
        stateq.updateU(split,r,s,x.nbr_vertices_subtree())
    else :
        s= 0
    for x in stateq.C2.keys():
        if x != split and stateq.accessC2(x,r,0) != math.inf:
            stateq.updateL(x, r, leftCost(qnode, x) - verticesToLeft(qnode, x, stateq, split, r))
            stateq.updateC2(x,r,s, updatel(qnode,state, x, 0, stateq.accessL(x,r)))
        else: 
            stateq.updateC2(x,r,s, updatel(qnode,state, x, 0, math.inf))
    
def stepS(qnode, state, stateq, r,s):
    vertex = min(stateq.C2, key= lambda x: stateq.accessC2(x,r, s-1))
    print(f"the value{stateq.accessL(vertex,r)}")
    stateq.updateW(r, s,stateq.accessW( r, s-1)+ stateq.accessC2(vertex, r, s-1) )
    stateq.updateU(vertex, r, s,stateq.accessU(vertex,r,s-1)+1)
    stateq.updateC2(vertex, r, s,updatel(qnode, state, vertex, stateq.accessU(vertex, r,s), stateq.accessL(vertex,r)))
    for y in stateq.vertices:
        if y != vertex:
            stateq.updateU(y, r,s, stateq.accessU(y,r,s-1))
            stateq.updateC2(y, r,s, stateq.accessC2(y, r,s-1))

def updatel(qnode, state, subtree, k, left):
    value = 0
    if isinstance(subtree, Leaf) and k == 0:
        value = left - rightCost(qnode, subtree)
    elif isinstance(subtree, Node):
        n = subtree.nbr_vertices_subtree() #-1
        if 0<= k and k < n:
            next = k+1 
            if k > n //2:
                k = n-k
            if next > n// 2:
                next = n - next
            print(k)
            value = state.accessM(subtree, next) - state.accessM(subtree, int(k)) + left - rightCost(qnode, subtree)
        else :
            value = math.inf
    elif k == 0:
        value = left - rightCost(qnode, subtree)
    else:
        value = math.inf 
    return value 

def verticesToLeft(qnode, subtree, stateq, split,r):
    if isinstance(subtree, Node):
        i = qnode.children.index(subtree)
    else: 
        i = getFirstSection(qnode, subtree)
    j = 0 
    nbr = 0
    sections = []
    for x in stateq.C2.keys():
        if stateq.accessC2(x,r,0) == math.inf:
            if isinstance(x, Node):
                j = qnode.children.index(x)
                if j < i:
                    nbr += x.nbr_vertices_subtree()
            else: 
                j = getLastSection(qnode, x)
                if j < i:
                    nbr += 1
    return nbr 





#everything below is working
def isFeasible(qnode, r,s):
    v1, v2 = getFirstsCenters(qnode)
    n1 = nb_vertices_induced(qnode, v1)
    n2 = nb_vertices_induced(qnode, v2)
    n12 = nb_vertices_intersection(qnode, v1, v2)
    if r > n1 - n12 and s != n1+n2 - n12 -r:
        return False
    if r < n1 -n12 and s < n1-r :
        return False 
    else: 
        return True  
     

#compute the maximal centers and ni-> nbr vertices in the subtree rooted at the sections
def getNextCenter(qnode, i, v1):
    potv2 = [v for v in qnode.vertices[i] if v not in qnode.vertices[0]]
    v2 = max(potv2, key = lambda x: getLastSection(qnode, x))
    return v2 

def getFirstsCenters(qnode):
    #print(qnode.vertices[0])
    v1 = max(qnode.vertices[0], key= lambda x: getLastSection(qnode, x))
    i = 1
    v2 = getNextCenter(qnode, i ,v1)
    while getLastSection(qnode, v2) <= getLastSection(qnode, v1): 
        i +=1 
        v2 = getNextCenter(qnode, i, v1)
    return v1, v2 

def nb_vertices_induced(qnode, vertex):
    i = getFirstSection(qnode, vertex)
    j = getLastSection(qnode, vertex)
    return nb_vertices_between(qnode, i,j)
    

def nb_vertices_intersection(qnode, v1, v2):
    i = getFirstSection(qnode,v2)
    j = getLastSection(qnode, v1)
    return nb_vertices_between(qnode, i,j)

def nb_vertices_between(qnode, i, j):
    k = i 
    count = 0
    sections = []
    while k <= j :
        sections = sections + [v for v in qnode.vertices[k]]
        count += qnode.children[k].nbr_vertices_subtree()
        k +=1     
    count+= len(set(sections))
    return count 

#main equal but if queue only contains one element, call finalS 

l1 = Leaf([7,9])
l2 = Leaf([2])
l3 = Leaf([6])
l4 = Leaf([4])
l5 = Leaf([5])


p = Pnode([3,4], [l1, l2, l3])
q = Qnode([[1],[1,2], [2,3], [3]], [l1, l2,l3,l4])
p1 = Pnode([7], [p, l4, l5])

l11 =Leaf([11])
l12 = Leaf([12])
l9 = Leaf([9])
l10 = Leaf([10])
pe = Pnode([13], [l9,l10])
pe2=Pnode([6,7], [l5,l11, l12])
#pe = Qnode([[13, 9], [13,10]], [Leaf([]), Leaf([])])

q1 = Qnode([[1],[1,3],[3]], [pe, l2, pe2])
r = Pnode( [8], [l4, q1])