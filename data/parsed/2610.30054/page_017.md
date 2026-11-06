whose tensor _T_ is \(\mathsf{P}_{a,b}\oplus_1\mathsf{P}_{a,b}\). Let _V_<sub>1</sub> be the image of \(\iota_b\) and _W_<sub>1</sub> the image of \(\iota_{a+b-1}\). We claim<tbc>

\(\mu(\mathcal{W}_{a-1}\times V_1)\subseteq W_1.\)

<tbc>This claim will let us apply Lemma 2.5. Indeed, for all \(f\in\mathcal{W}_{a-1}\) and \(p\in\mathcal{W}_{b-2}\),<tbc>

\(\mu\big(f,\iota_b(p)\big)=(-tfp,fp)=\iota_{a+b-1}(fp).\) (3.3)

<tbc>By Lemma 2.5, \(T\unknown_1T_1\oplus_1T_2\) for the tensors _T_<sub>1</sub> and _T_<sub>2</sub> of the bilinear maps

\(\mu_1:\mathcal{W}_{a-1}\times(V/V_1)\rightarrow(W/W_1)\text{and}\mu_2:\mathcal{W}_{a-1}\times V_1\rightarrow W_1\)

induced by \(\mu\). It remains to show that \(T_1\cong\mathsf{P}_{a,b+1}\) and \(T_2\cong\mathsf{P}_{a,b-1}\).

For _T_<sub>2</sub> this follows from (3.3), where we identify \(\mathcal{W}_{b-2}\cong V_1\) using the isomorphism \(\iota_b:\mathcal{W}_{b-2}\rightarrow V_1\), and similarly \(\mathcal{W}_{a+b-3}\cong W_1\).

For _T_<sub>1</sub> we use that the maps \(\sigma_b\) and \(\sigma_{a+b-1}\) are surjective with kernels _V_<sub>1</sub> and _W_<sub>1</sub>, so they induce isomorphisms from the quotients to W_<sub>b</sub>_ and W<sub>_a+b_-1</sub>. Since

\(\sigma_{a+b-1}\big(\mu(f,(g,h))\big)=fg+tfh=f\sigma_b(g,h)\)

for all \(f\in\mathcal{W}_{a-1}\) and \(g,h\in\mathcal{W}_{b-1}\), these isomorphisms identify the induced map \(\mu_1\) on the quotients with the multiplication map \(\mathcal{W}_{a-1}\times\mathcal{W}_b\rightarrow\mathcal{W}_{a+b-1}\), whose tensor is P<sub>_a,b_+1</sub>.

We now give the second proof, over C, which is insightful for readers familiar with representation theory. For \(d\ge 1\) let \(\mathcal{V}_d:=\mathrm{Sym}^d\mathbb{C}^2\subseteq(\mathbb{C}^2)^{\otimes d}\) be the subspace of symmetric tensors of order _d_ and let V<sub>0</sub>:=C. Then V_<sub>d</sub>_ is an irreducible SL<sub>2</sub>(C) representation under the diagonal action \(g\mapsto g^{\otimes d}\) of SL<sub>2</sub>(C), and its dual \(\mathcal{V}_d^*\) is isomorphic to the space C\[_x,y_\]_<sub>d</sub>_ of homogeneous polynomials of degree _d_ as an SL<sub>2</sub>(C) representation (see Fulton and Harris \[FH91, Chapter 11\]). We can identify \(\mathbb{C}[t]_{\le d}\) with C\[_x,y_\]_<sub>d</sub>_ via homogenization \(t^k\mapsto x^ky^{d-k}\). Under this identification, the polynomial multiplication tensor P<sub>_a,b_</sub> by definition describes the (bilinear) multiplication map \(\mathbb{C}[x,y]_{a-1}\times\mathbb{C}[x,y]_{b-1}\rightarrow\mathbb{C}[x,y]_{a+b-2}\). This map is SL<sub>2</sub>(C) equivariant. Under the standard identification of bilinear maps with tensors we have that \(\mathsf{P}_{a,b}\in\mathcal{V}_{a-1}\otimes\mathcal{V}_{b-1}\otimes\mathcal{V}_{a+b-2}^*\). Because this identification is SL<sub>2</sub>(C) equivariant, we obtain that P<sub>_a,b_</sub> is invariant under the diagonal SL<sub>2</sub>(C) action, that is, \(\mathsf{P}_{a,b}\in(\mathcal{V}_{a-1}\otimes\mathcal{V}_{b-1}\otimes\mathcal{V}_{a+b-2}^*)^{\mathrm{SL}_2(\mathbb{C})}\).

