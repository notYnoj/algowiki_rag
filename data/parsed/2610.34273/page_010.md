two polynomial comparisons after taking the power \(1/\eta_n\) in the partial-sum formula. On the diagonal,

\(H_d(a,\dots,a)=\left(\frac{na-(n-2)}{2}\right)^{2(n-1)/n}(a\ge 1).\)

Its growth exponent is therefore exactly the exponent forced by the upper-bound argument in Subsection 1.3. Raising it to \(\eta_n\) gives linear growth, consistent with the interpolation rank bound.

**Accounting for simultaneous separation.** The separation rule must be checked for every block count and every retained edge dimension. Let \(m,t\ge 1\) be integers, and let \(X_0,\dots,X_{m-1}\in\mathcal{F}_n\) have equal dimensions on their first _n_-2 legs. Write _e_=(_n_-1_,n_) and \(A=X_0\boxplus_e\cdots\boxplus_eX_{m-1}\). Lemma 5.4 uses the polynomial resource C_<sub>n</sub>(m,...,m,t_), with _n_-2 inputs of length _m_, to separate these blocks while retaining an edge of dimension _t_:

\(\left(\begin{array}{ c }
\oplus_{h=0}^{m-1}X_h \\
\otimes_K\mathbf{E}_{n-1,n}^{(t)}\unknown_{\mathrm{poly},n}A\otimes_K\mathsf{C}_n(m,\dots,m,t).
\end{array}\right)\)

This extends the resource form of separation in \[ABZ26, Proposition 3.5\]. Its weight construction forces all _n_-2 shared labels to equal the block label at once.

Put _w<sub>h</sub>_=V_<sub>n</sub>(X<sub>h</sub>_) for \(0\le h<m\). Hölder’s inequality and the partial-sum formula give<tbc>

\(\sum_{h=0}^{m-1}w_h\le m^{1-\eta_n}\mathcal{V}_n(A).\)

<tbc>The comparison function supplies the required factor: Lemma 5.8 gives \(H_d(m,\dots,m,t)\ge tm^{(d-1)/(d+1)}\), and hence

\(\mathcal{V}_n(\mathsf{C}_n(m,\dots,m,t))\ge t^{\eta_n}m^{1-\eta_n},\)

since \(\eta_n(d-1)/(d+1)=1-\eta_n\). Also, \(\mathcal{V}_n(\mathbf{E}_{n-1,n}^{(t)})=t^{\eta_n}\). Multiplying the Hölder bound by this edge value proves that the left-hand side of the separation rule has certificate value at most that of the right-hand side. Together with the preceding comparisons and the algebraic identities, this proves \(\mathcal{V}_n(X)\le\mathcal{V}_n(Y)\) whenever \(X\unknown_{\mathrm{poly},n}Y\) ; see Lemma 5.10.

**The complete-graph threshold.** The normalization _H<sub>d</sub>_(1_,...,_1_,b_)=_b_ gives \(\mathcal{V}_n(\mathbf{E}_{i,j}^{(2)})=2^{\eta_n}\) for every pair \(1\le i<j\le n\), while V_<sub>n</sub>_(**I**_<sub>n</sub>(R_))=_R_ for every positive integer _R_. Consequently,

\(\mathcal{V}_n(\mathbf{G}_{n,2})=2^{\genfrac(){pt}{2}{n}{2}\eta_n}=2^{n^2/4}.\)

Monotonicity now gives Theorem 1.2. Multiplicativity gives the same bound for tensor powers, and positivity allows a common auxiliary expression to be cancelled. If the diagonal budget is _R<sub>N</sub>h<sub>N</sub>_ for the _N_-th power and log<sub>2</sub>_h<sub>N</sub>=o(N_), the resulting inequality is \(\mathrm{log}_2R_N\ge Nn^2/4-\mathrm{log}_2h_N\). Dividing by _N_ proves the asymptotic barrier. The certificate is defined on formal expressions and is not asserted to be a spectral point on all complex tensors; the conclusion bounds the exponents obtainable from the specified rules.

Together, Theorems 1.1 and 1.2 explain the role of 9/4 in this method. It is the _n_=3 instance of _n_<sup>2</sup>/4, the continuous balanced-cut value for complete graphs, and it is also the threshold detected by the operational certificate. For even _n_, this value is an actual cut size, so the upper bound is exact. For odd _n_, the maximum cut is smaller by 1/4, while the stated polynomial constructions retain the threshold _n_<sup>2</sup>/4. The barrier locates the limitation of these constructions; it leaves open whether that extra 1/4 is present in the true asymptotic rank.

