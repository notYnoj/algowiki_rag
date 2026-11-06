afforded any ordering of its components. We first choose to place the link to its right, giving rise to redundant right-most central links (not shown). We retain one only, giving the familiar solution Figure 12(a), sans N-ops. The second solution, depicted in Figure 12(b), recognizes that the additional link is necessary in the case the 3-op is fully active (i.e., two outer swaps), its actions then juxtaposing two (as yet unordered) elements against each other into adjacent central position. As before, we guard against interference by employing a prefacing link whose two endpoints are the outer endpoints (elements) of the two links it protects.

The second solution (in Figure 12(b)) is in fact the O(_n_<sup>2</sup>) pair-wise comparison of all elements, taken in descending order, which necessarily ranks all elements. While not a viable solution for large _N_, for _N_=4 it sits close to the theoretical minimum (5 links, see Figure 13 below) and rewards the implementor with surprisingly good statistics for average swaps (2) while nonetheless executing in at most three hardware stages.

Large networks whose size _N_ is a power of two, have many prefacing links whose sorting statistics show a 50/50 probability of exchange. The transposition operator may be applied to any such link (and to any implicated links lying to its left) without changes to the average sorting statistics. The topological change may instead succeed in reducing the maximum number of exchanges. Applied to the network seen in Figure 12(a), we obtain the network depicted in Figure 13 below, where the maximum number of exchanges dropped from 5 to 4.

5
5
2.333
0
6
4
2
0
1
X
1
X
2
X
2
X
3
X
3
X
4
X
4
X
(a)
(b)

5
4
2.333
0
1
X
2
X
3
X
4
X

Figure 12: (a): Swap frequencies are <sup>1</sup>/2 at links 1,2,3,4; <sup>1</sup>/3 at link 5. (b): Swap frequencies are <sup>1</sup>/2 at link 1; <sup>1</sup>/3 at links 2 and 3; <sup>1</sup>/4, <sup>1</sup>/2, <sup>1</sup>/4 at (1,2), (2,3), (3,4) from the 3-op (1,2,3,4), respectively.

Figure 13: A 5-link sorting network for 4 elements. The last link has swap probability of <sup>1</sup>/3; all other links have swap probability of <sup>1</sup>/2.

