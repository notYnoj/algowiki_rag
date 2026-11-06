We argue that in the substeps 3.1 and 3.2 we enumerate all witnesses of \((A_{\ell,x}*B_{\ell,y})[i,j]\), including the desired proper witness _k_<sup>∗</sup>. Lemma 4.2 implements a potential-adjusting reduction. We are thus guaranteed that each exact triangle in \((A_{\ell,x},B_{\ell,y},R_{\ell,z})\) appears in T or it appears as an exact triangle in one of the instances in I. If the exact triangle (_i,k_<sup>∗</sup>_,j_) falls into the former case, we successfully discover it in substep 3.1. We focus on the latter case.

Focus on the instance \((A',B',R')\in\mathcal{I}\) in which the exact triangle (_i,k_<sup>∗</sup>_,j_) is present. Recall that this instance is a potential adjustment of \((A_{\ell,x},B_{\ell,y},R_{\ell,z})\), and thus

\(A'[i,k]=A_{\ell,x}[i,k]+u[i]+v[k]\text{or}A'[i,k]=\perp\text{for all}(i,k)\in[n_1]\times[n_2],\)<br>
\(B'[k,j]=B_{\ell,y}[k,j]-v[k]+w[j]\text{or}B'[k,j]=\perp\text{for all}(k,j)\in[n_2]\times[n_3],\)<br>
\(R'[i,j]=R_{\ell,z}[i,j]+u[i]+w[j]\text{or}R'[i,j]=\perp\text{for all}(i,j)\in[n_1]\times[n_3],\)

for some potential functions _u,v,w_. From this it follows that \((A'*B')[i,j]=R'[i,j]\). On the one hand, _k_<sup>∗</sup> witnesses \((A'*B')[i,j]\le R'[i,j]\). On the other hand, we cannot have \((A'*B')[i,j]<R'[i,j]\) as then, rewriting \(A',B',R'\) by the previous three identities, we would also have \((A_{\ell,x}*B_{\ell,y})[i,j]<R_{\ell,z}[i,j]\), leading to a contradiction.

Now, as \((A'*B')[i,j]=R'[i,j]\), it follows that each witness _k_ of \((A'*B')[i,j]\) must form an exact triangle (_i,k,j_) in \((P',Q',R')\) and thus also in \((A_{\ell,x},B_{\ell,y},R_{\ell,z})\). Hence, _k_ is a witness of \((A_{\ell,x}*B_{\ell,y})[i,j]\), and Property (iii) implies that _k_ is a \(2^\ell\)-pseudo-witness of (_i,j_). Recall that we assume that (_i,j_) is relevant at level \(\ell\), hence the total number of \(\ell\)-pseudo-witnesses is at most _t_. Therefore, we are guaranteed to list _all_ witnesses of \((A'*B')[i,j]\) by Lemma 5.1 (with high probability). In particular, we will list the proper witness _k_<sup>∗</sup>, and therefore update _C_\[_i,j_\] as intended.

This completes the description of the reduction and the correctness analysis.

## Running Time.

Summing over all _O(L_)=_O_(log_u_) levels, the total time of the steps as analyzed above is

\(\left(Kt\cdot\mathrm{MinPlus}(n_1,n_2,n_3|u;D\le n_2;\rho\le 1/D;K)+\frac{n_1n_2n_3}{K^{1/98000}}+\frac{n_1n_2n_3K}{t}\right)^{1+o(1)}\cdot\mathrm{log}u.\)

Pick \(t=K^{1+1/98000}\le K^2\). The total running time becomes

\(\left(K^3\cdot\mathrm{MinPlus}(n_1,n_2,n_3|u;D\le n_2;\rho\le 1/D;K)+\frac{n_1n_2n_3}{K^{1/98000}}\right)^{1+o(1)}\cdot\mathrm{log}u,\)

which is as claimed by readjusting _K_ to _K_<sup>1/3</sup>.

**Corollary 5.9.** _Let_ \(\kappa,\epsilon>0\) _and_ \(0<\alpha_2\le\alpha_1,\alpha_3\) _be constants. If_ \(\mathrm{MinPlus}(n^{\alpha_1},n^{\alpha_2},n^{\alpha_3}|D\le n^{\alpha_2};\rho\le 1/D;K\le n^\kappa)\le O(n^{\alpha_1+\alpha_2+\alpha_3-\epsilon})\) _then the APSP Hypothesis fails._

**Proof.** Suppose that \(\mathrm{MinPlus}(n^{\alpha_1},n^{\alpha_2},n^{\alpha_3}|D\le n^{\alpha_2};\rho\le 1/D;K\le n^\kappa)\le O(n^{\alpha_1+\alpha_2+\alpha_3-\epsilon})\), i.e., the _D_-uniform 1_/D_-regular \(n^\kappa\)-doubling Min-Plus Product is in time \(O(n^{\alpha_1+\alpha_2+\alpha_3-\epsilon})\) for all \(D\le n^{\alpha_2}\). Then by Lemma 5.7 applied with parameter \(K=n^{\mathrm{min}\{\kappa,\epsilon/2\}}\) the general Min-Plus Product of size \(n^{\alpha_1}\times n^{\alpha_2}\times n^{\alpha_3}\) over the universe \[_u_\] can be solved in time

\(\mathrm{MinPlus}(n^{\alpha_1},n^{\alpha_2},n^{\alpha_3}|u)\)<br>
\(\le\left(\mathrm{MinPlus}(n^{\alpha_1},n^{\alpha_2},n^{\alpha_3}|u;D\le n^{\alpha_2};K\le n^\kappa)\cdot n^{\epsilon/2}+\frac{n^{\alpha_1+\alpha_2+\alpha_3}}{n^{\mathrm{min}\{\kappa,\epsilon/2\}/300000}}\right)^{1+o(1)}\cdot\mathrm{log}u\)<br>
\(\le\left(n^{\alpha_1+\alpha_2+\alpha_3-\epsilon/2}+n^{\alpha_1+\alpha_2+\alpha_3-\mathrm{min}\{\kappa,\epsilon/2\}/300000}\right)^{1+o(1)}\cdot\mathrm{log}u\)<br>
\(\le n^{\alpha_1+\alpha_2+\alpha_3-\mathrm{min}\{\kappa,\epsilon/2\}/300000+o(1)}\cdot\mathrm{log}u.\)

