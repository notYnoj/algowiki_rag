4. **Adaptive stopping criterion**: saturation-based termination that keeps the recovery cost negligible relative to the hardware run being post-processed, with a bounded worst case.<tbc>

5. **Application of cluster updates to Rydberg atom array MIS**: We apply the cluster updates previously developed for classical solvers and superconducting annealers on quadratic binary optimization problems without field terms \[11\], to independent sets sampled by neutral atom hardware, with a feasibility argument showing that the exchange respects the independence constraint by construction.

The remainder of this paper is organized as follows. Section II describes the instances studied, quantum hardware setup, Houdayer cluster update algorithm, MIS repair procedure, and the stopping criterion. Section III presents amplification results, classical improvements, discovery dynamics, and efficiency analysis. Section IV discusses implications, limitations, and connections to related work. Section V concludes with future directions.

## II. METHODS

Our approach follows the hybrid quantum-classical workflow illustrated in Figure 1. Quantum hardware runs on QuEra’s Aquila quantum device generate an initial pool of candidate solutions for each problem instance. These quantum-generated samples are then passed to a classical post-processing pipeline based on Houdayer cluster updates \[11, 12\], which systematically recombine solution pairs to discover further distinct configurations at the same set size. Whether that size is the true optimum depends on the seed pool and is established separately in Section II F. The expanded solution pool is validated and the amplification factor is recorded. Throughout, S<sub>0</sub> denotes the seed pool, the distinct repaired solutions at the largest size _k_ reached in the hardware record, and S<sub>final</sub> the solutions held at the final size \(k_\mathrm{final}\ge k\) once post-processing terminates. The amplification factor is their ratio, _A=N_<sub>total</sub>_/N_<sub>quantum</sub>=|S<sub>final</sub>|/|S<sub>0</sub>|, with _N_<sub>quantum</sub>=|S<sub>0</sub>| and _N_<sub>total</sub>=|S<sub>final</sub>|. For the three instances whose size improved, _A_ and all aggregate statistics use the first pass at the seed size, and their pools at the improved size are reported in Section III D. The following subsections describe each component of the pipeline.

### A. Problem Instances

We evaluate our approach on 43 problem instances sourced from quantum hardware runs on QuEra’s Aquila quantum device from the study in Ref. \[7\], spanning three categories that cover a wide range of problem sizes and hardness regimes.

The **Benchmark Competition** category comprises four site-diluted union-jack graph instances (`HP125`, `HP1412`, `HP1435`, and `HP1478`), each with 137 atoms on a square lattice of side length _L_=14 \[7\]. The instance labels are mnemonics for the hardness parameter _H_ of Ref. \[7\] rather than a literal digit-by-digit encoding of it (`HP1478`, `HP1412`, `HP125`, and `HP1435` denote _H_=1.478, 14.12, 125.5, and 1435, respectively). The hardness parameter is the classical, conductance-like degeneracy ratio _H=D_<sub>|MIS|-1</sub>/(|MIS|_D_<sub>|MIS|</sub>), where \(D_\alpha\) is the number of independent sets of size \(\alpha\) \[16\], and the QAA success probability is suppressed exponentially in _H_ \[7\]. These four values range from near-trivial to seemingly intractable for unassisted QAA. The reference data of Refs. \[7, 17\] record _D_<sub>|MIS|-1</sub> for the other 39 instances, so _H_ is available for all 43 and spans 1.03 to 9717.

The **Hard** category comprises nine instances (115 to 231 atoms) on which Ref. \[7\] ran its qReduMIS pipeline on hardware. Their seeds come from the full-graph QAA runs of the same reference, as for the other families (Section IIB). On these instances the classical reduction rules stall before the kernel is eliminated, leaving a residual subproblem that quantum hardware is used to unblock, making them among the most challenging optimization problems in the dataset.

The **Standard test bed** category comprises thirty _L_=3 - _L_=16 instances (\(n=L\times L\) lattice sites and with 7 - 205 atoms) from the QAA hardware test bed \[4, 7\]. These fully-reducible instances span a wide range of problem sizes and graph structures arising from the unit disk constraint. Full instance specifications and quantum measurement data for both categories are provided in Refs. \[7, 17\].

### B. Quantum Hardware and Solution Seeds

Each problem instance is encoded as a unit disk graph on QuEra’s Aquila quantum device, where atoms are positioned at graph vertices and the Rydberg blockade radius defines graph connectivity \[4, 6\]. The device executes a time-dependent Hamiltonian evolution governed by global Rabi frequency and detuning controls, with the problem structure encoded through the atomic positions together with the blockade radius, which is itself set by the laser parameters. Following Ref. \[7\], with \(\hbar=1\), the Hamiltonian is

\(\mathcal{H}(t)=\frac{\Omega(t)}{2}\sum_i\left(e^{\mathrm{i}\phi(t)}|0\rangle_i\langle 1|+\mathrm{h}.\mathrm{c}.\right)-\delta(t)\sum_in_i+\sum_{i<j}V_{ij}n_in_j,\text{(1)}\)

where \(|0\rangle_i\) and \(|1\rangle_i\) are the ground and Rydberg states of atom _i_, \(n_i=|1\rangle_i\langle 1|\) is its occupation operator, \(\Omega(t)\) and \(\phi(t)\) are the Rabi frequency and phase of the global drive, and \(\delta(t)\) is the laser detuning. The interaction

