<tbc>\(p\in[0,\frac{1}{2})\) in time _O(n_log_n_) remains an interesting open problem.  1 compares the state-of- the-art works with our result.

To design RiffleSort we develop two sub-routines, NoisySearch and BasketSort, both of which can be of independent interest. NoisySearch takes _O_(log_n_) time to report an approximate rank of an external element _x_ w.r.t. an approximately sorted sequence having dislocation at most _d_ when only noisy comparisons between _x_ and the elements in the sequence are allowed. The reported rank differs from the true rank by at most _O(d_) with high probability. BasketSort re-sorts an approximately sorted sequence having _m_ elements and maximum dislocation at most _d_ and returns, with high probability, a sequence having maximum dislocation _O_(log_m_) and total dislocation _O(m_) in time \(O(d\cdot m)\). We note that NoisySearch works for any constant error probability \(p<\frac{1}{2}\), while BasketSort requires \(p<\frac{1}{4}\), i.e., the constraint on _p_ of RiffleSort is due to the analogous constraint in BasketSort. These algorithms answer Question 2 and Question 3, for their respective ranges of _p_.

## 1.2 Other related work

Computing with errors is often considered in the framework of a two-person game called _Rényi- Ulam Game_. In this game, a questioner tries to identify an unknown object _x_ from a universe _U_ by asking yes-or-no questions to a responder, but some of the answers might be wrong. The case in which _U_={1_,...,n_}, the questions are of the form "is _s\>x_?", and each answer is independently incorrect with probability \(p<\frac{1}{2}\) has been considered by Feige et al. \[15\], as we already mentioned. Ben-Or and Hassidim \[6\] then showed how to find _s_ using an optimal amount of queries up to additive polylogarithmic terms. The variant in which responder is allowed to adversarially lie up to _k_ times has been proposed by Rényi \[28\] and Ulam \[31\], which has then been solved by Rivest et al. \[29\] using only log_n+k_log_logn+O(k_log_k_) questions, which is tight. Among other results, near-optimal strategies for the distributional version of the game have been devised in \[14\]. For more related results, we refer the interested reader to \[27\] for a survey and to \[13\] for a monograph.

Regarding other sorting algorithms not mentioned before, Braverman et al. \[9\] studied algorithms which use _a bounded number of rounds_ for some "easier" versions of sorting, e.g., distinguishing the top _k_ elements from the others. The comparisons to be performed in each round are decided a priori, i.e., they do not depend on the results of the comparisons in the round. In each round, a fresh set of comparison outcomes is generated, and each round consists of \(\delta\cdot n\) comparisons. They evaluate the quality of an algorithm by estimating the number of "misclassified" elements and also consider a variant in which errors result in missing (rather than incorrect) comparison results.

Ajtai et al. \[3\] provided algorithms using _subquadratic_ time (and number of comparisons) when errors occur only between elements whose difference is at most some fixed threshold. Also, Damaschke \[14\] gave a subquadratic-time algorithm when the number _k_ of errors is known in advance.<tbc>

\begin{tabular}{cccc}
**Time** & **Maximum Dislocation** & **Total Dislocation** & **Reference** \\
_O(n_<sup>3+_f(p_)</sup>) & _O_(log_n_) w.h.p. & _O(n_) w.h.p. & \[10\] \\
_O(n_<sup>2</sup>) & _O_(log_n_) w.h.p. & _O(n_log_n_) w.h.p. & \[23\] \\
\(\widetilde{O}(n\sqrt{n})\) w.h.p. & _O_(log_n_) w.h.p & _O(n_) expected & \[19\] \\
_O(n_log_n_) & _O_(log_n_) w.h.p. & _O(n_) w.h.p. & \multirow{2}{*}{**this work**} \\
Any & \(\Omega(logn)\) w.h.p. & \(\Omega(n)\) expected & \\
\end{tabular}

1. Summary of the state-of-the-art. Here, _f(p_) is some function of _p_. The upper bound on _f(p_) resulting from the derivation in \[10\] is \(\frac{110525}{(1-2p)^4}\) . The notation \(\widetilde{O}(g(n))\) is a shorthand for _O(g(n_)polylog_n_).

