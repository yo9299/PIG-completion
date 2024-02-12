#import trees 

def expand_node(node):
    return node.children 

def bfs(tree):
    r = tree.get_root()
    sol= [r] + expand_node(r)
    to_be_expanded = [n for n in expand_node(r) if not n.is_leave()]
    #print([n.print_node() for n in to_be_expanded])
    while to_be_expanded != []:
        e= to_be_expanded.pop()
        #print(e.print_node())
        sol = sol + expand_node(e)
        to_be_expanded = to_be_expanded + [n for n in expand_node(e) if not n.is_leave()]
        #print([n.print_node() for n in to_be_expanded])

    sol.reverse()
    return sol

def create_indices(tree):
    sol =bfs(tree)
    for node in tree.nodes:
        node.index = sol.index(node)

