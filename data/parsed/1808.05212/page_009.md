final position. A single swap will place the remaining extrema; both extreme must be treated (a 2-op). With both extrema placed, median is properly placed by process of elimination".

Students of computer science will recognize Figure 1(a) as bubble-sort on three elements where the initial link leaves the maximum element in central position 2/3 of the time (for the remaining 1/3, it started in proper position and will not move), thereby encumbering subsequent links the task of floating it into its outer position. By comparison, the non-interfering method is seen as a selection or insertion sort whose improved swapping statistics are well-known. It is ironic such study of CE networks is rare and that the total number of links (or stages) has remained the sole performance metric for so long.

Conceptually, the longer prefacing element link in Figure 2(a) serves as a guard in assuring that no double-exchange occurs, allowing fusion into one 2-op. The final links might not be unit length, as seen in the improved sort/median on nine elements. The guard needs only protect (operate on) the outer two unshared elements. As a second and more interesting means of extension, we envision a 3-op of higher order, formed by allowing two adjacent 2-ops to execute concurrently. We explore the latter now.

## 4 Sorting _N_=4

A trial network (see Figure 11(a)) overlaps two optimal 3-sorts, sharing a central element, whose sorting statistics and testing reveal a maximum swap of four elements, occurring only with the center link (2,3) of the 3-op (1,2,3,4), which consists of 3 links without conflict: (1,2), (2,3), and (3,4) where (2,3) is either non-active or the _only_ active link. Unfortunately, this network fails to fully sort in five steps: 1/6 of the time, the central elements are transposed, requiring a sixth link as seen in Figure 11(b). This is both undesirable and surprising: the final link seemingly replicates the work concluded immediately its left. There are two remedies to this. Both rely on the fact that the central link in the 3-op might not execute, yet its operation is essential to attain a full sort.

Our first solution breaks the 3-op into its constituent links. Since they do not interfere, we are<tbc>

5
4
2.167
0.083
6
5
2.333
0
1
X
1
X
2
2-3
2
X
3
2-3
3
X
4
X
4
X
(a)
(b)

Figure 11: A sorting network for _N_=4 identifying min/max in (a) on the left, and fully sorting in (b) on the right.

