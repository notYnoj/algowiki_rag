## 2.3 Dynamic programming and partial solutions

Our algorithm uses dynamic programming (DP) to find an optimal exchange solution \((A,B)\) (\(A\subseteq\overline{G},B\subseteq G\)). Now we introduce a few terminologies that will help us describe our DP algorithm later.

**Definition 2.5** (Partial solutions and _I_-optimality)**.** A _partial exchange solution_ (or simply a _partial solution_) refers to a pair of item subsets \((A',B')\) where \(A'\subseteq\overline{G},B'\subseteq G\). The _weight_ and _profit_ of the partial solution \((A',B')\) are defined as \(W(A')-W(B')\) and \(P(A')-P(B')\) respectively.

Let \(I\subseteq[n]\) be an item subset. We say the partial solution \((A',B')\) is _supported on I_ if \(A'\cup B'\subseteq I\). We say \((A',B')\) is _I-optimal_, if there exists an optimal exchange solution (_A,B_) such that \(A'=A\cap I\) and \(B'=B\cap I\).

**Definition 2.6** (DP tables)**.** A _DP table of size L_ is an array \(q[-L..L]\) with entries \(q[z]\in\mathbb{Z}\cup\{-\infty\}\) for \(z\in\{-L,\dots,L\}\).<sup>7</sup> (By convention, assume \(q[z]=-\infty\) for |_z|\>L_.) We omit its index range and simply write _q_\[\] whenever its size is clear from context or is unimportant.

For an item subset \(I\subseteq[n]\), we say _q_\[\] is an _I-valid DP table_, if for every entry \(q[z]\neq-\infty\) there exists a corresponding partial solution \((A',B')\) supported on _I_ with weight \(W(A')-W(B')=z\) and profit \(P(A')-P(B')=q[z]\). An _I_-valid DP table _q_\[\] is said to be _I-optimal_ if it contains some entry _q_\[_z_\] that corresponds to an _I_-optimal partial solution.

For example, the trivial DP table with \(q[0]=0,q[z]=-\infty(z\neq 0)\) is \(\varnothing\)-optimal (it contains the empty partial solution \((\varnothing,\varnothing)\)). In dynamic programming we gradually extend this \(\varnothing\)-optimal DP table to an \[_n_\]-optimal DP table which should contain an optimal exchange solution. As a basic example, given an _I_-optimal DP table _q_\[-_L..L_\], for \(i\notin I\) we can obtain an \((I\cup\{i\})\)-optimal DP table \(q'[-L-w_i..L+w_i]\) in _O(L+w<sub>i</sub>_) time via the update rule \(q'[z]\leftarrow max\{q[z],q[z\mp w_i]\pm p_i\}\) (where \(\pm\) is + if \(i\in\overline{G}\), or - if \(i\in G\)).

Previous dynamic programming algorithms for 0-1 Knapsack \[PRW21, CLMZ24, AT19, KP04\] used the following standard lemma based on the SMAWK algorithm \[AKM<sup>+</sup>87\]:

**Lemma 2.7** (Batch-updating items of the same weight)**.** _Let_ \(I\subseteq[n]\) _and_ \(J\subseteq\overline{G}\) _be disjoint item subsets, and all_ \(j\in J\) _have the same weight w<sub>j</sub>=w. Suppose an upper bound_ \(L'\) _is known such that all_ \((I\cup J)\)_-optimal partial solutions_ \((A',B')\) _satisfy_ \(|W(A')-W(B')|\le L'\).

_Then, given an I-optimal DP table q_\[-_L..L_\]_, we can compute an_ \((I\cup J)\)_-optimal DP table_ \(q'[-L'..L']\) _in_ \(O(L+L'+|J|+w_{max}logw_{max})\) _time._

_The same statement holds if the assumption_ \(J\subseteq\overline{G}\) _is replaced by_ \(J\subseteq G\).

_Proof Sketch._ Let \(J=\{j_1,j_2,\dots,j_{|J|}\}\subseteq\overline{G}\) be sorted so that \(p_{j_1}>p_{j_2}>\cdots>p_{j_{|J|}}\). By the prefix property (Lemma 2.4), for function \(Q(x):=p_{j_1}+p_{j_2}+\cdots+p_{j_x}\) we know that \(q'[z]:=max_{x\ge 0}\{q[z-xw]+Q(x)\}\) gives an \((I\cup J)\)-optimal DP table \(q'[-L'..L']\). Moreover, due to the size of the tables, it suffices to maximize over \(x\ge 0\) where \(xw\le L+L'\), i.e., \(0\le x\le\lfloor(L+L')/w\rfloor\).

The task of computing \(q'[\rfloor\) can be decomposed into _w_ independent subproblems based on the remainder _r_=(_z_mod_w_). Each subproblem then translates to computing the (max,+)-convolution of the subsequence of _q_ with indices \(\equiv r(modw)\) and the array \([Q(0),\dots,Q(\lfloor(L+L')/w\rfloor)]\), which can be done in linear time using SMAWK algorithm \[AKM<sup>+</sup>87\] due to the concavity of \(Q(\cdot)\) (i.e., \(Q(x)-Q(x-1)\ge Q(x+1)-Q(x)\) for all \(x\ge 1\)). (Readers unfamiliar with the result of \[AKM<sup>+</sup>87\] may refer to Appendix A for an overview.) Hence, the total time for running SMAWK is linear in the total size of these arrays, which is \(O(L+L'+w)\).

<sup>7</sup>For brevity we call it size-_L_ despite its actual length being (2_L_+1).

