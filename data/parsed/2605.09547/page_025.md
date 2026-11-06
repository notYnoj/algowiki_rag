For all other edges, the initial flow values are simply the half of the edge capacities, so we do not need to store them, as we read in the edge capacity every time we see an edge.

Now, it is clear that the construction itself is feasible, so we need to show that it is centered. \[BLL<sup>+</sup>21\] also proves centrality.

**Lemma 6.2** (Initial point for the modified min cost flow, Lemma 7.5 of \[BLL<sup>+</sup>21\])**.** _Let_ \(\left[\begin{array}{ c }
s^{(\mathrm{init})} \\
\widetilde{s}^{(\mathrm{init})}
\end{array}\right]=\left[\begin{array}{ c }
c \\
\widetilde{c}
\end{array}\right]\) _and_ \(\mu^{(\mathrm{init})}=100m^2W^3\epsilon^{-1}\)_. Then, the point_ \(\left(\left[\begin{array}{ c }
x^{(\mathrm{init})} \\
\widetilde{x}^{(\mathrm{init})}
\end{array}\right],\left[\begin{array}{ c }
s^{(\mathrm{init})} \\
\widetilde{s}^{(\mathrm{init})}
\end{array}\right],\mu^{(\mathrm{init})}\right)\) _is_ \(\epsilon\)_-centered w.r.t. the linear program in_ (15).

Thus this is a suitable initial point for our algorithm.

Finally, we need to show that this modified flow does indeed solve the original flow problem. Let \(\mathrm{OPT}(\widetilde{G})\) be the optimal value of the above LP. Since the star-edge have cost \(>m\|c\|_\infty\), any flow that goes along these edges, i.e., some (_v,z),(z,w_), would be cheaper if it was instead routed along any other _vw_-path using only original edges. So the optimal solution does not use these edges, and thus the optimal flow on the original graph and the new graph is identical. This assumes that it is possible to re-route the flow. If that is impossible, then that would be there is no path from _v_ to _w_ in the residual graph and thus the demand of the original problem cannot be satisfied.

**Fact 6.3.** \(\mathrm{OPT}(\widetilde{G})=\mathrm{OPT}(G)\).

## 6.2 Final Point & Existence of Nearby Exact Solution

We now need to show that after running our algorithm we have indeed found a near optimal solution.

We prove the following lemma.

**Lemma 6.4.** _Given an_ \(\epsilon\)_-centered point_ \(\left(\left[\begin{array}{ c }
x \\
\widetilde{x}
\end{array}\right],\left[\begin{array}{ c }
s \\
\widetilde{s}
\end{array}\right],\mu\right)\) _of_ (15) _where_ \(\mu<\epsilon/n^2\)_, there exists x_<sup>OPT</sup> _which is an optimal flow for G for which for_ \(\widetilde{x}^\mathrm{OPT}=0\) _we have_ \(\|\left[\begin{array}{ c }
x \\
\widetilde{x}
\end{array}\right]-\left[\begin{array}{ c }
x^\mathrm{OPT} \\
\widetilde{x}^\mathrm{OPT}
\end{array}\right]\|_\infty\lesssim\epsilon W\).

_Proof._ Note from Fact 6.3 we have _x_<sup>OPT</sup> being an optimal flow for _G_ is equivalent to \(\left[\begin{array}{ c }
x^\mathrm{OPT} \\
\widetilde{x}^\mathrm{OPT}
\end{array}\right]\) being an optimal flow for \(\widetilde{G}\). Then, this lemma follows directly from Lemmas 6.5 and 6.7 when taking \(\mu\le\frac{\epsilon}{n^2}\).

**Lemma 6.5** (Extension of Lemma 7.7 of \[BLL<sup>+</sup>21\])**.** _Given an_ \(\epsilon\)_-centered point_ \(\left(\left[\begin{array}{ c }
x \\
\widetilde{x}
\end{array}\right],\left[\begin{array}{ c }
s \\
\widetilde{s}
\end{array}\right],\mu\right)\) _of_ (15) _where_ \(\mu<1/n\)_, there exists_ \(\left[\begin{array}{ c }
x^{(\mathrm{final})} \\
\widetilde{x}^{(\mathrm{final})}
\end{array}\right]\) _which is a feasible flow for_ \(\widetilde{G}\) _where_ \(c^\top x^{(\mathrm{final})}+\widetilde{c}^\top\widetilde{x}^{(\mathrm{final})}\le\mathrm{OPT}(\widetilde{G})+\mu n\)_. Moreover,_ \(\|\left[\begin{array}{ c }
x \\
\widetilde{x}
\end{array}\right]-\left[\begin{array}{ c }
x^{(\mathrm{final})} \\
\widetilde{x}^{(\mathrm{final})}
\end{array}\right]\|_\infty\lesssim\epsilon W\).

_Proof._ The first part of the lemma is simply Lemma 7.7 of \[BLL<sup>+</sup>21\].<br>
To show the moreover part, we use the following claim:

**Claim 6.6** (Claim A.6 of \[BLL<sup>+</sup>21\])**.**<tbc>

\(\left\|\Phi''\left(\left[\begin{array}{ c }
x \\
\widetilde{x}
\end{array}\right]\right)^\frac{1}{2}\left(\left[\begin{array}{ c }
x^{(\mathrm{final})} \\
\widetilde{x}^{(\mathrm{final})}
\end{array}\right]-\left[\begin{array}{ c }
x \\
\widetilde{x}
\end{array}\right]\right)\right\|_\infty\lesssim\epsilon\)

<tbc>Then we have for any edge _e_ (including star edges) \(\phi''(x_e)=\left(\frac{1}{x_e^2}-\frac{1}{(u_e-x_e)^2}\right)\lesssim\epsilon\). Recall \(0\le x_e\le u_e\le W\). Then

\(|x_e^{(\mathrm{final})}-x_e|\lesssim\frac{\epsilon}{(1/x_e^2+1/(u_e-x_e)^2)^{1/2}}\le\frac{\epsilon}{(2/W^2)^{1/2}}\le\epsilon W.\)

where the second step follows from \(1/x_e^2+1/(u_e-x_e)^2\ge 2/W^2\) for all \(0\le x_e\le u_w\le W\) (see Fact B.1) and the last step follows from simple algebra.

