## 7.1 Implementing RiffleSort using _O(n_) random bits w.h.p.

The only randomized steps of RiffleSort are the computation of the sequence \(S'\), which is obtained by shuffling the input sequence _S_ (see line 1 of Algorithm 1), and the partition of the _n_ input elements into the _k_+1 subsets _T_<sub>0</sub>_,T_<sub>1</sub>_,...,T<sub>k</sub>_ of _T_, as described in Section 3.1.

Since we are considering the case in which the positions of the elements in the input sequence do not depend on the comparison errors, we can simply skip the shuffling step of line 1, and set \(S'=S\) instead. We now argue that the partition _T_<sub>0</sub>_,...,T<sub>k</sub>_ can be found while only using _O(n_) random bits. In this regard, we will make use of the following more general result, whose proof does not depend on the details of RiffleSort nor on our error model and can be found in Appendix A.

Lemma 7.1. _There exists an algorithm that, given any set A of N elements and an integer_ \(h\in\{0,\dots,N\}\)_, returns a set chosen uniformly at random among all subsets of A with exactly h elements. The algorithm requires O(N_) _time and at most_ 60_N random bits with probability at least_ \(1-O\left(e^{-\sqrt{N}}\right)\).

Then, using the fact that \(|T_i|=\frac{1}{2}|T_{i+1}|\) for _i_=0_,...,k_-1, we can prove the following:

Lemma 7.2. _The partition T_<sub>0</sub>_,T_<sub>1</sub>_,...,T<sub>k</sub> of_ RiffleSort _can be found using O(n_) _time and at most_ 999_n random bits with probability at least_ 1-_O(n_<sup>-3</sup>).

Proof. Recall from Section 3.1 that \(k=\left\lceil log\frac{n}{\lceil\sqrt{n}\rceil}\right\rceil<1+\frac{1}{2}logn\), that \(|T_i|=2^i\cdot\lceil\sqrt{n}\rceil\) for _i_=0_,...,k_-1, and that \(T_k\le 2^k\cdot\lceil\sqrt{n}\rceil\).

To obtain the sought partition, we iteratively select _T<sub>i</sub>_ for starting form _i=k_ down to _i_=0. More precisely, we keep track of the set \(T'_i=S\backslash\bigcup_{j=i}^kT_i\) of all yet unselected elements (notice that \(T'_{k+1}=S\)), and we select _T<sub>i</sub>_ u.a.r. among all subsets of \(T'_{i+1}\) having |_T<sub>i</sub>_| elements using the algorithm of Lemma 7.1.

We have \(|T'_i|=\sum_{j=0}^{i-1}|T_i|<2^i\lceil\sqrt{n}\rceil\le 2^{i+1}\sqrt{n}\), and, using \(|T_i|\ge\sqrt{n}\), Lemma 7.1 ensures that the selection of each _T<sub>i</sub>_ requires no more than \(60|T'_{i+1}|\le 60\cdot 2^{i+2}\sqrt{n}\) random bits with probability at least 1-_O(e_<sup>-_n_<sup>1/4</sup></sup>). Then, this holds jointly for all _T<sub>i</sub>_ with probability at least \(1-O(k\cdot e^{-n^{1/4}})=1-O(n^{-3})\) and, in such a case, the overall number of used random bits is upper bounded by:

\(60\sqrt{n}\sum_{i=0}^k2^{i+2}<60\sqrt{n}\cdot 2^{k+3}<60\sqrt{n}\cdot 2^{4+\frac{1}{2}logn}<999n,\)

and a similar calculation yields the claimed upper bound on the running time. □

## 7.2 Derandomizing RiffleSort

We start by formalizing a simple technique that combines multiple biased coin flips to simulate the outcome of a single coin with a smaller bias.

Lemma 7.3. _Let_ \(\delta\in[0,1]\) _and let_ \(X_1,X_2,\dots,X_\eta\) _be_ \(\eta\ge 1\) _independent Bernoulli random variables where X<sub>i</sub> has parameter_ \(p_i\in\left[\frac{1}{2}-\frac{\delta}{2},\frac{1}{2}+\frac{\delta}{2}\right]\cdot Pr(\oplus_{i=1}^\eta X_i=1)\in\left[\frac{1}{2}-\frac{\delta\eta}{2},\frac{1}{2}+\frac{\delta\eta}{2}\right]\).

Proof. The proof is by induction on \(\eta\). The base case \(\eta=1\) is trivially true. Suppose now that the claim is true for \(\eta-1\ge 1\) Bernoulli random variables. Defining \(\rho=Pr(\oplus_{i=1}^{\eta-1}X_i=1)\), we have:

\(Pr\left(\oplus_{i=1}^\eta X_i=1\right)=Pr\left(\oplus_{i=1}^{\eta-1}X_i=0\right)Pr\left(X_\eta=1\right)+Pr\left(\oplus_{i=1}^{\eta-1}X_i=1\right)Pr\left(X_\eta=0\right)\)<br>
\(=(1-\rho)p_\eta+\rho(1-p_\eta)=\frac{1}{2}+2\left(\frac{1}{2}-p_\eta\right)\left(\rho-\frac{1}{2}\right).\)

