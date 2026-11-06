If \(h_i\in A\cap B\), then \(M_{h_i}\subseteq\overline{B^{^{\prime\prime}}}\subseteq\overline{C}\). The preceding disjointness and equal sizes imply _Y<sub>i</sub>=M<sub>h<sub>i</sub></sub>_. Thus the two copies of _h<sub>i</sub>_ form an isolated edge in _G_.

If a vertex of \(e\in B\) has degree 0 in _G_, then \(M_e\cap Y_i=\emptyset\) for all \(h_i\in A\), which implies that \(M_e\subseteq\overline{B^{^{\prime\prime}}}\), and this implies that \(A\cup\{e\}\) is independent in the polymatroid on _N_ given by _f_(). This cannot happen when the two-for-one heuristic stops. We conclude that every vertex of _B_ has degree at least one in _G_.

We claim that we cannot have a vertex of _A_ adjacent in _G_ to two singletons in _B_. Indeed, assume that \(h_i\in A\) is adjacent to _e_ and _f_ distinct singleton vertices of _B_. Then \(A':=A\backslash\{h_i\}\cup\{e,f\}\) has size |_A_|+1, since the isolated-edge property gives \(e,f\notin A\), and is an independent set, as we argue next. _e_ being a singleton implies that all elements of \(M_e\cap\overline{B^{^{\prime\prime}}}\) are in _Y<sub>i</sub>_. Same reasoning applies to _f_. Therefore \(\cup_{g\in A^\prime} M_g\subseteq\left(\overline{A}\backslash M_{h_i}\cup Y_i\right)\cup\left(M_e\cap\overline{B^{^{\prime\prime}}}\right)\cup\left(M_f\cap\overline{B^{^{\prime\prime}}}\right)\subseteq\left(\overline{A}\backslash M_{h_i}\cup Y_i\right)\cup\overline{B^{^{\prime\prime}}}\). As \(\overline{A}\backslash M_{h_i}\cup Y_i\) is a basis in \(M'\), we have that \(\left(\overline{A}\backslash M_{h_i}\cup Y_i\right)\cup\overline{B^{^{\prime\prime}}}\) is independent in _M_, and from this we deduce that \(\cup_{g\in A^\prime} M_g\) is independent in _M_, which implies that \(A'\) is independent in the polymatroid on _N_ given by _f_(). This cannot happen when the two-for-one heuristic stops.

Now we compare |_A_| with |_B_| using the arguments from the base case (Case 2) in the proof of Theorem 1 of \[21\]. In _G_, the degree of a vertex \(h_i\in A\) is at most _k_, as \(|Y_i|=|M_{h_i}|=f(h_i)\le k\) and _M<sub>e<sub>j</sub></sub>_ is disjoint from _M<sub>e<sub>l</sub></sub>_, for \(e_j\neq e_l\), \(e_j,e_l\in B\). Partition _B_ into _S_ and _D_, where _S_ is the set of singletons in _B_, and _D_ are the remaining vertices of _G_ that are in _B_. All the vertices in _D_ have degree at least two, and thus \(k|A|\ge|E(G)|\ge|S|+2|D|\). From the previous paragraph, \(|A|\ge|S|\). Add these two last equations and obtain that \((k+1)|A|\ge 2|B|\), which implies the ratio of at least 2/(_k_+1) for the two-for-one swap heuristic.

**Note.** It may be more intuitive to contract \(\overline{A}\cap\overline{B}\) early in the proof, but readjusting the definitions will make this proof longer.

A
C
B
B'

Figure 1: Illustrating the definitions of <o>_A_</o> - the black rounded rectangle, \(\overline{B^{^{\prime\prime}}}\) - the empty blue rounded rectangle, \(\overline{B^{^{\prime\prime}}}\) - the filled blue rounded rectangle, and <o>_C_</o> - the red rounded rectangle. Keep in mind that \(\overline{B}=\overline{B^{^{\prime\prime}}}\cup\overline{B^{^{\prime\prime}}}\) and \(\overline{B^{^{\prime\prime}}}\cap\overline{B^{^{\prime\prime}}}=\emptyset\).

