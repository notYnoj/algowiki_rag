Further, note that the function check(_G,X_) computes the coefficients of the _Spanning Tree Polynomial_. Specially, the coefficient _c_<sub>_w_<sub>1</sub>_,...w_<sub>_n_-1</sub></sub> of _P<sub>ST</sub>(G_) is equal to check(_G,X_) where _X_ is the set that contains a triple (_n,c,d_) if and only if the color (_c,d_) appears exactly _n_ times in the multiset {_w_<sub>1</sub>_,...w_<sub>_n_-1</sub>} (note that each _w<sub>i</sub>_ is actually a (_c,d_)-tuple). Thus, if \(P_{ST}(G)\equiv P_{ST}(H)\) then check(_G,X_)=check(_H,X_) for all \(X\in W\), proving the theorem.

To show \(P_{ST}(G)\equiv P_{ST}(H)\), we use a result from \[CY00\] which states that for each \(i\in[n]\)

\(\mathrm{Kir}(G)\equiv\mathrm{det}(\tilde{L}_i(G)),\)

where \(\tilde{L}_i(G)\) is the Laplacian _L(G_) of _G_ with its _i_-th row and _i_-th column removed. Note that \(\mathrm{det}(\tilde{L}_i(G))\) is a polynomial over the variables _X<sub>e</sub>_. Now, \(\mathrm{Kir}(G)|_{X_e=c(e)}\equiv P_{ST}(G)\) and \(\mathrm{Kir}(G)\equiv\mathrm{det}(\tilde{L}_i(G))\) implies that \(P_{ST}(G)\equiv\mathrm{det}(\tilde{L}_i^C(G))\) where \(\tilde{L}_i^C(G)\) is obtained by substituted each variable _X<sub>e</sub>_ in \(\tilde{L}_i(G)\) with _c(e_).

Thus, it is enough to prove \(P_{ST}(G)\equiv\mathrm{det}(\tilde{L}_i^C(G))\equiv\mathrm{det}(\tilde{L}_i^C(H))\equiv P_{ST}(H)\) whenever \(H\equiv_{2\text{-WL}}G\). By \[RS23\]<sup>28</sup>, _L<sup>C</sup>(G_) is cospectral to _L<sup>C</sup>(H_). Let \(d_i^G\) (respectively \(d_i^H\)) be the _i_th coefficient of the characteristic polynomial of _L<sup>C</sup>(G_) (respectively _L<sup>C</sup>(H_)). Note that \(d_i^H,d_i^G\in\mathbb{C}[c(e)]\).<sup>29</sup> Since _L<sup>C</sup>(G_) and _L<sup>C</sup>(H_) are cospectral, it follows that \(d_i^H=d_i^G\). Note that \(d_1^H\) is the linear coefficient of the characteristic polynomial.<sup>30</sup> A well-known theorem from linear algebra (see e.g. \[Alf18, Theorem 1.8\]) implies<tbc>

\(d_1^H\equiv-\sum_{i=1}^n\mathrm{det}(\tilde{L}_i^C(H)),d_1^G\equiv-\sum_{i=1}^n\mathrm{det}(\tilde{L}_i^C(G)).\)

<tbc>Now, since \(\mathrm{det}(\tilde{L}_i^C(H))\equiv\mathrm{det}(\tilde{L}_j^C(H))\) and \(\mathrm{det}(\tilde{L}_i^C(G))\equiv=\mathrm{det}(\tilde{L}_j^C(G))\) for all \(i,j\in[n]\), we obtain

\(P_{ST}(G)\equiv\mathrm{det}(\tilde{L}_i^C(G))\equiv\frac{-d_1^G}{n}\equiv\frac{-d_1^H}{n}\equiv\mathrm{det}(\tilde{L}_i^C(H))\equiv P_{ST}(H).\)

_Proof of Theorem 8.14._ Let \(B\in\mathbb{R}_{>0}\). According to Lemma 8.15, the triple \((W,\mathrm{check}:\mathcal{G}\times W\rightarrow\mathbb{R},\mathrm{cost}:W\rightarrow\mathbb{R})\) is a witness function of _OPT_. Further, Lemma 8.16 shows that check is 2-WL invariant on G. Thus, Lemma 8.7 implies that CSP is 2-WL invariant.

**Corollary 8.17.** _There is an algorithm that solves the_ CST _problem with k prior instances each of size at most n in O(kn_<sup>3</sup>log_n_) _preprocessing time and O(n_<sup>3</sup>log_n_) _query time._

_Proof._ This is a direct consequence of Theorem 8.3 combined with Theorem 8.14.

## 8.5 Examples when Weisfeiler-Leman Fails

Given a graph _G_ of order _n_ and maximum degree \(k\ge 3\). In \[CFI92\] Cai, Fürer, and Immerman introduced the idea of CFI graphs. A CFI graph is obtained by taking _G_, a parity \(p\in\{\mathrm{odd},\mathrm{even}\}\) and computing a labeled graph CFI(_G,p_). This construction can be performed in time \(O(2^k\cdot n)\).<sup>31</sup> Further, CFI(_G,p_) has a maximum degree at most 2<sup>_k_-2</sup>+1.

<sup>28</sup>See Theorem 26 combined with Example 22 that shows that Laplacian mapping \(G\rightarrow L(G)\) is in E. <sup>29</sup>That is, the ring of polynomials with variables _c(e_). <sup>30</sup>That is, the coefficient corresponding to _x_<sup>1</sup> in the characteristic polynomial of _L<sup>C</sup>(H_). <sup>31</sup>See \[CFI92, Section 6\] for a detailed construction. Note that in this paper _X(G_)=CFI(_G,_even) and \(\tilde{X}(G)=\mathrm{CFI}(G,\mathrm{odd})\).

