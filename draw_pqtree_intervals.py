#!/usr/bin/env python3

import matplotlib.pyplot as plt
import trees
from intervals_gen import *


def print_tree(tree: trees.Tree, permutation_index: int = 0, mappings: list[bool] = None):
    root = tree.get_root()
    fig, ax = plt.subplots()
    for idx, interval in enumerate(rec_gen_intervals(root, permutation_index)):
        ax.text(interval.start - 0.1, -interval.depth + 0.05, str(interval.index))

        if mappings is None:
            color = 'black'
        elif mappings[idx] == 'left':
            color = 'green'
        else:
            color = 'red'

        ax.plot([interval.start, interval.end], [-interval.depth, -interval.depth], color=color)

    ax.set_title('Intervals')
    # plt.grid(True)
    plt.show()


if __name__ == "__main__":
    tree = trees.test_tree
    print_tree(tree)