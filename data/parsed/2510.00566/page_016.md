<tbc>The preceding display should be read as a finite-sample cost model. For a concrete run, the empirical counterpart is<tbc>

\(\widehat{C}_N:=\alpha\frac{\mathrm{Cost}}{Nd},\)

<tbc>the measured constant multiplying \(1/\alpha\) in the dimensions-scanned fraction. The Gaussian order-statistic model predicts this constant through the average log margin _C<sub>N</sub>_ above. Since the per-candidate work is at most _d_, the contribution of any failure of \(\mathcal{E}_\delta\) is bounded by \(\delta Nd\) in expectation:

\(\mathbb{E}[\mathrm{Cost}]\lesssim\mathbb{E}[\mathrm{Cost}|\mathcal{E}_\delta]+\delta Nd,\)

so the same \(C_N/\alpha\) scaling is unaffected by choosing \(\delta\) small.

_Comparison to the naive cost._ The naive, brute-force method computes _N_ full _d_-dimensional distances, at cost _Nd_. The bound above is smaller by a factor that scales as \(\alpha\) (up to the slowly-varying and logarithmic terms), on the same high-probability event \(\mathcal{E}_\delta\).

_On the role of_ \(\alpha\). The parameter \(\alpha\) controls the decay \(e^{-\alpha m/d}\). If \(\alpha\le 1\), energy decays too slowly (at _m=d/_2 the remaining energy is at least _e_<sup>-1/2</sup>), leading to weak bounds and limited pruning; effective compaction corresponds to \(\alpha\) comfortably greater than 1. The high-probability analysis only replaces the expected-margin terms by their concentrated counterparts and leaves this qualitative conclusion unchanged.

**Proposition 5.1** (Expected refinement cost)**.** _Let_ \(\phi:=\mathbb{E}[\mathrm{Cost}]/(Nd)\) _be the average fraction of dimensions processed per candidate. Under Assumptions A1-A4,_

\(\mathbb{E}[\mathrm{Cost}]\lesssim\frac{C_N}{\alpha}Nd,\phi\lesssim\frac{C_N}{\alpha},\)

_where C<sub>N</sub> is the finite-sample constant defined in_ (6)_. Equivalently, Panorama evaluates only a fraction_ \(C_N/\alpha\) _of the Nd coordinates a brute-force scan would touch--a speedup of_ \(\alpha/C_N\) _over brute force._

Proof. Combining the pruning-depth model with the definition of _C<sub>N</sub>_,<tbc>

\(\phi=\frac{\mathbb{E}[\mathrm{Cost}]}{Nd}\approx\frac{1}{\alpha N}\sum_{i=\mathrm{max}\{i_0,k+1\}}^N\mathrm{min}\left\{\alpha,\left[\mathrm{ln}\frac{C_0}{\Delta_i}\right]_+\right\}=:\frac{C_N}{\alpha}.\)

<tbc>Under the Gaussian margin approximation, this is

\(C_N\approx\frac{|I_{C_0}|}{N}\mathrm{ln}\frac{C_0}{\sigma}-\zeta_N,\)

where \(\zeta_N\) is the averaged log-log term above. Thus the dependence on _N_ enters through the averaged log-log term. In practice the measured dimensions-scanned fraction reflects the effective constant for the candidate stream; across the datasets in the main paper that constant is order-one and close to 1. \(\square\)

## A.4 Proposition 5.2: Out-of-distribution cost

In deployment the query **q** and the database vectors {**x**_<sub>i</sub>_} may compact differently under the PCA transform _T_--the query might come from a different language, sensor, or be adversarial. Let \(\alpha_q\) and \(\alpha_x\) denote their decay rates:<tbc>

\(R_{T(\mathbf{q})}^{(m,d)}\approx\|\mathbf{q}\|^2e^{-\alpha_qm/d},R_{T(\mathbf{x}_i)}^{(m,d)}\approx\|\mathbf{x}_i\|^2e^{-\alpha_xm/d}.\) (8)

