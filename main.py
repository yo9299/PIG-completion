#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:12:45 2024

@author: vardevol
"""
import pnodes as p
import qnodes as q 
import trees 
import bfs 

def main(tree):
    state = p.create_initial_state(tree)
    i=0
    queue= sorted(bfs.dfs(tree).items(), key=lambda x:x[1])
    queue= [x[0] for x in queue]
    while i < len(queue):
        n = queue[i]
        if n.is_leave():
            n.print_node()
            state = p.update_leaves(state, n)
            #state = p.update_U(state, n)
            print(state.U)
            
        elif n.name == 'p': 
            n.print_node()
            state= p.update_M(state, n)
            print("M")
            print(state.M)
            state= p.update_U(state, n)
            print("U")
            print(state.U)
        elif n.name == 'q':
            #break
            state = q.computeqU(state, tree, n)
            
        i +=1 
    return state

s= main(trees.testp)
            
            
