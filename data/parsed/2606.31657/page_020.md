Fix any _d_-regular bipartite graph _G_=(_A,B,E_) on the vertex set \(A\cup B\) (|_A_|=|_B_|=_t/_2) and write \(\sigma(G)\in[0,1)\) for the _second singular value_ of its normalized adjacency matrix (equivalently: the largest nontrivial absolute eigenvalue of the random-walk matrix on _G_). Consider the non-adaptive 2-query tester _T_ that, on input \(y\in\{0,1\}^{tk}\),

chooses \(i\in[k]\) uniformly at random, chooses a random edge \((a,b)\in E\), queries the two symbols _y<sub>a,i</sub>,y<sub>b,i</sub>_, and _rejects_ iff _y<sub>a,i</sub>=y<sub>b,i</sub>_.

The blocklength is _n=tk_.

We use the following spectral Poincaré inequality for bipartite _d_-regular graphs.

**Lemma 4.5** (Edge Poincaré)**.** _For any_ \(f:A\cup B\rightarrow\mathbb{R}\),<tbc>

\(\frac{1}{|E|}\sum_{(u,v)\in E}\big(f(u)-f(v)\big)^2\ge 2(1-\sigma(G))\mathrm{Var}(f).\)

<tbc>_Proof._ Let _A<sub>G</sub>_ be the adjacency matrix of _G_ and _P=A<sub>G</sub>/d_. A standard calculation shows

\(\frac{1}{|E|}\sum_{(u,v)\in E}\big(f(u)-f(v)\big)^2=2\big(\langle f,f\rangle-\langle f,Pf\rangle\big).\)

Decompose \(f=\bar{f}\cdot\mathbf{1}+z\) with \(\langle z,\mathbf{1}\rangle=0\). Since **1** is an eigenvector of _P_ with eigenvalue 1 and all other singular values are at most \(\sigma(G)\) in absolute value, \(\langle f,Pf\rangle\le\bar{f}^2+\sigma(G)\langle z,z\rangle\). Thus \(2(\langle f,f\rangle-\langle f,Pf\rangle)\ge 2\big(\langle z,z\rangle-\sigma(G)\langle z,z\rangle\big)=2(1-\sigma(G))\mathrm{Var}(f)\), as claimed.

**Theorem 4.6.** _For the code_ \(\mathrm{Rep}^\pm(k,t)\)_, the following hold:_

1. _The relative distance is_ \(\delta=\frac{1}{k}=\frac{t}{n}\).<tbc>

2. _The rate is_ \(r=\frac{k}{n}=\frac{1}{t}\).<tbc>

_3._ _For every_ \(y\in\{0,1\}^n\),<tbc>

<tbc>\(\mathbf{Pr}\left[T\mathrm{rejects}y\right]\ge\kappa\cdot\delta_\mathrm{H}\big(y,\mathrm{Rep}^\pm(k,t)\big),\text{\textit{with}}\kappa=1-\sigma(G).\)<tbc>

<tbc>_In particular,_ \(\kappa\) _is an absolute constant that depends only on d and the expansion of G (and is independent of t and k, hence of the blocklength n)._<tbc>

_4._ _Each coordinate_ (_v,i),_ \(v\in A\cup B\)_, participates in exactly d possible queries (one per incident edge of G). Hence the (maximum) degree is d._

_Proof._ (1)-(2) As in the ordinary repetition code, the encoder \(x\mapsto y\) is injective with message length _k_ and blocklength _n=tk_; two distinct messages differing in one coordinate produce codewords that differ on all _t_ copies of that coordinate, giving minimum (absolute) distance _t_ and relative distance \(\delta=t/n=1/k\).

(3) _Soundness._ Fix a received word _y_ and a column \(i\in[k]\). Define the _flipped_ column \(g_i\in\{0,1\}^{A\cup B}\) by<tbc>

\(g_i(v)=\left\{\begin{array}{ c c }
y_{v,i} & v\in A, \\
1-y_{v,i} & v\in B,
\end{array}\right.\)

<tbc>so that _g<sub>i</sub>_ is constant iff the _i_-th column of _y_ belongs to the code constraint (_A_-entries equal and _B_- entries their complements). The nearest codeword in column _i_ is obtained by setting all _t_ positions to the majority bit of _g<sub>i</sub>_; hence the per-column contribution to the relative distance is<tbc>

\(\Delta_i=\mathrm{min}\{\mathrm{fractionof}1\text{’s in}g_i,\mathrm{fractionof}0\text{’s in}g_i\}.\)

