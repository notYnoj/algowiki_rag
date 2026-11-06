<tbc>\(c_{H_i,v}\le\mathrm{log}^{m^*}(n)t_i^{-\epsilon_1}\) for every \(i\le l'\) for some \(l'\le l\), and that \(H_{l^\prime}\) has depth _j_. By Lemma 6.53, we have since \(\delta_{H_{l^\prime+1},v}\equiv w_{l^\prime+1}(E_{H_{l^\prime+1}}(v,I_{t_{l^\prime+2}}))\) that

\(\delta_{H_{l^\prime+1},v}=\)<br>
\(\frac{w_{1^*}(E_{H_{1^*}}(v,I_{t_{l^\prime+2}}))}{w_{1^*}(E_{H_{1^*}}(v,I_{t_{l^\prime+1}}))}\prod_{t^*(k_{j-3})\le i\le l^\prime}\left(1\pm 2.1\left(\frac{1.1c_{H_i,v}}{\delta_{H_i,v}}+1.2\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}\right)\right).\)

Now, we have that \(\delta_*^-\le\frac{w_{1^*}(E_{H_{1^*}}(v,I_{t_{l^\prime+2}}))}{w_{1^*}(E_{H_{1^*}}(v,I_{t_{l^\prime+1}}))}\le\delta_*^+\) and, by induction, that \(\frac{1.1c_{H_i,v}}{\delta_{H_i,v}}\le\frac{2.2\mathrm{log}^{m^*}(n)t_i^{-\epsilon_1}}{\delta_*^-}\) , for every \(t^*(k_{j-3})\le i\le l'\) and every \(v\in V(H_{l^\prime+1})\), where \(1\ge\delta_*^->0\) is an absolute constant. In particular we have that

\(\prod_{t^*(k_{j-3})\le i\le l^\prime}\left(1\pm 2.1\left(\frac{1.1c_{H_i,v}}{\delta_{H_i,v}}+1.2\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}\right)\right)=\)<br>
\(\left(1\pm c\mathrm{log}^{m^*}(n)t_{l^\prime}^{-\epsilon_1}\right)^{40\mathrm{loglog}(n)}=(1\pm c\mathrm{log}^{m^*+1}(n)t_{l^\prime}^{-\epsilon_1}),\)

where we can take \(c=\frac{5}{\delta_*^-}+1\) and have that _c\>_0 is an absolute constant. In particular, this yields that

\(\delta_*^-/2\le(1-c\mathrm{log}^{m^*+1}(n)t_{l^\prime}^{-\epsilon_1})\delta_*^-\le\delta_{H_{l^\prime+1},v}\le(1+c\mathrm{log}^{m^*+1}(n)t_{l^\prime}^{-\epsilon_1})\delta_*^+\le 2\delta_*^+,\)

as required. It remains to upper bound \(c_{H_{l^\prime+1},v}\) for every \(v\in V(H_{l^\prime+1})\). For those vertices _v_ which are not \(l'\)-reachable, we have that \(c_{H_{l^\prime+1},v}\le t_1^{-\epsilon_1}\le\mathrm{log}^{m^*}(n)t_{l^\prime+1}^{-\epsilon_1}\). By Lemma 6.52 we have that, given (_H<sub>i</sub>,w<sub>i</sub>_) is _i_-permissible, \(c_{H_{i+1},v}\le\frac{c_{H_i,v}}{\delta_{H_i,v}}+2.2\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}\). Now, by induction we have that \(\delta_{H_i,v}\ge\delta_*^-/2\) for every \(i\le l'\) and so we may write \(c_{H_{i+1},v}\le\frac{2c_{H_i,v}}{\delta_*^-}+2.2\mathrm{log}^{3l_3+7}(n)t_i^{-\epsilon_1}\) for every \(i\le l'\). In particular, this yields that

\(c_{H_{l^\prime+1},v}\le\left(\frac{2}{\delta_*^-}\right)^{l^\prime-t^*(k_{j-3})}c_{H_{t^*(k_{j-3}),v}}+\sum_{i=1}^{l^\prime-t^*(k_{j-3})}\left(\frac{2}{\delta_*^-}\right)^i\cdot 2.2t_{l^\prime-i}^{-\epsilon_1}.\)

Furthermore, since \(H_{l^\prime}\) has depth _j_, we have that \(c_{H_{t^*(k_{j-3}),v}}=c_{H_{1^*,v}}\le t_1^{-\epsilon_1}\) for every \(v\in H_{t^*(k_{j-3})}\) and \(2.2\mathrm{log}^{3l_3+7}(n)t_{l^\prime-i}^{-\epsilon_1}\le 2.2\mathrm{log}^{3l_3+7}(n)t_{l^\prime}^{-\epsilon_1}\) for every \(i\in[1,l'-t^*(k_{j-3})]\), where \(l'-t^*(k_{j-3})\le 40\mathrm{loglog}(n)\). Thus we find that

\(c_{H_{l^\prime+1},v}\le\left(\frac{2}{\delta_*^-}\right)^{l^\prime-t^*(k_{j-3})}t_1^{-\epsilon_1}+2.2\mathrm{log}^{3l_3+7}(n)t_{l^\prime}^{-\epsilon_1}\sum_{i=1}^{l^\prime-t^*(k_{j-3})}\left(\frac{2}{\delta_*^-}\right)^i\)<br>
\(\le\mathrm{log}^{40\mathrm{log}(2/\delta_*^-)}(n)t_1^{-\epsilon_1}+40\mathrm{loglog}(n)\mathrm{log}^{40\mathrm{log}(2/\delta_*^-)+3l_3+7}(n)t_{l^\prime}^{-\epsilon_1}.\)

In particular, \(c_{H_{l^\prime+1},v}\le\mathrm{log}^{80\mathrm{log}(2/\delta_*^-)}(n)t_{l^\prime}^{-\epsilon_1}\), completing the proof. □

The following two propositions will be useful for the subsequent lemmas and corollaries.

Proposition 6.55. _Suppose that_ (_H<sub>i</sub>,w<sub>i</sub>_) _is i-permissible for every_ \(i\le l\)_. Then_

\(\frac{c_{H_i}}{\delta_{H_i}}\le\frac{2\mathrm{log}^{m^*}(n)t_l^{-\epsilon_1}}{\delta_*^-}\)

