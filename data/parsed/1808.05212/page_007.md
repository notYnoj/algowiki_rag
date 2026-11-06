Full sorting in 25 links<sup>1</sup> adds the four CE elements (2,4)(3,4)(6,8)(6,7); Bare median finding in 19 links omits (1,2) and (8,9) from the 2-ops (1,2,3) and (7,8,9), respectively. Note that these omissions cannot be made directly on the original net without permutations to allow for median. The final networks are presented in Figure 9 below.

## 2.3 Comparison

We summarize the benefits of the new design versus the old design in  1:

<sup>1</sup>Note that 25 is also the minimum number required to sort a 9-network; see [4,  (11) on page 226 in Section 5.3.4].

21
14
7.657
0.35
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
18
9.443
0
19
13
6.99
0.48
1
X
1
1-4
2
X
2
1-4
3
X
3
3-4
4
X
4
2-4
5
X
5
X
6
6-8
7
X
7
6-7
8
X
8
6-9
9
X

19
13
6.99
0.48
1
1-4
2
X
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

Figure 8: A new network based on 3-ops, featuring 6 stages.

(a)

(b)

Figure 9: Two sorting networks derived from that in Figure 8. (a) corresponds to the fully sorted version by adding the links (23), (34), (68), (67). (b) corresponds to the bare median version by deleting the links (1,2) and (8,9) from the 2-ops (1,2,3) and (7,8,9) respectively.

