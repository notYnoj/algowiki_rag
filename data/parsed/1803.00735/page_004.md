Let us illustrate the parameter sweep in Eq. (1) for a specific example instance with _N_=5 queens (see Fig. 1). The excluded diagonals chosen here restrict the ground state manifold to two solutions, and by biasing site (3,5) one of these solutions is singled out. The time evolution of the site occupations \(\langle\hat{n}_{ij}\rangle\) from numerically solving the time-dependent Schrödinger equation is shown in Fig. 2. Initially, the atoms are spread out in _x_-direction since the ground state of _H_(0)=_H_kin is a superposition of excitations along each tube. After evolving for a sufficiently large time \(J\tau/\hbar=49\), the system is in the ground state of _H_pr and thus assumed the solution of the optimization problem.

The energy spectrum of the given instance is shown in Fig. 3(a). The minimal gap between ground state (orange) and first excited state (green) determines the minimum sweep time \(\tau\) to remain in the ground state according to the Landau-Zener formula. At the end of the sweep, the ground state closely resembles the solution to the excluded diagonals problem shown in Fig. 1.

The Hilbert space for the atomic state corresponding to the configuration space mentioned above grows exponentially as _N<sup>N</sup>_ and thus, as usual for quantum systems, the computational costs get large for rather small systems. Simulations with significantly larger systems are hence not easily tractable.

## 3 Implementation

Here we propose a specific and at least conceptually simple and straightforward physical implementation of Eq. (1), where the _N_ queens are directly represented by _N_ ultracold atoms in an _N_x_N_ two-dimensional optical lattice. Assuming tight binding conditions the atoms are confined to the lowest band of the lattice. They can coherently tunnel between sites [51] and interact via collective light scattering within an optical resonator. To implement the required queens interactions via light scattering we make use of a set of optical field modes in a multi-mode standing- wave resonator [see Fig. 1(b)]. It was shown before that this configuration in principle allows to implement arbitrary site to site interactions [40] if a sufficient number of modes is used.

To reduce the necessary Hilbert space without loss of generality, it is sufficient to enable tunneling only along one dimension (_x_), e.g. the rows of the lattice and increase the lattice depth in the column (_y_) direction. This confines the atoms (queens) to move only along tubes in the _x_-direction forming a parallel array of _N_ 1D optical lattices as routinely used to study 1D physics with cold atoms [52].

Luckily, for the special case of the infinite range queens interactions, one can find a strikingly simple and intuitive example configuration requiring only few field modes for each of the three remaining queens interaction directions. For this we consider the optical lattice to be placed in the center symmetry plane of the optical resonator, where one has a common anti-node of all sym

Jt/h = 0 Jt/h = 7 Jt/h = 14 Jt/h = 21 1.0 0.8 Site occupations (nij) 0.6 Jt/h = 28 Jt/h = 35 Jt/h = 42 Jt/h = 49 0.4 0.2 y
0.0 x

(a) (b) 4
3 (En Eo)/J 2
1 0
0 10 20 30 40 0
10 20 30 40 Jt/h Jt/h

Figure 2: _Time evolution of site occupations._ - Each subplot shows a snapshot of the site occupations \(\langle\hat{n}_{ij}\rangle\) for the parameter sweep in Eq. (1) and a sweep time \(J\tau/\hbar=49\). This is the instance shown in Fig. 1a, where the excluded diagonals are indexed by D<sub>+</sub>={2,3,6,9} and D<sub>-</sub>={1,2,8,9} and one queen is pinned at site (3,5), i.e. T={(3,5)} (see text). The final values of the sweep are _U_<sub>Q</sub>=_J_, _U_<sub>D</sub>=5_J_, _U_<sub>T</sub>=2_J_ while _J_ is kept constant. Since the sweep time is large enough, the state of the system adiabatically converges to the unique solution of the problem, which can be easily verified.

Figure 3: _Energy spectrum._ - Eigenvalue spectrum of _H(t_) for (a) the model Hamiltonian [Eq. (1)] and (b) the Hamiltonian created by the field-atom interactions [Eq. (10)] for the instance described in Fig. 2. The orange and green lines show ground state and first excited state, respectively. The blue lines depict higher energy eigenstates. The low energy sector, and especially the minimal gap, are qualitatively similar.

