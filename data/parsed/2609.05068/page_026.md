where new variables \(y_{a_p^k}\) are introduced for every commodity \(k\in K\), path \(p\in P^k\) and arc \(a\in p\). Notice that this relaxation is the strongest one among those proposed in \[16\].

**Proposition 4.1.** _DCMCF<sub>env</sub> dominates DCMCF<sub>red</sub>._

_Proof._ Starting from a feasible solution of DCMF<sub>env</sub>, we build a feasible solution of DCMF<sub>red</sub> with the same objective value.<br>
Let then \(\left((\tilde{x}_p^k)_{k\in K,p\in P^k},(\tilde{y}_a)_{a\in A},\tilde{\gamma}\right)\) be a feasible solution of DCMF<sub>env</sub>, and let \(\left((\tilde{x}_p^k)_{k\in K,p\in P^k},(\tilde{z}_p^k)_{k\in K,p\in P^k},(\tilde{y}_a)_{a\in A},(\tilde{y}_{a_p^k})_{k\in K,p\in P^k,a\in p},\tilde{\gamma}\right)\) denote the solution that we aim to construct. We fix the variable values as follows:

\(\tilde{x}_p^k=\tilde{x}_p^k,\tilde{y}_a=\tilde{y}_a,\tilde{z}_p^k=\frac{\tilde{x}_p^k}{u_p^k},\tilde{y}_{a_p^k}=max(\bar{y}_a-(1-\bar{z}_p^k)u_a,\bar{z}_p^kl_a),\tilde{\gamma}=\tilde{\gamma}.\)

All constraints of DCMF<sub>red</sub>, except (29), are straightforwardly satisfied.<br>
As Constraints (18), (19) and (21) are satisfied, we necessarily have:

\(\sum_{a\in p}max(\frac{\bar{z}_p^k}{c_a-l_a},\frac{\bar{z}_p^k^2}{c_a\bar{z}_p^k-\bar{y}_a+(1-\bar{z}_p^k)u_a})-\bar{z}_p^kd^k\le 0\forall k\in K,p\in P^k.\)

If \(\bar{y}_a-(1-\bar{z}_p^k)u_a\ge\bar{z}_p^kl_a\), then \(\bar{y}_{a_p^k}=\bar{y}_a-(1-\bar{z}_p^k)u_a\), and \(max(\frac{\bar{z}_p^k}{c_a-l_a},\frac{\bar{z}_p^k^2}{c_a\bar{z}_p^k-\bar{y}_a+(1-\bar{z}_p^k)u_a})=\frac{\bar{z}_p^k}{c_a\bar{z}_p^k-\bar{y}_{a_p^k}}\). Conversely, if \(\bar{y}_a-(1-\bar{z}_p^k)u_a\le\bar{z}_p^kl_a\), then \(\bar{y}_{a_p^k}=\bar{z}_p^kl_a\), and

\(max(\frac{\bar{z}_p^k}{c_a-l_a},\frac{\bar{z}_p^k^2}{c_a\bar{z}_p^k-y_a+(1-\bar{z}_p^k)u_a})=\frac{\bar{z}_p^k}{c_a-l_a}=\frac{\bar{z}_p^k^2}{c_a\bar{z}_p^k-\bar{y}_{a_p^k}}.\)

This ensures that Constraints (29) are satisfied in both cases, proving the feasibility of the constructed solution of DCMF<sub>red</sub> with \(\tilde{\gamma}=\tilde{\gamma}\).

## 4.3 Additional valid constraints

Two additional sets of valid constraints can be considered in DCMCF relaxations. If variables \(z_p^k\) are considered, then we can obviously write:

\(\sum_{p\in P^k}z_p^k\ge 1\forall k\in K.\) (33)

