_Proof._ Let (_a,b_) be any edge in \(G'\). We will show that \(\beta_a+\beta_b\ge\mathsf{wt}_{M_1}(a,b)\). The proof that \(\gamma_a+\gamma_b\ge\mathsf{wt}_{M_2}(a,b)\) will be analogous. We know that \(\alpha'_a+\alpha'_b\ge\mathsf{wt}_{q^\prime}(a,b)\) (since \((\mathbf{q}',\unknown')\in\mathcal{L}_G\)). Let us consider the following cases:

1. \(\alpha'_a=\alpha'_b=1\): in this case \(\beta_a=\beta_b=1\). We have \(\beta_a+\beta_b=2\ge\mathsf{wt}_{M_1}(a,b)\).<tbc>

2. \(\alpha'_a=\alpha'_b=-1\): since \(\mathsf{wt}_{q^\prime}(a,b)\le\alpha'_a+\alpha'_b\), this means \(\mathsf{wt}_{q^\prime}(a,b)\le-2\), i.e., \(\mathsf{wt}_{q^\prime}(a,b)=-2\).<tbc>

- So _a_ prefers both its partners in \(\mathbf{q}'\) to _b_ and similarly, _b_ prefers both its partners in \(\mathbf{q}'\) to _a_. Hence both _a_ and _b_ prefer their respective partners in _M_<sub>1</sub> to each other. Thus wt<sub>_M_<sub>1</sub></sub>(_a,b_)=-2. Since \(\beta_a,\beta_b\ge-1\), we have \(\beta_a+\beta_b\ge\mathsf{wt}_{M_1}(a,b)\).<tbc>

3. \(\alpha'_a=0\) and \(\alpha'_b=-1\): so \(\mathsf{wt}_{q^\prime}(a,b)\le\alpha'_a+\alpha'_b=-1\). We have \(\beta_a=\beta_b=-1\) here (see Fig. 14, left).<tbc>

- Since \(\mathsf{wt}_{q^\prime}(a,b)\le-1\), either both \(\mathsf{vote}_a(b,\mathbf{q}'),\mathsf{vote}_b(a,\mathbf{q}')\) are at most -1/2 or one of \(\mathsf{vote}_a(b,\mathbf{q}')\), \(\mathsf{vote}_b(a,\mathbf{q}')\) is 0 and the other is -1. In both cases, _a_ and _b_ prefer their more preferred partners in \(\mathbf{q}'\) to each other. Moreover, _a_ and _b_ are matched in _M_<sub>1</sub> to their more preferred partners in \(\mathbf{q}'\). Thus \(\mathsf{wt}_{M_1}(a,b)=-2=\beta_a+\beta_b\).<tbc>

4. \(\alpha'_a=0\) and \(\alpha'_b=1\): so \(\mathsf{wt}_{q^\prime}(a,b)\le\alpha'_a+\alpha'_b=1\). Here \(\beta_a=-1\) and \(\beta_b=1\) here (see Fig. 14, right).<tbc>

- If \(q'_{(a,b)}>0\) then \(\mathsf{wt}_{q^\prime}(a,b)=\alpha'_a+\alpha'_b=1\), i.e., \(q'_{(a,b)}=1/2\) (since \(\mathsf{wt}_{q^\prime}(a,b)\) is odd). So \(\mathsf{vote}_a(b,\mathbf{q}')=\mathsf{vote}_b(a,\mathbf{q}')=1/2\). In other words, _a_ and _b_ are each other’s more preferred partners in \(\mathbf{q}'\). Observe that when \(\alpha'_a=0\) and \(\alpha'_b=1\), _a_ and _b_ are matched in _M_<sub>1</sub> to their more preferred partners in \(\mathbf{q}'\). Thus \((a,b)\in M_1\) and we have \(\beta_a+\beta_b=0=\mathsf{wt}_{M_1}(a,b)\).<tbc>

**-** Suppose \(q'_{(a,b)}=0\). Since \(\mathsf{wt}_{q^\prime}(a,b)\le 1\), we have \(\mathsf{vote}_a(b,\mathbf{q}')\le 0\) or \(\mathsf{vote}_b(a,\mathbf{q}')\le 0\). This means one of _a,b_ prefers its more preferred partner in \(\mathbf{q}'\) to the other. Since _a_ and _b_ are matched in _M_<sub>1</sub> to their more preferred partners in \(\mathbf{q}'\), we have \(\mathsf{wt}_{M_1}(a,b)\le 0=\beta_a+\beta_b\).<tbc>

<tbc>The cases where \(\alpha'_a\in\{\pm 1\}\) and \(\alpha'_b=0\) are analogous to case 3 and case 4.<tbc>

5. \(\{\alpha'_a,\alpha'_b\}=\{-1,1\}\). Suppose \(\alpha'_a=-1\) and \(\alpha'_b=1\). We have \(\beta_a=-1\) and \(\beta_b=1\) here, also \(\mathsf{wt}_{q^\prime}(a,b)\le 0\).<tbc>

- If \(q'_{(a,b)}>0\) then \(\alpha'_a+\alpha'_b=0=\mathsf{wt}_{q^\prime}(a,b)\). So _b_ is matched in _M_<sub>1</sub> either to _a_ or to a neighbor preferred to _a_. Hence, \(\mathsf{wt}_{M_1}(a,b)\le 0=\beta_a+\beta_b\).<tbc>

**-** Suppose \(q'_{(a,b)}=0\). Since \(\mathsf{wt}_{q^\prime}(a,b)\le 0\), either (i) one of _a,b_ prefers both its partners in \(\mathbf{q}'\) to the other or (ii) both _a,b_ like their more preferred partner in \(\mathbf{q}'\) to each other. In both cases, one of _a,b_ is matched in _M_<sub>1</sub> to a neighbor preferred to the other. Thus \(\mathsf{wt}_{M_1}(a,b)\le 0\), hence \(\beta_a+\beta_b=0\ge\mathsf{wt}_{M_1}(a,b)\).<tbc>

<tbc>The case where \(\alpha'_a=1\) and \(\alpha'_b=-1\) is analogous.<tbc>

6. \(\alpha'_a=\alpha'_b=0\): here we have \(\beta_a=-1\) and \(\beta_b=1\), also \(\mathsf{wt}_{q^\prime}(a,b)\le 0\).<tbc>

Ba = -1
Ya = 1
Ba = -1
Ya = 1
X'a
b'
b"
b'
b"
X'a
X'b
a'
a"
a'
a"
X'b
Bb = -1
Yb = -1
Bb = 1
Yb = 1

**Fig.14.** The case where \(\alpha'_a=0\) and \(\alpha'_b=-1\) is shown on the left and the case where \(\alpha'_a=0\) and \(\alpha'_b=1\) is shown on the right. In both cases, we have \(b'\succ_ab''\) and \(a'\succ_ba''\).

