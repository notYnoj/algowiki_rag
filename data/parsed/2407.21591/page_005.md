\(e(P_G)\ge\prod_{i=1}^{n-k}L_i!\Rightarrow e(P_G)\ge\prod_{i=1}^{n-k}2^{L_i-1}=2\genfrac(){pt}{2}{\sum_{i=1}^{n-k}(L_i-1)}{\sum_{i=1}^{(L_i-1)}}\Rightarrow e(P_G)\ge 2^k\)

Here, the first implication uses that \(x!\ge 2^{x-1}\) and the second implication uses Equation 1.

What remains is to show that \(\sum_{i=1}^klogd_i\in O(loge(P_G))\). To this end, we create a set of intervals:

**Definition 1.** _Let_ \(\pi^*\) _be the directed path that Algorithm 1 outputs. For any_ \(i\in[n]\) _denote by_ \(\pi^*(x_i)\) _the index of x<sub>i</sub> in_ \(\pi^*\)_. We create an embedding E of X by placing x<sub>i</sub> at position_ \(\pi^*(x_i)\).

_Recall that for_ \(i\in[k]\)_, p<sub>i</sub> is the finger from where Algorithm 1 invokes_ Search _with x<sub>i</sub> as the argument. We create as set_ R _of n open intervals_ \(R_i=(a_i,b_i)\subseteq[0,n]\) _as follows:_

• _If i\>k then_ \((a_i,b_i):=(\pi^*(x_i)-1,\pi^*(x_i))\).<tbc>

• _Else,_ \((a_i,b_i):=(\pi^*(p_i),\pi^*(x_i))\).

**Lemma 2.** _Given distinct_ \(x_i,x_j\in X\)_. If there exists a directed path from x<sub>i</sub> to x<sub>j</sub> in G then the intervals R<sub>i</sub>_=(_a<sub>i</sub>,b<sub>i</sub>_) _and R<sub>j</sub>_=(_a<sub>j</sub>,b<sub>j</sub>_) _are disjoint with_ \(b_i\le a_j\).

_Proof._ We consider three cases.

If _i\>k_ and _j\>k_ then _x<sub>i</sub>_ and _x<sub>j</sub>_ are part of the original longest directed path in _G_. If _x<sub>i</sub>_ has a directed path to _x<sub>j</sub>_ in _G_ then _x<sub>i</sub>_ precedes _x<sub>j</sub>_ on the original longest directed path. Thus, \(\pi^*(x_i)\) precedes \(\pi^*(x_j)\) and _R<sub>i</sub>_ and _R<sub>j</sub>_ are distinct unit intervals where _R<sub>i</sub>_ precedes _R<sub>j</sub>_.

If \(i\le k\) and _j\>k_ then _x<sub>i</sub>_ was inserted into the path \(\pi\) with _x<sub>j</sub>_ already in \(\pi\). Since \(\pi^*\) is a linear extension of _P<sub>G</sub>_, it follows that _x<sub>i</sub>_ was inserted preceding _x<sub>j</sub>_ in \(\pi\). It follows that _x<sub>i</sub>_ precedes _x<sub>j</sub>_ in \(\pi^*\) and thus \(R_i=(\pi^*(p_i),\pi^*(x_i))\) lies strictly before \(R_j=(\pi^*(x_j)-1,\pi^*(x_j))\).

If \(j\le k\) then the vertex _p<sub>j</sub>_ must equal or succeed _x<sub>i</sub>_ in the path \(\pi^*\). It follows that \(b_i=\pi^*(x_i)\le a_i=\pi^*(p_j)\). The fact that these intervals are open then makes them disjoint.

The set R induces an interval order _P_<sub>R</sub> over _X_, which is the partial order \(\prec_\mathcal{R}\) where _x<sub>i</sub>_ and _x<sub>j</sub>_ are incomparable whenever _R<sub>i</sub>_ and _R<sub>j</sub>_ intersect, and where otherwise \(x_i\prec_\mathcal{R}x_j\) whenever \(b_i\le a_j\). By Lemma 2, any linear order _L_ that extends _P_<sub>R</sub> must also extend _P<sub>G</sub>_ and so \(e(P_\mathcal{R})\le e(P_G)\). The number of linear extensions of an interval order is much easier to count. In fact, Cardinal, Fiorini, Joret, Jungers and Munro \[3\] and Van der Hoog, Kostityna, Löffler and Speckmann \[11\] already upper bound the number of linear extensions of an interval order. We paraphrase their upper bound, to give a weaker version applicable to this paper. For a proof from first principles, see Section 3.

**Lemma 3** (Lemma 1 in \[11\] and Lemma 3.2 in \[3\])**.** _Let_ R=(_R_<sub>1</sub>_,...R<sub>n</sub>_) _be a set of n open intervals in_ \[0_,n_\] _and let each interval have at least unit size. Let P_<sub>R</sub> _be its induced partial order. Then:_

\(\sum_{i=1}^nlog(|R_i|)\in O(loge(P_\mathcal{R})).\)

We are now ready to prove our main theorem:

**Theorem 1.** _Given a directed acyclic graph G over X, inducing a partial order P<sub>G</sub>, and an oracle O<sub>L</sub> whose queries specify a linear order L that extends P<sub>G</sub>, there exists an algorithm that uses linear space, O(n+m_+log_e(P<sub>G</sub>_)) _time and O_(log_e(P<sub>G</sub>_)) _oracle queries to output the sorted order of X._

