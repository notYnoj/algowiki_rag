<tbc>eventually. Therefore,

\(w_{t-1,i_t}=\frac{\phi(z_{t-1,i_t})}{\sigma_{t-1,i_t}}\ge\frac{\phi((B+Q_0)/\underline{\sigma})}{\bar{\sigma}}=:w_*>0\)

eventually. \(\square\)

We can now show that the score of any direction whose variance vanishes must itself vanish.

LEMMA D.6. _Let_ \(L\in\mathcal{D}\) _be a direction such that_<tbc>

\(L^\top\Sigma_{t-1}L\rightarrow 0.\)

<tbc>_Then_<tbc>

\(G_t(L)\rightarrow 0.\)

<tbc>_Proof._ For each _i_ with \(\sigma_{t-1,i}>0\), Cauchy-Schwarz gives,<tbc>

\(\left(\mathbf{g}_{t,i}^\top\Sigma_{t-1}L\right)^2\le\left(\mathbf{g}_{t,i}^\top\Sigma_{t-1}\mathbf{g}_{t,i}\right)\left(L^\top\Sigma_{t-1}L\right)=\sigma_{t-1,i}^2L^\top\Sigma_{t-1}L.\)

<tbc>Therefore,<tbc>

\(w_{t-1,i}\left(\mathbf{g}_{t,i}^\top\Sigma_{t-1}L\right)^2\le\phi(0)\sigma_{t-1,i}L^\top\Sigma_{t-1}L\le\phi(0)\bar{\sigma}L^\top\Sigma_{t-1}L\)

<tbc>eventually, by Lemma D.3. Summing over _i_ yields<tbc>

\(\sum_{i:\sigma_{t-1,i}>0}w_{t-1,i}\left(\mathbf{g}_{t,i}^\top\Sigma_{t-1}L\right)^2\le I\phi(0)\bar{\sigma}L^\top\Sigma_{t-1}L.\)

<tbc>Also, Cauchy-Schwarz gives \(\phi(z)^2\le\Phi(z)\Phi(-z)\), so \(0\le\delta_t(L)<1\) and \(\delta_t(L)/(L^\top\Sigma_{t-1}L)\le\beta_L^2\). Since \(\phi(z/\sqrt{1-s})\le\phi(z)\) for \(0\le s<1\) and \(1-\sqrt{1-s}\le s\), integrating in (D.1) and substituting the bounds above gives

\(0\le G_t(L)\le\frac{\delta_t(L)}{r_LL^\top\Sigma_{t-1}L}\sum_{i:\sigma_{t-1,i}>0}w_{t-1,i}\left(\mathbf{g}_{t,i}^\top\Sigma_{t-1}L\right)^2\le\frac{I\phi(0)\bar{\sigma}\beta_L^2}{r_L}L^\top\Sigma_{t-1}L\rightarrow 0.\square\)

We next show the complementary result, that if the recurrent span does not contain \(\mathbf{1}^\perp\), some score must remain bounded away from zero.

LEMMA D.7. _Fix a deterministic set_ \(\mathcal{E}\subseteq\mathcal{D}\)_, let M_:=span(E)_, and let R<sub>M</sub> and Q be the orthogonal projectors onto M and_ \(M^\perp\)_. Suppose_ \(\mathbf{1}^\perp\unknown\in M\)_. On any event_ \(\Omega\) _on which_

(_i)_ \(Q\Sigma_{t-1}Q\unknown cQ\) _eventually for some c\>_0,<tbc>

(_ii)_ \(\|R_M\Sigma_{t-1}Q\|_\mathrm{op}\rightarrow 0\)_, and_<tbc>

_(iii)_ \(\mathrm{sup}_t\|\mu_{t-1}\|_\infty<\infty\) _and_ \(\Sigma_{t-1}\unknown\overline{\Sigma}\) _eventually for some fixed positive semidefinite matrix_ \(\overline{\Sigma}\)_, we have_<tbc>

\(\mathrm{liminf}_{t\rightarrow\infty}\sum_{L\in\mathcal{D}}G_t(L)>0\text{\textit{a.s. on}}\Omega.\)

