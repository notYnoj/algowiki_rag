Therefore, _k_<sup>∗</sup> is a minimizer of this expression and thus a witness of \((A_{\ell,x}*B_{\ell,y})[i,j]\), proving (ii). Moreover, for each other witness _k_ we must have \(A[i,k]+B[k,j]<A[i,k^*]+B[k^*,j]+2^\ell\), and thus _k_ is a \(2^\ell\)-pseudo- witness, proving (iii).

Returning to the proof of Lemma 5.7, we are ready to state the reduction. We classify the pairs (_i,j_) into three categories based on their number of pseudo-witnesses:

1. If (_A∗B_)\[_i,j_\] has at least _t_1-pseudo-witnesses (i.e., witnesses) then we call (_i,j_) _exceptionally popular_.<tbc>

2. If (_A∗B_)\[_i,j_\] has at most _t_2_<sup>L</sup>_-pseudo-witnesses then we call (_i,j_) _exceptionally unpopular_.<tbc>

3. Otherwise we call (_i,j_) _ordinary_. For each ordinary pair there is some level \(0\le\ell<L\) such that (_i,j_) has at most \(t2^\ell\)-pseudo-witnesses and simultaneously at least \(t2^{\ell+1}\)-pseudo-witnesses--we say that (_i,j_) is _relevant_ at that level \(\ell\).

These definitions are only required for the analysis, and we do not compute the classification explicitly.

We will now describe the algorithm. We initially set _C_ to be the all-\(\perp\) matrix. Throughout we will only update _C_ via \(C[i,j]\leftarrow A[i,k]+B[k,j]\), so we will never underestimate the values of _A∗B_. We will deal with the exceptionally popular, exceptionally unpopular and ordinary pairs in three separate steps. The first and especially the second one can be regarded as exceptional special cases.

1. _(Exceptionally Popular Pairs)_ Sample a uniformly random subset \(\mathcal{K}\subseteq[n_2]\) with rate \(\Theta(t^{-1}log(n_1n_3))\). Then enumerate all triples \((i,k,j)\in[n_1]\times\mathcal{K}\times[n_3]\) and update \(C[i,j]\leftarrow min\{C[i,j],A[i,k]+B[k,j]\}\). Each exceptionally popular pair (_i,j_) has at least _t_ witnesses _k_, so with high probability we include at least one such witness in K. In this case we correctly assign _C_\[_i,j_\].<tbc>

2. _(Exceptionally Unpopular Pairs)_ By definition a pair (_i,j_) is exceptionally unpopular if it has less than _t_2_<sup>L</sup>_-pseudo-witnesses. But the matrices _A<sub>L</sub>_ and _B<sub>L</sub>_ in fact only contain two possible entries: 0 and \(\perp\). Hence, a pair (_i,j_) is exceptionally unpopular if and only if the number of indices _k_ with \(A[i,k]\neq\perp\) and \(B[k,j]\neq\perp\) is at most _t_. One way to deal with these pairs is to apply Lemma 5.1 in combination with the fast algorithm for Min-Plus Product to list _t_ witnesses in the product _A<sub>L</sub>∗B<sub>L</sub>_. (However, this product is of course just a Boolean matrix multiplication, so one could have also solved this step in \(\tilde{O}(t)\) matrix products.)<tbc>

3. _(Ordinary Pairs)_ To deal with the ordinary pairs, we prepare a low-rank matrix approximating _A∗B_ (in a sense that will be clear soon). Sample a uniformly random subset \(\mathcal{K}\subseteq[n_2]\) with rate \(\Theta(t^{-1}log(n_1n_3))\). Let _U_ be the submatrix of _A_ restricted to the columns in K and let _V_ be the submatrix of _B_ restricted to the rows in K. Compute the min-plus product _R=U∗V_ by brute-force. Note that _R_ is a matrix of rank at most _r_=|K| as is witnessed by the rank-_r_ decomposition (_U,V,S_) (for some appropriate matrix _S_ that is easy to compute along the way). With high probability, the rank is bounded by \(r=|\mathcal{K}|=\tilde{O}(n_2/t)\).<tbc>

Running Time:
O(n1n2n3/t).

Running Time:
O(t MinPlus(n1,n2,n3 | u 0)).

Running Time:
O(n1n2n3/t).

Run the following steps for all levels \(0\le\ell\le L\), for all \(x,y\in\{0,1\}\) and all \(z\in\{0,1,2,3\}\):

