### C.5 Three PSD matrix bounds

**Lemma C.5** (PSD off-block bound)**.** _If_ \(S\unknown 0\) _and B<sub>E</sub>,B<sub>F</sub> are orthonormal frames for orthogonal subspaces, then_ \(\|B_E^\top SB_F\|_F^2\le\mathrm{tr}(B_E^\top SB_E)\mathrm{tr}(B_F^\top SB_F)\).

_Proof._ The block is \((S^{1/2}B_E)^\top(S^{1/2}B_F)\), so \(\|B_E^\top SB_F\|_F\le\|S^{1/2}B_E\|_F\|S^{1/2}B_F\|_F\); square and use \(\|S^{1/2}B_E\|_F^2=\mathrm{tr}(B_E^\top SB_E)\), likewise for _B<sub>F</sub>_.

**Lemma C.6** (PSD product bound)**.** _For_ \(A,B\in\mathbb{S}_+^p\), \(\|AB\|_F^2\le\|A\|_\mathrm{op}\|B\|_\mathrm{op}\langle A,B\rangle\).

_Proof._ Since \(A^2\unknown\|A\|_\mathrm{op}A\) and \(B^2\unknown\|B\|_\mathrm{op}B\), and trace pairings of PSD matrices preserve the Loewner order, \(\|AB\|_F^2=\mathrm{tr}(A^2B^2)\le\|A\|_\mathrm{op}\mathrm{tr}(AB^2)\le\|A\|_\mathrm{op}\|B\|_\mathrm{op}\mathrm{tr}(AB)\).

**Lemma C.7** (Projection lower bound)**.** _Let_ \(W\in\mathbb{S}_+^p\) _and let P<sub>E</sub> be the orthogonal projector onto a subspace_ \(E\subseteq\mathbb{R}^p\)_. Then_ \(W\unknown aP_E\) _for some a\>_0 _if and only if_ \(E\subseteq\mathrm{ran}(W)\)_; in that case, when_ \(W\neq 0\)_, one may take_ \(a=\lambda_+(W)\)_, the smallest positive eigenvalue of W._

_Proof._ Necessity: if \(W\unknown aP_E\) and \(z\in\mathrm{ker}(W)\), then \(0=z^\top Wz\ge a\|P_Ez\|_2^2\), so _P<sub>E</sub>z_=0; hence \(\mathrm{ker}(W)\perp E\), i.e. \(E\subseteq\mathrm{ker}(W)^\perp=\mathrm{ran}(W)\). Sufficiency: for every _x_, \(x^\top Wx\ge\lambda_+(W)\|P_{\mathrm{ran}(W)}x\|_2^2\), and \(E\subseteq\mathrm{ran}(W)\) gives \(\|P_{\mathrm{ran}(W)}x\|_2\ge\|P_Ex\|_2\), so \(x^\top Wx\ge\lambda_+(W)x^\top P_Ex\).

_Remark_ C.8 (Positive definiteness on _E_ is not enough). The condition \(E\subseteq\mathrm{ran}(W)\) in Theorem C.7 cannot be replaced by "_W_ is positive definite on _E_", which only says \(E\cap\mathrm{ker}(W)=\{0\}\). For \(W=\left(1111\right)\) and _E_=span{_e_<sub>1</sub>}, the quadratic form \((te_1)^\top W(te_1)=t^2\) is positive on _E_, yet det(_W-aP<sub>E</sub>_)=-_a\<_0 for every _a\>_0, so no inequality \(W\unknown aP_E\) holds. In Theorem D.2 the stronger condition is available for both anchors because ran(_X_<sub>sc</sub>)=_U_ and ran(_S_<sub>sc</sub>)=_V_ .

## D Proofs of the Rigidity Theorem

Throughout, Theorem 3.1 is in force, endpoints are written \(\bar{Z}=\bar{X}-\sigma\bar{S}\) with \((\bar{X},\bar{S})\in\mathcal{X}_\star\times\mathcal{S}_\star\), and we use the conventions of Appendix C. Recall \(a_X=\lambda_\mathrm{min}(X_\mathrm{sc}|_U)>0\) and \(a_S=\lambda_\mathrm{min}(S_\mathrm{sc}|_V)>0\) from Theorem C.3, and set

\(R_X:=\mathrm{max}_{X\in\mathcal{X}_\star}\|X_\mathrm{sc}-X\|_F,R_S:=\mathrm{max}_{S\in\mathcal{S}_\star}\|S_\mathrm{sc}-S\|_F,\) (D.1)

finite by compactness. The implications of Theorem 3.2 are proved in the order (i)\(\Rightarrow\)(ii) (Appendix D.3), (ii)\(\Rightarrow\)(iii) (Appendix D.4), (iii)\(\Rightarrow\)(iv)\(\Rightarrow\)(i) and (iii)\(\Rightarrow\)(v)\(\Rightarrow\)(ii) (Appendix D.5). The "automatic" clause is Theorem D.1, and the \(\sigma\)-independence clause holds because (3.8) does not involve \(\sigma\) while the constants in (i), (iii), (iv) do.

### D.1 Interior endpoints: both identities and the linearization are automatic

**Lemma D.1** (Automatic interior identities)**.** _For_ \(\bar{S}\in\mathrm{ri}\mathcal{S}_\star\) _the primal identity in_ (3.8) _holds, and for_ \(\bar{X}\in\mathrm{ri}\mathcal{X}_\star\) _the dual identity holds. Moreover, for every_ \(\bar{Z}\in\mathrm{ri}\mathcal{Z}_\star\),

\(\mathcal{C}(\bar{Z})=\mathcal{D}=T_{\mathcal{Z}_\star}(\bar{Z}),\) (D.2)

_without any of the conditions (i)-(v)._

