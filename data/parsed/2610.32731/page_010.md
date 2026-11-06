On the other hand, consider the vertices in \(S\cap X\). Since _S_ is an antichain in _F_, also \(S\cap X\) is an antichain in _F_\[_X_\]. Let _Y_ be the smallest prefix containing \(S\cap X\). Then \(S\cap X\) contains precisely the leaves of _Y_ , so \(|S\cap X|=s(F,Y)\). Further note that \(Y\subseteq X\), since _X_ is a prefix, so in particular \(|Y|\le|X|=k-1\).

This implies that \(|S\cap X|=s(F,Y)\le s(F,k)\) by observation 6, and \(s(F,k)\le\mathrm{OPT}(F,k)+1\) by lemma 5. Overall, we have \(c(F,U)=|S|=|S\backslash X|+|S\cap X|\le 2\mathrm{OPT}(F,k)+2\), which is equivalent to the desired inequality.

Our final bound, used only for theorem 3, combines the ideas above with an information- theoretical lower bound. Recall that a forest is _k_-unbounded if all leaves have depth _k_ or more.

**Lemma 8** (\[KKZZ18, Theorem 12\])**.** _Let F be a disjoint union of m paths of length k. Then_ \(\mathrm{OPT}(F,k)\ge\Omega(m\mathrm{log}(k/m))\).

_Proof sketch._ By a standard combinatorial argument, there are \(\genfrac(){pt}{2}{m+k-1}{m-1}\) possible distributions of the smallest _k_ elements to the _m_ paths. Any algorithm finding the _k_-th smallest element must find the smallest _k_ elements to certify its result. By the information theoretic lower bound, this requires \(\mathrm{log}\genfrac(){pt}{2}{m+k-1}{m-1}\ge\Omega(m\mathrm{log}(k/m))\) comparisons.

**Lemma 9.** _Let_ \(k\in\mathbb{N}_+\) _and let F be a k-unbounded forest with m roots. Then_ \(\mathrm{OPT}(F,k)\ge\Omega(m\mathrm{log}(k/m))\).

_Proof._ First observe that _F_, due to being _k_-unbounded, must contain a prefix _U_ that induces the disjoint union of _m_ paths, each of length _k_. Since _U_ may contain the _k_ smallest nodes, selection on (_G,k_) is no easier than selection on (_G_\[_U_\]_,k_). Lemma 8 yields the desired lower bound for _G_\[_U_\].

**Theorem 10.** _Let_ \(k,k'\in\mathbb{N}_+\) _with_ \(k'<k\) _and let F be a k-unbounded forest. Let_ \(m=c^*(T,k')\)_. Then_ \(\mathrm{OPT}(F,k)\ge\Omega(m\mathrm{log}\frac{k-k'}{m})\).

_Proof._ By definition of _c_<sup>∗</sup>, there exists a prefix _U_ of _F_ of size at most \(k'\) with _c(F,U_)=_m_. That implies that \(F'=F-U\) has _m_ roots. Consider instances of the selection problem for (_F,k_) where the |_U_| smallest nodes are precisely _U_. Solving the problem on this subset of instances is the same as solving the selection problem for \((F',k-|U|)\). Thus, \(\mathrm{OPT}(F,k)\ge\mathrm{OPT}(F',k-|U|)\).

Observe that \(F'\) is (_k_-|_U_|)-unbounded. Thus, by lemma 9, we have \(\mathrm{OPT}(F',k-|U|)\ge\Omega(m\mathrm{log}\frac{k-|U|}{m})\). Since \(k-|U|\ge k-k'\), this concludes the proof.

## 4 Weighted soft heaps

In this section, we describe our new _weighted soft heap_ data structure. We start by formally defining classical soft heaps, mostly following Kaplan, Kozma, Zamir, and Zwick \[KKZZ18\]. Our definition has some small technical differences due to the need to store multiple copies<tbc>

