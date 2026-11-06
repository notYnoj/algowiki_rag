_Proof._ For each _j_, the expression in brackets is (_x_<sub>1</sub>+_x_<sub>2</sub>)_y<sub>j</sub>+x_<sub>1</sub>_q<sub>j</sub>+p<sub>j</sub>q<sub>j</sub>_. Summing over _j_, the first terms cancel the subtracted product, the second sum to zero because _q_<sub>1</sub>+_q_<sub>2</sub>+_q_<sub>3</sub>=0, and the last sum to _p_<sub>1</sub>_q_<sub>1</sub>+_p_<sub>2</sub>_q_<sub>2</sub> because _p_<sub>3</sub>=0.

Note that the variables _x<sub>i</sub>,y<sub>j</sub>_ can be arbitrary: the identity always recovers the same two-term dot product. We will choose them so that the six positive products for different outputs belong to one small collection.

## The shared products.

Fix the integer \(k\ge 2\) from Theorem 2.3 for the rest of this construction. Recall that _R=k_2<sup>_k_-1</sup> and _S_=3<sup>_k_-1</sup>, and let \(U\in\mathbb{Z}^{R\times 2}\) and \(V\in\mathbb{Z}^{2\times S}\). Label the rows of _U_ by (_h,u_), with \(h\in[k]\) and \(u\in\{1,2\}^{k-1}\), and the columns of _V_ by \(v\in\{1,2,3\}^{k-1}\). To match the three values of _j_ in Theorem 2.4, extend the entry notation by

\(U_{(h,u),3}=0,V_{3,v}=-V_{1,v}-V_{2,v}.\)

These are abbreviations for linear forms in the original entries.

For a tuple _a_ of length _k_, write \(a_{-\ell}\) for the tuple obtained by deleting coordinate \(\ell\), keeping the others in their original order. For example, (_a_<sub>1</sub>_,a_<sub>2</sub>_,a_<sub>3</sub>)<sub>-2</sub>=(_a_<sub>1</sub>_,a_<sub>3</sub>).

For each \(a\in\{1,2\}^k\) and \(b\in\{1,2,3\}^k\), define

\(A_{a,b}=\sum_{\ell=1}^k(-1)^{a_\ell-1}U_{(\ell,a_{-\ell}),b_\ell},B_{a,b}=\sum_{\ell=1}^k\mathbf{1}_{a_\ell=1}V_{b_\ell,b_{-\ell}}.\) (5)

Here \(\mathbf{1}_{a_\ell=1}\) is 1 if \(a_\ell=1\) and 0 otherwise. Our shared collection consists of the 6_<sup>k</sup>_ products _A<sub>a,b</sub>B<sub>a,b</sub>_. Each multiplies a linear form in _U_ by a linear form in _V_ .

The output ((_h,u),v_) uses the six products whose labels satisfy _a_<sub>-_h_</sub>=_u_ and _b_<sub>-_h_</sub>=_v_. Only the pair (_a<sub>h</sub>,b<sub>h</sub>_) varies, so these labels form a six-point coordinate line. Each label belongs to one such line for each \(h\in[k]\); thus each shared product serves _k_ outputs. Figure 2 illustrates this pattern for _k_=2.

Along this line, the \(\ell=h\) terms in equation (5) supply the entries of the desired dot product. The remaining terms play the roles of _x<sub>i</sub>,y<sub>j</sub>_ in Theorem 2.4, so one private product cancels their contribution. We verify this next.

j = 1
j = 2
j = 3
i = 1
(x1 + p1)(y1 + q1)
(x1 + p2)(y2 + q2)
(x1 + p3)(y3 + q3)
i = 2
(x2 - p1)y1
(x2 - p2)y2
(x2 - p3)y3
sum all six
+
x1(q1 + q2 + q3)
+
P1q1 + p2q2
Removed by subtracting one private product
Zero by the zero-sum relation
The desired dot product
Removed by subtracting one private product

Figure 1: The six products in equation (4) and their sum, with _p_<sub>3</sub>=0 and _q_<sub>1</sub>+_q_<sub>2</sub>+_q_<sub>3</sub>=0. Subtracting one private product leaves the desired dot product.

