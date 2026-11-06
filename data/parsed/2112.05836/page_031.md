<tbc>_Proof._ Consider the _k_-1 lists \(\mathbf{Vec}\mathbf{S}_{\mathbf{I}\ell}(L,v_i)\) for \(i\in[1,k-1]\). Additionally, let

\(Vec_E(v_k)[j]=\left\{\begin{array}{ c c }
v_k[h] & \text{if}j=h\cdot n^\ell \\
0 & \text{else.}
\end{array}\right.\)

Where the total length is \(|Vec_E(v_k)|=n^\ell\cdot(d-1)+1\).

Now create the lists<tbc>

\(X_i[j]=CG_i(\mathbf{Vec}\mathbf{S}_{\mathbf{I}\ell}(L,v_i)[j])\)

\(Y[j]=CG_k(Vec_E(v_k)[j]).\)

<tbc>Finally create the strings

\(IVG_i(L,\ell,v_1)=SAG_i(X_i)\)

\(EIVG(v_k)=SAG_y(Y).\)

Now, note that by construction the _k_-LCS of coordinate gadgets \(CG_i(\cdot)\) is either some value _z_ or _z_+1.

Now, note that _Vec<sub>E</sub>(v<sub>k</sub>_) has zeros in every location except \(h\cdot n^\ell\) for \(h\in[1,d]\). If we perfectly align _Vec<sub>E</sub>(v<sub>k</sub>_) with the (_k_-1) vectors \(\mathbf{Vec}\mathbf{S}_{\mathbf{I}\ell}(L,v_i)\), then these locations correspond with a vector in each! That is, as mentioned in Definition 6.8, the bits in locations \(j,j+n^\ell,\dots,j+(d-1)n^\ell\) correspond to a vector _w_ where _w_\[_h_\]=_u_\[_h_\]_v<sub>i</sub>_\[_h_\] and _u=List_\[_h_\]. If there are \((k-1)\ell\) vectors in _L_ that are orthogonal with _v_<sub>1</sub>_,...,v<sub>k</sub>_, then there should be a perfect alignment of these vectors such that in every alignment location there is at least one zero. That is, an alignment where every aligned _k_-tuple has a LCS of _z_+1 as opposed to _z_.

Let \(c=|CG_i(\cdot)|\). Let _z_+1 be the value of \(\delta_LCS(CG_1(b_1),\dots,CG_k(b_k))\) if \(b_1\cdots b_k=0\). So \(\delta_LCS(CG_1(b_1),\dots,CG_k(b_k))=z\) if \(b_1\cdots b_k=0\).

So, by Theorem 6.11, if there are \((k-1)\ell\) vectors in _L_ that are orthogonal with _v_<sub>1</sub>_,...,v<sub>k</sub>_ then<tbc>

\(\text{LCS}(IVG_1(L,\ell,v_1),\dots,EIVG(v_k))=C=2c(2((d-1)n^\ell+1)+(k-1)dn^\ell)+(z+1)((d-1)n^\ell+1).\)

<tbc>Otherwise,

\(\text{LCS}(IVG_1(L,\ell,v_1),\dots,IVG_{k-1}(L,\ell,v_{k-1}),EIVG(v_k))=C-1.\)

Now we are going to argue that we can compress _x_ strings \(IVG_i(L,\ell,v_1),\dots,IVG_i(L,\ell,v_x)\) or _EIVG(v_<sub>1</sub>)_,...,EIVG(v<sub>x</sub>_) with a total compression size of _O(xd+nd_). First, note that \(A_{-i}^f\) can be represented with an SLP of size \(O(lg(\ell)+lg(n))\). Now the rest of our string is a series of entries that look like \(A\cdot CG_i(b)\cdot B\). We can create a SLP for both \(S_0=A\cdot CG_i(0)\cdot B\) and \(S_1=A\cdot CG_i(1)\cdot B\) with size \(O(lg(\ell))\). We give the names of _S_<sub>0</sub>_,S_<sub>1</sub> to simplify the notation.

Next, if we are compressing _x_ different _EIVG(v<sub>i</sub>_) gadgets, first we want to compress \(S_0^{n^\ell-1}\) which appears repeatedly. We can do this with size \(O(\ell lg(n))\). Finally, we need to add the bits that correspond with each vector. We can do this with size _dx_. This gives a total size of \(O(\ell lg(n)+dx)\).

Finally, consider the case of compressing _x_ different \(IVG(L,\ell,v_j)\) gadgets. This part of the proof, where interleaves are very compressible, borrows very heavily from \[ABBK17\]. For this we note first that \(\mathbf{Vec}\mathbf{S}_{\mathbf{I}\ell}(L,v_j)\) has _d_ sections of size \(n^\ell\) that correspond to the _d_ dimensions of the vectors. Any section that corresponds to a _h_ where _v<sub>j</sub>_\[_h_\]=0 has \(n^\ell\) copies of _S_<sub>0</sub>. This can be represented with size \(O(\ell lg(n))\). When _v<sub>j</sub>_\[_h_\]=1 the section instead corresponds to \(\circ_{j\in[1,n^\ell]}\mathbf{List}[j][h]\). By using Definition 6.6 we can re-write this as

\(\mathbf{SubList}[L,k]=\circ_{j_1\in[1,n]}\circ_{j_2\in[1,n]}\circ_{j_3\in[1,n]}\cdots\circ_{j_k\in[1,n]}L[j_1][i]\cdot L[j_2][i]\cdots L[j_k][i].\)

Now note that **SubList**\[_L,_1\] is simply a string of _n_ bits and thus has a compression of size _n_. Now note that **SubList**\[_L,g_\] is simply a string formed by appending either **SubList**\[_L,g_-1\] or _n_<sup>_g_-1</sup> zeros. We can represent _n_<sup>_g_-1</sup> zeros with _O(g_lg(_n_)) variables. So, if **SubList**\[_L,g_\] has an SLP _f(g_) then **SubList**\[_L,g_+1\] has an SLP _f(g_+1)=_n+f(g_)+_g_lg(_n_). We have that _f_(1)=_n_, so _f(k_)=_kn+k_<sup>2</sup>lg(_n_)=_O(n_). Thus, the total size of compressing _x_ different \(IVG(L,\ell,v_j)\) gadgets is \(O(\ell lg(n)+dx+dn)\).