<tbc>**Proposition 5.2** (Out-of-distribution cost)**.** _With asymmetric compaction rates, the effective decay rate of the lower-bound error is the_ arithmetic mean \(\alpha_\mathrm{eff}=(\alpha_q+\alpha_x)/2\)_, and the expected cost satisfies_

\(\mathbb{E}[\mathrm{Cost}]\lesssim\frac{C_NNd}{\alpha_\mathrm{eff}}=\frac{2C_NNd}{\alpha_q+\alpha_x},\)

_in the same model sense as Proposition 5.1. If the OOD shift changes only the tail compaction rates, the same slowly varying margin constant C<sub>N</sub> applies; if it also changes the distance distribution, the bound holds with a modified margin constant_ \(C'_N\) _reflecting that distribution._

Proof. Only the per-candidate depth changes; the threshold, margin, and aggregation arguments are unchanged. The Cauchy- Schwarz remainder obeys, after substituting the asymmetric tails (8) and bounding norms by Assumption A2,

\(4\sqrt{R_{T(\mathbf{q})}^{(m,d)}}R_{T(\mathbf{x}_j)}^{(m,d)}}\)<br>
\(\le 4R^2\sqrt{e^{-\alpha_qm/d}}e^{-\alpha_xm/d}\)<br>
\(=4R^2e^{-(\alpha_q+\alpha_x)m/(2d)}\)<br>
\(=C_0e^{-\alpha_\mathrm{eff}m/d},\)

with \(\alpha_\mathrm{eff}=(\alpha_q+\alpha_x)/2\). Solving \(C_0e^{-\alpha_\mathrm{eff}m/d}<\Delta_i\) gives the capped per-candidate depth \(\rho_i\approx\mathrm{min}\{d,(d/\alpha_\mathrm{eff})[\mathrm{ln}(C_0/\Delta_i)]_+\}\). The threshold, margin, and aggregation arguments above are unchanged with \(\alpha\) replaced by \(\alpha_\mathrm{eff}\), yielding the stated cost. \(\square\)

_Remark_ (Graceful degradation). Even a fully out-of-distribution query with no compaction (\(\alpha_q\rightarrow 0\)) leaves \(\mathbb{E}[\mathrm{Cost}]\lesssim 2C_NNd/\alpha_x\): Panorama still benefits from the database compaction alone, a speedup of roughly \(\alpha_x/(2C_N)\) over brute force when the margin constant is unchanged. Performance degrades gracefully rather than collapsing, as long as the database vectors are well-compacted.

## A.5 Proposition 5.3: The \(\varepsilon\)-relaxation

Setting \(\varepsilon=1\) uses the exact Cauchy-Schwarz correction 2_C<sup>m</sup>_ and preserves recall. That worst-case correction is attained only at the adversarial residual alignment \(\rho_m=-1\); on real, isotropised residuals the typical alignment is \(\rho_m\approx 0\), where the correction is already a factor of two smaller. The \(\varepsilon\)-relaxation exploits this gap: it discounts the correction by a factor \(\varepsilon\in(0,1]\), pruning earlier at a controlled, quantifiable cost in recall. We first record the exact gap identity, then state the isotropy assumption that makes the typical case precise, and finally turn it into a cost bound that mirrors Proposition 5.1.

The \(\varepsilon\)-relaxed bound is<tbc>

\(\mathrm{LB}_\varepsilon^m(\mathbf{q},\mathbf{x})=A^m-2\varepsilon C^m,C^m:=\sqrt{R_{T(\mathbf{q})}^{(m,d)}}R_{T(\mathbf{x})}^{(m,d)},\)

<tbc>where \(A^m=R_{T(\mathbf{q})}^{(0,d)}+R_{T(\mathbf{x})}^{(0,d)}-2p^{(0,m)}(\mathbf{q},\mathbf{x})\). Define the residual inner product<tbc>

\(\pi_m=\sum_{j>m}T(\mathbf{q})_jT(\mathbf{x})_j\)

<tbc>and its normalised value<tbc>

\(\rho_m:=\frac{\pi_m}{C^m}\in[-1,1],\)

<tbc>where the bounds follow from Cauchy-Schwarz applied to the residual.

