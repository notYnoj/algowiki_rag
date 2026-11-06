<tbc>_PCS._ Figure 4 shows the PCS of each benchmark relative to TEAk for all configurations. TEAk generally has the highest PCS, and when it does not, it is within a few percent of the best. TEAk’s biggest advantage over the benchmarks is on larger problems (_I_=100) and larger _k_. To show more clearly how TEAk improves over the best benchmarks and how it compares with TEAk-_q_<sup>†</sup>(_t_), Figure 5 takes the four best-performing benchmarks, together with TEAk-_q_<sup>†</sup>(_t_), and plots the distribution over all configurations of their PCS relative to TEAk. Each benchmark falls short of TEAk by 5% or more in some configurations, while none beats it by more than 0.2% in any configuration. In addition, TEAk outperforms TEAk-_q_<sup>†</sup>(_t_) in 36 of the 48 configurations, and in every configuration the PCS of TEAk-_q_<sup>†</sup>(_t_) is between 0.8% below and 0.3% above that of TEAk.

_EOC over the whole budget._ Figure 6 plots EOC on a log scale against cumulative samples spent for the Gaussian family and each (_I,k_) pair. At _k_=1, the most competitive benchmarks are the TTTS variants, and for general _k_ the most competitive are gap-e, KL-LUCB, and the top-_k_ Thompson sampling methods. Which benchmark is best (or near-best) varies across configurations and varies with the budget within a configuration. TEAk is the exception: in every configuration, its EOC is the lowest, or close to it, across all budgets. The plots for the other three sampling families show a similar picture.

## 5.3. Batching

We now investigate TEAk’s performance in the batched setting, one of its main motivations. We compare against BatchSAR (Jun et al. 2016), a version of the successive accepts and rejects algorithm of Bubeck

TEAk TS-PPS-IDS KL-LUCB EMIp gap-e TTTS-IDS BOLD TEAk-q*(t) TS-KKT(.5)-IDS AOAm EOC-m Uniform TTTS AOAP EOC (log scale) k=1 k=3 k=5 k=10 10-2 10-3 k=1 k=5 k=10 k=20 10-2 10-3 k=1 k=5 k=10 k=20 10-2 100, budget 100k 10-3 0
25 50 75 0
25 50 75 0
25 50 75 0
25 50 75 % of max budget

**Figure 6** Gaussian: EOC (log scale) against budget (max budget = 1,000\(\cdot\)_I_). Rows vary the problem size _I_ and columns vary _k_.

