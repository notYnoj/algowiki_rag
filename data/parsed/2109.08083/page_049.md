<tbc>Note that this allows us to describe _L_<sup>∗</sup> as the difference of two matchings _M_<sup>+</sup> and _M_<sup>-</sup> such that \(|M^\pm|=O\left(p_Ln^{2.6\times 10^{-5}}\right)\), and all vertices covered by the matchings are within the interval \(I'_{n^{2.61\times 10^{-5}}}\).

## 4.2. Building and using the absorber

In this section we build an absorber \(A^*\supseteq A\) that is an absorber for any qualifying leave _L_<sup>∗</sup>. Let \(A\subseteq I'_{n^{10^{-4}}}\) so that every vertex in the interval is included inde pendently with probability _p<sub>A</sub>_ as defined in Definition 3.5. Let \(A':=A\cap I'_{n^{2.7\times 10^{-5}}}\). The initial step to showing this is to prove the following:

Lemma 4.6. _Given A as above and qualifying leave L_<sup>∗</sup>_, whp there exists_ \(\Phi_l\in\{-1,0,1\}^{E(\mathcal{T})}\) _such that_ \(\partial\Phi_l-L^*:=\mathbf{0}\) _and_ \(\partial\Phi_l^-\subseteq A'\).

That is, we show that given _A_ as above, whp we can describe _L_<sup>∗</sup> as the vertex shadow of two matchings \(M_A^+\) and \(M_A^-\) such that \(\bigcup M_A^-\subseteq A'\). We’ll do this as follows: let \(\Phi\) be a signed multi-set of edges obtained from covering the leave _L_<sup>∗</sup> such that every edge is contained in the interval \(I'_{n^{10^{-5}}}\), and \(|\Phi|=O\left(p_Ln^{2.6\times 10^{-5}}\right)\) as per Lemma 4.1. By Lemma 4.5, we obtain _M_<sup>+</sup> and _M_<sup>-</sup>, two matchings in the interval \(I'_{n^{2.61\times 10^{-5}}}\), such that \(\partial(M^+-M^-)=L^*\), and \(|M^-|=O\left(p_Ln^{2.6\times 10^{-5}}\right)\). Let _B_={_v_<sub>1</sub>_,...,v<sub>l</sub>_} be an enumeration of the vertices in \(\bigcup M^-\), such that vertices are enumerated according to part in the order _V_<sup>_X-Y_</sup>_,V_<sup>_X+Y_</sup>_,V<sup>Y</sup>,V<sup>X</sup>_. We know that \(B\subseteq I'_{n^{2.61\times 10^{-5}}}\) and that \(|B|=O\left(p_Ln^{2.6\times 10^{-5}}\right)\). For each \(v_i\in B\) there is a pair of oppositely signed edges \((e_i^+,e_i^-)\in M^+\times M^-\) such that \(e_i^+\cap e_i^-=\{v_i\}\). Given such a pair \((e_i^+,e_i^-)\), let \(Z_{(e_i^+,e_i^-)}\) be the collection of zero-sum configurations which contain \(e_i^+\) with negative sign, \(e_i^-\) with positive sign, and additionally satisfy the following: if \(v_i\in V^{X-Y}\) then all vertices are contained in \(I'_{n^{2.7\times 10^{-5}}/64}\), if \(v_i\in V^{X+Y}\) then all vertices are contained in \(I'_{n^{2.7\times 10^{-5}}/16}\), if \(v_i\in V^Y\) then all vertices are contained in \(I'_{n^{2.7\times 10^{-5}}/4}\), and if \(v_i\in V^X\) then all vertices are contained in \(I'_{n^{2.7\times 10^{-5}}}\).1

Let \(\Phi_1\in\{-1,0,1\}^{E(\mathcal{T})}\) be the vector of edges such that \(\Phi_1^+=M^+\) and \(\Phi_1^-=M^-\) We update _M_<sup>-</sup> to \(M_A^-\) via the following algorithm:

Algorithm 4.7.

_i_=1

**Input:** \((e_i^+,e_i^-)\), \(\Phi_i\).

**Step 1:** Enumerate the number of zero-sum configurations \(Z_{(e_i^+,e_i^-)}^*\) which are in \(Z_{(e_i^+,e_i^-)}\) and additionally use only vertices in \(A'\), other than those in \(e_i^+\cup e_i^-\), such that all vertices used are distinct from \(\partial\Phi_i^+\).

**Step 2:** If \(|Z_{(e_i^+,e_i^-)}^*|=0\), abort. Else, uniformly at random assign one of the \(|Z_{(e_i^+,e_i^-)}^*|\) such zero-sum configurations \(z_{(e_i^+,e_i^-)}\) to \((e_i^+,e_i^-)\).

**Step 3:** If _i=l_ stop. Else, let \(\Phi_{i+1}=\Phi_i\cup z_{(e_i^+,e_i^-)}\) and for each _j\>i_ update \((e_j^+,e_j^-)\) according to \(\Phi_{i+1}\). Increase _i_ by 1 and go to Step 1.

1We do this so that we don’t have to worry about zero-sum configurations ‘pushing out’ rather than in, which reduces case analysis.

