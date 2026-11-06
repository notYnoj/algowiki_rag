## 16 Asteroidal Triples and Friends in (Likely Necessary) Matrix Multiplication Time

If deg(_x_)=0, then \(V_x=\varnothing\) and _D<sub>x</sub>_=0, so Equation (2) holds in this case as well. We can use this last inequality in the following chain of inequalities:

\(2\cdot|\mathcal{C}^{i,j}|\cdot 2^{2j+2}>2\cdot\sum_{C\in\mathcal{C}^{i,j}}deg(C)^2\) (3)

\(\ge\sum_{x\in V}D_x\) (4)

\(\ge\sum_{x\in V}\big(deg(x)^2\cdot 2^{i-3}-deg(x)\cdot 2^{i+1}\big)\) (5)

\(\ge 2^{i-3}/n\cdot\big(\sum_{C\in\mathcal{C}^{i,j}}deg(C)\big)^2-2^{i+1}\cdot\sum_{C\in\mathcal{C}^{i,j}}deg(C)\) (6)

\(>2^{i-3+2j}/n\cdot|\mathcal{C}^{i,j}|^2-2^{i+j+2}\cdot|\mathcal{C}^{i,j}|,\) (7)

where we use:

**Equation (3):** By the definition of C_<sup>i,j</sup>_, we have deg(_C)\<_2<sup>_j_+1</sup> for any \(C\in\mathcal{C}^{i,j}\).

**Equation (4):** The expression \(\sum_{C\in\mathcal{C}^{i,j}}deg(C)^2\) counts all length-two walks in **F**_<sup>i,j</sup>_ whose endpoints lie in _V_ and whose middle vertex lies in C_<sup>i,j</sup>_, while \(\sum_{x\in V}D_x\) counts a subset of these walks.

**Equation (5):** Equation (2).

**Equation (6):** Cauchy-Schwarz inequality on a length-_n_ vector that contains deg(_x_) in the entry indexed by \(x\in V\) and an all-one vector of the same length. We also use that \(\sum_{x\in V}deg(x)=\sum_{C\in\mathcal{C}^{i,j}}deg(C)\).

**Equation (7):** By the definition of C_<sup>i,j</sup>_, we have \(2^j\le deg(C)<2^{j+1}\) for any \(C\in\mathcal{C}^{i,j}\).

The previous chain of inequalities yields immediately the claim:

\(|\mathcal{C}^{i,j}|<(2^{2j+2}+2^{i+1+j})\cdot n/2^{i-3+2j}=(2^{-i+6}+2^{-j+5})\cdot n.\) \(\triangleleft\)

Since {C_<sup>i,j</sup>_}_<sub>i,j</sub>_ partitions C, we conclude that:

\(|\mathcal{C}|\le\sum_{i=0}^{\lceil\mathrm{log}n\rceil}\sum_{j=0}^{\lceil\mathrm{log}n\rceil}|\mathcal{C}^{i,j}|\le n\cdot\big(\sum_{i=0}^{\lceil\mathrm{log}n\rceil}\sum_{j=0}^{\lceil\mathrm{log}n\rceil} 2^{-i+6}+\sum_{j=0}^{\lceil\mathrm{log}n\rceil}\sum_{i=0}^{\lceil\mathrm{log}n\rceil} 2^{-j+5}\big)\le n\cdot\lceil\mathrm{log}n\rceil\cdot(2^7+2^6)\le 400n\mathrm{log}n,\)

as desired.

Finally, we can show how to determine in time \(\tilde{\mathcal{O}}(n^\omega)\) whether a graph is AT-free by exploiting the structural result on AT-free graphs that we just established.

**Main Theorem 2.** _There is a deterministic_ \(\tilde{\mathcal{O}}(n^\omega)\)_-time algorithm that determines if a graph is AT-free._

**Proof.** Given an input graph **G**=(_V,E_), our algorithm proceeds as follows:

(i) First, we apply Main Theorem 1 to identify the collection C of all neighborhood-deleted components. Formally, let \(\mathcal{C}_x=\{C_x(v):v\in V\backslash N[x]\}\) denote the set of connected components in **G**_<sub>x</sub>_. Then, \(\mathcal{C}=\bigcup_{x\in V}\mathcal{C}_x\).

(ii) Via Lemma 3.2, we assign each component \(C\in\mathcal{C}\) a unique identifier _h(C_), which allows us to count the number of distinct components in \(\tilde{\mathcal{O}}(n^2)\) time. If |C|_\>_400_n_log_n_, we terminate the process and report that **G** is not AT-free.

(iii) Otherwise, for each distinct \(C\in\mathcal{C}\), we fix an arbitrary _representative_ vertex \(r_C\in V\) such that \(C\in\mathcal{C}_{r_C}\). We then construct a triangle detection instance on a graph **T** with O(_n_log_n_) vertices defined as follows:

The vertex set of **T** is C.

For every non-edge \(\{a,b\}\notin E\), we add an edge between _C<sub>a</sub>(b_) and _C<sub>b</sub>(a_) in **T** if and only if _r<sub>C<sub>a</sub>(b_)</sub>=_a_ and _r<sub>C<sub>b</sub>(a_)</sub>=_b_.

Finally, we report that **G** is AT-free if and only if **T** is triangle-free.

\(\blacksquare\)

