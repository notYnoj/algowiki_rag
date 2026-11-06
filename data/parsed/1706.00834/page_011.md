<tbc>over all multipaths in P_<sub>u<sub>i</sub></sub>_, we can turn the sum of products into product of sums as below:

\(Z_v=\sum_{m\in M_v^{(\mathrm{out})}}\widehat{w}_m\sum_{\unknown_1\in\mathcal{P}_{u_1}}\sum_{\unknown_2\in\mathcal{P}_{u_2}}\cdots\sum_{\unknown_k\in\mathcal{P}_{u_k}}\prod_{i=1}^k\widehat{W}(\unknown_i)\)<br>
\(=\sum_{m\in M_v^{(\mathrm{out})}}\widehat{w}_m\sum_{\unknown_1\in\mathcal{P}_{u_1}}\widehat{W}(\unknown_1)\underbrace{\sum_{\unknown_2\in\mathcal{P}_{u_2}}\cdots\sum_{\unknown_k\in\mathcal{P}_{u_k}}\prod_{i=2}^k\widehat{W}(\unknown_i))}_\text{does not depend on}\unknown_1\in\mathcal{P}_{u_1}\)<br>
\(=\sum_{m\in M_v^{(\mathrm{out})}}\widehat{w}_m\left(\sum_{\unknown_2\in\mathcal{P}_{u_2}}\cdots\sum_{\unknown_k\in\mathcal{P}_{u_k}}\prod_{i=2}^k\widehat{W}(\unknown_i)\right)\left(\sum_{\unknown_1\in\mathcal{P}_{u_1}}\widehat{W}(\unknown_1)\right)\)<br>
\(=\cdots\text{(Repeating for each sum}\sum_{\unknown_j\in\mathcal{P}_{u_j}})\)<br>
\(=\sum_{m\in M_v^{(\mathrm{out})}}\widehat{w}_m\prod_{i=1}^k\left(\underbrace{\sum_{\unknown\in\mathcal{P}_{u_i}}\widehat{W}(\unknown)}_{Z_{u_i}}\right)\)<br>
\(=\sum_{m\in M_v^{(\mathrm{out})}}\widehat{w}_m\prod_{i=1}^kZ_{u_i}.\) (4)

Equation (4) justifies Step 2. Now we prove that the new weight assignment in Step 3 will result in a distribution in Stochastic Product Form with correct expectation. For all \(v\in V-\mathcal{T}\) and for all \(m\in M_v^{(\mathrm{out})}\), set \(w_m^\mathrm{new}:=\widehat{w}_m\frac{\prod_{u:(v,u)\in m}Z_u}{Z_v}\) (Step 3). Property (2) of Definition 8 (i.e. stochasticity) is true since for all \(v\in V-\mathcal{T}\) :

\(\sum_{m\in M_v^{(\mathrm{out})}}w_m^\mathrm{new}=\sum_{m\in M_v^{(\mathrm{out})}}\widehat{w}_m\frac{\prod_{u:(v,u)\in m}Z_u}{Z_v}\)<br>
\(=\frac{1}{Z_v}\underbrace{\sum_{m\in M_v^{(\mathrm{out})}}\widehat{w}_m\prod_{u:(v,u)\in m}Z_u}_{Z_v}=1.\) (Equation (4))

