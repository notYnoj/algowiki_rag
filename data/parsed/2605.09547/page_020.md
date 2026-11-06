## 4.5 Implicit Representation of _x_, _s_

The main result of this subsection is the following lemma, which states that we have access to \(x_e^t\) and \(s_e^t\) for any given edge _e_. Note that we do not have an update time for these, as we do not store anything that needs to be updated; these are computed "on the fly."

**Lemma 4.14.** _Given the t_-1_-transcript of the IPM, and an edge e_=(_u,v_) _and its cost c<sub>e</sub>, we can query_ \(s_e^t\) _explicitly in O_(1) _time._

_Proof._ By Definition 4.2 of the _t_-transcript, we have _y_<sup>1</sup>_,...y<sup>t</sup>_ explicitly in memory. The slack is defined as _Ay<sup>t</sup>+s<sup>t</sup>=c_, so for edge _e_=(_u,v_) we have \(s_e^t=c_e-(y_u^t-y_v^t)\) for all _t_=1_,...,t_.

**Lemma 4.15.** _Given the t_-1_-transcript of the IPM, and an edge e_=(_u,v_) _and its cost c<sub>e</sub>, we can query_ \(x_e^t\) _explicitly in_ \(\mathcal{T}(t-1)+\widetilde{O}(1)\) _time._

_Proof._ To find _x<sup>t</sup>_, recall that we store \(\delta_c^1,\delta_c^2,\cdots,\delta_c^t\) and \(\delta_y^1,\delta_y^2,\cdots,\delta_y^t\) Note that

\((\delta_x^t)_e=(\Phi''(x^{t-1})^{-\frac{1}{2}}g_e^t-(\overline{\mathbf{T}^t})^{-1}\Phi''(x^{t-1})^{-1}\mathbf{A}(\delta_y^t+\delta_c^t))_e\)

Using the object \((\delta_x^t)_e\) and given \(x_e^{t-1}\), we can compute \((x^t)_e=x_e^{t-1}+(\delta_x^t)_e\). Thus, we complete the proof.

The above equation requires querying objects \(x_e^{t-1}\), \(g_e^t\), \(\tau^t\). Querying _x_<sup>_t_-1</sup> takes T(_t_-1) time, and by temporarily saving this value we can query both \(g_e^t\) and \(\tau^t\) in \(\widetilde{O}(1)\) time. Thus the total runtime for every edge query is \(\mathcal{T}(t-1)+\widetilde{O}(1)\).

## 4.6 Constructing matrix **H**, dual \(\delta_y^t\) and _y<sup>t</sup>_, and artificial variable \(\delta_c^t\)

We now describe how we can construct the (_t_+1)-transcript when given the _t_-transcript. The following lemma describes all the remaining necessary values.

**Lemma 4.16.** _Given the t-transcript of the IPM (Definition 4.2), then we can compute the following objects w.h.p. in O_(1) _passes (with polynomial time). Part 1._ **H**_<sup>t</sup>, Part 2._ \(\delta_y^t\)_, Part 3._ \(\delta_c^t\)_, Part 4. y<sup>t</sup>, Part 5._ \(\mu^t\)_. These additional values can be stored in_ \(\widetilde{O}(n)\) _additional space._

_Proof._ **Proof of Part 1.** To construct **H**_<sup>t</sup>_. We use Lemma 2.1, which tells us we need one pass over the input. For each edge, we need to find the edge weight \(\phi_e(x_e^{t-1})^{-1}(\tau_e^t)^{-1}\). These are given via Lemma 4.15 and Theorem 4.8. The former requires time T(_t_-1), and the latter \(\widetilde{O}(1)\) if we temporarily save our value of \(x_e^{t-1}\). Thus we can compute this in time _O(m_T(_t_-1)).

**Proof of Part 2.** \(\delta_y^t=(\mathbf{H})^{-1}\mathbf{A}^\top(\Phi''(x^{t-1})^{-\frac{1}{2}})g^t\). For this, first compute \(\mathbf{A}^\top(\Phi''(x)^{-\frac{1}{2}})g\) in one pass and time _O(mT_<sup>_t_-1</sup>). (This again requires us to compute _x<sub>e</sub>_ and _g<sub>e</sub>_ when we receive edge _e_ via Lemma 4.15 and Theorem 4.11.) We then solve the Laplacian system on spectral sparsifier **H**_<sup>t</sup>_ in time _O(m_).

**Proof of Part 3.** We have \(\delta_c=(\mathbf{H})^{-1}(\mathbf{A}^\top x-b)\). For this, we use one pass to compute \(\mathbf{A}^\top x-b\), then solve the Laplacian system on the spectral sparsifier, again using total time \(O(m\mathcal{T}(t-1))\).

**Proof of Part 4.** Compute and store \(y^t=y^{t-1}+\delta_y^t\).

**Proof of Part 5.** By definition from Algorithm 1, \(\mu^t\) is just \(\mu^t=(1-r)\mu^{t-1}\) Therefore, we complete the proof.

## 4.7 Constructing the Next Transcript

We first show the following

**Proposition 4.17.** \(\mathcal{T}(t-1)=T_0+\widetilde{O}(t)\)_, where T_<sub>0</sub> _is the time complexity of querying any_ \(x_e^1\).

_Proof._ We use induction over the number of iterations. Given the first iteration takes time _T_<sub>0</sub>, and Theorem 4.11 and lemma 4.15 tell us \(\mathcal{T}(t)=\mathcal{T}(t-1)+\widetilde{O}(1)\), the conclusion follows.

Then, our algorithm and its correctness follows direction from the above theorems:

