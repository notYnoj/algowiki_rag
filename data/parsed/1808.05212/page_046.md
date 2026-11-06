Note that the final sort is style (g), not (i). While not strictly a NICE network, a compact software implementation for N=5 appears under "Further Work".

Sorting N=6

For N=6 three-sort the elements (1,3,5) and symmetrically on (2,4,6). Note that in each case a central 2-op occurs on element 3 (4). We now center these two elements by again using a 2-op, but this time against the outer interval formed by the opposing 3-sort. That is, the 2-ops (1,4,5) and (2,3,6). These leads to a highly parallel execution model in which the central two elements are located at (3,4) albeit unordered. By the ranking nature of CE networks, elements (1,2) and (5,6) are also properly partitioned, albeit unsorted. Three concurrent links at (1,2) (3,4) and (5,6) thereby conclude the sort:

13 9 4.633 (1)k) first 2: .5, last 3: .2, else .33 I II III IV

A rework on the right preservers overall exchange statistics while lowering the worst-case performance to 8 swaps. Note that both networks complete in only four stages with central stages II and III involving all elements concurrently.

If the goal is to minimize average swaps in reduced links, these suffice, at

13 8 4.233 (m)

