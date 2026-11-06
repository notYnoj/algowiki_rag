## A Update and Emit Pseudocode

Algorithm 1 lists one batch of the streaming update (§3.5). Phase A advances every anchor’s sliding state and inserts the new signatures, splitting any directory whose population exceeds its occupancy bound (Prop. 4). Phase B forms candidates from the exact-prefix bucket and its margin-ordered Hamming-1 neighbors, rejects them with the Parseval bound (Lemma 2), computes exact distances for the survivors, and buffers the cell updates privately. Phase C merges the buffers in a fixed order, which is what makes the output independent of the thread schedule (Prop. 5). Algorithm 2 lists the emit stage (§3.6). It runs the hot-class sieve, then refinement to a fixpoint, then the final zero-snap and top-_k_ selection. As throughout, \(R=\gamma\alpha\) is the per-query verification budget.

**Algorithm 1** Update: one batch at the anchor lengths

Require: batch endpoints \(\tau_0,\dots,\tau_1,\tau_1-\tau_0+1=\beta\le excl\); anchors A<br>
 publish the \(\beta\) samples \(\triangleright\) batch pairs invalid (§3.5)<br>
 for all \(a\in A\) in parallel do \(\triangleright\) phase A: state<br>
   for \(\tau=\tau_0,\dots,\tau_1\) do<br>
   if \(\tau+1<a\) then continue<br>
   end if<br>
   \(q\leftarrow\tau-a+1\)<br>
   update moments and X<sub>1...K-1</sub>; form F<sub>q,a</sub> \(\triangleright\) Lemma 1<br>
   compute b<sub>a</sub>(q) and margins; insert q by prefix<br>
   if population \>\(\alpha 2^{da}\) then split to depth d<sub>a</sub>+1 \(\triangleright\) Prop. 4<br>
   end if<br>
   end for<br>
   end for<br>
   for all \((a,\tau)\in A\times\{\tau_0,\dots,\tau_1\}\) in parallel do \(\triangleright\) phase B: candidates<br>
   if \(\tau+1<a\) then continue<br>
   end if<br>
   \(q\leftarrow\tau-a+1\)<br>
   form Q<sub>a</sub>(q) from exact and margin-ordered Hamming-1 prefixes<br>
   for all \(c\in Q_a(q)\) do<br>
   if \(\underline{\mathrm{d}_{K,a}}(q,c)\ge\mathrm{max}(best_q,\hat{P}_a[c])\) then continue \(\triangleright\) Lemma 2<br>
   end if<br>
   \(\delta\leftarrow\mathrm{d}_\alpha(q,c)\) exactly<br>
   update best<sub>q</sub>; buffer candidate-endpoint update<br>
   end for<br>
   end for<br>
   for all \(a\in A\), fixed order do \(\triangleright\) phase C: merge<br>
   apply the query and candidate endpoint minima<br>
end for

**Algorithm 2** EMIT: sieve, refine to fixpoint, report

1: **for all** anchor a, bucket C with |C|\>R do \(\triangleright\) sieve<br>
   sort C by \(\langle g,F.\rangle\); verify each member against w sort neighbors; min-update \((\hat{P}_a,\hat{I}_a)\)<br>
   end for<br>
   repeat \(\triangleright\) refinement, \(\le P_\mathrm{max}\) rounds<br>
   \(\mathcal{A}\leftarrow\text{top cells of the current profiles}\)<br>
   for all \((m,i)\in\mathcal{A}\) with neighbor j (index or hint) do<br>
   recheck \(\{m\pm\Delta_m\}\times\{i\pm\Delta_p\}\times\{j\pm\Delta_p\}\) exactly; on improvement<br>
write cell and hint<br>
   end for<br>
until no improvement<br>
snap d \<\(\varepsilon_0\) to 0; return top-k under the m/2 overlap rule

## B Notation

2 collects the symbols used throughout the paper. Calligraphic letters denote sets of comparison triples, and hatted symbols denote maintained quantities, as opposed to their exact counterparts.

## C Deferred Proofs

