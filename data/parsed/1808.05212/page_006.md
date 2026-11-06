Using 21 links, we find minimum, maximum and median (see Figure 5 or Figure 6 above.) This design leads to efficient bare median (19 links) and full sorting (25 links) on nine-element arrays; see Figure 7 below.

Exchanges on 21 links occur when presented reverse sorted input, and (see Figure 5) 9<sup>27</sup>/<sub>35</sub>≈9.771 times on average which gives a relative frequency of (9<sup>27</sup>/<sub>35</sub>)/21=114/<sub>245</sub>≈47%.

## 2.2 New design using 3-ops

Substitution of s3 by its reworked 3-op version gives the network in Figure 8 below.

21
21
9.771 0.35
1
X
2
2-4
3
3-4
4
2-4
5
X
6
6-8
7
6-7
8
6-8
9
X

25
25
11.56
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
7
X
8
X
9
X

19
19
9.105 0.48
1
1-4
2
1-4
3
3-4
4
2-4
5
X
6
6-8
7
6-7
8
6-9
9
6-9

Figure 6: The 21-link network to determine the median from Figure 5 re-arranged. Note that there are 9 stages (stage 1: links (1,4)(2,5)(3,6); stage 2: links (4,7)(5,8)(6,9); stage 3: links (1,4)(2,5)(3,6); stage 4: links (1,2)(4,5)(7,9); stage 5: links (2,3)(5,6)(8,9); stage 6: links (1,2)(4,5)(7,9); stage 7: link (3,5); stage 8: link (5,7); stage 9: link (3,5)) that can be executed in parallel.

(a)

(b)

Figure 7: Two sorting networks derived from that in Figure 6. (a) corresponds to the fully sorted version by adding the links (23),(34),(68),(67) at the end. (b) corresponds to the bare median version by deleting the first (1,2) link and the last (7,8) link.

