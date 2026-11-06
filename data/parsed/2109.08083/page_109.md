<tbc>such edges do not contain any vertices within _K_<sub>_j_+1</sub>. Hence, given that \(v\in G'\), the number of edges it is contained in within a particular subset of _K_<sub>_j_+1</sub> is not affected from _G_ to \(G'\). Thus, by _i_-permissibility, the claim follows, completing the proof. □

Remark 6.29. Among other things, the proof of Theorem 6.28 shows that any function _f<sub>S</sub>_ or _f<sub>v</sub>_ as defined in statements (K1) and (K2) of the theorem is vertex or _v_-edge allowable for \((G,\omega,t_i,\eta_1)\) respectively. Furthermore it shows that \(\omega\) is edge allowable for \((G,\omega,t_i,\eta_1)\).

Before proceeding with details of the vortex, we include the following propositions concerning \(d_{\omega^\circ}(v)\) and \(\omega(E_G(v,I_{t_{i+1}}))\) for any _i_-permissible \((G,\omega)\), which will be useful for the subsequent corollary to Theorem 6.28 (Corollary 6.32), and at various stages in the next section.

Proposition 6.30. _Let_ \((G,\omega)\) _be i-permissible such that_ \(\omega\) _is an almost-perfect fractional matching for G. We define_<tbc>

\(\delta_{G,v}:=\omega(E_G(v,I_{t_{i+1}})),\)

<tbc>_and let_ \(\delta_G:=min_{v\in V(G[I_{t_{i+1}}])}\delta_{G,v}\)_. Suppose that_ \(d_{\omega,G}(v)=1-c_{G,v}\) _for all_ \(v\in V(G)\) _and let c<sub>G</sub>_:=max_<sub>v</sub>c<sub>G,v</sub>. Then_

\(1-d_{\omega^\circ}(v)=\left(1\pm\frac{c_{G,v}}{\delta_{G,v}}\right)\omega(E_G(v,I_{t_{i+1}}))=\left(1\pm\frac{c_G}{\delta_G}\right)\omega(E_G(v,I_{t_{i+1}}))\)

_for every_ \(v\in V(G[I_{t_{i+1}}])\)

Proof. By _i_-permissibility we have that \(0\le c_{G,v}\le log^{l_4}(n)t_i^{-\epsilon_1}\) for each \(v\in V(G[I_{t_{i+1}}])\). By Proposition 6.25 we have for each \(v\in V(G[I_{t_{i+1}}])\) that

\(1-d_{\omega^\circ}(v)=\omega(E_G(v,I_{t_{i+1}}))+c_{G,v}\)<br>
\(=\left(1+\frac{c_{G,v}}{\delta_{G,v}}\right)\omega(E_G(v,I_{t_{i+1}}))\le\left(1+\frac{c_G}{\delta_G}\right)\omega(E_G(v,I_{t_{i+1}})).\)

Additionally

\(1-d_{\omega^\circ}(v)\ge\omega(E_G(v,I_{t_{i+1}}))\ge\left(1-\frac{c_{G,v}}{\delta_{G,v}}\right)\omega(E_G(v,I_{t_{i+1}}))\)<br>
\(\ge\left(1-\frac{c_G}{\delta_G}\right)\omega(E_G(v,I_{t_{i+1}})),\)

proving the proposition. (Note that clearly \(\delta_{G,v},c_{G,v}\ge 0\) for all \(v\in V(G[I_{t_{i+1}}])\) since \(\omega\) is a fractional matching.) □

Proposition 6.31. _Given that_ \((G,\omega)\) _is i-permissible, for c<sub>G</sub> and_ \(\delta_G\) _as defined in Proposition 6.30 we have that_

\(\frac{c_G}{\delta_G}\le\frac{log^{l_4+l_3+2}(n)}{c_1t_i^{\epsilon_1}}.\)

Proof. We have by _i_-permissibility of \((G,\omega)\) that \(c_G\le log^{l_4}(n)t_i^{-\epsilon_1}\) and by Corollary 6.27 that \(\delta_G=min_{v\in V(G[I_{t_{i+1}}])}\omega(E_G(v,I_{t_{i+1}}))\ge\frac{c_1}{log^{l_3+2}(n)}\). □

