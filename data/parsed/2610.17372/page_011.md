\(\bullet\) Waiting vs traversal: traversal time \(T_\mathrm{trav}=\sum_\mathrm{hops}t_{uv}\tau\) and waiting time _T_<sub>wait</sub>=T_<sub>pq</sub>-T_<sub>trav</sub>, and waiting fraction _f<sub>w</sub>=T_<sub>wait</sub>/T_<sub>pq</sub>_.<tbc>

\(\bullet\) Temporal density: snapshot-wise average degree \(\bar{k}_t(R)\) over _t_=1_,...,M_ (Fig. 7) and summary statistics ( 7).

These metrics validate the intended behavior of the model: under intermittent contacts, shortest communication time depends not only on hop count but also on waiting induced by misalignment with feasible runs in _CS<sub>pq</sub>_.

## 6.8 Implementation Details and Reproducibility

All experiments are run on a Linux workstation (Ubuntu 22.04) equipped with a 64-thread AMD EPYC-class CPU, 256 GB RAM, and an NVIDIA A100 GPU (80 GB) used for data-parallel kernels where applicable.

Temporal-graph construction and analysis are implemented in Python 3.11 using NumPy/Pandas. Connectivity strings are stored in both (i) unpacked boolean arrays (for debugging and baseline agreement tests) and (ii) bit-packed form (for scalable run detection and memory efficiency). Performance-critical loops (e.g., searching for contiguous runs and updating candidate tuples) are JIT-compiled with Numba. All configuration files (orbital parameters, \((\tau,M)\),<tbc>

Interval 1
Interval 2
Interval 3
Interval 4
S4
S4
S3
S4
S3
S4
S3
S3
S5
S3
S5
S2
S2
S2
S2
S2
S2
S6
S17
S17
S6
S17
S17
S17
S18
S18
S16
S16
S1
S18
S16
S1
S18
S16
S1
S7
S7
S7
S7
S19
S15
S0
S19
S15
S0
S19
S15
S0
S19
S15
S0
S8
S8
S8
S20
S22
S14
S20
S22
S14
S20
S22
S14
S20
S22
S14
S20
S22
S14
S9
S9
S21
S9
S21
S9
S21
S9
S21
S13
S13
S13
S10
S12
S10
S12
S10
S12
S11
S11
S12
S11
S11
S11
S12
focus=S7 1 degree=6
focus=S7 1 degree=5
focus=S7 1 degree=7
focus=S7 1 degree=5

Connectivity storyboard (23 satellites) across four snapshot intervals Snapshot 0 (t=0s) Snapshot 1 (t=30s)
neighbors=22
neighbors=22
Snapshot 2 (t=60s)
Snapshot 3 (t=90s)
neighbors=22
neighbors=21

Selected Satellite Connectivity Across Four Snapshot Intervals

Fig. 4. Selected satellite connectivity across four snapshot intervals (sample1). A focus satellite (S7) and its incident edges are shown over four consecutive snapshots in a 23-node neighborhood. Highlighted links indicate feasible contacts in each snapshot; interval-wise degree annotations quantify neighborhood churn that induces waiting under time-respecting routing.

Fig. 5. Connectivity storyboard (23 satellites) across four snapshot intervals. A focus satellite (blue) and its time-varying neighbors (orange) are shown over four consecutive snapshots. The visualization emphasizes that adjacency is time dependent; temporal routes must follow time-ordered contact opportunities captured by connectivity strings \(CS_{pq}^{(R)}\).

