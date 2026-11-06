can enforce all shared labels simultaneously, with the number of blocks and the dimension of the retained edge chosen independently.

**Lemma 5.4** (separation with a polynomial resource)**.** _Let_ \(m,t\ge 1\) _be integers, and let_ \(X_0,\dots,X_{m-1}\in\mathcal{F}_n\) _have equal dimensions on their first n_-2 _legs. Put e_=(_n_-1_,n_) _and_ \(A=X_0\boxplus_e\cdots\boxplus_eX_{m-1}\)_. Then_<tbc>

\(\mathrm{ev}\left(\left(\oplus_{h=0}^{m-1}X_h\right)\otimes_K\mathbf{E}_{n-1,n}^{(t)}\right)\unknown\mathrm{ev}\left(A\otimes_K\mathsf{C}_n(\underbrace{m,\dots,m}_{n-2},t)\right).\)

<tbc>_Proof._ Put \(\ell=n-2\). Reverse the last coordinate of the auxiliary polynomial atom, so that its supported indices satisfy

\(v=g_1+\cdots+g_\ell+u,0\le g_j<m(1\le j\le\ell),0\le u<t.\)

Its last dimension is \(\ell(m-1)+t\). In the matched-block representative of ev(_A_), write \(h\in[m]_0\) for the common block label on the last two legs. A shared-leg coordinate of the product consists of an original coordinate and a label _g<sub>j</sub>_. The last two coordinates include, respectively, (_h,u_) and (_h,v_), in addition to their original within-block indices.

Assign weight \(g_j^2\) on shared leg _j_, weight \(2hu+\ell h^2\) on leg _n_-1, and weight -2_hv_ on leg _n_. The total weight of every supported term is

\(\sum_{j=1}^\ell g_j^2+2hu+\ell h^2-2hv=\sum_{j=1}^\ell(g_j-h)^2.\)

It is nonnegative, and it vanishes precisely when _g<sub>j</sub>=h_ for every \(1\le j\le\ell\). The retained terms then satisfy \(v=u+\ell h\). Thus every shared leg acquires the block label _h_, and the additional index \(u\in[t]_0\) is shared only by the last two legs.

On the last leg and within block _h_, keep exactly the auxiliary coordinates \(v=\ell h,\dots,\ell h+t-1\), and relabel them by \(u=v-\ell h\). Project all unused coordinates to zero. On each shared leg, reorder the pair consisting of the old coordinate and _g<sub>j</sub>=h_ so that _h_ is the block label. These maps retain every term of weight zero, with its original coefficient, and give the full direct sum of \(\mathrm{ev}(X_h)\otimes_KE_{n-1,n}^{(t)}\) over \(h\in[m]_0\). The edge atom in the statement has the same tensor class as this edge tensor. Composing the weight degeneration with the projections and coordinate permutations proves the claim.

## 5.2 Permitted derivations and their soundness

The preceding lemma gives a tensor comparison for every permitted choice of blocks. We now fix the rules by which this comparison and the polynomial constructions may be combined. Listing these rules explicitly is essential: validity of two tensor evaluations alone does not authorize replacement inside a partial sum with shared coordinates.

**Definition 5.5** (permitted polynomial derivations)**.** Let \(\unknown_{\mathrm{poly},n}\) be the least reflexive and transitive relation on F_<sub>n</sub>_ with the rules below. In this definition, \(X\doteq Y\) means that both \(X\unknown_{\mathrm{poly},n}Y\) and \(Y\unknown_{\mathrm{poly},n}X\) are rules. All expressions must satisfy the dimension requirements in Definition 5.2.

(i) _Full combinations and leg permutations._ If \(X\unknown_{\mathrm{poly},n}Y\) and \(U\unknown_{\mathrm{poly},n}V\) , then<tbc>

<tbc>\(X\oplus_KU\unknown_{\mathrm{poly},n}Y\oplus_KV,X\otimes_KU\unknown_{\mathrm{poly},n}Y\otimes_KV.\)<tbc>

