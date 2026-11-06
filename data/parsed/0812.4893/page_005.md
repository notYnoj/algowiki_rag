## 2.2 Almost Stable vs. Stable

While an almost stable matching is robust to change in the preferences, this is not the case for a stable matching. For example, consider the following graph where the numbered edge ends indicate preference rankings (the most preferred match has rank 1).

Now transpose the preferences shown in boldface to obtain a graph whose unique stable matching is edge-disjoint from the unique stable matching in the original graph.

Thus, a single transposition in preferences can force every match to break up.

From the perspective of distributed computation, this example shows that every node must have essentially complete information about the network to arrive at a stable matching. In particular, if each node initially knows only its neighbours and its own preferences, the number of communication steps required between neighbours is linear in the diameter of the network.

Gathering global information is hardly practical in a very large-scale distributed system, especially if the network undergoes frequent changes. The ease with which almost stable matchings can be computed in a distributed setting comes as a positive surprise.

## 2.3 Definition of Almost Stable

Our results are somewhat oblivious to the exact definition of an "almost stable" matching. The number of unstable edges (blocking pairs) appears to be generally accepted as a basic measure of instability [1,3,5,19], but one could equally well consider other measures. For example, one can consider the number of nodes that are endpoints of unstable edges.

Naturally we must measure stability in relation to some other quantity; an absolute guarantee of stability cannot be achieved in constant time. We have chosen to measure the number of unstable edges relative to |_M_|, as this gives us the strongest results when compared with other quantities such as |_R_|, |_B_|, \(|R\cup B|\), |_E_|, and |_R_||_B_|, each of which is at least as large as |_M_|. Eriksson and Häggström [5] provide arguments in favour of comparing unstable edges to |_E_|.

1
1
2
1
2
1
2
1
2
1
1
2
1
2
1
2
1
2
1
2
1
2
1
2
1
2

1
1
2
1
2
1
2
1
2
1
2
1
2
1
1
2
1
2
1
2
1
2

