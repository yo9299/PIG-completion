#!/usr/bin/env python3

import matplotlib.pyplot as plt
import trees
from intervals_gen import *


def print_tree(tree: trees.Tree, permutation_index: int = 0, mappings: list[bool] = None):
    root = tree.get_root()
    fig, ax = plt.subplots()
    intervals = rec_gen_intervals(root, permutation_index)
    for idx, interval in enumerate(intervals):
        if mappings is None:
            color = 'black'
            cost = None
        elif mappings[idx] == 'left':
            color = 'green'
            cost = len(list(filter(lambda i: i.end < interval.start, intervals)))
        else:
            color = 'red'
            cost = len(list(filter(lambda i: i.start > interval.end, intervals)))

        ax.plot([interval.start, interval.end], [-interval.depth, -interval.depth], color=color)

        label = f"{interval.index} cost: {cost}" if cost is not None else f"{interval.index}"

        ax.text(interval.start - 0.1, -interval.depth + 0.05, label)


    ax.set_title('Intervals')
    # plt.grid(True)
    plt.show()


if __name__ == "__main__":
    tree = trees.test_tree
    print_tree(tree)