Finally, we confirm that the exponentially high probability bound holds on _n_ for the in-place, randomized algorithm. By Lemma 2.4 and (D.2), across all instances there are a total of \(k\le n\) cache inserts. Since failed probes accumulate monotonically with each insertion, we couple the actual execution with a hypothetical one that performs exactly _n_ insertions using the same random bits. Under this coupling, the actual number of failed probes _p_ is stochastically dominated by the number of failed probes in the _n_-insertion process. Paralleling the reasoning of [App. C], we therefore obtain the same tail bound on _p_:

\(Pr[p>2n]\le Pr[NB(n,1/2)>2n]\le(27/32)^n\)

## E Notation Glossary

In this glossary, notation is grouped by section. Each table provides the definition of relevant notation in the context of their respective sections.

\begin{tabular}{cc}
**Notation** & **Definition** \\ _m_ & Number of active elements. \\ _A_ & Block of all _m_ active elements to be sorted. \\ _B_ & Block of 3_m_-1 buffer elements, identifiable from active elements by a single comparison. \\ _V_ & Bit vector of _m/_lg<sup>2</sup>_m_ bits. reading requires 1 comparison, writing 3 moves. \\ \end{tabular}

\begin{tabular}{cc}
**Notation** & **Definition** \\ _F_ & Frame memory, part of _B_ containing frame elements. \\ _G_ & Cache memory, part of _B_ made up of cache lines. \\ _S_ & Segment memory, part of _B_ made up of segments. \\ _r\#_ & Number of frame elements/cache lines/segment pointers/cache integers. \\ _s\#_ & Number of additional segments, i.e. segments exluding _S_<sub>0</sub>. \\ _fi_ & The _i_th frame element in _F_. \\ _f'i_ & The _i_th active frame element in _F_. \\ _Gi_ & The _i_th cache line in _G_, corresponding with _fi_. \\ _G'i_ & The _i_th active cache line in _G_, corresponding with _f'i_. \\ _g_ & Max capacity of a cache line. \\ _Si_ & The _i_th segment in _S_, corresponding with _f'i_. \\ _s_ & Length of a segment. \\ _P_ & Pointer data in _V_. \\ _Pi_ & The _i_th segment pointer in _P_, corresponding with _fi_. \\ _P'i_ & The _i_th active segment pointer in _P_, corresponding with _f'i_. \\ _Ii_ & The _i_th cache integer in _I_, corresponding with _Gi_. \\ _I'i_ & The _i_th active cache integer in _I_, corresponding with _G'i_. \\ _Ri_ & The _i_th representative, a compound data type formed by _fi_, _Gi_, _Pi_ and _Ii_. \\ _R'i_ & The _i_th active representative, corresponding with _Si_. Defined as _Rj_ where _j_ is the _i_th smallest value such that _fj_ is active. \\ \end{tabular}

** E.1:** Section 2 Notation

** E.2:** Section 2.1 Notation

