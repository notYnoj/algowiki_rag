**Lemma A.2** (High-probability bound on the sampled threshold via DKW)**.** _Let the squared distances be i.i.d. with CDF F. For any_ \(\epsilon\in(0,1)\)_, with probability at least_ \(1-2e^{-2i\epsilon^2}\) _(Dvoretzky-Kiefer- Wolfowitz [39]), the k_th _order statistic_ \(\tau_i\) _satisfies_

\(F^{-1}\big(max\big\{0,\frac{k}{i+1}-\epsilon\big\}\big)\le\tau_i\le F^{-1}\big(min\big\{1,\frac{k}{i+1}+\epsilon\big\}\big).\)

_Under the Gaussian assumption A3 (_\(F(r)=\Phi((r-\mu)/\sigma)\)_), this gives in particular_

\(\tau_i\le\mu+\sigma\Phi^{-1}\big(\frac{k}{i+1}+\epsilon\big)\text{\textit{with probability at least}}1-2e^{-2i\epsilon^2}.\)

Proof. Let _F<sub>i</sub>_ be the empirical CDF of the first _i_ distances. The DKW inequality gives \(Pr(sup_t|F_i(t)-F(t)|>\epsilon)\le 2e^{-2i\epsilon^2}\). On the event sup_<sub>t</sub>_ \(|F_i-F|\le\epsilon\) we have \(F(t)-\epsilon\le F_i(t)\le F(t)+\epsilon\) for all _t_; monotonicity of _F_<sup>-1</sup> then gives \(F^{-1}(u-\epsilon)\le F_i^{-1}(u)\le F^{-1}(u+\epsilon)\) for all \(u\in(0,1)\). Taking _u=k/(i_+1) and recalling \(\tau_i=F_i^{-1}(k/(i+1))\) yields the two-sided bound. Under A3, \(F^{-1}(p)=\mu+\sigma\Phi^{-1}(p)\), which gives the Gaussian form. \(\square\)

A new candidate is tested against \(\tau_i\); in the Gaussian model, a representative non-near-neighbour candidate has squared distance near the mean \(\mu\). This lets us define a model margin.

**Definition A.3** (Model margin \(\Delta_i\))**.** Fix \(\epsilon_i\in(0,1)\) and set the sampled _k_th-NN threshold upper bound

\(K_i:=\mu+\sigma\Phi^{-1}\big(\frac{k}{i+1}+\epsilon_i\big),\Delta_i:=\mu-K_i=-\sigma\Phi^{-1}\big(\frac{k}{i+1}+\epsilon_i\big).\)

On the DKW event of Lemma A.2, the model threshold is at most _K<sub>i</sub>_. Thus a representative non-near-neighbour candidate at squared distance \(\mu\) has model margin at least \(\Delta_i\). We use \(\Delta_i\) as the per-step representative margin in the cost model; candidate-level fluctuations are absorbed into the averaged constant _C<sub>N</sub>_ below. The margin is positive whenever \(\frac{k}{i+1}+\epsilon_i<\frac{1}{2}\) (so \(\Phi^{-1}(\cdot)<0\)).

_Uniform high-probability schedule._ Fix a target failure probability \(\delta\in(0,1)\) and set<tbc>

\(\epsilon_i:=\sqrt{\frac{1}{2i}ln\frac{2N}{\delta}}.\)

<tbc>By a union bound over \(i\in\{k+1,\dots,N\}\), the event

\(\mathcal{E}_\delta:=\cap_{i=k+1}^N\big\{\tau_i\le\mu+\sigma\Phi^{-1}\big(\frac{k}{i+1}+\epsilon_i\big)\big\}\)

holds with probability at least \(1-\delta\). All bounds below are stated on \(\mathcal{E}_\delta\).

A candidate **x**_<sub>j</sub>_ is pruned at level _m_ once its lower bound exceeds the threshold. A sufficient condition is that the worst-case lower- bound error falls below the margin of the candidate processed at step _i_:<tbc>

\(\|\mathbf{q}-\mathbf{x}_j\|^2-\mathrm{LB}^m(\mathbf{q},\mathbf{x}_j)<\Delta_i.\)

<tbc>By Cauchy-Schwarz the left-hand side is at most four times the geometric mean of the tail energies; applying Assumptions A1 and A2,<tbc>

