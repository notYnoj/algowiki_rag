<tbc>Proof of Proposition 3.8. Since \(\sum_iv_i=0\) and \(\sum_iv_i=0(modn)\), by Proposition 3.9, we may efficiently write **v** as the sum of (1,-1,-1,1) vectors with indices of the form (_a,b,c,b+c-a_). Each of these vectors can be obtained from a simple matrix, for example that indexed by _a_ and _b_ in the rows, and 0 and _c-a_ in the columns. Thus **v** has a decomposition as simple matrices and so \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T}')\). □

It is worth noting here that the simple matrix yielding \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T}')\) with \(supp(\mathbf{v})=\{a,b,c,b+c-a\}\) is not unique. This will be relevant when we consider sub-lattices of T . We finish the discussion of \(\mathcal{L}_1^{X+Y}(\mathcal{T}')\) with a final proposition.

Proposition 3.10. _The collection of vectors with weights_ (1,-1,-1,1) _and indices of the form_ (_a,b,c,b+c-a_) _is generating for_ \(\mathcal{L}_1^{X+Y}(\mathcal{T}')\).

Proof. The collection of such vectors is generating if and only if any \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T}')\) can be written as the sum of such vectors. Fix \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T}')\). By Proposition 3.7, \(\sum_iv_i=0\) and \(\sum_iv_i=0(modn)\), and thus by Proposition 3.9 we are done. □

Remark 3.11. It is worth noting that a similar approach works to yield a generating set for \(\mathcal{L}_1^J(\mathcal{T}')\) for any _J_. Indeed, if we start with an \(n\times n\) matrix where rows correspond to vertices from _V_ <sup>_X+Y_</sup> and columns correspond to vertices from _V<sup>Y</sup>_, then integer combinations of simple matrices will yield all possible combinations where the total weight on each coordinate in _V_ <sup>_X+Y_</sup> and _V<sup>Y</sup>_ is identically zero, and the weights given to coordinates in _V<sup>X</sup>_ can be obtained from taking the differences down the forward diagonals (i.e. if (_a,b_) has entry _c_ in the \(n\times n\) matrix, then this entry adds weight _c_ to \(a-b\in V^X\), and clearly shifting up and down the forward diagonal containing (_a,b_) we have entries \((a+\delta,b+\delta)\), where \(\delta\in[0,n-1]\), and these entries contribute their weight to \((a+\delta)-(b+\delta)=a-b\in V^X\) too).

We may also deduce the following lemma about \(\mathcal{L}(\mathcal{T}')\).

Lemma 3.12. \(\mathbf{v}\in\mathcal{L}(\mathcal{T}')\) _if and only if the following both hold:_

(_i)_ \(\sum_iv_i^X=\sum_iv_i^Y=\sum_iv_i^{X+Y}\),<tbc>

_(ii)_ \(\sum_iv_i^X+\sum_iv_i^Y=\sum_iv_i^{X+Y}mod(n)\).

Proof. Considering an edge \(e\in\mathcal{T}'\) we have that the vector \(\mathbf{v}\in\mathcal{L}(\mathcal{T}')\) associated to the edge _e_ satisfies (i) and (ii). Thus the associated vector of any linear combination of edges will also satisfy (i) and (ii), which by definition covers all \(\mathbf{v}\in\mathcal{L}(\mathcal{T}')\). Considering now a vector **v** such that (i) and (ii) hold we may modify **v** to **u** by adding the shadow vectors of edges in such a way as to make \(\mathbf{u}^\mathbf{X},\mathbf{u}^\mathbf{Y}\equiv\mathbf{0}\). But adding these edges will force \(\sum_iu_i^{X+Y}=0\) and \(\sum_iu_i^{X+Y}=0mod(n)\). Thus by Proposition 3.8 we have that \(\mathbf{u}\in\mathcal{L}_1^{X+Y}(\mathcal{T}')\), so **u** can be seen as the vertex shadow of a linear combination of edges of \(\mathcal{T}'\). But since **v** can be obtained from **u** by removing edges, we must then also have that \(\mathbf{v}\in\mathcal{L}(\mathcal{T}')\). □

We previously mentioned that \(\mathcal{T}'(n)\) has a perfect matching only if _n_ is odd. We show that this can be deduced from the above understanding of the lattice.

Corollary 3.13. _Suppose that_ \(\mathcal{T}'(n)\) _has a perfect matching. Then n is odd._

Proof. Suppose that \(\mathcal{T}'(n)\) has a perfect matching. Then \(\mathbf{1}\in\mathcal{L}(\mathcal{T}')\). By Lemma 3.12 we have that \(\sum_iv_i^X=\sum_iv_i^Y=\sum_iv_i^{X+Y}\) and \(\sum_iv_i^X+\sum_iv_i^Y=\)

