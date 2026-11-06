<tbc>_u_<sub>1</sub>_,...,u<sub>n</sub>_ a nonzero sequence if \(u_\ell\neq 0\) for some \(1\le\ell\le n\). We use _e<sub>A</sub>(w_) to denote the smallest natural number _i_ such that \(\sum_{j=1}^mw(a_j)a_j^i\) is nonzero in Z_/p_Z. We have the following conclusion.

**Lemma 2.1.** _Let A, w and e<sub>A</sub>(w_) _be as above. Then_<tbc>

\(e_A(w)\le|A|-1.\)

<tbc>_Proof._ It is proved by contradiction. Suppose that \(e_A(w)\ge|A|\). This means

\(\sum_{j=1}^mw(a_j)a_j^i=0\) (2.1)

for all \(0\le i\le m-1\).

The (coefficients) matrix _M_ is defined to be<tbc>

\(M=(a_j^{i-1})_{1\le i\le m}.\) (2.2)

<tbc>Note that<tbc>

\(det(M)=\prod_{1\le i<j\le m}(a_j-a_i).\)

<tbc>Since _a_<sub>1</sub>_,...,a<sub>m</sub>_ are pairwise distinct in Z_/p_Z, det(_M_) is nonzero. Consider the system of linear equations

\(M\mathbf{x}=\mathbf{0},\) (2.3)

where **x**=(_x_<sub>1</sub>_,...,x<sub>m</sub>)<sup>T</sup>_ and **0**=(0_,...,_0)_<sup>T</sup>_.

On one hand, (2.3) has only the zero solution due to the fact that det(_M_) is nonzero. On the other hand, (_w(a_<sub>1</sub>)_,...,w(a<sub>m</sub>_))_<sup>T</sup>_ is a solution to (2.3) in view of (2.1). This is a contradiction since \(w(a_\ell)\) is nonzero in Z_/p_Z for some \(1\le\ell\le m\). This completes the proof. □

The inequality in Lemma 2.1 is sharp since we have the following.

**Lemma 2.2.** _Let A_={_a_<sub>1</sub>_,...,a<sub>m</sub>_} _be a subset of_ Z_/p_Z _with_ \(m\ge 2\)_. Then there exists a nonzero sequence w(a_<sub>1</sub>)_,...,w(a<sub>m</sub>_) _such that_<tbc>

\(e_A(w)=|A|-1.\)

<tbc>_Proof._ The proof is similar to that of Lemma 2.1. Let _M_ be as in (2.2). Now consider the linear equations

\(M\mathbf{x}=\mathbf{b},\) (2.4)

where **x**=(_x_<sub>1</sub>_,...,x<sub>m</sub>)<sup>T</sup>_ and **b**=(0_,...,_0,1)_<sup>T</sup>_. Since det(_M_) is nonzero, (2.4) has a unique solution (_w_<sub>1</sub>_,...,w<sub>m</sub>)<sup>T</sup>_. Since **b** is a nonzero vector, (_w_<sub>1</sub>_,...,w<sub>m</sub>)<sup>T</sup>_ is also a nonzero vector. In particular, we have

