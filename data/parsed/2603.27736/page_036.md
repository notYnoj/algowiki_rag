The correctness claim is that after step 1 is complete we have correctly assigned _C_\[_i,j_\]=(_A∗B_)\[_i,j_\] for all unpopular pairs (_i,j_). Fix any such pair, and let _k_ be a witness of (_i,j_). In each iteration the probability that we include _k_ into K is \(\rho\), and independently the probability that we miss all other pseudo-witnesses of (_i,j_) in K is at least \(1-\rho tn_2/n'_2\ge 1/2\), by a union bound over the at most \(tn_2/n'_2\) pseudo-witnesses of (_i,j_). Hence, with probability at least \(\rho/2\) the only pseudo-witness of (_i,j_) in _K_ is a proper witness, and so the algorithm is forced to list the triple (_i,k,j_). Over the \(O(\rho^{-1}\mathrm{log}(n_1n_3))\) iterations this event happens at least once for each unpopular pair (_i,j_) with high probability.<tbc>

2. _(Popular Pairs)_ We deal with the popular pairs by solving _O_(1) low-rank Exact Triangle instances. Specifically, repeat the following steps for all offsets \(z\in\{0,1,2\}\). Recall from the first paragraph that we have access to a matrix \(\tilde{C}\) that approximates _A∗B_ with small additive error, so in the _z_-th iteration our goal is to correctly assign _C_\[_i,j_\]=(_A∗B_)\[_i,j_\] for all entries popular pairs (_i,j_) with \((A*B)[i,j]=\tilde{C}[i,j]+z\).<tbc>

2.1. Sample a uniformly random subset \(\mathcal{K}\subseteq[n_2]\) with rate \(\Theta(n'_2/(tn_2)\mathrm{log}(n_1n_3))\). The resulting set has size \(|\mathcal{K}|=\tilde{O}(n'_2/t)\) with high probability. Moreover, with high probability K contains at least one pseudo-witness for each popular pair (_i,j_).<tbc>

2.2. Let _U_<sub>1</sub> be the matrix _A_<sub>1</sub> restricted to the columns in K, let _V_<sub>1</sub> be the matrix _B_<sub>1</sub> restricted to the rows in K and compute their min-plus product _R_<sub>1</sub>=_U_<sub>1</sub>∗_V_<sub>1</sub>. Additionally, report a witness _k_ for each output entry (_i,j_) by Lemma 5.1. Let _S_<sub>1</sub> be the matrix that stores these witnesses in the form _S_<sub>1</sub>\[_i,j_\]=_k_. Then observe that (_U_<sub>1</sub>_,V_<sub>1</sub>_,S_<sub>1</sub>) is a valid rank-_r_<sub>1</sub> decomposition of _R_<sub>1</sub> for \(r_1=|\mathcal{K}|=\tilde{O}(n'_2/t)\).<tbc>

2.3. Let _R_ be the \(n_1\times n_3\) matrix defined by<tbc>

<tbc>\(R[i,j]=\left\{\begin{array}{ c c }
\tilde{C}[i,j]+z & \text{if}\lfloor(\tilde{C}[i,j]+z)/q\rfloor=R_1[i,j], \\
\perp & \text{otherwise.}
\end{array}\right.\)<tbc>

<tbc>We can now find a rank-_r_ decomposition of _R_ for _r=r_<sub>1</sub>_q_. As outlined before, this step involves trivially bounding the select-plus rank of \(R-q\cdot R_1\) by _O(q_) (Fact 3.2) and then applying submultiplicativity (Fact 3.3).<tbc>

<tbc>Concretely, we compute the rank decomposition (_U,V,S_) of _R_ from the data we have precom puted in step 2.2 as follows. Let \(U\in\mathbb{Z}^{[n_1]\times(\mathcal{K}\times[q])}\) be the matrix obtained from \(q\cdot U_1\in\mathbb{Z}^{[n_1]\times\mathcal{K}}\) by replacing each column by _q_ copies, where in the \(\ell\)-th copy we add \(\ell\) to all entries. Next, we ob tain \(V\in\mathbb{Z}^{(\mathcal{K}\times[q])\times[n_3]}\) from \(q\cdot V_1\in\mathbb{Z}^{\mathcal{K}\times[n_3]}\) by duplicating each row _q_ times (but without further additions). Finally, define _S_ by<tbc>

<tbc>\(S[i,j]=\left\{\begin{array}{ c c }
(S_1[i,j],R[i,j]\mathrm{mod}q) & \text{if}R[i,j]\neq\perp, \\
\perp & \text{if}R[i,j]=\perp.
\end{array}\right.\)<tbc>

Running Time:
O(MinPlus(n1, n'2,n3|u\le p)
n22)

Running Time:
O(MinPlus(n1, n'2,n3|u\le p))

