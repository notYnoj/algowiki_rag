_Proof._ In the preprocessing phase, we run the preprocessing of Lemma 3. In the query phase, we repeatedly call the query phase of Lemma 3, with geometrically decreasing values of \(\beta\):

1. Preprocessing: Run the preprocessing of Lemma 3.<tbc>

2. For \(\beta=n,n/2,n/4,\dots,1\):<tbc>

3. Run the query phase of Lemma 3 with parameter \(\beta\) to obtain an estimate \(\widetilde{L}\).<tbc>

4. If \(\widetilde{L}\ge\ell\): return "\(L\ge\ell\)"<tbc>

5. If \(\widetilde{L}\le\ell/\beta-1\): return "\(L<\ell\)"

Let us first argue correctness. Since Lemma 3 computes a common subsequence of _x,y_, we have \(\widetilde{L}\le L\). Thus, if \(\widetilde{L}\ge\ell\), we correctly infer \(L\ge\ell\). Moreover, w.h.p. \(\widetilde{L}\) satisfies \(\widetilde{L}>L/\beta-1\). Therefore, if \(\widetilde{L}\le\ell/\beta-1\), we can infer \(L<\ell\), and this decision is correct with high probability. Finally, in the last iteration (where \(\beta=1\)), we have \(\ell/\beta-1=\ell-1\), and thus one of \(\widetilde{L}\ge\ell\) or \(\widetilde{L}\le\ell/\beta-1\) must hold, so the algorithm indeed returns a decision.

The expected time of the query phase of Lemma 3 is \(\widetilde{O}((n+M)/\beta+1)\). Since \(\beta\) decreases geometrically, the total expected time of our algorithm is dominated by the last call.

If \(L\ge\ell\), the last call is at the latest for \(\beta=1\). This yields running time \(\widetilde{O}(n+M)\le\widetilde{O}((n+M)L/\ell)\).

If \(L<\ell\), note that for any \(\beta\le\frac{\ell}{L+1}\) we have \(\widetilde{L}\le L\le\ell/\beta-1\), and thus we return "\(L<\ell\)". Because we decrease \(\beta\) by a factor 2 in each iteration, the last call satisfies \(\beta\ge\frac{\ell}{2(L+1)}\). Hence, the expected running time is \(\widetilde{O}((n+M)(L+1)/\ell+1)\). If \(L\ge 1\) then this time bound simplifies to \(\widetilde{O}((n+M)L/\ell+1)\). If _L_=0, then also _M_=0, and the time bound becomes \(\widetilde{O}(n/\ell+1)\). In both cases we can bound the expected running time by the claimed \(\widetilde{O}((n+M)L/\ell+n/\ell)\), since \(\ell\le n\).

## 4.2 Approximating the Number of Matching Pairs

Recall that for given strings _x,y_ of length _n_ the number of matching pairs _M=M(x,y_) can be computed in time _O(n_), which is linear in the input size. However, later in the paper we will split _x_ into substrings _x_<sub>1</sub>_,...,x<sub>n/m</sub>_ and _y_ into substrings _y_<sub>1</sub>_,...,y<sub>n/m</sub>_, each of length _m_, and we will need estimates of the numbers of matching pairs _M<sub>ij</sub>=M(x<sub>i</sub>,y<sub>j</sub>_). In this setting, the input size is still _n_ (the total length of all strings _x<sub>i</sub>_ and _y<sub>j</sub>_) and the output size is (_n/m_)<sup>2</sup> (all numbers _M<sub>ij</sub>_), but we are not aware of any algorithm computing the numbers _M<sub>ij</sub>_ in near-linear time in the input plus output size \(\widetilde{O}(n+(n/m)^2)\).<sup>5</sup> Therefore, we devise an approximation algorithm for estimating the number of matching pairs.

**Lemma 6.** _For_ \(x_1,\dots,x_{n/m},y_1,\dots,y_{n/m}\in\Sigma^m\) _write M<sub>ij</sub>=M(x<sub>i</sub>,y<sub>j</sub>_) _and_ \(M=\sum_{i,j}M_{ij}\)_. Given the strings x_<sub>1</sub>_,...,x<sub>n/m</sub>,y_<sub>1</sub>_,...,y<sub>n/m</sub> and a number q\>_0_, we can compute values_ \(\widetilde{M}_{ij}\) _that w.h.p. satisfy_ \(M_{ij}/8-q\le\widetilde{M}_{ij}\le 4M_{ij}\)_, in total expected time_ \(\widetilde{O}(n+M/q)\).

This yields a near-linear-time constant-factor approximation of all _above-average M<sub>ij</sub>_: By setting \(q:=\Theta(\frac{Mm^2}{n^2})\), in expected time \(\widetilde{O}(n+(n/m)^2)\) we obtain a constant-factor approximation of all values _M<sub>ij</sub>_ with \(M_{ij}\gg q\).

_Proof._ The algorithm works as follows.

1. _Graph Construction_: Build a three-layered graph _G_ on vertex set \(V(G)=L\cup U\cup R\), where _L_ has a node _i_ for every string _x<sub>i</sub>_, _R_ has a node _j_ for every string _y<sub>j</sub>_, and _U_ has a node \((\sigma,\ell,r)\) for any \(\sigma\in\Sigma\) and \(0\le\ell,r\le logm\). Put an edge from \(i\in L\) to \((\sigma,\ell,r)\in U\) iff \(\#_\sigma(x_i)\in[2^\ell,2^{\ell+1})\). Similarly, put an edge from \(j\in R\) to \((\sigma,\ell,r)\in U\) iff \(\#_\sigma(y_j)\in[2^r,2^{r+1})\). Note that all frequencies and thus all edges of this graphs can be computed in total time \(\widetilde{O}(n)\). For \(i\in L\) and \(j\in R\), we denote by \(U_{ij}\subseteq U\) their<tbc>

<sup>5</sup>In fact, one can show conditional lower bounds from Boolean matrix multiplication that rule out near-linear time for computing all _M<sub>ij</sub>_’s unless the exponent of matrix multiplication is \(\omega=2\).

