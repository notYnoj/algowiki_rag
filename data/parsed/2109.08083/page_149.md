<tbc>where \(c_1c_2t_0^2p_\mathrm{gr}^4\gg\frac{t_0^{1+\eta}}{1-t_0^{-1}}\), as required to satisfy (6.2). Thus by Theorem 6.2 there exists a matching \(M_0^o\) such that (as well as (i)-(v)), we have that

\(|M_0^o\cap E_{AB}(H_0^o[I_{t_0}\backslash I_{t_{20}}])|=q_{AB}(M_0^o)=(1\pm t_0^{-\epsilon})\sum_{e\in E(H)}q_{AB}(e)w(e)\)<br>
\(=(1\pm t_0^{-\epsilon})\sum_{e\in E_{AB}(H_0^o[I_{t_0}\backslash I_{t_{20}}])}w_0(e)\)

for each \(AB\in\{OE,EO\}\), as claimed. □

Now in _H_<sub>0</sub> we still have wrap-around edges, and thus for _n_ odd we still have additional parity requirements to adjust for depending on the types of edges in \(M_0^o\).

**6.5.5. Parity to reach** _H_<sub>1</sub>**.** To adjust for any parity disparity in _H<sup>c</sup>_, we were able to simply balance out the disparity by _adding_ wrap-around edges of appropriate types. Now to adjust for any disparity in \(H_0^c\) (again presuming _n_ is odd) we cannot proceed in this way since vertices remaining to be covered may not have sufficiently large wrap around degree in _I_<sub>_t_<sub>1</sub></sub>. We now, however, have that every vertex should have sufficiently large non-wrap around degree into _I_<sub>_t_<sub>1</sub></sub>. (This was not the case for the first step, hence why we do it differently in each step.) Note, also, that any parity disparity can only be caused by the existence of edges of the relevant wrap-around type appearing in \(M_0^o\), thus we can try to fix the disparity by first _removing_ sufficiently many edges from \(M_0^o\) to reduce the disparity to 0.

Proposition 6.82. _There exists a constant_ \(C'_0\) _such that the parity disparity of_ \(H_0^c\), \(P_0^c\)_, satisfies_<tbc>

\(P_0^c\le C'_0p_\mathrm{gr}t_0^{1-\epsilon/2}.\)

<tbc>Proof. We have from (6.13) that<tbc>

\(|V_{O/E}^{X\pm Y}(H_0^c)|=\sum_{v\in V_{O/E}^{X\pm Y}(H_0)}1-d_{w_0^c}(v)\pm t_0^\epsilon\sum_{v\in V_{O/E}^{X\pm Y}(H_0)}d_{w_0^c}(v).\)

<tbc>We split the sum to consider vertices in _I_<sub>_t_<sub>1</sub></sub> and _I_<sub>_t_<sub>0</sub></sub>\\_I_<sub>_t_<sub>1</sub></sub> separately. In particular, we know for \(v\in I_{t_0}\backslash I_{t_1}\) that \(1-d_{w_0^c}(v)\le 2.2p_\mathrm{gr}^{-2}t_0^{-\epsilon}\), and furthermore, that \(|V_{O/E}^{X\pm Y}(H_0[I_{t_0}\backslash I_{t_1}])|\le|V_{O/E}^{X\pm Y}(H[I_{t_0}\backslash I_{t_1}])|(1+o(1))\frac{t_0p_\mathrm{gr}}{5}\) . Then since \(\sum_{v\in V_{O/E}^{X\pm Y}(H_0)}d_{w_0^c}(v)=O(t_0p_\mathrm{gr})\), the difference in remaining vertices of odd parity outside _I_<sub>_t_<sub>1</sub></sub> over both the _X+Y_ and _X-Y_ parts is at most<tbc>

\(O(t_0^{1-\epsilon} p_\mathrm{gr})+2.2p_\mathrm{gr}^{-2}t_0^{-\epsilon}(1+o(1))\frac{4t_0p_\mathrm{gr}}{5}\le 2p_\mathrm{gr}^{-1}t_0^{1-\epsilon}.\)

<tbc>Now, to consider the maximum disparity inside _I_<sub>_t_<sub>1</sub></sub>, recall from Corollary 6.80 that for each \(v\in V(H_0[I_{t_1}])\),<tbc>

\(1-d_{w_0^c}(v)=(1\pm 44.1C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})w_0(E_{H_0}(v,I_{t_1})),\)

<tbc>and by Proposition 6.78, that

\(w_0(E_{H_0}(v,I_{t_1}))=(1\pm 2.2C_0p_\mathrm{gr}^{-2}t_0^{-\epsilon})\frac{w_H(E_H(v,I_{t_1}))}{w_H(E_H(v,I_{t_0}))}.\)

