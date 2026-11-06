<tbc>For \(x(P)\ge 1\), select an _X_ site _a_ and a _Y/Z_ site \(b\in\mathrm{supp}(P)\). Define \(P'\) by replacing _X<sub>a</sub>_ with _Y<sub>a</sub>_ and _P<sub>b</sub>_ with _I<sub>b</sub>_. The resulting string \(P'\) has one fewer _X_ factor (_x_(\(P')=x(P)-1\)) while preserving the even parity of _Y/Z_ factors \((y(P')+z(P')=y(P)+z(P))\), giving a reduced support size of \(s(P')=s-1\).

Define the auxiliary two-body operator _B_:=_iZ<sub>a</sub>P<sub>b</sub>_. If _P<sub>b</sub>=Z_, _B=iZ<sub>a</sub>Z<sub>b</sub>_ is a fundamental generator (deg(_B_)=1); if _P<sub>b</sub>=Y_ , _B=iZ<sub>a</sub>Y<sub>b</sub>_ has degree deg(_B_)=2. Evaluating the Lie bracket \([B,iP']\) confirms that _iP_ is recovered (up to a non-zero scalar) via:<tbc>

\(iP\propto[iZ_aP_b,iP'].\) (C8)

<tbc>Applying the induction hypothesis \(\mathrm{deg}(iP')\le 2s(P')-1\) together with the filtration bracket compatibility property (33), we obtain

\(\mathrm{deg}(iP)\le\mathrm{deg}(iP')+\mathrm{deg}(iZ_aP_b)\le(2s(P')-1)+2=2(s-1)-1+2=2s-1,\)

completing the inductive step.

**Case 3: Pure** _X_ **strings (**_y_**(_P_)=_z(P_)=0**).** Let _t_:=_x(P_) denote the number of _X_ factors. By the basis conditions (C4), _t\<n_, so \(1\le t\le n-1\). If _t_=1, _P=X<sub>a</sub>_ is a single-qubit generator, so \(\mathrm{deg}(iP)=1\le 2n-1\). In case \(t\ge 2\), since _t\<n_, there exists at least one unoccupied site \(c\notin\mathrm{supp}(P)\) (_P<sub>c</sub>=I_). Select two distinct sites \(a,b\in\mathrm{supp}(P)\) and construct the auxiliary string \(P'\) by replacing _X<sub>a</sub>_ and _X<sub>b</sub>_ with _Y<sub>a</sub>_ and _Y<sub>b</sub>_, respectively. The string \(P'\) has \(x(P')=t-2\) and \(y(P')=2,z(P')=0\), yielding a total support size of \(s(P')=t\).

Since \(P'P'\) falls under Case 1 if _t_=2 (mixed string with \(y(P')+z(P')=2\)), and under Case 2 otherwise, its degree is bounded by \(\mathrm{deg}(iP')\le 2s(P')-1=2t-1\). Evaluating the double Lie bracket with the fundamental generators _iZ<sub>c</sub>Z<sub>a</sub>_ and _iZ<sub>c</sub>Z<sub>b</sub>_ (each of degree 1) confirms that _iP_ is recovered via:<tbc>

\(iP\propto[iZ_cZ_b,[iZ_cZ_a,iP']].\) (C9)

<tbc>Applying the filtration bracket compatibility property (33), we obtain

\(\mathrm{deg}(P)\le\mathrm{deg}(P')+1+1\le 2(x(P')+y(P')+z(P'))-1+2=2x(P)+1\le 2(n-1)+1\le 2n-1\)

Since every basis element of g<sub>_K<sub>n</sub>,_free</sub> falls into one of these three cases, every basis string _P_ satisfies \(\mathrm{deg}(iP)\le 2n-1\), establishing the stabilization bound \(\mathcal{D}_{\mathfrak{g}_{K_n,\mathrm{free}}}\le 2n-1\).

**Remark C.1.** The structural properties of the generators can be exploited to establish a straightforward linear lower bound on the filtration level of any given Pauli string. For any two Pauli strings _p_ and _q_, the support of their commutator is contained within the union of their individual supports, \(\mathrm{supp}([P,Q])\subseteq\mathrm{supp}(P)\cup\mathrm{supp}(Q)\). As the generators of \(\mathfrak{g}_{\Gamma,\mathrm{free}}\) are at most 2-local, commuting a Pauli string _P_ with a generator string _Q_ (where \(|\mathrm{supp}(Q)|\le 2\)) can increase the cardinality of the support of _P_ by at most \(|\mathrm{supp}(Q)|-1\le 1\). Consequently, if a basis element _P_ belongs to the minimal filtration component \(\mathcal{F}_m^{\mathfrak{g}_{\Gamma,\mathrm{free}}}\), its filtration index must satisfy \(m\ge k-1\).

_Proof of Theorem VII.5._ For _n_=2, the reduced generating set is {_iX_<sub>1</sub>_,iZ_<sub>1</sub>}, so its algebra is su(2) and its filtration stabilizes at degree \(2\le 2n-1\). Henceforth we assume \(n\ge 3\). Since vertex _v_ is connected to every other vertex in _K<sub>n</sub>_, its neighborhood is \(\mathcal{N}_v=V(\Gamma)\backslash\{v\}\), containing _n_-1 vertices. Consequently, every single- site operator _iZ<sub>w</sub>_ for \(w\in V(\Gamma_v)\) is a fundamental generator of the reduced Lie algebra \(\mathfrak{g}_{K_n,\mathrm{free}}^v\). Combining these with the generators _iX<sub>w</sub>_ yields the full single-site local algebra su(2) at each vertex \(w\in V(\Gamma_v)\) within the second filtration component.

To establish the depth bound, let \(\mathcal{Q}\neq I\) be a non-trivial string on the _n_-1 remaining qubits. We analyze the generation degree deg(_i_Q) across three exhaustive cases:

**Case 1: standard parity strings.** If Q satisfies the basis conditions (C4) on the complete graph _K_<sub>_n_-1</sub>, then by Theorem VII.3 applied to _n_-1 vertices, its generation degree is bounded by

\(\mathrm{deg}(i\mathcal{Q})\le 2(n-1)-1=2n-3\le 2n-1.\) (C10)

