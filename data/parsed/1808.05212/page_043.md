whose sorting statistics and testing reveal a maximum swap of four elements, occurring only with the central 3-op not active, as desired. Unfortunately, this network fails to fully sort in five steps: 1/3 of the time the central elements are transposed, requiring a resort to the six link for seen in (f). This is both undesirable and surprising: the final link seemingly replicates the work concluded immediately its left. There are two remedies to this. Both rely on the fact that the central link in the 3-op might not execute, yet its operation is essential to attain a full sort.

Our first solution breaks the 3-op into its constituent links. Since they do not interfere, we are afforded any ordering of its components. We first choose to place the link to its right, giving rise to redundant right-most central links (not shown). We retain one only, giving the familiar solution (g), sans N-ops.

The second (h) recognizes that the additional link is necessary in the case the 3-op is fully active (two swaps, outer), its actions then juxtaposing two (as yet unordered) elements against each other into adjacent central position. As before we guard against interference by employing a prefacing link whose two endpoints are the outer endpoints (elements) of the two links it protects:

The second solution is in fact the O(n^2) pair-wise comparison of all elements, taken in descending order, which necessarily ranks all elements. While not a viable solution for large N, for N=4 it sits close to the theoretical minimum (5 links) and rewards the implementor with surprisingly good statistics for average swaps (2) while nonetheless executing in at most three hardware stages.

Large networks whose size N is a power of two, have many prefacing links whose sorting statistics show a 50/50 probability of exchange. The transposition operator may be applied to any such link (and to any implicated links lying to its left) without changes to the average sorting statistics. The topological change may instead succeed in reducing the maximum number of exchanges.

Applied to the third or fourth link (but not both) seen in stage (g) II yields

