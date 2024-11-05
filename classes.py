import numpy as np

class Node:
    def __init__(self, vertices, children):
        self.vertices = vertices
        self.children = children 
        self.index = 0
    
    def nbr_vertices(self):
        """Base method. Should be overridden in subclasses."""
        raise NotImplementedError("This method should be implemented by subclasses.")

    def nbr_vertices_descendants(self):
        return sum(child.nbr_vertices_subtree() for child in self.children)
    
    def nbr_vertices_subtree(self):
        """Calculates total vertices in the subtree rooted at this node."""
        return self.nbr_vertices() + self.nbr_vertices_descendants() #sum(child.nbr_vertices_subtree() for child in self.children)
    
    def get_vertices(self):
        """Base method. Should be overridden in subclasses."""
        raise NotImplementedError("This method should be implemented by subclasses.")
    
    def get_vertices_subtree(self):
        return self.get_vertices() + sum([c.get_vertices_subtree() for c in self.children], [])
    
    
    def put_index(self, ind):
        self.index = ind 

    def size(self):
        return 1 + sum([s.size() for s in self.children])
    
    def get_descendants(self):
        return self.children + sum([s.get_descendants() for s in self.children], [])
    
    def __repr__(self):
        return (f"Pnode(vertices={self.vertices}, children=["
                + ", ".join(repr(child) for child in self.children) + "])")
    


class Pnode(Node):
    def __init__(self, vertices, children):
        super().__init__(vertices, children) 

    def nbr_vertices(self):
        return (len(self.vertices))
    
    def get_vertices(self):
        return self.vertices
    
    def __repr__(self):
        return (f"Pnode(vertices={self.vertices}, children=["
                + ", ".join(repr(child) for child in self.children) + "])")
    
    
class Leaf(Pnode):
    def __init__(self, vertices, children=[]):
        super().__init__(vertices, children)
       
    def __repr__(self):
        return f"Leaf(vertices={self.vertices})"
    

    
    
class Qnode(Node):
    def __init__(self, vertices, children): #sections):
        super().__init__(vertices, children)
        #self.sections = sections 
        #self.children = [c.child for c in sections]

    def nbr_vertices(self):
        return len(list(set([v for section in self.vertices for v in section])))
    #sum([s.nbr_vertices() for s in self.sections])
    def get_vertices(self):
        return list(set([v for sublist in self.vertices for v in sublist]))
    
    
    def __repr__(self):
        return (f"Qnode(vertices={self.vertices}, children=["
                + ", ".join(repr(child) for child in self.children) + "])")
  
class State:
#n = tree.size 
#r = math.floor(tree.nb_vertices/2) +1
    def __init__(self, n, r):
        self.n = n
        self.r = r 
        self.W = np.array(np.ones((n,r))*np.inf)
        self.M= np.array(np.ones((n,r))*np.inf)
        self.U = np.array(np.ones((n,r))*np.inf)
        #self.tree = tree 

    def updateW(self, node, r, value):
        self.W[node.index][r] = value

    
    def updateM(self, node, r, value):
        self.M[node.index][r] = value

    def accessM(self, node, r):
        print(f"node{node} r{r}")
        return self.M[node.index][int(r)]
    
    def accessW(self, node, r):
        return self.W[node.index][r]

    
    def updateU(self, node,r, value):
        self.U[node.index][r] = value

    def accessU(self, node, r):
        return self.U[node.index][r]


class StateQ:
    def __init__(self,  qnode):
        #n is the nbr
        self.r = qnode.nbr_vertices_subtree() +1
        self.vertices = qnode.get_vertices() + qnode.children #qnode.get_vertices_subtree()
        self.C = {x: np.zeros(self.r) for x in qnode.get_vertices() + qnode.children }
        self.W = np.zeros(self.r)
        self.U = {x: np.zeros(self.r) for x in qnode.get_vertices() + qnode.children }

    def accessC(self, vertex, r):
        return self.C[vertex][r]
    
    def accessU(self, vertex, r):
        return self.U[vertex][r]
    
    def accessW(self, r):
        return self.W[r]
    
    def updateC(self, vertex, r, value):
        self.C[vertex][r] = value 

    def updateU(self, vertex, r, value ):
        self.U[vertex][r] = value 
    def updateW(self, r, value):
        self.W[r] = value

