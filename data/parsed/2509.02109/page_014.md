<tbc>framework encompasses the case of non-uniform weights, as illustrated theoretically and experimentally, it appears that the non-uniform weight setting is impractical. As a result, we recommend using uniform weights, in particular using the fixed-weights EM approach (Algorithm 2) for speed and stability. Assuming fixed uniform weights in GMMs is a very classical assumption in the machine learning literature, made for instance in all the recent \[Kim22; Lam+22; Hui+24; PLK26\]. Fixed weights do not need to be uniform and can be fixed for instance to the target GMM weights. We investigate further the local minima that arise in this case in Appendix A.7.4.

## 4.4 Stochastic \(\mathrm{EM}-\mathrm{MW}_2^2\) Flow with Fixed Weights

We consider a similar setting to Section 4.2 but introduce stochasticity in the flow at each step by performing EM only on a subsample of the optimised source point cloud and of the target point cloud. While we illustrate the technique on a toy example here, this "minibatch" stochastic gradient descent method is useful in practice when the dataset size is too large for simultaneous optimisation \[Fat+20; Fat+21b; Fat+21a; Ton+24\]. The same principle is applied to the image generation task in Appendix A.9.7. We observe in Fig. 5 that the general trajectory remains similar to the deterministic case. Notice that in this setting, the components are sufficiently close together to interact, yielding non-rectilinear trajectories when points are influenced by multiple components. This is amplified by the stochasticity of the method.

## 4.5 Quantitative Study of EM Convergence and Gradients

We study the impact of the number of points _n_, components _K_ and EM iterations _T_ on the convergence of EM iterations (to a fixed point of _F_), the local contractivity of _F_ around the fixed point, and the gradient approximation methods introduced in Section 2.3. The experimental setting is as follows: for each of the three parameters _n,K,T_ separately (say _n_), we consider a range of values<tbc>

EM Flow with Non-Uniform Weights
EM Flow Weights with Non-Uniform Weights
EM Flow with Uniform Weights
final GMM
(0, 0, 1)
source GMM
final GMM
source GMM
(0, 0, 1)
target GMM
target GMM
102
101
0
100
200
300
400
500
Iteration
(a) Particle flow (NU).
(b) Weight evolution on the simplex (NU).
(c) Particle flow (U).
(d) Energy evolutions.

Sample Ratio: 0.25
Sample Ratio: 0.5
Sample Ratio: 1.0
MW 2 Loss per Iteration
Sample Ratio: 0.25
Sample Ratio: 0.5
Sample Ratio: 1.0
101
100
0
200
400
600
800
1000
1200
1400
Iteration

Figure 4: Flow of E_<sub>T</sub>_ with the AD method and standard EM Algorithm 1. We compare two settings: one with non-uniform GMM weights (NU) and one with uniform weights (U).

Figure 5: Stochastic Flow of E_<sub>T</sub>_ for Algorithm 2 with the full automatic differentiation method. We vary the sub-sampling ratio \(r\in(0,1]\), which corresponds to performing EM on only \([r\times n]\) random points from the current point cloud at each step.

