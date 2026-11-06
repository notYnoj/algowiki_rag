Finally, let us now present Gerald Norris Shapiro’s network (taken from [4, Figure 51]) for sorting six elements in Figure 22:

Given the minimum number of links (12), Shapiro’s network has the minimum number of stages (5); however, in terms of worst case scenario and average number of swaps, the networks in Figure 20 and Figure 21 do better at the expense of just one more stage.

## 6.3 Sorting _N_=7

In this section, we describe three networks for _N_=7. We start with two networks for determining the _median_ of 7 elements. Figure 23 is a network for finding the median of 7 numbers, requiring a low average of only 3.481 exchanges.

The network in Figure 23 has 15 links. The network in Figure 24 finds the median with only 13 links, albeit increasing the average of exchanges to 4.49.

12
11
5.367
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

15
8
3.481
0.52
1
1-3
2
1-3
3
1-3
4
X
5
5-7
6
5-7
7
5-7

Figure 22: Shapiro’s network for sorting six elements, requiring 5 stages and 12 links.

Figure 23: A network to determine the median of 7 elements, with a low average of 3.481 exchanges.

