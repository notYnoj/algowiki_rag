This allows us to define the following divide-et-impera scheme that we will use to solve SED.

We write \((s,s',q,q')\)-DISED to denote an instance of the DISED Problem with input \(s<q\in\mathbf{S}\) and \(s'<q'\in\mathbf{S}'\).

Given an \((s,s',q,q')\)-DISED instance, we define its _size_ as

\(max\left\{|\mathsf{sub}(s)\backslash\mathsf{sub}(q)|,|\mathsf{sub}(s')\backslash\mathsf{sub}(q')|\right\},\)

and _global tree size_ as

\(min\left\{|\mathsf{sub}(s)|,|\mathsf{sub}(s')|\right\}.\)

We make two further remarks about an \((s,s',q,q')\)-DISED instance. First, input and output of an \((s,s',q,q')\)-DISED of size _m_ are of order O(_m_<sup>2</sup>). Second, there exist two types of symmetry in the DISED Problem:

(**a**) swapping the role of **F** and \(\mathbf{F}'\) does not change the input/output of the problem, we refer to this symmetry as _swap symmetry_; and

(**b**) reversing **F** and \(\mathbf{F}'\) does not change the input/output of the problem, we refer to this symmetry as _reverse symmetry_.

These symmetries help simplify computations, reducing the need for different computations in symmetric cases.

## 5.1 Algorithm for DISED

In the following (sub)section, we present a divide-et-impera algorithm ADISED solving DISED. The following two lemmas, the proof of which we defer to Section 5.3 and Section 5.4, motivate such an approach.

**Lemma 5.2.** _Consider an_ \((s,s',q,q')\)_-DISED instance of size m such that s immediately precedes q or s’ immediately precedes q’. Then, we can solve the_ \((s,s',q,q')\)_-DISED instance in time_ O(T<sub>_MUL_</sub>(_m_)+_m_<sup>2+_o_(1)</sup>).

_Furthermore, if the DISED instance is unweighted and has global tree size_ D_, then the algorithm takes time_ O(T<sub>_MonMUL_</sub>(_m,m,m,_D)+_m_<sup>2+_o_(1)</sup>_g_(D)) _where_ T<sub>_MonMUL_</sub>(_m,m,m,_D)=O(_f(m)g_(D)) _for some functions f,g._

**Lemma 5.3.** _Suppose we are given an_ \((s,s',q,q')\)_-DISED instance of size m, and let_ \(r\in\mathbf{S}\) _be such that s\<r\<q. Then, we can reduce the_ \((s,s',q,q')\)_-DISED instance to the_ \((s,s',r,q')\)_-DISED and_ \((r,s',q,q')\)_-DISED instances in time_ O(T<sub>_MUL_</sub>(_m_)+_m_<sup>2+_o_(1)</sup>).

_Furthermore, if the DISED instance is unweighted and has global tree size_ D_, then the reduction takes time_ O(T<sub>_MonMUL_</sub>(_m,m,m,_D)+_m_<sup>2+_o_(1)</sup>_g_(D)) _where_ T<sub>_MonMUL_</sub>(_m,m,m,_D)=O(_f(m)g_(D)) _for some functions f,g._

Divide-et-Impera Spine Edit Distance (DISED)
Input: s < q < S, s' < q' < S' and
(i) sim(F[ x .. y ), F'[ x' .. y' )) for all (x, x') ∈ B1 (s, s' , q, q') and (y, y') ∈ B1 (s, s' , q, q').
(ii) sim(F[ x .. y ), sub(q')) for all x, y ∈ [ l(s) .. l(q) ].
(iii) sim(F[ x .. y ), sub(q')) for all x, y ∈ [ r(q) .. r(s) ].
(iv) sim(sub(q), F'[ x' .. y' )) for all x', y' ∈ [ l(s') .. l(q') ].
(v) sim(sub(q), F'[ x' .. y' )) for all x', y' ∈ [ r(q') .. r(s') ].
Output: The values
(i) sim(F[ x .. y ), F'[ x' .. y' )) for all (x, x') ∈ B1 (s, s' , q, q') and (y, y') ∈ B1 (s, s' , q, q').

