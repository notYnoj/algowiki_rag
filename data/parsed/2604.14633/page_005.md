i.e., for each arc (_u,v_) in the residual graph, add _w(u,v_) to the tail _u_ and subtract _w(u,v_) from the head _v_. In other words, we "undirect" the residual graph and encode the arc directions through a gradient function.

**Lemma 5.** _For any set_ \(S\subseteq V\)_, we have_ \(\mathbf{g}(S)=w(\partial^+S)-w(\partial^-S)\).

_Proof._ Any arc \((u,v)\in\partial^+S\) contributes _w(u,v_) to **g**(_S_) since we add _w(u,v_) to the tail \(u\in S\), while the subtraction at the head \(v\notin S\) is not counted in **g**(_S_). Similarly, any arc \((u,v)\in\partial^-S\) contributes -_w(u,v_) to **g**(_S_). All other arcs contribute 0 since either \(u,v\notin S\) in which case there is no contribution, or \(u,v\in S\) in which case the contributions of +_w(u,v_) and -_w(u,v_) cancel out.

**Lemma 6.** _If the minimum ratio cut has ratio_ \(\mathbf{g}(S)/w(\partial S)\ge-1/3\)_, then_ \(w(\partial^+S)\ge\frac{1}{2}w(\partial^-S)\) _for all_ \(S\subseteq V\) .

_Proof._ It suffices to show that a cut \(S\subseteq V\) with \(w(\partial^+S)<\frac{1}{2}w(\partial^-S)\) implies that \(\mathbf{g}(S)/w(\partial S)<-1/3\). By the previous lemma, we have \(\mathbf{g}(S)=w(\partial^+S)-w(\partial^-S)\). Together with \(w(\partial S)=w(\partial^+S)+w(\partial^-S)\), we obtain

\(3\cdot\mathbf{g}(S)+w(\partial S)=3\cdot(w(\partial^+S)-w(\partial^-S))+(w(\partial^+S)+w(\partial^-S))\)<br>
\(=4\cdot w(\partial^+S)-2\cdot w(\partial^-S)\)<br>
\(<2\cdot w(\partial^-S)-2\cdot w(\partial^-S)\)<br>
\(=0,\)

or equivalently \(\mathbf{g}(S)/w(\partial S)<-1/3\), as desired.

## 2.1 Dynamic Data Structure

To compute and maintain our balancing weights, we use the following data structure defined in \[VDBCK<sup>+</sup>24\]:

**Definition 7** (\(\alpha\)-approximate min-ratio cut data structure, Definition 5.2 of \[VDBCK<sup>+</sup>24\])**.** _For a weighted undirected graph H_=(_V,E,_**u**) _where_ \(\mathbf{u}\in\mathbb{R}^E\) _and_ \(\mathbf{u}(e)\in[1/U,U]^3\) _for_ \(\mathrm{log}U=\tilde{O}(1)\)_, an initial gradient_ \(\mathbf{g}\in\mathbb{R}^V\) _where_ \(\mathbf{g}\perp\unknown\) _and_ \(\mathbf{g}(v)\in[-U,U]\)_, an initial potential vector_ \(\mathbf{y}\in\mathbb{R}^V\)_, and a detection threshold parameter_ \(\epsilon\)_, an_ \(\alpha\)_-approximate min-ratio cut data structure_ D _implicitly maintains the potential vector_ **y** _and supports the following operations:_

• InsertEdge(_e_),DeleteEdge(_e_)_: inserts/deletes the edge e with weight_ **u**(_e_).<tbc>

• Update\(\mathrm{Gradient}(u,v,\delta)\)_: updates_ \(\mathbf{g}(u)\leftarrow\mathbf{g}(u)+\delta\) _and_ \(\mathbf{g}(v)\leftarrow\mathbf{g}(v)-\delta\).<tbc>

• Potential(_v_)_: returns_ **y**(_v_).<tbc>

<sup>3</sup>The only difference is that \[VDBCK<sup>+</sup>24\] enforces \(\mathbf{u}(e)\in[1,U]\) while we require the weaker \(\mathbf{u}(e)\in[1/U,U]\). However, we can scale all **u**(_e_) and **g**(_v_) by _U_, giving \(\mathbf{u}(e)\in[1,U^2]\) and \(\mathbf{g}(v)\in[-U^2,U^2]\), which preserves all ratios and still satisfies \(\mathrm{log}U^2=\tilde{O}(1)\). We also scale the initial **y** by 1_/U_ and apply their data structure with each \(\eta\) in ToggleCut(\(\eta\)) scaled by 1_/U_, so that the value **u**(_e_)(**y**(_u_)-**y**(_v_)) remains unchanged. Assuming the original constraint \(\mathbf{u}(e)\in[1,U]\) and tracking the scaling by _U_ is cumbersome, so we instead assume the weaker \(\mathbf{u}(e)\in[1/U,U]\) directly.

