## 4 An Overview of the Algorithm

Our main result is a linear time algorithm for LCS with approximation factor _O(n_<sup>0.497956</sup>). We obtain this result through an array of combinatorial algorithms. In this section, we explain the intuition behind each algorithm and defer the details and proofs to Sections 6, 7, and 8. Our analysis involves nontrivial applications of Dilworth’s theorem, Mirsky’s theorem, and Turán’s theorem which may be of independent interest. Before we begin, let us first discuss how a linear time algorithm can approximate LCS within a factor \(\sqrt{n}\).

For a given pair of strings _s_ and <o>_s_</o>, we construct a string _s_<sup>∗</sup> from _s_ by removing each character of _s_ with probability \(1-1/\sqrt{n}\). Due to the construction of _s_<sup>∗</sup>, both \(|s^*|=O(\sqrt{n})\) and \(|\text{lcs}(s^*,\overline{s})|=\Omega(|\text{lcs}(s,\overline{s})|/\sqrt{n})\) hold w.h.p. Hence, it suffices to compute the LCS of _s_<sup>∗</sup> and <o>_s_</o>. To this end, we slightly modify the conventional dynamic program for computing LCS and construct a two-dimensional array _T_<sup>∗</sup> that stores the following information<tbc>

\(T^*[i][j]=\left\{\begin{array}{ c c }
\text{the smallest}k\text{s.t.} & \text{if}|\text{lcs}(s^*,\overline{s})|\ge j \\
|\text{lcs}(s^*[1,i],\overline{s}[1,k])|\ge j & \text{otherwise}
\end{array}\right.\)

<tbc>Using the above definition, we can construct table _T_<sup>∗</sup> via the following recursive formula:

\(T^*[i][j]:=\mathrm{min}\left\{\begin{array}{ c c }
T^*[i-1][j], & \text{first}(\overline{s},T^*[i-1][j-1],s_i^*) \\
\text{first}(\overline{s},T^*[i-1][j-1],s_i^*) & \text{if}(\overline{s},T^*[i-1][j-1],s_i^*)
\end{array}\right.\) (4.1)

where \(\text{first}(\overline{s},T^*[i-1][j-1],s_i^*)\) is the index of the first occurrence of \(s_i^*\) in <o>_s_</o> after position _T_<sup>∗</sup>\[_i_-1\]\[_j_-1\] (or \(\infty\) if \(s_i^*\) does not appear in <o>_s_</o> after position _T_<sup>∗</sup>\[_i_-1\]\[_j_-1\]). Notice that both _i_ and _j_ lie in range \[0,|_s_<sup>∗</sup>\]] which is bounded by \(O(\sqrt{n})\). In addition to this, \(\text{first}(\overline{s},T^*[i-1][j-1],s_i^*)\) can be computed in time _O_(log_n_) via a simple data structure and thus Algorithm 0 can be implemented in time \(O(\sqrt{n}^2\mathrm{log}n)=O(n\mathrm{log}n)\).

Observation 4.1. _With high probability, Algorithm 0 approximates LCS within a factor of_ \(\sqrt{n}\) _in near linear time_ (_O(n_log_n_)).

We improve Algorithm 0 through an array of combinatorial algorithms. To keep the analysis simple, for now, we only focus on beating the \(\sqrt{n}\) barrier and obtaining an approximation factor which is better than \(\sqrt{n}\) by a multiplicative factor of \(n^\epsilon\) for some \(\epsilon>0\). Thus, for the sake of simplicity, we define the notation <o>_O_</o> which is similar to the _O_ notation except that <o>_O_</o> hides all _n_<sup>_o_(1)</sup> factors.

Definition 1.<tbc>

\(f(n)\in\overline{O}(g(n))\Longleftrightarrow f(n)\in O(n^{o(1)}g(n)).\)

<tbc>We similarly define notations \(\overline{o},\overline{\Omega}\), and \(\overline{\omega}\) as follows:

Definition 2.<tbc>

\(f(n)\in\overline{o}(g(n))\Longleftrightarrow g(n)\notin\overline{O}(f(n))\)<br>
\(f(n)\in\overline{\Omega}(g(n))\Longleftrightarrow g(n)\in\overline{O}(f(n))\)<br>
\(f(n)\in\overline{\omega}(g(n))\Longleftrightarrow f(n)\notin\overline{O}(g(n))\)

