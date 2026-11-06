In particular, the energy increase of each arc \((u,v)\in\partial^+C\) is at most \(\eta\cdot\frac{1}{1-1/(8\alpha)}\cdot w(u,v)\), and the energy decrease from each arc \((u,v)\in\partial^-C\) is at least \(\eta\cdot\frac{1}{1+1/(8\alpha)}\cdot w(u,v)\). Summed over all such arcs, the net change in energy is at most<tbc>

\(\eta\cdot\frac{1}{1-1/(8\alpha)}\cdot w(\partial^+C)-\eta\cdot\frac{1}{1+1/(8\alpha)}\cdot w(\partial^-C).\)

<tbc>Recall that \(\mathbf{g}(C)/\mathbf{u}(\partial C)\le g/u\le-1/(3\alpha)\) and \(\mathbf{g}(C)=\tilde{w}(\partial^+C)-\tilde{w}(\partial^-C)\) and \(\mathbf{u}(\partial C)=\tilde{w}(\partial^+C)+\tilde{w}(\partial^-C)\). We have

\(3\alpha\cdot\mathbf{g}(C)+\mathbf{u}(\partial C)\le 0\Longleftrightarrow(3\alpha+1)\cdot\tilde{w}(\partial^+C)-(3\alpha-1)\cdot\tilde{w}(\partial^-C)\le 0\)<br>
\(\Longleftrightarrow\tilde{w}(\partial^+C)\le\frac{3\alpha-1}{3\alpha+1}\cdot\tilde{w}(\partial^-C).\)

Together with the approximation of weights (Lemma 12), we have<tbc>

\(w(\partial^+C)\le\frac{1}{1-\epsilon}\cdot\tilde{w}(\partial^+C)\le\frac{1}{1-\epsilon}\cdot\frac{3\alpha-1}{3\alpha+1}\cdot\tilde{w}(\partial^-C)\le\frac{1}{1-\epsilon}\cdot\frac{3\alpha-1}{3\alpha+1}\cdot(1+\epsilon)\cdot w(\partial^-C).\)

<tbc>Since \(\epsilon=1/(8\alpha)\), it follows that the net change in energy is at most

\(\eta\cdot\frac{1}{1-1/(8\alpha)}\cdot w(\partial^+C)-\eta\cdot\frac{1}{1+1/(8\alpha)}\cdot w(\partial^-C)\)<br>
\(\le\eta\cdot\frac{1}{1-1/(8\alpha)}\cdot\frac{1+1/(8\alpha)}{1-1/(8\alpha)}\cdot\frac{3\alpha-1}{3\alpha+1}\cdot w(\partial^-C)-\eta\cdot\frac{1}{1+1/(8\alpha)}\cdot w(\partial^-C)\)<br>
\(\le\eta\cdot-\Omega\left(\frac{1}{\alpha}\right)\cdot w(\partial^-C)\)<br>
\(\le\eta\cdot-\Omega\left(\frac{1}{\alpha}\right)\cdot\tilde{w}(\partial^-C).\)

Recall that \(\mathbf{u}(\partial C)\ge u/\alpha\), which means that \(\eta=\frac{1}{16\alpha u}\ge\frac{1}{16\alpha^2\mathbf{u}(\partial C)}\). Also, since **g**(_C)\<_0, we have \(\tilde{w}(\partial^-C)\ge\frac{1}{2}\tilde{w}(\partial C)=\frac{1}{2}\mathbf{u}(\partial C)\). We conclude that the net change in energy is at most

\(\frac{1}{16\alpha^2\mathbf{u}(\partial C)}\cdot-\Omega\left(\frac{1}{\alpha}\right)\cdot\frac{1}{2}\mathbf{u}(\partial C)=-\Omega\left(\frac{1}{\alpha^3}\right),\)

as desired.

Next, suppose that the algorithm finds an augmenting path from _s_ to _t_. The following lemma bounds the total increase in energy from flipping the arcs along the augmenting path.

**Lemma 15** (Energy increase)**.** _Assume that all vertex potentials are within an additive M of each other, i.e.,_ \(|\mathbf{y}(u)-\mathbf{y}(v)|\le M\) _for all_ \(u,v\in V\) _. Suppose the algorithm flips all arcs along a (simple) path from s to t. The total energy increases by at most_ **y**(_t_)-**y**(_s_)+(_n_-1)ln(_M_+1).

_Proof._ Recall that<tbc>

\(\mathcal{E}(u,v)=\left\{\begin{array}{ c c }
ln(M+1)-ln(\mathbf{y}(v)-\mathbf{y}(u)+1) & \text{if}\mathbf{y}(v)\ge\mathbf{y}(u), \\
ln(M+1)+\mathbf{y}(u)-\mathbf{y}(v) & \text{if}\mathbf{y}(v)\le\mathbf{y}(u).
\end{array}\right.\)

