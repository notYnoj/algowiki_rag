The algorithm uses the following one-sided version, traditionally called the transportation cost:

\(W_t(i,j):=\left\{\begin{array}{ c c }
V_t(i,j), & \widehat{\mu}_{t,i}\ge\widehat{\mu}_{t,j}, \\
0, & \widehat{\mu}_{t,i}<\widehat{\mu}_{t,j}.
\end{array}\right.\)

Thus evidence is counted only when the first arm has at least as large an empirical mean as the second. This is the ordered transportation cost of Jourdan et al. \[9\]. In particular, if _i_ is the empirical leader and \(j\neq i\), then _W<sub>t</sub>(i,j_)=_V<sub>t</sub>(i,j_).

For Bernoulli KL, the minimizing common mean is the sample-size-weighted pooled mean \(x_t(i,j)=\frac{N_{t,i}\widehat{\mu}_{t,i}+N_{t,j}\widehat{\mu}_{t,j}}{N_{t,i}+N_{t,j}}\) , with the same formula for \(V_t^\mu(i,j)\) after replacing empirical means by population means.

After _t_ pulls, the algorithm first identifies the empirical leader \(B_{t+1}\in argmax_{i\in[K]}\widehat{\mu}_{t,i}\) and sets the current recommendation to \(\widehat{i}_t:=B_{t+1}\). If the stopping condition is not met and no guard is active, it then chooses \(C_{t+1}\in argmin_{j\neq B_{t+1}}\left\{W_t(B_{t+1},j)+logN_{t,j}\right\},\) again with the same fixed tie-breaking rule, and pulls the leader with probability \(\beta\in(0,1)\) and the challenger with probability \(1-\beta\). Before the empirical leader is permanently correct, \(\beta\) is literally the leader-selection probability; after stabilization, it controls the sampling fraction of the true best arm.

We also study an optional _exploration guard_. It is activated whenever \(min_{i\in[K]}N_{t,i}<\sqrt{t/K}\) and then pulls a least-sampled arm instead of using the top-two decision. The leader _B_<sub>_t_+1</sub> is still defined on guarded rounds, whereas the challenger _C_<sub>_t_+1</sub> is used only on unguarded rounds. Let \(G_t^\text{tot}\) denote the number of guarded pulls made by time _t_. Throughout the paper, the _unguarded algorithm_ means the original \(\beta\)-EB-TCI rule without this modification. We use the time-dependent GLR stopping threshold of Jourdan et al. \[9\],

\(c(t,\delta)=log(1/\delta)+2log(1+t/2)+2+log(K-1).\) (3.1)

The stopping time and terminal recommendation are

\(\tau_\delta:=inf\left\{t\ge K:min_{j\neq B_{t+1}}W_t(B_{t+1},j)>c(t,\delta)\right\},\widehat{i}_{\tau_\delta}:=B_{\tau_\delta+1}.\) (3.2)

The martingale analysis of Jourdan et al. \[9\] gives the following error guarantee for this stopping rule on bounded rewards:

\(\mathbb{P}_\mu\big(\tau_\delta<\infty,\widehat{i}_{\tau_\delta}\neq i^\star\big)\le\delta\)

for any adaptive sampling rule. This statement controls the chance of a wrong recommendation on runs that stop; it does not prove that the stopping time is finite. Almost-sure termination is established separately by the stopping-time results in Sections 5-6. Combining termination with the display above gives \(\delta\)-correctness in each regime covered by our theorems. Appendix B gives the formal reduction.

**Algorithm 1** \(\beta\)-EB-TCI with GLR stopping and optional exploration guard

1: Pull each arm once.

2: **for** _t=K,K_+1_,..._ **do**

3: \(B_{t+1}\in argmax_{i\in[K]}\widehat{\mu}_{t,i}\) _fixed deterministic tie-breaking_

4: \(\widehat{i}_t\leftarrow B_{t+1}\)

5: **if** \(min_{j\neq B_{t+1}}W_t(B_{t+1},j)>c(t,\delta)\) **then**

6: stop and recommend \(\widehat{i}_t\)

7: **end if**

8: **if** the guard is enabled and \(min_{i\in[K]}N_{t,i}<\sqrt{t/K}\) **then**

9: \(I_{t+1}\in argmin_{i\in[K]}N_{t,i}\) _guarded pull_

10: **else**

11: \(C_{t+1}\in argmin_{j\neq B_{t+1}}\left\{W_t(B_{t+1},j)+logN_{t,j}\right\}\)

12: Draw \(U_{t+1}\sim Ber(\beta)\) independently of the past.

13: \(I_{t+1}\leftarrow B_{t+1}\) if _U_<sub>_t_+1</sub>=1, and \(I_{t+1}\leftarrow C_{t+1}\) otherwise.

14: **end if**

15: **end for**

