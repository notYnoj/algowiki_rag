_Proof._ We reduce MaxIP to CMM with \(f_{\chi^2}\). Let _A_, _B_, _m_, _n_, `enc`, \(\ell=\lceil log(n+1)\rceil+1\), and the strings _u<sub>j</sub>_, _w<sub>j</sub>_ (\(1\le j\le m\)) be as in the proof of Theorem A.2. If all vectors in _A_ or all vectors in _B_ are zero, the maximum inner product is 0, so we assume that both sets contain a non-zero vector.

Every block \(0\cdot\mathtt{enc}(i)\#_j\) of _u<sub>j</sub>_ has length \(\ell+1\), so consecutive occurrences of #_<sub>j</sub>_ in _u<sub>j</sub>_ are \(\ell+1\) positions apart. Hence, a length-\(\ell\) substring of _u<sub>j</sub>_ contains at most one occurrence of #_<sub>j</sub>_, and if it contains none, it is the first \(\ell\) symbols of a block, that is, \(0\cdot\mathtt{enc}(i)\) for some _i_ with _a<sub>i</sub>_\[_j_\]=1. The same holds for _w<sub>j</sub>_ with \(1\cdot\mathtt{enc}(i)\) and _b<sub>i</sub>_\[_j_\]=1.

We construct \(\langle G=(V,E),\ell\rangle\) as follows; all nodes other than the _u<sub>j</sub>_ and _w<sub>j</sub>_ are isolated. For each \(1\le j\le m\), we add the _complement nodes_

\(u'_j=\circ_{1\le i\le n a_i[j]=0}0\cdot\mathtt{enc}(i)\#'_j\text{and}w'_j=\circ_{1\le i\le n b_i[j]=0}1\cdot\mathtt{enc}(i)\#'_j,\)

where \(\#'_1,\dots,\#'_m\) are fresh symbols; thus \(u'_j\) (resp. \(w'_j\)) contains the encoding of _i_ if and only if _u<sub>j</sub>_ (resp. _w<sub>j</sub>_) does not. Let Z_<sub>U</sub>_ (resp. Z_<sub>W</sub>_) be the set of all special length- \(\ell\) substrings of _u_<sub>1</sub>_,...,u<sub>m</sub>_ (resp. _w_<sub>1</sub>_,...,w<sub>m</sub>_); by our assumption, both are non-empty. For each \(1\le r\le m^2\),<tbc>

<tbc>we add the _padding nodes_

\(z_r^U=\circ_{Z\in\mathcal{Z}_U}Z\$_r^U\text{and}z_r^W=\circ_{Z\in\mathcal{Z}_W}Z\$_r^W,\)

where the \(\$_r^U\) and \(\$_r^W\) are fresh, pairwise distinct symbols. Since each block \(Z\$_r^U\) has length \(\ell+1\), the argument above shows that every length-\(\ell\) substring of \(z_r^U\) contains \(\$_r^U\) or belongs to Z_<sub>U</sub>_; in particular, \(z_r^U\) contains no plain substring. The same holds for \(z_r^W\). Finally, if some _u<sub>j</sub>_, _w<sub>j</sub>_, \(u'_j\), or \(w'_j\) is the empty string, we omit that node, together with the edge {_u<sub>j</sub>,w<sub>j</sub>_} if _u<sub>j</sub>_ or _w<sub>j</sub>_ is omitted. Thus _E_ consists of the edges {_u<sub>j</sub>,w<sub>j</sub>_} with both endpoints non-empty, so \(|E|\le m\). For each _j_, at least one of \(u_j,u'_j\) and at least one of \(w_j,w'_j\) is non- empty, and all padding nodes are non-empty; hence \(|V|\ge 2m^2+2m\). Figure A.2 illustrates the construction.

Recall that, for a motif pair {_X,Y_}, _V<sub>X</sub>_ (resp. _V<sub>Y</sub>_) is the set of nodes in which _X_ (resp. _Y_ ) occurs, _k<sub>X</sub>_=|_V<sub>X</sub>_|, _k<sub>Y</sub>_=|_V<sub>Y</sub>_|, \(k_{X,Y}=|V_X\cap V_Y|\), and \(\overline{E_{X,Y}}=\mathrm{ed}(G)\cdot E_{k_X,k_Y,k_{X,Y}}^\mathrm{max}\), where \(E_{k_X,k_Y,k_{X,Y}}^\mathrm{max}\) is the number of unordered pairs {_x,y_} of distinct nodes with \(x\in V_X\) and \(y\in V_Y\). Every motif pair {_X,Y_} with |_E<sub>X,Y</sub>_|=0 has score 0, so it remains to consider pairs with \(|E_{X,Y}|\ge 1\). To compare their scores, let \(\mu:=\mathrm{ed}(G)\cdot m^2\); we show that \(\overline{E_{X,Y}}=\mu\) whenever _X_ and _Y_ are plain motifs occurring in _G_ such that _X_ starts with 0 and _Y_ starts with 1, and \(\overline{E_{X,Y}}>\mu\) whenever _X_ or _Y_ is special. Since \(|E|\le m\) and \(|V|\ge 2m^2+2m\), note that

\(0<\mu=\frac{|E|\cdot m^2}{\genfrac(){pt}{2}{|V|}{2}}\le\frac{m^3}{\genfrac(){pt}{2}{2m^2+2m}{2}}<1,\)

where \(\mu>0\) as \(E\neq\emptyset\) (otherwise, no pair remains to be considered). We first consider pairs of two plain motifs and then pairs in which at least one motif is special.

Every plain substring of a node is the first \(\ell\) symbols of a block, hence of the form \(0\cdot\mathtt{enc}(i)\) or \(1\cdot\mathtt{enc}(i)\) with \(1\le i\le n\). The motif \(0\cdot\mathtt{enc}(i)\) occurs in _u<sub>j</sub>_ if _a<sub>i</sub>_\[_j_\]=1, in \(u'_j\) if _a<sub>i</sub>_\[_j_\]=0, and in no other node, as the padding nodes contain no plain substring; analogously for \(1\cdot\mathtt{enc}(i)\) with _w<sub>j</sub>_, \(w'_j\), and _b<sub>i</sub>_. We call a motif pair {_X,Y_} a _plain pair_ if _X_ and _Y_ are plain motifs occurring in _G_ such that _X_ starts with 0 and _Y_ starts with 1. By the above, \(X=0\cdot\mathtt{enc}(i)\) and \(Y=1\cdot\mathtt{enc}(i')\) for some \(i,i'\in\{1,\dots,n\}\) (possibly \(i=i'\)). For a plain pair, we have _k<sub>X</sub>=k<sub>Y</sub>=m_ and _k<sub>X,Y</sub>_=0, so \(\overline{E_{X,Y}}=\mu\). Moreover, _E<sub>X,Y</sub>_ consists of the edges {_u<sub>j</sub>,w<sub>j</sub>_} with \(a_i[j]=b_{i^\prime}[j]=1\), so \(|E_{X,Y}|=\langle a_i,b_{i^\prime}\rangle\). Consequently, \(f_{\chi^2}(G,\{X,Y\})=s(\langle a_i,b_{i^\prime}\rangle,\mu)\), which, by Theorem A.3(a), is 0 if \(\langle a_i,b_{i^\prime}\rangle=0\) and strictly increasing in \(\langle a_i,b_{i^\prime}\rangle\) otherwise. Every other pair {_X,Y_} of plain motifs has |_E<sub>X,Y</sub>_|=0: either _X_ and _Y_ occur

u1
001#1 011#1
101#1
w1
u2
010#2 011#2
101#2 111#2
w2
u3
001#3 010#3
110#3 111#3
w3
complement nodes
u'
010#1
110#1 111#1
w'
u2
001#2
110#2
w2
u3
011#3
101#3
w3
padding nodes
Z1
01#1$U 1#10
01#1$W 1#21
Z1
Z1
Z9
01#1$9 1#10
01#1$9 1#21
Z9

Figure A.2: The construction in the proof of Corollary A.4 for the vectors of Figure A.1. The complement nodes and the _m_<sup>2</sup>=9 padding nodes on each side are isolated. Each of `011` and `101` now occurs in exactly _m_=3 nodes, and each padding node \(z_r^U\) (resp. \(z_r^W\)) contains every special length-3 substring of _u_<sub>1</sub>_,u_<sub>2</sub>_,u_<sub>3</sub> (resp. _w_<sub>1</sub>_,w_<sub>2</sub>_,w_<sub>3</sub>), such as `1#10` (resp. `1#21`).

