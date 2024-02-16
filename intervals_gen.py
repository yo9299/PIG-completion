#!/usr/bin/env python3
import trees
import itertools
import functools
import math
from operator import mul

class Interval:
    def __init__(self, depth: int, index: int, start: int, end: int):
        self.depth = depth
        self.index = index
        self.start = start
        self.end = end


def count_permutations(node: trees.Tree_node):
    sub_permutations = functools.reduce(mul, [count_permutations(n) for n in node.children], 1)
    match node.name:
        case 'p':
            # Account for all the possible subtrees permutations
            return sub_permutations * math.factorial(len(node.children))
        case 'q':
            # Account for both the forward and flipped representation
            return  sub_permutations * 2
        case 'l':
            return sub_permutations

    print("Unknown node type", node.name)
    assert False

def gen_factorial_mapping(size, perm_index):
    vals = list(range(size))

    perm_vals = []

    while len(vals) > 0:
        index = perm_index % len(vals)
        perm_index //= len(vals)
        perm_vals.append(vals[index])
        vals.pop(index)
    return perm_vals

def rec_gen_intervals(node: trees.Tree_node, perm_index: int = 0) -> list[Interval]:
    match node.name:
        case 'p':
            subtrees: list[list[Interval]] = []


            # Choose the desired permutation
            perm_cardinality = math.factorial(len(node.children))
            p_node_permutation = perm_index % perm_cardinality

            perm_children = [node.children[i] for i in gen_factorial_mapping(len(node.children), p_node_permutation)]

            # Remove the possible choices from the perm_index
            perm_index //= perm_cardinality

            for c in perm_children:

                # Handle subtree permutation
                subtree_perm_cardinality = count_permutations(c)
                subtree_perm = perm_index % subtree_perm_cardinality
                perm_index //= subtree_perm_cardinality

                subtrees.append(rec_gen_intervals(c, subtree_perm))

            intervals: list[Interval] = []

            # Adjust intervals positions
            y_offset = 0
            max_y = y_offset
            for subtree in subtrees:
                for subinterval in subtree:
                    subinterval.start += y_offset
                    subinterval.end += y_offset
                    subinterval.depth += len(node.vertices)
                    max_y = max(max_y, subinterval.end)
                    intervals.append(subinterval)

                y_offset = max_y + 0.5

            # Add p managed intervals covering all the subtrees intervals
            for d, v in enumerate(node.vertices):
                intervals.append(Interval(d, v, 0, max_y))

            return intervals

        case 'q':
            managed_depth = 0
            intervals = []
            y_offset = 0
            open_intervals = {}

            managed_count = len(set(itertools.chain(*node.vertices)))

            # Choose between forward and reverse q node representation
            iterator = zip(node.children, node.vertices) if perm_index % 2 == 0 else reversed(list(zip(node.children, node.vertices)))
            perm_index //= 2

            for (c, v) in iterator:
                def process_open_interval(interval: tuple[int, int]):
                    (open_int, open_pos) = interval
                    if not open_int in v:
                        intervals.append(Interval(process_open_interval.managed_depth, open_int, open_pos, y_offset))
                        process_open_interval.managed_depth += 1
                        return False
                    return True
                process_open_interval.managed_depth = managed_depth

                # Close intervals that do not appear in the clique anymore
                open_intervals = dict(filter(process_open_interval, open_intervals.items()))

                managed_depth = process_open_interval.managed_depth


                # Spacing of subtrees
                y_offset += 0.5

                # Add new intervals
                for nv in v:
                    if nv not in open_intervals.keys():
                        open_intervals[nv] = y_offset

                max_y = y_offset

                # Handle subinterval permutation
                subinterval_perm_cardinality = count_permutations(c)
                subinterval_perm = perm_index % subinterval_perm_cardinality
                perm_index //= subinterval_perm_cardinality

                subintervals = rec_gen_intervals(c, subinterval_perm)
                for subinterval in subintervals:
                    subinterval.start += y_offset
                    subinterval.end += y_offset
                    subinterval.depth += managed_count
                    max_y = max(max_y, subinterval.end)
                    intervals.append(subinterval)
                y_offset = max_y

            # Close all remaining open intervals
            for (open_int, open_pos) in open_intervals.items():
                intervals.append(Interval(managed_depth, open_int, open_pos, y_offset))
                managed_depth += 1

            return intervals
        case 'l':
            assert perm_index == 0
            # Return an unitary interval
            return [Interval(i, v, 0, 1) for (i, v) in enumerate(node.vertices)]

    print("Unknown node type", node.name)
    assert False