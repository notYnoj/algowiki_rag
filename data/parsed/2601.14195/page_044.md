## 8 Conclusion

We studied a family of natural optimisation problems arising from stable matching theory and initiated the study of a minimax notion of almost-stability. Through examples and experiments, we showed that minimax almost-stability is a viable alternative to previously studied notions of almost-stability, bringing its own unique advantages and challenges.

Across bipartite and general settings, our results, a subset of which are summarised in  3, reveal a sharp contrast between very strong intractability and tractable special cases, such as when preference lists are very short. In particular, we highlight that while the problems aiming to minimise either blocking pairs or blocking agents can be solved in exponential time in the optimum parameter value (i.e., the problems lie in the complexity class XP with respect to this parameter), this is not the case for our new problem variants, which are NP-hard even for a fixed optimum parameter value. This naturally raises the question of whether other parameters can restore computational tractability when kept small.

Beyond their algorithmic significance, these findings also carry implications for multi-agent systems. In many practical applications where centralised coordination mechanisms are sought, solutions need to be robust to agent incentives to deviate, even when full stability is unattainable, and fairness considerations are crucial. We presented a new approach and characterised the computational possibilities and limits of achieving such robustness. Finally, we showed that although the intractability results hold even under strong restrictions, the ILP models that we proposed can be solved very efficiently in practice, thus posing an applicable tool to real-world settings. Simultaneously, our experiments showed that a balanced solution that distributes the burden of instability well is usually attainable in practice, often requiring no agent to experience<tbc>

\begin{tabular}{cccccccc}
 & & \multicolumn{4}{c}{SRI} & \multicolumn{2}{c}{SMI} \\
 & & \multicolumn{2}{c}{Minimax-Max} & \multicolumn{2}{c}{Minimax} & \multicolumn{2}{c}{Minimax-Max} \\
 & & m-mm-bp & avg. time (s) & m-mm-bp & avg. time & m-mm-bp & avg. time (s) \\
\multirow{3}{*}{_n_=50} & _l_=5 & 2 & _\<_0.38 & 1 & _\<_0.35 & 3 & _\<_0.32 \\
 & _l_=15 & 1 & _\<_0.38 & 1 & _\<_0.35 & 1 & _\<_0.32 \\
 & _l_=25 & 1 & 0.38 & 1 & 0.35 & 0 & 0.32 \\
\multirow{3}{*}{_n_=100} & _l_=5 & 3 & _\<_1.07 & 1 & _\<_1.02 & 4 & _\<_0.82 \\
 & _l_=15 & 2 & _\<_1.07 & 1 & _\<_1.02 & 2 & _\<_0.82 \\
 & _l_=25 & 2 & 1.07 & 1 & 1.02 & 2 & 0.82 \\
\multirow{3}{*}{_n_=200} & _l_=5 & 4 & _\<_4.36 & 1 & _\<_4.63 & 5 & _\<_3.23 \\
 & _l_=15 & 5 & _\<_4.36 & 1 & _\<_4.63 & 4 & _\<_3.23 \\
 & _l_=25 & 5 & 4.36 & 1 & 4.63 & 4 & 3.23 \\
\end{tabular}

\begin{tabular}{ccc}
 & SRI & Max-SMI \\
MinBP & P (\(d\le 2\)) \[9\], XP (\(\kappa\)) \[1\] & P (\(d\le 2\) and CL) \[10\], XP (\(\kappa\)) \[10\] \\
(\(\kappa=min|bp(M)|\)) & NP-h (\(d\le 3\) and CL) \[1, 9\], W\[1\]-h (\(\kappa\)) \[12\] & NP-h (\(d\le 3\)) \[10\] \\
MinBA & P (\(d\le 2\)) \[24\], XP (\(\kappa\)) \[12\] & P (\(d\le 2\) and CL) \[10\], XP (\(\kappa\)) \[10\] \\
(\(\kappa=min|ba(M)|\)) & NP-h (\(d\le 5\) \[12\] and CL \[24\]), W\[1\]-h (\(\kappa\)) \[12\] & NP-h (\(d\le 3\)) \[10\] \\
Minimax<sup>∗</sup> & P (\(d\le 2\)) \[T5.1\] & P (\(d\le 2\) and CL) \[T5.2,\(\top\)\] \\
(\(\kappa=minmax|bp_i(M)|\)) & NP-h (\(\kappa=1\), \(d\le 10\) and CL) \[T4.1-4.2\] & NP-h (\(\kappa=1\), \(d\le 3\)) \[T4.4\] \\
\end{tabular}

2: Experimental results: worst case mm-bp and average timing

3: Overview of key complexity results. Here, _d_ denotes the maximum preference list length (also denoted by _d_<sub>max</sub> in other parts of the paper), and CL indicates complete preference lists. Our contributions are coloured in blue. The following symbols are used: \(\top\) (result holds trivially), <sup>∗</sup> (we newly introduced these problems).

