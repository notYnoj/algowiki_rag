## 8 Conclusion

In this paper, we considered a simple premise: some agents can initiate blocking pair-based deviations, and some agents cannot. We aimed to answer the following question from a computational complexity point of view: Can we find desirable matchings in which no deviator is incentivised to deviate? The short answer is yes, but only under strong assumptions on the input. Our key insights are summarised in  1 and reveal a sharp contrast between strong intractability and tractable special cases.

We conclude with a number of open questions. For instance, on the parametrised complexity front, are the problems Deviator-sri and Deviator-Max-sri in FPT with respect to just |_D_|, rather than the combined parameter (|_D|,d_<sub>max</sub>)? We conjecture that the answer is no, as it might be the case that \(|D|\checkmark d_\mathrm{max}\), but our current reductions rely on the fact that _D_ is sufficiently large. It would also be interesting to study approximation algorithms in the setting of deviator stability, although we highlight that strong inapproximability results for almost- stable matchings are known \[1, 8, 12\] and that we proved that even deciding whether there exists a matching where no deviator is blocking is NP-complete. Thus, it might be interesting to study algorithms that give guarantees with respect to the number of deviators that are in no or in few blocking pairs, while ignoring the remaining deviators. Lastly, on a more practical front, it would be interesting to design, deploy and study real-world multi-agent systems using deviator-stable matchings - how do we accurately identify deviators in practice, and are there sufficiently few to render our parametrised algorithms efficient?

### Statements and Declarations

Frederik Glitzner is supported by a Minerva Scholarship from the School of Computing Science, University of Glasgow.

### Acknowledgements

The authors would like to thank the anonymous reviewers for helpful comments and suggestions on an earlier version of this paper. In particular, two comments led to Remarks 3.3 and 3.6.

\begin{tabular}{ccc}
 & sri & Max-sri \\
MinBP & P (\(d\le 2\)) \[7\], XP (\(\kappa\)) \[1\] & P\(^\dagger\) (\(d\le 2\) and CL) \[8\], XP\(^\dagger\) (\(\kappa\)) \[8\] \\
(\(\kappa=\mathrm{min}|bp(M)|\)) & NP-h (\(d\le 3\) and CL) \[1, 7\], W\[1\]-h (\(\kappa\)) \[11\] & NP-h\(^\dagger\) (\(d\le 3\)) \[8\] \\
MinBA & P (\(d\le 2\)) \[T7.1\], XP (\(\kappa\)) \[11\] & P\(^\dagger\) (\(d\le 2\) and CL) \[8\], XP\(^\dagger\) (\(\kappa\)) \[8\] \\
(\(\kappa=\mathrm{min}|ba(M)|\)) & NP-h (\(d\le 5\) \[11\] and CL \[T7.2\]), W\[1\]-h (\(\kappa\)) \[11\] & NP-h\(^\dagger\) (\(d\le 3\)) \[8\] \\
Minmax & P (\(d\le 2\)) \[25\] & P\(^\dagger\) (\(d\le 2\) and CL) \[\[25\],\(^\top\)\] \\
(\(\kappa=\mathrm{minmax}|bp_i(M)|\)) & NP-h (\(\kappa=1\), \(d\le 10\) and CL) \[25\] & NP-h\(^\dagger\) (\(\kappa=1\), \(d\le 3\)) \[25\] \\
Deviator\(^*\) & P (\(d\le 2\)) \[T6.1\] & P (\(d\le 2\)) \[T6.2\] \\
(\(\kappa_1=|D|\), & FPT ((\(d,\kappa_1\))) \[C4.4\] & FPT ((\(d,\kappa_1\))) \[C4.2\] \\
\(\kappa_2=\mathrm{min}|\bigcup_{a_i\in D}bp_i(M)|\)) & XP ((\(\kappa_1,\kappa_2\))) \[C4.4\] & XP ((\(\kappa_1,\kappa_2\))) \[C4.2\] \\
 & NP-h (\(\kappa_2=0\), \(d\le 5\) and CL) \[T3.5\] & NP-h\(^\dagger\) (\(\kappa_2=0\), \(d\le 3\)) \[T3.1\] \\
Deviator-BA\(^*\) & P (\(d\le 2\)) \[T6.1\] & P (\(d\le 2\)) \[T6.2\] \\
(\(\kappa_1=|D|\), & FPT ((\(d,\kappa_1\))) \[C5.5\] & FPT ((\(d,\kappa_1\))) \[C5.5\] \\
\(\kappa_2=\mathrm{min}|ba(M)\cap D|\)) & XP ((\(\kappa_1,\kappa_2\))) \[C5.5\] & XP ((\(\kappa_1,\kappa_2\))) \[C5.5\] \\
 & NP-h (\(\kappa_2=0\), \(d\le 5\) and CL) \[T5.1\] & NP-h\(^\dagger\) (\(\kappa_2=0\), \(d\le 3\)) \[T5.1\] \\
\end{tabular}

1: Overview of complexity results. Here, _d_ denotes the maximum preference list length (also denoted by _d_<sub>max</sub> in other parts of the paper), and CL indicates complete preference lists. Our contributions are coloured in blue. The following symbols are used: \(^\top\) (result holds trivially), † (positive result only established for bipartite smi instances), ‡ (negative result holds even for bipartite smi instances), \* (we newly introduced these problems).

