**The Fractional Matching** \(q'\)**.** We extend **_q_** to a half-integral matching \(q'\) in \(G'\) as follows.

- for each \(e\in E\): assign \(q'_e=q_e\);<tbc>

**-** for every \(u\in U_A\cup U_B\): assign \(q'_{(u,u^\prime)}=1\).

Thus \(q'=q\cup\{(u,u'):u\in U_A\cup U_B\}\). Observe that the fractional matching \(q'\) is _perfect_ in \(G'\). This is because all vertices in \(A\cup B\) that are outside \(U_A\cup U_B\) were already (completely) matched in **_q_**. The vertices left unmatched in **_q_** are precisely those in \(U_A\cup U_B\), and each \(u\in U_A\cup U_B\) is now matched to its _twin_ \(u'\in U'_A\cup U'_B\) in \(q'\). The following lemma will be useful to us. Let \(n'=|A'\cup B'|\).

**Lemma 5.** _The half-integral matching_ \(q'\) _is popular in_ \(G'\)_, and it has a witness_ \(\alpha'\in\{0,\pm 1\}^{n^\prime}\).

_Proof._ It follows from the _special_ half-integrality of **_q_** in _G_ (no vertex is half-matched) that \(\mathsf{wt}_q(e)\in\mathbb{Z}\) for all \(e\in E\); also \(\mathsf{wt}_q(u,u)\in\{0,-1\}\) for all vertices \(u\in A\cup B\). Consider the LP with objective function \(\mathrm{min}\sum_{u\in A\cup B}\alpha_u\) and constraints (3)-(4), with **_q_** replacing **_x_** in these constraints. The total unimodularity of this system implies that **_q_** has an integral witness \(\alpha\); more precisely, \(\alpha\in\{0,\pm 1\}^n\).

Also \(\alpha_u=\mathsf{wt}_q(u,u)=q_{(u,u)}-1=0\) for every \(u\in U_A\cup U_B\) (by complementary slackness on (4)): this is because \(\alpha\) is an optimal solution to the above LP and **_q_** is an optimal solution to the dual LP that maximizes wt_<sub>q</sub>_(**_x_**) subject to constraints (5)-(6). We refer to \[27\] for details.

In order to prove the popularity of \(q'\), we will define a witness \(\alpha'\) for \(q'\) as follows: let \(\alpha'_u=\alpha_u\) for all \(u\in A\cup B\) and \(\alpha'_u=0\) for \(u\in U'_A\cup U'_B\). As \(\alpha\in\{0,\pm 1\}^n\), we have \(\alpha'\in\{0,\pm 1\}^{n^\prime}\). We need to show that \(q'\) and \(\alpha'\) satisfy constraints (2)-(6). We already know that \(q'\) satisfies (5)-(6). We will now show that (2)-(4) are satisfied.

1. \(\sum_{u\in A^\prime\cup B^\prime}\alpha'_u=0\): this follows from the definition of \(\alpha'\) and the fact that \(\sum_{u\in A\cup B}\alpha_u=0\).<tbc>

2. \(\alpha'_a+\alpha'_b\ge\mathsf{wt}_{q^\prime}(a,b)\) for all \((a,b)\in E'\): this follows from the fact that \(\alpha'_a+\alpha'_b=\alpha_a+\alpha_b\ge\mathsf{wt}_q(a,b)=\mathsf{wt}_{q^\prime}(a,b)\) for all \((a,b)\in E\). The new edges in \(G'\) are \((u,u')\) for \(u\in U_A\cup U_B\) and we have \(\alpha'_u+\alpha'_{u^\prime}=0=\mathsf{wt}_{q^\prime}(u,u')\).<tbc>

3. \(\alpha'_v\ge-1=\mathsf{wt}_{q^\prime}(v,v)\) for all \(v\in A'\cup B'\).

Thus the half-integral matching \(q'\) is popular in \(G'\) with witness \(\alpha'\). \(\square\)

It was shown in \[27\] that any popular fractional matching that is perfect can be written as a convex combination of popular matchings; moreover, these popular matchings can be efficiently computed. Theorem 11<tbc>

UA
UA
A
UB
UB

**Fig.5.** Vertices in gray sets, i.e., in \(U'_A\cup U'_B\), are the new vertices in \(G'\) and the new edges are \((u,u')\) for \(u\in U_A\cup U_B\). The edges shown here are in the half-integral matching \(q'\).

