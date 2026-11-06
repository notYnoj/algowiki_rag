<tbc>Recall that \(\widehat{W}(\unknown)=\prod_{m^\prime\in M}(\widehat{w}_{m^\prime})^{\pi_{m^\prime}}\). Thus, we can factor out the weight \(\widehat{w}_m\) associated with multiedge \(m\in M_v^{(\mathrm{out})}\). Assume the multiedge _m_ comprised of edges from the node _v_ to the nodes _u_<sub>1</sub>_,...,u<sub>k</sub>_. Notice, excluding _m_ from the multipath, we are left with _k_ number of multipaths from the _u<sub>i</sub>_’s:

\(Z_v=\sum_{m\in M_v^{(\mathrm{out})}}\sum_{\unknown\in\mathcal{P}_v\text{starts with}m}\widehat{W}(\unknown)\)<br>
\(=\sum_{m\in M_v^{(\mathrm{out})}}\widehat{w}_m\sum_{\unknown_1\in\mathcal{P}_{u_1}}\sum_{\unknown_2\in\mathcal{P}_{u_2}}\cdots\sum_{\unknown_k\in\mathcal{P}_{u_k}}\prod_{i=1}^k\widehat{W}(\unknown_i).\)

After factoring \(\widehat{w}_m\) out, the sum \(\sum_{\unknown_1\in\mathcal{P}_{u_1}}\sum_{\unknown_2\in\mathcal{P}_{u_2}}\cdots\sum_{\unknown_k\in\mathcal{P}_{u_k}}\) iterates over all combinations of all multipaths sourced from all _u<sub>i</sub>_’s associated with the multiedge _m_. Recall that P_<sub>u<sub>i</sub></sub>_ is the set of all multipaths sourced from _u<sub>i</sub>_ and sinking at T . Since each \(\unknown_i\) iterates<tbc>

T
T
T
1
1
1
1
1
1
1
1
3
3
3
3
5
2
2
2
1
1
1
5
1
1
1
5
1
14
5
1
2
2
10
14
3
3
14
3
14
1
14
1
1
S
S
S

Figure 2: Example of weight pushing for regular DAGs i.e. when |_U_|=1 for all multiedges \((v,U)\in M\). (Left) the unnormalized weights \(\widehat{w}_m\) for all multiedges/edges _m_ in the DAG. (Middle) the normalizations _Z<sub>v</sub>_ for all vertices \(v\in V\) using the Steps 1 and 2 of the weight pushing algorithm. (Right) the new weights \(w_m^\mathrm{new}\) which are in Stochastic Product Form using the Step 3 of the weight pushing algorithm.

