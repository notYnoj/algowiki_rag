_Proof._ Our algorithm runs in \(O(n+m+k+\sum_{i=1}^klogd_i)\) time and uses \(O(k+\sum_{i=1}^klogd_i)\) queries. By Lemma 1, \(k\in O(loge(P_G))\). The set R of Definition 1 is a set where each interval _R<sub>i</sub>_ has at least unit size. By Lemma 2, \(e(P_\mathcal{R})\le e(P_G)\). For \(i\le k\), the size |_R<sub>i</sub>_| must be at least _d<sub>i</sub>_ since there are per construction at least _d<sub>i</sub>_ vertices on the subpath from \(\pi^*(p_i)\) to \(\pi^*(q_j)\) in the embedding _E_. It follows by Lemma 3 that \(\sum_{i=1}^klogd_i\in O(loge(P_\mathcal{R}))\subseteq O(loge(P_G))\).

## 3 Deriving Lemma 3 from first principles

We consider the following statement:

**Lemma 3** (Lemma 1 in \[11\] and Lemma 3.2 in \[3\])**.** _Let_ R=(_R_<sub>1</sub>_,...R<sub>n</sub>_) _be a set of n open intervals in_ \[0_,n_\] _and let each interval have at least unit size. Let P_<sub>R</sub> _be its induced partial order. Then:_<tbc>

\(\sum_{i=1}^nlog(|R_i|)\in O(loge(P_\mathcal{R})).\)

<tbc>While this lemma follows verbatim from Lemma 1 in \[11\] (which itself is weaker version of Lemma 3.2 in in \[3\]), we also give a proof from first principles. We reindex R so that (_R_<sub>1</sub>_,R_<sub>2</sub>_,...,R<sub>m</sub>_) is a maximum cardinality set of pairwise-disjoint intervals in _R_, sorted from left to right. For any \(R_i\in\mathcal{R}\) we denote by mid(_R<sub>i</sub>_) its centre. We define an (_n-m_)-dimensional polytope associated with R.

\(A=\left\{x\in\mathbb{R}^n\big|x_i=mid(R_i)\text{for}i\le m\text{and}x_i\in R_i\text{for}i>m\right\}\)

The volume of this polytope is \(Vol(A)=\prod_{i=m+1}^n|R_i|\). Any \(x=(x_1,\dots,x_n)\in A\) with distinct coordinates defines a linear extension _L_ of _P_<sub>R</sub> via the rule "\(i\prec j\) if and only if _x<sub>i</sub>\<x<sub>j</sub>_". We call the point _x_ a _realisation of L_. Observe that not all linear extensions of _P_<sub>R</sub> have a realisation \(x\in A\).

**Claim 1.** _Let L be a linear extension of P<sub>R</sub>. Let_ \(A_L=\left\{x\in A\big|x\text{realises}L\right\}\)_, then_<tbc>

\(Vol(A_L)\le(2e)^{n-m}.\)

<tbc>_Proof._ Consider the _m_+1 open intervals:<tbc>

\(I:=(-0.5,mid(R_1)),\dots,(mid(R_i),mid(R_{i+1})),\dots,(mid(R_{m-1}),n+0.5).\)

<tbc>For all \((i,j)\in[m]\times[m]\), the intervals (_R<sub>i</sub>,R<sub>j</sub>_) are disjoint and have length at least 1. It follows that each interval in _I_ has length at least 1. Suppose that _L_ cannot be realised, then Vol(_A<sub>L</sub>_)=0. Otherwise, we observe that for any \(x,x'\) realising _L_ and any \(i\in\{m+1,\dots,n\}\), an interval in _I_ contains _x<sub>i</sub>_ if and only if it contains \(x'_i\). This allows us to say that an interval in _I_ is _occupied under L_ if it contains _x<sub>i</sub>_ for any realisation _x_ of _L_ and any _i\>m_. There are at most _n-m_ occupied intervals, and therefore at least _m_+1-(_n-m_)=(2_m_+1-_n_) non-occupied intervals in _I_. Let _G<sub>L</sub>_ be the union of the occupied intervals. Then \(|G_L|\le|(-0.5,n+0.5)|-(2m+1-n)=2(n-m)\), as each non-occupied interval has length at least 1. Let:<tbc>

\(B_L=\left\{y\in\mathbb{R}^m\times G_L^{n-m}\big|y_i=mid(R_i)\text{for}i\le m\text{and}(x_j<x_k\Leftrightarrow y_j<y_k)\text{for}j,k>m\right\}.\)

