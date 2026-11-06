<tbc>Since _G_<sup>∗</sup>\[_X_(H)\] is _k_-colorable, we have \(|Y(\mathcal{H})|\ge|X(\mathcal{H})|/k\). Moreover, each subset \(W\subseteq Y(\mathcal{H})\) is also an independent set (see Figure 7). Therefore, we can write down 2<sup>|_Y_(H)|</sup> history sequences as follows (we add _W_ to each of _A_<sub>1</sub>_,...,A<sub>t</sub>_ and to _I<sub>t</sub>_):

\(F(\mathcal{H},W):=(A_1\cup W,I_1,\dots,A_{t-1}\cup W,I_{t-1},A_t\cup W,I_t\cup W)\text{, for each}W\subseteq Y(\mathcal{H})\text{.}\)

The sequence _F_(H_,W_) is indeed a valid history sequence up to level _t_. This can be shown as follows. First, for every _i\<t_, _I<sub>i</sub>_ is an independent set of \(G^*[A_i\cup W]\), because _I<sub>i</sub>_ is an independent set of _G_<sup>∗</sup>\[_A<sub>i</sub>_\]. Second, \(A_{i+1}\cup W=N_{A_i\cup W}(I_i)\) holds, because if some vertex \(w\in W\) has no neighbor in _I<sub>i</sub>_, then _w_ should have been put into bin _J<sub>i</sub>_ instead of _J<sub>t</sub>_. Third, \(I_t\cup W\) is an independent set because \(W\subseteq Y(\mathcal{H})\) is an independent set and every vertex in \(W\subseteq J_t\) has no neighbor in _I<sub>t</sub>_.

Next, the constructed histories _F_(H_,W_), over all \(\mathcal{H}\in\mathbb{H}'\) and \(W\subseteq Y(\mathcal{H})\), are pairwise distinct. This is because, from a history sequence \(F(\mathcal{H},W)=(A'_1,I'_1,\dots,A'_t,I'_t)\), we can uniquely recover _W_ as \(I'_t\cap N(v)\), and hence we can also uniquely recover the original history sequence H. The reason for \(W=I'_t\cap N(v)\) is that, for \(I'_t=I_t\cup W\), each vertex in _I<sub>t</sub>_ is not adjacent to _v_ (due to \(v\in J_t\)), but each vertex in _W_ is adjacent to _v_ (due to \(W\subseteq X(\mathcal{H})\)). Therefore, the total probability of all history sequences _F_(H_,W_) is at most 1:

\(\sum_{\mathcal{H}\in\mathbb{H}^\prime}\sum_{W\subseteq Y(\mathcal{H})}p(F(\mathcal{H},W))\le 1\text{.}\) (1)

On the other hand, we also have a lower bound on the probability _p(F_(H_,W_)) in terms of _p_(H). This is calculated as follows:

\(p(F(\mathcal{H},W))=p(\mathcal{H})\cdot\frac{\lambda^{|W|}}{\prod_{i=1}^t\{Z_\lambda(G^*[A_i\cup W])/Z_\lambda(G^*[A_i])\}}\)<br>
\(\ge p(\mathcal{H})\cdot\frac{\lambda^{|W|}}{\{(1+\lambda)^{|W|}\}^t}\)<br>
\(=p(\mathcal{H})\cdot\left\{\frac{\lambda}{(1+\lambda)^t}\right\}^{|W|}\text{.}\)

The first equality is derived from Proposition 18, and the inequality is derived from Proposition 9. Therefore, by the binomial theorem, we obtain

\(\sum_{W\subseteq Y(\mathcal{H})}p(F(\mathcal{H},W))\ge p(\mathcal{H})\cdot\left\{1+\frac{\lambda}{(1+\lambda)^t}\right\}^{|Y(\mathcal{H})|}\text{.}\) (2)

Neighbor of v
Max Independent Set
v
v
J1
Jt
J1
Jt
J1
Jt
Definition of X(H)
Definition of Y(H)
F(H, W) is defined for all W (H)

**Figure 7:** An illustration of the sets _X_(H), _Y_(H), and \(W\subseteq Y(\mathcal{H})\) used to construct a new history sequence _F_(H_,W_).

