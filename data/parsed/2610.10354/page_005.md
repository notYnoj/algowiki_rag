<tbc>of the BSG Theorem--and how we overcome them--let us take a short excursus into additive combinatorics.

Intuitively, the BSG theorem states that any set _A_ with a lot of "local structure", e.g., in the form of many solutions to the equation _a_<sub>1</sub>+_a_<sub>2</sub>=_a_<sub>3</sub>+_a_<sub>4</sub> for \(a_1,a_2,a_3,a_4\in A\), must admit a large subset _H_ that is "globally structured", in the sense that the _sumset_ \(H+H=\left\{a+b:a,b\in H\right\}\) is small. Such sets _H_ are also called _low-doubling_ sets since their _doubling_ \(\frac{|H+H|}{|H|}\) is small. To state the BSG Theorem quantitatively, let us introduce a piece of notation that will turn out convenient later:

\(\mathrm{Pop}^k(A;p)=\left\{x:|\{(a_1,\dots,a_k)\in A^k:x=a_1+\cdots+a_k\}|\ge p\right\},\)

i.e., the set of all sums \(a_1+\cdots+a_k\) that can be expressed in at least _p_ distinct ways. We refer to these as the _popular k-sums_. Then the BSG theorem can be equivalently stated in the following (non-standard) form:<sup>3</sup>

**Theorem 1.1** (BSG Theorem, Reformulated)**.** _Let_ \(A\subseteq\mathbb{Z}\) _be a set with_ \(\mathrm{Pop}^4(A;|A|^3/K)\neq\emptyset\)_. Then there is a set_ \(H\subseteq\mathbb{Z}\) _satisfying that:_

• \(|H|\le|A|\) _(in fact, we can take H as a subset of A),_<tbc>

• \(|H+H|\le K^{O(1)}|H|\),<tbc>

• \(|A\cap H|\ge|A|/K^{O(1)}\).

In other words, the existence of a popular 4-sum certifies the presence of a large low-doubling subset.

Unfortunately, the BSG Theorem is insufficient to deal with sets exhibiting much weaker additive structure. Consider the following example. Let _A_ be a random size-_n_ set in a large universe {0_,...,u_}, say for _u=n_<sup>10</sup>. In this case, with good probability, each 4-sum is unique. In particular, there are no popular 4-sums. This is consistent with the fact that _A_ contains no large low-doubling subset. Nevertheless, _A_ is not entirely unstructured: it is contained in a much larger low-doubling set, namely the entire universe {0_,...,u_}. The challenge is that this weak global structure is invisible to the 4-sums. Our key insight is that such weak structure can be detected by moving to larger _k_-sums. Specifically, we show that for sufficiently large _k_, the presence of a popular _k_-sum reveals the desired structure. This leads to the following higher-order analogue of the BSG Theorem.

**Theorem 1.2** (Popular _k_-Sums Imply Low-Doubling Structure)**.** _For every c\>_0 _and_ \(\epsilon>0\)_, there is some_ \(k=k(c,\epsilon)\) _such that the following holds. Let_ \(A\subseteq\mathbb{Z}\) _and assume that_ \(\mathrm{Pop}^k(A;p)\neq\emptyset\) _for some_ \(p=\Omega(|A|^{k-1-c})\)_. Then there exists a set_ \(H\subseteq\mathbb{Z}\) _and some_ \(K=O_{c,\epsilon}(|A|^\epsilon)\) _such that:_

• \(|H|\le K|A|^{1+c}\),<tbc>

• \(|H+H|\le K|H|\),<tbc>

• \(|A\cap H|\ge|A|/K\).

<sup>3</sup>To relate Theorem 1.1 to the usual BSG Theorem (e.g., Theorem 2.3), note that _A_ has a popular 4-sum, \(\mathrm{Pop}^4(A;|A|^3/K)\neq\emptyset\), if and only if _A_ has large _additive energy_, \(E(A)\ge|A|^3/K'\), where _K_ and \(K'\) depend polynomially on each other. The "if" direction is immediate by Cauchy-Schwarz. The "only if" direction follows from some basic Fourier analysis and Hölder’s inequality (see e.g., \[JX23, Lemma 2.11\]).

