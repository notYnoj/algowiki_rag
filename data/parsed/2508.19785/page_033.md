<tbc>that \(Pr(Y_\lambda=1)=\sum_{I\in U}X_IPr(I)\ge\frac{1}{2}\left(\frac{p}{1-p}\right)^{2(y-x)-1}\forall\lambda\in\{0,1\}^t\). We are now ready to bound the probability that _Y_=1, indeed:

\(Pr(Y=1)=\sum_{\lambda\in\{0,1\}^t}Pr(Y_\lambda=1)p_\lambda\ge\frac{1}{2}\left(\frac{p}{1-p}\right)^{2(y-x)-1}\sum_{\lambda\in\{0,1\}^t}p_\lambda=\frac{1}{2}\left(\frac{p}{1-p}\right)^{2(y-x)-1},\)

where the last equality follows from the fact that \(p_\lambda\) is a probability distribution over the elements \(\lambda\in\{0,1\}^t\), and hence \(\sum_{\lambda\in\{0,1\}^t}p_\lambda=1\). □

As a first consequence of the previous lemma, we obtain the following:

Theorem 6.2. _No (possibly randomized) algorithm can achieve maximum dislocation o_(log_n_) _with high probability._

Proof. By Lemma 6.1, any algorithm, when invoked on a random instance, must return a permutation \(\rho\) in which elements 1 and \(h=\lfloor\frac{logn}{2log(1-p)/p}\rfloor\) appear in the wrong relative order with a probability larger than \(\frac{1}{n}\). When this happens, at least one of the following two conditions holds: (i) the position of element 1 in \(\rho\) is at least \(\lceil\frac{h}{2}\rceil\); or (ii) the position of element _h_ in \(\rho\) is at most \(\lfloor\frac{h}{2}\rfloor\). In any case, the maximum dislocation must be at least \(\frac{h}{2}-1=\Omega(logn)\). □

Finally, we are also able to prove a lower bound to the total dislocation.

Theorem 6.3. _No (possibly randomized) algorithm can achieve an expected total dislocation of o(n_).

Proof. Let _A_ be any algorithm and let \(\langle\pi,C\rangle\) be a random instance on an even number of elements _n_. We define _X<sub>k</sub>_ for \(0\le k<n/2\) to be an indicator random variable that is 1 if and only if \(A(\langle\pi,C\rangle)\) returns a permutation of _S_ in which elements 2_k_+1 and 2_k_+2 appear in the wrong relative order.

By Lemma 6.1 we know that \(Pr(X_k=1)\ge\frac{1}{2}\frac{p}{1-p}\). We can hence obtain a lower bound on the expected total dislocation _D_ achieved by _A_ as follows:

\(\mathbb{E}[D]\ge\sum_{k=0}^{n/2-1}\mathbb{E}[X_k]\ge\sum_{k=0}^{n/2-1}\frac{1}{2}\cdot\frac{p}{1-p}\ge\frac{n}{4}\cdot\frac{p}{1-p}=\Omega(n).\) □

## 7 Derandomization

In this section, we consider the case in which the elements to be approximately sorted are subject to persistent random comparison errors with probability at least _q_ and at most _p_, for some positive constants _p_ and _q_ with \(p\le\frac{9q+1}{8q+11}\), and the positions of the elements in the input sequence do not depend on the comparison errors. Under these assumptions, we can exploit the intrinsic random nature of comparison faults to derandomize RiffleSort while maintaining its _O(n_log_n_) running time. In other words, the sequence returned by the derandomized version of RiffleSort is completely determined by the input sequence and by the observed comparison errors, and no access to an external source of random bits is required.

This section is organized as follows: first we show that (a slight variant of) RiffleSort can be implemented so that the overall number of random bits required is _O(n_) with high probability. Then, we show that we can use the outcomes of the noisy comparisons among some of the input elements to generate \(\Omega(n)\) biased, but almost-uniform random bits, and that using these almost- uniform random bits in place of the truly uniform ones does not affect the asymptotic guarantees of RiffleSort.

