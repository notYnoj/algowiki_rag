<tbc>As was the case for _V<sub>S</sub>_ we have that

\(-\frac{3b^{1/3}|E_\mathcal{T}(v,S)|}{np}+\frac{3e_d|E_\mathcal{T}(v,S)|}{n^2p}=\Theta\left(\frac{b^{1/3}|E_\mathcal{T}(v,S)|}{np}\right)\le 0\)

and the ‘big-O’ terms are all \(o\left(\frac{b^{1/3}|E_\mathcal{T}(v,S)|}{np}\right)\) and we also yield that \(\mathbb{E}'(\Delta E_{v,S}^-(i))\ge 0\) by the same arguments.

Finally, concerning the trend hypotheses, by similar arguments we get that

\(\mathbb{E}'(\Delta Z_\mathcal{A}^+(i))\le\)<br>
\(-\frac{12(|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{12}+b^{1/3}|Z_\mathcal{A}(\mathcal{T}^{-A^*})|)(np^3-e_d)}{n^2p^4}+\frac{12|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{11}}{n}\)<br>
\(+O\left(\frac{|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{12}}{n^2p^4}+\frac{|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{10}}{|V(0)|^2}+\frac{e_q|Z_\mathcal{A}(\mathcal{T}^{-A^*})|np^{15}}{Q(i)^2}+\frac{b|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{11}}{n}\right)\)<br>
\(\le-\frac{12b^{1/3}|Z_\mathcal{A}(\mathcal{T}^{-A^*})|}{np}+\frac{12e_d|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^8}{n^2}\)<br>
\(+O\big(\frac{|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^8}{n^2}+\frac{|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{10}}{n^2}+\frac{e_q|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^7}{n^3}\)<br>
\(+\frac{b|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{11}}{n}+\frac{e_db^{1/3}|Z_\mathcal{A}(\mathcal{T}^{-A^*})|}{n^2p^4}\big),\)

and as before see both that

\(-\frac{12b^{1/3}|Z_\mathcal{A}(\mathcal{T}^{-A^*})|}{np}+\frac{12e_d|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^8}{n^2}=\Theta\left(\frac{b^{1/3}|Z_\mathcal{A}(\mathcal{T}^{-A^*})|}{np}\right)\le 0\)

and the ‘big-O’ terms are \(o\left(\frac{b^{1/3}|Z_\mathcal{A}(\mathcal{T}^{-A^*})|}{np}\right)\). Again we have that the details show ing \(\mathbb{E}'(\Delta Z_\mathcal{A}^-(i))\ge 0\) follow by precisely the same arguments.

It remains to confirm the boundedness hypotheses for each of our secondary variables. Once again the strategy is very similar to that for the vertex degrees. One difference is to note immediately (as already noted when verifying the trend hypotheses) that since _e<sub>V<sub>S</sub></sub>_, _e<sub>E<sub>v,S</sub></sub>_ and _e<sub>Z<sub>A</sub></sub>_ are all constant so when considering the maximum change in variable from step _i_ to step _i_+1 this term does not need any consideration. It then also follows that the same bounds that apply for \(\Delta X^+(i)\) will also immediately apply for \(\Delta X^-(i)\). For degree-type properties we again have that -|_E_<sub>T</sub>(_v,S_)|_p_<sup>3</sup> is increasing and in particular \(0\le|E_\mathcal{T}(v,S)|(p(i+1)^3-p(i)^3)=O\left(\frac{|E_\mathcal{T}(v,S)|}{n}\right)\), and \(0\ge\Delta E_{v,S}(i)\ge-4\) (due to the maximum pair degree of 1 unless (_v,u_) is such that \(v\in V^{X+Y}\) and \(u\in V^{X-Y}\) or vice versa, in which case pair degree is at most 2). Then we may set \(\theta_E=O\left(\frac{|E_\mathcal{T}(v,S)|}{n}\right)\) and \(\Theta_E=C_{E_{v,S}}\) for some constant _C<sub>E<sub>v,S</sub></sub>_ satisfying \(C=max\{4,11\theta_E\}\). Then \(\theta_E\Theta_Enplog^2(n)=O(|E_\mathcal{T}(v,S)|plog^2(n))\checkmark b^{2/3}|E_\mathcal{T}(v,S)|^2\) and this cover the cases for both \(\Delta E_{v,S}^\pm(i)\). The argument is similar for \(\Delta V_S^\pm\). In particular we have \(0\le|S|(p(i+1)^3-p(i)^3)=O\left(\frac{|S|}{n}\right)\) and also that \(0\ge\Delta V_S(i)\ge-4\) since removing an edge from _T<sub>i</sub>_ removes at most 4 vertices from \(V(i)\supseteq V(i)\cap S\). Then we may set \(\theta_V=O\left(\frac{|S|}{n}\right)\) and \(\Theta_V=C_{V_S}\) for some constant _C<sub>V<sub>S</sub></sub>_ satisfying \(C_{V_S}=max\{4,11\theta_V\}\)

