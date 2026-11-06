# GOLDEN RATIO GROWTH AND PHASE TRANSITIONS IN CHROMATIC COUNTS OF CIRCULAR CHORD GRAPHS

Abstract. We study generalized circular chord graphs \(\mathcal{C}_n^{(k)}\), formed from a cycle _C<sub>n</sub>_ by adding fixed-offset chords of length _k_ and, for even _n_, diameters. Using transfer matrix methods, we derive exact formulas for 3-colorings when _k_=3: for odd _n_, we obtain

where _L<sub>n</sub>_ is the Lucas sequence and (_s<sub>n</sub>_) satisfies _s_<sub>_n_+3</sub>=-_s_<sub>_n_+2</sub>-_s<sub>n</sub>_, yielding golden-ratio asymptotic growth \(\varphi^n+O(\rho^n)\) along odd indices. For even _n_, we construct a paired-window transfer matrix that exactly enumerates \(P(\mathcal{C}_{2m}^{(3)},3)\) while capturing diameter constraints. The chromatic counts exhibit pronounced modular patterns across residue classes without universal vanishing rules (see OEIS A383733). We provide efficient algorithms for exact enumeration and demonstrate applications to cyclic scheduling problems where these results serve as feasibility engines for airline gate assignment, wireless sensor networks, and multiprocessor task coordination.

### 1. Introduction

Graph coloring traces its origins to the four-color problem and connects combinatorics with algebraic methods through the chromatic polynomial _P(G,x_), which counts proper _x_- colorings of graph _G_ [3, 18]. Classical families exhibit well-understood behavior: cycles satisfy _P(C<sub>n</sub>,x_)=(_x_-1)_<sup>n</sup>_+(-1)_<sup>n</sup>(x_-1) and show parity-driven oscillations [22]. By contrast, circulant and circulant-like graphs with edges at fixed modular offsets remain comparatively underexplored from the viewpoint of exact chromatic polynomials [2].

This paper studies a natural circulant-type family we call generalized circular chord graphs, denoted \(\mathcal{C}_n^{(k)}\): starting from the cycle _C<sub>n</sub>_, we add fixed-offset chords of length _k_, and for even _n_ we also add diameter edges. The resulting graphs are vertex-transitive and interpolate between sparse cycles and denser circulant structures. For _k_=3 and _q_=3 colors we observe chromatic phase transitions manifesting as modular patterns in \(P(\mathcal{C}_n^{(3)},3)\) across residue classes of _n_. These transitions are driven by the interplay of cycle edges, _k_-chords, and diameter constraints, creating distinct structural regimes where the chromatic feasibility changes systematically with _n_."

Methodologically, we combine optimized backtracking with transfer-matrix constructions. Our main theoretical contributions for _k_=3, _q_=3 are: (i) for odd _n_ we derive an exact spectral decomposition yielding a precise order-7 linear recurrence and asymptotic law \(P(\mathcal{C}_n^{(3)},3)=\varphi^n+O(\rho^n)\) with dominant base \(\varphi=(1+\sqrt{5})/2\); (ii) for even _n_ we construct a paired-window transfer matrix that exactly enumerates \(P(\mathcal{C}_{2m}^{(3)},3)\) and captures residue-class effects; (iii) for general (_k,q_) we show that \(P(\mathcal{C}_n^{(k)},q)=tr(A_{k,q}^n)\) for a finite matrix _A<sub>k,q</sub>_, establishing that \(n\mapsto P(\mathcal{C}_n^{(k)},q)\) satisfies a linear homogeneous recurrence.

arXiv:2509.05845v1 [math.CO] 6 Sep 2025

ROGELIO N. LOPEZ-BONILLA, JULIAN ALLAGAN, SHAWN M. LANGLEY, AND ANGEL J. CLINTON

