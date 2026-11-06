Define \(A_\mathrm{heavy}^\mathrm{c}\) to be the \(n^*/G\times m/B\) matrix obtained by _contracting_ each block in _A_<sub>heavy</sub> to a single entry, i.e., non-zero blocks become 1 and all-zero blocks become 0. Because each heavy block contains a (**.**), \(A_\mathrm{heavy}^\mathrm{c}\) is _P_-free, implying \(\|A_\mathrm{heavy}^\mathrm{c}\|_1\) (the number of heavy blocks) is at most Ex(_P,n_<sup>∗</sup>_/G,m/B_). Since each heavy block consists solely of middle 1s, each is _Q_<sub>_a_+1_,b_+1</sub>-free; see Figure 3. Thus,

\(\|A_\mathrm{heavy}\|_1\le\mathrm{Ex}(P,n^*/G,m/B)\cdot\mathrm{Ex}(Q_{a+1,b+1},G,B).\) (4)

Let \(A_\mathrm{light}^\mathrm{c}\) be obtained by contracting the _B_ columns in each slab of _A_<sub>light</sub> to a single column. \(A_\mathrm{light}^\mathrm{c}\) inherits the _Q<sub>a,b</sub>_-freeness of _A_<sub>light</sub> and _A_, so the contribution of light 1s in the light-first and light-last categories is at most

\(2\|A_\mathrm{light}^\mathrm{c}\|_1\le 2\mathrm{Ex}(Q_{a,b},n^*,m/B).\) (5)

What remains is to bound the light 1s in the light-middle category. Construct an \(n^*/G\times m/B\) matrix _A_<sub>lightmid</sub> by the following procedure, which is similar to that of \[Gen09\]. Assume the rows of _A_<sub>lightmid</sub> are numbered from bottom to top. For each _i_ independently, scan the blocks in slab _i_ that contain light-middle 1s from bottom to top, setting \(A_\mathrm{lightmid}(\ell_0,i)=A_\mathrm{lightmid}(\ell_1,i)=\cdots=1\) according to the following rules. See Figure 4.

1. \((\ell_0,i)\) is the first block in slab _i_ containing a light-middle 1.<tbc>





Figure 2: Vertical lines mark the boundary of some slab. If _Q_<sub>0,1</sub> appears in one slab of _A_<sub>first</sub>, then there must be an occurrence of _Q=Q_<sub>0,0</sub> in _A_.

Figure 3: If an instance of _Q_<sub>2,2</sub> is contained in a single slab of middle 1s (e.g., _A_<sub>heavy</sub> or _A_<sub>light</sub>), then _Q_<sub>1,1</sub> must also appear in _A_. This inference relies on how _contains_ is defined for _Q<sub>a,b</sub>_ matrices in Definition 3.1. In particular, it is critical that all-zero rows of _Q_<sub>2,2</sub> must _not_ be all-zero in the instance of middle 1s.

