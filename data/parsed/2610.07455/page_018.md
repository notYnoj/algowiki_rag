_Proof of Lemma 4.2._ Given a stream of _R_-constraints, replace each arriving constraint by the _R<sup>⋆</sup>_- constraint on the same scope and run an algorithm for _R<sup>⋆</sup>_. By Lemma 4.3, the final instance has the same two optimum values and is satisfiable exactly when the original instance is satisfiable. Conversely, replace every _R<sup>⋆</sup>_-constraint by the _R_-constraint on the same scope and use the same lemma again. Both transformations use only constant extra space and preserve the number of variables and constraints, the stream order, and simplicity. Finally, if _R_ is symmetric, then \(R^\star=R\cap C^k\) is symmetric as well.

Thus, from this point on, we may reduce to the core before proving any upper or lower bound.

## 4.2 Hard pinnings in a core relation

For the satisfiability lower bound, Bob will want to force the variables to a chosen witness assignment _s_. Ordinary _R_-constraints may not be able to distinguish _s_ from \(\sigma\circ s\) for an automorphism \(\sigma\), but this ambiguity is harmless by Observation 4.1. The next lemma shows that this is the only ambiguity we need to keep.

**Lemma 4.4** (Hard pinning)**.** _Let_ \(R\subseteq D^k\) _be a core relation, let X be a set of variables, and let_ \(s:X\rightarrow D\)_. There is an R-instance P<sub>s</sub> on X and O<sub>R</sub>_(1) _additional variables such that_

\(\{\alpha|_X:\alpha\in\mathrm{Sat}(P_s)\}=\{\sigma\circ s:\sigma\in\mathrm{Aut}(R)\}.\)

_Moreover, P<sub>s</sub> has O<sub>R</sub>_(|_X_|+1) _constraints._

The proof uses the following property of cores. Changing one domain value to another must make some tuple leave the relation.

**Lemma 4.5.** _Let_ \(R\subseteq D^k\) _be a core relation. For every distinct_ \(a,b\in D\)_, there is a tuple_ \(r=(r_1,\dots,r_k)\in R\) _and a coordinate_ \(t\in[k]\) _such that r<sub>t</sub>=a and_ \(r^{t\leftarrow b}\notin R\).

_Proof._ Define \(\sigma:D\rightarrow D\) by \(\sigma(a)=b\) and \(\sigma(c)=c\) for \(c\neq a\). The map \(\sigma\) is not injective, so it cannot be an endomorphism of the core relation _R_. Choose \(r\in R\) such that \(\sigma(r)\notin R\), and replace the occurrences of _a_ in _r_ by _b_ one at a time. The initial tuple is in _R_ and the final tuple is not, so at some first replacement we obtain a tuple outside _R_. Immediately before that replacement we have a tuple \(r'\in R\) with \(r'_t=a\), while \((r')^{t\leftarrow b}\notin R\). This is the required tuple.

We now build the hard-pinning instance. Intuitively, we introduce additional variables to represent the values of _D_, and a group of constraints forces their assigned values to form one automorphism of _R_.

_Proof of Lemma 4.4._ The first step is to introduce extra variables that represent the values in the domain, up to one common automorphism. For CUT, these are two adjacent variables, so they must receive opposite values. More formally, for every \(a\in D\), introduce an extra variable _y<sub>a</sub>_. For every tuple \(r=(r_1,\dots,r_k)\in R\), add the constraint _R(y_<sub>_r_<sub>1</sub></sub>_,...,y<sub>r<sub>k</sub></sub>_). Next, we add constraints that pin the variables in _X_ to _s_ up to the same automorphism. For every \(x\in X\), every \(r\in R\), and every \(t\in[k]\) with _r<sub>t</sub>=s(x_), also add _R(y_<sub>_r_<sub>1</sub></sub>_,...,y_<sub>_r<sub>t</sub>_-1</sub>_,x,y_<sub>_r<sub>t</sub>_+1</sub>_,...,y<sub>r<sub>k</sub></sub>_). Call the resulting instance _P<sub>s</sub>_. It uses |_D_|=_O<sub>R</sub>_(1) extra variables and _O<sub>R</sub>_(|_X_|+1) constraints.

We now prove that the added constraints give the required hard pinning. Let \(\alpha\) satisfy _P<sub>s</sub>_ and define \(\sigma:D\rightarrow D\) by \(\sigma(a)=\alpha(y_a)\). The first family of constraints shows that \(\sigma(r)\in R\) for every \(r\in R\), so \(\sigma\) is an endomorphism of _R_. Since _R_ is a core, \(\sigma\) is an automorphism. Fix \(x\in X\), put _a=s(x_), and let \(b=\sigma^{-1}(\alpha(x))\). Suppose \(b\neq a\). By Lemma 4.5, there are \(r\in R\) and \(t\in[k]\) such<tbc>

