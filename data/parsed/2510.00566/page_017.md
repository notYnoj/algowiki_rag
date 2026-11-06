<tbc>**Lemma A.7** (Gap identity)**.** _For every level m,_<tbc>

\(\|\mathbf{q}-\mathbf{x}\|^2-\mathrm{LB}_\varepsilon^m(\mathbf{q},\mathbf{x})=2C^m(\varepsilon-\rho_m).\)

<tbc>Proof. Direct expansion:

\(\|\mathbf{q}-\mathbf{x}\|^2=R_{T(\mathbf{q})}^{(0,d)}+R_{T(\mathbf{x})}^{(0,d)}-2\sum_{j=1}^dT(\mathbf{q})_jT(\mathbf{x})_j\)<br>
\(=A^m-2\pi_m.\)

Subtracting the relaxed bound,

\(\|\mathbf{q}-\mathbf{x}\|^2-\mathrm{LB}_\varepsilon^m(\mathbf{q},\mathbf{x})=(A^m-2\pi_m)-(A^m-2\varepsilon C^m)\)<br>
\(=2(\varepsilon C^m-\pi_m)\)<br>
\(=2C^m(\varepsilon-\rho_m).\square\)

At \(\varepsilon=1\) and worst case \(\rho_m=-1\) the gap is 4_C<sup>m</sup>_, matching the strict cost bound; at \(\varepsilon=1\) and typical \(\rho_m\approx 0\) the gap is 2_C<sup>m</sup>_, a factor of 2 tighter.

**Assumption A5** (Residual isotropy)**.** For non-near-neighbour pairs (**q**,**x**), the residual coordinates (_T_(**q**)_<sub>j</sub>,T_(**x**)_<sub>j</sub>)<sub>j\>m</sub>_ are independent and uniformly distributed on the sphere in R<sup>_d-m_</sup> (independently for **q** and **x**). Consequently, by standard high-dimensional concentration,

\(\rho_m\sim\mathcal{N}\big(0,\frac{1}{d-m}\big)\text{approximately}.\)

_Remark._ Assumption A5 is realised by the intra-level isotropization step in the main paper’s variance-shaping transform. It applies only to non-near-neighbour pairs; for true _k_-NN pairs the residuals are correlated (the nearness manifests in the residual), so \(\rho_m\) for true neighbours concentrates strictly above 0. The recall loss at \(\varepsilon<1\) arises precisely from neighbour pairs with \(\rho_m>\varepsilon\).

**Lemma A.8** (Pruning depth, \(\varepsilon\)-relaxed)**.** _Under Assumptions A1-A5, for non-near-neighbour candidates and a margin_ \(\Delta>0\)_, the pruning depth at the_ \(\varepsilon\)_-relaxed bound is_<tbc>

\(d^{(\varepsilon)}(\Delta)\approx\frac{d}{\alpha}\mathrm{ln}\frac{2R^2}{\Delta}+\frac{d}{\alpha}\mathrm{ln}\varepsilon.\)

<tbc>Proof. Under A5, \(\rho_m\) concentrates at 0 with deviation \(1/\sqrt{d-m}\). Substituting \(\rho_m\approx 0\) in Lemma A.7,<tbc>

\(\|\mathbf{q}-\mathbf{x}\|^2-\mathrm{LB}_\varepsilon^m(\mathbf{q},\mathbf{x})\approx 2\varepsilon C^m.\)

<tbc>Applying Assumption A1 to both factors of _C<sup>m</sup>_ and Assumption A2,<tbc>

\(2\varepsilon C^m\approx 2\varepsilon\|\mathbf{q}\|\|\mathbf{x}\|e^{-\alpha m/d}\le 2\varepsilon R^2e^{-\alpha m/d}.\)

<tbc>Pruning occurs at the smallest _m_ for which this is at most \(\Delta\):

\(2\varepsilon R^2e^{-\alpha m/d}\le\Delta\Longleftrightarrow m\ge\frac{d}{\alpha}\mathrm{ln}\frac{2\varepsilon R^2}{\Delta}=\frac{d}{\alpha}\mathrm{ln}\frac{2R^2}{\Delta}+\frac{d}{\alpha}\mathrm{ln}\varepsilon.\)

The first term is the typical-case pruning depth at \(\varepsilon=1\), with prefactor 2_R_<sup>2</sup> rather than the strict-mode prefactor _C_<sub>0</sub>=4_R_<sup>2</sup>. The two prefactors differ by a constant inside the log and are absorbed into the same slowly-varying constant as in Proposition 5.1.

