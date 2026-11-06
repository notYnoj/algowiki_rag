**Definition 3.2** (Alignment graph)**.** For two strings _X_ and _Y_ , the alignment graph **G**_<sub>X,Y</sub>_ is a weighted undirected graph with vertex set \(\{v_{x,y}:x\in[0..|X|],y\in[0..|Y|]\}\) and edges:

• \(v_{x,y-1}\leftrightarrow v_{x,y}\) of length 1, for \(x\in[0..|X|]\) and \(y\in[1..|Y|]\);<tbc>

• \(v_{x-1,y}\leftrightarrow v_{x,y}\) of length 1, for \(x\in[1..|X|]\) and \(y\in[0..|Y|]\);<tbc>

• \(v_{x-1,y-1}\leftrightarrow v_{x,y}\) of length 0, for \(x\in[1..|X|]\) and \(y\in[1..|Y|]\) such that _X_\[_x_\]=_Y_\[_y_\].

**Observation 3.3.** _Let d be the metric induced by G<sub>X,Y</sub>. All_ \(x,x'\in[0..|X|]\) _and_ \(y,y'\in[0..|Y|]\)_, satisfy_

\(d(v_{x,y},v_{x^\prime,y^\prime})=\left\{\begin{array}{ c c }
\delta_D(X(x\dots x'],Y(y\dots y']) & \text{\textit{if}}x\le x'\text{\textit{and}}y\le y', \\
\delta_D(X(x'\dots x],Y(y'\dots y]) & \text{\textit{if}}x'\le x\text{\textit{and}}y'\le y, \\
|x-x'|+|y-y'| & \text{\textit{otherwise}}.
\end{array}\right.\)

For two ranges \([x\dots x']\subseteq[0..|X|]\) and \([y\dots y']\subseteq[0..|Y|]\), the subgraph of _G<sub>X,Y</sub>_ induced by \(\{v_{\bar{x},\bar{y}}:\bar{x}\in[x\dots x'],\bar{y}\in[y\dots y']\}\) is denoted \(G_{X,Y}^{[x\dots x^\prime],[y\dots y^\prime]}\) and called a _block_ in _G<sub>X,Y</sub>_. For a block _B_, we distinguish the _input vertices_ \(\mathrm{in}^B=(v_{x^\prime,y},v_{x^\prime-1,y},\dots,v_{x,y},v_{x,y+1},\dots,v_{x,y^\prime})\) and the _output vertices_ \(\mathrm{out}^B=(v_{x^\prime,y},v_{x^\prime,y+1},\dots,v_{x^\prime,y^\prime},v_{x^\prime-1,y^\prime},\dots,v_{x,y^\prime})\); both sequences consist of \(|B|:=(x'-x)+(y'-y)+1\) vertices. The _DIST<sub>B</sub>_ table is a \(|B|\times|B|\) matrix with entries \(DIST_B[i,j]=d(\mathrm{in}_i^B,\mathrm{out}_j^B)\) for \(i,j\in[1..|B|]\). The _DIST<sub>B</sub>_ table satisfies the Monge property \[Tis15\]: \(DIST_B[i,j]+DIST_B[i',j']\le DIST_B[i,j']+DIST_B[i,j']\) holds for all \(i,i',j,j'\in[1..|B|]\) such that \(i\le i'\) and \(j\le j'\). For two strings \(X,Y\in\Sigma^*\), we also define _DIST<sub>X,Y</sub>_ to be _DIST<sub>B</sub>_ for \(B=G_{X,Y}^{[0..|X|],[0..|Y|]}\). By Observation 3.3, if \(B=G_{X,Y}^{[x\dots x^\prime],[y\dots y^\prime]}\), then \(DIST_B=DIST_{X(x\dots x^\prime],Y(y\dots y^\prime]}\).

### Box decomposition

For two strings \(X,Y\in\Sigma^*\), the _box decomposition_ **B** of the graph _G<sub>X,Y</sub>_ is defined based on decompositions \(X=X_1\circ\cdots\circ X_{p_X}\) and \(Y=Y_1\circ\cdots\circ Y_{p_Y}\) into non-empty fragments, called _phrases_.

Let us define sets \(\{b_0^X,\dots,b_{p_X}^X\}\) and \(\{b_0^Y,\dots,b_{p_Y}^Y\}\) of _phrase boundaries_ in _X_ and _Y_ , respectively, so that the phrases are \(X_i=X(b_{i-1}^X\dots b_i^X]\) for \(i\in[1..p_X]\) and \(Y_j=Y(b_{j-1}^Y\dots b_j^Y]\) for \(j\in[1..p_Y]\). A vertex _v<sub>x,y</sub>_ is a _boundary vertex_ if _x_ is a phrase boundary in _X_ or _y_ is a phrase boundary in _Y_ , and a _grid vertex_ if both _x_ is a phrase boundary in _X_ and _y_ is a phrase boundary in _Y_ . The box decomposition **B** is an indexed family \((B_{i,j})_{i\in[1..p_X],j\in[1..p_Y]}\) of _boxes_ \(B_{i,j}:=G_{X,Y}^{[b_{i-1}^X\dots b_i^X],[b_{j-1}^Y\dots b_j^Y]}\).

## 3.1 Portal-Respecting Walks

Hermelin et al. \[HLLW13\] applied a box decomposition obtained via an analogue of Corollary 3.9 to determine \(\delta_D(X,Y)\) using a dynamic-programming procedure computing \(\delta_D(X[1..x],Y[1..y])\) for all boundary vertices _v<sub>x,y</sub>_. We reduce the number of DP states by considering only a selection **P** of boundary vertices, called _portals_. This allows improving the running time from \(\widetilde{O}(\frac{NM}{\tau})\) to \(\widetilde{O}(|\mathbf{P}|)\), but reduces the search space from the family of all walks \(v_{0,0}\rightsquigarrow v_{x,y}\) to walks that cross box boundaries only at portals. Below, we formally define such portal-respecting walks and provide a construction suitable for approximating \(\delta_D(X,Y)\).

**Definition 3.4.** Let **B** be a box decomposition of _G<sub>X,Y</sub>_ and let **P** be a set _portals_ (selected boundary vertices). We say that a walk _W_ is a _portal-respecting_ (_i,j)-walk_ if _W_ is a concatenation of walks \(W'\) and \(W''\) such that:

• \(W''\) starts at an input portal of _B<sub>i,j</sub>_ and is entirely contained within _B<sub>i,j</sub>_, and<tbc>

• \(W'\) is the empty walk at _v_<sub>0,0</sub>, a portal-respecting (_i_-1_,j_)-walk, or a portal-respecting (_i,j_-1)-walk.

Let us fix a box decomposition **B** of _G<sub>X,Y</sub>_, and a set of portals **P**. For a box \(B_{i,j}\in\mathbf{B}\), let \(\mathbf{P}_{i,j}=\mathbf{P}\cap\mathrm{out}^{B_{i,j}}\) denote the output portals of _B<sub>i,j</sub>_. Moreover, for a vertex \(v_{x,y}\in B_{i,j}\), we denote \(d_{x,y}=d(v_{0,0},v_{x,y})=\delta_D(X[1..x],Y[1..y])\) and let \(D_{x,y}^{i,j}\) be the minimum length of a portal-preserving (_i,j_)-walk ending at _v<sub>x,y</sub>_.

**Lemma 3.5.** _Given a set of portals_ **P** _for a box decomposition_ **B** _of G<sub>X,Y</sub>, the length of the shortest portal-respecting_ (_p<sub>X</sub>,p<sub>Y</sub>)-walk ending at v_<sub>|_X_|,|_Y_|</sub> _can be computed in_ \(\widetilde{O}(|\mathbf{P}|)\) _time provided_ \(\widetilde{O}(1)\)_-time random access to the DIST matrices of all the boxes of_ **B**.

_Proof._ For each box \(B_{i,j}\in\mathbf{B}\), our algorithm computes \(D_{x,y}^{i,j}\) for all vertices \(v_{x,y}\in\mathbf{P}_{i,j}\). For this, the boxes _B<sub>i,j</sub>_ containing any output portal are processed in the order of non-decreasing values _i+j_.

