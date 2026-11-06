<tbc>decision. Their agreement rate is

\(\alpha=\frac{1}{n_\mathrm{cal}}\sum_{(i,j)\in\mathcal{C}_0}\mathbf{1}[\tilde{y}_{ij}=y_{ij}].\) (1)

This step serves two purposes: it estimates whether the VLM-derived ordering is trustworthy enough to support MergeSort, and it initializes Elo ratings from reliable human comparisons before any inference is attempted.

_Pointwise VLM pre-scoring._ For each item _x<sub>i</sub>_, the VLM is queried _K_ times with prompt perturbations or simulated annotator diversity, producing pointwise scores \(\{v_i^{(k)}\}_{k=1}^K\). We define the mean pre-score as

\(\bar{v}_i=\frac{1}{K}\sum_{k=1}^Kv_i^{(k)}.\) (2)

The initial order \(\pi_0\) is obtained by sorting items according to \(\bar{v}_i\) from worst to best.

_Agreement-aware Elo warm start._ The code applies an agreement-conditioned warm start rather than directly trusting the VLM scores. Let

\(z_i=2\left(\frac{\bar{v}_i-v_\mathrm{min}}{v_\mathrm{max}-v_\mathrm{min}+\varepsilon}-\frac{1}{2}\right),c_i=\frac{|\bar{v}_i-\mathrm{median}(\bar{v})|}{v_\mathrm{max}-v_\mathrm{min}+\varepsilon},\) (3)

where \(z_i\in[-1,1]\) is the centered normalized pre-score and _c<sub>i</sub>_ measures how far item _i_ lies from the ambiguous center of the score distribution. Because all three trusted cases share the same value, the warm start reduces to a single _banded_ gate: an item inherits VLM structure only if its centeredness _c<sub>i</sub>_ clears an agreement-dependent threshold \(\tau(\alpha)\),

\(R_i^{(0)}=1500+250z_i\cdot\mathbf{1}[c_i\ge\tau(\alpha)],\tau(\alpha)=\left\{\begin{array}{ c c }
0, & \alpha\ge 0.70, \\
0.3, & 0.60\le\alpha<0.70, \\
0.5, & \alpha<0.60.
\end{array}\right.\) (4)

The band widens (higher \(\tau\)) as agreement drops, so when the VLM is less trustworthy only items far from the ambiguous center--where even a noisy prior is likely directionally correct--inherit a non-neutral rating; everyone else starts at 1500. The final Round-0 Elo state is then blended with the ratings accumulated from calibration comparisons:

\(R_i\leftarrow 0.5R_i+0.5R_i^{(0)}.\) (5)

This conservative blending limits anchoring by imperfect VLM priors while still injecting useful global structure.

