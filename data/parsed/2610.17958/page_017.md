<tbc>edge {_u<sub>j</sub>,w<sub>j</sub>_}; such a coordinate _j_ contributes to no inner product, so this does not affect the argument below. For each \(1\le j\le m\), let

\(u_j=\circ_{1\le i\le n}_{a_i[j]=1}0\cdot\mathsf{enc}(i)\#_j\text{and}w_j=\circ_{1\le i\le n}_{b_i[j]=1}1\cdot\mathsf{enc}(i)\#_j,\)

where \(\circ\) denotes string concatenation. That is, the node corresponding to each index is labeled by an encoding of the vectors that have that index set to 1. Figure A.1 illustrates the construction. Notice that our encoding requires exactly \(\lceil log(n+1)\rceil\) bits (after padding with zeros); hence, we set \(\ell:=\lceil log(n+1)\rceil+1\).

By construction, if there are vectors \(a_i\in A\) and \(b_j\in B\) such that \(\sum_{k=1}^ma_i[k]b_j[k]\ge p\), then the strings \(0\cdot\mathsf{enc}(i)\) and \(1\cdot\mathsf{enc}(j)\) are substrings of endpoints of at least _p_ edges of _G_. In particular, notice that, for any \(j\in[m]\), we can choose a pair (_X<sub>j</sub>,Y<sub>j</sub>_) of length-\(\ell\) binary strings such that _X<sub>j</sub>_ and _Y<sub>j</sub>_ are substrings of nodes _u<sub>j</sub>_ and _w<sub>j</sub>_, respectively, and none of them contain the separator symbol #_<sub>j</sub>_ (unless the _j_-th bit is unset in all vectors in at least one of _A_ and _B_, in which case we can simply ignore it); hence, they encode vectors whose inner product equals at least 1.

Conversely, suppose that strings _X_ and _Y_ are length- \(\ell\) substrings of endpoints of at least _p_ edges in an instance of CMM obtained by our construction. If either string contains a separator symbol #_<sub>k</sub>_, then it occurs only in _u<sub>k</sub>_ and _w<sub>k</sub>_, so {_u<sub>k</sub>,w<sub>k</sub>_} is the only edge whose endpoints can contain both strings, and the support value of {_X,Y_} is at most 1; in that case we may replace {_X,Y_} by a pair (_X<sub>k</sub>,Y<sub>k</sub>_) as described in the previous paragraph. Thus, we assume that _X_ and _Y_ are length-\(\ell\) binary strings. Since all edges connect one node from _U_ with one from _W_ and by the choice of the labels, we may also assume that _X_ starts with a 0 (and thus occurs only in _U_) and _Y_ starts with a 1 (and thus occurs only in _W_). Since \(\ell=\lceil log(n+1)\rceil+1\), the strings _X_ and _Y_ without their leading bit are the binary encodings of integers \(i,j\in\{1,\dots,n\}\); let \(a_i\in A\) and \(b_j\in B\) be the corresponding vectors. By construction, _X_ occurs in _u<sub>k</sub>_ if and only if _a<sub>i</sub>_\[_k_\]=1, and _Y_ occurs in _w<sub>k</sub>_ if and only if _b<sub>j</sub>_\[_k_\]=1. Hence, the edges whose endpoints contain _X_ and _Y_ are exactly the edges {_u<sub>k</sub>,w<sub>k</sub>_} with _a<sub>i</sub>_\[_k_\]=_b<sub>j</sub>_\[_k_\]=1, and therefore \(\sum_{k=1}^ma_i[k]b_j[k]=|E_{X,Y}|\ge p\).

It is easy to calculate that for this instance, \(N\in\mathcal{O}(m\cdot nlogn),|V|\in\mathcal{O}(m)\), and \(|E|\in\mathcal{O}(m)\), thus giving the claimed lower bound under SETH. \(\sqcap\sqcup\)

As for the lower bound with \(f_{\chi^2}\), some care is needed to carry the result over from _f<sub>E</sub>_, since \(f_{\chi^2}(G,\{X,Y\})\) compares |_E<sub>X,Y</sub>_| with the expected number <o>_E<sub>X,Y</sub>_</o> of edges, which depends on _k<sub>X</sub>,k<sub>Y</sub>_, and _k<sub>X,Y</sub>_. Call a length<tbc>

\(\ell\)

<tbc>string _plain_ if it is a string over {0,1}, and _special_ otherwise. In the construction of Theorem A.2, the plain motifs are the encodings \(0\cdot\mathsf{enc}(i)\) and \(1\cdot\mathsf{enc}(i)\) of the vectors, whereas every special motif contains a separator symbol. This construction has two shortcomings with respect to \(f_{\chi^2}\). First, \(X=0\cdot\mathsf{enc}(i)\) occurs in as many nodes as _a<sub>i</sub>_ has ones (and analogously for \(1\cdot\mathsf{enc}(i)\) and _b<sub>i</sub>_), so the expected number of edges varies between pairs of plain motifs, and \(f_{\chi^2}\) does not rank them by their inner product alone. Second, \(f_{\chi^2}\) favors motif pairs that occur in very few nodes, since their expected number of edges is tiny and a single edge already yields a large score; special motifs are of this kind. We neutralize both effects by adding isolated nodes to the construction in the proof of Theorem A.2.

Both shortcomings, as well as our remedy, concern how \(f_{\chi^2}\) relates to the number |_E<sub>X,Y</sub>_| of edges and to the expected number <o>_E<sub>X,Y</sub>_</o> of edges; by definition, \(f_{\chi^2}(G,\{X,Y\})\) depends only on these two quantities, so it is convenient to view it as a function of them. We need two of its properties: if the expected number of edges is fixed and below 1, then more edges yield a higher score, which lets pairs of plain motifs be ranked by their inner product; and if there is a single edge, then a larger expected number of edges yields a lower score, which lets pairs of plain motifs beat pairs containing a special motif. Formally, for an integer \(t\ge 0\) and a real number _x\>_0, let

\(s(t,x):=\left\{\begin{array}{ c c }
\frac{(t-x)^2}{x} & \text{if}t>x, \\
0 & \text{otherwise},
\end{array}\right.\)

so that \(f_{\chi^2}(G,\{X,Y\})=s(|E_{X,Y}|,\overline{E_{X,Y}})\) whenever <o>_E<sub>X,Y</sub>_</o>_\>_0. The two properties are then as follows.

Observation A.3. _Let_ 0_\<x\<_1_. Then_

(_a)_ _s_(0_,x_)=0_, and s(t,x_) _is strictly increasing in t for integers_ \(t\ge 1\);<tbc>

(_b)_ _s_(1_,y)\<s_(1_,x_) _for every real number y\>x._

_Proof._ For (a), we have _s_(0_,x_)=0 as 0_\<x_, and _s(t,x_)=(_t-x_)<sup>2</sup>_/x_ for \(t\ge 1>x\), which is strictly increasing in \(t\ge x\). For (b), if \(y\ge 1\), then _s_(1_,y_)=0_\<s_(1_,x_) because _x\<_1; otherwise, we have _s_(1_,z_)=_g(z_) for \(z\in\{x,y\}\), where _g(z_):=(1-_z_)<sup>2</sup>_/z_=1_/z_-2+_z_. Since 0_\<x\<y\<_1, we have _xy\<_1, and thus _s_(1_,x_)-_s_(1_,y_)=(1_/x_-1_/y_)+(_x-y_)=(_y-x_)\(\big(\)1/(_xy_)-1\(\big)\)_\>_0. \(\sqcap\sqcup\)

With Theorem A.3 at hand, we are ready to prove the lower bound with \(f_{\chi^2}\).

Corollary A.4. _There is no algorithm solving CMM with_ \(f_{\chi^2}\) _in time_ \(\mathcal{O}(N^{2-\varepsilon} poly(|E|,|V|))\)_, for any_ \(\varepsilon>0\)_, unless SETH fails._

