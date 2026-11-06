On the other hand,

\(\sum_{i\ge 1}\mathbb{P}[m\ge i]H(Y_i|X,Q_i,m\ge i)=\sum_{i\ge 1}\mathbb{P}[m\ge i]h(p)(1-q_i)\)<br>
\(=h(p)\left(\sum_{i\ge 1}\mathbb{P}[m\ge i]-\sum_{i\ge 1}\mathbb{P}[m\ge i]q_i\right)\)<br>
\(\ge h(p)(\mathbb{E}[m]-n)\)<br>
\(=(1-o(1))h(p)\mathbb{E}[m].\)

Plugging the above two inequalities in Equation (2), we get

\(I(X;Q^m,Y^m)\le(1+o(1))\mathbb{E}[m]-(1-o(1))h(p)\mathbb{E}[m]\)<br>
\(\le(1+o(1))I(p)\mathbb{E}[m].\)

Combining with Equation (1), we get \(\mathbb{E}[m]\ge(1-o(1))\frac{nlogn}{I(p)}\) .

Before we give lower bound for the number of queries made to elements in the same group, we first show the following technical lemma that will be useful later.

**Lemma 28.** _Let_ \((X_n)_{n\ge 0}\) _be a Markov process defined as_<tbc>

\(X_0=0,X_{n+1}=X_n+\left\{\begin{array}{ c c }
+1 & w.p. 1-p, \\
-1 & w.p. p.
\end{array}\right.\)

<tbc>_Let_ \(\tau\) _be a random variable supported on_ \(\mathbb{Z}_{\ge 0}\)_. Suppose there exists_ \(\delta>0\) _such that_<tbc>

\(\mathbb{E}[\tau]\le(1-\delta)m/(1-2p).\)

<tbc>_Then_<tbc>

\(\mathbb{P}[X_\tau\le m]\ge\delta/2-o_m(1).\)

<tbc>_Proof._ Let _E_<sub>1</sub> be the event that \(\tau\le(1-\delta/2)m/(1-2p)\). Let _E_<sub>2</sub> be the event that \(X_t\le m\) for all \(t\le(1-\delta/2)m/(1-2p)\). By Markov’s inequality, \(\mathbb{P}[E_1]\ge\delta/2\). By concentration inequalities, \(\mathbb{P}[E_2]\ge 1-o_m(1)\). Using union bound, we have

\(\mathbb{P}[X_\tau\le m]\ge\mathbb{P}[E_1\wedge E_2]\ge\delta/2-o_m(1).\)

**Lemma 29.** _Fix any (deterministic or randomized) algorithm for_ NoisySorting(_n_) _with error probability o_(1)_. Let k|n. Let L be the input list of_ NoisySorting(_n). Suppose we partition L into n/k groups A_<sub>1</sub>_,...,A<sub>n/k</sub> where for all_ \(1\le i<j\le n/k\)_, for all_ \(x\in A_i\), \(y\in A_j\)_, we have x\<y. Let U_<sup>=</sup> _denote the number of queries made to elements in the same group._

_Then_ \(\mathbb{E}[U^=]\ge(1-o(1))\frac{(n-n/k)log(n-n/k)}{(1-2p)log\frac{1-p}{p}}\) _, even if the input is a uniformly random permutation._<tbc>

