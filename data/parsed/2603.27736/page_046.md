• _(Edges)_ For each \(A[i,k]\neq\perp\) we add an edge \((i,(k,A[i,k]))\in I\times K_1\), and for each \(B[k,j]\neq\perp\) we add an edge \(((k,B[k,j]),j)\in K_2\times J\). Finally, add all edges \(((k,x_1),(k,x_2))\in K_1\times K_2\).<tbc>

• _(Node Weights)_ Let \(u=max_{x\in X}|x|\). All nodes in _I_ and _J_ have weight 10_u_. All nodes (_k,x_) in _K_<sub>1</sub> and _K_<sub>2</sub> have weight 10_u+x_.

We compute the pairwise distances in _G_ in time \(O(n^{2.5-\epsilon})\), and claim that the resulting distances between any pair of nodes \(i\in I\) and \(j\in J\) is exactly (_A∗B_)\[_i,j_\]+40_u_. Indeed, whenever _k_ is a witness of (_A∗B_)\[_i,j_\] then the nodes \((i,(k,A[i,k]),(k,B[k,j]),j)\in I\times K_1\times K_2\times J\) form a path of weight

\(10u+(10u+A[i,k])+(10u+B[k,j])+10u=(A*B)[i,j]+40u.\)

Conversely, all _i-j_-paths of weight less than 42_u_ necessarily have at most 3 edges, and thus have the form \((i,(k',w_1),(k',w_2),j)\in I\times K_1\times K_2\times J\). But then \(A[i,k']=x_1\) and \(B[k',j]=x_2\), and thus \((A*B)[i,j]\le w_1+w_2\).

We finally characterize the complexity of node-weighted APSP in graphs with small weights {0_,...,u_} (conditioned on the Strong APSP Hypothesis). The characterization of directed graphs is easy: Even for unweighted directed graphs (i.e., _u_=1) we cannot beat time _O(n_<sup>2.5</sup>) without breaking the Strong APSP Hypothesis (Theorem 1.7).

For node-weighted graphs, the fastest-known APSP algorithm runs in time \(\tilde{O}(min\{n^{(3+\omega)/2},n^\omega u\})\) (up to improvements from rectangular matrix multiplication), by combining the \(\tilde{O}(n^{(3+\omega)/2})\)-time algorithm for general node weights by \[4\], with Shoshan and Zwick’s \(\tilde{O}(n^\omega u)\)-time algorithm for small edge weights \[90\]. We show that this time is optimal (if \(\omega=2\)), conditioned on the Strong APSP Hypothesis:

**Theorem 6.1** (Node-Weighted APSP with Small Weights)**.** _Let_ \(\delta\ge 0\)_. APSP in undirected node-weighted graphs with weights in_ \(\{0,\dots,n^\delta\}\) _cannot be solved in time_ \(O(n^{min\{2.5,2+\delta\}-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong APSP Hypothesis fails._

**Proof.** The statement is trivially true for \(\delta=0\) (as it is impossible for any subquadratic-time algorithm to write down the _n_<sup>2</sup> pairwise distances). So suppose that \(\delta>0\), and choose \(\alpha=min\{1/2,\delta\}>0\).

We show that an \(O(n^{min\{2.5,2+\delta\}-\epsilon})=O(n^{2+\alpha-\epsilon})\)-time algorithm for undirected node-weighted APSP implies that \(MinPlus(n,n^\alpha,n|u\le n^\alpha)=O(n^{2+\alpha-\epsilon})\), which contradicts the Strong APSP Hypothesis by Corollary 5.4. For this reduction we mimic the proof of Theorem 1.14 almost exactly. Specifically, given matrices _A,B_ of sizes \(n\times n^\alpha\) and \(n^\alpha\times n\) with entries bounded by \(u=n^\alpha\), we construct the same undirected graph on the four vertex parts \(I=[n],K_1=[n^\alpha]\times X,K_2=[n^\alpha]\times X,J=[n]\), where _X_={0_,...,u_} denotes the set of weights. Analogously, the number of nodes is at most \(|I|,|J|\le n\) and \(|K_1|,|K_2|\le O(n^{2\alpha})\le O(n)\), and the _I-J_-distances encode the min-plus product _A∗B_. Notably, this time the node weights are bounded by \(O(u)=O(n^\alpha)\). Therefore, we can solve this constructed instance in time \(O(n^{2+\alpha-\epsilon})\), leading to the desired contradiction.

## 6.2 Min Product

Min Product is a particularly simple intermediate matrix product problem, equivalent to the restriction of Min-Plus Product where one matrix consists only of entries \(\{0,\perp\}\). This problem was studied before in \[4\] (under the name _Boolean_ Min-Plus Product). While perhaps not as important in its own right, one can easily conclude the hardness of other intermediate problems from the hardness of Min Product.

**Definition 6.2** (Min Product)**.** _The_ min product _of two matrices_ \(A\in\mathbb{Z}^{n\times n}\) _and_ \(B\in\{0,1\}^{n\times n}\) _is the matrix_ \(C\in\mathbb{Z}^{n\times n}\) _defined by_

\(C[i,j]=min_{k\in[n]B[k,j]=1}A[i,k].\)

_The_ Min Product _problem is to compute the min product of two given matrices A,B._

