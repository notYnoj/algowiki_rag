## H.1 Algorithms and implementation

All variants use the same GLR stopping rule, the threshold \(c(t,\delta)=log(1/\delta)+2log(1+t/2)+2+log(K-1)\), and smallest-index deterministic tie-breaking. We compare three sampling variants:

• **Unguarded penalized**: the original rule, with challenger \(C_{t+1}\in argmin_{j\neq B_{t+1}}\{W_t(B_{t+1},j)+logN_{t,j}\}\).<tbc>

• **Guarded penalized**: the same rule, except that if \(min_iN_{t,i}<\sqrt{t/K}\), the algorithm pulls a least-sampled arm.<tbc>

• **Unpenalized ablation**: the challenger minimizes _W<sub>t</sub>(B_<sub>_t_+1</sub>_,j_) instead of _W<sub>t</sub>(B_<sub>_t_+1</sub>_,j_)+log_N<sub>t,j</sub>_; the stopping rule, threshold, initialization, and tie-breaking are unchanged.

The implementation evaluates the Bernoulli two-sample GLR at the pooled mean, uses numba- accelerated simulation kernels, and records every run in a raw CSV with the stopping time, final recommendation, cap indicator, guard count, final arm counts, and optimal population weights.

### Computing the population benchmark and finite-confidence predictor

For each instance and each \(\beta\), we compute \(T_\beta^\star(\mu)\) from the Bernoulli equalization system. For fixed \(\alpha\in(0,1)\) and challenger \(j\neq i^\star\), define<tbc>

\(I_j^\alpha(w)=inf_{x\in(0,1)}\{\alpha d(\mu_{i^\star},x)+wd(\mu_j,x)\},w>0.\)

<tbc>The optimizer is characterized by a scalar \(\lambda_\alpha\) such that<tbc>

\(I_j^\alpha(w_j^\alpha)=\lambda_\alpha\forall j\neq i^\star,\sum_{j\neq i^\star} w_j^\alpha=1-\alpha,\)

<tbc>and \(T_\alpha^\star(\mu)=1/\lambda_\alpha\). Numerically, we solve this by bisection on \(\lambda_\alpha\) and, inside each step, by bisection on the strictly increasing inverse maps \((I_j^\alpha)^{-1}\). This avoids a generic constrained optimizer and is stable on the equal-close instances. The plotted predictor keeps the exact finite-confidence threshold:

\(t_\text{pred}(\mu,\beta,\delta)=min\{t\ge K:t/T_\beta^\star(\mu)>c(t,\delta)\}.\)

### Experiment grids and replication counts

The full run contains 23,050 independent simulation runs.  1 lists the grids used in the paper.

The main evaluation instances are

\(\text{SEP5}=[0.70,0.50,0.40,0.30,0.20],\text{CLUSTER-CLOSE5}=[0.70,0.64,0.63,0.62,0.61],\)<br>
\(\text{TIE-CLOSE4}=[0.60,0.56,0.56,0.56].\)

The \(\beta\)-sweep uses CLUSTER-CLOSE5 and TIE-CLOSE4, \(\beta\in\{0.2,0.3,\dots,0.8\}\), \(\delta=10^{-6}\), and the guarded penalized variant. The guard-overhead family uses \[0.60,0.56_,...,_0.56\] with \(K\in\{4,8,12,16\}\), \(\beta=0.5\), and \(\delta=10^{-6}\). The stress experiments use TIE-CLOSE4, \(\beta=0.5\), and \(\delta=10^{-8}\).

### Randomness, caps, and uncertainty summaries

The seed policy is deterministic: consecutive integer seeds are assigned in experiment-specification order, starting at 20260424. All runs use a fail-safe cap of 700,000 rounds. A cap hit is recorded as \(\tau_\delta=700,000\); no penalized evaluation run<tbc>

\begin{tabular}{ccc}
Experiment & Grid & Runs \\
Main evaluation & 3 instances \(\times\) 3 values of \(\beta\times 5\) values of \(\delta\times 2\) variants \(\times 200\) reps & 18,000 \\
\(\beta\)-sweep & 2 instances \(\times\) 7 values of \(\beta\times 200\) reps & 2,800 \\
Stress survival & 2 penalized variants \(\times 600\) reps & 1,200 \\
Penalty ablation & 1 unpenalized variant \(\times 500\) reps & 500 \\
Guard overhead & \(K\in\{4,8,12,16\}\) with reps 200,200,100,50 & 550 \\
\end{tabular}

1: Experiment grids. The three main evaluation instances are SEP5, CLUSTER-CLOSE5, and TIE-CLOSE4. The evaluation confidence levels are 10<sup>-4</sup>,10<sup>-5</sup>,10<sup>-6</sup>,10<sup>-7</sup>,10<sup>-8</sup>.

