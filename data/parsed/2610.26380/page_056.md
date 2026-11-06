<tbc>_Proof._ Because the vectors **_e_**_<sub>a</sub>_-**_e_**_<sub>b</sub>_, \(a\neq b\), span \(\mathbf{1}^\perp\), the assumption \(\mathbf{1}^\perp\nsubseteq M\) implies that there exist \(a\neq b\) such that \(Q(\mathbf{e}_a-\mathbf{e}_b)\neq\mathbf{0}\). Set \(\delta:=\frac{1}{2}\left\|Q(\mathbf{e}_a-\mathbf{e}_b)\right\|_2>0\). Since _Q_(**_e_**_<sub>a</sub>_-**_e_**_<sub>b</sub>_)=_Q_(**_g_**_<sub>t,a</sub>_-**_g_**_<sub>t,b</sub>_), for every _t_, there exists \(i_t\in\{a,b\}\) such that \(\left\|Q\mathbf{g}_{t,i_t}\right\|_2\ge\delta\). Using \(\left\|\mathbf{g}_{t,i_t}\right\|_2\le 2\), condition (i), and condition (ii),

\(\sigma_{t-1,i_t}^2=\mathbf{g}_{t,i_t}^\top\Sigma_{t-1}\mathbf{g}_{t,i_t}\)<br>
\(\ge(Q\mathbf{g}_{t,i_t})^\top\Sigma_{t-1}(Q\mathbf{g}_{t,i_t})-2\left|(R_M\mathbf{g}_{t,i_t})^\top\Sigma_{t-1}(Q\mathbf{g}_{t,i_t})\right|\)<br>
\(\ge c\left\|Q\mathbf{g}_{t,i_t}\right\|_2^2-2\|R_M\Sigma_{t-1}Q\|_\mathrm{op}\|R_M\mathbf{g}_{t,i_t}\|_2\|Q\mathbf{g}_{t,i_t}\|_2\)<br>
\(\ge c\delta^2-8\|R_M\Sigma_{t-1}Q\|_\mathrm{op}.\)

Therefore,

\(\mathrm{liminf}_{t\rightarrow\infty}\sigma_{t-1,i_t}^2\ge c\delta^2>0.\)

By Lemma D.5, there exists _w_<sub>∗</sub>_\>_0 such that eventually \(w_{t-1,i_t}\ge w_*\). The same bounds also imply that _z_<sub>_t_-1_,i<sub>t</sub>_</sub> is bounded eventually.

Since D is finite and its span contains \(\mathbf{1}^\perp\), there exists \(\kappa>0\) such that, for every \(\mathbf{y}\in\mathbb{R}^I\),

\(\sum_{L\in\mathcal{D}}(L^\top\mathbf{y})^2\ge\kappa\|\mathbf{y}\|_2^2.\)

Applying this with \(\mathbf{y}=\Sigma_{t-1}\mathbf{g}_{t,i_t}\), and using \(\mathbf{g}_{t,i_t}\in\mathbf{1}^\perp\) and \(\|\mathbf{g}_{t,i_t}\|_2\le 2\), gives

\(\sum_{L\in\mathcal{D}}\left(\mathbf{g}_{t,i_t}^\top\Sigma_{t-1}L\right)^2\ge\kappa\left\|P\Sigma_{t-1}\mathbf{g}_{t,i_t}\right\|_2^2\ge\frac{\kappa}{4}\left(\mathbf{g}_{t,i_t}^\top P\Sigma_{t-1}\mathbf{g}_{t,i_t}\right)^2=\frac{\kappa}{4}\sigma_{t-1,i_t}^4.\)

For \(0\le s\le 1/2\),

\(\frac{1}{\sqrt{1-s}}\phi\left(\frac{z}{\sqrt{1-s}}\right)\ge\phi(z)\mathrm{exp}\left(-\frac{z^2s}{2(1-s)}\right)\ge\phi(z)e^{-z^2/2}.\)

Since the upper limit in (D.1) is less than 1, retaining only the _i<sub>t</sub>_ summand and integrating over the first half of its interval gives

\(G_t(L)\ge\frac{\delta_t(L)e^{-z_{t-1,i_t}^2/2}}{4r_LL^\top\Sigma_{t-1}L}w_{t-1,i_t}\left(\mathbf{g}_{t,i_t}^\top\Sigma_{t-1}L\right)^2.\)

The definition of \(\delta_t(L)\) gives

\(\frac{\delta_t(L)}{L^\top\Sigma_{t-1}L}=\frac{\beta_L^2}{1+\beta_L^2L^\top\Sigma_{t-1}L}\frac{\phi(\alpha_t(L))^2}{\Phi(\alpha_t(L))\Phi(-\alpha_t(L))}.\)

By condition (iii), the boundedness of _z_<sub>_t_-1_,i<sub>t</sub>_</sub>, and continuity and strict positivity of the expression above, there exists \(\tau_*>0\) such that eventually

\(\frac{\delta_t(L)e^{-z_{t-1,i_t}^2/2}}{4r_LL^\top\Sigma_{t-1}L}\ge\tau_*(L\in\mathcal{D}).\)

Consequently,

\(\sum_{L\in\mathcal{D}}G_t(L)\ge\tau_*w_{t-1,i_t}\sum_{L\in\mathcal{D}}\left(\mathbf{g}_{t,i_t}^\top\Sigma_{t-1}L\right)^2\ge\frac{\tau_*w_*K}{4}\sigma_{t-1,i_t}^4.\)

Thus

\(\mathrm{liminf}_{t\rightarrow\infty}\sum_{L\in\mathcal{D}}G_t(L)\ge\frac{\tau_*w_*K}{4}c^2\delta^4>0.\) \(\square\)

