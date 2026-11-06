**Lemma 2.** _For_ \(X=\{X^{(S,\bar{S})}|\bar{S}\subseteq S\subseteq F\}\)_, with_ \(X^{(S,\bar{S})}\in(\mathbb{C}^n)^{\otimes(d-|S|)}\) _and Y, Z defined similarly,_

\(\phi_\mathrm{BCW}^{\otimes d}(X,Y,Z)=\sum_{G\sqcup H=F}\sum_{U\sqcup V\sqcup W=G}\sum_{\bar{U}\sqcup\bar{V}\sqcup\bar{W}=H}\sum_{\mathbf{i}\in\unknown 0,n-1\unknown^G}X_{\mathbf{i}|_{G\backslash U}}^{(U\sqcup H,\bar{U})}Y_{\mathbf{i}|_{G\backslash V}}^{(V\cup H,\bar{V})}Z_{\mathbf{i}|_{G\backslash W}}^{(W\cup H,\bar{W})},\) (34)

_where_ \(\sqcup\) _is disjoint union and we use the shorthand notation,_

\(\sum_{A\sqcup B\sqcup C=D}=\sum_{(A,B,C):A\sqcup B\sqcup C=D}.\) (35)

_Proof._ Each tensor contraction term in \(\phi_\mathrm{BCW}^{\otimes d}\) is a tensor product of \(|G|\le d\) terms from \(\phi_\mathrm{CW}\) (indexed by _G_) and |_H_| scalar-valued terms introduced in \(\phi_\mathrm{BCW}\) (indexed by _H_), such as _X_<sup>({0},{1})</sup>_Y_<sup>({0},{1})</sup>_Z_<sup>({0},{0})</sup>. The latter |_H_| scalar-valued terms correspond to a tripartition of the indices omitted from all three tensor variables in the term, with the block of variables indexed accordingly. Only coordinates in _G_ are summed, since those in _H_ are omitted from all three blocks.

A selection of these contractions is conflict-free if no two share a variable block in any of the three spaces and zeroing all unselected blocks leaves exactly the selected contractions. Indexing the selected contractions by _t_, the restriction gives independent matrix products \(\langle n^{|V_t|},n^{|W_t|},n^{|U_t|}\rangle\) and has border rank at most (_n_+2)_<sup>d</sup>_.

## 5.2 Aggregation of Tensor Contractions

We approach the simultaneous matrix products selected from powers of the little CW tensor in a bottom-up manner, by considering trilinear aggregation of tensor contractions.

We define a trilinear aggregation of tensor contractions by a subset of balanced tripartitions \(\mathcal{S}\subseteq B_{N,N,N}\). We are then interested in a factorization of the trilinear form corresponding to |S| simultaneous matrix- matrix products of matrices of dimension _n<sup>N</sup>_, all viewed as different contractions of order 2_N_ tensors. With _d_=3_N_,

\(\phi_\mathcal{S}(X,Y,Z)=\sum_{(U,V,W)\in\mathcal{S}}\sum_{\mathbf{i}\in\unknown 0,n-1\unknown^d}X_{\mathbf{i}|_{U^c}}^{(U)}Y_{\mathbf{i}|_{V^c}}^{(V)}Z_{\mathbf{i}|_{W^c}}^{(W)}.\) (36)

For \(j\in\{1,2,3\}\), let \(\pi_j(\mathcal{S})\) denote the projection of S onto its _j_th coordinate. We seek to obtain \(\phi_\mathcal{S}\) from the aggregated trilinear form,

\(\sum_{\mathbf{i}\in\unknown 0,n-1\unknown^d}\big(\sum_{U\in\pi_1(\mathcal{S})}X_{\mathbf{i}|_{U^c}}^{(U)}\big(\sum_{V\in\pi_2(\mathcal{S})}Y_{\mathbf{i}|_{V^c}}^{(V)}\big)\big(\sum_{W\in\pi_3(\mathcal{S})}Z_{\mathbf{i}|_{W^c}}^{(W)}\big).\) (37)

Index the tripartitions in S by _t_, writing (_U<sub>t</sub>,V<sub>t</sub>,W<sub>t</sub>_).

A mixed choice (_U<sub>i</sub>,V<sub>j</sub>,W<sub>k</sub>_) selects one factor from each of the three sums in (37). For each coordinate \(r\in F\), its local multiplicity \(\eta_r(i,j,k)\in\{0,1,2,3\}\) is the number of sets among _U<sub>i</sub>,V<sub>j</sub>,W<sub>k</sub>_ that contain _r_. Since _U<sub>i</sub>,V<sub>j</sub>,W<sub>k</sub>_ specify omitted coordinates, the index in coordinate _r_ occurs in exactly \(3-\eta_r\) of the selected tensors. When it occurs in two tensors, summation over that index contracts the corresponding pair of fibers, as in the trilinear form for matrix multiplication. When it occurs in all three tensors, the summation is over their entrywise (Hadamard) product. An index occurring in only one tensor can be summed within that tensor, while an index absent from all three simply replicates the same value. We use the following names for these four cases:

For a balanced mixed choice, \(\sum_{r\in F}\eta_r(i,j,k)=|U_i|+|V_j|+|W_k|=d\). Thus, in the absence of linearly reducible and replicated coordinates, every \(\eta_r\) is one and the selected sets form a tripartition.

\begin{tabular}{ccc}
\(\eta_r\) & number of tensors containing the index & index type \\
0 & 3 & Hadamard index \\
1 & 2 & pairwise contraction index \\
2 & 1 & linearly reducible index \\
3 & 0 & replicated index \\
\end{tabular}

