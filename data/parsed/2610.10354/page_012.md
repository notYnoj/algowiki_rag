the universe \[_n_\] is in time \(O(n^{2-\epsilon^\prime})\) (contradicting the Strong Min-Plus Convolution Hypothesis). Let _A,B_ denote the given length-_n_ sequences over the universe \[_n_\]. We rewrite the sequences into their base-\(\sqrt{n}\) representation as

\(A=A_1\cdot q+A_0,\)<br>
\(B=B_1\cdot q+B_0,\)

where the four sequences _A_<sub>0</sub>_,B_<sub>0</sub>_,A_<sub>1</sub>_,B_<sub>1</sub> are each over the universe \([\sqrt{n}]\). Let us call an index _i_ a _witness_ of _k_ if (_A∗B_)\[_k_\]=_A_\[_i_\]+_B_\[_k-i_\], and a _pseudo-witness_ if (_A_<sub>1</sub>∗_B_<sub>1</sub>)\[_k_\]=_A_<sub>1</sub>\[_i_\]+_B_<sub>1</sub>\[_k-i_\]. Equivalently, the pseudo-witnesses are those indices that would become indices when rounding _A,B_ to multiples of \(\sqrt{n}\). By standard approaches, we can assume _A_<sub>0</sub> and _B_<sub>0</sub> have entries less than \(\sqrt{n}/2\), so that a witness must be a pseudo-witness.

We will now execute the structure-versus-randomness paradigm that we sketched in the beginning. The notion of _pseudo-randomness_ turns out to concern the number of pseudo-witnesses: in a pseudo-random instance, all indices _k_ have few pseudo-witnesses, say at most \(n^{1/2+\epsilon/2}\). This is indeed a good case for our reduction, as we can afford to list _all_ pseudo-witnesses. Notably, this list also contains the true witnesses. To obtain the list of pseudo-witnesses, we apply a simple sampling trick (Lemma 2.14), reducing the listing problem to \(\tilde{O}(n^{1/2+\epsilon/2})\) plain min-plus convolutions of restrictions of _A_<sub>1</sub> and _B_<sub>1</sub>. These are sequences over the universe \([\sqrt{n}]\), and can thus be convolved in time \(O(n^{3/2-\epsilon})\) by our initial assumption. The total time is \(O(n^{2-\epsilon/2})\).

Of course, we first need to transform the initial instance (_A,B_) into a pseudo-random one, and this is where the rank becomes relevant. To simplify in this overview, suppose that _all_ indices _k_ have many (i.e., more than \(n^{1/2+\epsilon/2}\)) pseudo-witnesses.<sup>7</sup> In this case, so we claim, the whole instance has low rank and can directly be solved in subquadratic time. To see this, we first apply the standard reduction from Min-Plus Convolution to 3SUM: We approximate _C≈A∗B_ (by some standard trick, with coordinate-wise constant additive error), then replace the sequences _A,B,C_ by their _indexed sets_

\(\mathcal{A}=\{(i,A[i]):0\le i\le n\},\)<br>
\(\mathcal{B}=\{(j,B[j]):0\le j\le n\},\)<br>
\(\mathcal{C}=\{(k,C[k]):0\le k\le 2n\},\)

and solve the remaining 3SUM instance (A,B,C). These are 2-dimensional sets that can be flattened to plain integers via the usual embedding. We argue that C has low rank, \(r(\mathcal{C})\le\tilde{O}(n^{1-\epsilon/4})\). This can be shown in two steps:

• First, consider the set<tbc>

<tbc>\(\mathcal{C}_1=\{(k,(A_1*B_1)[k]\cdot\sqrt{n}):0\le k\le 2n\}.\)<tbc>

<tbc>Assuming that each _k_ has many pseudo-witnesses, we can sample a set of \(\tilde{O}(n^{3/4-\epsilon/4})\) indices \(X\subseteq[0,n]\). With good probability, for each _k_ we include some witness \(i\in X\) and simultaneously also \(k-i\in X\). In this case, the set<tbc>

<tbc>\(\mathcal{X}_1=\{(i,A_1[i]\cdot\sqrt{n}):i\in X\}\cup\{(j,B_1[j]\cdot\sqrt{n}):j\in X\}\)<tbc>

<tbc>satisfies \(\mathcal{C}_1\subseteq\mathcal{X}_1+\mathcal{X}_1\), witnessing that \(r(\mathcal{C}_1)\le|\mathcal{X}_1|\le O(n^{3/4-\epsilon/4})\).

<sup>7</sup>In fact, this idealized situation is impossible. For instance, _k_=0 always has exactly one (pseudo-)witness, namely _i_=0. But this is a technicality that shall not concern us in this overview.

