Therefore, assume |_L<sub>B</sub>(P_)|_\>_0 and denote _B(P_)={_x_<sub>0</sub>_,x_<sub>1</sub>_,...,x<sub>t</sub>_}. Since \(\ell(v)\le\ell(u)\), \(x_2\neq u\). Consider the sub-path _P_<sub>_v,x_<sub>2</sub></sub>=_P_<sub>_x_<sub>1</sub>_,x_<sub>2</sub></sub>. Then, the set \(L_B(P_{v,x_2})\subset L_B(P)\) by Lemma A.1 and \(\ell(x_2)\in L_B(P)\backslash L_B(P_{v,x_2})\) so that _L<sub>B</sub>(P_) is strictly larger. By the inductive hypothesis, in the \(\ell(v)\)-th iteration of Algorithm 12,

\(\hat{\delta}_{\ell(v)}(v^*,u)\le(\hat{\delta}_{\ell(x_2)}(x_2^*,v)+1)+\delta(x_2,u)+1\)<br>
\(\le\delta(x_2,v)+2|L_B(P_{v,x_2})|+\delta(x_2,u)+3\)<br>
\(\le\delta(u,v)+2|L_B(P)|+1\)

When \(v\in D_{\ell(v)}\),

\(\hat{\delta}(v,u)\le\hat{\delta}_{\ell(x_2)}(x_2^*,v)+1+\delta(x_2,u)\)<br>
\(\le\delta(x_2,v)+2|L_B(P_{x_1,x_2})|+\delta(x_2,u)+2\)<br>
\(\le\delta(v,u)+2|L_B(P)|\)

Now, let \(j\ge\ell(v)\) and \(v\in D_j\). If |_L<sub>B</sub>(P,j_)|=0, then \(P\subset E_j\) and we compute an exact distance in the _j_-th iteration. Otherwise, let _b=b(v,P_) and \(b^*\in D_{\ell(b)}\) where \(\ell(b)<j\) so that,

\(\hat{\delta}_j(v,u)\le\hat{\delta}_{\ell(b)}(v,b^*)+1+\delta(b,u)\)<br>
\(\le\delta(v,b)+2|L_B(P_{b,v})|+2+\delta(b,u)\)<br>
\(\le\delta(u,v)+2|L_B(P,j)|\)

where we have used the inductive hypothesis and \(L_B(P_{b,v})\subset L_B(P,j)\) and \(\ell(b)\in L_B(P,j)\backslash L_B(P_{b,v})\).

In many cases for our algorithms, it suffices to use the following weaker lemma. Here, we bound the additive error simply by the number of levels occurring in the shortest path, whereas above the notion of blocking vertices takes into account the specific positions where each level occurs.

**Lemma A.3.** _Let u,v be vertices in a graph G and P be a shortest path between u,v. Suppose_ \(\ell(v)\le\ell(u)\).

_For_ \(j\ge\ell(v)\)_, let_ \(L(P,j)=\{\ell(w)\text{\textit{s.t.}}w\in P\text{\textit{and}}\ell(w)<j\}\) _and let_ \(L(P)=L(P,\ell(v))=\{\ell(w)\text{\textit{s.t.}}w\in P\text{\textit{and}}\ell(w)<\ell(v)\}\)_. Then, Algorithm 12 in the_ \(\ell(v)\)_-th iteration computes distance estimate_ \(\hat{\delta}\) _such that,_<tbc>

\(\delta(v^*,u)\le\hat{\delta}_{\ell(v)}(v^*,u)\le\delta(v,u)+2|L(P)|+1\)

<tbc>_Furthermore, for_ \(j\ge\ell(v)\) _such that_ \(v\in D_j\),

\(\hat{\delta}_j(v,u)\le\delta(v,u)+2|L(P,j)|\)

_Proof._ This follows from Lemma A.2 as \(L_B(P,j)\subset L(P,j)\) for all paths _P_ and iterations _j_.

## B Dominating Sets and Degree Decomposition

In this section, we give the proofs of Lemmas 2.4, 2.5, 2.6 and 6.1.

**Lemma 2.4.** _Let U be a universe of n elements. Let_ F={_S_<sub>1</sub>_,...,S<sub>n</sub>_} _denote a collection of subsets_ \(S_i\subset U\) _such that_ \(|S_i|\ge s\) _for all i. Then, there is a deterministic algorithm **HittingSet** that computes a hitting set X of size_ \(O\left(\frac{nlogn}{s}\right)\) _of_ F _in time_ \(\tilde{O}(ns)\)_. There is also a randomized algorithm **rHittingSet** that with high probability computes a hitting set X of size_ \(O\left(\frac{nlogn}{s}\right)\) _of_ F _in time O(n)._

