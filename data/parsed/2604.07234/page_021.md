<tbc>We note that the application of Hoeffding’s inequality in (3.15) is conservative and involves a denominator of 4 in the exponential (rather than 2) due to subtleties arising from ties giving \(\Delta(Y^{(i)})=0\), and thus

(3.16) \(\mathbb{P}\left(\mathrm{maj}(X'^{(i)})=\mathrm{maj}(Y^{(i)}),\Delta(Y^{(i)})>0\right)\neq 1/2.\)

It is readily confirmed that as \(b\rightarrow\infty\), the LHS of (3.16) tends to 1/2 and the proportion of bad blocks is vanishing, so our Hoeffding invocation is justified. A union bound and these observations now yield that

\(\mathbb{P}\left(T_\mathrm{std}\left(X',Y\right)\ge\frac{1+\beta^\star(\alpha)}{2}\right)\le\sum_{(Y^{(1)},\dots,Y^{(B)})\in\mathcal{N}\mathcal{E}_\mathrm{std}(Y)}\mathbb{P}\left(\frac{1}{B}\sum_{i=1}^BA_\mathrm{loc}\left(X'^{(i)},Y^{(i)}\right)\ge\frac{1+\beta^\star(\alpha)}{2}\right)\le^{(3.15)}\left|\mathcal{N}\mathcal{E}_\mathrm{std}(Y)\right|\cdot\mathrm{exp}\left(-B\cdot\frac{\beta^\star(\alpha)^2}{4}\right)\le^{(3.14)}e^{B\cdot o_b(1)}\mathrm{exp}\left(-B\cdot\frac{\beta^\star(\alpha)^2}{4}\right)\text{(3.17)}\le^{(b\mathrm{large})}\mathrm{exp}\left(-B\cdot\frac{\beta^\star(\alpha)^2}{8}\right)=e^{-\Omega(N)}.\)

This establishes the desired guarantee. □

As the statement of Proposition 3.8 and the definition of the good set G(_X_) were phrased with respect to induced total alignment, our next task is to relate standardized total alignment to induced total alignment. Towards this end, we introduce the following standardization algorithm, which will serve as our key link between the two different kinds of near-equipartitions of Definition 3.3.

**Definition 3.10** (Standardization algorithm)**.** For a string \(y\in\{0,1\}^M\), say we are given an induced near-equipartition \(\left(y^{(1)},\dots,y^{(B)}\right)\in\mathcal{N}\mathcal{E}_\mathrm{ind}(y)\), and denote the collection of indices corresponding to _exceptional_ blocks of this induced near-equipartition via<tbc>

\(\mathcal{I}_{\left(y^{(1)},\dots,y^{(B)}\right)}^\mathrm{exc}:=\left\{i\in[B]:|y^{(i)}|\notin\left[(1-\delta)\alpha b,(1+\delta)\alpha b\right]\right\}.\)

<tbc>The _standardization algorithm_ defines a corresponding map

(3.18) \(\varphi_y:\mathcal{N}\mathcal{E}_\mathrm{ind}(y)\rightarrow\mathcal{N}\mathcal{E}_\mathrm{std}(y).\)

The algorithm proceeds sequentially through the strings _y_<sup>(_i_)</sup>, constructing \(\left(\tilde{y}^{(1)},\dots,\tilde{y}^{(B)}\right)\in\mathcal{N}\mathcal{E}_\mathrm{std}(y)\) sequentially. Say that the algorithm has processed \(\left(y^{(1)},\dots,y^{(i)}\right)\) and has constructed \(\left(\tilde{y}^{(1)},\dots,\tilde{y}^{(i)}\right)\) so that

(3.19) \(y^{(1)}\cdots y^{(i)}=\tilde{y}^{(1)}\cdots\tilde{y}^{(i)}.\)

The next strings \(\tilde{y}^{(k)}\) for \(k\ge i+1\) are constructed via the following procedure. We continue reading strings _y_<sup>(_i_+1)</sup>_,y_<sup>(_i_+2)</sup>_,..._ and stop when we either

(a) first hit a string _y_<sup>(_k_)</sup> for which \(k\in\mathcal{I}_{\left(y^{(1)},\dots,y^{(B)}\right)}^\mathrm{exc}\),<tbc>

(b) progress through \(b^\epsilon\) strings without hitting such a string _y_<sup>(_k_)</sup> for which \(k\in\mathcal{I}_{\left(y^{(1)},\dots,y^{(B)}\right)}^\mathrm{exc}\), or<tbc>

(c) reach the final string _y_<sup>(_B_)</sup> of the induced near-equipartition \(\left(y^{(1)},\dots,y^{(B)}\right)\).

Take the corresponding sequence of strings \(\left(y^{(i+1)},\dots,y^{(j)}\right)\) that we have just progressed through. We construct \(\left(\tilde{y}^{(i+1)},\dots,\tilde{y}^{(j)}\right)\) as follows.

\(\bullet\) If \(j\in\mathcal{I}_{\left(y^{(1)},\dots,y^{(B)}\right)}^\mathrm{exc}\), then let \(\tilde{y}^{(j)}=y^{(j)}\). If _j\>i_+1, then for the remaining indices _i_+1_,...,j_-1, let \(|\tilde{y}^{(k)}|=\alpha b\) for all \(k\in\{i+1,\dots,j-2\}\) and set \(\tilde{y}^{(j-1)}\) accordingly so that<tbc>

(3.20) \(y^{(1)}\cdots y^{(j)}=\tilde{y}^{(1)}\cdots\tilde{y}^{(j)}\)

