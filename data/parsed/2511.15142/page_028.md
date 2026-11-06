_Proof._ Suppose for contradiction that the claim fails, and let _k_ be the smallest integer for which a counterexample exists. The statement is trivial for _k_=1, so \(k\ge 2\). Let \(\sigma=(y_1,\dots,y_{k+1})\) be such a minimal counterexample. Then there exist distinct subsets \(S,T\subseteq[k]\) satisfying

\(\sum_{i\in S}(y_{i+1}-y_i)=\sum_{i\in T}(y_{i+1}-y_i).\)

By minimality, the symmetric difference \(S\triangle T\) must contain _k_; otherwise, restricting to the first _k_-1 elements would yield a smaller counterexample. Without loss of generality, assume \(k\in S\) and define \(S'=S\backslash\{k\}\).

Rearranging gives<tbc>

\(y_{k+1}-y_k=\sum_{i\in[k-1]}\big(\unknown_{S^\prime}(i)-\unknown_T(i)\big)(y_{i+1}-y_i).\)

<tbc>Substituting into the telescoping sum<tbc>

\(y_{k+1}-y_1=(y_{k+1}-y_k)+\sum_{i\in[k-1]}(y_{i+1}-y_i),\)

<tbc>we obtain

\(y_{k+1}-y_1=\sum_{i\in[k-1]}\big(1+\unknown_{S^\prime}(i)-\unknown_T(i)\big)(y_{i+1}-y_i),\)

so _y_<sub>_k_+1</sub>-_y_<sub>1</sub> lies in the conic hull of {_y_<sub>2</sub>-_y_<sub>1</sub>_,...,y<sub>k</sub>-y_<sub>_k_-1</sub>}, contradicting the conic independence of \(\sigma\).

**Lemma A.6** (\[KLMZ17\])**.** _The conic dimension of any subset of_ {0,1}_<sup>d</sup> is at most O(d_log_d). In fact, it is the smallest k such that_ 2_<sup>k</sup>\>_(2_k_+1)_<sup>d</sup>._

_Proof._ Let \(\sigma=(y_1,\dots,y_{k+1})\) be a conically independent sequence of Boolean points. By Lemma A.5, the 2_<sup>k</sup>_ subset sums

\(\sum_{i\in S}(y_{i+1}-y_i),S\subseteq[k],\)

are all distinct. Each such sum is an integer vector in \[-_k,k\]<sup>d</sup>_, of which there are at most (2_k_+1)_<sup>d</sup>_ possibilities. Hence \(2^k\le(2k+1)^d\), implying that _k=O(d_log_d_).

## A.3 Beyond the Hypercube

In this section, we consider extensions of the above claim for the Boolean hypercube: to the setting of hypergrids, and to getting \(\varepsilon\)-approximate solutions for other bounded sets.

### Hypergrids and Bounded-Precision Solutions

A more general version of Lemma A.6 when points belong to {0,1_,...,N_-1}_<sup>d</sup>_ shows that the conic dimension is shown to be at most _O(d_log(_Nd_)). The proof is very similar to that of Lemma A.6 above; see \[KLMZ17, Lemma 4.2\].

### \(\varepsilon\)-Approximate Solutions for Bounded Sets

For bounded sets \(\mathcal{P}\subset\mathbb{B}_d=\{x\in\mathbb{R}^d;\|x\|_2\le 1\}\) it is possible to bound an approximate version of the conic dimension, which leads to an algorithm that returns an \(\varepsilon\)-approximate point. Given a comparison oracle, the algorithm returns \(\widehat{x}\in\mathcal{P}\) such that \(\langle w^*,\widehat{x}\rangle\le\langle w^*,x\rangle+\varepsilon\) for all \(x\in\mathcal{P}\).

For the following definition, we will use the notion of the distance: given a set \(S\subset\mathbb{R}^d\) and a point \(x\in\mathbb{R}^d\), define \(\mathrm{dist}(x,S)=\mathrm{min}_{y\in S}\|x-y\|_2\).

