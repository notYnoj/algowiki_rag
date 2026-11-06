Thus \((\alpha'_a+\alpha'_b)\in\{0,\pm 1\}\).

_Case 1._ \(\alpha'_a+\alpha'_b=0\). So either (i) \(I_{b^\prime\prec_ab}=1\) and \(I_{a^\prime\prec_ba}=0\) or (ii) \(I_{b^\prime\prec_ab}=0\) and \(I_{a^\prime\prec_ba}=1\). In other words, in the half-integral matching \(\mathbf{q}'\): either (i) _b_ is the better of _a_’s two partners in **_q_** and _a_ is the worse of _b_’s two partners in **_q_** or (ii) _b_ is the worse of _a_’s two partners in **_q_** and _a_ is the better of _b_’s two partners in **_q_**.

Since \(\alpha'_a+\alpha'_b=0\), either \(\alpha'_a=\alpha'_b=0\) or \(\{\alpha_a,\alpha_b\}=\{1,-1\}\).

(1.1) Suppose \(\alpha'_a=\alpha'_b=0\). In case (i) above, _b_ is in the _first_ cell of \(X'_a\) and similarly, _a_ is in the _first_ cell of \(X'_b\). In case (ii), _b_ is in the _second_ cell of \(X'_a\) and similarly, _a_ is in the _second_ cell of \(X'_b\).<tbc>

(1.2) Suppose \(\{\alpha_a,\alpha_b\}=\{1,-1\}\). In case (i), _b_ is in the _second_ cell of \(X'_a\) and similarly, _a_ is in the _second_ cell of \(X'_b\). In case (ii), _b_ is in the _first_ cell of \(X'_a\) and similarly, _a_ is in the _first_ cell of \(X'_b\).

_Case 2._ \(\alpha'_a+\alpha'_b=1\). So \(I_{b^\prime\prec_ab}=I_{a^\prime\prec_ba}=1\). Hence, in the half-integral matching \(\mathbf{q}'\): _b_ is the better of _a_’s two partners in **_q_** and _a_ is the better of _b_’s two partners in **_q_**. Since \(\alpha'_a+\alpha'_b=1\), \(\{\alpha'_a,\alpha'_b\}=\{0,1\}\).<tbc>

(2.1) If \(\alpha'_a=0\) and \(\alpha'_b=1\), then _b_ is in the first cell of \(X'_a\) and similarly, _a_ is in the first cell of \(X'_b\).<tbc>

(2.2) If \(\alpha'_a=1\) and \(\alpha'_b=0\), then _b_ is in the second cell of \(X'_a\) and similarly, _a_ is in the second cell of \(X'_b\).

_Case 3._ \(\alpha'_a+\alpha'_b=-1\). So \(I_{b^\prime\prec_ab}=I_{a^\prime\prec_ba}=0\). So in the half-integral matching \(\mathbf{q}'\): _b_ is the worse of _a_’s two partners in **_q_** and _a_ is the worse of _b_’s two partners in **_q_**. Since \(\alpha'_a+\alpha'_b=-1\), \(\{\alpha'_a,\alpha'_b\}=\{0,-1\}\).

(3.1) If \(\alpha'_a=0\) and \(\alpha'_b=-1\), then _b_ is in the second cell of \(X'_a\) and _a_ is in the second cell of \(X'_b\).<tbc>

(3.2) If \(\alpha'_a=-1\) and \(\alpha'_b=0\), then _b_ is in the first cell of \(X'_a\) and _a_ is in the first cell of \(X'_b\).

Thus in all cases, we have seen that the cell with _b_ in \(X'_a\) and the cell with _a_ in \(X'_b\) are exactly aligned with each other. \(\sqcap\sqcup\)

**Lemma 12.** _M_<sub>1</sub> _and M_<sub>2</sub> _are popular in_ \(G'\).

_Proof._ We will use the vectors \(\unknown\) and \(\unknown\) defined in Section 4.2 below the statement of Theorem 11. For all \(v\in A\cup B\), we have: \(\beta_v\ge-1=\mathsf{wt}_{M_1}(v,v)\) and \(\gamma_v\ge-1=\mathsf{wt}_{M_2}(v,v)\). Claim 10 and Claim 11 show that \(\unknown\) and \(\unknown\) satisfy the other properties of witnesses we need to show. Hence _M_<sub>1</sub> and _M_<sub>2</sub> are popular in \(G'\). \(\sqcap\sqcup\)

**Claim 10** \(\sum_{u\in A^\prime\cup B^\prime}\beta_u=0\) _and_ \(\sum_{u\in A^\prime\cup B^\prime}\gamma_u=0\).

_Proof._ For every edge \((a,b)\in M_1\), we will show that \(\beta_a+\beta_b=0\). Since _M_<sub>1</sub> is a perfect matching, this implies \(\sum_{u\in A^\prime\cup B^\prime}\beta_u=0\). Let \((a,b)\in M_1\).

Suppose \(q'_{(a,b)}=1\). Then using complementary slackness as discussed in the proof of Lemma 11, we deduce \(\alpha'_a+\alpha'_b=\mathsf{wt}_{q^\prime}(a,b)=0\). So either \(\alpha'_a=\alpha'_b=0\) or \(\{\alpha'_a,\alpha'_b\}=\{-1,1\}\). In the former case, \(\beta_a=-1\) and \(\beta_b=1\); in the latter case, \(\beta_a=\alpha'_a\) and \(\beta_b=\alpha'_b\), thus \(\{\beta_a,\beta_b\}=\{-1,1\}\). Hence in all cases, we have \(\beta_a+\beta_b=0\).

Suppose \(q'_{(a,b)}=1/2\). Consider all cases in the proof of Lemma 11.

- Consider case (1.1). In sub-case (i): \(\beta_a=-1\) and \(\beta_b=1\); in sub-case (ii): \(\beta_a=1\) and \(\beta_b=-1\).<tbc>

- In case (1.2), we have \(\beta_a=\alpha'_a\) and \(\beta_b=\alpha'_b\). Since \(\{\alpha'_a,\alpha'_b\}=\{1,-1\}\), we have \(\{\beta_a,\beta_b\}=\{1,-1\}\).<tbc>

- In case (2.1) and in case (3.2), we have \(\beta_a=-1\) and \(\beta_b=1\).<tbc>

**-** In case (2.2) and in case (3.1), we have \(\beta_a=1\) and \(\beta_b=-1\).

Thus in all cases, we have \(\beta_a+\beta_b=0\). It can similarly be shown that for every edge \((a,b)\in M_2\), we have \(\gamma_a+\gamma_b=0\). Thus \(\sum_{u\in A^\prime\cup B^\prime}\gamma_u=0\). \(\sqcap\sqcup\)

**Claim 11** _For every edge_ (_a,b_) _in_ \(G'\)_, we have:_ \(\beta_a+\beta_b\ge\mathsf{wt}_{M_1}(a,b)\) _and_ \(\gamma_a+\gamma_b\ge\mathsf{wt}_{M_2}(a,b)\).

