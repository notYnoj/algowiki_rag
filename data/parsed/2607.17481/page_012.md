<tbc>\(G_{k,m}=(1-q^m)/(1-q)\), and \(q^m=e^{-2\pi ik}=1\) makes the numerator zero. Hence _G<sub>k,m</sub>_=0. □

Lemma 4 (Quantized bound safety). _With features stored at relative precision_ \(\varepsilon\)_, shrinking the computed bound by_ \((1-\lambda)\) _preserves Lemma 2 whenever the bound exceeds_ \(\sqrt{2m}\cdot 2\sqrt{2}\varepsilon/\lambda\).

Proof of Lemma 2. Let \(\hat{A}_k\) and \(\hat{B}_k\) be the DFT coefficients of the z-normalized windows _Z<sub>i,m</sub>_ and _Z<sub>j,m</sub>_, and write \(t_k=|\hat{A}_k-\hat{B}_k|^2\). Parseval’s theorem for the DFT states<tbc>

\(\mathrm{d}_m(i,j)^2=\sum_{r=0}^{m-1}\big(Z_{i,m}[r]-Z_{j,m}[r]\big)^2=\frac{1}{m}\sum_{k=0}^{m-1}t_k.\)

<tbc>Both windows have mean zero, so \(\hat{A}_0=\hat{B}_0=0\) and _t_<sub>0</sub>=0. Both windows are real, so \(\hat{A}_{m-k}=\overline{\hat{A}_k}\) and \(\hat{B}_{m-k}=\overline{\hat{B}_k}\), and taking magnitudes gives _t_<sub>_m-k_</sub>=_t<sub>k</sub>_ for \(1\le k\le m-1\). Hence<tbc>

\(2\sum_{k=1}^{K^\prime} t_k=\sum_{k=1}^{K^\prime}\big(t_k+t_{m-k}\big).\)

