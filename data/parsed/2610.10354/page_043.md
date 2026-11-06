## 6 Lower Bounds for Intermediate Convolution Problems

In this section, we show our lower bounds for intermediate problems under the Strong Min-Plus Convolution Hypothesis (also under the standard Min-Plus Convolution Hypothesis if we assume Hypothesis 1.7).

We start with a useful lemma, which separately handles those heavy input entries.

**Lemma 6.1.** _Let_ (_A,B_) _be a given Min-Plus Convolution Listing instance with listing threshold_ \(n^\ell\) _for some_ \(\ell\ge 1/2\)_. Suppose C=A∗B is also given and let_ \(\delta>0\) _be a given constant. Then in_ \(\widetilde{O}(n^{2-\delta/2})\) _time, we can reduce it to a Min-Plus Convolution Listing instance_ \((A,B')\)_, where all entries in B that appear more than_ \(n^{\ell+\delta}\) _times are replaced with_ \(\perp\).

**Proof.** Call a value _v_ in _B_ heavy if it appears more than \(n^{\ell+\delta}\) times in _B_. Note that there could be at most \(O(n^{1-\ell-\delta})\) heavy value _v_. It suffices to list up to \(n^\ell\) witnesses (_i,j_) per output _C_\[_k_\], among those witnesses where _B_\[_j_\] is a heavy element.

To do so, let _v_ be an arbitrary heavy element in _B_, and define \(J_v=\{j\in[0,n]:B[j]=v\}\). For every distinct value _u_ in _A_, define \(I_u=\{i\in[0,n]:A[i]=u\}\) and \(K_{u+v}=\{k\in[0,2n]:C[k]=u+v\}\). These sets can be precomputed in near-linear time. Clearly, a pair \((i,j)\in I_u\times J_v\) is a witness for _C_\[_i+j_\] if \(i+j\in K_{u+v}\).

For a fixed pair of _u,v_, using FFT, we can verify whether each \(k\in K_{u+v}\) has a witness from \(I_u\times J_v\) in \(\widetilde{O}(n)\) total time for all _k_. Moreover, using standard sampling-based approaches (Lemma 2.15), we can list up to \(\lfloor\frac{|I_u|}{n^{1-\ell-\delta/2}}\rfloor\) witnesses per \(k\in K_{u+v}\) in \(\widetilde{O}(\lfloor\frac{|I_u|}{n^{1-\ell-\delta/2}}\rfloor n+1)\) time. The +1 term in the previous running time is needed for the case \(\lfloor\frac{|I_u|}{n^{1-\ell-\delta/2}}\rfloor=0\). Over all values of _v_ and _u_, the total cost for this case is thus (up to polylog(_n_) factor)

\(\sum_u\sum_v\left(\left\lfloor\frac{|I_u|}{n^{1-\ell-\delta/2}}\right\rfloor n+1\right)\le n^{1-\ell-\delta}\sum_u\left(\frac{|I_u|}{n^{1-\ell-\delta/2}}\cdot n+1\right)\le O(n^{2-\delta/2}).\)

Hence, it suffices to consider some \(k\in K_{u+v}\) for sub-instances (_I<sub>u</sub>,J<sub>v</sub>,K_<sub>_u+v_</sub>) where _k_ has at least \(\lfloor\frac{|I_u|}{n^{1-\ell-\delta/2}}\rfloor\) witnesses (and we have not found up to \(n^\ell\) witnesses in the input instance (_A,B_) for _k_). In this case, we simply spend _O_(|_I<sub>u</sub>_|) time to list all the witnesses for _k_ in (_I<sub>u</sub>,J<sub>v</sub>,K_<sub>_u+v_</sub>). Let _U<sub>k</sub>_ be the set of _u_ where we need to perform this brute-force over _I<sub>u</sub>_ for _k_. Note that for a fixed _k_, _C_\[_k_\]=_u+v_ is fixed; in addition, the number of heavy values _v_ is \(O(n^{1-\ell-\delta})\), so the number of _u_ where \(k\in K_{u+v}\) is also \(O(n^{1-\ell-\delta})\). Hence \(|U_k|\le O(n^{1-\ell-\delta})\).

As we only need to output \(n^\ell\) total witnesses for _k_, we have<tbc>

\(\sum_{u\in U_k}\left\lfloor\frac{|I_u|}{n^{1-\ell-\delta/2}}\right\rfloor\le n^\ell,\)

<tbc>which implies (recall we assume \(\ell\ge 1/2\))<tbc>

\(\sum_{u\in U_k}\frac{|I_u|}{n^{1-\ell-\delta/2}}\le|U_k|+n^\ell\le n^{1-\ell-\delta}+n^\ell=O(n^\ell).\)

<tbc>Hence, the cost for a particular value of _k_ is

\(O\left(\sum_{u\in U_k}|I_u|\right)\le O(n^\ell\cdot n^{1-\ell-\delta/2})=O(n^{1-\delta/2}).\)

Summing over all possible _k_ gives an \(O(n^{2-\delta/2})\) running time, as desired.

