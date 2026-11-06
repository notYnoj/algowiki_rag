elements concurrently.

If the goal is to reduce average swaps in reduced links, the network in Figure 19 will do that, at the expense of additional stages:

Applying basic techniques (symmetric min/max, applied successively) leads to the network depicted in Figure 20 which sorts six elements in just 12 links – the minimum:

The user may achieve the smallest total number of swaps (8 compared to 9) at the cost of a slightly increased average number of swaps. (This trade-off with mild change in topology symmetry is seen with large networks in general.)

13
8
4.233
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

12
9
4.567
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

12
8
4.7
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

Figure 19: A network to sort 6 elements with minimum average-swap performance.

Figure 20: A network to sort 6 elements with the minimum number (12) of links.

Figure 21: Another network to sort 6 elements with the minimum number (12) of links but reduced worst- case scenario at the cost of slightly worse average swap performance.

