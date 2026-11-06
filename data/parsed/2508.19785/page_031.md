Moreover, by Lemma 5.11, \(Pr(S_{w^\prime}\in\mathcal{S})=1-O\left(\frac{logm}{m^4log\frac{1}{\rho}}\right)\). By observing that an execution of `BasketSort` with initial window size _w<sub>S</sub>_ can be broken down into (i) all the rounds corresponding to window sizes from _w<sub>S</sub>_ (included) to \(w'\) (excluded) resulting in the sequence \(S_{w^\prime}\) and (ii) an execution of `BasketSort` on \(S_{w^\prime}\) with initial window size \(w'\), we can write:<sup>9</sup>

\(Pr\left(\sum_{x\in S}disl(x,S_1)\le(\gamma+1)m\right)\ge\sum_{S^\prime\in\mathcal{S}}Pr(BS(S_{w^\prime})=1|S_{w^\prime}=S')\cdot Pr(S_{w^\prime}=S')\)<br>
\(\ge\left(1-\frac{1050lnm}{(1-\rho)\kappa(p,q,\rho)}\cdot exp\left(-\frac{m(1-\rho)^3\kappa(p,q,\rho)}{16669800ln^3m}\right)\right)\cdot Pr(S_w\in\mathcal{S})\)<br>
\(\ge\left(1-\frac{1050lnm}{(1-\rho)\kappa(p,q,\rho)}\cdot exp\left(-\frac{m(1-\rho)^3\kappa(p,q,\rho)}{16669800ln^3m}\right)\right)\cdot\left(1-O\left(\frac{logm}{m^4log\frac{1}{\rho}}\right)\right)\)<br>
\(\ge 1-\frac{1050lnm}{(1-\rho)\kappa(p,q,\rho)}\cdot exp\left(-\frac{m(1-\rho)^3\kappa(p,q,\rho)}{16669800ln^3m}\right)-O\left(\frac{logm}{m^4log\frac{1}{\rho}}\right).\) □

Combining Lemmas 5.1, 5.12 and 5.19 we obtain the main result of this section:

Theorem 5.20. _Consider a set of m elements subject to persistent random comparison faults with probability at least q and at most p, for some constants p,q with_ \(0\le q\le p<\frac{9q+1}{8q+11}\)_. Let S be a sequence of these m elements (possibly chosen as a function of the errors), and let_ \(w_S\ge disl(S)\). `BasketSort`(_S,w<sub>S</sub>_) _is a deterministic algorithm that approximately sorts S in O(mw<sub>S</sub>_) _worst-case time. The maximum dislocation and the total dislocation of the returned sequence are at most_ \(\beta_{max}\cdot lnm\) _and_ \(\beta_{tot}\cdot m\)_, respectively, with probability_ 1-_O(m_<sup>-3</sup>)_, where_ \(\beta_{max}\ge 2\) _and_ \(\beta_{tot}\) _are constants that come from Lemma 5.12 and Lemma 5.19, respectively, and depend only on p and q._

## 6 Lower Bounds

In this section, we derive a lower bound on the maximum dislocation that can be achieved _with high probability_ by any sorting algorithm (Theorem 6.2), and a lower bound on the total dislocation that can be achieved _in expectation_ by any sorting algorithm (Theorem 6.3) even when the probability of comparison errors between pairs of distinct elements are uniform, i.e., when _q=p_ for some constant \(0<p<\frac{1}{2}\).

Throughout this section, we let set _S_={1,2_,...,n_} be the _set_ of elements to be sorted. We can think of an instance of our sorting problem as a pair \(\langle\pi,C\rangle\) where \(\pi\) is a permutation of _S_ and _C_=(_c<sub>i,j</sub>)<sub>i,j</sub>_ is an \(n\times n\) matrix that encodes the outcomes of the comparisons as seen by the sorting algorithm. More precisely, _c<sub>i,j</sub>_="_\<_" if _i_ is reported to be smaller than _j_ when comparing _i_ and _j_ and _c<sub>i,j</sub>_="_\>_" otherwise. Note that _c<sub>i,j</sub>_="_\<_" if and only if _c<sub>j,i</sub>_="_\>_", and hence in what follows, we will only define _c<sub>i,j</sub>_ for _i\<j_.

The following lemma is a key ingredient in the derivations of our lower bounds.

Lemma 6.1. _Let_ \(x,y\in S\) _with x\<y. Let A be any (possibly randomized) algorithm. On a random instance, the probability that A returns a permutation in which elements x and y appear the wrong relative order is at least_ \(\frac{1}{2}\left(\frac{p}{1-p}\right)^{2(y-x)-1}\).

<sup>9</sup>The collection of rounds considered in (i) might be empty.

