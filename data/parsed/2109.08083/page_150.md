<tbc>Then

\(|V_{O/E}^{X\pm Y}(H_0^c[I_{t_1}])|=(1\pm t_0^{-\epsilon})\sum_{v\in V_{O/E}^{X\pm Y}(H_0[I_{t_1}])}1-d_{w_0^c}(v)\)<br>
\(=(1\pm 46.3C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})\sum_{v\in V_{O/E}^{X\pm Y}(H_0[I_{t_1}])}\frac{w_H(E_H(v,I_{t_1}))}{w_H(E_H(v,I_{t_0}))}\)<br>
\(=(1\pm 46.4C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})\sum_{v\in V_{O/E}^{X\pm Y}(H_0[I_{t_1}])}\frac{|E_\mathcal{T}(v,I_{t_1})|}{|E_\mathcal{T}(v,I_{t_0})|},\)

where the last equality holds using Theorem 3.28, and the fact that _w<sub>H</sub>_ is a uniform weight function. Now we may proceed as in Proposition 6.68, splitting the summa- tion across consecutive intervals, this time of size \(t_0^{1-\epsilon/2}\). Letting I be a partition of \(I_{t_1}\cap X+Y\) into intervals of size \(t_0^{1-\epsilon/2}\), then for _v<sub>I</sub>_ the vertex in the middle of \(I\in\mathcal{I}\), let \(d_I^i=|E_\mathcal{T}(v,I_{t_i})|\) for \(i\in\{0,1\}\). Then we have that \(|E_\mathcal{T}(u,I_{t_i})|=d_I^i\pm O(t_0^{1-\epsilon/2})\) for every \(u\in I\) and \(i\in\{0,1\}\). Noting that for every vertex \(u\in I_{t_1}\) and \(i\in\{0,1\}\) we have that \(|E_\mathcal{T}(u,I_{t_i})|=\Theta(t_0)\) we thus find that

\(\sum_{v\in V_O^{X+Y}(H_0[I_{t_1}])}\frac{|E_\mathcal{T}(v,I_{t_1})|}{|E_\mathcal{T}(v,I_{t_0})|}=(1\pm O(t_0^{-\epsilon/2}))\sum_{I\in\mathcal{I}}\sum_{v\in V_O^{X+Y}(H_0[I])}\frac{d_I^1}{d_I^0}\)<br>
\(=(1\pm O(t_0^{-\epsilon/2}))\sum_{I\in\mathcal{I}}\frac{d_I^1}{d_I^0}|V_O^{X+Y}(H_0[I])|,\)

where, by Claim 6.69 and Lemma 6.73(iv), we have that \(|V_O^{X+Y}(H_0[I])|=(1\pm O(t_0^{-\epsilon/2}))|V_O^{X-Y}(H_0[I])|\). From this it follows that

\(\sum_{v\in V_O^{X+Y}(H_0[I_{t_1}])}\frac{|E_\mathcal{T}(v,I_{t_1})|}{|E_\mathcal{T}(v,I_{t_0})|}=(1\pm O(t_0^{-\epsilon/2}))\sum_{I\in\mathcal{I}}\frac{d_I^1}{d_I^0}|V_O^{X-Y}(H_0[I])|\)<br>
\(=(1\pm O(t_0^{-\epsilon/2}))\sum_{I\in\mathcal{I}}\sum_{v\in V_O^{X-Y}(H_0[I])}\frac{d_I^1}{d_I^0}\)<br>
\(=(1\pm O(t_0^{-\epsilon/2}))\sum_{v\in V_O^{X-Y}(H_0[I_{t_1}])}\frac{|E_\mathcal{T}(v,I_{t_1})|}{|E_\mathcal{T}(v,I_{t_0})|}.\)

In particular, then, we have that \(|V_O^{X+Y}(H_0^c[I_{t_1}])|=(1\pm O(t_0^{-\epsilon/2}))|V_O^{X-Y}(H_0^c[I_{t_1}])|\). Hence, as \(|V_O^{X+Y}(H_0^c[I_{t_1}])|=O(t_0p_\mathrm{gr})\) the parity disparity is at most \(O(t_0^{1-\epsilon/2}p_\mathrm{gr})\), since \(t_0^{-\epsilon/2}\checkmark p_{gr}^2\). That is there exists a constant \(C'_0\) such that \(P_0^c\le C'_0p_\mathrm{gr}t_0^{1-\epsilon/2}\), as required. □

Now, as noted before Proposition 6.82, we can only obtain such disparity from such edges which we wish to balance out having been used in the matching \(M_0^o\).

Proposition 6.83. _There exists a constant c such that at least ct_<sub>0</sub>_p_<sub>gr</sub> _edges of_ \(M_0^o\) _are wrap-around edges of each type which avoid I_<sub>_t_<sub>20</sub></sub>.

