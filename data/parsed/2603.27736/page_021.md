#### Running Time.

To compute the sets \(I_\ell\) and \(J_\ell\) we first precompute the statistics \(|\{j\in[m]:S[i,j]=\ell\}|\) (for all \(i,\ell\)) and \(|\{i\in[n]:S[i,j]=\ell\}|\) (for all \(j,\ell\)) in time \(\tilde{O}(nm+nr+mr)\). Afterwards we can read off \(I_\ell\) and \(J_\ell\) in the same running time. Then it is straightforward to compute the partition \(A=A_\text{row}\sqcup A_\text{col}\sqcup A_\text{sm}\) in time \(\tilde{O}(nm)\). It remains to analyze the time to compute the rank decompositions of _A_row, _A_col and _A_sm. The decompositions of _A_row and _A_col are computable from (_U,V,S_) in linear time \(\tilde{O}(nm)\). For the decomposition of _A_sm the dominating step is the computation of S in time \(\tilde{O}(nmr)\) by Lemma 3.7; the remaining steps run in time \(\tilde{O}(nm+nr+mr)\).

## 4 Low-Rank Exact Triangle

The main result of this section is that Low-Rank Exact Triangle can be solved in subcubic time:

**Theorem 4.1** (Low-Rank Exact Triangle)**.** _The r-rank Exact Triangle problem can be solved in deterministic time_

\(\text{ExactTri}(n,n,n|r)\le n^{3+o(1)}\cdot\left(\frac{r}{n^{3-\omega}}\right)^{1/200000}.\)

The point of this theorem is that for \(r\le n^{3-\omega-\epsilon}\) this running time is truly subcubic, \(O(n^{3-\Omega(\epsilon)})\). We have not attempted to optimize the constant 200000. Likely, it can be improved dramatically, but for all our applications the constant does not matter. The proof of Theorem 4.1 is an algorithmic reduction from the Low-Rank Exact Triangle problem via various intermediate steps to the Uniform Low-Doubling Exact Triangle problem:

**Lemma 4.2** (Reduction from Low-Rank to Uniform Low-Doubling Exact Triangle)**.** _For any parameter_ \(K\ge 1\) _there is a potential-adjusting reduction from any r_-rank _Exact Triangle instance to K(n_<sub>1</sub>_n_<sub>2</sub>_n_<sub>3</sub>)<sup>_o_(1)</sup> _instances that are each D_-uniform, 1_/D_-regular _and K_-doubling _for some_ \(D\le r\)_. The reduction runs in deterministic time_ (_n_<sub>1</sub>_n_<sub>2</sub>_n_<sub>3</sub>_/K_<sup>1/98000</sup>+(_n_<sub>1</sub>_n_<sub>2</sub>+_n_<sub>1</sub>_n_<sub>3</sub>+_n_<sub>2</sub>_n_<sub>3</sub>)_rK_)<sup>1+_o_(1)</sup>_. In particular:_

\(\text{ExactTri}(n_1,n_2,n_3|r)\)<br>
\(\le\left(K\cdot\text{ExactTri}(n_1,n_2,n_3|D\le r;\rho\le 1/D;K)+\frac{n_1n_2n_3}{K^{1/98000}}+(n_1n_2+n_2n_3+n_1n_3)rK\right)^{1+o(1)}.\)

Intuitively, this lemma states that we can reduce an _r_-rank instance in subcubic time to few instances that are _r_-uniform and _K_-doubling, for an arbitrarily small polynomial \(K=n^{^\epsilon}\). (In fact, the instances are also regular, but we do not need to rely on this extra constraint here.) This is a special case of Exact Triangle that can be solved in subcubic time by a simple algebraic algorithm; see \[4, Lemma 5.5\]<sup>15</sup>.

**Lemma 4.3** (Uniform Low-Doubling Exact Triangle \[4\])**.** _Any Exact Triangle instance_ (_A,B,C_) _can be solved in deterministic time_ \(\tilde{O}(\text{MM}(n_1,n_2,n_3)\cdot|X+X|)\)_, where X is the set of integer entries in A, B and C. In particular:_

\(\text{ExactTri}(n_1,n_2,n_3|D;K)=\tilde{O}(\text{MM}(n_1,n_2,n_3)\cdot DK).\)

<sup>15</sup>A subtlety in \[4, Lemma 5.5\] is that it only determines the edges \((i,j)\in[n_1]\times[n_3]\) that are involved in exact triangles, but not the edges \((i,k)\in[n_1]\times[n_2]\) and \((k,j)\in[n_2]\times[n_3]\). However, since in Lemma 4.3 _X_ denotes the set of entries in all three matrices _A,B,C_, we can simply apply \[4, Lemma 5.5\] three times on all rotations of the instance (_A,B,C_). Alternatively, as stated in \[4\], one can apply the Baur-Strassen trick \[51, 16\].

