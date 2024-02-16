#!/usr/bin/env python3

import trees
from intervals_gen import count_permutations, rec_gen_intervals, Interval
from draw_pqtree_intervals import print_tree

def solve_for_intervals(intervals: list[Interval]) -> tuple[int, list[bool]]:
    cost = 0
    solution = []
    for interval in intervals:
        left_cost = 0
        right_cost = 0
        for other in intervals:
            if other.end < interval.start:
                left_cost += 1
            elif other.start > interval.end:
                right_cost += 1
        if left_cost <= right_cost:
            cost += left_cost
            solution.append("left")
        else:
            cost += right_cost
            solution.append("right")
    return cost, solution


def main(tree: trees.Tree):
    root = tree.get_root()

    best_repr = None

    perm_count = count_permutations(root)
    # Generate all the possible permutations of the tree
    for perm in range(perm_count):
        intervals = rec_gen_intervals(root, perm)
        # Solve and choose the best solution with its interval representation
        cost, mapping = solve_for_intervals(intervals)
        if best_repr is None or cost < best_repr[0]:
            best_repr = (cost, perm, intervals, mapping)
    return best_repr


if __name__ == "__main__":
    tree = trees.testp
    cost, perm, _, mapping = main(tree)
    print("Cost", cost)

    draw_intervals = True

    if draw_intervals:
        print_tree(tree, perm, mapping)

