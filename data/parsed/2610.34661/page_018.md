is active; the analysis does not use an upper bound for it. Since \(\Phi_H\in V_h^0\), Step 4 is one Newton step on the fine mesh started from the coarse solution, cf. \[37, 19\].

## 5.2 Error analysis

Throughout this subsection, \(\Phi_h\in V_h^0\) denotes the solution of the fine-mesh nonlinear problem (41) with _U_<sup>∗</sup>=_U<sub>h</sub>_, i.e., the "exact" fine-mesh finite element solution, and \(u_h=G+\Psi_h+\Phi_h\) as in Corollary 4.10. The first lemma is the analogue of \[19, Lemma 4.1\] and shows that the two-grid solution differs from the fine-mesh solution by a quantity that is quadratic in the coarse-mesh error.

**Lemma 5.1.** _Let Assumption 2.1 and_ (3) _hold and_ \(\tau>0\)_. Let_ \(\Phi_H\in V_H^0\subset V_h^0\) _be any function and let_ \(\Phi_h^\mathrm{tg}\in V_h^0\) _be defined by_ (58)_. Then_

\(\left|\left|\Phi_h-\Phi_h^\mathrm{tg}\right|\right|\right|\le\frac{1}{2}C_2C_P\epsilon_p^{-1/2}\left|\left|\Phi_h-\Phi_H\right|\right|_{0,4}^2.\) (61)

_Proof._ Write \(b(\xi):=\rho_\tau(U_h+\xi)\) for the fine-mesh nonlinearity, so that \(b'(\xi)=\rho'_\tau(U_h+\xi)\) and \(|b''(\xi)|\le C_2\) a.e. in _D<sub>s</sub>_ by (21). Let \(\chi\in V_h^0\) and put \(\theta:=\Phi_h-\Phi_H\in V_h^0\). By Taylor’s formula with integral remainder, a.e. in _D<sub>s</sub>_,<tbc>

\(b(\Phi_h)=b(\Phi_H)+b'(\Phi_H)\theta+\int_0^1(1-\vartheta)b''(\Phi_H+\vartheta\theta)\theta^2\mathrm{d}\vartheta.\)

<tbc>Testing the fine problem (41) (with _U_<sup>∗</sup>=_U<sub>h</sub>_) with \(\chi\) and inserting this expansion,

\(0=a(\Phi_h,\chi)+\left(b(\Phi_h),\chi\right)_{D_s}=a(\Phi_H,\chi)+\left(b(\Phi_H),\chi\right)_{D_s}+a(\theta,\chi)+\left(b'(\Phi_H)\theta,\chi\right)_{D_s}+R(\chi),\text{(62)}\)

where

\(R(\chi):=\int_0^1(1-\vartheta)\left(b''(\Phi_H+\vartheta\theta)\theta^2,\chi\right)_{D_s}\mathrm{d}\vartheta\)

satisfies

\(|R(\chi)|\le\frac{1}{2}C_2\left|\left|\theta\right|\right|_{0,4}^2\left|\left|\chi\right|\right|_{0,2}.\) (63)

On the other hand, (58) can be written as<tbc>

\(a(\Phi_h^\mathrm{tg}-\Phi_H,\chi)+\left(b'(\Phi_H)(\Phi_h^\mathrm{tg}-\Phi_H),\chi\right)_{D_s}=-a(\Phi_H,\chi)-\left(b(\Phi_H),\chi\right)_{D_s}.\)

<tbc>Adding this identity to (62) and rearranging gives, with \(\omega:=\Phi_h-\Phi_h^\mathrm{tg}=\theta-(\Phi_h^\mathrm{tg}-\Phi_H)\),<tbc>

\(a(\omega,\chi)+\left(b'(\Phi_H)\omega,\chi\right)_{D_s}=-R(\chi)\forall\chi\in V_h^0.\)

<tbc>Choosing \(\chi=\omega\), using \(b'>0\), (63), (10) and (13),

\(\left|\left|\left|\omega\right|\right|\right|^2\le a(\omega,\omega)+\left(b'(\Phi_H)\omega,\omega\right)_{D_s}=-R(\omega)\le\frac{1}{2}C_2\left|\left|\theta\right|\right|_{0,4}^2C_P\epsilon_p^{-1/2}\left|\left|\left|\omega\right|\right|\right|,\)

which gives (61) after dividing by \(\left|\left|\left|\omega\right|\right|\right|\).

We now combine Lemma 5.1 with the _L_<sup>4</sup> estimates of Corollary 4.9, applied on both meshes.

