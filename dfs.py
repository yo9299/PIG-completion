#this module contains the functions necessary to find the order in which we process the nodes of a mpq-tree in the dynamic prog algo

def exploreNum(graphe, i, pref, suff, p, s):
    pref[i] = p
    p = p+1
    for j in i.children:
        if pref[j]==-1:
            pref, suff, p, s = exploreNum(graphe, j, pref, suff, p, s)
    suff[i] = s
    s = s+1
    return pref, suff, p, s
    
#returns suffix order of nodes of a given tree after DFS exploration    
def dfs(tree):
    nodes = tree.get_descendants()
    pref = dict.fromkeys(nodes)  #tree.nodes)
    suf = dict.fromkeys(nodes)
    for i in nodes:
        pref[i] = -1
        suf[i] = -1
    p = 0
    s = 0
    for i in nodes:
        if pref[i] ==-1:
            pref, suf, p, s = exploreNum(tree, i, pref, suf, p, s)
    suf[tree] = s
    return suf 


def create_indices(tree):
    sol =dfs(tree)
    tree.put_index(sol[tree])
    for node in tree.get_descendants():
        node.put_index(sol[node]) #
        #node.index = sol[node]