<tbc>The cap \(K'\le\lceil m/2\rceil-1\) is equivalent to \(2K'<m\). Under it, the index sets \(\{1,\dots,K'\}\) and \(\{m-K',\dots,m-1\}\) are disjoint subsets of {1_,...,m_-1}, so the right side above is a sum of \(2K'\) distinct terms of the full Parseval sum. Every _t<sub>k</sub>_ is nonnegative, so

\(2\sum_{k=1}^{K^\prime} t_k\le\sum_{k=0}^{m-1}t_k=m\mathrm{d}_m(i,j)^2.\)

By Lemma 1, the stored features equal the coefficients \(\hat{A}_k\) and \(\hat{B}_k\), so the left side equals \(m\underline{\mathrm{d}_{K,m}^2}(i,j)\) by the definition of the bound in §3.2. Dividing by _m_ and taking square roots gives \(\underline{\mathrm{d}_{K,m}}(i,j)\le\mathrm{d}_m(i,j)\). □

Proof of Proposition 2. (i) In the proof of Lemma 2 above, \(m\underline{\mathrm{d}_{K,m}^2}(i,j)=2\sum_{k=1}^{K^\prime} t_k\) is a sum of \(2K'\) distinct nonnegative terms of the full Parseval sum \(\sum_{k=0}^{m-1}t_k=m\mathrm{d}_m(i,j)^2\), and no step of that argument constrains _K_. This proves the inequality for every \(K\ge 2\). For \(K_1\le K_2\) the caps satisfy \(K'_1\le K'_2\), and the sub-sum at _K_<sub>2</sub> contains the sub-sum at _K_<sub>1</sub> plus nonnegative terms, which proves the monotonicity. (ii) An evaluated pair’s exact distance is computed from raw samples and window moments in the closed form of §2. No write reads the features, and the features are read only to propose, filter, and order candidate pairs (§3.4, §3.6). A different width therefore changes only the evaluated set S, and Proposition 1 gives soundness for every \(\mathcal{S}\subseteq\mathcal{U}\). □

Proof of Proposition 4. Let _P_ be the number of windows in one anchor’s directory and let _d_ be its prefix depth. A further split is possible while _d_ is smaller than the signature width _B_, since deepening the prefix uses one signature bit beyond the current depth. While a split is possible, the split rule fires as soon as an insertion pushes _P_ above \(\alpha 2^d\), so \(P\le\alpha 2^d\) holds after every insertion, and the mean bucket occupancy _P/_2_<sup>d</sup>_ is at most \(\alpha\). Before the first split the directory may be far below this bound. After the first split, the split that brought the directory to its current depth _d_ fired because _P_ exceeded \(\alpha 2^{d-1}\), and _P_ never decreases, so \(\alpha 2^{d-1}<P\le\alpha 2^d\) and the mean occupancy lies in \((\alpha/2,\alpha]\). A doubling at depth _d_ rehomes at most \(\alpha 2^d+1\) entries. The split that reached the final depth _D_ fired because the population then exceeded \(\alpha 2^{D-1}\), which<tbc>

<tbc>is smaller than _P_final, so the total rehoming work over all doublings is at most

\(\sum_{j=1}^D\big(\alpha 2^j+1\big)\le 2\alpha 2^D+D<4P_\mathrm{final}+D.\)

This is _O(P_final) moves over _P_final insertions, which is _O_(1) amortized per insertion. Once _d_ reaches the signature width or the implementation cap, no bit remains to split on, and no further occupancy guarantee is possible without raising that limit. □

Proof of Proposition 3. Consider a matchable pair. For each anchor \(a\in M_A\), let _E<sub>a</sub>_ be the event that anchor _a_ discovers the pair, meaning that the two windows collide in anchor _a_’s directory and that the budgeted scan then retains the pair. By the definitions of _p<sub>a</sub>_ and _c<sub>a</sub>_ in the statement, Pr\[_E<sub>a</sub>_\]=_p<sub>a</sub>c<sub>a</sub>_. Treat the series as given, so that the only remaining randomness is in the projections \(g_{a,\ell}\). Every quantity that determines _E<sub>a</sub>_ is a function of the data and of anchor _a_’s own projections _g_<sub>_a,_1</sub>_,...,g<sub>a,B</sub>_ and of nothing else: the signatures of the two windows, the bucket each occupies, the other occupants of that bucket, and the scan’s deterministic selection within it all depend only on these (§3.4). The projection families of different anchors are drawn independently, so the events \(\{E_a\}_{a\in M_A}\) are functions of mutually independent random variables and are therefore mutually independent, and so are their complements. Hence

\(\mathrm{Pr}\big[\cap_{a\in M_A}E_a^\mathrm{c}\big]=\prod_{a\in M_A}\mathrm{Pr}\big[E_a^\mathrm{c}\big]=\prod_{a\in M_A}\big(1-p_ac_a\big),\)

which establishes the claimed bound. □

Proof of Lemma 3. Write \(p(y)=\langle g,y\rangle\) for the projection of a feature vector _y_, so the sieve sorts the class by _p_. A member _x_ lands strictly between _u_ and _v_ in the sorted order exactly when _p(x_) lies strictly between _p(u_) and _p(v_), which happens exactly when \(p(x)-p(u)=\langle g,x-u\rangle\) and \(p(x)-p(v)=\langle g,x-v\rangle\) differ in sign. By Fact 1, this event has probability \(\angle(x-u,x-v)/\pi\) over the Gaussian draw of _g_. That angle is the angle at which _x_ sees the segment from _u_ to _v_. The segment has length \(\delta\), and _x_ lies at distance at least _r<sub>x</sub>_ from both of its endpoints, so the angle is largest when both distances equal _r<sub>x</sub>_ exactly, the isosceles configuration with \(\mathrm{sin}(\theta/2)=\delta/2r_x\). The function arcsin is convex on \[0,1\] with arcsin(0)=0 and \(\mathrm{arcsin}(1)=\pi/2\), so \(\mathrm{arcsin}(z)\le(\pi/2)z\) there. The probability that _x_ lands between the pair is therefore at most<tbc>

\(\frac{\theta}{\pi}\le\frac{2\mathrm{arcsin}(\delta/2r_x)}{\pi}\le\frac{2}{\pi}\cdot\frac{\pi}{2}\cdot\frac{\delta}{2r_x}=\frac{\delta}{2r_x}.\)

<tbc>Let _N_ be the number of members landing strictly between _u_ and _v_. _N_ is a sum of indicator variables, one per other member, so linearity of expectation gives the first claim,

\(\mathbb{E}[N]\le\frac{\delta}{2}\sum_x\frac{1}{r_x}.\)

If _u_ and _v_ are separated by more than _w_ positions in the sorted order, then at least _w_ members lie strictly between them, so that event implies \(N\ge w\). Outcomes with \(N\ge w\) contribute at least _w_ to the expectation, and all other outcomes contribute at least zero, so \(\mathbb{E}[N]\ge w\mathrm{Pr}[N\ge w]\). Dividing by _w_ gives the second claim, \(\mathrm{Pr}[N\ge w]\le\mathbb{E}[N]/w\). □

