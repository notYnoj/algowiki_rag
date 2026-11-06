**Truncated Geometric Variates.** Besides the Bounded Geometric variates, the so-called _Truncated Geometric_ random variates are also of great importance to many applications. As we see in Section 4, it is a crucial building block in our optimal DPSS algorithm. Given \(p\in(0,1)\) and \(n\in\mathbb{N}\), the truncated geometric distribution, denoted by T-Geo(_p,n_), defined on {1_,...,n_}, has distribution:

\(Pr[T-Geo(p,n)=i]=\frac{p(1-p)^{i-1}}{1-(1-p)^n},\text{for}i\in\{1,\dots,n\}.\)

The probability function of truncated geometric distribution can be interpreted as a conditional probability as follows. Consider sampling each item from a bucket of _n_ items with probability _p_ independently. Then T-Geo(_p,n_) is identically distributed as the smallest index of the sampled items, conditioned on at least one item being sampled.

**Proof of Theorem 1.3.** We consider the following possible cases:

**Case 1 (**\(n\le 2\)**):** This is the trivial case to generate _i_∼T-Geo(_p,n_). If _n_=1, then T-Geo(_p,n_)=1 always holds. If _n_=2, it can be verified that T-Geo(_p,n_) returns either _i_=1 with probability \(\frac{1}{2-p}\) or _i_=2 with probability \(\frac{1-p}{2-p}\). In this case, T-Geo(_p,n_) is identically distributed as \(Ber(\frac{1-p}{2-p})+1\). By Fact 1, this can be achieved in _O_(1) expected running time with _O_(1) worst-case space. Thus, Theorem 1.3 holds.

**Case 2.1 (**\(n\ge 3\) **and** \(np\ge 1\)**):** In this case, an _i_∼T-Geo(_p,n_) can be realized by repeatedly generating _i_∼B-Geo(_p,n_+1) until \(i\le n\) holds. In each generation, \(i\le n\) happens with probability \(1-(1-p)^n>1-\frac{1}{e}\) because \(np\ge 1\). Thus, _i_ is realized from T-Geo(_p,n_) in _O_(1) trials in expectation. By Fact 3, Theorem 1.3 holds.

**Case 2.2 (**\(n\ge 3\) **and** _np\<_1**):** To handle this case, we propose an algorithm which runs as follows:

\(\bullet i\leftarrow 0\);

\(\bullet\) while \(i\le n\) do:

\(-i\leftarrow i+B-Geo(\frac{2}{n},n+1)\);

\(-\) if \(i\le n\) and Ber((1-_p)^{i-1})=1

\* generate \(c\leftarrow Ber(\frac{1}{2p^*})\), with \(p^*=\frac{1-(1-p)^n}{np}\) ;

\* if _c_=1, **return** _i_ as a realization of a random variate from T-Geo(_p,n_);

\(\bullet\) start over from the first step with \(i\leftarrow 0\);

To complete the proof of Theorem 1.3, we show the correctness and running time cost of the above algorithm.

<u>Correctness</u>. Observe that the B-Geo\((\frac{2}{n},n+1)\) generation in the while-loop simulates the subset sampling process of choosing _i_, for each index _i_, independently with probability 2_/n_. Thus, each _i_ has probability 2_/n_ of being sampled in this step. Next, _i_ is provisionally accepted with probability (1-_p)_<sup>_i_-1</sup> via a Bernoulli trial, and _i_ is further eventually accepted with probability \(\frac{1}{2p^*}\). Therefore, combining all these probabilities, we have:

\(Pr[i\text{is returned as a T-Geo}(p,n)\text{variate}]=\frac{2}{n}\cdot(1-p)^{i-1}\cdot\frac{1}{2\cdot\frac{1-(1-p)^n}{np}}=\frac{p(1-p)^{i-1}}{1-(1-p)^n}.\)

Hence, our algorithm for _np\<_1 case correctly realizes a T-Geo(_p,n_) random variate.

<u>The Running Time</u>. First, it can be verified that, B-Geo(2_/n,n_+1) returns \(i\le n\) within _O_(1) trials in expectation. Next, we prove that, given an _i_, our algorithm accepts _i_ with at least constant probability. To see this, given an _i_, it is accepted by the first Bernoulli trial with probability \((1-p)^{i-1}\ge(1-p)^n\ge(1-\frac{1}{n})^n\ge\frac{8}{27}\), where the second last inequality comes from the fact that

