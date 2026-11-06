The constructions of  7 use the big-CW restriction of Section 5.1. Their border-rank bounds follow from the restriction identity and the counts by covered size. Complete data are in `inc6p51` and `inc9p68`, respectively, in the directory indexed by Appendix F. These and the unequal-shape constructions of  6 are tabulated comparisons, not curves in the figures.

### E.2 Norms of the incomplete big-CW restrictions

For the rational degeneration defining \(\phi_\mathrm{BCW}\) in Section 4, distribute the absolute scalar coefficient of each rank-one term equally among its three factors. Put its sign in the output factor. For \(0<\lambda<1/n\), set \(t=1-n\lambda\). Up to column signs, each factor has columns

\(\lambda^{-2/3}(e_0+\lambda e_i)(1\le i\le n),\lambda^{-1}\left(e_0+\lambda^2\sum_{i=1}^ne_i\right),t^{1/3}\lambda^{-1}e_0+\lambda^2t^{-2/3}e_{n+1}.\) (183)

Summing their outer products and restricting to the span of _e_<sub>0</sub>, \(n^{-1/2}\sum_{i=1}^ne_i\), and _e_<sub>_n_+1</sub> gives

\(H(\lambda)=\left(\begin{array}{ c c c }
n\lambda^{-4/3}+\lambda^{-2}(1+t^{2/3}) & \sqrt{n}(\lambda^{-1/3}+1) & \lambda t^{-1/3} \\
\sqrt{n}(\lambda^{-1/3}+1) & \lambda^{2/3}+n\lambda^2 & 0 \\
\lambda t^{-1/3} & 0 & \lambda^4t^{-4/3}
\end{array}\right).\) (184)

The remaining _n_-1 directions in the middle block have eigenvalue \(\lambda^{2/3}\). A retained variable block has a word \(\alpha\in\{0,1,2\}^d\), determined by its scalar, active, and barred coordinates of the variable blocks in Lemma 2. For each variable space, form the matrix indexed by its retained words,

\(G_{\alpha\beta}(\lambda)=\prod_{j=0}^{d-1}H_{\alpha_j\beta_j}(\lambda).\) (185)

The factor’s squared spectral norm is \(\lambda_\mathrm{max}(G)\). Indeed, decomposing each middle coordinate into its sum and orthogonal complement splits the Gram matrix into invariant subspaces. Each other invariant block is entrywise bounded by a principal submatrix of _G_: an orthogonal middle-coordinate direction replaces _H_<sub>11</sub> by \(\lambda^{2/3}\le H_{11}\). All entries are nonnegative, so monotonicity of the spectral radius and the principal-submatrix bound give no larger eigenvalue. The product of the three square roots gives \(\sigma(\Xi(\lambda))\) without forming the tensor-power factors.

For the two incomplete families of  7, this yields

These values use the displayed rational big-CW realization and its original parameter, with the scalar weights balanced as above.

## F Construction data

The indices below locate the supplied data for the numerical results. Each construction has a readable file `\<identifier\>.txt` in `anc/constructions/`, listing its tripartitions and exponents or the corresponding incomplete tripartitions. The correction rule is given in the file, with explicit correction sets when required.  8 locates all centered constructions used in the figures or discussed in Section 8.2.  9 separately locates the weighted constructions used in Figure 3; their supports and gradings need not agree with centered constructions having the same _N,p_. The machine-readable index is `anc/auxiliary/construction\_usage. csv`.

\begin{tabular}{ccc}
_d_ & _p_ & \(\sigma(\Xi(\lambda))\) to leading order \\
6 & 51 & \(64\sqrt{2}\lambda^{-34/3}\) \\
9 & 68 & \(512\lambda^{-15}\) \\
\end{tabular}

