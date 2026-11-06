### Conclusion.

We have shown \(\text{Iso-}\mathsf{Gl}\in\mathsf{Gl}\) and \(\mathsf{Gl}\le_m\text{Iso-Gl}\), therefore Iso-Gl is Gl-complete.

We conclude this section by showing that the promise problem is at most as hard as Gl independent of the problem it is based on.

**Lemma 9.11.** _Let_ \(\Pi\) _be a decision problem. Then_ Iso-\(\Pi\) _is in_ Gl.

_Proof._ We give a polynomial-time many-one reduction from Iso-\(\Pi\) to Gl.

On input (_I,J_), output the pair (_I,J_) as an instance of Gl (i.e., the question whether \(I\cong J\)). This mapping is polynomial time.

We claim it is correct under the promise defining Iso-\(\Pi\). If \((I,J)\in\text{Iso-}\Pi_\mathrm{YES}\), then \(J\cong I\), hence (_I,J_) is a YES-instance of Gl. If \((I,J)\in\text{Iso-}\Pi_\mathrm{NO}\), then \(I\in\Pi\) and \(J\notin\Pi\). Since \(\Pi\) is isomorphism-invariant, \(J\cong I\) would imply \(J\in\Pi\), a contradiction; hence \(J\unknown\cong I\), and (_I,J_) is a NO-instance of Gl.

Therefore, deciding \((I,J)\in\mathsf{Gl}\) decides \((I,J)\in\text{Iso-}\Pi\), and thus Iso-\(\Pi\le_m\mathsf{Gl}\), i.e. Iso-\(\Pi\) is in Gl.

## 9.3 Isomorphism-Preserving Reductions

A tool we use to show the hardness is isomorphism-preserving reductions

**Definition 9.12.** We call a function _R_ that maps instances of \(\Pi\) to instances of \(\Pi'\) an _isomorphism- preserving reduction_ if:

• _R_ is polynomial time computable.<tbc>

• _R_ is _correct_, that is \(I\in\Pi\) is a YES-instance of \(\Pi\) if and only if _R(I_) is a YES-instance of \(\Pi'\).<tbc>

• _R_ is _isomorphism-preserving_, that is if \(I_1,I_2\in\Pi\) are isomorphic in \(\Pi\) then _R(I_<sub>1</sub>)_,R(I_<sub>2</sub>) are isomorphic in \(\Pi'\).

We write \(\Pi\le_p^\cong\Pi'\) if such a reduction exits. Further, we say that a problem \(\Pi'\) is Gl-hard if \(\mathsf{Gl}\le_p^\cong\Pi'\).

The property of isomorphism-preserving reductions is that they can be used to show Gl-hardness of promise problems.

**Lemma 9.13.** _Let_ \(\Pi\) _and_ \(\Pi'\) _be decision problems. If_ Iso-\(\Pi\) _is_ Gl_-hard and_ \(\Pi\le_p^\cong\Pi'\)_, then_ Iso-\(\Pi'\) _is_ Gl_-hard._

_Proof._ Since Iso-\(\Pi\) is Gl-hard, there exists a polynomial-time reduction \(g:\mathsf{Gl}\le_m\text{Iso-}\Pi\).

It therefore suffices to give a polynomial-time reduction \(f:\text{Iso-}\Pi\le_m\text{Iso-}\Pi'\).

Let (_I,J_) be an instance of Iso-\(\Pi\). Since \(\Pi\le_p^\cong\Pi'\), there exists an isomorphism-preserving many-one reduction _R_ from \(\Pi\) to \(\Pi'\). Define

\(f(I,J):=(R(I),R(J)).\)

We check that _f_ maps promised instances to promised instances and preserves YES/NO.

### YES case.

If \((I,J)\in\text{Iso-}\Pi_\mathrm{YES}\), then \(I\in\Pi\) and \(J\cong I\). By correctness, \(R(I)\in\Pi'\), and by isomorphism preservation, \(R(J)\cong R(I)\). Hence \(f(I,J)\in\text{Iso-}\Pi'_\mathrm{YES}\).

