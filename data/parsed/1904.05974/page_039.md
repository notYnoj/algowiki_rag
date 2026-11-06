## Appendix: Proof of Theorem 11 (derived from \[27\])

_Proof._ Consider any \(a\in A'\). Since \(\mathbf{q}'\) is half-integral, the vertex _a_ has at most 2 partners in \(\mathbf{q}'\). Call these 2 partners _b_ and \(b'\): it could be the case that \(b=b'\). If \(b=b'\) then we have \(q'_{(a,b)}=1\); else \(q'_{(a,b)}=q'_{(a,b^\prime)}=1/2\). We will form an array \(X'_a\) with 2 cells (each of length 1/2) as follows. In case _a_ has a single partner _b_ in \(\mathbf{q}'\) then both cells of \(X'_a\) have _b_ in them. Else, recalling that \(\alpha'\in\{0,\pm 1\}^{n^\prime}\) (where \(n'=|A'\cup B'|\)) and assuming without loss of generality that \(b\prec_ab'\):

- if \(\alpha'_a\in\{\pm 1\}\), then \(X'_a=(b,b')\), i.e., _a_’s partners in \(\mathbf{q}'\) are arranged in _increasing_ order of _a_’s preference order.<tbc>

**-** if \(\alpha'_a=0\) then \(X'_a=(b',b)\), i.e., _a_’s partners in \(\mathbf{q}'\) are arranged in _decreasing_ order of _a_’s preference order.

Consider any \(b\in B'\). Since \(\mathbf{q}'\) is half-integral, the vertex _b_ has at most 2 partners in \(\mathbf{q}'\). Call these 2 partners _a_ and \(a'\): it could be the case that \(a=a'\). If \(a=a'\) then we have \(q'_{(a,b)}=1\); else \(q'_{(a,b)}=q'_{(a^\prime,b)}=1/2\). We will form an array \(X'_b\) with 2 cells (each of length 1/2) as follows. In case _b_ has a single partner _a_ in \(\mathbf{q}'\) then both cells of \(X'_b\) have _a_ in them. Else, assuming without loss of generality \(a\prec_ba'\):

- if \(\alpha'_b\in\{\pm 1\}\), then \(X'_b=(a',a)\), i.e., _b_’s partners in \(\mathbf{q}'\) are arranged in _decreasing_ order of _b_’s preference order.<tbc>

**-** if \(\alpha'_b=0\), then \(X'_b=(a,a')\), i.e., _b_’s partners in \(\mathbf{q}'\) are arranged in _increasing_ order of _b_’s preference order.

Define sets _M_<sub>1</sub> and _M_<sub>2</sub> as follows:

\(M_1=\{(u,v):u\in A'\cup B'\text{and}v\text{is in the first cell of}X'_u\}\)<br>
\(M_2=\{(u,v):u\in A'\cup B'\text{and}v\text{is in the second cell of}X'_u\}.\)

We will now adapt the proof from \[27\] to show in Lemma 11 and Lemma 12 that both _M_<sub>1</sub> and _M_<sub>2</sub> are popular matchings in \(G'\). Thus \(\mathbf{q}'=(I_{M_1}+I_{M_2})/2\) for popular matchings _M_<sub>1</sub> and _M_<sub>2</sub> in \(G'\). \(\square\)

**Lemma 11.** _M_<sub>1</sub> _and M_<sub>2</sub> _are matchings in_ \(G'\).

_Proof._ For any vertex \(u\in A\cup B\), we need to show that if \((a,b)\in M_1\) (resp., _M_<sub>2</sub>) then there is no other edge incident to either _a_ or _b_ in _M_<sub>1</sub> (resp., _M_<sub>2</sub>). If \(q'_{(a,b)}=1\), then \(X'_a\) has the vertex _b_ in both cells and similarly, \(X'_b\) has the vertex _a_ in both cells. Thus (_a,b_) is the only edge incident to _a_ and to _b_ in both _M_<sub>1</sub> and _M_<sub>2</sub>.

Suppose \(q'_{(a,b)}=1/2\). We need to show that _b_ is in the first (resp., second) cell of \(X'_a\) if and only if _a_ is in the first (resp., second) cell of \(X'_b\). It was shown in \[27\] that the LP that leads to the formulation of the popular fractional matching polytope (constraints (2)-(6) for the graph \(G'\)) is _self-dual_, i.e., the dual LP is same as the primal LP. So \((\mathbf{q}',\alpha')\) is both a primal optimal and a dual optimal solution. Complementary slackness implies that for every edge (_a,b_) such that \(q'_{(a,b)}>0\), we have \(\alpha'_a+\alpha'_b=\mathsf{wt}_{q^\prime}(a,b)\); in other words, the edge covering constraint for edge (_a,b_) is _tight_. So we have:<tbc>

\(\alpha'_a+\alpha'_b=\sum_{b^\prime:b^\prime\prec_ab}q'_{(a,b^\prime)}-\sum_{b^\prime:b^\prime\prec_ab}q'_{(a,b^\prime)}+\sum_{a^\prime:a^\prime\prec_ba}q'_{(a^\prime,b)}-\sum_{a^\prime:a^\prime\prec_ba}q'_{(a^\prime,b)}.\)

<tbc>Since \(\mathbf{q}'\) is a half-integral matching and \(q'_{(a,b)}=1/2\), there is a unique neighbor \(b'\neq b\) of _a_ such that \(q'_{(a,b^\prime)}=1/2\). Similarly, there is a unique neighbor \(a'\neq a\) of _b_ such that \(q'_{(a^\prime,b)}=1/2\). Let \(I_{b^\prime\prec_ab}\) be the indicator variable that is 1 if \(b'\prec_ab\) and it is 0 otherwise. Similarly for \(I_{b^\prime\prec_ab},I_{a^\prime\prec_ba}\), and \(I_{a^\prime\prec_ba}\). Hence:

\(\alpha'_a+\alpha'_b=\frac{1}{2}\cdot(I_{b^\prime\prec_ab}-I_{b^\prime\prec_ab}+I_{a^\prime\prec_ba}-I_{a^\prime\prec_ba})=(2\cdot I_{b^\prime\prec_ab}-1+2\cdot I_{a^\prime\prec_ba}-1)/2\)<br>
\(=I_{b^\prime\prec_ab}+I_{a^\prime\prec_ba}-1.\)

