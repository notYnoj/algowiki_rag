\(\frac{v^\top L_Hv}{v^\top L_Gv}=\frac{u^\top L_G^{+/2}L_HL_G^{+/2}u}{u^\top u}\le\lambda_1(L_G^{+/2}L_HL_G^{+/2})\le 1+\varepsilon\)

and

\(\frac{v^\top L_Hv}{v^\top L_Gv}=\frac{u^\top L_G^{+/2}L_HL_G^{+/2}u}{u^\top u}\ge\lambda_n(L_G^{+/2}L_HL_G^{+/2})\ge 1-\varepsilon\)

where both final inequalities follows the Courant-Fischer formula.

By the union bound, both conditioning events (bounds on the number of edges and on the eigenvalues) occur with non-zero probability. This means there exists _H_ with \(m\cdot\left(\frac{1}{2}\pm\lambda\right)\) edges that is a \(\sqrt{\frac{Cnlogn}{\lambda m}}\)-spectral sparsifier of _G_. Finally, each edge of _H_ has its weight at most doubled up from _G_. Thus, the maximum weight of _H_ is at most 2_W_.

**Fact B.8.** \(\sum_{e\in E}Y_e=L_G^{+/2}L_HL_G^{+/2}\) _and_ \(\mathbb{E}\left(\sum_{e\in E}Y_e\right)=\Pi\).

_Proof._ Consider the following derivation:

\(\sum_{e\in E}Y_e=\sum_{e\in E_\mathrm{low}}Y_e+\sum_{e\in E_\mathrm{high}}Y_e\)<br>
\(=\sum_{e\in E_\mathrm{low}}L_G^{+/2}\left(2w_ez_e\cdot\chi_e\chi_e^\top\right)L_G^{+/2}+\sum_{e\in E_\mathrm{high}}L_G^{+/2}\left(w_e\chi_e\chi_e^\top\right)L_G^{+/2}\)<br>
\(=L_G^{+/2}\left(\sum_{e\in E_\mathrm{low}}2w_ez_e\cdot\chi_e\chi_e^\top+\sum_{e\in E_\mathrm{high}}w_e\chi_e\chi_e^\top\right)L_G^{+/2}\)<br>
\(=L_G^{+/2}L_HL_G^{+/2}.\)

This proves the first equality.

For the second equality, notice that E(_L<sub>H</sub>_)=_L<sub>G</sub>_ since each \(e\in E_\mathrm{low}\) has equal probabilities of its weight being doubled or zeroed. As a result, we have:

\(\mathbb{E}\left(\sum_{e\in E}Y_e\right)=\mathbb{E}\left(L_G^{+/2}L_HL_G^{+/2}\right)=L_G^{+/2}\mathbb{E}\left(L_H\right)L_G^{+/2}=L_G^{+/2}L_GL_G^{+/2}=\Pi\)

as wished.

**Fact B.9.** _For every_ \(e\in E_\mathrm{low}\)_, we have_ \(\lambda_1(Y_e)\le\frac{2n}{\lambda m}\).

_Proof._ Following Corollary B.5, we have

\(\lambda_1(Y_e)=\|y_e\|^2=2w_ez_e\cdot\|L_G^{+/2}\chi_e\|_2^2\le 2w_e\cdot\chi_e^\top L_G^+\chi_e=2w_eR_e\le\frac{2n}{\lambda m}\)

where the first inequality is due to the fact that \(z_e\in\{0,1\}\) and the second inequality is due to the definition of _E_<sub>low</sub>.

Now we are ready to prove an analogue of Theorem 2.6 for spectral sparsifier which is inherently a stronger result.

**Theorem B.10.** _Let G be an unweighted undirected connected graph with n vertices and average degree d. Then, for any_ \(\varepsilon\in(0,1)\)_, there is an_ \(\varepsilon\)_-spectral sparsifier of G with_ \(O\left(\frac{n\mathrm{log}^2n}{\varepsilon^2}\right)\) _edges and edge weights bounded by_ \(O\left(\frac{\varepsilon^2d}{\mathrm{log}^2n}\right)\).

