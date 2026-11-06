The normalization by |_E_| allows comparisons between graphs of different sizes, as in  2. It is different from a spectral edge weight \(p_{i,j}^{(\phi)}\): the latter records the value of a fixed spectral point on the single-edge tensor \(E_{i,j}^{(q)}\) and is introduced in Definition 4.3. The triangle-cover upper bound used in that comparison is proved in Theorem A.5.

**Definition 2.23** (graph cuts)**.** Let _G_=(_V,E_) be a finite simple undirected graph with \(|V|\ge 2\). For a nonempty proper subset \(S\subset V\) , define<tbc>

\(\delta_G(S)=\{(u,v)\in E:|\{u,v\}\cap S|=1\}.\)

<tbc>The _maximum-cut size_ and _minimum-cut size_ are<tbc>

\(\mathrm{MaxCut}(G)=\mathrm{max}_{\varnothing\neq S\subseteq V}|\delta_G(S)|,\mathrm{MinCut}(G)=\mathrm{min}_{\varnothing\neq S\subseteq V}|\delta_G(S)|.\)

<tbc>Grouping the tensor legs in _S_ and _V_\\_S_ gives a matrix of rank \(q^{|\delta_G(S)|}\); see Definition A.1 and Lemma A.3. Proposition A.4 and Theorem B.4 give, respectively,

\(\mathrm{log}\widetilde{\mathrm{R}}(\mathsf{GT}_2(G))\ge\mathrm{MaxCut}(G),\mathrm{log}\widetilde{\mathrm{Q}}(\mathsf{GT}_2(G))=\mathrm{MinCut}(G).\)

The second equality is due to Vrana and Christandl \[VC17\]; Appendix B supplies a complete proof for graphs in tensor notation. For disconnected graphs, MinCut(_G_)=0 and \(\widetilde{\mathrm{Q}}(\mathsf{GT}_2(G))=1\). For every integer \(k\ge 2\), a cut of _K<sub>k</sub>_ with _s_ vertices on one side has _s(k-s_) crossing edges. Its maximum and minimum over \(1\le s\le k-1\) are \(\lfloor k^2/4\rfloor\) and _k_-1, respectively. Thus MaxCut(_K<sub>k</sub>_)=\(\lfloor k^2/4\rfloor\) and MinCut(_K<sub>k</sub>_)=_k_-1.

## 3 Separating Several Shared Tensor Legs

In this section, we consider tensors whose blocks have disjoint coordinates on two legs and may share all their remaining legs. These matched blocks form a partial direct sum in the sense of Definition 2.9. We show that a linear number of full direct-sum copies suffices to separate all the shared legs at once, with each output block retaining an edge tensor. We then apply this construction to blocks of a fixed type to obtain the entropy inequality used in the polynomial argument. The construction extends the single-shared-leg separation of OpenAI \[Ope26a, Proposition 3.1 and Corollary 3.2\].

### 3.1 A finite separation construction

The construction proceeds in two steps. A Fourier projection first imposes one linear relation on tentative block labels. Local weights then make the total degree equal to a sum of squared label differences, so its zero-degree part has the required block label on every shared leg. We give the coordinate offsets explicitly to include blocks of different sizes and zero blocks.

**Theorem 3.1** (simultaneous separation)**.** _Let_ \(k\ge 2\) _and_ \(M\ge 1\) _be integers, and put_ \(\ell=k-2\)_. Choose positive integers_ \(d_1,\dots,d_\ell\) _and, for every integer_ \(0\le h<M\)_, positive integers b<sub>h</sub>,c<sub>h</sub>. Let A<sub>h</sub> be a complex k-th order tensor specified in coordinates of dimensions_ \((d_1,\dots,d_\ell,b_h,c_h)\)_. Put_<tbc>

\(\beta_h=\sum_{t=0}^{h-1}b_t,\gamma_h=\sum_{t=0}^{h-1}c_t(0\le h\le M),\)

<tbc>_where the sums for h_=0 _are empty. Define a complex k-th order tensor A in coordinates of dimensions_ \((d_1,\dots,d_\ell,\beta_M,\gamma_M)\) _by_<tbc>

\(A_{a_1,\dots,a_\ell,\beta_h+b,\gamma_h+c}=(A_h)_{a_1,\dots,a_\ell,b,c}\)

