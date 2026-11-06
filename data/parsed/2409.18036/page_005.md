### 2.2 Dynamic Parameterized Subset Sampling

Consider a set of _n items S_={_x_<sub>1</sub>_,...,x<sub>n</sub>_}; each item has a _weight w(x<sub>i</sub>_) which is a _non-negative_ integer. Without loss of generality, we assume that the largest possible value of _n_, denoted by _n_<sub>max</sub> and the largest possible value of the item weights, denoted by _w_<sub>max</sub> can be represented with one word (of _d_ bits) in the Word RAM model. Therefore, \(d\in\Omega(log(n_{max}\cdot w_{max}))\) holds all the time.

Define \(W_S(\alpha,\beta)=\alpha\cdot\sum_{x\in S}w(x)+\beta\) as the _parameterized total weight function_ of all the items in _S_ by two parameters \(\alpha\) and \(\beta\), where both \(\alpha\) and \(\beta\) are _non-negative rational numbers_ and each can be represented by a _O_(1)-word numerator and a _O_(1)-word denominator. Thus, the parameterized total weight \(W_S(\alpha,\beta)\) of _S_ fits in _O_(1) words. Furthermore, if the value of \(\sum_{x\in S}w(x)\) is pre-computed and maintained, the value of \(W_S(\alpha,\beta)\) can be computed in _O_(1) time.

Given a pair of parameters \((\alpha,\beta)\), a _parameterized subset sampling query_ on _S_ asks for a subset \(T\subseteq S\) such that each item \(x\in S\) is selected in _T_ independently, with probability \(p_x(\alpha,\beta)=min\left\{\frac{w(x)}{W_S(\alpha,\beta)},1\right\}\). Moreover, the expected size of _T_ is defined as \(\mu_S(\alpha,\beta)=\sum_{x\in S}p_x(\alpha,\beta)\). Observe that since the parameters \((\alpha,\beta)\) are given on-the-fly in a parameterized subset sampling query, the sampling probability of each item can be vastly different with different parameters \((\alpha,\beta)\).

In this paper, we study the problem of parameterized subset sampling on a _dynamic setting_, where the item set _S_ can be updated by insertions of new items (associated with a weight) and deletions of existing items from _S_. We call this problem the _Dynamic Parameterized Subset Sampling_ (DPSS) problem. It is worth mentioning that in the DPSS problem, the sampling probability of each item is not only affected by the parameters \((\alpha,\beta)\), but also by the updates on _S_. To see this, consider a fixed pair \((\alpha,\beta)\); before and after the insertion of an item with a very large weight, the value of \(W_S(\alpha,\beta)\) can change significantly and hence, such an update dramatically changes the sampling probabilities of all the items.

Our goal is to design a data structure for solving the DPSS problem such that: (i) it can be constructed in _O(n_) time and consumes _O_(|_S_|) space at all times, (ii) it can answer every parameterized subset sample query in \(O(1+\mu_S(\alpha,\beta))\) expected time, and (iii) it supports each update to _S_ in _O_(1) worst-case time.

## 3 Sampling Random Variates in the Word RAM Model

In this section, we discuss how to exactly and efficiently sample, in the Word RAM model, the key random variates in our optimal DPSS algorithm. Due to the importance of random variate generation, we believe that these new algorithms would be of independent interest to other problems.

As we see in the next section, our algorithm needs to generate a number of variants of _Bernoulli_ and _Geometric_ random variates. We explore each in turn.

### 3.1 Bernoulli Random Variate Generation in the Word RAM Model

Consider a real number \(p\in(0,1)\), the _Bernoulli distribution_ parameterized by _p_, denoted by Ber(_p_), takes values in {0,1} with probability Pr\[Ber(_p_)=1\]=1-Pr\[Ber(_p_)=0\]=_p_. In particular, our algorithm needs to generate the following three types of Bernoulli random variates, Ber(_p_):<br>
**type (i)** _p_ is a _rational number_ with numerator and denominator both fitting in _O_(1) words;<br>
**type (ii)** _p=p_<sup>∗</sup>, where \(p^*=\frac{1-(1-q)^n}{n\cdot q}\) , where _q_ is a rational number represented by a pair of _O_(1)-word numerator and denominator, _n_ is a _O_(1)-word integer, and \(n\cdot q\le 1\);<br>
**type (iii)** \(p=\frac{1}{2p^*}\), with _p_<sup>∗</sup> as in type (ii).<br>
For type (i), Bringmann and Friedrich \[7\] proved the following result:

FACT 1 (\[7\]). _If p is a rational number with numerator and denominator being O_(1)_-word integers, then Ber(p_) _can be evaluated in O_(1) _expected running time, and O_(1) _worst-case space._

