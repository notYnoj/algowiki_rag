For a tripartition (_U,V,W_) of _F_, metric preservation in Claim 1, applied in each coordinate, gives

\(\sum_{\mathbf{i}\in\unknown 0,n-1\unknown^F}X_{\mathbf{i}|_{U^c}}^{(U)}Y_{\mathbf{i}|_{V^c}}^{(V)}Z_{\mathbf{i}|_{W^c}}^{(W)}=\sum_{\mathbf{i}\in\unknown 0,n+1\unknown^F}\Phi_{U,F}(X^{(U)})_\mathbf{i}\Phi_{V,F}(Y^{(V)})_\mathbf{i}\Phi_{W,F}(Z^{(W)})_\mathbf{i},\) (62)

a decomposition of the contraction into (_n_+2)_<sup>d</sup>_ rank-one terms. The right-hand side is also defined for sets that do not form a tripartition. If |_U_|+|_V_|+|_W_|=_d_, such a choice omits some coordinate in at least two blocks, so the second or third identity of Claim 1 makes the sum zero. Consequently, for a balanced conflict-free family, aggregating the embedded blocks preserves the selected products and eliminates all mixed products.

## 5.5 Full Bilinear Algorithm for Simultaneous Contraction

We now combine the embeddings introduced in the preceding subsections into a full algorithm for simultaneous matrix multiplication. The algorithm is relatively simple and exact, and hence may be of practical interest, though the corrections introduced in Section 5.6 give a strictly smaller rank bound. Throughout this subsection, let

\(d=3N.\) (63)

Exact-rank bounds for these balanced families of compatible tripartitions are already known. Flavi, Jelisiejew, and Michałek \[20, Corollary 6.11 and Proposition 6.13\] bound the rank of the full balanced little- CW restriction, including its shared variable blocks. Their result implies that every conflict-free family \(\mathcal{S}\subseteq B_{N,N,N}\) satisfies

\(R\big(\langle n^N,n^N,n^N\rangle^{\oplus|\mathcal{S}|}\big)\le(n+2)^{3N}-\genfrac(){pt}{2}{3N}{2N+1}(n+1)^{N-1}.\) (64)

The algorithm below gives an explicit aggregation formula with the simpler known budget (_n_+2)<sup>3_N_</sup>.

Recall the combined embedding \(\Phi_{S,F}\) and its transpose from Definition 12. Here \(\langle A,B\rangle=\sum_\mathbf{i}A_\mathbf{i}B_\mathbf{i}\), without complex conjugation. We have

\(\big\langle\Phi_{S,F}^\star(T),Z\big\rangle=\big\langle T,\Phi_{S,F}(Z)\big\rangle\forall Z\in(\mathbb{C}^n)^{\otimes|F\backslash S|}.\) (65)

Algorithm 1 first embeds and sums the _A_ input blocks, and does the same for the _B_ input blocks. It multiplies the two aggregates entrywise, then applies \(\Phi_{W_s,F}^\star\) to recover each output _C_<sup>(_s_)</sup>. Thus by one aggregate evaluation, the algorithm computes _m_ independent contractions.

**Theorem 2** (Correctness of Algorithm 1)**.** _If_<tbc>

\(\mathcal{S}=\{(U_s,V_s,W_s)\}_{s=1}^m\subseteq B_{N,N,N}\) (66)

<tbc>_satisfies_<tbc>

\(U_i\sqcup V_j\sqcup W_\ell=F\Longrightarrow i=j=\ell,\) (67)

<tbc>_then Algorithm 1 computes the m simultaneous contractions_<tbc>

\(C_\unknown^{(s)}=\sum_{\mathbf{i}\in\unknown 0,n-1\unknown^d\mathbf{i}|_{W_s^c}=\unknown} A_{\mathbf{i}|_{U_s^c}}^{(s)}B_{\mathbf{i}|_{V_s^c}}^{(s)}.\) (68)

<tbc>_In particular, this gives a bilinear algorithm of rank at most_<tbc>

\((n+2)^d=(n+2)^{3N}.\) (69)

<tbc>_Proof._ Let<tbc>

\(Z^{(s)}\in(\mathbb{C}^n)^{\otimes 2N}\)

