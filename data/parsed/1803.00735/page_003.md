## 2 Quantum simulation of the _N_- queens problem

Following the idea of adiabatic quantum computation [16-18], we construct a classical problem Hamiltonian _H_pr such that its ground state corresponds to the solutions of the _N_-queens problem. In order to find this ground state, the system is evolved with the time-dependent Hamiltonian

\(H(t)=H_\mathrm{kin}+\frac{t}{\tau}H_\mathrm{pr}\) (1)

from _t_=0 to \(t=\tau\). Initially at _t_=0, the system is prepared in the ground state of _H_(0)=_H_kin. During the time evolution, the second term is slowly switched on. If this parameter sweep is slow enough, the system stays in the instantaneous ground state and finally assumes the ground state of \(H(\tau)\) at \(t=\tau\). If the lowest energy gap of _H_pr is much larger than the one of _H_kin, this state is close to the ground state of _H_pr and thus the solution of the optimization problem.

In the following we construct the problem Hamiltonian _H_pr and the driver Hamiltonian _H_kin. The system is modeled as a 2D Bose- Hubbard model with annihilation (creation) op erators \(b_{ij}\) (\(b_{ij}^\dagger\)) on the sites (_i,j_). A position of a queen is represented by the position of an atom in an optical lattice with the total number of atoms being fixed to _N_. The non-attacking condition between queens, which amounts to interactions between two sites (_i,j_) and (_k,l_), is implemented with four constraints: There can not be two queens on the same line along (i) the _x_- direction _j=l_, (ii) the _y_-direction _i=k_, the diagonals (iii) _i+j=k+l_ and (iv) _i-j=k-l_.

Condition (i) is implemented by using an initial state with one atom in each horizontal line at _y<sub>j</sub>_ and restricting the atomic movement to the _x_- direction [see Fig. 1(b)]. Thereby we use the a priori knowledge that a solution has one queen in a row, which reduces the accessible configuration space size from \(\genfrac(){pt}{2}{N^2}{N}\) to _N<sup>N</sup>_ configurations. In this vein the restricted tunneling Hamiltonian [32] is given by

\(H_\mathrm{kin}=-J\sum_{i,j=1}^N\hat{B}_{ij},\) (2)

where _J_ is the tunneling amplitude and \(\hat{B}_{ij}=b_{i,j}^\dagger b_{i+1,j}+b_{i+1,j}^\dagger b_{i,j}\) with \(\hat{B}_{Nj}=0\) are the tunneling operators.

Constraints (ii), (iii) and (iv) are enforced by infinite range interactions between the atoms with

\(H_\mathrm{Q}=U_\mathrm{Q}\sum_{ijkl=1}^NA_{ijkl}\hat{n}_{ij}\hat{n}_{kl},\) (3)

where \(\hat{n}_{i,j}=b_{i,j}^\dagger b_{i,j}\) and _U_<sub>Q</sub>_\>_0. The interaction matrix is

\(A_{ijkl}=\left\{\begin{array}{ c c } 3 & \text{if}(i,j)=(k,l) \\ 1 & \text{if}i=k\vee i+j=k+l\vee i-j=k-l \\ 0 & \text{otherwise},\end{array}\right.\) (4)

where in the first case all three constraints are broken.

In order to implement variations of the _N_- queens problem, we need to exclude diagonals (for the excluded diagonals problem) and pin certain queens (for the completion problem). These additional conditions are implemented by local energy offsets of the desired lattice sites

\(H_\mathrm{pot}=U_\mathrm{D}\sum_{i,j=1}^ND_{ij}\hat{n}_{ij}-U_\mathrm{T}\sum_{i,j=1}^NT_{ij}\hat{n}_{ij}.\) (5)

For _U_<sub>D</sub>_\>_0 the first term renders occupations of sites on chosen diagonals energetically unfavorable. Each diagonal (in + and - direction) has an index summarized in the sets D<sub>+</sub> and D<sub>-</sub>, respectively, and the coefficients are

\(D_{ij}=\left\{\begin{array}{ c c } 2 & \text{if}i+j-1\in\mathcal{D}_+\wedge i-j+N\in\mathcal{D}_- \\ 1 & \text{if}i+j-1\in\mathcal{D}_+\vee i-j+N\in\mathcal{D}_- \\ 0 & \text{otherwise}.\end{array}\right.\) (6)

For _U_<sub>T</sub>_\>_0, the second term favors occupations of certain sites. The sites where queens should be pinned to are pooled in the set T and therefore the coefficients are given by

\(T_{ij}=\left\{\begin{array}{ c c } 1 & \text{if}(i,j)\in\mathcal{T} \\ 0 & \text{otherwise}.\end{array}\right.\) (7)

The problem Hamiltonian of the _N_-queens problem with excluded diagonals is then

\(H_\mathrm{pr}=H_\mathrm{Q}+H_\mathrm{pot}.\) (8)

Note that due to the initial condition atoms never meet and sites are occupied by zero or one atom only. Hence the system can be effectively described by spin operators [31, 40], also without large contact interactions.

