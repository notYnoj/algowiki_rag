3.1. Let \(R_{\ell,z}=\lfloor R/2^\ell\rfloor\) be the \(n_1\times n_3\) matrix defined by<tbc>

<tbc>\(R_{\ell,z}[i,j]=\left\lfloor\frac{R[i,j]}{2^\ell}\right\rfloor-z.\)<tbc>

<tbc>Obtain a rank-\(r'=O(r)\) decomposition for \(R_{\ell,z}\) by appropriately rounding the rank-_r_ decomposition of _R_. Run Lemma 4.2 on the Exact Triangle instance \((A_{\ell,x},B_{\ell,y},R_{\ell,z})\) with parameter _K_. This is a potential-adjusting reduction, and hence the output is (I,T)--a set of \(r'\)-uniform _K_- doubling Exact Triangle instances I and a set of special triples \(\mathcal{T}\subseteq[n_1]\times[n_2]\times[n_3]\). Afterwards, enumerate all triples \((i,k,j)\in\mathcal{T}\) and update \(C[i,j]\leftarrow min\{C[i,j],A[i,k]+B[k,j]\}\).<tbc>

3.2. Enumerate all instances \((P',Q',R')\in\mathcal{I}\). Lemma 4.2 guarantees that \((P',Q',R')\) is an _D_-uniform 1_/D_-regular _K_-doubling Exact Triangle instance for some \(D\le r'\). Hence, \((P',Q')\) is an _D_- uniform 1_/D_-regular _K_-doubling Min-Plus Product instance. In fact, we may loosely bound \(D\le r'=O(r)=O(n_2)\) here. We compute the min-plus product \(P'*Q'\) and list _t_ witnesses for each output entry (_i,j_) by Lemma 5.1. For each triple (_i,k,j_) reported in this way we update \(C[i,j]\leftarrow min\{C[i,j],A[i,k]+B[k,j]\}\).<tbc>

<tbc>We argue that we correctly compute _C_\[_i,j_\] for all ordinary pairs (_i,j_). Fix any such pair, and let \(\ell\) be a level at which (_i,j_) is relevant. By definition, (_i,j_) has at least \(t2^{\ell+1}\)-pseudo-witnesses. Thus, with high probability we include at least one \(2^{\ell+1}\)-pseudo-witness in the randomly sampled set K. It follows that<tbc>

<tbc>\((A*B)[i,j]\le R[i,j]<(A*B)[i,j]+2^{\ell+1}.\)<tbc>

<tbc>Property (i) of Claim 5.8 further implies that there exist \(x,y\in\{0,1\}\) satisfying<tbc>

<tbc>\((A_{\ell,x}*B_{\ell,y})[i,j]=\left\lfloor\frac{(A*B)[i,j]-(x+y)2^{\ell-1}}{2^\ell}\right\rfloor.\)<tbc>

<tbc>Putting both statements together, we have<tbc>

<tbc>\(\left\lfloor\frac{R[i,j]}{2^\ell}\right\rfloor-3\le(A_{\ell,x}*B_{\ell,y})[i,j]\le\left\lfloor\frac{R[i,j]}{2^\ell}\right\rfloor,\)<tbc>

<tbc>and consequently, there is some \(z\in\{0,1,2,3\}\) such that \((A_{\ell,x}*B_{\ell,y})[i,j]=R_{\ell,z}[i,j]\). In particular, for each witness _k_ of \((A_{\ell,x}*B_{\ell,y})[i,j]\), (_i,k,j_) forms an exact triangle in the instance \((A_{\ell,x},B_{\ell,y},R_{\ell,z})\). Moreover, all these witnesses are \(2^\ell\)-pseudo-witnesses of (_A∗B_)\[_i,j_\] by Property (iii), and they include at least one proper witness _k_<sup>∗</sup> of (_A∗B_)\[_i,j_\] by Property (ii).

Running Time: The O(1) calls to Lemma 4.2 take time
1+o(1)
For the inequality we have used that n2 n1,n3 and that r' = O(r) = O(n2/t).

Running Time:
O(|I| t MinPlus(n1,n2,n3 u;D n2; 1/D; K))
(K - MinPlus(n1,n2,n3 u;D n2; 1/D; K))
1+o(1)

