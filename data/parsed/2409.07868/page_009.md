## 3.3 General sequences

Finally, we remove the restriction of inputs to permutation sequences. Let us first describe a standard way used to deal with general pattern-avoiding sequences in previous works [CGK<sup>+</sup>15, BKO24]. The repeated elements in an arbitrary \(\pi\)-avoiding sequence _S_ can be perturbed to obtain a permutation sequence \(S'\) that avoids some pattern \(\pi'\) where \(|\pi'|=2|\pi|\). It follows that a linear sorting algorithm for pattern-avoiding permutations can be applied to \(S'\) in order to sort _S_. See [CGK<sup>+</sup>15] for more details. However, the relationship between \(c_\pi\) and \(c_{\pi^\prime}\) is not known in general, and as a result, we might lose the optimal asymptotic dependence on the pattern \(\pi\).

For this reason, we take a different path of carefully analyzing the behavior of Algorithm 2 on general \(\pi\)-avoiding sequences. Specifically, we launch Algorithm 2 on arbitrary \(\pi\)-avoiding input while breaking all ties according to their position on input, i.e., we perform a stable merge. Note that this tie-breaking can occur both when selecting the _d_-tuple of the smallest sequences in each round as well as during any merging. We claim that the asymptotic bound on runtime does not deteriorate.

Observe that Claim 3.3 is the only place in the analysis of Algorithm 2 where we used the fact that _S_ is a permutation sequence. It therefore suffices to show that analogous claim holds for general sequences and the promised runtime follows immediately.

**Lemma 3.4.** _On an arbitrary_ \(\pi\)_-avoiding sequence S, Algorithm 2 terminates after at most_ \(\lceil logc_\pi\rceil+2\) _phases._

_Proof._ Assume for a contradiction that more phases than \(\lceil logc_\pi\rceil+2\) are needed and set \(i=\lceil logc_\pi\rceil+2\). Our goal is to show that, in fact, the algorithm should have terminated in the _i_th phase. Our choice of _i_ guarantees that \(2^i\ge 4c_\pi\) and therefore we have \(d_i\ge 4c_\pi\).

We distinguish between two different types of rounds during the execution of Algorithm 2 on general sequences. A round is _heavy_ if all elements processed during it are equal in value; otherwise we say that the round is _light_. A _value_ of a heavy round is simply the singular value of all the elements processed in that round. We shall bound the number of heavy and light rounds independently. Furthermore, we focus only on rounds that touch exactly _d_ sequences. Let us call such rounds _full_. Observe that there can be at most one non-full round, the final one, and we can handle this round separately regardless of its type.

\(M(j,k)=\left\{\begin{array}{ c c }
1 & \text{if the sequence}S'_j\text{was touched by a full heavy round of value}x_k \\
0 & \text{otherwise.}
\end{array}\right.\)

<tbc>As we already argued, no sequence was touched by two different heavy rounds of the same value. Moreover, we only count full rounds that touched exactly _d_ sequences and therefore, the number of 1-entries in _M_ is

\(H\cdot d_i>\frac{m_i}{4}\cdot 4c_\pi=m_i\cdot c_\pi.\)

It follows that _M_ again contains an occurrence of \(\pi\) by Lemma 2.1 and since all its elements come from pairwise distinct sequences, we can find an occurrence of \(\pi\) in the original input sequence _S_. Therefore, we reached a contradiction and conclude that \(H\le\frac{m_i}{4}\) .

