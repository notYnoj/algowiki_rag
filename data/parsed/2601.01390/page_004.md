**Lemma 2.1.** _Given a set X of integers in_ \[_u_\] _and a number k, we can compute_ \(\Sigma_i(X)\) _for all_ \(i\in[k]\)_, in_ \(\widetilde{O}(k^3u)\) _deterministic time._

_Afterwards, for any given_ \(i\in[k]\) _and_ \(y\in\Sigma_i(X)\)_, we can report one subset_ \(S\subseteq X\) _with_ |_S_|=_i and_ \(\sigma(S)=y\)_, in_ \(\widetilde{O}(k)\) _time._

_Proof._ W.l.o.g., assume that _u_ is a power of 2. A _dyadic interval_ is an interval of the form \((a,a+\ell]\) where the length \(\ell\) is a power of 2 and _a_ is divisible by \(\ell\). For each dyadic interval \(I=(a,a+\ell]\subseteq(0,u]\), we want to compute \(\{\Sigma_i(X\cap I)\}_{i\in[k]}\).

Decompose _I_ into two dyadic subintervals \(I'=(a,a+\ell/2]\) and \(I''=(a+\ell/2,a+\ell]\). We can compute \(\{C_i:=\Sigma_i(X\cap I)\}_{i\in[k]}\) from \(\{A_{i^\prime}:=\Sigma_{i^\prime}(X\cap I')\}_{i^\prime\in[k]}\) and \(\{B_{i^{\prime\prime}}:=\Sigma_{i^{\prime\prime}}(X\cap I'')\}_{i^{\prime\prime}\in[k]}\) by the formula \(C_i=\bigcup_{i^\prime,i^{\prime\prime}:i^\prime+i^{\prime\prime}=i}(A_{i^\prime}+B_{i^{\prime\prime}})\). Since \(A_{i^\prime}\subseteq(ai',(a+\ell/2)i']\) and \(B_{i^{\prime\prime}}\subseteq((a+\ell/2)i'',(a+\ell)i'']\) are contained in intervals of length \(O(k\ell)\) for each \(i',i''\in[k]\), we can compute each sumset \(A_{i^\prime}+B_{i^{\prime\prime}}\) via a convolution of two Boolean vectors of length \(O(k\ell)\) in \(O(k\ell log(k\ell))\) time. For each element \(z\in A_{i^\prime}+B_{i^{\prime\prime}}\), we can also compute a _witness_ \((x,y)\in A_{i^\prime}\times B_{i^{\prime\prime}}\) with _x+y=z_, in \(O(k\ell log^{O(1)}(k\ell))\) time using the deterministic witness-finding technique by Alon and Naor \[AN96\].<sup>4</sup> The total cost over all _O(k_<sup>2</sup>) choices of \((i',i'')\) is \(O(k^3\ell log^{O(1)}\ell)\). For each element \(z\in C_i\), we can also record an \((i',i'')\) with \(i'+i''=i\) and \(z\in A_{i^\prime}+B_{i^{\prime\prime}}\).

Proceeding bottom-up over all dyadic intervals, which have total length _O(u_log_u_), we obtain a total running time of \(\widetilde{O}(k^3u)\). For the root interval _I_<sub>0</sub>=(0_,u_\], we can report a subset corresponding to a given \(i\in[k]\) and \(y\in\Sigma_i(X\cap I_0)\) in \(\widetilde{O}(k)\) time by backtracking using the witnesses to the convolutions.

_(Note._ Koiliaris and Xu’s original version of the algorithm \[KX19\] achieved \(\widetilde{O}(k^2u)\) time instead of \(\widetilde{O}(k^3u)\), essentially by observing that the _C<sub>i</sub>_’s can be computed by a single convolution of vectors of length \(O(k^2\ell)\), instead of _O(k_<sup>2</sup>) convolutions of vectors of length \(O(k\ell)\). Also, they performed the divide-and- conquer slightly differently, by sorting the elements _x_<sub>1</sub>_,...,x<sub>n</sub>_ of _X_ and computing \(\{\Sigma_i(\{x_j:j\in I\})\}_{i\in[k]}\) for dyadic intervals \(I\subseteq(0,n]\). This allows some log_u_ factors to be replaced by log_n_, which isn’t important to us, although this alternative will be useful later in Section 3.)

## 2.2 Halver

The key idea behind our algorithm concerns the construction of a _halver_, which we define below:

**Definition 2.2.** _Given a set X of positive integers, and numbers k and_ \(\Delta\)_, a_ \((k,\Delta)\)-halver _of X is a partition of X into two disjoint subsets_ \(X'\) _and_ \(X''\) _with the following property:_

_For every subset_ \(S\subseteq X\) _with_ \(|S|\le k\)_, there exists a subset_ \(\hat{S}\subseteq X\) _with_ \(|\hat{S}|\le k\), \(\sigma(\hat{S})=\sigma(S)\)_, and_ \(|\hat{S}\cap X'|,|\hat{S}\cap X''|\le|\hat{S}|/2+\Delta\).

Note the slight subtlety with the existential quantifier in the above definition (since there could be multiple subsets with the same cardinality and the same sum as _S_). We recall a well-known fact from discrepancy theory:

**Lemma 2.3.** _Given a set X and a collection_ C _of subsets of X each of size at most k, we can compute a partition of X into two subsets_ \(X'\) _and_ \(X''\) _such that_ \(|S\cap X'|,|S\cap X''|\le|S|/2+O(\sqrt{|S|log|\mathcal{C}|})\) _for all_ \(S\in\mathcal{C}\)_, in O(k_|C|+|_X_|) _deterministic time._

<sup>4</sup>Alon and Naor’s witness-finding technique was originally described for matrix multiplication, but the technique is general and applies to convolution.

