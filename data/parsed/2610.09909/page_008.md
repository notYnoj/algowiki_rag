<tbc>_Proof._ Let \(K\in\mathcal{T}_h^\Gamma\) be a cut element. By Remark 2.3, there exists a path of elements<tbc>

\(K=K_0,K_1,\dots,K_N\)

<tbc>such that \(K_N\in\mathcal{T}_h^\mathrm{in}\) and, for each _i_=1_,...,N_, the elements _K_<sub>_i_-1</sub> and _K<sub>i</sub>_ share a common face \(F_i\in\mathcal{F}_h^\Gamma\). Applying Lemma 3.2 successively along the path \(\{K_i\}_{i=0}^N\), we obtain<tbc>

\(\|v_h\|_{H^2(K)}^2\le C\big(\|v_h\|_{H^2(K_N)}^2+\sum_{i=1}^N\sum_{j=2}^{2k}h_{F_i}^{2j-3}\|\left\unknown\partial_n^jv_h\right\unknown\|_{L^2(F_i)}^2\big).\)

<tbc>For \(\mathbf{x}\in\Omega_h^\mathrm{in}\backslash\Omega\), Assumptions (P1)-(P2) give \(0\le\phi(\mathbf{x})\le Ch^{k+1}\) which implies \(|\Omega_h^\mathrm{in}\backslash\Omega|\le Ch^{k+1}\). The polynomial inverse estimate on the quasi-uniform mesh then yields<tbc>

\(\|v_h\|_{H^2(\Omega_h^\mathrm{in})}^2\le\|v_h\|_{H^2(\Omega)}^2+Ch^{k+1-d}\|v_h\|_{H^2(\Omega_h)}^2.\)

<tbc>Combining this bound with the preceding path estimates and using their bounded overlap, we can absorb the resulting \(Ch^{k+1-d}\|v_h\|_{H^2(\Omega_h)}^2\) term for sufficiently small _h_, since _k_+1-_d\>_0. We therefore obtain<tbc>

\(\|v_h\|_{H^2(\Omega_h)}^2\le C\big(\|v_h\|_{H^2(\Omega)}^2+j_h(v_h,v_h)\big).\) (3.4)

<tbc>Write \(v_h=\phi_hw_h=\phi w_h+(\phi_h-\phi)w_h\). Since \(\phi=0\) on \(\Gamma=\partial\Omega\), we have \(\phi w_h\in H^2(\Omega)\cap H_0^1(\Omega)\). The _H_<sup>2</sup>-regularity of the physical domain \(\Omega\) therefore gives

\(\|\phi w_h\|_{H^2(\Omega)}\le C\|\Delta(\phi w_h)\|_{L^2(\Omega)}\)<br>
\(\le C\|\Delta v_h\|_{L^2(\Omega)}+C\|\Delta((\phi_h-\phi)w_h)\|_{L^2(\Omega)}.\)

Consequently,

\(\|v_h\|_{H^2(\Omega)}\le C\|\Delta v_h\|_{L^2(\Omega)}+C\|(\phi_h-\phi)w_h\|_{H^2(\Omega)}.\) (3.5)

Using the approximation properties of \(\phi_h\), the product rule, and the local inverse inequalities, we obtain

\(\|(\phi_h-\phi)w_h\|_{H^2(\Omega)}\le C\big(h^{k-1}\|w_h\|_{L^\infty(\Omega_h)}+h^k\|w_h\|_{W^{1,\infty}(\Omega_h)}\)<br>
\(+h^{k+1}\|w_h\|_{W^{2,\infty}(\Omega_h)}\big)\le Ch^{k-1}\|w_h\|_{L^\infty(\Omega_h)}.\)

By the Hardy-type inequality associated with the exact level-set function \(\phi\),<tbc>

\(\|w_h\|_{L^\infty(\Omega_h)}\le C\|\phi w_h\|_{W^{1,\infty}(\Omega_h)}.\)

<tbc>Since \(\phi w_h=v_h-(\phi_h-\phi)w_h\), the product rule, the maximum-norm approximation properties of \(\phi_h\), and the inverse inequality yield<tbc>

\(\|w_h\|_{L^\infty(\Omega_h)}\le C\|v_h\|_{W^{1,\infty}(\Omega_h)}+C\left(\|\nabla(\phi_h-\phi)\|_{L^\infty(\Omega_h)}+h^{-1}\|\phi_h-\phi\|_{L^\infty(\Omega_h)}\right)\|w_h\|_{L^\infty(\Omega_h)}.\)

<tbc>For _h_ sufficiently small, the last term can be absorbed, and hence<tbc>

\(\|w_h\|_{L^\infty(\Omega_h)}\le C\|v_h\|_{W^{1,\infty}(\Omega_h)}\le Ch^{-d/2}\|v_h\|_{H^2(\Omega_h)}.\)

<tbc>It follows that<tbc>

\(\|(\phi_h-\phi)w_h\|_{H^2(\Omega)}\le Ch^{k-1-d/2}\|v_h\|_{H^2(\Omega_h)}.\) (3.6)

<tbc>Combining (3.5) and (3.6), we obtain<tbc>

\(\|v_h\|_{H^2(\Omega)}\le C\|\Delta v_h\|_{L^2(\Omega)}+Ch^{k-1-d/2}\|v_h\|_{H^2(\Omega_h)}.\)

<tbc>Substituting this estimate into (3.4) and taking square roots gives<tbc>

\(\|v_h\|_{H^2(\Omega_h)}\le C\big(\|\Delta v_h\|_{L^2(\Omega)}+j_h(v_h,v_h)^{1/2}+h^{k-1-d/2}\|v_h\|_{H^2(\Omega_h)}\big).\)

<tbc>Since \(k\ge 3\), the last term can be absorbed into the left-hand side for _h_ sufficiently small. Hence,

\(\|v_h\|_{H^2(\Omega_h)}^2\le C\big(\|\Delta v_h\|_{L^2(\Omega)}^2+j_h(v_h,v_h)\big)\le C\big(\|\Delta v_h\|_{L^2(\Omega_h)}^2+j_h(v_h,v_h)\big)\)

with \(\Omega\subset\Omega_h\), which is the desired estimate and concludes the proof. □

