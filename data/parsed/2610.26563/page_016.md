where _e<sub>a</sub>,e<sub>b</sub>_ are the standard basis vectors of C_<sup>n</sup>_.

Applying this identity independently in all _d_ coordinates gives<tbc>

\(\sum_{s=1}^m\big\langle C^{(s)},Z^{(s)}\big\rangle=\sum_{s=1}^m\sum_{\mathbf{i}\in\unknown 0,n-1\unknown^d}A_{\mathbf{i}|_{U_s^c}}^{(s)}B_{\mathbf{i}|_{V_s^c}}^{(s)}Z_{\mathbf{i}|_{W_s^c}}^{(s)}.\) (75)

<tbc>Regrouping by<tbc>

\(\alpha=\mathbf{i}|_{W_s^c}\) (76)

<tbc>yields

\(\sum_{s=1}^m\big\langle C^{(s)},Z^{(s)}\big\rangle=\sum_{s=1}^m\sum_{\alpha\in\unknown 0,n-1\unknown^{2N}}\left(\sum_{\mathbf{i}\in\unknown 0,n-1\unknown^d}A_{\mathbf{i}|_{U_s^c}}^{(s)}B_{\mathbf{i}|_{V_s^c}}^{(s)}\right)Z_\alpha^{(s)}.\) (77)

Since the _Z_<sup>(_s_)</sup> are arbitrary, the displayed coefficient is precisely the output tensor _C_<sup>(_s_)</sup>.

Finally, the algorithm performs one scalar multiplication for each<tbc>

\(\mathbf{k}\in\unknown 0,n+1\unknown^d,\)

<tbc>and all other operations are linear. Hence the bilinear rank is at most

\(|\unknown 0,n+1\unknown^d|=(n+2)^d=(n+2)^{3N}.\) (78)

## 5.6 Centered corrections and exact rank

For a fixed-shape conflict-free family, the weighted embedding gives an exact algorithm with rank at most (_n_+2)_<sup>d</sup>_. We now use the smaller centered dimension _n_+1 and cancel replicated cross terms by lower-order aggregates.

Let

\(\mathcal{S}=\{\mathcal{S}_1,\dots,\mathcal{S}_m\},\mathcal{S}_t=(U_t,V_t,W_t),U_t\sqcup V_t\sqcup W_t=F,\) (79)

where _t_=1_,...,m_ and the part sizes may depend on _t_.

Assign independent input blocks _X_<sup>(_t_)</sup>_,Y_<sup>(_t_)</sup> and output variables _Z_<sup>(_t_)</sup> to each S_<sub>t</sub>_. In particular, for \(t\neq t'\), _X_<sup>(_t_)</sup> and \(X^{(t^\prime)}\) are distinct blocks even when \(U_t=U_{t^\prime}\), and similarly for _Y_ and _Z_. The resulting target direct sum is

\(\phi_\mathcal{S}(X,Y,Z)=\sum_{t=1}^m\sum_{\mathbf{i}\in\unknown 0,n-1\unknown^F}X_{\mathbf{i}|_{U_t^c}}^{(t)}Y_{\mathbf{i}|_{V_t^c}}^{(t)}Z_{\mathbf{i}|_{W_t^c}}^{(t)}.\) (80)

The summand indexed by _t_ is the matrix multiplication tensor<tbc>

\(\big\langle n^{|V_t|},n^{|W_t|},n^{|U_t|}\big\rangle.\)

<tbc>**Definition 13** (Centered lifting)**.** _Let_ \(P\subseteq S\subseteq F\)_, and let_ \(T\in(\mathbb{C}^n)^{\otimes|F\backslash S|}\) _have modes indexed by F_\\_S. Define_ \(\Gamma_S^P(T)\in(\mathbb{C}^{n+1})^{\otimes|F\backslash P|}\) _by centering T and replicating it along S_\\_P:_

\(\Gamma_S^P(T)_\mathbf{j}=\big(\mu^{\otimes|F\backslash S|}(T)\big)_{\mathbf{j}|_{F\backslash S}},\mathbf{j}\in\unknown 0,n\unknown^{F\backslash P}.\) (81)

_We abbreviate_ \(\Gamma_S^\emptyset\) _by_ \(\Gamma_S\).

To cancel cross terms that share replicated coordinates _P_, we aggregate all lower-order liftings whose input blocks omit these coordinates.

