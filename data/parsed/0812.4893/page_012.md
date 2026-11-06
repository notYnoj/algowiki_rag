**Lemma 3.** _For all i_=2,3_,... it holds that_ \(f_i(R)\le f_{i-1}(R)\).

_Proof._ Consider the red turn at round _i_. The potential of a red node \(r\in R\) changes only if it receives a message. First, if _r_ receives a ‘reject’ message during round _i_, the potential of _r_ at end of round _i_ may change but it does not increase, that is, \(f_i(r)\le f_{i-1}(r)\). Second, if _r_ receives a ‘break’ message from a blue node _b_, there is a unique red node _q_ that receives an ‘accept’ message from _b_. In this case the potential of _q_ decreases from _f_<sub>_i_-1</sub>(_q_)=_w_({_q,b_}) to _f<sub>i</sub>(q_)=0 while the potential of _r_ increases from _f_<sub>_i_-1</sub>(_r_)=0 to \(f_i(r)\le w(\{r,b\})\le w(\{q,b\})=f_{i-1}(q)\). Third, if _r_ receives an isolated ‘accept’ message (without an associated ‘break’ message), \(f_i(r)=0\le f_{i-1}(r)\). The claim follows by taking the sum over all ‘reject’ messages, all ‘break’-‘accept’ matches, and all isolated ‘accept’ messages during round _i_.

**Lemma 4.** _For all i_=2,3_,... it holds that_ \(w(L_i)\ge(i-1)f_i(R)\).

_Proof._ By Lemma 2 and Lemma 3, we have

\(w(L_i)=w(L_i)-w(L_1)=\sum_{j=2}^iw(L_j)-w(L_{j-1})\ge\sum_{j=2}^if_j(R)\ge(i-1)f_i(R).\)

**Lemma 5.** _For all i_=2,3_,... it holds that_ \(w(L_i)\le(\Delta-1)w_i(B)\)

_Proof._ A blue node \(b\in B\) can lose an incident edge {_r,b_} during round _j_=2,3_,...,i_ only if _b_ is matched at the end of round _j_ with a node that _b_ prefers to _r_. Put otherwise, if \(\{r,b\}\in L_j\backslash L_{j-1}\), then \(w(\{r,b\})<w_j(b)\le w_i(b)\). The last inequality follows because each \(b\in B\), once matched, only changes to a more preferred match. Furthermore, a blue node can lose at most \(\Delta-1\) incident edges.

**Lemma 6.** _For all_ \(\gamma>0\) _and_ \(i\ge 1+(\Delta-1)/\gamma\) _it holds that_ \(f_i(R)\le\gamma w_i(B)\).

_Proof._ By Lemma 4 and Lemma 5.

## 6 Applications

### 6.1 Proof of Theorem 1

For the purpose of analysis, set _w(e_)=1 for all \(e\in E\). Then |_M<sub>i</sub>_|=_w<sub>i</sub>(B_), so Lemma 6 and \(i\ge 1+(\Delta-1)/\gamma\) imply \(f_i(R)\le\gamma|M_i|\). Denote by _u<sub>i</sub>_ the number of unstable edges in _E_\\_M<sub>i</sub>_. Because _f<sub>i</sub>(R_) counts the number of unmatched red nodes with a nonempty _C<sub>i</sub>(r_), it follows from Lemma 1 that \(u_i\le\Delta f_i(R)\). Thus, \(\gamma=\epsilon/\Delta\) gives \(u_i\le\epsilon|M_i|\) for \(i\ge 1+\Delta(\Delta-1)/\epsilon\).

We can choose an integer \(i<2+\Delta^2/\epsilon\). We can compute _M<sub>i</sub>_ in _i_ rounds or \(T=2i<4+2\Delta^2/\epsilon\) synchronous communication steps.

The proof for the case when ties in the preference lists are allowed, is analogous.