This appendix completes every claim the paper states without proof. Six statements of §3 defer their proofs here, one lemma appears here for the first time, and one step that §3.2 uses without derivation is carried out in full. Lemma 2 states that the truncated spectral sum of §3.2 never exceeds the exact z-normalized distance, and that the cap \(K'\) prevents a frequency bin and its mirror image from being counted twice when the window is shorter than twice the retained width. Proposition 2 states that no spectral width can invalidate an output, because the bound stays a lower bound at every width and a width change alters only the set of evaluated pairs. Proposition 4 states that splitting a directory whenever its population crosses the occupancy threshold keeps the mean bucket size near the target \(\alpha\), at rehoming cost that amortizes to a constant per insertion. Proposition 3 states that the probability that every anchor misses a matchable pair is the product of the per-anchor miss probabilities, because each anchor draws its own projections. Lemma 3 states that the closest pair of a hot class lands within a few positions of each other when the class is sorted by one random projection. Proposition 5 states that the emitted motifs are identical for every thread count and schedule. The new statement is Lemma 4. The feature cache is the largest memory consumer (§3.7), so Panache stores features in single rather than double precision (§3.2). Rounding perturbs every stored coefficient, and a bound computed from perturbed features can come out larger than the true bound. Larger is the dangerous direction, since an overestimated lower bound could discard a pair whose exact distance would have survived the test. The implementation therefore shrinks every computed bound by \(1-\lambda\) before the comparison, and the lemma proves the shrink covers the rounding error whenever the bound is large enough to prune at all. Single precision halves the cache, and the bound stays a true lower bound. The proofs below derive every inequality they use. The uncovered step, the vanishing geometric sum in the proof of Lemma 1, is completed first.

Geometric sum in Lemma 1. The proof in §3.2 uses that _G<sub>k,m</sub>_, the sum of \(e^{-2\pi ik/m}\) over _r_=0_,...,m_-1, vanishes when \(k\neq 0\) (mod _m_). The sum is a geometric series with ratio \(q=e^{-2\pi ik/m}\). For \(k\neq 0\) (mod _m_) the ratio satisfies \(q\neq 1\), so the series sums to<tbc>

\begin{tabular}{cc}
_T_, _n_ & time series and its length \\
\(m\in[m_\mathrm{min},m_\mathrm{max}]\), _L_ & window length; interval size \\
_T<sub>i,m</sub>_, _Z<sub>i,m</sub>_ & window at start _i_; its z-normalized form \\
d<sub>_m_</sub>(_i,j_) & z-normalized Euclidean distance \\
_excl_ & exclusion radius for valid pairs \\
_P<sub>m</sub>_, \(I_m\); \(\hat{P}_m\), \(\hat{I}_m\) & exact and maintained profile rows \\
U; S; P<sup>S</sup> & comparison universe; evaluated set; induced profile \\
\(\tau\); _q_ & stream time (latest sample); window start \\
_A_, _a_, _s_ & anchor set; an anchor length; anchor stride \\
\(K,K'\) & retained spectral width; aliasing-safe cap \\
_F<sub>i,m</sub>_ & normalized non-DC spectral feature vector \\
\(\underline{\mathrm{d}_{K,m}}(i,j)\) & Parseval lower bound on d<sub>_m_</sub>(_i,j_) \\
_B_; \(b_a(i)\); \(g_{a,\ell}\) & signature width; a signature; a projection \\
_d_, _d_<sub>0</sub> & directory depth; probe reference depth \\
\(\alpha\); \(\gamma\); \(R=\gamma\alpha\) & occupancy target; multiplier; verification budget \\
\(\beta\) & micro-batch size (\(\beta\le excl\)) \\
_w_ & sieve neighbor width \\
\(\Delta_m\), \(\Delta_p\), P<sub>max</sub> & refinement radii and round cap \\
\(\eta\); \(\theta_K\) & energy-capture threshold; sampled feature angle \\
\(\lambda\); \(\varepsilon_0\) & bound shrink factor; zero-snap threshold \\
\(\varphi\) & fraction of candidates reaching exact evaluation \\
\end{tabular}

** 2: Symbols used throughout the paper.**

