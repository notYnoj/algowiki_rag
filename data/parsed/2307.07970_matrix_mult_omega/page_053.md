satisfy all these requirements.) We include these Lagrange multiplier constraints (34) in our optimization problem (28).<sup>5</sup> Similarly, in Theorem 6.3, we also introduce Lagrange multiplier constraints when we need to ensure that some distribution has maximum entropy given its marginals.

### Smooth the landscape.

In Theorems 5.3 and 6.3, the intermediate variables named _E_<sub>1</sub>_,E_<sub>2</sub>_,E_<sub>3</sub> are minimums of three terms. If we calculate them according to the definition, it would create a "spike" (non- differentiable point) in the landscape, which is unfriendly for many optimizable methods including SQP. (SQP requires all objective and constraint functions to be twice continuously differentiable.) To address this issue, we treat _E_<sub>1</sub>_,E_<sub>2</sub>_,E_<sub>3</sub> as optimizable variables and transform the minimum into linear inequality constraints:

\(E=min(x,y,z)\Rightarrow E\le x,E\le y,E\le z.\)

Since _E_ (any of _E_<sub>1</sub>_,E_<sub>2</sub>_,E_<sub>3</sub>) is positively correlated with the number of matrix multiplication tensors we produce, we do not need to worry that _E_ takes on a value smaller than min(_x,y,z_). The newly introduced constraints are linear and thus have smooth landscapes. We include these auxiliary optimizable parameters and constraints in the optimization problem (28). In practice, we also observe that SQP would not work well without this type of smoothing.

### Numerical results.

We wrote a MATLAB \[Mat22\] program to solve the optimization problem (28), with the help of SNOPT \[GMS05\], a software package for solving large-scale optimization problems. By running the program for different \(\kappa\), we obtained various upper bounds of \(\omega(1,\kappa,1)\), as shown in  1. All bounds are obtained by analyzing the fourth power<sup>6</sup> of the CW tensor with _q_=5. Specifically, we obtained the important bounds \(\omega\le 2.371552\), \(\alpha\ge 0.321334\), and \(\mu\le 0.527661\). The code and parameters are available at `https://osf.io/7wgh2/?view\_only=ce1a6a66d9fc432d8f6da39a6ea4b6e4`.

## References

<sup>5</sup>In the program, we use the exponential form of (28): \(exp(\lambda_X(i)+\lambda_Y(j)+\lambda_Z(k)+\lambda_S-1)=\alpha_{max}(i,j,k)\), in order to avoid numerical issues like ln0. <sup>6</sup>Our analysis also works for the eighth power, but it was too slow to solve the optimization problem due to the large number of parameters.

