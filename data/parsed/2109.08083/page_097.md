<tbc>_i_<sup>∗</sup>+1. Additionally, by Corollary 6.13, edges of type \((\alpha,\beta,0)_{c_g-i^*}\) with \(\alpha\neq 0\) gain weight \(\Theta\left(\frac{1}{p_\mathrm{gr}^3k_{c_g-i^*}\mathrm{log}(n)}\right)\) in this step of the algorithm. Before running the itera tion, by induction such an edge _e_ satisfies (iii), where \(\sum_{j=0}^{i^*-1}O\left(\frac{k_{c_g-j}}{p_\mathrm{gr}^3t_1^2}\right)=o(w_1(e))\). So after running the iteration we get that \(w_{(1,c_g-(i^*+1))}(e)=(1\pm o(1))w_1(e)+\Theta\left(\frac{1}{p_\mathrm{gr}^3k_{c_g-i^*}\mathrm{log}(n)}\right)=\Theta\left(\frac{1}{p_\mathrm{gr}^3k_{c_g-i^*}\mathrm{log}(n)}\right)\)for every edge of type \((\alpha,\beta,0)_{c_g-i^*}\), so (ii) holds. To see (iii) and (iv), note that every edge _e_ of type \((\alpha,\beta,\gamma)_{c_g-(i^*+1)}\) is of type \((0,\beta,\gamma)_{c_g-i^*}\), and so by induction \(w_1(e)\le w_{(1,c_g-i^*)}(e)\le w_1(e)+\sum_{j=0}^{i^*-1}O\left(\frac{k_{c_g-j}}{p_\mathrm{gr}^3t_1^2}\right)\). In running the iteration of the algorithm, again using Corollary 6.13, such an edge gains weight at most \(O\left(\frac{k_{c_g-i^*}}{p_\mathrm{gr}^3t_1^2}\right)\), so the upper bounds for (iii) and (iv) are satisfied. Finally to see the lower bounds, note that _e_ could only have lost weight if it is of type (0,1,3)_<sub>c<sub>g</sub>-i_<sup>∗</sup></sub>. Such an edge is of type \((1,\beta,\gamma)_{c_g-(i^*+1)}\), so (iv) holds. Also, such an edge _e_ loses weight at most _O(w_<sub>1</sub>(_e_)log<sup>-1</sup>(_n_)), and since it was of type \((0,\beta,\gamma)_{c_g-i^*}\), by induction (iii) also holds, completing the proof. □

In particular, Lemma 6.15 tells us that Algorithm 6.9 completes. Indeed, by construction it could only fail if at some iteration we caused some edges to have negative weight, as then the new weighting would not be an almost-perfect fractional matching for _H_<sub>1</sub>. Furthermore, taking _w_<sub>1∗</sub>:=_w_<sub>(1,0)</sub>, we have from Lemma 6.15 that

(6.10) \(w_{(1,0)}(e)=\left\{\begin{array}{ c c }
0 & \text{for every}l\text{-bad edge, where}l>0, \\
\Theta\left(\frac{1}{p_\mathrm{gr}^3k_l\mathrm{log}(n)}\right) & \text{for every edge of type}(\alpha,\beta,0)_l \\
w_1(e)(1\pm o(1))) & \text{where}\alpha\neq 0\text{and}l>0, \\
w_1(e)(1\pm o(1))) & \text{for every edge of type}(0,\beta,\gamma)_1.
\end{array}\right.\)

It remains to prove Theorem 6.12 which follows almost immediately.

Proof of Theorem 6.12. Assuming Theorem 6.1, we have by construction of Algorithm 6.9, and observing from Lemma 6.15 and the discussion following it, that the Algorithm does not abort, and it follows immediately that (_i_), (_iii_) and (_iv_) all hold. By (6.10), which considers every edge in _H_<sub>1</sub>, we have immediately that (ii) holds, as required. □

Having proved Theorem 6.12, we note the following corollary, that will be useful to note for the remainder of the iterative matching process.

Corollary 6.16. _For every_ \(j\in[c_h]\) _and every_ \(v\in H_{1*}[I_{t_j}]\),<tbc>

\(\frac{w_{1*}(E_{H_{1*}}(v,I_{t_{j+1}}))}{w_{1*}(E_{H_{1*}}(v,I_{t_j}))}=\Theta(1)\le 1.\)

<tbc>Proof. Firstly, using the fact that \(E_{H_{1*}}(v,I_{t_{j+1}})\subseteq E_{H_{1*}}(v,I_{t_j})\), it follows trivially that \(\frac{w_{1*}(E_{H_{1*}}(v,I_{t_{j+1}}))}{w_{1*}(E_{H_{1*}}(v,I_{t_j}))}\le 1\). Suppose that _I<sub>t<sub>j</sub></sub>_ has depth _l_. If \(v\in K_{l+1}\), then \(\frac{w_{1*}(E_{H_{1*}}(v,I_{t_{j+1}}))}{w_{1*}(E_{H_{1*}}(v,I_{t_j}))}=1\). Suppose \(v\in K_l\backslash K_{l+1}\). Then every edge in _H_<sub>1∗</sub> containing _v_ has weight either \(\Theta\left(\frac{1}{p_\mathrm{gr}^3k_l\mathrm{log}(n)}\right)\) or \(\Theta\left(\frac{1}{p_\mathrm{gr}^3k_{l+1}\mathrm{log}(n)}\right)\), and every edge containing _v_ in _H_<sub>1∗</sub>\[_I<sub>t<sub>j</sub></sub>_\] which is _not_ in _H_<sub>1∗</sub>\[_I_<sub>_t_<sub>_j_+1</sub></sub>\] has weight \(\Theta\left(\frac{1}{p_\mathrm{gr}^3k_l\mathrm{log}(n)}\right)\checkmark\Theta\left(\frac{1}{p_\mathrm{gr}^3k_{l+1}\mathrm{log}(n)}\right)\).

