#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 17:22:16 2024

@author: vardevol
"""
import matplotlib.pyplot as plt

n=3 # Number of vertices
m=8 # Number of directed edges
# r in {0, 1} => Extra shift?
# b in {0, 1, 2, 3} =>

L=2*n
rulers=[]
edges = [(0,2), (1,2)]

# For each stage
for j in range(m):
    for g in range(4):
        # Stage description
        for v in range(n):
            for r in range(2):
                rulers.append((r+2*v, [r+2*(v+n*(g+4*j)), r+2*(v+n*(g+4*j)) + L ], f"")) # f"r{r}v{v}g{g}j{j}"))

lorries = []

for v in range(n):
    for j in range(m):
        for g in range(4):
            lorries.append((v, [1+2*(v+n*(g+4*j)), 2*(v+n*(g+4*j))+L-1], v))

walls=[]

for v in range(n):
    walls.append((v, [2*v - L, 2*v]))

    start = 2*v + 8 * n * m
    walls.append((v, [start, start + L]))

cars=[]

for e in edges:
    g = 2
    stage = 4*(edges.index(e)) + g
    if e[0] < e[1]:
        gu = 2
        stageu = stage
    elif e[0] > e[1]:
        gu = 1
        stageu = stage-1
    cars.append([stageu*L +3*e[0], stageu*L +3*e[0]])
    cars.append([stage*L + 3*e[1], stage*L + 3*e[1]])


def draw_intervals(rulers, wall, lorry, car):
    fig, ax = plt.subplots()

    y_pos = 0

    rulers.sort(key=lambda x: x[0])
    wall.sort(key=lambda x: x[0])
    lorry.sort(key=lambda x: x[0])

    for i, (pos, interval, vertex) in enumerate(rulers):
        if i > 0 and rulers[i - 1][0] != pos:
            y_pos += 1
        ax.plot([interval[0], interval[1]], [y_pos, y_pos], color='blue')
        label_x = (interval[0] + interval[1]) / 2  # Calculate x-coordinate for label
        label_y = y_pos + 0.1  # Adjust y-coordinate for label position
        ax.text(label_x, label_y, f'{vertex}', ha='center', va='bottom', fontsize=8)  # Add text label

    y_pos += 1
    walls_idx = 0
    for i, (pos, interval,vertex) in enumerate(lorry):

        if i > 0 and lorry[i - 1][0] != pos:
            y_pos += 1


        # Draw walls
        while walls_idx < len(walls) and walls[walls_idx][0] == pos:
            wall_interval = walls[walls_idx][1]
            ax.plot([wall_interval[0], wall_interval[1]], [y_pos, y_pos], color='green')
            walls_idx += 1


        ax.plot([interval[0], interval[1]], [y_pos, y_pos], color='red')
        label_x = (interval[0] + interval[1]) / 2  # Calculate x-coordinate for label
        label_y = y_pos + 0.1  # Adjust y-coordinate for label position
        ax.text(label_x, label_y, f'{vertex}', ha='center', va='bottom', fontsize=8, color = 'red')  # Add text label

    for i, interval in enumerate(car):
        ax.plot([interval[0], interval[1]], [y_pos-0.5, y_pos+0.5], color='black')
        y_pos += 1

    # ax.set_yticks(vertex)
    #ax.set_yticklabels([f'Interval {i}' for i in range(len(intervals))])
    #ax.set_xlabel('Value')
    #ax.set_ylabel('Interval')
    ax.set_title('Construction')
    plt.grid(True)
    plt.show()


draw_intervals(rulers, walls, lorries, cars)
