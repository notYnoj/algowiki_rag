<tbc>for the longest common subsequence or the shortest common supersequence problems, which is impossible under SETH (see \[BK15, ABW15\]). For the min-variant of the subsequence relation or the max-variant of the supersequence relation, we show that a truly subquadratic algorithm would imply a faster algorithm for the Orthogonal Vectors problem, which is also impossible under SETH \[ABDN18, Wil05\]. On the positive side, however, we show that all these problems can be solved within the original matching complexity of \(O(|w|\cdot|r|)\), in particular generalising the fact that longest common subsequences and shortest common supersequences can be computed within this bound. We also show that the same upper bounds apply for the infix, prefix, and (left-)extension relations, and that they are all optimal under SETH.

In this regard, it is worth noting that both the max-variant for the subsequence relation and the min-variant for the supersequence relation properly extend the classical regex matching problem, since a matching maximum-length subsequence _u_ or minimum-length supersequence _v_ equals _w_ if and only if \(w\in\mathsf{L}(r)\). In fact, we could interpret _u_ and _v_ as a fuzzy measure for regex matching: The tighter _w_ is sandwiched in between _u_ and _v_, the more it can be interpreted as matching the regex _r_, where the optimum _u=v=w_ is reached when \(w\in\mathsf{L}(r)\).

Finally, we investigate the complexity of checking whether _all_ strings _u_ with \(u\unknown w\) match _r_. While it is easy to see that this can be solved efficiently for the infix and prefix relations, it becomes intractable for the (left-)extension, subsequence and supersequence relations. We pinpoint the complexity of all these variants (conditionally on SETH).

See s 1 and 2 for an overview of all our upper and lower complexity bounds.

## 1.2 Motivations and Related Work

Subsequences and supersequences play an important role in many different areas of theoretical computer science: in formal languages and logics (e.g., piecewise testable languages \[Sim72, Sim75, KS19, PSVV24\], or subword order and downward closures \[HSZ17, KZ19, Kus20, Zet16\]), in combinatorics on words \[RS15, FGK<sup>+</sup>15, Sek12, MSY04, Sal05, SV23\] or combinatorial pattern<tbc>

\begin{tabular}{cccc}
 & \(\unknown\)-matching & min/max-variant & universal-variant \\
subsequence & _O_(|_w|+m_) & _O_(|_w|m_) & coNP \\
supersequence & _O_(|_w|+m_) & _O_(|_w|m_) & PSPACE \\
infix & _O_(|_w|m_) & _O_(|_w|m_) & _O_(|_w_|<sup>2</sup>_m_) \\
prefix & _O_(|_w|m_) & _O_(|_w|m_) & _O_(|_w|m_) \\
extension & _O_(|_w|m_) & _O_(|_w|m_) & PSPACE \\
left-extension & _O_(|_w|m_) & _O_(|_w|m_) & PSPACE \\
\end{tabular}

\begin{tabular}{cccc}
 & \(\unknown\)-matching & min/max-variant & universal-variant \\
subsequence & -- & no \(O((|w|m)^{1-\epsilon})\) & coNP-hard \\
supersequence & -- & no \(O((|w|m)^{1-\epsilon})\) & PSPACE-hard \\
infix & no \(O((|w|m)^{1-\epsilon})\) & no \(O((|w|m)^{1-\epsilon})\) & no \(O(|w|^{2-\epsilon}\text{poly}(m))\) \\
prefix & no \(O((|w|m)^{1-\epsilon})\) & no \(O((|w|m)^{1-\epsilon})\) & no \(O((|w|m)^{1-\epsilon})\) \\
extension & no \(O((|w|m)^{1-\epsilon})\) & no \(O((|w|m)^{1-\epsilon})\) & PSPACE-hard \\
left-extension & no \(O((|w|m)^{1-\epsilon})\) & no \(O((|w|m)^{1-\epsilon})\) & PSPACE-hard \\
\end{tabular}

1: Upper bounds for the different problem variants. The problem \(\unknown\)-matching is to check whether there is a string \(u\unknown w\) that matches the regex, where \(\unknown\) is one of the string relations displayed in the first column; the min/max-variant computes a smallest/longest such string, and the universal variant checks if all strings \(u\unknown w\) match the regex. Note that _m_ is the size of the \(\varepsilon\)NFA (or, equivalently, the regular expression).

2: Conditional lower bounds for the different problem variants. All lower bounds are conditional on SETH. Note that _m_ is the size of the \(\varepsilon\)NFA (or, equivalently, the regular expression).

