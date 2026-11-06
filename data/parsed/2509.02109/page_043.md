`return R`

`@staticmethod`

`def backward(ctx, H):`

`P, S = ctx.saved\_tensors`

`H\_sym = .5 \* (H + H.transpose(-2, -1))`

`D = S.unsqueeze(-1) + S.unsqueeze(-2)`

`G = (P.transpose(-2,-1) @ H\_sym @ P) / D`

`G = G.masked\_fill(D == 0, 0)`

`return P @ G @ P.transpose(-2, -1)`

## A.9 Experimental Details and Additional Results

### A.9.1 Unbalanced GMM-OT

The difficulties of optimising non-uniform mixture weights described in Section 3.3 motivate relaxing the marginal constraints. Balanced GMM-OT requires the transport plan to match the mixture weights exactly. The unbalanced formulation of Section 3.4 penalises marginal discrepancies: increasing the penalty progressively restores the marginal constraints, providing a transition from the relaxed problem to balanced OT.

We illustrate this approach using the non-uniform source and target GMMs of Section 4.3. We compare flows with learnable weights under balanced OT, unbalanced OT with a fixed penalty, and an increasing penalty followed by balanced OT. In the unbalanced formulation Eq. (21), we take equal penalties \(\lambda_0=\lambda_1=\lambda\). Since the optimisation objectives differ, all curves report the balanced cost Eq. (14). Figure 20 shows a lower final balanced cost for both strategies involving unbalanced OT, with the smallest value obtained by the strategy where we progressively increase the penalty.

### A.9.2 Impact of the Number of Components for the Gradient Methods

In this section, we present the impact of the parameter _K_ in the setting of Section 4.5. We fix _n_=2000_,d_=3 and _T_=30, varying \(K\in\{3,5,8,10,12,15\}\) in Fig. 21. The results suggest that the number of components _K_ greatly impacts the difficulty of the EM algorithm to converge to a "stable" fixed point, incurring worsening gradient approximations. In certain settings, the spectral norm of the Jacobian can be of the order of 1, completely invalidating the OS method. The AI method is successful for low values of _K_, however for larger _K_, neither OS nor AI approximate the AD method satisfactorily. In this experiment, we required a regularisation of 10<sup>-8</sup>_I<sub>d</sub>_ for the covariances for numerical stability.

### A.9.3 Barycentres

We consider a barycentre problem similar to Section 5.1, with more complex datasets: we take three two-dimensional images _I_<sub>1</sub>, _I_<sub>2</sub> and _I_<sub>3</sub>, we randomly sample _n_=500 points \(Y_i\in\mathbb{R}^{n\times 2}\) from each. In<tbc>

Balanced cost
Balanced
Unbalanced (A = 1000)
Increasing A
Balanced
Unbalanced (A = 1000)
Increasing A
102
101
100
0
200 Iteration
400
Source GMM
Final GMM
Target GMM

Figure 20: Comparison of balanced and unbalanced particle flows for non-uniform weights.

