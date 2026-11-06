Partition _A_ into _slabs_ of _B_ consecutive columns. A row is called _local_ if it has a non-zero intersection with exactly one slab and _global_ otherwise. The 1s in local/global rows are themselves local/global. Let _n<sub>i</sub>_ be the number of rows local to slab _i_ and _n_<sup>∗</sup> be the number of global rows, so \(n=n^*+\sum_in_i\).

Suppose _A(r,c_)=1 is a 1 appearing in a global row _r_ and slab _s_=\[_c/B_\]. We classify this 1 as _first_ if the intersection of row _r_ and slabs 1_,...,s_-1 are zero, _last_ if the intersection of row _r_ and slabs _s_+1_,...,_\[_m/B_\] is zero, and _middle_ otherwise.

Since each slab is itself _Q<sub>a,b</sub>_-free, the total number of local 1s is at most

\(\sum_{i=1}^{\lceil m/B\rceil}\mathrm{Ex}(Q_{a,b},n_i,m_i),\) (2)

where _m<sub>i</sub>_ is the number of columns in slab _i_, which is exactly _B_ except perhaps the last slab. Similarly, if _A_<sub>first</sub> and _A_<sub>last</sub> are the matrices of first 1s and last 1s, then each slab of _A_<sub>first</sub> is _Q_<sub>_a,b_+1</sub> free, and each slab of _A_<sub>last</sub> is _Q_<sub>_a_+1_,b_</sub>-free; see Figure 2. Letting \(n_i^f(n_i^l)\) be the number of rows with first (last) 1s in slab _i_, we can upper bound first and last 1s as follows.

\(\|A_\mathrm{first}\|_1+\|A_\mathrm{last}\|_1\le\sum_{i=1}^{\lceil m/B\rceil}\big(\mathrm{Ex}(Q_{a,b+1},n_i^f,m_i)+\mathrm{Ex}(Q_{a+1,b},n_i^l,m_i)\big)\)<br>
\(\le\mathrm{Ex}(Q_{a,b+1},n^*,m-m_{\lceil m/B\rceil})+\mathrm{Ex}(Q_{a+1,b},n^*,m-m_1).\) (3)

In Eqn. (3) we use the _superadditivity_ of Ex to simplify the expression. For any _R_, \(\mathrm{Ex}(R,n_1,m_1)+\mathrm{Ex}(R,n_2,m_2)\le\mathrm{Ex}(R,n_1+n_2,m_1+m_2)\). Note that \(\sum_in_i^f=\sum_in_i^l=n^*\) and that the first and last slabs contain no last 1s and first 1s, respectively.

Let _A_<sup>∗</sup> be the \(n^*\times m\) matrix formed by the global rows and containing only the middle 1s. We partition the rows of _A_<sup>∗</sup> into horizontal slabs of _G_ rows each, so the intersections of the horizontal and vertical slabs induce \(G\times B\) _blocks_. Call a \(G\times B\) block in _A_<sup>∗</sup> _heavy_ if it contains a (\(\unknown\)), and _light_ otherwise. The middle 1s inside heavy/light blocks are themselves called heavy/light. Let _A_<sub>heavy</sub> and _A_<sub>light</sub> be the \(n^*\times m\) matrices containing heavy and light 1s, respectively. In a light block, the first 1 and last 1 of each row are called _light-first_ and _light-last_, and all other 1s in the row are _light-middle_.

All 1s
Local
Global
First
Middle
Last
Light
Heavy
Light-first
Light-middle
Light-last

