## 2 Improved Approximation for Coloring 3-Colorable Graphs

### 2.1 Independent Set

In this section, we prove the following lemma providing an approximation algorithm for finding an independent set in a 3-colorable graph:

**Lemma 2.1.** _Given a 3-colorable graph G_=(_V,E_) _and a parameter_ \(r\in\mathbb{Z}_{>0}\)_, there exists an algorithm that, with probability at least_ 1/2_, outputs an independent set of size at least_ \(\alpha(G)/r\) _in time_ \(O^*\left(exp\left(\tilde{O}\left(\frac{nlog^{5/2}r}{r^3}\right)\right)\right)\).

We use the following lemma from \[3\].

**Lemma 2.2** (\[3\])**.** _Let_ \(\mathcal{A}(G')\) _be an approximation algorithm that outputs an independent set of_ \(G'\) _of size_ \(\alpha(G')/r\)_. Suppose_ \(\mathcal{A}(G')\) _runs in time_ \(T_\mathcal{A}(n',r)\) _(where_ \(n'=|V(G')|\)_) when G has maximum degree d(r), where_ \(d(r)\ge 2r\)_. Then, there is an algorithm that given any graph G, outputs an independent set of G of expected size_ \(\alpha(G)/r\) _in expected time_ \(O^*\left(exp\left(\frac{n}{d(r)}log(4d(r)/r)\right)T_\mathcal{A}(n,r)\right)\).

We note that the algorithm of \[3\] only calls \(\mathcal{A}(G')\) on graphs \(G'\) obtained by deleting vertices and edges from _G_. Therefore, if _G_ is 3-colorable, we can assume \(G'\) is as well. The seminal work of Karger, Motwani, and Sudan \[18\] provides a polynomial time algorithm to color 3-colorable graphs using _O(d_<sup>1/3</sup>log<sup>1/2</sup>_d_log_n_) colors, where _d_ is the maximum degree of the input graph. We will use the following lemma from their analysis:

**Lemma 2.3** (\[18\])**.** _Given a_ 3_-colorable graph G, there exists a polynomial time algorithm to find an independent set of size_ \(\Omega(n/(d^{1/3}\sqrt{logd}))\)_, where d is the maximum degree of the input graph._

Combining these two results, we obtain the following corollary:

**Corollary 2.4.** _Given a_ 3_-colorable graph G, there exists a polynomial time algorithm that outputs an independent set of expected size_ \(\alpha(G)/r\) _in expected time_ \(O^*\left(exp\left(\tilde{O}\left(\frac{nlog^{5/2}r}{r^3}\right)\right)\right)\).

_Proof._ We refer to the algorithm given by Lemma 2.3 as A. By Lemma 2.3, for any 3-colorable graph \(G'\) with maximum degree \(d=\frac{r^3}{log^{3/2}r}\), \(\mathcal{A}(G')\) outputs an independent set of size

\(\Omega\left(\frac{n}{d^{1/3}\sqrt{logd}}\right)=\Omega\left(\frac{n\sqrt{log(r)}}{r\sqrt{log(r/logr)}}\right).\)

Note that since \(G'\) is 3-colorable, \(\alpha(G')\ge n/3\). Thus we can choose \(d(r)=\tilde{O}(r^3/log^{3/2}r)\) so that \(\mathcal{A}(G')\) outputs an independent set of size \(\alpha(G')/r\) in polynomial time (recall here that \(\tilde{O}\) suppresses polyloglog(_r_) factors).

We then apply Lemma 2.2 on the input _G_ with \(\mathcal{A}(G')\) as defined above to obtain an independent set of expected size \(\alpha(G)/r\) in expected time

\(O^*\left(exp\left(\frac{nlog^{3/2}r}{r^3}log\left(\frac{4r^3}{rlog^{3/2}r}\right)\right)poly(n)\right)=O^*\left(exp\left(\tilde{O}\left(\frac{nlog^{5/2}r}{r^3}\right)\right)\right).\)

