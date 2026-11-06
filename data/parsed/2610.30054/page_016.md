**Proposition 3.5** (From partial direct sum to direct sum)**.** _Let_ \(m,t\ge 1\) _be integers. Let T_<sub>1</sub>_,...,T<sub>m</sub> be tensors with_ \(T_\ell\in U\otimes V_\ell\otimes W_\ell\)_. Then_

\((T_1\oplus\cdots\oplus T_m)\otimes\mathsf{P}_{1,t}\triangleleft(T_1\oplus_1\cdots\oplus_1T_m)\otimes\mathsf{P}_{m,t}.\)

Note how in the degeneration of Proposition 3.5, the right-hand side has the polynomial multiplication tensor P_<sub>m,t</sub>_ as a factor, and the left-hand side the polynomial multiplication tensor P<sub>1_,t_</sub>. We may think of P_<sub>m,t</sub>_ as a resource that enables the degeneration while being partially "consumed" in the process, leaving P<sub>1_,t_</sub> in the result.

_Proof._ Let \(T=T_1\oplus_1\cdots\oplus_1T_m\). Without loss of generality (embed the spaces into F_<sup>n</sup>_ for a large enough _n_, which gives restrictions in both directions), we take \(U=V_\ell=W_\ell=\mathbb{F}^n\). Let \(\{e_a\}_a\), \(\{e_b^\ell\}_b\) and \(\{e_c^\ell\}_c\) be the standard bases for _U_, \(V_\ell\) and \(W_\ell\) respectively. By definition,

\(T\otimes\mathsf{P}_{m,t}=\sum_{\ell=1}^m\sum_{a,b,c=1}^n\sum_{i\in[m],j\in[t]}(T_\ell)_{a,b,c}\left(e_a\otimes e_i\right)\otimes\left(e_b^\ell\otimes e_j\right)\otimes\left(e_c^\ell\otimes e_{i+j-1}\right).\) (3.2)

We will apply a monomial degeneration, as in Lemma 2.6, to this tensor. Define the weights<tbc>

\(w_1(e_a\otimes e_i)=i^2,w_2(e_b^\ell\otimes e_j)=\ell^2+2\ell(j-1),w_3(e_c^\ell\otimes e_k)=-2\ell k.\)

<tbc>On the term with indices \(\ell\), _i_ and _j_, the third-leg index is _k=i+j_-1, and the sum of the weights is \(i^2+\ell^2+2\ell(j-1)-2\ell(i+j-1)=(i-\ell)^2\). This is nonnegative, and zero exactly when \(i=\ell\). So \(T\otimes\mathsf{P}_{m,t}\) degenerates to

\(\sum_{\ell=1}^m\sum_{a,b,c}\sum_{j\in[t]}(T_\ell)_{a,b,c}\left(e_a\otimes e_\ell\right)\otimes(e_b^\ell\otimes e_j)\otimes(e_c^\ell\otimes e_{\ell+j-1}).\)

The \(\ell\)th summand lies in \((U\otimes e_\ell)\otimes(V_\ell\otimes\mathbb{F}^t)\otimes(W_\ell\otimes\mathbb{F}^{m+t-1})\), so the summands no longer share the first leg. Mapping \(e_c^\ell\otimes e_{\ell+j-1}\) to \(e_c^\ell\otimes e_j\), and all other basis vectors to 0, on the third leg restricts this tensor to \((T_1\otimes\mathsf{P}_{1,t})\oplus\cdots\oplus(T_m\otimes\mathsf{P}_{1,t})=(T_1\oplus\cdots\oplus T_m)\otimes\mathsf{P}_{1,t}\).

## 3.3 Concavity degeneration for P_<sub>a,b</sub>_

In this subsection we will prove a degeneration relation among polynomial multiplication tensors P_<sub>a,b</sub>_, which can be interpreted as a discrete concavity in _b_. We will first prove it using Lemma 2.5. Afterwards, we will give a second proof over C, using the Clebsch-Gordan rule for representations of the special linear group SL<sub>2</sub>(C).

**Lemma 3.6** (Concavity degeneration)**.** _Let_ \(a\ge 1\) _and_ \(b\ge 2\) _be integers. Then_<tbc>

\(\mathsf{P}_{a,b+1}\oplus_1\mathsf{P}_{a,b-1}\triangle_1\mathsf{P}_{a,b}\oplus_1\mathsf{P}_{a,b}.\)

<tbc>_Proof._ We will apply Lemma 2.5 to the bilinear map that sends (_f,(g,h_)) to (_fg,fh_), whose tensor is \(\mathsf{P}_{a,b}\oplus_1\mathsf{P}_{a,b}\), and to subspaces for which the induced maps on the subspaces and on the quotients have tensors P_<sub>a,b</sub>_-1 and P_<sub>a,b</sub>_+1. For every integer \(d\ge 0\), let \(\mathcal{W}_d:=\mathbb{F}[t]_{\le d}\). For every integer \(d\ge 2\), let<tbc>

\(\iota_d:\mathcal{W}_{d-2}\rightarrow\mathcal{W}_{d-1}\oplus\mathcal{W}_{d-1}:p\mapsto(-tp,p),\sigma_d:\mathcal{W}_{d-1}\oplus\mathcal{W}_{d-1}\rightarrow\mathcal{W}_d:(g,h)\mapsto g+th.\)

<tbc>Then \(\iota_d\) is injective and \(\sigma_d\) is surjective. For \(g,h\in\mathcal{W}_{d-1}\), we have _g+th_=0 exactly when _g_=-_th_ and \(h\in\mathcal{W}_{d-2}\), so the kernel of \(\sigma_d\) is the image of \(\iota_d\). Let \(V:=\mathcal{W}_{b-1}\oplus\mathcal{W}_{b-1}\) and \(W:=\mathcal{W}_{a+b-2}\oplus\mathcal{W}_{a+b-2}\), and consider the bilinear map<tbc>

\(\mu:\mathcal{W}_{a-1}\times V\rightarrow W:\left(f,(g,h)\right)\mapsto(fg,fh),\)

