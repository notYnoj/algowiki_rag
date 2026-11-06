# ENUMERATION OF ONE-CYCLE SIGNED CHORD DIAGRAMS AND THEIR DUALS FOR OPTIMAL MORSE FLOWS ON CLOSED SURFACES

A PREPRINT

**Alexandr Prishlyak**<br>
Taras Shevchenko National University of Kyiv, Ukraine<br>
`prishlyak@knu.ua`

October 15, 2026

**ABSTRACT**

Optimal Morse vector fields on closed surfaces, i.e. fields with the minimal possible number of critical points (a single source and a single sink), are classified up to topological trajectory equivalence by one-cycle signed chord diagrams Kybalko et al. (2018).We recall this construction and the associated duality, which corresponds to reversing the direction of the flow, in a unified encoding in which both endpoints of a chord carry the same label, and we make it algorithmic. We give an explicit traversal procedure that detects one-cycle diagrams, a canonical form of an equivalence class under cyclic shifts, reversal and relabeling of chords, and a construction of the dual diagram. On this basis we describe an algorithm that enumerates all one-cycle signed chord diagrams with a given number of chords, both for orientable and for non-orientable surfaces, groups them into equivalence classes, pairs each class with its dual, and identifies the self-dual ones. The algorithm is implemented in Python and archived in Zenodo; its output is validated against the Harer–Zagier numbers in the orientable case and against orbit-size counts in both cases. We also note that, when a one-cycle diagram is read as a cellular embedding of a one-vertex graph, its dual diagram describes the embedding of the dual graph.

**_Keywords_** Morse flow · topological classification · vector field · signed chord diagram · dual diagram · surface topology

### 1 Introduction

The topological classification of dynamical systems is a foundational problem in geometric topology and the qualitative theory of differential equations. Structurally stable systems are of particular importance because their qualitative phase portraits remain invariant under small _C_<sup>1</sup>-perturbations of the vector field Peixoto (1959); Palis and de Melo (1982). On closed surfaces, such structurally stable flows are precisely the Morse–Smale vector fields Peixoto (1973); Oshemkov and Sharko (1998); Kibkalo and Yokoyama (2022). Gradient-like systems and Morse flows arise naturally as gradient fields of Morse functions with respect to suitable Riemannian metrics Smale (1960, 1961).

According to Smale’s construction, an optimal Morse flow, that is, one with a single source and a single sink, specifies a polar Morse function once all saddle points are placed at the same critical level. In Fomenko’s topological classification of integrable Hamiltonian systems and of functions on surfaces Bolsinov and Fomenko (2004), such a structure is a simple atom with one input and one output, which corresponds to an edge of degree 2 in the associated Reeb (Kronrod– Reeb) graph Reeb (1946); Kronrod (1950); Kravchenko and Maksymenko (2019); Tereshchenko and Prishlyak (2024); Tereshchenko et al. (2025). The global topological structure of such flows is therefore encoded by one-cycle signed (marked) chord diagrams Kybalko et al. (2018).

Fine topological invariants and combinatorial structures for flows and functions on surfaces have been developed in many settings. For closed two-dimensional manifolds, combinatorial schemes, three-color graphs, chord diagrams and _F_-atoms were used to classify optimal flows, simple Morse functions and functions with non-degenerate critical points<tbc>



