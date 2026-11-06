**Algorithm 1** Cyclic coordinate descent for ma-QAOA

**Input:** ma-QAOA objective \(F_p(\Theta)\), initial parameter vector \(\Theta^{(0)}=(\theta_1^{(0)},\dots,\theta_D^{(0)})\), maximum number of sweeps _T_max, tolerance \(\varepsilon\), optimisation sign \(s\in\{+1,-1\}\)

**Output:** Optimised parameter vector \(\Theta^\star\)

1: \(\Theta\leftarrow\Theta^{(0)}\)

2: \(F^\mathrm{curr}\leftarrow F_p(\Theta)\)

3: **for** _t_=1_,...,T_max **do**

4: \(F^\mathrm{start}\leftarrow F^\mathrm{curr}\)

5: **for** _d_=1_,...,D_ **do**

6: \(\varphi\leftarrow\theta_d\)

7: \(f_0\leftarrow F^\mathrm{curr}\)

8: \(f_+\leftarrow F_p(\theta_1,\dots,\theta_d+\pi/2,\dots,\theta_D)\triangleright\) expectation-value evaluation

9: \(f_-\leftarrow F_p(\theta_1,\dots,\theta_d-\pi/2,\dots,\theta_D)\triangleright\) expectation-value evaluation

10: \(g\leftarrow 2f_0-f_+-f_-\)

11: \(h\leftarrow f_+-f_-\)

12: \(\theta_d^\star\leftarrow\mathcal{W}\big(\varphi+s\frac{\pi}{2}-\mathrm{atan}2(g,h)\big)\triangleright\mathcal{W}(\cdot)\) wraps the angle modulo \(2\pi\)

13: \(\theta_d\leftarrow\theta_d^\star\)

14: \(F^\mathrm{curr}\leftarrow\frac{f_++f_-}{2}+s\frac{\sqrt{g^2+h^2}}{2}\)

15: **end for**

16: **if** \(\big|F^\mathrm{curr}-F^\mathrm{start}\big|<\varepsilon\) **then**

17: **break**

18: **end if**

19: **end for**

20: \(\Theta^\star\leftarrow\Theta\)

21: **return** \(\Theta^\star\)

the noiseless setting, each update moves the selected coordinate directly to the analytic extremum of its one-dimensional objective, so the objective is monotonically non-decreasing for maximisation tasks. However, because the method updates only one coordinate at a time, it does not explicitly capture correlations among parameters and may converge to a suboptimal coordinate-wise optimum. Algorithm 1 outlines the coordinate descent training procedure for ma-QAOA.

## 4 Performance Evaluation

### 4.1 Evaluation Setup

We evaluate the proposed training method on the maximum independent set problem. For a graph _G_=(_V,E_), each vertex is represented by a single qubit, and a measured bit value _x<sub>i</sub>_=1 indicates that vertex _i_ is selected; feasible solutions therefore satisfy _x<sub>i</sub>x<sub>j</sub>_=0 for every edge \((i,j)\in E\). We generated the benchmark connected Erd ̋os-Rényi graphs from the families in  1 using 15 random seeds each. Constraints are handled using a feasibility-preserving MIS mixer: the circuit starts from \(|0\rangle^{\otimes n}\), without initial Hadamard gates, and applies a controlled _R<sub>X</sub>_ rotation to a vertex only when all of its neighbouring vertices are unselected. We compare the proposed method with representative gradient-based, stochastic, and derivative-free baselines, including vanilla gradient descent (GD), adaptive moment estimation (Adam) \[Kingma and Ba, 2014\], simultaneous perturbation stochastic approximation (SPSA) \[Spall, 2002\], constrained optimisation by linear approximations (COBYLA) \[Powell, 1994\], the Nelder-Mead simplex method (NM) \[Nelder and Mead, 1965\], Powell’s derivative-free conjugate-direction method (Powell) \[Powell, 1964\], and the limited-memory Broyden-Fletcher-Goldfarb-Shanno algorithm with bound constraints (L-BFGS- B) \[Byrd et al., 1995\]. Since optimisers differ in the number of objective calls required per update, we report training cost in terms of the number of expectation-value evaluations rather than the number of optimiser iterations. Each expectation-value evaluation corresponds to estimating the objective value at a fixed parameter setting; on quantum hardware, this requires repeated circuit preparations and measurements, with the total shot cost scaling with the chosen shot budget. This metric therefore provides a hardware-relevant proxy for the computational cost incurred on the quantum device.

