While not strictly a NICE network, a compact software implementation for _N_=5 is a good project for future work.

## 6.2 Sorting _N_=6

For _N_=6, three-sort the elements (1,3,5) and symmetrically on (2,4,6), after sorting (1,5) and (2,6). Note that in each case a central 2-op occurs on element 3 (4). We now center these two elements by again using a 2-op, but this time against the outer interval formed by the opposing 3-sort; that is, the 2-ops (1,4,5) and (2,3,6). These leads to a highly parallel execution model in which the central two elements are located at (3,4) albeit unordered. By the ranking nature of CE networks, elements (1,2) and (5,6) are also properly partitioned, albeit unsorted. Three concurrent links at (1,2), (3,4) and (5,6) thereby conclude the sort (see Figure 17):

A rework of the network from Figure 17 presented in Figure 18 preserves the overall exchange statistics while lowering the worst-case performance to 8 swaps.

Note that both networks complete in only four stages with the two central stages involving all<tbc>

13
9
4.633
0
1
X
2
X
3
X
4
X
5
X
6
X

13
8
4.633
0
1
X
2
X
3
X
4
X
5
X
6
X

Figure 17: A network to sort 6 elements.

Figure 18: A rework of the network from Figure 17 to sort 6 elements with improved worst-case performance.

