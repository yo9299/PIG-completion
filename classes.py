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
        return self.M[node.index][r]
    
    def accessW(self, node, r):
        return self.W[node.index][r]

    
    def updateU(self, node,r, value):
        self.U[node.index][r] = value

    def accessU(self, node, r):
        return self.U[node.index][r]


    
l = Leaf([1,2])

p = Pnode([3,4], [l])


class Section:
    def __init__(self, vertices, child):
        self.vertices = vertices 
        self.child = child 
    
    def nbr_vertices(self):
        return len(self.vertices)
    

    def __repr__(self):
        return f"Section(vertices={self.vertices}, child={repr(self.child)})"

s = Section( [1,2,3], p) 

l1 = Leaf([4,7])
l2 = Leaf([])
l3 = Leaf([5])
l4 = Leaf([6])
q = Qnode([[1],[1,2], [2,3], [3]], [l1, l2,l3,l4])