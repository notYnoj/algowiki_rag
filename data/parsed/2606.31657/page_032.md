_Proof._ The inequality \(\mathrm{Inf}(f)\le D(f)\) is classical for Boolean functions; see, for example, Rossman’s discussion of formula average sensitivity \[41\]. Therefore every coordinate counted in Corollary 6.4 also has decision-tree depth \(\Omega(k)\).

What is new here is an explicit satisfiable bounded-occurrence family for which, even allowing internal randomness and approximation in expectation, linearly many seedwise output bits have linear deterministic query complexity with respect to the message coordinates, on average over the seed. This contrasts with local-access results that achieve polylogarithmic query complexity under strong LLL-type sparsity assumptions or in the high-_k_/low-degree regime \[13, 42\].

## 6.5 Constant-Depth Circuits and s

We now record a bounded-depth consequence. Boppana’s average-sensitivity bound for constant- depth circuits and Rossman’s strengthening for bounded-depth formulas place polynomial-size bounded-depth computation in the low-influence regime on the message cube \[5, 41\]. Since our hard family is embedded into the standard SAT encoding by a linear-size _NC_<sup>0</sup> map, the same barrier transfers to randomized bounded-depth computation for finding near-satisfying assignments on satisfiable Max E3SAT instances.

**Corollary 6.8** (No polynomial-size constant-depth randomized circuits for finding near-satisfying assignments)**.** _Fix the standard binary encoding of_ 3_-CNF formulas with n variables and M clauses. Then there is no randomized polynomial-size constant-depth circuit family that, on every satisfiable input formula of this size, outputs in expectation a_ \((1-\eta)\)_-approximate assignment. The same holds for randomized bounded-depth formula families._

_More quantitatively, for every fixed depth D, any such depth-D randomized circuit family must have size_ \(\mathrm{exp}\big(n^{\Omega_D(1)}\big)\).

_Proof._ Suppose there were such a randomized polynomial-size constant-depth circuit family for the encoded 3-CNF inputs. Write it as a deterministic circuit family<tbc>

\(C_{n,M}(x,r)\)

<tbc>with an explicit random seed _r_, and let _A_ denote the induced output distribution when _r_ is sampled uniformly. Composing with the hard embedding<tbc>

\(m\longmapsto x(m)=\mathrm{Enc}_{n,M}(\Phi(m))\)

<tbc>yields, for each fixed seed _r_, a deterministic polynomial-size constant-depth multi-output circuit<tbc>

\(F_r(m)=\big(f_{1,r}(m),\dots,f_{n,r}(m)\big)\)

<tbc>on the message cube, because _x_ is computable by a linear-size _NC_<sup>0</sup> circuit. (The same substitution argument applies to formulas.) By Corollary 6.3, one has<tbc>

\(\mathbb{E}_R\big[\sum_{v=1}^n\mathrm{Inf}(f_{v,R})\big]=\Omega(nk).\)

<tbc>On the other hand, Boppana’s average-sensitivity upper bound for bounded-depth circuits and Rossman’s strengthening for bounded-depth formulas imply that every output bit of a polynomial- size constant-depth circuit or formula has sublinear influence on {0,1}_<sup>k</sup>_, uniformly over the fixed seed _r_ \[5, 41\]. Hence<tbc>

\(\mathbb{E}_R\big[\sum_{v=1}^n\mathrm{Inf}(f_{v,R})\big]=o(nk),\)

