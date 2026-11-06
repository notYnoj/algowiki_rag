## 7.1 SETH-hardness of exact string alignment with preprocessing

The Strong Exponential Time Hypothesis is an (extreme) strengthening of \(\mathsf{P}\neq\mathsf{NP}\) postulating that _k_-SAT on _n_ variables requires \(2^{(1-\delta_k)n}\) time. Building on \[AHWW16\], we can prove our hardness based on the milder BP-SETH which replaces _k_-CNF with a branching program:

_Hypothesis_ 1 (BP-SETH). Given a branching program over _n_ variables of width _W_ and length _T_ such that _T<sup>W</sup>_=2<sup>_o(n_)</sup>, deciding whether it has a satisfying assignment requires time 2<sup>(1-_o_(1))_n_</sup> time.

_Theorem_ 17 (BP-SETH hardness).

_Unless BP-SETH is false, there is no algorithm that preprocesses two input strings in polynomial time and then computes their (edit distance / longest common subsequence / dynamic time warping) in truly-subquadratic time._

_Remark._ We remark that unlike with _k_-SAT, it is plausible that the brute-force algorithm for BP- SAT is optimal to within poly(_n_) factors, and in fact better algorithms would imply new circuit lower bounds (\[AHWW16\] and references therein). Under a corresponding strengthening of BP-SETH one can show that string alignment with preprocessing requires _N_<sup>2</sup>/polylog(_N_) time.

The proof of Theorem 17 builds on _alignment gadgets_ and _normalized vector gadgets (NVG)_ from previous works on SETH and BP-SETH hardness of string alignment \[BI18, BK15, AHWW16\]. Each NVG represents a half-assignment to the branching program, and the alignment gadgets define a composition of the NVGs into two long strings. Here we deviate from typical SETH-hardness proofs of sequence similarity, and use a divide-and-conquer approach of \[WW18\] to construct two larger sets of shorter strings. This allows us to reuse the preprocessing of each shorter string when we compare every pair to look for a satisfying assignment (aka a satisfying pair of half-assignments).

Below we use dist() to refer to the distance under the relevant similarity measure (edit distance / longest common subsequence / dynamic time warping); for longest common subsequence we use the "co-LCS" (edit-distance-without-substitutions) distance dist(_A,B_):=_n_-LCS(_A,B_).

## Normalized Vector Gadgets

Given a BP \(\varphi\) of width _W_ and length _T_, _normalized vector gadgets_ (NVG) map half assignments \(a,b\in\{0,1\}^{n/2}\) into strings such that:

\(\mathrm{dist}(\mathrm{NVG}_A(a),\mathrm{NVG}_B(b))=\left\{\begin{array}{ c c }
c_T & \text{if assignment}(a\circ b)\text{satisfies}\varphi; \\
c_F & \text{otherwise}
\end{array}\right.,\)

where _c<sub>T</sub>\<c<sub>F</sub>_ are integers that depend on _W,T_.

_Lemma_ 18 (Normalized Vector Gadgets \[AHWW16\]).

_Given a BP of width W and length T, we can construct NVGs of length T_<sup>_O_(log(_W_))</sup>) _for all half assignments_ \(a,b\in\{0,1\}^{n/2}\) _in time_ \(2^{n/2}\cdot T^{O(\mathrm{log}(W))}\)).

## Alignment Gadgets

Consider two ordered sets of strings A,B of cardinalities _n<sub>A</sub>\<n<sub>B</sub>_, respectively. An alignment \(\mu\) is a monotone partial mapping from A to \(\mathcal{B}\cup\{\perp\}\). An alignment \(\mu\) is _structured_ if it maps the _i_-th string in A to the \(i+\Delta\) string in B for some fixed shift \(\Delta\) and for all \(a\in\mathcal{A}\).

The cost of a mapping \(\mu\) is defined by:<tbc>

\(\mathrm{cost}(\mu,\mathcal{A},\mathcal{B}):=\sum_{a\in\mathcal{A}}\mathrm{dist}(a,\mu(a)).\)

