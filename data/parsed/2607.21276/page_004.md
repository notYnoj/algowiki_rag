We say that (_P,p(n_)) _fine-grained reduces_ to (_Q,q(n_)) and write \((P,p(n))\le(Q,q(n))\) if \((P,p(n))\le_\delta(Q,q(n))\) for some function \(\delta:\mathbb{R}_{>0}\rightarrow\mathbb{R}_{>0}\).

If \((P,p(n))\le(Q,q(n))\), then any improvement over the running time _q(n_) for the problem _Q_ implies an improvement over the running time _p(n_) for the problem _P_: for any \(\varepsilon>0\), there is \(\delta>0\), such that if _Q_ can be solved in time \(O(q(n)^{1-\varepsilon})\), then _P_ can be solved in time \(O(p(n)^{1-\delta})\).

### 2.2 Standard Hardness Hypotheses

The most frequently used hardness assumptions in fine-grained reductions are the following.

**SETH:** for every \(\varepsilon>0\), there exists _k_ such that _k_-SAT cannot be solved in time \(O(2^{(1-\varepsilon)n})\).

**3-SUM Hypothesis:** for every \(\varepsilon>0\), 3-SUM cannot be solved in time \(O(n^{2-\varepsilon})\).

**APSP Hypothesis:** for every \(\varepsilon>0\), APSP cannot be solved in time \(O(n^{3-\varepsilon})\).

### 2.3 Efficient Self-reducibility

Here, we formalize the notion of efficient self-reducibility as a fine-grained reduction from a problem to smaller instances of the same problem. This notion may be viewed as a fine-grained version of the notion of strong downward self-reducibility introduced in \[11\].

**Definition 2.** _Let P be a problem and_ \(p:\mathbb{Z}_{\ge 0}\rightarrow\mathbb{Z}_{\ge 0}\) _be a non-decreasing function. We say that P is_ efficiently self-reducible for _p(n), if for any_ \(0<\alpha<1\) _there exists a fine-grained reduction_ \((P,p(n))\le(P,p(n))\) _such that the size_ \(n'\) _of every instance solved by an oracle satisfies_

\(p(n')\le p(n)^\alpha.\) (1)

In a sense, efficient self-reducibility says that to solve _P_ faster than in _p(n_) time, it suffices to design a faster than _p(n_) time algorithm for small size instances.

It is known that problems from popular hardness assumptions satisfy this property.

• SAT is efficiently self-reducible for 2_<sup>n</sup>_: branch on all but \(\alpha n\) variables to get \(2^{n(1-\alpha)}\) instances each depending on \(\alpha n\) variables (inequality (1) turns into \(2^{\alpha n}\le(2^n)^\alpha\)).<tbc>

• APSP is efficiently self-reducible for _n_<sup>3</sup> as APSP is equivalent to min-plus matrix multiplication: to multiply two \(n\times n\)-matrices, break them into \(n^\alpha\times n^\alpha\)-matrices; then, it remains to multiply \(n^{3-3\alpha}\) matrices of size \(n^\alpha\times n^\alpha\) (inequality (1) turns into \((n^\alpha)^3\le(n^3)^\alpha\)).<tbc>

• 3-SUM is efficiently self-reducible for _n_<sup>2</sup>: an instance of size _n_ can be reduced to \(O(n^{2-2\alpha})\) instances of size \(n^\alpha\) as shown in \[15\] (inequality (1) turns into \((n^\alpha)^2\le(n^2)^\alpha\)).

## 3 Impossibility of Reductions to Exponentially Hard Problems

In this section, we prove the main result: if Edge Coloring is \(\alpha^{n^2}\)-hard under SETH, then SETH is false. We then generalize this result by replacing Edge Coloring with any problem whose conjectured bound is truly exponential in terms of the input bit-length and SAT with any self-reducible problem. The main idea of the proof is the following. Using a reduction from SAT to Edge Coloring, we design an algorithm that solves SAT faster than in 2_<sup>n</sup>_. To this end, similarly to the Method<tbc>

