## D.1 Setup and Methodology

### Implementation.

All experiments use a single-threaded, 64-bit C++17 implementation compiled with `-03` and no target-specific vectorization. Wall-clock time is measured with high-resolution timers; each configuration is run for multiple independent seeds and we report the median together with the interquartile range (IQR). No parallelism or GPU acceleration is used.

### Metrics.

For each instance we record:

• \(U=|\Sigma(S)|\) (or per-half \(U_i=|\Sigma(\ell_i)|\) when using meet-in-the-middle),<tbc>

• the collision entropy _H<sub>c</sub>(S_)=_n_-log<sub>2</sub>_U_,<tbc>

• total number of extension attempts and collision resolutions, and<tbc>

• wall-clock time _T_ for full constructive-certificate enumeration.

When _U_ is small enough to store exactly, we count it via exact hashing. For larger _n_ where exact counting may be infeasible under memory limits, we estimate _U_ using a standard streaming distinct-counter (with sub-percent relative error at the configured memory budget); in those cases, only trend lines are reported. All qualitative trends are consistent with exact counts on smaller instances.

### Workloads.

We vary three structure "knobs" known to affect collisions:

a) _Numeric density:_ draw _a<sub>i</sub>_∼Unif({1_,...,_2_<sup>w</sup>_}) for several word sizes _w_,<tbc>

b) _Duplicates:_ start from a base multiset and inject \(d\in\{0,2,4,\dots\}\) extra copies of randomly chosen elements, and<tbc>

c) _Additive progressions:_ splice arithmetic-progressions of fixed length into otherwise uniform data.

Unless noted otherwise, we sort inputs once (for cache locality) but the algorithm does not rely on ordering for correctness.

## D.2 Extremely Dense Instances (_n_=100)

Here we stress-test the density knob by fixing _n_=100 and drawing elements from very small ranges \[1,2_<sup>w</sup>_\] with \(w\in\{12,16,20,24\}\). As _w_ decreases, collisions become pervasive and _U_ collapses far below the collision-free ceiling. In meet-in-the-middle terms, the per-half certificate sizes _U_<sub>0</sub>_,U_<sub>1</sub> drop by orders of magnitude relative to 2<sup>_n/_2</sup>.

_Observation._ Across densities, we observe a monotone relationship between _T_ and _U_: for fixed _n_, the median wall-time scales linearly with _U_ (up to polynomial factors in _n_), in line with Theorem 1 (deterministic \(O(U\cdot n^2)\)) and Theorem 2 (expected \(O(U\cdot n)\)). In particular, once \(U\checkmark 2^{n/2}\) due to density-induced collisions, runtime drops commensurately.

### Practical note.

For _n_=100 and large _w_, exact per-half certificates may exceed memory on commodity hardware; in those regimes we report consistent trends using streaming distinct-count estimates and terminate runs upon reaching a fixed memory cap. Full details and complete plots are provided in §6 of \[Sal25\].

