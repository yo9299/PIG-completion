#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:12:45 2024

@author: vardevol
"""
import pnodes as p
import trees 
import bfs 

def main(tree):
    state = p.create_initial_state(tree)
    i=0
    while i < len(bfs.bfs(tree)):
        n = bfs.bfs(tree)[i]
        if n.is_leave():
            state = p.update_leaves(state, n)
            #state = p.update_U(state, n)
            #print(state.M)
            
        elif n.name == 'p': 
            n.print_node()
            state= p.update_M(state, n)
            print("M")
            print(state.M)
            state= p.update_U(state, n)
            print("U")
            print(state.U)
        #elif n.name == 'q':
            
        i +=1 
    return state

s= main(trees.test_tree)
            
            
