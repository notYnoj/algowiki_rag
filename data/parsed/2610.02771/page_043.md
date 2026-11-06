## E Detailed algorithms

This section gives the full pseudocode for the routines described in Section 3. The PAC theorems in the main text assume that valid anchors _c<sub>k</sub>_ satisfying \(|\mu_k-c_k|\le\sigma\) are supplied. If anchors are not supplied but the means are known to lie in \([-\lambda,\lambda]\), the algorithms call MEDIANEST (Algorithm 1 in Appendix A) for each arm and then run the BAI routine with the remaining confidence budget. This adds the localization cost stated in Remark 1.

**Algorithm 2** One randomized tail-integral query, TAILINTEGRALQUERY

**Require:** arm _k_, anchor _c<sub>k</sub>_, clipping level \(L\ge\sigma\), variance proxy \(\sigma\)

1: Set \(\alpha_L\leftarrow 1+log(L/\sigma)\) and \(g_L(t)\leftarrow[\alpha_Lmax\{\sigma,t\}]^{-1}\) for \(t\in[0,L]\)

2: Draw \(S\in\{+1,-1\}\) uniformly and draw _T∼g<sub>L</sub>_

3: **if** _S_=+1 **then**

4: Query arm _k_ with threshold set \([c_k+T,\infty)\) and observe \(Y=\mathbf{1}\{X_k\ge c_k+T\}\)

5: **else**

6: Query arm _k_ with threshold set \((-\infty,c_k-T]\) and observe \(Y=\mathbf{1}\{X_k\le c_k-T\}\)

7: **end if**

8: **return** \(Z\leftarrow 2SY/g_L(T)\)

**Algorithm 3** FIXEDCLIP-1BITBAI

**Require:** arms A=\[_K_\], variance proxy \(\sigma\), accuracy \(\varepsilon\), confidence \(\delta\), anchors \((c_k)_{k=1}^K\) or range \(\lambda\)

1: **if** anchors are not supplied **then**

2: **for** _k_=1_,...,K_ **do**

3: \(c_k\leftarrow\text{MEDIANEST}(k,\lambda,\sigma,\delta/(2K))\)

4: **end for**

5: Set \(\delta_0\leftarrow\delta/2\)

6: **else**

7: Set \(\delta_0\leftarrow\delta\)

8: **end if**

9: Set \(L_\varepsilon\leftarrow 2\sigma^2/\varepsilon\), \(\gamma\leftarrow\delta_0/K\)

10: **for** _k_=1_,...,K_ **do**

11: Initialize an empty list Z_<sub>k</sub>_

12: Append TAILINTEGRALQUERY\((k,c_k,L_\varepsilon,\sigma)\) to Z_<sub>k</sub>_

13: **end for**

14: **loop**

15: **for** _k_=1_,...,K_ **do**

16: \(N_k\leftarrow|\mathcal{Z}_k|\), \(\widehat{\mu}_k\leftarrow c_k+N_k^{-1}\sum_{Z\in\mathcal{Z}_k}Z\)

17: \(\beta_k\leftarrow\beta_\varepsilon(N_k,\gamma)\)

18: \(\text{LCB}_k\leftarrow\widehat{\mu}_k-\beta_k\), \(\text{UCB}_k\leftarrow\widehat{\mu}_k+\beta_k\)

19: **end for**

20: **for** _k_=1_,...,K_ **do**

21: \(B_k\leftarrow max_{\ell\neq k}\text{UCB}_\ell-\text{LCB}_k\)

22: **end for**

23: \(h\leftarrow argmin_{k\in\mathcal{A}}B_k\), \(\ell\leftarrow argmax_{a\neq h}\text{UCB}_a\)

24: **if** \(B_h\le\varepsilon\) **then**

25: **return** _h_

26: **end if**

27: \(k_t\leftarrow argmax_{a\in\{h,\ell\}}\beta_a\)

28: Append TAILINTEGRALQUERY\((k_t,c_{k_t},L_\varepsilon,\sigma)\) to Z_<sub>k<sub>t</sub></sub>_

29: **end loop**

