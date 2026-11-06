<tbc>**6.5.2. Parity modifications and the greedy cover to reach** _H_<sub>0</sub>**.** First note that, as previously mentioned, these parity modifications are only required when _n_ is odd. In this case, in the first two steps we will need to modify \(M_H^o\) and the subsequent matching we shall obtain from _H_<sub>0</sub>, \(M_0^o\), to ensure that the leave _L_<sup>∗</sup> at the end of the process satisfies parity requirements for a particular ‘zero-summing’ strategy (i.e. that of Proposition 4.4).

We start by noting the distribution of odd and even vertices in parts \(|V_{O/E}^{X\pm Y}(H^c)|\). First note (trivially) that \(|V_O^{X+Y}(H^c)|+|V_E^{X+Y}(H^c)|=|V_O^{X-Y}(H^c)|+|V_E^{X-Y}(H^c)|\) with no error terms, since we only ‘lose’ vertices by removing disjoint edges, each of which removes exactly one from each part. Let \(P_G:=||V_O^{X+Y}(G)|-|V_O^{X-Y}(G)||\), the absolute difference in number of odd vertices in the _X+Y_ and _X-Y_ parts in some \(G\subseteq\mathcal{T}\) . We refer to _P<sub>G</sub>_ as the _parity disparity of G_. To calculate the parity disparity of _H<sup>c</sup>_, we shall use the valid layer intervals we have been keeping track of in Theorem 3.28 (iv) and which were originally introduced in Definition 3.27, which will enable us to break up particular summations into small subsets in a useful way.

Proposition 6.68. _The parity disparity of H<sup>c</sup>, P<sub>H<sup>c</sup></sub>, satisfies_<tbc>

\(P_{H^c}\le 2.1t_0^{1-\epsilon} p_\mathrm{gr}.\)

<tbc>Proof. We have from (6.13) that<tbc>

\(|V_O^{X\pm Y}(H^c)|=\sum_{v\in V_O^{X\pm Y}(H)}(1-d_{w_H^o}(v))\pm t_0^{-\epsilon}\sum_{v\in V_O^{X\pm Y}(H)}d_{w_H^o}(v).\)

<tbc>Claim 6.69.

\(\sum_{v\in V_O^{X-Y}(H)}(1-d_{w_H^o}(v))=(1\pm O(t_0^{-2\epsilon}))\sum_{v\in V_O^{X+Y}(H)}(1-d_{w_H^o}(v)).\)

Proof of claim. Let I be a partition of \([-\frac{n-1}{2},\frac{n-1}{2}]\) into consecutive inter vals of size \(t_0^{1-2\epsilon}\). Then for any interval \(I\in\mathcal{I}\), by Theorem 3.28 (iv), we have that \(|V_O^{X+Y}(H[I])|=(1\pm 2\alpha_G)|V_O^{X-Y}(H[I])|\). Now let _v<sub>I</sub>_ be the vertex in the middle of interval _I_ and let \(d_I:=(1-d_{w_H^o}(v_I))\). Then for every \(v\in I\), by Theorem 3.28 (ii) we have that \((1-d_{w_H^o}(v))=(1\pm O(t_0^{-2\epsilon}))d_I\). Finally, for two vertices _v_<sub>_X+Y_</sub> and _v_<sub>_X-Y_</sub> with the same index in parts _X+Y_ and _X-Y_ , we have that \(d_{w_T^o}(v_{X+Y})=d_{w_T^o}(v_{X-Y})\), and hence, by Theorem 3.28 (ii), \(d_{w_H^o}(v_{X+Y})=(1\pm 2\alpha_G)d_{w_H^o}(v_{X-Y})\). Thus, since \(t_0^{-2\epsilon}\gg\alpha_G\), we find that

\(\sum_{v\in V_O^{X-Y}(H)}(1-d_{w_H^o}(v))=\sum_{I\in\mathcal{I}}\sum_{v\in V_O^{X-Y}(H[I])}(1-d_{w_H^o}(v))\)<br>
\(=\sum_{I\in\mathcal{I}}\sum_{v\in V_O^{X-Y}(H[I])}(1\pm O(t_0^{-2\epsilon}))d_I=\sum_{I\in\mathcal{I}}|V_O^{X-Y}(H[I])|(1\pm O(t_0^{-2\epsilon}))d_I\)<br>
\(=(1\pm O(t_0^{-2\epsilon}))\sum_{I\in\mathcal{I}}|V_O^{X+Y}(H[I])|d_I=(1\pm O(t_0^{-2\epsilon}))\sum_{I\in\mathcal{I}}\sum_{v\in V_O^{X+Y}(H[I])}(1-d_{w_H^o}(v))\)<br>
\(=(1\pm O(t_0^{-2\epsilon}))\sum_{v\in V_O^{X+Y}(H)}(1-d_{w_H^o}(v)).\)

□

