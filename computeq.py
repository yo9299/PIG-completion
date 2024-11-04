from classes import Node, StateQ
#create state of qnode with cr,x u0x and wr -> tgen update M
import math 
import numpy as np 

def updateQnode(qnode, state):
    s = initialize(qnode, state)
    n = qnode.nbr_vertices_subtree()
    print(s.W)
     
    for r in range(1,n+1):
        stepR(qnode, state, s, r )
        
    for r in range(math.floor(qnode.nbr_vertices_subtree()/2) +1):
        print(r)
        print(s.accessW(r))
        state.updateM(qnode,r, min(s.accessW(r), s.accessW(n-r)))
    
    

        
def initialize(qnode, state):
    w = 0 
    stateq = StateQ(qnode)
    for i in qnode.children:
        w += state.accessM(i,0) +rightCost(qnode, i)*i.nbr_vertices_subtree() 
    sections = set()
    for j in qnode.vertices:
        for el in j:
            if el not in sections:
                sections.add(el)
    w += sum(rightCost(qnode, e) for e in sections)
    stateq.updateW(0, w)

    for v in stateq.C.keys(): #qnode.get_vertices_subtree():
        stateq.updateC(v, 0, update(qnode, state, v, 0))
    return stateq

def stepR(qnode, state, stateq,r):
    vertex = min(stateq.C, key= lambda x: stateq.accessC(x,r-1))
    stateq.updateW(r, stateq.accessW( r-1)+ stateq.accessC(vertex, r-1) )
    stateq.updateU(vertex, r, stateq.accessU(vertex,r-1)+1)
    stateq.updateC(vertex, r, update(qnode,state,vertex, stateq.accessU(vertex, r)))
    for y in stateq.vertices:
        if y != vertex:
            stateq.updateU(y, r, stateq.accessU(y,r-1))
            stateq.updateC(y, r, stateq.accessC(y, r-1))


def update(qnode, state, subtree, k):
    value = 0
    if isinstance(subtree, Node):
        if 0<= k and k <= subtree.nbr_vertices_subtree() -1:
            value = state.accessM(subtree, k+1) - state.accessM(subtree, int(k)) + leftCost(qnode, subtree) - rightCost(qnode, subtree)
        else :
            value = math.inf
    elif k == 0:
        value = leftCost(qnode, subtree) - rightCost(qnode, subtree)
    else:
        value = math.inf 
    return value 


def leftCost(qnode, subtree):
    #subtree can be a subtree or a vertex in a section
    if isinstance(subtree, Node):
        i = qnode.children.index(subtree)
    else: 
        i = 0 
        found = False 
        while i< len(qnode.vertices) and not found:
            if subtree in qnode.vertices[i]:
                found = True 
            else: 
                i += 1 
                print(subtree)
    j= 0
    cost = 0
    added = set(qnode.vertices[i])
    while j< i:
        t = qnode.children[j]
        cost += t.nbr_vertices_subtree() 
        for vert in qnode.vertices[j]:
            if vert not in added:
                cost +=1
                added.add(vert)
        j+=1
    return cost


def rightCost(qnode, subtree):
    #subtree can be a subtree or a vertex in a section
    if isinstance(subtree, Node):
        i = qnode.children.index(subtree)
    else: 
        i = len(qnode.vertices)-1 
        found = False 
        while not found:
            if subtree in qnode.vertices[i]:
                found = True 
            else: 
                i -= 1 
    j= len(qnode.vertices)-1
    cost = 0
    added = set(qnode.vertices[i])
    while j> i:
        t = qnode.children[j]
        cost += t.nbr_vertices_subtree() 
        for vert in qnode.vertices[j]:
            if vert not in added:
                cost +=1
                added.add(vert)
        j-=1
    return cost

