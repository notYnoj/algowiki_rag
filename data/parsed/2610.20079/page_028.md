<tbc>For \(N\ge M^2\), we also have \(N\ge\widehat{M^2}\) and may apply Proposition 8.2. Since \(p\ge h\), the parameter relations and the scan cost of layout conversion give

\(O\big(\frac{N}{\widehat{B}}\big[1+\frac{\widehat{p}}{\widehat{a}^\tau\widehat{h}^\varepsilon}\big]\big)=O\big(\frac{N}{B}\big[1+\frac{p}{a^\tau h^\varepsilon}\big]\big).\)

This preserves the large-input bound. For \(M\le N\le M^2\), local sorting satisfies \((h/a)^\tau=h/(a^\tau h^\varepsilon)\le logN/(a^\tau h^\varepsilon)\); for \(N\ge M^2\), we have \(p\le logN\). Combining the two cases gives (2).

Finally, if _M\<C_<sub>∗</sub>, then _B_ is bounded, so the _O(N_) cost of Lemma 8.3 is also _O(N/B_) and satisfies both the large-input and main bounds. For local sorting, \(n\le M^2\) is bounded as well, and direct comparison sorting suffices. The simulations, subarray sorts, and merges preserve correctness, the _M_-word memory bound, and polynomial disk space.

## B Exact Verification of the Fixed Parameters

The exponent requires only a coarse logarithm bound and an exact rational comparison; high- precision numerical logarithms are unnecessary.

**Lemma B.1** (A strict inequality for the exponent)**.** For _m_=512, \(\varepsilon=3/200000=1.5\times 10^{-5}\), and \(\eta=33/338432\), we have \(\varepsilon lnm<\eta\).

_Proof._ The first four terms of the exponential series give<tbc>

\(e^{7/10}>1+\frac{7}{10}+\frac{(7/10)^2}{2}+\frac{(7/10)^3}{6}=\frac{12013}{6000}>2.\)

<tbc>Thus ln2_\<_7/10 and ln512=9ln2_\<_63/10. Direct multiplication gives

\(\eta-\varepsilon\frac{63}{10}=\frac{15909}{5288000000}>0.\)

The claimed strict inequality follows.

**Corollary B.2** (A finite block length)**.** Let \(D\ge 1\) be the startup delay of the finite gate schedule, including any relay vertices used to remove parallel edges. Taking \(k=\lceil D(1-\eta)/\eta\rceil+1\) bits at each source gives common rate \(k/(k+D)>1-\eta\).

_Proof._ The chosen integer satisfies \(k>D(1-\eta)/\eta\). Rearranging gives the claim, and the pipeline construction in Section 5.4 realizes that rate.

## C Arbitrary Field Widths and Prefix Counts

The recursion in Section 6 requires width _t_<sub>0</sub>_m<sup>k</sup>_ and a prefix-segment count divisible by _W<sup>k</sup>_. An actual array may satisfy neither condition, and directly padding its prefix count can increase the data volume too much. We first take a few high-order digits from the fields being interchanged, using existing data to create enough segments, then pad their count to the required multiple. Once the count is sufficiently large, padding costs only a constant factor in volume. We decompose the remaining width into recursive scales and interchange the corresponding pairs. Keep the parameters of that section, with \(t_0=\Theta(log(M/B))\).

