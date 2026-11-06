<tbc>Since consecutive values of _r<sub>i</sub>_ differ by a factor of \(1+1/\alpha\), the edge (_s,x_) can belong to at most \(1+log_{1+1/\alpha} R_{\beta^\prime}\le 8\) sets \(E_{s,i}^\star\). Hence<tbc>

\(\sum_{i=0}^LOPT_{i,s}\le\sum_{i=0}^L|E_{s,i}^\star|\le 8|E_s^\star|.\)

<tbc>Combining this with Claim 2.7,

\(|E_s|\le\sum_{i=0}^L|E_s^i|\le(lnn+1)\sum_{i=0}^LOPT_{i,s}\le 8(lnn+1)|E_s^\star|.\)

Summing over all sources \(s\in P\) gives \(|E|\le 8(lnn+1)|E^\star|\).

### 2.6 Combining the Two Constructions.

_Proof of Theorem 1.4._ Run both Algorithm 2.3 and Algorithm 2.4, and return the graph with fewer edges. By Lemma 2.2, both candidate graphs are \(\alpha\)-navigable, so the returned graph is also \(\alpha\)- navigable. If _G_<sub>const</sub> is the graph returned by Algorithm 2.3 and _G_<sub>log</sub> is the graph returned by Algorithm 2.4, then the final output _G_ satisfies

\(|E(G)|\le|E(G_\mathrm{const})|\text{and}|E(G)|\le|E(G_\mathrm{log})|.\)

Therefore Lemma 2.3 gives the \((\alpha,2\alpha+8+4/\alpha)\)-bicriteria 5-approximation guarantee, and Lemma 2.6 gives the \((\alpha,\alpha+5+2/\alpha)\)-bicriteria _O_(ln_n_)-approximation guarantee. The running time remains \(\tilde{O}(\alpha n^2log\Delta)\), which is \(\tilde{O}(n^2log\Delta)\) for constant \(\alpha\).

## 3 Hardness Proof.

In this section we prove Theorem 1.5. We reduce Set Cover to \((\alpha,2\alpha-\eta)\)-bicriteria approximation of \(\alpha\)-navigable graphs on metric point sets.

**Lemma 3.1** (\[DS13\])**.** _Let_ (U,F) _be a set cover instance with n elements and m=n<sup>d</sup> sets for some constant d=O_(1)_. It is NP-hard to compute a_ \(\frac{1}{2}lnn\)_-approximation of minimum set cover._

_Proof of Theorem 1.5._ Fix constants \(\alpha\ge 1\) and \(\eta\in(0,1)\). Let (U,F) be a hard Set Cover instance from Lemma 3.1, with _n_ elements and \(m\le n^d\) sets for a constant _d=O_(1). We may assume that the instance is feasible and that its optimum value |_C<sup>⋆</sup>_| is at least 20: if |_C<sup>⋆</sup>|\<_20, then the optimum can be found by exhaustive search over all subsets of at most 19 sets, which takes polynomial time because _d_ is a constant.

### Reduction from Set Cover to \((\alpha,2\alpha-\eta)\)-Bicriteria Approximation.

Let<tbc>

\(K=\left\lceil\frac{2(m+n+1)}{\eta}\right\rceil.\)

<tbc>We create _K_ disjoint copies of the Set Cover instance, denoted by (U_<sub>i</sub>,_F_<sub>i</sub>_) for \(1\le i\le K\). We represent each set and each element by a distinct vertex, using the same notation for the vertex and the object it represents. For each copy _i_, we also introduce a unique hub point _c<sub>i</sub>_, and write<tbc>

\(P_i=\{c_i\}\cup\mathcal{F}_i\cup\mathcal{U}_i,P=\bigcup_{i=1}^KP_i.\)

