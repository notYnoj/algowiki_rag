• If _i_ is a \(\times x\) gate in-between the \(\ell\)th and \(\ell+1\)st multiplicative layers, set \(R_i\leftarrow R_i+R_j\times x\), where _j_ is the input gate.<tbc>

• If _i_ is a +_x_ gate in-between the \(\ell\)th and \(\ell+1\)st multiplicative layers, set \(R_i\leftarrow R_i+R_j+x\), where _j_ is the input gate.<tbc>

• If _i_ is a product gate on the \(\ell+1\)st layer of the circuit, set \(R_i\leftarrow R_i+R_jR_k\), set \(R_i^{(1)}\leftarrow R_i^{(1)}+R_k\), and set \(R_i^{(2)}\leftarrow R_i^{(2)}+R_j\), where _j_ and _k_ are the two input gates.

iv) For each gate _i_ (in order of layers, from the output layer backwards):<tbc>

• If _i_ is an addition gate in-between the \(\ell\)th and \(\ell+1\)st multiplicative layers, set \(R_i\leftarrow R_i-R_j-R_k\), where _j_ and _k_ are the two input gates.<tbc>

• If _i_ is a \(\times x\) gate in-between the \(\ell\)th and \(\ell+1\)st multiplicative layers, set \(R_i\leftarrow R_i-R_j\times x\), where _j_ is the input gate.<tbc>

• If _i_ is a +_x_ gate in-between the \(\ell\)th and \(\ell+1\)st multiplicative layers, set \(R_i\leftarrow R_i-R_j-x\), where _j_ is the input gate.<tbc>

v) Run \(A_\ell\) in reverse.<tbc>

vi) For each gate _i_ (in order of layers, from the input layer forwards):<tbc>

• If _i_ is an addition gate in-between the \(\ell\)th and \(\ell+1\)st multiplicative layers, set \(R_i\leftarrow R_i+R_j+R_k\), where _j_ and _k_ are the two input gates.<tbc>

• If _i_ is a \(\times x\) gate in-between the \(\ell\)th and \(\ell+1\)st multiplicative layers, set \(R_i\leftarrow R_i+R_j\times x\), where _j_ is the input gate.<tbc>

• If _i_ is a +_x_ gate in-between the \(\ell\)th and \(\ell+1\)st multiplicative layers, set \(R_i\leftarrow R_i+R_j\), where _j_ is the input gate.<tbc>

• If _i_ is a product gate on the \(\ell+1\)st layer of the circuit, set \(R_i\leftarrow R_i-R_jR_i^{(1)}-R_i^{(2)}R_k\), where _j_ and _k_ are the two input gates.

Observe that, for any non-product gate _i_ between the \(\ell\)th and \(\ell+1\)st layers, _i_ will be reset initially, computed after step iii), and then reset again after step vi). By the same analysis as in \[BCKLS14\], all of the product gates will therefore end up computed at the end of this program. All of the steps are reversible, so we now have a reversible algorithm \(A_{\ell+1}\), which makes two calls to \(A_\ell\) plus an additional \(\widetilde{O}\left(wT\right)\) runtime overhead, and results in all of the gates on multiplicative layer \(\ell+1\) being computed. Note that this algorithm by default wouldn’t result in the gates prior to multiplicative layer \(\ell+1\) being computed. However, we can easily fix this by running \(A_\ell\) again. If the final tail of layers in the circuit are all linear (the last layer isn’t multiplicative), we can compute up to those layers by simply running steps i), \(A_\ell\) (where \(\ell\) is the last multiplicative layer), and iii) on them.

Now, evaluating _A<sub>d</sub>_ will take runtime \(\widetilde{O}\left(3^dwT\right)\), and clean space _O_(log(_w_)+_d_+log(_T_)) (for the global time counter) plus _O(S_) (for the individual register operations). _A<sub>d</sub>_ results in the circuit’s outputs being added into the dirty registers as elements of K_<sub>n</sub>_ -- we observe in Appendix A that such a program can efficiently be converted into one that instead bitwise-XORs the circuit outputs into the dirty space. \(\blacksquare\)

## 4.2 Application: Fourier Transforms

One particularly useful corollary of Theorem 4.3 is the fact that we can implement fast Fourier transforms catalytically:

**Definition 4.4** (Principal Root of Unity)**.** \[BP94, p.11\] Let K be a finite ring and 1_\<m\<_|K|. \(\omega_m\in\mathcal{K}\) is a _principal root of unity_ of order _m_ iff:

• \((\omega_m)^m=1\).<tbc>

• \(\sum_{j=0}^{m-1}(\omega_m)^{ij}=0\) for all \(1\le i<m\).<tbc>

