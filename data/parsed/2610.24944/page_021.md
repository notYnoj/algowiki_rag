## A.7 MAX-4-CUT Hardness

The gadget in Section 5.4 gives the exact ratio 84931/86101, compared with 195581/198140 (Nagda et al., 2025). Integer edge weights make the gadget’s finite objectives recoverable without relying on floating-point optimizer output. The hardness statement uses the original reduction, with the improved weighted gadget substituted into it.

## A.8 Polyomino Growth: Klarner’s Constant

The number of fixed polyominoes grows exponentially at rate \(\lambda\). Extending the neighborhood recurrence method of Bui (2025), Épi improves the published upper bound 4.5238 to

\(\lambda\le\frac{429569}{100000}=4.29569.\)

The certificate covers 1,186 neighborhood types. A separate checker reconstructs the geometric rules, checks the recurrence dependencies and verifies the rational supersolution. Verifying the supersolution against every recurrence constraint establishes the bound for polyominoes of all sizes.

## A.9 Additive Combinatorics: _B<sub>h</sub>[g_] Sets

A _B<sub>h</sub>[g_] set has at most _g_ unordered representations of any integer as a sum of _h_ elements. For \(g\ge 2\), the framework of Timmons (2016) bounds the size of such a set \(A\subseteq[N]\) by

\(|A|\le(1+o_N(1))(C_hgN)^{1/h}.\)

Épi improves all five coefficients below. The published column follows Timmons’  1. The new values are rounded upward.

Each certificate supplies a rational cosine kernel. Interval arithmetic establishes its minimum on the full domain and propagates that bound to _C<sub>h</sub>_. Earlier and new kernels are evaluated by the same frozen implementation.

## A.10 Quartic Feigenbaum Attractor Dimension

Burbanks et al. (2021) give a rigorous enclosure of the quartic attractor’s Hausdorff dimension. Using their rigorous fixed-point enclosure, Épi proves

\(0.6425750638035370\le dim_H(A_4)\le 0.6425750659339700.\)

The published interval has endpoints 0.6395131468772885 and 0.6473156929016112 (rounded outward). The new interval has width \(2.130433\times 10^{-9}\), more than 3.6 million times narrower than the cited rigorous interval. A separate implementation checks the pressure inequalities throughout the domain.

\begin{tabular}{ccc}
**h** & **Published coefficient** & **Épi coefficient**\\
3 & 14.3 & 14.287390218082\\
4 & 71.49 & 70.289552594834\\
5 & 413.07 & 408.104453996958\\
6 & 2774.16 & 2749.492485514635\\
7 & 21294.74 & 21149.189776156220\\
\end{tabular}



** 6:** Improved upper-bound coefficients for _B<sub>h</sub>[g_] sets.

