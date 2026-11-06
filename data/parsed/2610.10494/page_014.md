Each \(Q(\varepsilon_j)\) is a restriction of \(T^{\otimes N}\). To form the displayed weighted sum from their direct sum, identify the corresponding variables on all three legs and scale the variables on one leg of copy _j_ by _c<sub>j</sub>_. These are allowed linear substitutions, proving (8). Applying a character and taking _N_-th roots gives

\(\lambda(S)\le(NL+1)^{1/N}\lambda(T).\)

Letting \(N\rightarrow\infty\) proves \(\lambda(S)\le\lambda(T)\). No continuity assumption on \(\lambda\) is needed.

## Appendix E. Replicating a convolution

_Proof of Lemma 2.2._ Put _P(t_)=_t<sup>m</sup>_-1. Repeated polynomial division writes the inputs uniquely as

\(F=\sum_{a=0}^{r-1}F_aP^a,G=\sum_{b=0}^{s-1}G_bP^b,\mathrm{deg}F_a,\mathrm{deg}G_b<m.\)

These are invertible linear coordinates: the basis polynomials _t<sup>d</sup>P<sup>a</sup>_ have distinct leading degrees _ma+d_. On the output retain the analogous blocks _H<sub>c</sub>_ for \(0\le c<r+s-1\). They use _m(r+s_-1) independent coordinates, within the original output length _m(r+s_)-1. Divide each _F<sub>a</sub>G<sub>b</sub>=Q<sub>ab</sub>+PR<sub>ab</sub>_ with deg_Q<sub>ab</sub>,_deg_R<sub>ab</sub>\<m_. Scale input blocks _a,b_ by \(\varepsilon^{-a},\varepsilon^{-b}\) and output block _c_ by \(\varepsilon^c\). The transformed product has

\(H_c=\sum_{a+b=c}Q_{ab}+\varepsilon\sum_{a+b=c-1}R_{ab}.\)

Let \(\alpha_1,\dots,\alpha_m\) be the distinct roots of _P_. Since \(Q_{ab}(\alpha_h)=F_a(\alpha_h)G_b(\alpha_h)\), the limit gives

\(H_c(\alpha_h)=\sum_{a+b=c}F_a(\alpha_h)G_b(\alpha_h)(1\le h\le m).\)

Evaluation at _m_ distinct points is invertible on each block of degree less than _m_. The resulting coordinates therefore give _m_ independent convolutions of lengths _r,s_. The evaluation step is the usual diagonalization of cyclic convolution \[5, Theorem 5 and Section 5.1\]; the displayed scalings prove the degeneration, with coefficient degree at most one.

## Appendix F. Counting and rescaling

We give the complete counting argument and justify the real-length profiles used in Sections 3- 4.

To prove (10), fix an integer \(q\ge 1\) and put \(m=\lfloor N\mathrm{log}_2q\rfloor\). Monotonicity in dimension and \(B_i(q)^{\otimes N}\cong B_i(q^N)\) give

\(2^{mp_i}\le\lambda(B_i(q))^N\le 2^{(m+1)p_i}.\)

Take _N_-th roots and let \(N\rightarrow\infty\). The interval \[0,1\] follows from \(1\le\lambda(B_i(2))\le 2\).

_Proof of Lemma 3.3._ For every tuple \(\sum_hn_h=N\), applying \(\lambda\) to (13) gives

\(2M\lambda(T)^N\ge M^{1+p_i}\prod_h\lambda(T_h)^{n_h}.\)

Put \(a_h=\lambda(T_h)^{1/p_i}\). Cancel _M_ and take the power 1_/p<sub>i</sub>_:<tbc>

\(M\prod_ha_h^{n_h}\le 2^{1/p_i}\lambda(T)^{N/p_i}.\)

