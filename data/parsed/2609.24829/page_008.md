The choice to decrease our guess by a factor of 2 with each pass is quite arbitrary, and results in the logarithmic number of passes. One could ask what would happen if we were to use a larger factor decrease _r_ in order to get at most _c=O_(1) passes? That is, we look for _r_ such that we can set \(\tau_j=r^{-j}m^{3/2}\) and _r_<sup>-_c_</sup>_m_<sup>3/2</sup>=1. Consequently, _r=m_<sup>3/2_c_</sup>. The correctness of the algorithm with geometrically decreasing guesses with a factor of _r_ goes through just the same, however there is a cost in terms of space complexity: Suppose that \(T\le m\). Then \(s(m,\tau)=\widetilde{O}(m/\sqrt{\tau})\). On pass _j_ where \(\tau_j\le T\le r\tau_j\) we terminate, and use expected space \(s(m,\tau_j)\le s(m,T/r)=\widetilde{O}(m/\sqrt{T/r})=\widetilde{O}(m^{1+3/4c}/\sqrt{T})\). That is, the reduced number of passes comes at a cost of space blowup; We wish to maintain a small space complexity - even at the cost of more than constant passes, or a worse approximation.

## 3.3 Segmenting a Stream

The aforementioned space blowup illustrates the need to search for a different approach. A first attempt is to partition a prefix of a randomly-ordered stream into 1_/p_ segments \(\langle S_1|S_2|\cdots|S_{1/p}\rangle\) where each edge \(e\in S_i\) with probability _p_. Deciding on a _fixed_ size for each segment _m<sub>i</sub>_ makes the analysis difficult, as each segment is a sample of _m<sub>i</sub>_ edges from _G without replacement_. To circumvent this issue, we sample the set of 1_/p_ lengths from a _multinomial_ distribution. This solution is captured by the following lemma:

**Lemma 3.1.** Let _S_ be a length _m_ random-order stream of the edge set _E_. Sample \((m_1,\dots,m_{1/p})\sim Mult(m;p,\dots,p)\), and let \(\langle S_1|S_2|\cdots|S_{1/p}\rangle\) be a segmentation of _S_ into 1_/p_ segments, where |_S<sub>j</sub>_|=_m<sub>j</sub>_. Then for each \(F\subset E\) with |_F_|=_k_, Pr\[_S<sub>i</sub>=F_\]=_p<sup>k</sup>_(1-_p_)<sup>_m-k_</sup>.

_Proof._ The probability _S<sub>i</sub>=F_ is

\(Pr\left[m_i=k\right]\cdot Pr\left[random\text{subset of}k\text{elements equals}F\right]=\genfrac(){pt}{2}{m}{k}p^k(1-p)^{m-k}\frac{1}{\genfrac(){pt}{2}{m}{k}}=p^k(1-p)^{m-k}.\)

That is, the distribution of _S<sub>i</sub>_ is the same as a sampled set of edges from _E_ where each edge is added to _S<sub>i</sub>_ independently with probability _p_. We use this argument repeatedly. Therefore, while the segments are simply contiguous parts of a random order stream, we refer to them as sets obtained by independently sampling edges with the appropriate probability. We face two problems: (i) Different segments of the stream may not be representative of the entirety of the stream, and (ii) We need to ensure that we advance to a sufficiently accurate guess before we run out of data.

The first challenge is less of a concern for randomly ordered streams, and is handled by the following lemma:

**Lemma 3.2** (Lemma 4.1, informal)**.** Let _G_ be a graph with _n_ vertices and _T_ triangles, and let _T<sub>p</sub>_ be the number of triangles in the graph formed by sampling each edge independently with probability _p_. Then with probability at least 1-1_/n_<sup>4</sup>, _T<sub>p</sub>_ is within \(\pm\varepsilon p^3max(\tau,T)\) of _p_<sup>3</sup>_T_, where \(\tau=\widetilde{\Omega}(\varepsilon^{-2}p^{-1}\eta+\varepsilon^{-2}p^{-5})\) and \(\eta\ge\Delta_e\).

That is, as long as we have an upper bound on \(\Delta_e\), the number of triangles in each segment is sufficiently concentrated around its mean. There is a natural upper bound of _n_ on \(\Delta_e\) which leads us to a preliminary result: A one pass algorithm that either outputs an approximation of _T_, or declares that _T_ is upper bounded by \(\widetilde{O}(n)\).

Note that _t_ is the smallest integer satisfying \(2^{-t}m^{3/2}\le\tau^*\), so \(2^{-(t-1)}m^{3/2}>\widetilde{\Omega}(\varepsilon^{-2}n)\ge 1\), therefore \(2^{t-1}\le m^{3/2}\) which implies _t=O_(log(_n_)).

To fix notation, for each \(j\in[t]\), we call _S<sub>j</sub>_ a _segment_ of _S_, and let _T<sub>j</sub>_ be the number of triangles in the _j_th segment. We say that a segment is _representative_ if \(T_j\in(1\pm\varepsilon)t^{-3}max(T,\tau^*)\). In particular, when \(T\ge\tau^*\), a representative segment satisfies \(T_j\in(1\pm\varepsilon)t^{-3}T\).

