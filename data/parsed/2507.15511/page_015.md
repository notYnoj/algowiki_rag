### 6.2 Refining SETH Lower Bounds

Our view reframes unconditional 2<sup>_n/_2</sup> hardness claims for general Subset-Sum: such claims are meaningful primarily on the structure-resistant slice Subset-Sum\(^{\ge\delta}\). We state this formally.

_Theorem_ 7 (SETH under entropy constraints)_. Assume SETH. Then no_ \(O^*(2^{\epsilon n})\) _algorithm can solve all of_ Subset-Sum\(^{\ge\delta}\) _for any_ \(\epsilon<\delta\).

_Proof sketch._ Take a collision-resistant reduction from _k_-SAT that maps instances to \((S,t)\in\text{Subset-Sum}^{\ge\delta}\) with polynomial blowup. If an \(O^*(2^{\epsilon n})\) algorithm existed for all such (_S,t_) with \(\epsilon<\delta\), composing would yield an \(O^*(2^{\epsilon^\prime m})\) algorithm for _k_-SAT with \(\epsilon'<1\), contradicting SETH.

## 7 Proof-of-Concept Experiments

We provide _proof-of-concept_ experiments to sanity-check the theory. The goal is not a systems study but to verify that the observed running time tracks the structural parameter that our analysis identifies. We benchmark on synthetic instances where we can precisely control structure, using _n_=48 so that full per-half enumeration is feasible on a commodity desktop CPU. Throughout we split _S_ into two halves by alternating indices, so each half has size _k=n/_2=24. For each instance we fully enumerate _both_ halves to obtain \(U_0:=|\Sigma(\ell_0)|\) and \(U_1:=|\Sigma(\ell_1)|\), and we measure wall-clock time of the deterministic enumerator (hashing disabled) to avoid randomness. Our hypothesis is that introducing additive redundancy collapses _U<sub>i</sub>_, and runtime scales proportionally with _U_<sub>0</sub>+_U_<sub>1</sub> (hence with \(\widehat{U}:=max\{U_0,U_1\}\) for fixed _n_).

We manipulate three knobs known to induce subset-sum collisions: numeric density, duplicate elements, and additive progressions. For each setting we run the _full_ certificate construction on each half (no early termination) to measure the cost of generating \(\Sigma(\ell_i)\). Additional methodology appear in Appendix D.

• **Numeric density.** Restricting values to a smaller bit-length _w_ forces collisions by the pigeonhole principle.<tbc>

• **Duplicate elements.** Introducing identical elements creates trivial additive dependencies.<tbc>

• **Additive progressions.** Planting short arithmetic progressions creates correlated dependencies.

### Results (sanity check).

We observe large, systematic variation in _U<sub>i</sub>_ under these perturbations: uniform-like inputs typically satisfy _U<sub>i</sub>_≈2_<sup>k</sup>_, whereas structured inputs collapse by orders of magnitude. For fixed _n_, the measured runtime of IC-SubsetSum varies proportionally with _U_<sub>0</sub>+_U_<sub>1</sub> (equivalently with \(\widehat{U}\) up to a factor 2), consistent with the proven \(O\big((U_0+U_1)n^2\big)\) bound. These experiments corroborate the central claim that _structure (collisions)_ \(\Rightarrow\) _smaller_ \(U\Rightarrow\) _faster enumeration_.

\begin{tabular}{ccc}
**Structural knob** & **Setting** & _U<sub>i</sub>/_2_<sup>k</sup>_ \\
Numeric density (_n_=48) & \(w=32\rightarrow 24\rightarrow 16\) & \(1.00\rightarrow 0.84\rightarrow 0.027\) \\
Duplicates (_n_=48) & \(0\rightarrow 2\rightarrow 4\) duplicates & \(1.00\rightarrow 0.57\rightarrow 0.32\) \\
Additive progressions (_n_=48) & 1 seq (len 4) / 2 seq (len 4) & 0.69 / 0.47 \\
\end{tabular}

1: Effect of structure on the per-half distinct-sum count. We report the ratio _U<sub>i</sub>/_2_<sup>k</sup>_ with _k=n/_2=24 (median over halves for a representative run).

