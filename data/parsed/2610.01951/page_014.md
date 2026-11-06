**Main notation.**

## A Technical Ingredients from Prior Work

For completeness, we state the results from prior work used in the analysis and clarify the role of each one. The distinction matters because error control at stopping, concentration under adaptive sampling, and sufficient exploration address different parts of the argument.

### Stopping-rule error guarantee.

The bounded-reward result of Jourdan et al. \[9, Lemma 2\], specialized to the Bernoulli transportation cost and threshold (3.1), gives

\(\mathbb{P}_\mu\left(\tau_\delta<\infty,\widehat{i}_{\tau_\delta}\neq i^\star\right)\le\delta\)

for any adaptive sampling rule. This statement controls recommendation error on the joint event that the procedure stops. It does not by itself establish almost-sure termination, an upper bound on the stopping time, or a bound on the conditional error probability given stopping. Section B verifies that our Bernoulli stopping statistic is the specialization covered by this result.

### Time-uniform Bernoulli concentration.

We use the one-dimensional KL confidence-sequence bound of Kaufmann and Koolen \[13, Section 3.3.2, Equation (14)\]. Lemma D.1 applies it to each arm and evaluates it at the adaptive pull counts, yielding the simultaneous event

\(N_{t,i}d(\widehat{\mu}_{t,i},\mu_i)\le c_0\left(log\frac{K}{\eta}+loglog(et)\right)\text{for all}t\ge K\text{and}i\in[K].\)

This concentration statement is the probabilistic starting point for our pairwise-GLR transfer. Entry into the stabilized regime, challenger growth, and stopping are consequences of the subsequent analysis of the algorithm, not of the confidence sequence alone.

### Sufficient exploration for the all-distinct corollary.

Corollary 6.5 uses the sufficient-exploration theorem of Jourdan et al. \[9\] for pairwise-distinct means and for the unguarded tie-breaking convention<tbc>

\begin{tabular}{cc}
H.1 & Algorithms and implementation ..... 39 \\
H.2 & Idealized population-allocation reference ..... 40 \\
H.3 & Supplementary figures ..... 41 \\
\end{tabular}

\begin{tabular}{cc}
Symbol & Meaning \\
_K_ & number of arms, with \(K\ge 2\) \\
\(\mu=(\mu_1,\dots,\mu_K)\) & vector of Bernoulli means \\
_i<sup>⋆</sup>_ & unique best arm \\
\(\delta\) & target error probability \\
\(\beta\) & probability of sampling the leader on non-guard rounds \\
_N<sub>t,i</sub>_ & number of pulls of arm _i_ up to time _t_ \\
\(\widehat{\mu}_{t,i}\) & empirical mean of arm _i_ at time _t_ \\
_B_<sub>_t_+1</sub> & empirical leader at round _t_+1 \\
_C_<sub>_t_+1</sub> & challenger at round _t_+1 \\
_V<sub>t</sub>(i,j_) & symmetric empirical pairwise Bernoulli GLR \\
\(V_t^\mu(i,j)\) & population counterpart of _V<sub>t</sub>(i,j_) \\
_W<sub>t</sub>(i,j_) & one-sided transportation cost used by the algorithm \\
_N_<sub>eff_,t_</sub>(_i,j_) & effective sample size _N<sub>t,i</sub>N<sub>t,j</sub>/(N<sub>t,i</sub>+N<sub>t,j</sub>_) \\
\(\tau_\delta\) & stopping time \\
\(c(t,\delta)\) & stopping threshold \\
\(\alpha_t\) & best-arm sampling fraction _N<sub>t,i<sup>⋆</sup></sub>/t_ \\
_t<sub>U</sub>_ & _U_-stabilization time \\
\(\Gamma_{n,s}^\text{disc}(\mu)\) & discrete penalized allocation benchmark \\
\(T_\alpha^\star(\mu)\) & characteristic time with best-arm fraction fixed to \(\alpha\) \\
\(T^\star(\mu)\) & global characteristic time \(min_{\alpha\in(0,1)}T_\alpha^\star(\mu)\) \\
\end{tabular}

