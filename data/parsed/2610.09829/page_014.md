## Edge selection gadget.

We construct the edge selection gadget _F_ as follows (see Figure 6).

(i) Construct a cycle _C=v_<sub>0</sub>_...v_<sub>_p_-1</sub>_v_<sub>0</sub> of length _p=L_+4_m_+2; we assume that for \(i\ge p\), _v<sub>i</sub>=v_<sub>_i_mod_p_</sub>.<tbc>

(ii) For each \(i\in[m]\), construct

- a (_v_<sub>2_i_-1</sub>_,v_<sub>2_i_+2_m_-2</sub>)-path _P<sub>i</sub>_ of length _L_-2_m_+1,<tbc>

- a \((v_{2i+2m-1},v_{2i+2m+\ell-1})\)-path _Q<sub>i</sub>_ of length \(\ell\),<tbc>

- a \((v_{2i+2m+\ell},v_{2i+4m+\ell-1})\)-path \(P'_i\) of length _L_-2_m_+1,<tbc>

**-** a \((v_{2i+4m+\ell},v_{2i+4m+2\ell})\)-path \(Q'_i\) of length \(\ell\).

Notice that for each \(i\in[m]\), the length of _P<sub>i</sub>_ and \(P'_i\) is odd. We select the middle edges of these paths and denote them by _e<sub>i</sub>_ and \(e'_i\), respectively. We say that the _m_-tuples (_e_<sub>1</sub>_,...,e<sub>m</sub>_) and \((e'_1,\dots,e'_m)\) are _roots_ of _F_. For \(i\in[m]\), we say that _e<sub>i</sub>_ and \(e'_i\) are opposite. For every \(i\in[m]\), we denote by \(C_i,C'_i,S_i,S'_i\) the cycles obtained from the paths \(P_i,P'_i,Q_i,Q'_i\), respectively, by connecting their endpoints by the shortest paths in the cycle _C_.

The properties of the edge selection gadget are summarized in the following lemma.

**Lemma 4.1.** _The edge selection gadget F has the following properties:_

(_i)_ \(\Delta(F)\le 3\) _and the endpoints of the root edges are of degree two,_<tbc>

Q2
Qm
Q1
P' 1
em
V2m+l+1
e'
Pm
V2m+1
e2
V2m
V4m+l+1
P' 2
P2
V4m+l+2
e1
v1
e' m
P1
Vo = V4m+L+2
P' m
C
Q' m
Q'2

Figure 6: Construction of the edge selection gadget. Notice that because \(2m-1<\ell\), _P<sub>m</sub>_ has one endpoint on the shortest path in _C_ between the endpoints of _Q_<sub>1</sub> and, symmetrically, \(P'_m\) has one endpoint on the shortest path in _C_ between the endpoints of \(Q'_1\).