\(4\sqrt{R_{T(\mathbf{q})}^{(m,d)}R_{T(\mathbf{x}_j)}^{(m,d)}}\le 4\sqrt{\|\mathbf{q}\|^2\|\mathbf{x}_j\|^2e^{-2\alpha m/d}}\le C_0e^{-\alpha m/d},C_0:=4R^2.\)

<tbc>Pruning is therefore guaranteed once \(C_0e^{-\alpha m/d}<\Delta_i\), i.e.<tbc>

\(e^{-\alpha m/d}<\frac{\Delta_i}{C_0}\Longleftrightarrow m>\frac{d}{\alpha}ln\frac{C_0}{\Delta_i}.\)

<tbc>**Lemma A.4** (Model pruning depth)**.** _The modelled number of dimensions_ \(\rho_i\) _processed for the candidate at step i is_<tbc>

\(\rho_i\approx min\big\{d,\frac{d}{\alpha}\big[ln\frac{C_0}{\Delta_i}\big]_+\big\},C_0=4R^2,[x]_+:=max\{0,x\}.\)

<tbc>The total cost is dominated by the sum of the pruning dimensions over the _N_ candidates. Writing \(i_0:=min\{i\ge k+1:\frac{k}{i+1}+\epsilon_i<\frac{1}{2}\}\) for the first index at which the model margin becomes positive,<tbc>

\(\mathrm{Cost}=\sum_{i=k+1}^N\rho_i\approx\sum_{i=max\{i_0,k+1\}}^N\frac{d}{\alpha}min\big\{\alpha,\big[ln\frac{C_0}{\Delta_i}\big]_+\big\}.\)

<tbc>Let \(I_{C_0}:=\{i\in\{max\{i_0,k+1\},\dots,N\}:\Delta_i\le C_0\}\) and _N_<sub>_C_<sub>0</sub></sub>:=max_I_<sub>_C_<sub>0</sub></sub>. Then<tbc>

\(\sum_i\big[ln\frac{C_0}{\Delta_i}\big]_+=\sum_{i\in I_{C_0}}(lnC_0-ln\Delta_i)=|I_{C_0}|lnC_0-ln\big(\prod_{i\in I_{C_0}}\Delta_i\big).\)

<tbc>Equivalently, define the finite-sample model constant

\(C_N:=\frac{1}{N}\sum_{i=max\{i_0,k+1\}}^Nmin\big\{\alpha,\big[ln\frac{C_0}{\Delta_i}\big]_+\big\}.\) (6)

This is the average capped log-margin cost per candidate.

**Lemma A.5** (Model cost via averaged margins)**.** _The total computational cost is modelled by_<tbc>

\(\mathrm{Cost}\approx\frac{C_N}{\alpha}Nd.\)

<tbc>_When the cap at d is inactive on the contributing window, this is equivalently_<tbc>

\(C_N\approx\frac{1}{N}\big(|I_{C_0}|lnC_0-ln\prod_{i\in I_{C_0}}\Delta_i\big).\)

<tbc>The exact finite-sample constant is the average in Lemma A.5. To see its dependence on the Gaussian model parameters, write \(p_i:=k/(i+1)+\epsilon_i\). When _p<sub>i</sub>_ lies in the lower tail, the usual Gaussian- quantile approximation gives

\(\Delta_i=-\sigma\Phi^{-1}(p_i)\approx\sigma\sqrt{2ln(1/p_i)}.\) (7)

Substituting (7) into the average shows that the constant has the representative form<tbc>

\(C_N\approx\frac{|I_{C_0}|}{N}ln\frac{C_0}{\sigma}-\zeta_N\text{(with the cap at}\alpha\text{applied candidate-wise),}\)

<tbc>where

\(\zeta_N:=\frac{1}{2N}\sum_{i\in I_{C_0}}ln\big(2ln(1/p_i)\big).\)

The term \(\zeta_N\) varies only through a log-log dependence on the effective tail probabilities. In finite samples we keep _C<sub>N</sub>_ as the empirical/model constant rather than treating the endpoint approximation for \(\zeta_N\) as an exact asymptotic identity.

Using Lemma A.5:

**Corollary A.6** (Finite-sample cost form)**.** _On_ \(\mathcal{E}_\delta\)_, the modelled cost to process the candidate set is_<tbc>

\(\mathrm{Cost}\lesssim\frac{C_N}{\alpha}Nd,C_N\approx\frac{|I_{C_0}|}{N}ln\frac{C_0}{\sigma}-\zeta_N.\)

