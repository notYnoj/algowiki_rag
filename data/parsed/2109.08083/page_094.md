<tbc>of Algorithm 6.9 inductively to deduce that it does not abort prematurely, and produces a weighting _w_<sub>1∗</sub> satisfying the claims of Theorem 6.12.

In preparation for the proof of Theorem 6.12, recalling Fact 3.24 about zero- sum configurations in T , we state the following corollary about these configurations in _H_<sub>1</sub>.

Corollary 6.13. _For every_ \(i\in[c_g]\) _the following hold:_<tbc>

\(|\mathcal{Z}_{i,e,H_1}^+(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
\Theta\left(j_it_1p_\mathrm{gr}^{12}\right) & \text{\textit{if}}e\text{\textit{is a bad edge}}, \\
O\left(k_it_1p_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=1\text{\textit{, and}}\gamma=3\text{\textit{,}} \\
0 & \text{\textit{otherwise}}.
\end{array}\right.\)

\(|\mathcal{Z}_{i,e,H_1}^-(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
\Theta\left(t_1^2p_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha\neq 0\text{\textit{and}}\gamma=0\text{\textit{,}} \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=0\text{\textit{, and}}c=4\text{\textit{,}} \\
O\left(j_ik_ip_\mathrm{gr}^{12}\right) & \text{\textit{if}}\alpha=0\text{\textit{,}}\beta=1\text{\textit{, and}}\gamma=3\text{\textit{,}} \\
0 & \text{\textit{otherwise}}.
\end{array}\right.\)

<tbc>_Finally, for every bad edge e,_

\(\mathcal{Z}_{i,e,H_1}^2=O\left(k_it_1p_\mathrm{gr}^{12}\right).\)

Proof. The statement follows immediately from Fact 3.24 and Theorem 6.1 (v). □

Unpacking Algorithm 6.9, note that the _i<sup>th</sup>_ iteration of the algorithm shifts weight _from_ only those edges which are (_c<sub>g</sub>-i_+1)-bad or of type (0,1,3)<sub>_c<sub>g</sub>-i_+1</sub>. Observe that (_c<sub>g</sub>-i_+1)-bad edges are then not touched in any further iterations of the algorithm, and edges of type (0,1,3)<sub>_c<sub>g</sub>-i_+1</sub> are only considered in one more iteration. In particular, edges of type (0,1,3)<sub>_c<sub>g</sub>-i_+1</sub> are of type \((1,\beta,\gamma)_{c_g-i}\), and by nature of having a vertex in _K<sub>c<sub>g</sub>-i</sub>_ are no longer in play after step _i_+1 of the algorithm (since by definition they are not of type \((\alpha,\beta,\gamma)_j\) for any combination of \(\alpha,\beta,\gamma\) with _j\<c<sub>g</sub>-i_). Thus when considered this last time, they are either (_c<sub>g</sub>-i_)-bad, in which case their weight is reduced to 0 in the _i_+1 iteration of the algorithm, or they are of type (1,3,0)<sub>_c<sub>g</sub>-i_</sub> in which case they _gain_ weight. The key point here is that any edge can only _lose_ weight in at most two steps of the process, and in a step where this is not reducing the weight on a bad edge to 0 (which can be at most one of the two steps), we’ll show that the edge _e_ loses weight at most \(O\left(\frac{1}{p_\mathrm{gr}^3t_1\mathrm{log}(n)}\right)\). Thus, since until this point the edge only gains weight or remains at weight _w_<sub>1</sub>(_e_) as a result of previous iterations of the algorithm, we have that it retains weight at least _w_<sub>1</sub>(_e_)(1-_O_(log<sup>-1</sup>(_n_))) before becoming either a bad edge in the next step, or an edge of type (1,3,0), and so in particular the algorithm never aborts due to the weight on an edge becoming negative.

As per Steps 1 and 2 of Algorithm 6.9, for each \(z\in\mathcal{Z}_{i,H_1}^2\), we define<tbc>

\(w(z):=\frac{1}{p_\mathrm{gr}^{15}j_it_1^2},\)

<tbc>and for each _i_-bad edge _e_ and \(z_e\in\mathcal{Z}_{i,e,H_1}^+(\mathrm{bad})\backslash\mathcal{Z}_{i,H_1}^2\), we define

\(w(z_e):=\frac{w_{(1,i)}(e)-\sum_{z\in\mathcal{Z}_{i,e,H_1}^2}w(z)}{|\mathcal{Z}_{i,e,H_1}^+(\mathrm{bad})\backslash\mathcal{Z}_{i,H_1}^2|}.\)