**Lemma 3.7.** _Let_ \(i,j\ge 0\) _be integers. We have that_ \(\mathcal{V}_i\otimes\mathcal{V}_j\cong\oplus_{k=0}^{\mathrm{min}(i,j)}\mathcal{V}_{i+j-2k}\)_. In particular, for every integer_ \(\ell>i+j\), \((\mathcal{V}_i\otimes\mathcal{V}_j\otimes\mathcal{V}_\ell^*)^{\mathrm{SL}_2(\mathbb{C})}=0\) _and_ \((\mathcal{V}_i\otimes\mathcal{V}_j\otimes\mathcal{V}_{i+j}^*)^{\mathrm{SL}_2(\mathbb{C})}=\mathbb{C}\mathsf{P}_{i+1,j+1}\).

_Proof._ The first statement is standard, see e.g. \[FH91, Exercise 11.11\]. The two equalities follow from the standard identification of SL<sub>2</sub>(C)-equivariant linear maps \(\mathcal{V}_\ell\rightarrow\mathcal{V}_i\otimes\mathcal{V}_j\) with \((\mathcal{V}_i\otimes\mathcal{V}_j\otimes\mathcal{V}_\ell^*)^{\mathrm{SL}_2(\mathbb{C})}\): by the first statement, \(\mathcal{V}_\ell\) with \(\ell>i+j\) does not occur in \(\mathcal{V}_i\otimes\mathcal{V}_j\) and V<sub>_i+j_</sub> occurs once, so Schur’s lemma tells us the two spaces have dimension 0 and 1 respectively; the second equality follows because \(\mathsf{P}_{i+1,j+1}\in(\mathcal{V}_i\otimes\mathcal{V}_j\otimes\mathcal{V}_{i+j}^*)^{\mathrm{SL}_2(\mathbb{C})}\).

_Proof of Lemma 3.6 over_ C. By Lemma 3.4, we have<tbc>

\(\mathsf{P}_{a,b}\oplus_1\mathsf{P}_{a,b}\cong\mathsf{P}_{a,b}\otimes\mathsf{P}_{1,2}\in\big((\mathcal{V}_{a-1}\otimes\mathcal{V}_0)\otimes(\mathcal{V}_{b-1}\otimes\mathcal{V}_1)\otimes(\mathcal{V}_{a+b-2}^*\otimes\mathcal{V}_1^*)\big)^{\mathrm{SL}_2(\mathbb{C})}.\)

<tbc>Since V<sub>0</sub>=C, we have \(\mathcal{V}_{a-1}\otimes\mathcal{V}_0=\mathcal{V}_{a-1}\). By Lemma 3.7 we know that \(\mathcal{V}_d\otimes\mathcal{V}_1\cong\mathcal{V}_{d+1}\oplus\mathcal{V}_{d-1}\) as SL<sub>2</sub>(C) representations, for every integer \(d\ge 1\). Thus, there exist SL<sub>2</sub>(C)-equivariant isomorphisms \(B:\mathcal{V}_{b-1}\otimes\mathcal{V}_1\rightarrow\mathcal{V}_b\oplus\mathcal{V}_{b-2}\) and \(C:\mathcal{V}_{a+b-2}^*\otimes\mathcal{V}_1^*\rightarrow\mathcal{V}_{a+b-1}^*\oplus\mathcal{V}_{a+b-3}^*\) such that<tbc>

\(T:=(I\otimes B\otimes C)(\mathsf{P}_{a,b}\otimes\mathsf{P}_{1,2})\in\big(\mathcal{V}_{a-1}\otimes(\mathcal{V}_b\oplus\mathcal{V}_{b-2})\otimes(\mathcal{V}_{a+b-1}^*\oplus\mathcal{V}_{a+b-3}^*)\big)^{\mathrm{SL}_2(\mathbb{C})}\) (3.4)

