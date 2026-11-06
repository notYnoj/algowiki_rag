## 5 Simultaneous Tensor Contraction

### 5.1 The Coppersmith-Winograd Tensor as Aggregated Tensor Contractions

In this section, we show that powers of the little CW and big CW tensors have natural interpretations in terms of tensor contractions associated with tripartitions. As a bilinear map, we may interpret the little CW tensor as taking inputs \(a^{(0)}\in\mathbb{C}\), \(a^{(1)}\in\mathbb{C}^n\), \(b^{(0)}\in\mathbb{C}\), \(b^{(1)}\in\mathbb{C}^n\), and computing<tbc>

\(c^{(0)}=(a^{(1)})^Tb^{(1)},c^{(1)}=a^{(0)}b^{(1)}+a^{(1)}b^{(0)}.\) (25)

<tbc>Following notation we used for tripartitions before, we may label the variables in the trilinear forms as _X_={_X_<sup>({})</sup>_,X_<sup>({0})</sup>}, _Y_={_Y_<sup>({})</sup>_,Y_<sup>({0})</sup>}, _Z_={_Z_<sup>({})</sup>_,Z_<sup>({0})</sup>}, and write the CW tensor as

\(\phi_\mathrm{CW}(X,Y,Z)=\sum_{i=0}^{n-1}\big(X_i^{(\{\})}Y_i^{(\{\})}Z^{(\{0\})}+X_i^{(\{\})}Y^{(\{0\})}Z_i^{(\{\})}+X^{(\{0\})}Y_i^{(\{\})}Z_i^{(\{\})}\big).\) (26)

Here, we label each component of _X_, _Y_, _Z_ by the (possibly empty) subset of indices that is excluded from the variable. The index space is {0}, and hence the only two such subsets are {} and {0}.

Recall our definition of tripartitions _B<sub>s,t,v</sub>_ in (13), and define all tripartitions as

\(P_w=\bigcup_{s,t,v\in\mathbb{Z}_{\ge 0}s+t+v=w}B_{s,t,v}.\) (27)

For higher tensor powers, let \(d\ge 1\). We have the following relation (recall Definition 2).

**Lemma 1.**

\(\phi_\mathrm{CW}^{\otimes d}(X,Y,Z)=\sum_{(U,V,W)\in P_d}\sum_{\mathbf{i}\in[\unknown 0,n-1]^d}X_{\mathbf{i}|_{U^c}}^{(U)}Y_{\mathbf{i}|_{V^c}}^{(V)}Z_{\mathbf{i}|_{W^c}}^{(W)}.\) (28)

_Proof._ The claim follows by induction on _d_. _P<sub>d</sub>_ may be obtained by adding an item to one of the three parts of each tripartition in _P_<sub>_d_-1</sub>. These are exactly the terms we get in \(\phi_\mathrm{CW}^{\otimes d}\), since \(\phi_\mathrm{CW}^{\otimes d}=\phi_\mathrm{CW}^{\otimes(d-1)}\otimes\phi_\mathrm{CW}\), \(\phi_\mathrm{CW}^{\otimes(d-1)}\) contains the terms in _P_<sub>_d_-1</sub> by induction, and (26) maps \(\phi_\mathrm{CW}\) to an item in _U_, _V_, or _W_.

Coppersmith and Winograd consider a restriction of this tensor by zeroing out blocks of variables _X_<sup>(_U_)</sup>, _Y_ <sup>(_V_)</sup>, _Z_<sup>(_W_)</sup> for some choices of _U_, of _V_ , and of _W_. Ultimately, they obtain a set of independent matrix- matrix products with border rank at most (_n_+2)_<sup>d</sup>_. This bound follows by tensoring the (_n_+2)-term little CW degeneration _d_ times; zeroing variable blocks cannot increase the resulting number of rank-one terms. Appendix C.4 gives the smaller bound _n_<sup>3</sup>+6_n_<sup>2</sup> for the balanced cube, whose six matrix products share variable blocks.

The big CW tensor similarly gives contractions indexed by incomplete tripartitions. In each tensor-power term, write \(F=G\sqcup H\), where the factors on _G_ come from the little CW tensor and those on _H_ from the three additional scalar terms. The two tripartitions \(U\sqcup V\sqcup W=G\) and \(\bar{U}\sqcup\bar{V}\sqcup\bar{W}=H\) specify these choices. As a bilinear map, the big CW tensor may be interpreted as taking inputs \(a^{(0)},\hat{a}^{(0)},b^{(0)},\hat{b}^{(0)}\in\mathbb{C}\) and \(a^{(1)},b^{(1)}\in\mathbb{C}^n\), and computing

\(c^{(0)}=a^{(0)}\hat{b}^{(0)}+\hat{a}^{(0)}b^{(0)}+(a^{(1)})^Tb^{(1)},\hat{c}^{(0)}=a^{(0)}b^{(0)},c^{(1)}=a^{(0)}b^{(1)}+a^{(1)}b^{(0)}.\) (29)

We write \(X^{(S,\bar{S})}\) for a variable block of order _d_-|_S_| that omits coordinates _S_. Within _S_, the subset \(\bar{S}\) selects the additional scalar variable (index _n_+1), and \(S\backslash\bar{S}\) selects the original scalar variable (in dex 0). In a tensor-power term, the _X_-block thus has \(S=U\cup H\) and \(\bar{S}=\bar{U}\subseteq H\). For the big CW tensor, we then have _X_={_X_<sup>({},{})</sup>_,X_<sup>({0},{})</sup>_,X_<sup>({0},{})</sup>}, _Y_={_Y_<sup>({},{})</sup>_,Y_<sup>({0},{})</sup>_,Y_<sup>({0},{})</sup>}, _Z_={_Z_<sup>({},{})</sup>_,Z_<sup>({0},{})</sup>_,Z_<sup>({0},{})</sup>}, with

\(\phi_\mathrm{BCW}(X,Y,Z)=\phi_\mathrm{CW}(\{X^{(\{\},\{\})},X^{(\{0\},\{\})}\},\{Y^{(\{\},\{\})},Y^{(\{0\},\{\})}\},\{Z^{(\{\},\{\})},Z^{(\{0\},\{\})}\})\) (30)

\(+X^{(\{0\},\{\})}Y^{(\{0\},\{\})}Z^{(\{0\},\{0\})}\) (31)

\(+X^{(\{0\},\{\})}Y^{(\{0\},\{0\})}Z^{(\{0\},\{\})}\) (32)

\(+X^{(\{0\},\{0\})}Y^{(\{0\},\{\})}Z^{(\{0\},\{\})}.\) (33)

