<tbc>Lemma 4.13 with parameter _K_. This results in a set of \(t^{875}(n_1n_2n_3)^{o(1)}\cdot K^{1/112}\le K(n_1n_2n_3)^{o(1)}\) instances that are uniform, regular and low-doubling as claimed. The total running time is

\(\big(\frac{n_1n_2n_3}{t}+(n_1n_2+n_2n_3+n_1n_3)rt^{875}+t^{875}\cdot\big(\frac{n_1n_2n_3}{K^{1/112}}+(n_1n_2+n_2n_3+n_1n_3)rK^{1/112}\big)\big)^{1+o(1)}\)<br>
\(=\big(\frac{n_1n_2n_3}{K^{1/98000}}+(n_1n_2+n_2n_3+n_1n_3)rK\big)^{1+o(1)}.\)

This completes the reduction and thus the proof of Theorem 4.1.

## 5 Universe Reductions for Min-Plus Product

In this section, we develop the universe reductions for Min-Plus Product (and thereby for APSP). The structure of this section is as follows: In Section 5.1 we recap a standard trick from fine-grained complexity. In Section 5.2 we give the universe reduction from small universes to even smaller universes (say from _u=n_ to \(u=\sqrt{n}\)), proving Theorem 1.7. In Section 5.3 we give the reduction from Min-Plus Product to Uniform Low-Doubling Min-Plus Product. And in Section 5.4 we conclude the conditional universe reduction from polynomially large to small universes, proving Theorem 1.13.

### 5.1 Listing-to-Decision Reduction

Before we start, we recap a standard _listing-to-decision reduction_ that allows to transform any detection algorithm into an algorithm that also lists some "witnesses" for a quite general class of problems. In the context of Min-Plus Product, we call _k_ a _witness_ of (_A∗B_)\[_i,j_\] if _A_\[_i,k_\]+_B_\[_k,j_\]=(_A∗B_)\[_i,j_\]. Then:

**Lemma 5.1** (Listing-to-Decision Reduction for Min-Plus Product)**.** _Let_ (_A,B_) _be a Min-Plus Product instance, and assume that there is an algorithm computing the min-plus product_ \(A'*B'\) _of any restrictions of A and B in time T. Then, for any parameter_ \(t\ge 1\)_, we can compute lists of up to t witnesses for all_ (_A∗B_)\[_i,j_\] _in randomized time_ \(\tilde{O}(Tt)\).

**Proof Sketch.** The proof is a by-now standard argument from sparse recovery; we only give a quick sketch here. Consider the restrictions \(A'\) and \(B'\) randomly obtained from _A_ and _B_ as follows. Sample \(\ell\in[\lceil\mathrm{log}n_2\rceil]\) uniformly at random, then sample \(K\subseteq[n_2]\) uniformly at random with rate \(2^{-\ell}\). Let \(A'\) be the matrix obtained from _A_ by setting all columns _k_ that are not present in _K_ to \(\perp\). It can be shown that, for any fixed pair (_i,j_), with probability at least \(\Omega(1/\mathrm{log}n_2)\) in the min-plus product \(A'*B\) _exactly one_ witness of (_i,j_) is still present. In this case we say that (_i,j_) is _successful_. Moreover, by symmetry this unique witness is sampled uniformly at random.

We now argue that by _O_(log_n_<sub>2</sub>) calls to the fast algorithm we can identify the surviving witness for all successful pairs (_i,j_). To this end, identify each entry \(k\in[n_2]\) with its \(L=\lceil\mathrm{log}n_2\rceil\)-bit binary representation. We write \(k[\ell]\) for the \(\ell\)-th bit. Let \(A'_\ell\) be the matrix obtained from \(A'\) where we replace the _k_-th column by \(\perp\) if \(k[\ell]=0\). We compute the min-plus products \(A'_\ell*B\) for all \(\ell\in[L]\). Now take any successful pair (_i,j_), and inspect the sequence \((A'_0*B)[i,j],\dots,(A'_L*B)[i,j]\). Some of these values are exactly equal to (_A∗B_)\[_i,j_\], others are strictly larger--the length-_L_ bit-string indicating the larger values is exactly the bit-representation of the unique witness _k_ of (_i,j_). In particular, for all successful pairs (_i,j_) we can read off (and verify) the surviving witness _k_.

Overall, by repeating this procedure \(\tilde{O}(t)\) times, we expect to list \(\tilde{O}(t)\) uniformly random witnesses for each entry (_A∗B_)\[_i,j_\]. Thereby we either list _t_ distinct witnesses (if they exist), or otherwise have listed all witnesses with good probability.

With exactly the same proof one can also list witnesses for the Exact Triangle problem, see the following Lemma 5.2. In this context we call _k_ a _witness_ of _C_\[_i,j_\] if _A_\[_i,k_\]+_B_\[_k,j_\]=_C_\[_i,j_\]. Similarly, in this case _j_ is a _witness_ of _A_\[_i,k_\] and _i_ is a witness of _B_\[_k,j_\].

