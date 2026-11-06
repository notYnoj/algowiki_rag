**Claim 6.7.** _For_ est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] _where_ (_l,r_\] _is a scale-s interval such that_ \(s\in\widetilde{S}\)_. Let <o>p</o><sub>l,r</sub> be the shortest_ \(\widetilde{S}\)_-regular_ \(\langle l,y_l\rangle\)_-_\(\langle r,y_r\rangle\) _path. We have the following:_

**We only give up when weight distribution is imbalanced** _if_ \(max_{1\le i\le M}\mathrm{appr}[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]=\omega\left(\frac{\mathrm{appr}[l,y_l,r,y_r]}{M}\right)\)_, then_ \(\mathrm{TD}_M(W(\overline{p_{l,r}}))=\omega\left(\frac{w(\overline{p_{l,r}})}{M}\right)\).

**If we do not give up, we obtain a good estimate** _if_ \(\mathrm{max}_{1\le i\le M}\mathrm{appr}[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]\le\frac{\mathrm{appr}[l,y_l,r,y_r]}{M}\mathrm{loglog}(n)\)_, then with probability_ \(1-\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\), \(\left(2\sum_{i=1}^M\eta_{l,r,i}\mathrm{est}[m_{i-1},\overline{y_i},m_i,\overline{y_i}]\right)\) _approximates_ \(\left(\sum_{i=1}^M\mathrm{est}[m_{i-1},\overline{y_i},m_i,\overline{y_i}]\right)\) _with additive error o_ \(\left(\frac{w(\overline{p_{l,r}})}{\mathrm{log}^{0.02}(n)}\right)\).

To sum up, we compute the estimate in the following way:

\(\mathrm{est}[l,y_l,r,y_r]:=\left\{\begin{array}{ c c }
\mathrm{ew}[l,y_l,r,y_r], & \text{if}s=0 \\
\mathrm{min}_{\widehat{Y}\in\text{✓✓✓}}\sum_{i=1}^M\mathrm{est}[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i], & \text{if}0<s\notin\widetilde{S} \\
\mathrm{min}\left(2\sum_{i=1}^M\eta_{l,r,i}\mathrm{est}[m_{i-1},\overline{y_i},m_i,\overline{y_i}], & \text{if}\left(\left(s\in\widetilde{S}\right)\wedge \\
\mathrm{appr}[l,y_l,r,y_r] & \text{if}\left(\mathrm{max}_{1\le i\le M}\mathrm{appr}[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}] \\
\mathrm{appr}[l,y_l,r,y_r], & \text{if}\left(s\in\widetilde{S}\right)\wedge \\
\mathrm{max}_{1\le i\le M}\mathrm{appr}[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}] & >\frac{\mathrm{appr}[l,y_l,r,y_r]}{M}\mathrm{loglog}(n)
\end{array}\right)
\end{array}\right),\) (22)

Finally, to obtain appr\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] which is a constant-factor approximation of the length of the shortest \(\widetilde{S}\)-regular \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path where (_l,r_\] is a scale-_s_ interval, we can use the following recursion:

\(\mathrm{appr}[l,y_l,r,y_r]:=\left\{\begin{array}{ c c }
\mathrm{aprew}[l,y_l,r,y_r], & \text{if}s=0 \\
\mathrm{min}_{\widehat{Y}\in\text{✓✓✓}}\sum_{i=1}^M\mathrm{appr}[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i], & \text{if}s\notin\widetilde{S} \\
\sum_{i=1}^M\mathrm{appr}[m_{i-1},\overline{y_i},m_i,\overline{y_i}], & \text{if}s\in\widetilde{S}
\end{array}\right.,\) (23)

To efficiently minimize over anchor path \(\widehat{Y}\) on passive scale _s_, consider the following "Scale-(_s_-1) Sparsified Grid Graph":

**Definition 6.8** (Scale-(_s_-1) Sparsified Grid Graph)**.** The Scale-(_s_-1)-Sparsified Grid Graph defined on est is as follows:

**Vertices** We only consider vertices \(\langle x,y\rangle\) in the Sparsified Edit Distance Grid Graph with the additional constraint that _I_<sub>_s_-1</sub>|_x_;

**Edges** There is an edge from \(\langle x,y\rangle\) to \(\langle x+I_{s-1},y'\rangle\) (if both exist) such that \(|y'-y|\le I_{s-1}\) with a weight of \(\mathrm{est}[x,y,x+I_{s-1},y']\) (or \(\mathrm{appr}[x,y,x+I_{s-1},y']\) for computing appr).

