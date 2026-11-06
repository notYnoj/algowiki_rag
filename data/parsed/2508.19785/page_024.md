\(1-9w\cdot exp(-w\cdot\kappa(p,q,\rho)).\) Whenever this is the case, \(rank(x,B)-\rho\frac{w}{2}\le pos(x,A)\le rank(x,B)+\rho\frac{w}{2}\) and the claim follows by combining such inequality with \(|x-\tau_w(x)|=|rank(x,B)-pos(x,A)|\). □

We now show that if all elements are good w.r.t. _w_, they are also likely to all be good w.r.t. \(\lfloor\rho w\rfloor\).

Lemma 5.10. _Consider a round of_ `BasketSort` _having window size w. If all elements in S<sub>w</sub> are good w.r.t. w, then all elements in_ \(S_{\lfloor\rho w\rfloor}\) _are good w.r.t._ \(\rho w\) _with probability at least_ \(1-9mw\cdot exp\left(-w\cdot\kappa(p,q,\rho)\right)\).

Proof. Notice that, since all elements in \(\sigma\) are good w.r.t. _w_, they are also happy w.r.t. _w_. Then, using Lemma 5.9 and the union bound, we have that all elements _x_ satisfy \(|x-\tau_w(x)|\le\rho\frac{w}{2}\) with probability at least \(1-9mw\cdot exp\left(-w\cdot\kappa(p,q,\rho)\right)\).

Suppose that this is indeed the case and focus on a single element _x_. For all elements _y_ with \(y<x-\rho w\), we have \(\tau_w(y)\le y+\rho\frac{w}{2}<x-\rho\frac{w}{2}\le\tau_w(x)\). Similarly, for all elements _y_ with \(y>x+\rho w\), we have \(\tau_w(y)\ge y-\rho\frac{w}{w}>x+\rho\frac{w}{2}\ge\tau_w(x)\). In other words, \(x-\rho w\le\sigma_{\lfloor\rho w\rfloor}(x)\le x+\rho w\), i.e., \(|\sigma_{\lfloor\rho w\rfloor}(x)-x|\le\rho w\). Since both _x_ and \(\sigma_{\lfloor\rho w\rfloor}(x)\) are integers, \(|\sigma_{\lfloor\rho w\rfloor}(x)-x|\le\lfloor\rho w\rfloor\) implying that _x_ is good w.r.t. \(\lfloor\rho w\rfloor\). □

We can use the above result to give a lower bound to the probability that all elements remain good for all sufficiently large window sizes.

Lemma 5.11. _Consider an execution of_ `BasketSort` _with_ \(w_S\ge disl(S)\)_. With probability at least_ \(1-O\big(\frac{logm}{m^4log\frac{1}{\rho}}\big)\)_, all elements_ \(x\in S\) _are good w.r.t. all window sizes w with_ \(w\ge\frac{6}{\kappa(p,q,\rho)}lnm\) _considered by the algorithm._

Proof. We start by focusing on a generic round having window size \(w\ge\frac{6}{\kappa(p,q,\rho)}lnm\). If all elements are good w.r.t. _w_, then all elements are also happy w.r.t. _w_ and Lemma 5.10 ensures that the maximum dislocation of \(\sigma_{\lfloor\rho w\rfloor}\) is at most \(\lfloor\rho w\rfloor\) with probability at least

\(1-9mw\cdot exp\left(-w\cdot f\left(p,\rho\right)\right)\ge 1-9mw\cdot exp(-6lnm)\ge 1-9m^2\cdot\frac{1}{m^6}=1-\frac{9}{m^4},\)

and, whenever this happens, all elements are alo good w.r.t. \(\lfloor\rho w\rfloor\).

Since all elements are good w.r.t. the window size \(w_S\le m\), we have that the probability that all elements remain good w.r.t. all the \(O(log_{1/\rho} m)\) subsequent window sizes _w_ such that \(w\ge\frac{6}{\kappa(p,q,\rho)}lnm\) is at least \(1-O\left(\frac{log_{1/\rho} m}{m^4}\right)=1-O\left(\frac{logm}{m^4log\frac{1}{\rho}}\right)\). □

Whenever all elements are good w.r.t. all window sizes \(w=\Omega(logm)\), the dislocation of the sequence returned by `BasketSort` is _O_(log_m_), which allows us to prove the following:

Lemma 5.12. _The maximum dislocation of the sequence returned by_ `BasketSort` _with_ \(w_S\ge disl(S)\) _is at most_ \(\frac{9}{\rho(1-\rho)}+\frac{54}{\rho(1-\rho)\cdot\kappa(p,q,\rho)}lnm\) _with probability at least_ \(1-O\big(\frac{logm}{m^4log\frac{1}{\rho}}\big)\).

Proof. Let _w_ be the smallest window size _w_ that satisfies \(w\ge\frac{6}{\kappa(p,q,\rho)}lnm\).<sup>5</sup> By Lemma 5.11, all elements are good w.r.t. _w_ with probability at least \(1-O(\frac{logm}{m^4log\frac{1}{\rho}})\). When this is indeed the case, the maximum dislocation of \(\sigma_w\) is at most \(w<\frac{1}{\rho}+\frac{6}{\rho\cdot\kappa(p,q,\rho)}lnm\), where we used \(\lfloor\rho w\rfloor<\frac{6}{\kappa(p,q,\rho)}lnm\).<tbc>

<sup>5</sup>If no such window size exists, then \(w_S<\frac{6}{\kappa(p,q,\rho)}lnm\), and, by the algorithm’s precondition and by Lemma 5.5, the maximum dislocation of the returned sequence is at most \((1+\frac{8}{1-\rho})w_S<\frac{6}{\kappa(p,q,\rho)}+\frac{48}{(1-\rho)\cdot\kappa(p,q,\rho)}\), which satisfies the claim.

