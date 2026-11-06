**Algorithm 11** CheckAliased(_q_) -- 2-lane \((\tilde{\sigma},\chi)\)

**Require:** _q_ -- a _k_-permutation state; alias pairs \((x_0^{(0)},x_1^{(0)})\) on \(\ell_0\) and \((x_0^{(1)},x_1^{(1)})\) on \(\ell_1\) with indices \((i_0^{(0)},i_1^{(0)})\), \((i_0^{(1)},i_1^{(1)})\)

**Ensure:** Verifies whether _q_ completes a valid solution under Controlled Aliasing

1: Let _t_ be the target

2: \(b\leftarrow q\).split, \(b'\leftarrow 1-b\)

3: \(\mathrm{Sum}_b\leftarrow\sum_{x\in\ell_b}x\); \(\mathrm{Sum}_{b^\prime}\leftarrow\sum_{x\in\ell_{b^\prime}} x\)

4: \(s_\mathrm{real}\leftarrow q\).sum \(\triangleright\) true sum on split _b_

5: \(\mathsf{Memo}'\leftarrow\mathsf{Memo}_{b^\prime}\) \(\triangleright\) maps \(\tilde{\sigma}\) to two buckets \(\chi\in\{0,1\}\)

6: \((u_0,u_1)\leftarrow(x_0^{(b^\prime)},x_1^{(b^\prime)})\triangleright\) alias pair on the other half

7: **function** TestDirectOnRight(_s_) \(\triangleright\) seek _B_ with \(\sigma(B)=t-s\)

8: **for** \(\chi_R\in\{0,1\}\) **do**

9: \(\tilde{\sigma}_R\leftarrow\mathrm{AliasedValue}\big(t-s,\chi_R,u_0,u_1\big)\)

10: **if** \(\tilde{\sigma}_R\in\mathsf{Memo}'\) **and** \(\mathsf{Memo}'[\tilde{\sigma}_R][\chi_R]\neq\perp\) **then**

11: **return true**

12: **return false**

13: **function** TestRightComplement(_s_) \(\triangleright\) seek _B_ with \(\sigma(\ell_{b^\prime}\backslash B)=t-s\)

14: \(g\leftarrow\mathrm{Sum}_{b^\prime}-(t-s)\triangleright\) goal real sum for _B_

15: **for** \(\chi_R\in\{0,1\}\) **do**

16: \(\tilde{\sigma}_R\leftarrow\mathrm{AliasedValue}\big(g,\chi_R,u_0,u_1\big)\)

17: **if** \(\tilde{\sigma}_R\in\mathsf{Memo}'\) **and** \(\mathsf{Memo}'[\tilde{\sigma}_R][\chi_R]\neq\perp\) **then**

18: **return true**

19: **return false**

_Intra-half direct/self-complement:_

20: **if** _s_<sub>real</sub>=_t_ **or** Sum_<sub>b</sub>-s_<sub>real</sub>=_t_ **then**

21: **Output:** direct solution found

22: **return**

_Cross-half patterns:_

23: **if** TestDirectOnRight(_s_<sub>real</sub>) **then**

24: **Output:** direct across splits; **return**

25: **if** TestRightComplement(_s_<sub>real</sub>) **then**

26: **Output:** mixed (right-complement); **return**

27: \(s_\mathrm{comp}\leftarrow\mathrm{Sum}_b-s_\mathrm{real}\)

28: **if** TestDirectOnRight(_s_<sub>comp</sub>) **then**

29: **Output:** mixed (left-complement); **return**

30: **if** TestRightComplement(_s_<sub>comp</sub>) **then**

31: **Output:** double complement; **return**

## D Experimental Details

We provide additional data and methodology for the experiments summarized in Section 7. Our aim is not to claim new empirical bests, but to validate the central prediction of our theory: for fixed _n_, the wall-time of IC-SubsetSum closely tracks the size of the constructive certificate \(U=|\Sigma(S)|\).

