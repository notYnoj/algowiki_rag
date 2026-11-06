<tbc>To the best of our knowledge, there is no previous work showing how to generate a realization of Ber(_p_) of either type (ii) or type (iii) in _O_(1) expected time with _O(n_) worst-case space. However, as we see in Section 4, these two types of Bernoulli random variates play a crucial role in our optimal DPSS algorithm. We prove the following theorem:

Theorem 3.1. _Consider a Bernoulli random variate, Ber(p), in the form of either p=p_<sup>∗</sup> _or_ \(p=\frac{1}{2p^*}\)_, with_ \(p^*=\frac{1-(1-q)^n}{n\cdot q}\) _, where q is a rational number represented by a pair of O_(1)_-word numerator and denominator, n is a O_(1)_-word integer, and_ \(n\cdot q\le 1\)_; Ber(p_) _can be generated in O_(1) _expected time with O(n_) _worst-case space._

_Definition 3.2 (i-Bit Approximation)._ Consider a value _p_, possibly comprising an infinite sequence of bits. An _i-bit approximation_ of _p_, denoted by \(\tilde{p}_i\), is an approximation value of the _i_ most-significant bits in _p_, i.e., satisfies \(|\tilde{p}_i-p|\le 2^{-i}\), while \(\tilde{p}_i\) itself consists of at most _i_+1 bits.

We prove Theorem 3.1 via the following algorithmic framework of Bringmann and Friedrich \[7\]:

Fact 2 (\[7, 10\]). _Consider a Bernoulli random variate, Ber(p_) _with rational parameter_ \(p\in(0,1)\)_. Suppose the numerator and the denominator of p both can be represented with O(n_) _words, and p can be evaluated in O(poly(n_)) _time and the i-bit approximation,_ \(\tilde{p}_i\)_, of p can be evaluated in O(poly(i_)) _time. Then Ber(p_) _can be generated in O_(1) _expected time with O(n_) _worst-case space in the Word RAM model._

Lemma 3.3. \[<sup>∗</sup>\] _These two claims hold simultaneously: (i) the numerator and the denominator of p=p_<sup>∗</sup> _both can be represented with O(n_) _words and p can be evaluated in O(poly(n_)) _time; and (ii) there exists an algorithm that can evaluate each i-bit approximation_ \(\tilde{p}_i\) _of p=p_<sup>∗</sup>_, satisfying all conditions stated in Theorem 3.1, in O(poly(i_)) _time._

Lemma 3.4. \[<sup>∗</sup>\] _These two claims hold simultaneously: (i) the numerator and the denominator of_ \(p=\frac{1}{2p^*}\) _both can be represented with O(n_) _words and p can be evaluated in O(poly(n_)) _time; and (ii) there exists an algorithm that can evaluate each i-bit approximation_ \(\tilde{p}_i\) _of_ \(p=\frac{1}{2p^*}\)_, satisfying all conditions stated in Theorem 3.1, in O(poly(i_)) _time._

## 3.2 Geometric Random Variate Generation in the Word RAM Model

Consider a parameter \(p\in(0,1)\). The _Geometric distribution_ Geo(_p_) takes _discrete_ values in N. Specifically, Pr\[Geo(_p_)=_i_\]=_p_(1-_p_)<sup>_i_-1</sup>, for \(i\in\mathbb{N}\). As the value of a geometric variate can be arbitrarily large (though it is not really likely), thus in theory, it is impossible to generate variates from a geometric distribution with worst-case bounded space.

**Bounded Geometric Variates.** Nonetheless, in many application scenarios, including our optimal DPSS algorithm, geometric random variates within a bounded range are sufficient. This is known as the _Bounded Geometric distribution_. Given an integer \(n\in\mathbb{N}\), the bounded geometric distribution, denoted by B-Geo(_p,n_), is defined as min{_n,_Geo(_p_)} with distribution:

\(Pr[\text{B-Geo}(p,n)=i]=\left\{\begin{array}{ c c }
p(1-p)^{i-1} & i\in\{1,\cdots,n-1\}; \\
(1-p)^{n-1} & i=n.
\end{array}\right.\)

Bringmann and Friedrich \[7\] studied the generation of bounded geometric random variates in the Word RAM model and gave the following theorem:

Fact 3 (\[7\]). _Let_ \(p\in(0,1)\) _be a rational number with numerator and denominator fitting in O_(1) _words and n be a positive integer fitting in O_(1) _words. A random variate from_ B-Geo(_p,n_)=min{_n,_Geo(_p_)} _can be realized in O_(1) _expected time and O(n_) _space in the worst case._

