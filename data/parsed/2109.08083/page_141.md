<tbc>Thus, since \(t_0^{-\epsilon}\sum_{v\in V_O^{X\pm Y}(H)}d_{w_H^o}(v)\le t_0^{1-\epsilon}\), we have that<tbc>

\(|V_O^{X+Y}(H^c)|=(1\pm O(t_0^{-2\epsilon}))\sum_{v\in V_O^{X-Y}(H)}(1-d_{w_H^o}(v))\pm(1\pm\alpha_G)t_0^{1-\epsilon} p_\mathrm{gr},\)

<tbc>and

\(|V_O^{X-Y}(H^c)|=\sum_{v\in V_O^{X\pm Y}(H)}(1-d_{w_H^o}(v))\pm(1\pm\alpha_G)t_0^{1-\epsilon} p_\mathrm{gr}\)

and the result follows. □

Without loss of generality, assume that there are more odd parity vertices in _V(H<sup>c</sup>_\[_X-Y_\]) than _V(H<sup>c</sup>_\[_X+Y_\]), and thus fewer even vertices in _V(H<sup>c</sup>_\[_X-Y_\]) than _V(H<sup>c</sup>_\[_X+Y_\]). Hence to fix the parity issues, we wish to greedily form \(M'_H\supseteq M_H^o\) by adding _P<sub>H<sup>c</sup></sub>_ disjoint edges from _H<sup>c</sup>_, such that they have even and odd vertices in the _X+Y_ and _X-Y_ parts respectively. We simultaneously try to cover any vertices outside _I_<sub>_t_<sub>0</sub></sub>, using these additional edges as much as possible to balance the parity issues, and then deal with any remaining parity issues after this cover step.

Let \(U_{H^c}^X\) and \(U_{H^c}^Y\) denote the sets of vertices in \((V(H^c)\backslash I_{t_0})\cap X\) and \((V(H^c)\backslash I_{t_0})\cap Y\) respectively. We’ll drop the subscript _H<sup>c</sup>_ when it is clear from context. (Since _I_<sub>_t_<sub>0</sub></sub> covers \(V(H^c)\cap X\pm Y\) , there are no other vertices to consider outside of the target interval.)

Proposition 6.70. _We have that_<tbc>

\(|U^{X/Y}|\le t_0^{1-\epsilon} p_\mathrm{gr}.\)

<tbc>Proof. By (6.13) we have that

\(|U^{X/Y}|=\sum_{v\in V(H[X/Y])\backslash I_{t_0}}(1-d_{w_H^o}(v))\pm|V(H[X/Y])\backslash I_{t_0}|t_0^{-\epsilon}\)<br>
\(\le|V(H[X/Y])\backslash I_{t_0}|(2\alpha_G+t_0^\epsilon),\)

since we know from Proposition 6.65 that \(d_{w_H^o}(v)\ge 1-2\alpha_G\) for every \(v\in V(H)\backslash I_{t_0}\). Then since \(|V(\mathcal{T}[X/Y])\backslash I_{t_0}|=\frac{2t_0}{3}\) , by Theorem 3.28(i) we have that,

\(|V(H[X/Y])\backslash I_{t_0}|\le\frac{2.1t_0p_\mathrm{gr}}{3}.\)

Since \(\alpha_G\checkmark t_0^{-\epsilon}\), the claim follows. □

Now for a vertex \(v\in U^X\cup U^Y\) we want to lower bound the number of feasible edges that we may cover _v_ by in _H<sup>c</sup>_, which also help to balance out the parity disparity. We deliberately restrict to edges which avoid vertices in _I_<sub>_t_<sub>20</sub></sub>. This is so that any properties that this process affects are only to vertices with index of size \(\Theta(n)\). In this way we are helping to preserve ‘nice’ properties of smaller order vertices (which we need to last longer for the process to be successful) in a straightforward way.

Proposition 6.71. _Every vertex_ \(v\in(V(H^c)\backslash I_{t_1})\cap(X\cup Y)\) _satisfies_

\(|E_{H^c}(v,I_{t_0}\backslash I_{t_{20}})\cap E_{AB}(\mathcal{T})|\ge\frac{t_0p_\mathrm{gr}^3}{1500},\)

_for_ \(AB\in\{OE,EO\}\).

