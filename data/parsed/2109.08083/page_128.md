<tbc>had the same properties as in (_H_<sub>1<sup>∗</sup></sub>_,w_<sub>1<sup>∗</sup></sub>). Thus by Lemma 6.52(iv)

\(w_{i+1}(E_{H_{i+1}}(v,S_1,S_2,S_3))=\)<br>
\(\left(1\pm\left(\frac{1.1c_{H_i,v}}{\delta_{H_i,v}}+1.2\mathrm{log}^{3l_2+7}(n)t_i^{-\epsilon_1}\right)\right)\frac{w_i(E_{H_i}(v,S_1,S_2,S_3))}{w_i(E_{H_i}(v,I_{t_{i+1}}))}\)

for every \(t^*(k_{j-3})\le i\le l\), and

\(w_{t^*(k_{j-3})}(E_{H_{t^*(k_{j-3})}}(v,S_1,S_2,S_3))=w_{1^*}(E_{H_{1^*}}(v,S_1,S_2,S_3)).\)

Iterating to get \(\frac{w_i(E_{H_i}(v,S_1,S_2,S_3))}{w_i(E_{H_i}(v,I_{t_{i+1}}))}\) in terms of \(\frac{w_{i-1}(E_{H_{i-1}}(v,S_1,S_2,S_3))}{w_{i-1}(E_{H_{i-1}}(v,I_{t_{i+1}}))}\) , which is pos sible for all \(t^*(k_{j-3})+1\le i\le l\) by assumption that (_H<sub>i</sub>,w<sub>i</sub>_) is _i_-permissible in each of these cases, we get that

\(\frac{w_i(E_{H_i}(v,S_1,S_2,S_3))}{w_i(E_{H_i}(v,I_{t_{i+1}}))}=\)<br>
\(\frac{\left(1\pm\left(\frac{1.1c_{H_{i-1},v}}{\delta_{H_{i-1},v}}+1.2\mathrm{log}^{3l_2+7}(n)t_{i-1}^{-\epsilon_1}\right)\right)w_{i-1}(E_{H_{i-1}}(v,S_1,S_2,S_3))w_{i-1}(E_{H_{i-1}}(v,I_{t_i}))}{\left(1\pm\left(\frac{1.1c_{H_{i-1},v}}{\delta_{H_{i-1},v}}+1.2\mathrm{log}^{3l_2+7}(n)t_{i-1}^{-\epsilon_1}\right)\right)w_{i-1}(E_{H_{i-1}}(v,I_{t_i}))w_{i-1}(E_{H_{i-1}}(v,I_{t_{i+1}}))}\)<br>
\(=\left(1\pm 2.1\left(\frac{1.1c_{H_{i-1},v}}{\delta_{H_{i-1},v}}+1.2\mathrm{log}^{3l_2+7}(n)t_{i-1}^{-\epsilon_1}\right)\right)\frac{w_{i-1}(E_{H_{i-1}}(v,S_1,S_2,S_3))}{w_{i-1}(E_{H_{i-1}}(v,I_{t_{i+1}}))}.\)

This yields the result. □

We now obtain bounds for _c<sub>H<sub>i</sub>,v</sub>_ and \(\delta_{H_i,v}\) for every _i_ and _v_. Recall (from Proposition 6.30), that _c<sub>G,v</sub>_ and \(\delta_{G,v}\) are defined for \((G,\omega)\) an _i_-permissible pair for some _i_, and in this case, \(\delta_{G,v}:=\omega(E_G(v,I_{t_{i+1}}))\), and \(c_{G,v}:=1-d_{\omega,G}(v)=1-\omega(E_G(v,I_{t_i}))\). We also have that \(\delta_G:=\mathrm{min}_{v\in V(G[I_{t_{i+1}}])}\delta_{G,v}\), and \(c_G:=\mathrm{max}_{v\in V(G)}c_{G,v}\). We wish to show that both _c<sub>H<sub>i</sub>,v</sub>_ and \(\frac{c_{H_i,v}}{\delta_{H_i,v}}\) do not blow up through the process for all _i_ and _v_.

Recall further Definition 6.20:<tbc>

\(\delta_*^-:=\mathrm{min}\left\{\mathrm{min}_{i\in[c_h]}\frac{w_{1^*}(E_{H_{1^*}}(v,I_{t_{i+1}}))}{w_{1^*}(E_{H_{1^*}}(v,I_{t_i}))},\delta_{1^*}^-\right\}.\)

<tbc>We also define

\(\delta_*^+:=\mathrm{max}\left\{\mathrm{max}_{i\in[c_h]}\frac{w_{1^*}(E_{H_{1^*}}(v,I_{t_{i+1}}))}{w_{1^*}(E_{H_{1^*}}(v,I_{t_i}))},\delta_{1^*}^+\right\}\)

and note by Corollary 6.16 and Lemma 6.23, we have that \(1\ge\delta_*^\pm>c\) where _c\>_0 is an absolute constant. Furthermore, note that subsequently we have \(40\mathrm{log}(\frac{2}{\delta_*^-})>3l_3+7=28\).

Proposition 6.54. _There exists a constant_ \(1\le m^*\le 80\mathrm{log}\left(\frac{2}{\delta_*^-}\right)\) _such that for any l the following holds: Suppose that_ (_H<sub>i</sub>,w<sub>i</sub>_) _is i-permissible for every_ \(1^*\le i\le l\)_. Then for every_ \(1^*\le i\le l+1\) _and_ \(v\in V(H_i)\), \(\frac{\delta_*^-}{2}\le\delta_{H_i,v}\le 2\delta_*^+\)_, and_ \(c_{H_i,v}\le\mathrm{log}^{m^*}(n)t_i^{-\epsilon_1}\).

Proof. We prove the proposition via strong induction. First note that the base case is satisfied by Lemma 6.23. We now assume that \(\frac{\delta_*^-}{2}\le\delta_{H_i,v}\le 2\delta_*^+\), and

