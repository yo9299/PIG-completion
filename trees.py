#class for all nodes being p
import bfs 
class Tree_node:
    #vertices is a list of lists if it is a Q-node
    def __init__(self, children, vertices, name):
        self.children = children 
        self.vertices = vertices
        #self.cost = 0 
        self.name = name
        #name can be leaf, p or q 
        self.size = len(self.vertices)
        self.index= 0
    
    def is_leave(self):
        return self.children == []
    
    #eliminate
    def nb_vertices_node(self):
        if self.name == 'q':
            nb = len(list(set([v for section in self.vertices for v in section])))
        else:
            nb = len(self.vertices)
        return nb
    
    def print_node(self):
        print("Vertices: " + str(self.vertices) + "index: " + str(self.index))
    
    
class Tree:
    def __init__(self, nodes):
        self.nodes = nodes
        self.size = len(self.nodes)
        #esta funcion está mal, no fun
        self.nb_vertices= sum([v.nb_vertices_node() for v in self.nodes])
        #self.nb_vertices = len([[v] for n in self.nodes for v in n.vertices])
        
    def initialize_indices(self):
        bfs.create_indices(self)
        #for i in range(self.size):
         #   self.nodes[i].index= i 

    def is_root(self, r):
        for n in self.nodes: 
            if r in n.children:
                return False 
        return True 

    def get_root(self):
        for n in self.nodes:
            if self.is_root(n):
                return n
        else:
            return None
        #return filter(self.is_root(), self.nodes) 
    
    def get_parent(self, node):
        for n in self.nodes:
            if node in n.children:
                return n 
        return None 
    
    def get_brothers(self, node):
        p = self.get_parent(node)
        return [ c for c in p.children if c != node]

    def get_leaves(self):
        leaves= [] 
        for n in self.nodes:
            if n.is_leave():
                leaves.append(n)
        return leaves
    
    def print_tree(self):
        r = self.get_root()
        r.print_node()
        #queue = [] 
   
    def nb_vertices_subtree(self, node):
        if node.is_leave() :
            return node.nb_vertices_node() 
        else: 
            sum = node.nb_vertices_node()
            for c in node.children: 
                sum = sum + self.nb_vertices_subtree(c)
            return sum 
            #return node.nb_vertices_node() + sum(list(map(self.nb_vertices_node(), node.children)))
    def size_set_subtrees(self, list_s):
        return sum([self.nb_vertices_subtree(n) for n in list_s])
         
class State:
    def __init__(self, W, M, U, tree):
        self.W = W
        self.M=M
        self.U = U
        self.tree = tree 
   

ll = Tree_node([], [1], "l")
lr = Tree_node([], [2,3], "l")
lm = Tree_node([], [0], "l")
cl = Tree_node([ll,lr,lm], [5], "p")
cr = Tree_node([], [4], "l")
root = Tree_node([cl,cr], [6], "p")


test_tree= Tree([ root, cl, cr, ll, lr, lm])

l9= Tree_node([], [9], "l")
l10 = Tree_node([], [10], "l")
l5 = Tree_node([], [5], "l")
l11 = Tree_node([], [11], "l")
l12 = Tree_node([], [12], "l")
l2 = Tree_node([], [2], "l")
l4 = Tree_node([], [4], "l")
pe = Tree_node([l9,l10], [12], "p")
pe2 = Tree_node([l5,l11,l12], [6,7], "p")
q1 = Tree_node([pe, l2, pe2], [[1],[1,3],[3]], "q")
r = Tree_node([l4, pe, pe2], [8], "p")

he1 = Tree([pe2, l5, l11,l12, pe, l9, l10])
testp = Tree([r, l4, pe, pe2, l9, l10, l5,l11,l12])
testq = Tree([r, q1,pe2, pe, l4, l2, l12, l11, l5, l10, l9])


