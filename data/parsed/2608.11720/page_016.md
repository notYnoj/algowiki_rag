<tbc>_Let_ E _be a finite-dimensional environment and let_ \(\rho\) _be a state on_ \(\mathsf{X}(1)\mathsf{X}(2)\cdots\mathsf{X}(n-1)\mathsf{E}\)_. Suppose that each vertex_ \(p\in[n-1]\) _measures_ X(_p_)Y(_p_) _in the maximally entangled basis, obtains outcome k<sub>p</sub>, and the corresponding correction P<sub>k<sub>p</sub></sub> is applied on_ Z(_p_+1)_. Then the resulting state on_ \(\mathsf{Z}(2)\mathsf{Z}(3)\cdots\mathsf{Z}(n)\mathsf{E}\) _is the reduced state obtained from_ \(\rho\) _by relabelling each_ X(_p_) _as_ Z(_p_+1)_, for_ \(p\in[n-1]\).

## 6.2. The Simulation Algorithm.

We refer to B from Theorem 3 as the simulation algorithm and to A as the original algorithm. Let us now describe the simulation algorithm formally. In Step (I), nodes prepare maximally entangled states in registers T (indexed by the round and direction in which they are used), and they share half of each maximally entangled state with their neighbors during Step (II). Note that Step (II) is the unique communication round of this algorithm. Step (III) implements _T_ rounds of wishful teleportation (see Figure 2 for an illustration). Steps (IV) and (V) perform the final measurement and produce the final output of algorithm B.

**Algorithm B.** One-Round Simulation of a _T_-round algorithm \(\mathcal{A}=(U_0,U_1,\dots,U_T,\Pi)\)

(I) Each vertex _p_ prepares registers \(\mathsf{L}_1(p)\otimes\mathsf{M}(p)\otimes\mathsf{R}_1(p)\) in the state \(U_0|000\rangle\), registers L_<sub>t</sub>(p_), R_<sub>t</sub>(p_) for \(t\in[2,T+1]\) in the state \(|0\rangle\), and the registers<tbc>

<tbc>\(\mathsf{T}_{t,L}(p)\otimes\mathsf{T}'_{t,L}(p)\text{and}\mathsf{T}_{t,R}(p)\otimes\mathsf{T}'_{t,R}(p)\)<tbc>

<tbc>in the maximally entangled state \(|\Phi\rangle\) for all \(t\in[T]\).<tbc>

(II) Using _one communication round_, for all _p_ and \(t\in[T]\) swap<tbc>

<tbc>\(\mathsf{T}'_{t,L}(p)\leftrightarrow\mathsf{R}_{t+1}(p-1)\text{and}\mathsf{T}'_{t,R}(p)\leftrightarrow\mathsf{L}_{t+1}(p+1).\)<tbc>

(III) For \(t\in[T]\) times and _with no communication_, each vertex _p_:<tbc>

(i) measures \(\mathsf{L}_t(p)\otimes\mathsf{T}_{t,L}(p)\) in the basis \(\{\Phi_k,k\in[d^2]\}\), obtains the outcome \(k_{t,L}(p)\in[d^2]\) and then applies the unitary _P<sub>k<sub>t</sub>,L</sub>(p_) on R<sub>_t_+1</sub>(_p_);<tbc>

(ii) measures \(\mathsf{R}_t(p)\otimes\mathsf{T}_{t,R}(p)\) in the basis \(\{\Phi_k,k\in[d^2]\}\), obtains the outcome \(k_{t,R}(p)\in[d^2]\) and then applies the unitary _P<sub>k<sub>t</sub>,R</sub>(p_) on L<sub>_t_+1</sub>(_p_);<tbc>

(iii) applies the unitary _U<sub>t</sub>_ on \(\mathsf{L}_{t+1}(p)\otimes\mathsf{M}(p)\otimes\mathsf{R}_{t+1}(p)\).<tbc>

(IV) Measure \(\Pi\) on \(\mathsf{L}_{T+1}(p)\otimes\mathsf{M}(p)\otimes\mathsf{R}_{T+1}(p)\) and obtains \(a(p)\in\Sigma\) as the outcome.<tbc>

(V) Vertex _p_ outputs<tbc>

(8) \(\lambda_p=(k_{1,L}(p),k_{1,R}(p),\dots,k_{T,L}(p),k_{T,R}(p),a(p)).\)

Compared to the Definition 3.1 of the quantum-PN model, Algorithm B uses mid-circuit measurements and unitaries with classical control. The well-known _principle of deferred measurement_ states that measurements can always be moved to the end of a quantum circuit, and that classically controlled operations can be substituted by conditional quantum gates \[NC10, Sec. 4.4\]. Therefore, B is still a one-round quantum-PN algorithm on directed cycles, in the same sense as in Definition 3.1.

As proven formally below, the simulation algorithm can be understood as having two behaviours. First, suppose the keys obtained in Step (III) are such that

(9) \(k_{t,L}(p)=k_{t,L}(p+1)\text{and}k_{t,R}(p)=k_{t,R}(p-1)\)

for every \(t\in[T]\). Then, the corrections _P<sub>k<sub>t</sub>,L</sub>(p_) and _P<sub>k<sub>t</sub>,R</sub>(p_) applied by vertex _p_ to the registers R<sub>_t_+1</sub>(_p_) and L<sub>_t_+1</sub>(_p_) lead to successful teleportations. Suppose this holds for all adjacent vertices inside an interval _J<sub>s</sub>_=\[_s,s_+2_T+r_-1\], where \(s\in[n]\) and the interval is understood cyclically. Then B correctly simulates A on the interval \[_s+T,s+T+r_-1\], which is at the center of _J<sub>s</sub>_

