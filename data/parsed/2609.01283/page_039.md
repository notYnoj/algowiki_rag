## Encoding the update _U<sub>H</sub>_.

Given an update set \(U\subseteq E\) with |_U_|=_f_, we explicitly translate it into _U<sub>H</sub>_ as below (see Figure 1).

• **For** \((a,b)\notin M\) **(added/removed):** Apply the identical operation to (_a_<sub>2</sub>_,b_<sub>2</sub>) in Layer 2.<tbc>

• **For** \((a,b)\in M\) **(deleted):** Remove (_a_<sub>1</sub>_,b_<sub>1</sub>) from Layer 1; remove one edge each of the following forms - (_a_<sub>1</sub>_,a_<sub>2</sub>),(_b_<sub>1</sub>_,b_<sub>2</sub>),(_r<sub>a</sub>,s<sub>a</sub>),(r<sub>b</sub>,s<sub>b</sub>_); and finally add the following edges with zero cost - (_r<sub>a</sub>,r<sub>b</sub>),(s<sub>a</sub>,a_<sub>1</sub>),(_s<sub>b</sub>,b_<sub>1</sub>).

## The projection.

Given a valid \(\beta\)-factor _F_ of _H+U<sub>H</sub>_, we project it back to _G_ by defining \(M':=(M\backslash\mathrm{D})\cup\mathrm{A}\), where A is the set of non-_M_ edges whose Layer 2 copy is selected, and D is the set of base _M_-edges that are _either_ selected in Layer 1 or deleted by _U_.

**Theorem 7.7.** _G+U contains an_ \(\alpha\)_-factor if and only if H+U<sub>H</sub> contains a_ \(\beta\)_-factor. Moreover, under the costs assigned above,_

\(c(M')=c(M)+c_H(F)-\sum_{e\in U\cap M,deleted}c(e).\) (1)

_Consequently, a min-cost_ \(\alpha\)_-factor of G+U corresponds exactly to a min-cost_ \(\beta\)_-factor of H+U<sub>H</sub>, and (ignoring costs) existence transfers bi-directionally._

_Proof._ For any vertex _v_, let del(_v_) denote the number of _M_-edges deleted at _v_. The _U<sub>H</sub>_ encoding activates exactly del(_v_) sink pairs at _v_<sub>1</sub> by altering the edges incident to _r<sub>v</sub>_ and _s<sub>v</sub>_.

\((\Leftarrow)\) Let _F_ be a valid \(\beta\)-factor in _H+U<sub>H</sub>_. Observe that the update _U<sub>H</sub>_ deletes del(_v_) edges of the form (_s<sub>v</sub>,r<sub>v</sub>_) and adds del(_v_) zero-cost edges connecting _r<sub>v</sub>_ to other _r_-vertices. Thus, _r<sub>v</sub>_ maintains<tbc>

X
a = 1
a = 1
a1
b1
C1
d1
e1
a
b
Sa
Sb
Sc
Sb
Se
X
X
X
C
a = 2
ra
b
rc
rd
Te
a2
b2
c2
d2
e2
d
X
e
a = 1
a = 1
G
H

Figure 1: The reduction for _f_=1: deleting (_d,e_) in _G_ (with \(\alpha(a)=\alpha(b)=\alpha(e)=\alpha(d)=1\) and \(\alpha(c)=2\)) induces five deletions and three additions (shown in green) in _H_; the layer-1 edges are toggled out and layer-2 edges are toggled into the \(\beta\)-factor in _H+U<sub>H</sub>_, resulting in the \(\alpha\)-factor of _G+U_ consisting of the edges {(_a,b),(c,d),(c,e_)}.

