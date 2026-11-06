shortest path _P_ from _u<sub>i</sub>_ to _v_<sub>_j_+1</sub> and a shortest path _Q_ from _u_<sub>_i_+1</sub> to _v<sub>j</sub>_; see Figure 5. As these four vertices lie in the order _u<sub>i</sub>,u_<sub>_i_+1</sub>_,v_<sub>_j_+1</sub>_,v<sub>j</sub>_ on the outer face of _G_ (some of these vertices may coincide with each other), the paths _P_ and _Q_ intersect at a common vertex \(w\in V(G)\). As _P_ and _Q_ are shortest paths, we have

\(D_{i,j+1}+D_{i+1,j}=(dist_G(u_i,w)+dist_G(w,v_{j+1}))+(dist_G(u_{i+1},w)+dist_G(w,v_j))\)<br> \(=(dist_G(u_i,w)+dist_G(w,v_j))+(dist_G(u_{i+1},w)+dist_G(w,v_{j+1}))\)<br> \(\ge D_{i,j}+D_{i+1,j+1}.\blacktriangleleft\)

We now show that the matrix _M<sup>s</sup>_ contains all range LIS values.

\(\blacktriangleright\) **Lemma B.8.** _For a subpermutation s of length n and any_ \(i,j\in[0..n]\)_, we have_

\(M_{i,j}^s=\left\{\begin{array}{ c c }
\mathsf{LIS}(s[i..j)), &  \\
-2\cdot(i-j), & 
\end{array}\right.\)

_Furthermore, all corresponding longest paths are monotone in both coordinates._

**Proof.** First, assume that \(i\ge j\). Consider some path _P_ from (_i,_0) to (_j,|s_<sup>∗</sup>|). Let _k_ be the number of edges of the third type from Definition B.4 on this path, and \(\ell\) be the number of edges of the fourth type on this path. As edges of the first two types have weights zero, the length of _P_ is \(k-2\ell\). Note that the first coordinate of the vertex along the path _P_ is increased by at least _k_ and decreased by at least (_i-j_)+_k_. Only edges of the fourth type decrease the first coordinate of the current vertex, so \(\ell\ge(i-j)+k\). Therefore, the length of _P_ is at most \(k-2\cdot((i-j)+k)=-2\cdot(i-j)-k\le-2\cdot(i-j)\). Furthermore, there exists a path of length exactly \(-2\cdot(i-j)\): it first takes vertical edges of weight 0 from (_i,_0) to (_i,|s_<sup>∗</sup>|), and then horizontal backward edges of weight -2 from (_i,|s_<sup>∗</sup>|) to (_j,|s_<sup>∗</sup>|). Therefore, \(M_{i,j}^S=-2\cdot(i-j)\). The only way to achieve this length is for _k_=0, and thus any such longest path is monotone in both coordinates.

We now consider the case _i\<j_. Let _P_ be the longest path from (_i,_0) to (_j,|s_<sup>∗</sup>|). We first show that _P_ is monotone in both coordinates. As there are no edges in _G<sup>s</sup>_ that decrease the second coordinate of a vertex, _P_ is monotone in the second coordinate. It remains to show that _P_ is monotone in the first coordinate. For the sake of contradiction, suppose that it is not, that is, there exist two vertices \((x,y_1),(x,y_2)\in P\) such that between them the vertices of _P_ have the first coordinates not equal to _x_. Similarly to the case \(i\ge j\) (in particular, _i=j_), any such subpath of _P_ from (_x,y_<sub>1</sub>) to (_x,y_<sub>2</sub>) has non-positive length. Furthermore, the only path of length zero is the vertical path \((x,y_1)\rightarrow(x,y_1+1)\rightarrow\cdots\rightarrow(x,y_2)\). Hence, _P_ is not the longest path, thus leading to a contradiction. Therefore, indeed, every longest path _P_ from (_i,_0) to (_j,|s_<sup>∗</sup>|) is monotone in both dimensions. Consequently, _P_ only uses the edges of the first three types from Definition B.4, and thus its length is equal to the number of edges of the third type that it uses. It is easy to see that there is a bijection between the increasing subsequences of _s[i..j_) and collections of edges of the third type that may lie on a path from (_i,_0) to (_j,|s_<sup>∗</sup>|). Therefore, \(M_{i,j}^s=\mathsf{LIS}(s[i..j))\). \(\blacktriangleleft\)

\(\blacktriangleright\) **Corollary B.9.** _For a subpermutation s and a core element_ \((i,j,v)\in\mathrm{core}(M^s)\)_, we have_ \(i\le j\).

**Proof.** For _i\>j_, all elements in _M<sup>s</sup>[i..i_+1][_j..j_+1] satisfy the conditions for the second case of Lemma B.8, and thus \(M_{i,j}^s\square=0\). \(\blacktriangleleft\)

\(\blacktriangleright\) **Observation B.10.** _For an integer-valued Monge matrix A, we have_ \(\delta(A)\le\delta^\Sigma(A)\).

