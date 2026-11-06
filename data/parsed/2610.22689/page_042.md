<tbc>For state preparation, at the stage involving _k_ remaining qubits, the disentangling construction of Ref. \[26, Theorems 8-9\] uses at most 2_<sup>k</sup>_ one-qubit rotations and 2_<sup>k</sup>_-2 CNOTs. Including two rotations for the final one-qubit state gives

\(s_q^\mathrm{prep}\le 2+\sum_{k=2}^q2^k=2^{q+1}-2,\)

and

\(c_q^\mathrm{prep}\le\sum_{k=2}^q(2^k-2)=2^{q+1}-2q-2.\)

A state-to-state circuit is obtained by composing the inverse preparation circuit for \(|\psi\rangle\) with the preparation circuit for \(|\phi\rangle\). Doubling these counts gives

\(s_q^\mathrm{state}\le 2^{q+2}-4,c_q^\mathrm{state}\le 2^{q+2}-4q-4,\)

which proves (88).

## 1. Verification of Theorems VIII.5 and VIII.8

In this subsection, we present the constructive proofs and analytical verifications for the global circuit depth bounds established in Theorem VIII.5 for Pauli-generated full DLAs and Theorem VIII.8 for multi- angle MIS QAOA.

_Proof of Theorem VIII.5._ For a nonidentity Pauli string _P_, define its filtration depth by

\(\delta(P):=\mathrm{min}\{j|iP\in\mathcal{F}_j^\mathbf{a}\}.\)

The space \(\mathcal{F}_j^\mathbf{a}\) is spanned by left-nested Lie words of length at most _j_ in the native generators. Because every nonzero commutator of Pauli strings is proportional to a single Pauli string, and distinct Pauli strings are linearly independent, the inclusion \(iP\in\mathcal{F}_{\delta(P)}^\mathbf{a}\) implies that some nonzero nested Lie word of length at most \(\delta(P)\) is proportional to _iP_.

If _S_ and _Q_ are anticommuting Hermitian Pauli strings satisfying _SQ+QS_=0, then<tbc>

\(\mathrm{Ad}_{e^{\frac{\pi}{4}iS}}(iQ)=e^{\frac{\pi}{4}iS}(iQ)e^{-\frac{\pi}{4}iS}=-SQ.\)

<tbc>It follows recursively that _iP_ can be written in the form<tbc>

\(iP=\pm\mathrm{Ad}_V(iP_r),V=e^{\frac{\pi}{4}iP_{r_1}}\cdots e^{\frac{\pi}{4}iP_{r_{\ell-1}}},\ell\le\delta(P),\)

<tbc>for some native Pauli generator \(P_r\in\mathbf{a}\). Consequently, the targeted flow decomposes as<tbc>

\(e^{itP}=Ve^{\pm itP_r}V^{-1},\)

<tbc>which incurs at most

\(2\delta(P)-1\le 2\mathcal{D}_\mathbf{a}-1\)

primitive exponential steps, establishing (91).

In particular, since any single-qubit unitary \(U\in SU(2)\) can be parameterized via Euler rotations as

\(U=e^{i\frac{\alpha}{2}X}e^{i\frac{\beta}{2}Y}e^{i\frac{\gamma}{2}Z},\) (D1)

each constituent single-qubit rotation requires at most 2D**<sub>a</sub>**-1 native generator steps. Accounting for the three rotation axes yields the uniform bound

\(K_{1\mathrm{q}}\le 3(2\mathcal{D}_\mathbf{a}-1)=6\mathcal{D}_\mathbf{a}-3.\) (D2)

