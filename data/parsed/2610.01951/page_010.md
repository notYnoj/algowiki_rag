### Takeaway.

On the tested Bernoulli instances, the observed mean stopping times closely follow the predictor that combines \(T_\beta^\star(\mu)\) with the actual stopping threshold. The guard adds very few pulls, whereas removing the logarithmic penalty substantially worsens the equal-mean stress test. These experiments support the mechanisms analyzed here; they do not establish uniform superiority over other best-arm identification algorithms.

## 8 Conclusion

We analyzed the exact logarithmically penalized challenger in Bernoulli \(\beta\)-EB-TCI at finite confidence. In the stabilized regime, every suboptimal-arm pull count grows linearly and the stopping-time upper bound has the exact fixed-\(\beta\) leading term \(T_\beta^\star(\mu)log(1/\delta)\); lower-order constants are not optimized.

The deterministic unguarded rule has a non-asymptotic high-probability stopping bound, while its expected bound additionally requires finite-mean sufficient exploration. For pairwise-distinct means, Jourdan et al. [9] supply this property only for their tie-breaking variant. The guard supplies it for arbitrary _K_ with only \(O(\sqrt{Kt})\) guarded pulls by time _t_. The proof is Bernoulli-specific with fixed \(\beta\); extensions beyond Bernoulli rewards, online \(\beta\) adaptation, and finite-mean stabilization with tied suboptimal means remain open.

Finite-confidence calibration of the stopping time
Separated instance: sep5
Equal-close tie class: tie-close4
2300
unguarded
2200
guarded
105000
guarded
tpred
tpred
2100
100000
Stopping time
Stopping time
2000
95000
1900
90000
1800
1700
85000
1600
80000
1500
10
12
14
16
18
10
12
14
16
18
Confidence scale log(1/6)
Confidence scale log(1/6)

