<tbc>module with a cost affine in the number of labels, so losses defined on the partition (and, in future work, weak or scribble supervision) can reach the costs. What it does not buy on PanNuke is accuracy beyond a well-tuned post-hoc watershed with the same supervision, and the paper says so.

## B Derivations

### B.1 Random walks and random forests

Grady reads the seeded Random Walker as follows: _x<sub>i</sub>_ is the probability that a random walk started at pixel _i_, which crosses edge _e_ with probability proportional to _w<sub>e</sub>_, reaches a foreground seed before a background seed. Sect. 3 reads the same _x<sub>i</sub>_ as the probability that a random 2-forest connects _i_ to the foreground node. The two readings are the same harmonic function, written in two ways; the forest reading is the probabilistic watershed of Fita Sanmartín et al. \[16\], restated here on the augmented graph, where the unaries are edges to the label nodes.

Let \(G'\) be the augmented graph: the pixel graph, two label nodes _F_ and _B_, and for every pixel _i_ the edges (_i,F_) of weight \(a_i^1\) and (_i,B_) of weight \(a_i^0\). Let \(L'\) be its Laplacian and \(L'_U\) the submatrix on the pixels, i.e. \(L'\) with the rows and columns of _F_ and _B_ removed, so that \(L'_U=L(w)+\text{diag}(a^0+a^1)\) and system (3) reads \(L'_UX=a^1\).

_Random walk._ Let _h<sub>i</sub>_ be the probability that the walk from _i_ reaches _F_ before _B_. Then _h<sub>F</sub>_=1, _h<sub>B</sub>_=0, and at every pixel the first step gives \(h_i=\sum_{j\sim i}w_{ij}h_j/\sum_{j\sim i}w_{ij}\), the sum running over the pixel neighbours and the two label nodes. This says \((L'h)_i=0\) at every pixel with the boundary values on _F_ and _B_, i.e. \(L'_Uh=a^1\). The system is non-singular (it is diagonally dominant with a strictly dominant row wherever a unary is positive), so _h=x_.

_Random 2-forest._ By Cramer’s rule, \(x_i=\text{det}L'_U[i\leftarrow a^1]/\text{det}L'_U\), where \([i\leftarrow a^1]\) replaces column _i_ by the right-hand side. The all-minors matrix-tree theorem \[10\] evaluates both determinants. \(\text{det}L'_U\) is the minor of \(L'\) with the vertices _F_ and _B_ deleted: it equals the sum, over the spanning forests of \(G'\) with exactly two trees, one containing _F_ and the other _B_, of the product of the edge weights of the forest. The numerator is, up to a sign that cancels in the ratio, the minor of \(L'\) with rows {_F,B_} and columns {_i,B_} deleted, which the same theorem evaluates as the sum over those 2-forests in which _i_ lies in the tree of _F_. Hence

\(x_i=\frac{\sum_{\mathcal{F}:i\sim F}\prod_{e\in\mathcal{F}}w_e}{\sum_\mathcal{F}\prod_{e\in\mathcal{F}}w_e},\) (5)

the probability that _i_ is attached to _F_ when a 2-forest is drawn with probability proportional to its weight. With _w<sub>e</sub>=e_<sup>-_pc<sub>e</sub>_</sup> and _a=e_<sup>-_pc_</sup> the weight of a forest is \(e^{-p}\sum_{e\in\mathcal{F}}c_e\): the distribution is the Gibbs distribution over 2-forests with energy the total cost of the forest, at inverse temperature _p_. As \(p\rightarrow\infty\) it concentrates on the forests of minimum total cost, i.e. on the maximum-weight spanning forests separating _F_ from _B_, which is the Power Watershed; when several forests tie,

