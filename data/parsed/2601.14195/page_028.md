<tbc>We already noted that (2,2)-e3-sat instances satisfy \(m=\frac{4}{3}n\) and that \(n\in 3\mathbb{N}\). Let

\(q=1-\varepsilon,\)<br>
\(k=\left\lfloor N^{1-\varepsilon}\right\rfloor=\left\lfloor N^q\right\rfloor,\)<br>
\(r=n/3,\)<br>
\(X=8n+2m=32r,\text{and}\)<br>
\(Y=6m=24r.\)

Then

\(N=8n+2m\left(1+3\left\lfloor N^{1-\varepsilon}\right\rfloor\right)\)<br>
\(=X+Y\cdot k\)<br>
\(=r(32+24k),\)

where the non-negative integer \(k=\lfloor N^q\rfloor\) must satisfy \(k^{1/q}\le X+Y\cdot k<(k+1)^{1/q}\). A suitable _k_ must exist - consider the continuous function \(\phi(k)=k^{1/q}-Y\cdot k\) for \(k\in[0,\infty)\). Clearly, by \(q\in(0,1)\) and \(X\in\mathbb{N}\), \(\phi(0)=0\) and \(lim_{k\rightarrow\infty}\phi(k)=\infty\). Notice, furthermore, that \(\phi\) is convex, has a unique minimum and two (not necessarily distinct) _x_-axis intercepts at _k_<sub>0</sub>=0 and \(k_1\in[0,\infty)\) such that \(\phi\) is non-positive on \[_k_<sub>0</sub>=0_,k_<sub>1</sub>\], and strictly positive and monotonically increasing on \((k_1,\infty)\). By the intermediate value theorem, there must exist a point _t_<sub>∗</sub>_\>_0 such that \(\phi(t_*)=X\). By _X\>_0, clearly _t_<sub>∗</sub>_\>k_<sub>1</sub>. Let \(k_*=\lfloor t_*\rfloor\). By definition, \(k_*\le t_*<k_*+1\), so by being monotonically increasing on \((k_1,\infty)\), we must have that \(\phi(k_*)\le\phi(t_*)=X<\phi(k_*+1)\), which is equivalent to \(k_*^{1/q}-Y\cdot k_*\le X<(k_*+1)^{1/q}-Y\cdot(k_*+1)\). Adding \(Y\cdot k_*\) to all parts of the inequality, and keeping in mind that _Y_=6_m\>_0, yields \(k_*^{1/q}\le X+Y\cdot k_*<(k_*+1)^{1/q}-Y<(k_*+1)^{1/q}\) as above. This establishes the existence of an appropriate construction with _N_ agents.

We set out to argue that the reduction can be performed in polynomial time (in the size of _B_), so let us show how to choose such a suitable value of _k_ that ensures that \(k=\lfloor N^{1-\varepsilon}\rfloor\) efficiently. Note that if \(k\ge\frac{X}{Y}=\frac{32r}{24r}=\frac{4}{3}\), then \(X+Y\cdot k\le 2Y\cdot k\), so from \(k^{1/q}\le X+Y\cdot k\) we get that \(k\le(X+Y\cdot k)^q\le(2Y\cdot k)^q\). Rearranging, multiplying both sides by 1_/k<sup>q</sup>_ and keeping in mind that _k\>_0, we get \(k^{1-q}\le(2Y)^q\) and so \(k\le(2Y)^\frac{q}{1-q}\). Thus, finally, we get that \(0\le k\le k_\text{max}\), where \(k_\text{max}=\left\lceil max\left\{\frac{X}{Y},(2Y)^\frac{q}{1-q}\right\}\right\rceil\). Thus, the search for _k_ (and hence for _N_) requires at most \(O(k_\text{max})=O(r^\frac{q}{1-q})=O(n^\frac{1-\varepsilon}{\varepsilon})\) time, by considering at all integers between 0 and _k_max, which is polynomial in _n_ (as \(\varepsilon\) is fixed) and thus also in the size of _B_ as required.

## 5 Efficient Algorithms for Very Short Preference Lists

While we have shown strong intractability results even in cases where preference lists are of bounded length, we will now consider the case where preference lists are very short. As has been shown for similar optimisation problems such as MinBP-AlmostStable-sri and MinBP- AlmostStable-Max-smi, preference lists of length at most 2 guarantee a sufficiently simple instance structure to allow for optimal algorithms that can be executed in polynomial time. In Section 5.1, we will give such an algorithm for minimax matchings in sri. Then, in Section 5.2, we will extend our algorithm to the Max-smi case. Although the setting where preference lists are of length at most 2 is very constrained, we highlight that these algorithms apply whenever choices are very limited. Furthermore, the algorithms can also be useful in the following scenario: agents may indicate their top 2 choices, then we compute a minimax almost-stable maximum- cardinality matching, and then we find a maximum-cardinality matching among the remaining unmatched agents. This ensures desirable stability guarantees with respect to the top 2 choices of agents, and, subject to this, minimises the number of unmatched agents.

