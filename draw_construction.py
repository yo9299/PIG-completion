#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 17:22:16 2024

@author: vardevol
"""
import matplotlib.pyplot as plt

n=3
m=2
L=2*n
rulers=[]
edges = [(0,2), (1,2)]

for r in range(2):
    for v in range(n):
        for b in range(4):
            for j in range(m):
                rulers.append( ([r+2*(v+2*n*(b+m*j)), r+2*(v+2*n*(b+m*j)) + L ], v))
                
lorries = [] 

for v in range(n):
    for b in range(4):
        for j in range(m+1):
            lorries.append(([1+2*(v+2*n*(b+m*j)), 2*(v+2*n*(b+m*j))+L-1], v))
            
walls=[]

for v in range(n):
    walls.append([0, 2*v])
    walls.append([8*m*n+L-2*(n-v-1), 8*m*n+L])
    
cars=[]

for e in edges:
    g = 2 
    stage = 4*(edges.index(e)) + g 
    if e[0] < e[1]:
        gu = 2 
        stageu = stage 
    elif e[0] > e [1]:
        gu = 1 
        stageu = stage-1 
    cars.append([stageu*L +3*e[0], stageu*L +3*e[0]])
    cars.append([stage*L + 3*e[1], stage*L + 3*e[1]])


def draw_intervals(intervals, wall, lorry, car):
    fig, ax = plt.subplots()
    for i, (interval, vertex) in enumerate(intervals):
        ax.plot([interval[0], interval[1]], [i, i], color='blue')
        label_x = (interval[0] + interval[1]) / 2  # Calculate x-coordinate for label
        label_y = i + 0.1  # Adjust y-coordinate for label position
        ax.text(label_x, label_y, f'{"v"}{vertex}', ha='center', va='bottom', fontsize=8)  # Add text label
    for i, interval in enumerate(wall):
        ax.plot([interval[0], interval[1]], [i+0.5, i+0.5], color='green')
    
    for i, (interval,vertex) in enumerate(lorry):
        ax.plot([interval[0], interval[1]], [i+0.75, i+0.75], color='red')
        label_x = (interval[0] + interval[1]) / 2  # Calculate x-coordinate for label
        label_y = i + 0.1  # Adjust y-coordinate for label position
        ax.text(label_x, label_y, f'{"v"}{vertex}', ha='center', va='bottom', fontsize=8, color = 'red')  # Add text label
    
    for i, interval in enumerate(car):
        ax.plot([interval[0], interval[1]], [i-0.5, i+0.5], color='black')
    
    ax.set_yticks(vertex)
    #ax.set_yticklabels([f'Interval {i}' for i in range(len(intervals))])
    #ax.set_xlabel('Value')
    #ax.set_ylabel('Interval')
    ax.set_title('Construction')
    #plt.grid(True)
    plt.show()


draw_intervals(rulers, walls, lorries, cars)
