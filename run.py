# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)

print search.breadth_first_graph_search(ab).path()
print search.depth_first_graph_search(ab).path()
print search.ramification_limitated_graph_search(ab).path()
print search.ramification_limitation_subest_search(ab).path()

# print search.iterative_deepening_search(ab).path()
# print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
