Sample \(X\subseteq[0,n]\) uniformly at random with rate \(p=n^{-\rho}\). By Chernoff’s bound, this set has size \(|X|=O(n^{1-\rho})\) with high probability. Compute the sequence \(R\in\mathbb{Z}^{[0,2n]}\) defined by<tbc>

<tbc>\(R[k]=min_{i,j\in Xi+j=k}\left\lfloor\frac{A[i]}{2^\ell}\right\rfloor+\left\lfloor\frac{B[j]}{2^\ell}\right\rfloor+z\)<tbc>

<tbc>by brute-force. Moreover, construct the set<tbc>

<tbc>\(\mathcal{X}=\left\{\left(i,\left\lfloor\frac{A[i]}{2^\ell}\right\rfloor\right):i\in X\right\}\cup\left\{\left(j,\left\lfloor\frac{B[j]}{2^\ell}\right\rfloor+z\right):j\in X\right\},\)<tbc>

<tbc>and observe that \(\mathcal{R}:=\mathcal{I}(R)\subseteq\mathcal{X}+\mathcal{X}\). In particular, the rank of R is at most \(r=|\mathcal{X}|\le 2|X|=O(n^{1-\rho})\).<tbc>

3.2. For convenience, write P:=I(_P_) and Q:=I(_Q_). Apply Lemma 4.3 to the 3SUM instance (P,Q,R) and the set X (which satisfies \(\mathcal{R}\subseteq\mathcal{X}+\mathcal{X}\), as required). This is an instance of 3SUM over the group Z<sup>2</sup>, which can be easily mapped to plain integers via the standard embedding into disjoint bit-blocks. The output of Lemma 4.3 consists of

• \(O(n^\epsilon)\) subinstances \((\mathcal{P}'\subseteq\mathcal{P},\mathcal{Q}'\subseteq\mathcal{Q},\mathcal{R}'\subseteq\mathcal{R})\), each provided with a \((O(n^\epsilon),O(n^{2-2\rho}))\)- container H of \(\mathcal{P}'\cup\mathcal{Q}'\cup\mathcal{R}'\), and<tbc>

• a set of 3SUM solutions \(\mathcal{T}\subseteq\mathcal{P}\times\mathcal{Q}\times\mathcal{R}\).<tbc>

3.3. For each triple \(((i,a),(j,b),(k,c))\in\mathcal{T}\) : Update \(C[k]\leftarrow min\{C[k],A[i]+B[j]\}\).<tbc>

3.4. For each subinstance \((\mathcal{P}',\mathcal{Q}',\mathcal{R}')\): Let \(P'\) denote the restriction of _P_ so that \(\mathcal{P}'=\mathcal{I}(P')\). Similarly, let \(Q'\) denote the restriction of _Q_ so that \(\mathcal{Q}'=\mathcal{I}(Q')\). Let \((P',Q')\) be one of the designated Min-Plus Convolution Listing instances with threshold _t_. We solve the instance by the reduction. The output is a set of witnesses, i.e., triples (_i,j,k_) with \(P'[i]+Q'[j]=(P'*Q')[k]\). For each such triple update \(C[k]\leftarrow min\{C[k],A[i]+B[j]\}\).

In the end, we return the sequence _C_ computed before. This completes the description of the algorithm. It should be clear that cases 1 and 2 correctly assign _C_\[_k_\]=(_A∗B_)\[_k_\] for all exceptional indices _k_, but it remains to show that the same holds for the ordinary ones.

Fix any ordinary index _k_<sup>∗</sup>. Let \(0\le\ell<L\) be the scale at which _k_<sup>∗</sup> becomes relevant (i.e., (_A∗B_)\[_k_<sup>∗</sup>\] has at most \(t2^\ell\)-pseudo-witnesses and at least \(t2^{\ell+1}\)-pseudo-witnesses). Also, fix any witness _i_<sup>∗</sup> of (_A∗B_)\[_k_<sup>∗</sup>\] and let _j_<sup>∗</sup>=_k_<sup>∗</sup>-_i_<sup>∗</sup>. Let \(x,y\in\{0,1\}\) be such that \((A[i^*]mod2^\ell)\in x2^{\ell-1}+[0,2^{\ell-1})\) and \((B[j^*]mod2^\ell)\in y2^{\ell-1}+[0,2^{\ell-1})\). Now focus on any iteration corresponding to our choice of \(\ell,x,y\) (and some _z_ to be determined soon).

**Claim 5.4.** _In any iteration corresponding to these choices of_ \(\ell,x,y\)_, it holds that:_

(_i)_ _i_<sup>∗</sup> _is a witness of_ (_P∗Q_)\[_k_<sup>∗</sup>\]_, and_ \(P[i^*]+Q[j^*]\le\lfloor(A*B)[k^*]/2^\ell\rfloor\)_, and_<tbc>

(_ii)_ _every witness of_ (_P∗Q_)\[_k_<sup>∗</sup>\] _is a_ \(2^\ell\)_-pseudo-witness of_ (_A∗B_)\[_k_<sup>∗</sup>\].<tbc>

