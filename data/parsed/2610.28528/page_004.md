<tbc>_V<sub>ij</sub>=C_<sub>6</sub>/|**x**_<sub>i</sub>_-**x**_<sub>j</sub>_|<sup>6</sup> is the van der Waals coupling between atoms at positions **x**_<sub>i</sub>_ and **x**_<sub>j</sub>_, with _C_<sub>6</sub> the van der Waals coefficient. Unlike the zero-field spin glasses for which Houdayer cluster updates were developed \[12\], this Hamiltonian contains a field term, the detuning \(\delta(t)\) acting on every _n<sub>i</sub>_. At the conclusion of each quantum anneal, whose duration is of order microseconds, projective site-resolved measurements yield a classical bit string indicating the Rydberg state of each atom. Raw outcomes that violate independence constraints due to finite blockade strength or imperfect adiabaticity are repaired using the procedure described in Section IID. Repeating this process over many shots yields an initial pool S<sub>0</sub> of distinct solutions at the largest size the hardware attained, which Section IIF compares against the certified optimum.

All 43 seed pools derive from direct anneals on the full problem instance (1000 shots per instance \[7\], of which 49 to 946, median 426, survive post-selection for correct atom loading), and the repair step leaves most of each measurement intact: on average 92% to 94% of the atoms<tbc>

<tbc>in a repaired seed come from the measurement itself for the 30 standard instances, and 90% to 93% for the nine hard instances. For the hard family these are the vanilla QAA runs on the full graph that Ref. \[7\] reports as the baseline for its qReduMIS pipeline, not the kernel measurements taken inside that pipeline. The qReduMIS pipeline itself is considerably stronger and reaches the optimum on all nine instances.

Across our 43-instance dataset, the seed pools hold between 2 and 493 distinct solutions (mean 57.0, median 16). On six instances (`L12\_seed2922`, `L14\_seed1590`, `L14\_seed2358`, `L14\_seed2480`, `L15\_seed3591`, and `L17\_seed424`) only one solution reaches the best MIS size, and the implementation pairs it with the best solution one atom smaller, so their pools of two include that solution. On 35 of the 43 instances that size is the certified optimum (Section IIF). Eighteen instances yielded fewer than 10 unique solutions, 16 produced between 10 and 99, and 9 produced between 100 and 493. This regime ranging between approximately 10 and a few hundred solutions is characteristic of quantum annealers,<tbc>

a
Si quantum seed, |s| = 16
Sj quantum seed, |s| = 16
G[Aij], = = S, = Sj
S'
new solution, |s'| = 16
3
2
i
+
=
5
6
b
3
in the independent set
shared backbone Si n Sj
node of a Aij cluster
swapped in
swapped out
not selected
b
next pair
select pair (si, Sj)
find clusters in G[Aij]
enumerate 2c candidates
repair & filter
pool Sfinal
pool Sfinal
c = 8 here
28 = 256
256 valid, 254 new

FIG. 1. Houdayer cluster update mechanism for ground-state manifold amplification. **(a)** A single update, shown on a real instance from our data set (`atoms\_L8\_seed3066`: 51 atoms, 135 unit-disk edges, |MIS|=16) and read left to right as an identity. Two solutions _s<sub>i</sub>_ and _s<sub>j</sub>_ returned by the QuEra Aquila hardware, both of optimum size 16, are combined into their symmetric difference \(\Delta_{ij}=s_i\oplus s_j\). Atoms belonging to a solution are drawn as filled blue markers and unselected atoms as open circles. The 8 atoms selected in both solutions form the shared backbone (blue squares) and are untouched by the update; the 16 atoms of \(\Delta_{ij}\) (orange diamonds) split into _c_=8 disjoint connected components of \(G[\Delta_{ij}]\), numbered and joined by bars. Exchanging the atoms of any one cluster between the two solutions yields a distinct independent set of the same size; the fourth lattice shows the result \(s'\) for cluster 1, where one atom is swapped in (bold diamond) and one swapped out (dotted outline). Because the clusters are disjoint and the backbone is preserved, each of the _c_ clusters can be exchanged independently, so this single pair generates 2_<sup>c</sup>_=256 candidate configurations. For this pair all 256 are independent sets of size 16, the maximum for this instance, and 254 of them are new, illustrating why no Metropolis-style rejection step is required. **(b)** Algorithm flow, annotated beneath each step with the corresponding numbers for the pair in (a). Quantum measurements provide the seed pool S<sub>0</sub>, of size _N_<sub>quantum</sub>; the algorithm iterates over pairs drawn from that pool, enumerating and repairing 2_<sup>c</sup>_ candidates per pair. Iteration continues until saturation (newly discovered solutions over a 500-pair sliding window fall below 0.1% of the current pool size), exhaustive pair processing, or a computational budget of 10<sup>5</sup> pairs, yielding _N_<sub>total</sub> solutions with amplification factor _A=N_<sub>total</sub>_/N_<sub>quantum</sub>.

