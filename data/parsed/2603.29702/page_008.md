of the recursion tree. Each scale \(s\in\underline{[S]}\) is sampled i.i.d. with probability \(1/\mathrm{log}_M^c(n)\) for some constant 0_\<c\<_1 into the set of _active scales_ \(\tilde{S}\). For each interval on an active scale, we randomly discard half of its sub-intervals, pretending that all edges weights in those sub-intervals are 0. In total, we discard all but \(2^{-|\tilde{S}|}=2^{-\mathrm{log}^{\Omega(1)}(n)}\)-fraction of the x-axis.

Given a fixed good path, it is not hard to show that we can, with high probability, accurately estimate its true length by simply dividing its length in the surviving columns by the probability of survival, or more formally, we can change (1) to the following:

\(\mathrm{ans}[l,y_l,r,y_r]:=2\mathrm{min}_\widehat{Y}\sum_{i=1}^M\eta_i\mathrm{ans}[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i],\) (2)

where each \(\eta_i\in\{0,1\}\) is uniformly sampled, and the _i_-th sub-interval is discarded if and only if \(\eta_i=0\).

However, the algorithm may hallucinate other paths that overfit the samples, as illustrated in Fig. 4. To handle this, we first observe that if there were only one candidate path, we would have obtained a good estimate. In general the algorithm should consider exponentially many candidate paths. But our divide-and- conquer algorithm considers the path one scale at a time, and we show that, at the granularity of a typical scale, it indeed suffices to consider just a single candidate path without losing too much precision.

The key observation driving our algorithm is that we can also restrict our attention to paths of bounded "curvature." Specifically, consider an interval (_l,r_\] with sub-intervals (_m<sub>i</sub>,m_<sub>_i_+1</sub>\] for \(m_i=l+i\cdot\frac{r-l}{M}\) . To reduce the possibility of hallucinating a path that overfits the samples, we reduce the number of candidate sequences of anchors (_p(m_<sub>1</sub>)_,p(m_<sub>2</sub>)_,...,p(m_<sub>_M_-1</sub>)) that the path _p_ can have to just one single "straight- line" sequence, ideally one where for every _i_ we have<sup>10</sup> \(p(m_i)=\left\lfloor p(l)+i\frac{p(r)-p(l)}{M}\right\rfloor\), or more formally, we modify (2) to the following:

\(\mathrm{ans}[l,y_l,r,y_r]:=2\sum_{i=1}^M\eta_i\mathrm{ans}\left[m_{i-1},\left\lfloor p(l)+(i-1)\frac{p(r)-p(l)}{M}\right\rfloor,m_i,\left\lfloor p(l)+i\frac{p(r)-p(l)}{M}\right\rfloor\right].\)

<sup>10</sup>Here and throughout, we use the standard notation of \(\lfloor\cdot\rceil\) for round-to-nearest-integer, with ties e.g. rounded down.

S
= (2n-n)
S
= (2n-n)
S
= (2n-n)

Figure 3: Sub-sampling

Illustration of sub-sampling columns with branching factor _M_=4. On the left, we have \(\widetilde{S}=\{S\}\), and diagonal- shaded intervals are discarded. On the right, we have \(\widetilde{S}=\{S-1,S\}\), and diamond-grid-shaded intervals are also discarded.