**Proposition 5.3** (Cost under \(\varepsilon\)-relaxation)**.** _Under Assumptions A1- A5 and_ \(\varepsilon\in(1/e,1]\)_, the expected refinement cost of Panorama with the_ \(\varepsilon\)_-relaxed bound satisfies_<tbc>

\(\mathbb{E}[\mathrm{Cost}_\varepsilon]\lesssim\frac{Nd\left(c_\mathrm{typ}+\mathrm{ln}\varepsilon\right)}{\alpha},\)

<tbc>_where c_<sub>typ</sub> _is the typical-residual version of the constant C<sub>N</sub> (with prefactor_ 2_R_<sup>2</sup> _instead of the strict worst-case_ 4_R_<sup>2</sup>_). Since the empirical typical-case constant is close to_ 1_, the simplified model is_ \(\mathbb{E}[\mathrm{Cost}_\varepsilon]\lesssim Nd(1+\mathrm{ln}\varepsilon)/\alpha\)_, equivalently_ \(\alpha_\mathrm{eff}(\varepsilon)\approx\alpha/(1+\mathrm{ln}\varepsilon)\)_. For_ \(\varepsilon<1\)_, each candidate is pruned_ \((d/\alpha)\mathrm{ln}(1/\varepsilon)\) _dimensions earlier on average than at_ \(\varepsilon=1\) _until the cap at zero dimensions becomes active._

Proof. The argument mirrors the cost proof, with the pruning depth of Lemma A.4 replaced by Lemma A.8. We work on the same high-probability event \(\mathcal{E}_\delta\) (Lemma A.2); the threshold and margin analysis are unchanged. Substituting the margin asymptotic (7) into Lemma A.8 and aggregating as in Proposition 5.1, the additive \((d/\alpha)\mathrm{ln}\varepsilon\) term carries through the sum to give<tbc>

\(\mathbb{E}[\mathrm{Cost}_\varepsilon]\lesssim\frac{Nd}{\alpha}\left(c_\mathrm{typ}+\mathrm{ln}\varepsilon\right),\)

<tbc>where \(c_\mathrm{typ}=\mathrm{ln}(2R^2/\sigma)-\zeta_N\) is the typical-residual counterpart of _C<sub>N</sub>_, shifted only by ln2 (the typical-case prefactor is 2_R_<sup>2</sup> rather than _C_<sub>0</sub>=4_R_<sup>2</sup>) and inheriting the same log-log behaviour. Since _c_<sub>typ</sub> is observed to be ≈1,

\(\mathbb{E}[\mathrm{Cost}_\varepsilon]\lesssim\frac{Nd\left(1+\mathrm{ln}\varepsilon\right)}{\alpha}.\square\)

_Remark_ (Validity range). The asymptotic requires \(c_\mathrm{typ}+\mathrm{ln}\varepsilon>0\). Setting _c_<sub>typ</sub>=1 gives the conventional threshold \(\varepsilon>1/e\approx 0.37\); the actual threshold is dataset-dependent. Below it, the formula predicts a negative pruning depth--an artifact: the bound clears the margin already at _m_=0, and the cost is governed by other factors (heap warm-up, fixed per-candidate overhead). In this regime \(\varepsilon\) should be tuned empirically.

_Remark_ (Additive vs. multiplicative). The \(\varepsilon\)-relaxation contributes _additively_ to the per-candidate pruning depth, in contrast to the multiplicative \(1/\alpha\) scaling of the base model. A moderate \(\varepsilon=0.7\) shifts the prefactor by ln0.7≈-0.36, enough to produce a noticeable QPS gain without changing the leading \(1/\alpha\) behaviour, while preserving near-perfect recall.

Proposition 5.3 characterises the speed side of the \(\varepsilon\) knob. Pruning at \(\varepsilon<1\) discards true _k_-nearest-neighbour pairs whose residual ratio \(\rho_m\) exceeds \(\varepsilon\). The recall loss thus depends on the dataset- specific distribution of \(\rho_m\) for true _k_-NN pairs, which is measurable per dataset (see the \(\varepsilon\) ablation in the main paper). We do not attempt a closed-form recall bound; the \(\rho_m\) distribution for _k_-NN pairs concentrates strictly above 0 (these pairs are correlated, breaking the isotropy of A5), and recall begins to degrade once \(\varepsilon\) falls below the bulk of this distribution.

