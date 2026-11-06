For uniform replacement, Eqs. (69) and (72) reduce to

\(Z_q(p)=2\sqrt{\frac{p(1-p)}{q-1}}+\frac{q-2}{q-1}p,\) (77)

\(\delta_\mathrm{cyc}(D,q)=\frac{q-1}{(D-1)(\sqrt{D+q-2}+\sqrt{D-2})^2}.\) (78)

Since \(Z_q(1/2)>1/2\ge 1/(D-1)\), this crossing lies below 1/2; the full-range strong converse therefore justifies the notation \(\delta_\mathrm{rel}(D,q)\) used above. Thus Theorem 5 gives \(\delta_\mathrm{rel}(D,q)\sim(q-1)/(4D^2)\) when _q=o(D_<sup>2/3</sup>). For _q_=2, the reliability endpoint is exact at every \(D\ge 3\):

\(\delta_\mathrm{rel}(D,2)=\delta_\mathrm{cyc}(D,2)=\frac{1}{2}\left(1-\sqrt{1-\frac{1}{(D-1)^2}}\right).\) (79)

## 3.3 Decoding with Linear Programming

Although minimum-weight decoding is NP-hard for _q\>_2, a polynomial-time decoder can still recover from a positive fraction of randomly located symbol errors. We establish this for the standard nonbinary local-polytope LP decoder \[Fla+09\] on the Linial-Simkin ensemble. The recovery bound uses only the graph’s degree and girth but is independent of the alphabet size.

### 3.3.1 The decoder

Let _H=B<sup>T</sup>_, write _h<sub>ve</sub>=H<sub>ve</sub>_, and let \(\partial v\) be the edges incident to _v_. Given a syndrome \(\mathbf{s}\in\mathrm{im}H\), define the local constraint set

\(\mathcal{C}_v(s_v):=\left\{(b_e)_{e\in\partial v}\in\unknown_q^{\partial v}:\sum_{e\in\partial v}h_{ve}b_e=s_v\right\}.\) (80)

Instead of choosing a single error value on each edge _e_, the LP assigns a probability _x<sub>e,a</sub>_ to each possible value \(a\in\unknown_q\). These real-valued variables are called _symbol marginals_; write **x** for the vector of all such variables. At each vertex _v_, the LP also chooses a probability distribution \(\lambda_{v,\mathbf{b}}\) over the assignments in C_<sub>v</sub>(s<sub>v</sub>_). The two local distributions involving an edge must give the same marginal probabilities for its value. The constraints are

\(x_{e,a}\ge 0,\sum_{a\in\unknown_q}x_{e,a}=1,\lambda_{v,\mathbf{b}}\ge 0,\sum_{\mathbf{b}\in\mathcal{C}_v(s_v)}\lambda_{v,\mathbf{b}}=1,x_{e,a}=\sum_{\mathbf{b}\in\mathcal{C}_v(s_v)b_e=a}\lambda_{v,\mathbf{b}}(v\in V,e\in\partial v,a\in\unknown_q).\text{(81)}\)

The local distributions need not come from a joint distribution on complete words satisfying all checks. The LP minimizes the relaxed Hamming weight

\(\mathcal{L}(\mathbf{x})=\sum_{e\in E}(1-x_{e,0}).\) (82)

