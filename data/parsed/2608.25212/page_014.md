_Proof._ We construct the promised data structure as follows. Let \(\ell=max(1,\lfloor logN\rfloor)\) and partition \[_N_\] into \(m=\lceil\frac{N}{\ell}\rceil\) blocks _B_<sub>1</sub>_,...,B<sub>m</sub>_ of length \(\ell\); the last block is shorter if needed. For an interval \(I\subseteq[N]\), define:

• \(\text{inter}(I)\subseteq[m]\) to be the (nonempty) interval of indices of blocks that intersect _I_;<tbc>

• \(\text{core}(I)\subseteq[m]\) to be the (possibly empty) interval of indices of blocks that are fully contained within _I_;<tbc>

• fringe(_I_) to be the collection (of size at most 2) of nonempty intervals \(I\cap B_i\) over all blocks \(i\in\text{inter}(I)\backslash\text{core}(I)\).

See Fig. 5 for an illustration. All of the above can be computed from _I_ in constant time. Also, whenever _I_ is a subinterval of _B<sub>i</sub>_, let \(\text{rel}_i(I)\subseteq[\ell]\) be the position of the interval _I_ relative to _B<sub>i</sub>_, i.e., the interval _I_ with both endpoints shifted by \(-(i-1)\ell\).

We instantiate three types of auxiliary data structures for Interval-Intersect.

outvertices uI
I3
u[2,5]
I2
u[1,2]
I1
1
2
3
4
5
6
7
8
Io
u[8,8]
Io
1
2
3
4
5
6
7
8
I1
I2
v[3,6]
v[4,7]
I3
a
a
invertices VI
Ia := [3,7] = [3,6] U [4,7]

fringe(I) = {IL, IR}
IL
IR
I
B1
B2
B3
B4
B5
B6
B7
B8
inter(I) = [2,7]
core(I) = [3,6]

Figure 4: The graph _H_ with _N_=8 and a single interval _I<sub>a</sub>_=\[3,7\]. There is a directed path from _u_<sub>\[2,5\]</sub> to _a_. Note that, on the contrary, one cannot reach _a_ from _u_<sub>\[1,2\]</sub> or from _u_<sub>\[8,8\]</sub>.

Figure 5: The objects inter(_I_), core(_I_), and fringe(_I_) for _m_=8 and some interval _I_.

