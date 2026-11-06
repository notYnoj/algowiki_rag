• For every constituent tensor _T<sub>i,j,k</sub>_ that appears in our interface tensors, we directly set \(\alpha_{i,j,k}\) as its split distribution in every region, and let _A_<sub>1</sub>=_A_<sub>2</sub>=_A_<sub>3</sub>=1/3, which means that all three regions are symmetric to each other.<tbc>

• The distribution used in our global stage is set to \(\alpha\) as well. Other parameters are uniquely determined by these specified ones.<tbc>

• For every constituent tensor _T<sub>i,j,k</sub>_ that contains a zero, say _i_=0, we choose its complete split distributions \(\beta_X,\beta_Y,\beta_Z\) that maximizes its size as an inner product tensor, i.e., maximizes \(H(\beta_Y)\).<tbc>

• Other parameters are uniquely determined by the specified ones.

It is easy to see that these parameters form a feasible solution. Furthermore, these parameters actually lead to the same upper bound on \(\omega\) as Le Gall’s analysis. We start from this feasible solution and perform SQP to obtain an upper bound for \(\omega=\omega(1,1,1)\).

For \(\kappa\neq 1\), our strategy is to start with a solution for another \(\kappa\) nearby. For example, it is natural to believe that a good solution for \(\omega(1,0.95,1)\) is similar to that for \(\omega(1,1,1)\). Therefore, we use our parameters for \(\omega(1,1,1)\) as the initial point for optimizing the bound of \(\omega(1,0.95,1)\), and proceed with SQP to obtain the bound for \(\omega(1,0.95,1)\). Then, we can further start with our parameters for \(\omega(1,0.95,1)\) to obtain parameters for \(\omega(1,0.90,1)\), and so on.

## Lagrange multipliers.

In Theorem 5.3, we need to calculate \(P_\alpha=\mathrm{max}_{\alpha^\prime\in D}H(\alpha')-H(\alpha)\) where _D_ represents the set of distributions that share marginals with \(\alpha\). Although this definition of \(P_\alpha\) is not a closed form in terms of \(\alpha\), we can let the max-entropy distribution \(\alpha_\mathrm{max}:=\mathrm{argmax}_{\alpha^\prime\in D}H(\alpha')\) be an optimizable variable, and use the method of Lagrange multipliers to ensure that \(\alpha'\) has the largest entropy among _D_.

Formally, we first add linear constraints to force \(\alpha_\mathrm{max}\) and \(\alpha\) to have the same marginals:

\(\sum_{j+k=2^{\ell^*}-i}\left(\alpha_\mathrm{max}(i,j,k)-\alpha(i,j,k)\right)=0,\forall i=0,1,\dots,2^{\ell^*},\) (29)

\(\sum_{i+k=2^{\ell^*}-j}\left(\alpha_\mathrm{max}(i,j,k)-\alpha(i,j,k)\right)=0,\forall j=0,1,\dots,2^{\ell^*},\) (30)

\(\sum_{i+j=2^{\ell^*}-k}\left(\alpha_\mathrm{max}(i,j,k)-\alpha(i,j,k)\right)=0,\forall k=0,1,\dots,2^{\ell^*},\) (31)

\(\sum_{i,j,k}\alpha_\mathrm{max}(i,j,k)=1,\) (32)

\(\alpha_\mathrm{max}(i,j,k)\ge 0,\forall i+j+k=2^{\ell^*}.\) (33)

Let \(\lambda_X(i),\lambda_Y(j),\lambda_Z(k),\lambda_S\) (\(0\le i,j,k\le 2^{\ell^*}\)) be Lagrange multipliers for (29), (30), (31), (32) respectively, which we also treat as optimizable variables. Then the first-order optimality of \(H(\alpha_\mathrm{max})\) can be written as

\(\lambda_X(i)+\lambda_Y(j)+\lambda_Z(k)+\lambda_S=\mathrm{ln}\alpha_\mathrm{max}(i,j,k)+1,\forall i+j+k=2^{\ell^*}.\) (34)

(Note that any \(\alpha_\mathrm{max}\) satisfying (34) will also satisfy strict inequalities in (33), thus we do not need to create Lagrange multipliers for (33).) Since the entropy function \(H(\cdot)\) is strictly concave, any \(\alpha_\mathrm{max}\) satisfying these constraints is guaranteed to have maximum entropy. (Conversely, the true max-entropy distribution \(\alpha_\mathrm{max}\) will<tbc>

