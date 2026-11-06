**Lemma 4.1** (Rescaled profiles)**.** _The limit in_ (18) _exists. The profiles g<sub>ij</sub> are continuous, coordinatewise nondecreasing, and satisfy_<tbc>

\(min\{r,s\}\le g_{ij}(r,s)\le r+s,g_{ij}(r,s)=g_{ji}(s,r),g_{ij}(tr,ts)=tg_{ij}(r,s).\) (19)

<tbc>_For p<sub>i</sub>\>_0, \(g_{ij}^{1/p_i}\) _is concave in s and satisfies_

\(g_{ij}(r,3s+r)^{1/p_i}\ge 2g_{ij}(r,s)^{1/p_i}+g_{ik}(r,s)^{1/p_i}.\) (20)

_For p<sub>j</sub>\>_0, \(g_{ij}^{1/p_j}\) _is concave in r. All lengths and scale factors here may be arbitrary positive reals._

The discrete inequalities thus become inequalities about homogeneous curves. The additive -1 in (16) disappears at this scale. The proof first compares rational lengths at a common integer scale; homogeneity and monotonicity then give continuity and the real extension. Appendix F includes that argument and verifies that rounding the lengths in (18) does not change the limit.

## 5. Common slopes and the angular constraint

With the profile properties from Lemma 4.1, we can now relate the three dot-product parameters \(p_i\in[0,1]\). Comparing the growth of differently oriented convolutions leads to the angular constraint in Proposition 5.2. This is the only result from this section needed for the running-time bounds in Section 6.

Index the three tensor legs by 1,2,3. Full proofs of this section’s slope and growth claims are in Appendix G.

**Lemma 5.1** (Common slopes and affine bounds)**.** _Fix i with p<sub>i</sub>\>_0_, and let j,k be the other legs. The functions P<sub>ij</sub>(s_)=_g<sub>ij</sub>_(1_,s_)<sup>1_/p<sub>i</sub>_</sup> _and P<sub>ik</sub>(s_)=_g<sub>ik</sub>_(1_,s_)<sup>1_/p<sub>i</sub>_</sup> _have a common asymptotic slope L<sub>i</sub>\>_0_. There are offsets satisfying_<tbc>

\(c_{ij},c_{ik}\ge 0,c_{ij}+c_{ik}\le 1,\) (21)

<tbc>_such that, for all real s,t\>_0,

\(P_{ij}(s+t)\ge P_{ij}(s)+L_it,L_is\le P_{ij}(s)\le L_i(s+c_{ij}),\)

_and likewise for P<sub>ik</sub>._

Concavity gives each curve a limiting slope. The coupled tripling inequalities force the two slopes to agree. Writing _R=P<sub>ij</sub>+P<sub>ik</sub>_, they also give \(R(3s+1)\ge 3R(s)\); iteration yields \(R(s)\le L_i(2s+1)\). Consequently the two curves stay above their common limiting line, and their normalized vertical offsets are nondecreasing with sum at most one. Their limits are _c<sub>ij</sub>,c<sub>ik</sub>_. This explains both the affine bounds and the constraint on their sum.

**Proposition 5.2** (Angular constraint)**.** _The dot-product parameters of every tensor character satisfy_

\(\sum_{i=1}^3arccos\sqrt{p_i}\ge\frac{\pi}{2}.\) (22)

_Proof outline._ If some _p<sub>i</sub>_=0, its summand is already \(\pi/2\). Assume all three parameters are positive. For this outline, suppose _g=g<sub>ij</sub>_ is differentiable. The increment and upper bounds in<tbc>

