_Proof._ The assertion is immediate when _W(J_)=0, so assume _W(J)\>_0. Because the instance is integer weighted, we simply replace each constraint _C_ of weight _w<sub>J</sub>(C_) by _w<sub>J</sub>(C_) labeled unit-weight copies. Denote the resulting unweighted multiset by \(J^\unknown\); it has exactly _W(J_) occurrences. Now, for this _unweighted_ CSP instance, we construct the canonical "violation code".

\(\mathcal{C}_{J^\unknown}=\left\{\big(\mathbf{1}[\alpha\text{violates}C]\big)_{C\in J^\unknown}:\alpha:V(J)\rightarrow D\right\}\subseteq\{0,1\}^{W(J)}.\) (6.8)

We claim that

\(\mathsf{NRD}(\mathcal{C}_{J^\unknown})\le\mathsf{NRD}_n(R).\) (6.9)

Indeed, suppose that _t_ coordinates form an identity submatrix, and let _C_<sub>1</sub>_,...,C<sub>t</sub>_ be the corresponding constraint copies. For every \(i\in[t]\), the row containing the _i_th diagonal 1 is an assignment that violates _C<sub>i</sub>_ and satisfies every _C<sub>j</sub>_ with \(j\neq i\). Hence {_C_<sub>1</sub>_,...,C<sub>t</sub>_} is a nonredundant _R_-instance on at most _n_ variables. Notice also that two copies of the same constraint, or two distinct constraints operating on the same ordered tuple of variables, have identical columns and therefore cannot both appear in such an identity submatrix.

Next, we apply (6.4) to \(\mathcal{C}_{J^\unknown}\). Its integer weight vector approximately preserves the number of violated copies for every assignment. To build the ultimate sparsifier, we collapse all selected copies belonging to the same occurrence of _J_ and add their weights. Since we impose no restriction on computation time, the required weight vector can be found deterministically within the stated space bound by enumerating candidate supports and integer weights and checking the inequalities over all assignments. Coordinates that are identically zero may be discarded, while every remaining selected weight is at most \((1+\eta)W(J)\), so this search is finite. This then yields (6.6) and (6.7).

Now, we proceed to give the streaming construction. It is enough to consider an ultimate sparsifier accuracy of \(0<\varepsilon\le 1/2\). For a larger error, run the construction with error 1/2. We then set

\(\eta_\ell=\frac{\varepsilon}{20(\ell+1)^2}(\ell\ge 1).\) (6.10)

The algorithm maintains at most one sparsifier at each level \(\ell\ge 0\). A level-\(\ell\) sparsifier represents a block of exactly \(2^\ell\) original constraints in the stream. Whenever the algorithm stores two sparsifiers at level \(\ell\), we take their weighted union _J_ and replace it by

\(\mathrm{Red}_{\eta_{\ell+1}}(J),\)

which now constitutes a sparsifier at level \(\ell+1\). We repeat this carry operation until every level again contains at most one sparsifier.

**Claim 6.11.** _Let H<sub>B</sub> be a level-_\(\ell\) _sparsifier and let I<sub>B</sub> be the unweighted subinstance consisting of its underlying block of constraints. Then, for every assignment_ \(\alpha\),

\(\left(\prod_{j=1}^\ell(1-\eta_j)\right)\mathrm{unsatval}_{I_B}(\alpha)\le\mathrm{unsatval}_{H_B}(\alpha)\le\left(\prod_{j=1}^\ell(1+\eta_j)\right)\mathrm{unsatval}_{I_B}(\alpha).\) (6.12)

_Consequently, the union of the sparsifiers remaining at the end of the stream is a_ \((1\pm\varepsilon)\)_-sparsifier of the entire input._

_Proof._ We prove (6.12) by induction on \(\ell\). It is an equality at level zero. Suppose two level-\((\ell-1)\) sparsifiers _H_<sub>_B_<sub>1</sub></sub> and _H_<sub>_B_<sub>2</sub></sub> are merged. Since all values are nonnegative, adding their two inductive inequalities shows that their weighted union has the same multiplicative bounds relative to \(I_{B_1}\unknown I_{B_2}\).

