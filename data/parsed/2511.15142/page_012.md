**Corollary 3.6.** _For any_ \(\widehat{w}\in\mathrm{int}(C_{\sigma^*})\)_, if_ \(\mathrm{CCO}(\widehat{w})=(y_1,\dots,y_k)\)_, then_ \(\langle w^*,y_i-y_j\rangle\le 0\) _for all_ \(1\le i\le j\le k\)_. Consequently,_ \(y_1\in\mathrm{argmin}_{x\in\mathcal{P}}\langle w^*,x\rangle\).

(Again, we defer these proofs to Section B.) From Corollary 3.6, it is evident that identifying any point in the interior of \(C_{\sigma^*}\) suffices to identify the global optimizer. Naturally, we will set the polytope to \(C_{\sigma^*}\) with an added box constraint \(P:=C_{\sigma^*}\cap B_\infty(0,1)\). We now describe how the CCO oracle can act as a separation oracle for _P_ as long as the optimal solution has not been found.

## 3.4 CCO as a Separation Oracle

We implement the separation oracle for \(P\subseteq C_{\sigma^*}\) using Corollary 3.6. Given a query point \(\widehat{w}\) (the center of the current ellipsoid), we compute the sequence \((y_1,\dots,y_k)=\mathrm{CCO}(\widehat{w})\). We then check if this sequence is non-decreasing with respect to the hidden vector _w_<sup>∗</sup> using the comparison oracle.

If the sequence is non-decreasing with respect to _w_<sup>∗</sup>, then by the properties of the CCO (specifically Equation (1)), _y_<sub>1</sub> is an optimal solution, and the algorithm terminates.

Conversely, if the sequence is _not_ non-decreasing with respect to _w_<sup>∗</sup>, then \(\widehat{w}\) cannot be in the interior of \(C_{\sigma^*}\). In this case, there must exist a pair of indices _i,j_ such that the CCO ordering dictates \(\langle\widehat{w},y_i-y_j\rangle\le 0\), but the true objective satisfies \(\langle w^*,y_i-y_j\rangle>0\). By the definition of \(C_{\sigma^*}\), the condition \(\langle w^*,y_i-y_j\rangle>0\) implies that every point \(w\in C_{\sigma^*}\) must satisfy \(\langle w,y_i-y_j\rangle\ge 0\). Since \(\widehat{w}\) violates this inequality, the hyperplane \(\mathcal{H}=\{w:\langle w,y_i-y_j\rangle=0\}\) validly separates \(\widehat{w}\) from the target polytope _P_.

We now have all the components for the dual ellipsoid algorithm, which is presented as Algorithm 4:

4.1 **Initialization:** Bounding radius \(R=\sqrt{d}\) for the initial ellipsoid E<sub>0</sub>=_B_<sub>2</sub>(**0**_,R_) and facet complexity \(\phi=O(\langle\mathcal{P}\rangle)\) as input to Algorithm 3.<br>
4.2 **For** _t_=1 to _T_ **do:**<br>
4.3 Let (_y_<sub>1</sub>_,...,y<sub>k</sub>_)=CCO(_w_<sub>_t_-1</sub>) be the conic certificate obtained for weight _w_<sub>_t_-1</sub>.<br>
4.4 Using the comparison oracle for _w_<sup>∗</sup>, verify if:<br>
\(\langle w^*,y_1\rangle\le\langle w^*,y_2\rangle\le\cdots\le\langle w^*,y_k\rangle.\) (6)<br>
4.5 **If** all comparisons are true **then**:<br>
4.6 **Return** (YES,_y_<sub>1</sub>). (_y_<sub>1</sub> _is guaranteed to be an optimal solution_)<br>
4.7 **Else**: (_a violation is found_)<br>
4.8 Find indices _j,j_+1 such that \(\langle w^*,y_j-y_{j+1}\rangle>0\).<br>
4.9 Set normal n<sub>t</sub>=y<sub>j</sub>-y<sub>j+1</sub> and half-space \(\mathcal{H}_t=\{w\in\mathbb{R}^d:\langle w,n_t\rangle\ge 0\}\).<br>
4.10 _(Note:_ H_<sub>t</sub> separates w_<sub>_t_-1</sub> _from w_<sup>∗</sup>_)._<br>
4.11 Set _w<sub>t</sub>_ as the center of ellipsoid E_<sub>t</sub>_ updated according to the seperating hyperplane H_<sub>t</sub>_<br>
by Algorithm 3.<br>
4.12 **End For**<br>
4.13 Return NO.

**Theorem 3.7.** _Algorithm 4 is guaranteed to return_ (YES,_y_) _with_ \(y\in\mathrm{argmin}_{x\in\mathcal{P}}\langle w^*,x\rangle\) _for_ \(T=O(d^3\langle\mathcal{P}\rangle)\).

_Proof._ The algorithm terminates in one of two ways. If the loop returns (YES,_y_<sub>1</sub>) at step _t_, then by the properties of the CCO (specifically Equation (1)), _y_<sub>1</sub> is an optimal solution.

**Algorithm 4:** Dual Ellipsoid Algorithm

