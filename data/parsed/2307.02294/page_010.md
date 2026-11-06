2. \(\ell_j>\ell_{j-1}\) is the first index such that some column in blocks \((\ell_{j-1},i),\dots,(\ell_j,i)\) contains two light-middle 1s.

Call the interval of blocks \((\ell_{j-1},i),\dots,(\ell_j-1,i)\) in _A_<sub>light</sub> (i.e., excluding \((\ell_j,i)\)) a _chunk_. By construction, the intersection of a column and a chunk can contain at most one light-middle 1. (Note that no light block contains two light-middle 1s in the same column, for otherwise it would contain a \((\bullet)\) pattern and be classified as heavy.) We claim _A_<sub>lightmid</sub> is \(P\otimes\genfrac(){pt}{2}{\bullet}{\bullet}\)-free, and therefore the number of light-middle 1s in _A_<sub>light</sub> is, by superadditivity, at most

\(B\cdot\|A_\mathrm{lightmid}\|_1\le B\cdot\mathrm{Ex}(P\otimes\genfrac(){pt}{2}{\bullet}{\bullet},n^*/G,m/B)\le\mathrm{Ex}(P\otimes\genfrac(){pt}{2}{\bullet}{\bullet},Bn^*/G,m).\) (6)

Consider an occurrence of \(\genfrac(){pt}{2}{\bullet}{\bullet}\) in _A_<sub>lightmid</sub>, say \(A_\mathrm{lightmid}(\ell_j,i)=A_\mathrm{lightmid}(\ell_{j^\prime},i)=1\). By construction they lie in different chunks, thus there must be a column in slab _i_ of _A_<sub>light</sub> that contains two light- middle 1s in blocks \((\ell_j,i),\dots,(\ell_{j^\prime},i)\) inclusive. Together with a light-first and light-last 1, this forms a \((\bullet)\) pattern. Thus, any occurrence of \(P\otimes\genfrac(){pt}{2}{\bullet}{\bullet}\) in _A_<sub>lightmid</sub> implies an occurrence of \(Q=P\otimes(\bullet)\) in _A_<sub>light</sub>, contradicting the fact that _A_<sub>light</sub> is _Q<sub>a,b</sub>_-free.

Combining Eqns. (2,3,4,5,6), we arrive at a recursive upper bound on Ex(_Q<sub>a,b</sub>,n,m_).

\(\mathrm{Ex}(Q_{a,b},n,m)\le\sum_{i=1}^{[m/B]}\mathrm{Ex}(Q_{a,b},n_i,m_i)\text{local 1s}\)<br>
\(+\mathrm{Ex}(Q_{a,b+1},n^*,m-m_{[m/B]})+\mathrm{Ex}(Q_{a+1,b},n^*,m-m_1)\text{first and last 1s}\)<br>
\(+\mathrm{Ex}(P,n^*/G,m/B)\cdot\mathrm{Ex}(Q_{a+1,b+1},G,B)\text{heavy middle 1s}\)<br>
\(+2\mathrm{Ex}(Q_{a,b},n^*,m/B)\text{light-first/-last 1s}\)<br>
\(+\mathrm{Ex}(P\otimes\genfrac(){pt}{2}{\bullet}{\bullet},Bn^*/G,m).\text{light-middle 1s}\) (7)

## 3.2 Analysis of The Recurrence

**Lemma 3.2.** _Let t_=3_k_-(_a+b_) _be the number of 1s in Q<sub>a,b</sub>. If t_=3 _then_ \(\mathrm{Ex}(Q_{a,b},n,m)\le 2n+(2k-1)(m-2)\) _and if t_=2 _then_ \(\mathrm{Ex}(Q_{a,b},n,m)\le n+(2k-1)(m-1)\).

