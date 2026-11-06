## Max-Variant of the Matching Problem for the Supersequence Relation.

Given an instance of UOV with sets of vectors \(U=\{u_1,\dots,u_n\},V=\{v_1,\dots,v_t\}\subseteq\{0,1\}^d\) we define \(Z=\Pi_{j\in[d]}c_j\) and the following two functions that operate on binary vectors:

\(F(v)=\Pi_{j\in[d]:v[j]=1}c_j\)<br>
\(G(u)=\left(\Pi_{j\in[d]:u[j]=0}c_j\right)\$^{1+\|u\|_1}\)

Note that \(F(v)\unknown_\mathsf{sub}Z\) so MaxSup(_F(v),Z_)=|_Z_|=_d_. Further observe that \(F(v)\unknown_\mathsf{sub}G(u)\Longleftrightarrow v\perp u\), so if \(v\perp u\) we have MaxSup(_F(v),G(u_))=|_G(u_)|=_d_+1.

Consider the regular expression \(Y:=Z\vee G(u_1)\vee G(u_2)\dots\vee G(u_n)\). Then we have:

\(\mathsf{MaxSup}(F(v),Y)=d+\unknown[\exists_{i\in[n]}v\perp u_i],\) (1)

where the function \(\unknown\) is defined as \(\unknown[\mathcal{P}]\) equals 1 if the predicate P holds, and 0 otherwise.

We now use Claim 7.7 to combine our construction for various vectors _v_ in such a way that they do not affect each other. Let _w=F(v_<sub>1</sub>)#_F(v_<sub>2</sub>)#_...F(v<sub>t</sub>_)# and _R_=(_Y_#)_<sup>t</sup>_. In order to avoid clutter, whenever _i_ is not quantified, we mean \(i\in[t]\). Then we have:

\(\mathsf{MaxSup}(w,R)=\mathsf{MaxSup}\left(\Pi_i(F(v_i)\#),\Pi_i(Y\#)\right)\text{(definition of}w\text{and}R\text{)}\)<br>
\(=\sum_i(\mathsf{MaxSup}\left(F(v_i),Y\right)+1)\text{(Claim 7.7)}\)<br>
\(=\sum_i\left(d+\unknown[\exists_{k\in[n]}v_i\perp u_k]+1\right)\text{(Equation 1)}\)<br>
\(=t(d+1)+|\{i:\exists_{k\in[n]}v_i\perp u_k\}|\)

To conclude, there exists an orthogonal pair of vectors \((u,v)\in U\times V\) iff MaxSup(_w,R)\>t(d_+1).

Now suppose that there exists an algorithm that solves the max-variant of the matching problem for the supersequence relation in time \(O((|w||R|)^{1-\epsilon})\) for some \(\epsilon>0\). As |_w_|=_O(td_) and |_R_|=_O(ntd_), this yields an algorithm for UOV in time \(O((nt^2d^2)^{1-\epsilon})=O(n^{(1+2\alpha)(1-\epsilon)}\mathrm{poly}(d))\). Choosing \(\alpha:=\epsilon/2\) we obtain an algorithm for UOV that runs in time \(O(n^{(1+\epsilon)(1-\epsilon)}\mathrm{poly}(d))=O(n^{1+\alpha-(\alpha+\epsilon^2)}\mathrm{poly}(d))\) which violates UOVH. This concludes the proof for the case of non- constant-size alphabets.

## Constant-Site Alphabet.

Now we show how to adjust the above construction to operate on constant-size alphabets. Note that the only strings containing characters _c<sub>⋆</sub>_ in their definition are _Z,F(v_), and _G(u_) where both _F(v_) and the prefix of _G(u_) before $’s are subsequences of _Z_.

Let \(\Sigma'=\{0,1,\$,\#\}\) and define a function \(\delta\) by \(\delta(1):=10\) and \(\delta(0):=0\). We define \(Z':=(\delta(1))^d=(10)^d\), \(F'(v)=\Pi_{j\in[d]}\delta(v[j])\), and \(G'(u):=\left(\Pi_{j\in[d]}\delta(\neg u[j])\right)\$^{1+\|u\|_1}\) where \(\neg x=1-x\) is the negation of a bit. Similarly as in Claim 7.7, now the 0’s serve as separators that ensure that 1’s are matched only between the corresponding positions, because we have the same number of 0’s in \(Z',F'(v)\) and \(G'(u)\).

Note that we have \(F'(v)\unknown_\mathsf{sub}Z'\) and \(\mathsf{MaxSup}(F'(v),Z')=|Z'|=2d\). Next, we have \(F'(v)\unknown_\mathsf{sub}G'(u)\Longleftrightarrow v\perp u\), so if \(v\perp u\) we have \(\mathsf{MaxSup}(F'(v),G'(u))=|G'(u)|=2d+1\). We define \(Y',w'\) and \(R'\) as before, but now using the new expressions \(Z',G'\) and \(F'\). Then, \(\mathsf{MaxSup}(F'(v),Y')=2d+\unknown[\exists_{i\in[n]}v\perp u_i]\) and finally \(\mathsf{MaxSup}(w',R')=t(2d+1)+|\{i:\exists_{k\in[n]}v_i\perp u_k\}|\). The result of the running time analysis is unchanged for the new construction. This concludes the proof for the case of constant-size alphabet \(\Sigma'=\{0,1,\$,\#\}\) for the max-variant of the matching problem for the supersequence relation.

## Min-Variant of the Matching Problem for the Subsequence Relation.

The reduction for this problem will be a slight adjustment of the reduction from the previous paragraphs. Again we start with the construction for non-constant size alphabets. Given an instance of UOV, we<tbc>

