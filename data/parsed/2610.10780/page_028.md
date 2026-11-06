Since the phase starts with \(|S\cap I|=O(m^{2/3}n^{2/3}(\mathrm{log}^{(i-1)}q)^4)\), the first outcome can occur only _O_(log<sup>(_i_)</sup>_q_) times before the second outcome must occur.<sup>2</sup> Unlike the symmetric case algorithm, we do not have an efficient test for whether the second outcome has already occurred. Instead, we simply run the phase for \(\hat{c}\mathrm{log}^{(i)}q\) iterations, where \(\hat{c}\) is a sufficiently large constant depending on \(\rho\) and _c_<sup>∗</sup>.

In the following, we describe a single iteration. For simplicity, we assume \(i\ge 3\). The cases _i_=1,2 are identical except for the running-time bounds. We assume that

\(|S\cap I_{j-1}|\ge c^*m^{2/3}n^{2/3}(\mathrm{log}^{(i)}q)^4,\)

since otherwise the second outcome already holds.

We first invoke the standard subroutine in _O(n_log_m_) time, obtaining a collection \(\Gamma\) of bicliques. We use index _p_ to refer to a recursive subproblem _T(q,q_) in Recurrence (11). For each subproblem _p_, it is associated with a subset \(A_p\subseteq A\) and \(B_p\subseteq B\) with \(|A_p|\le q\) and \(|B_p|\le q\). Let _S<sub>p</sub>_ denote the set of interpoint distances between _A<sub>p</sub>_ and _B<sub>p</sub>_. Depending on the context, _S<sub>p</sub>_ may also refer to the corresponding point pairs.

Let _S_<sub>0</sub> denote the set of distances of _S_ that are not in _S<sub>p</sub>_ for any subproblem _p_. Then _S_<sub>0</sub> and the sets _S<sub>p</sub>_ for all subproblems _p_ form a partition of _S_. Moreover, \(S_0\cap I_{j-1}\) is precisely the set of distances recorded by \(\Gamma\).

For every subproblem _p_, we apply Theorem 3 to (_A<sub>p</sub>,B<sub>p</sub>_) and _I_<sub>_j_-1</sub> with parameter _i_. This produces a collection of bicliques \(\Gamma_p\) in _O(q_<sup>4/3</sup>/(log<sup>(_i_)</sup>_q_)<sup>2</sup>) time. Since there are _O(r_<sup>2</sup>) subproblems, the total running time is \(O(r^2)\cdot O(q^{4/3}/(\mathrm{log}^{(i)}q)^2)=O(m^{2/3}n^{2/3}/(\mathrm{log}^{(i)}q)^2)\).

Let \(N(\Gamma_p)\) denote the number of pairs recorded by \(\Gamma_p\).

We call a subproblem _p bounded_ if \(N(\Gamma_p)\le c_1q^{4/3}(\mathrm{log}^{(i)}q)^4\), where _c_<sub>1</sub> is the constant from Theorem 3; otherwise _p_ is _unbounded_. Let _P_<sub>1</sub> and _P_<sub>2</sub> denote the sets of bounded and unbounded subproblems, respectively. Define \(S_1=\bigcup_{p\in P_1}S_p\), \(S_2=\bigcup_{p\in P_2}S_p\), and \(S_{02}=S_0\cup S_2\). Then _S_<sub>02</sub> and _S_<sub>1</sub> form a partition of _S_.

For every bounded subproblem \(p\in P_1\), Lemma 6 implies that \(|S_p\cap I_{j-1}|=O(q^{4/3}(\mathrm{log}^{(i)}q)^4)\). Since there are _O(r_<sup>2</sup>) bounded subproblems, \(|S_1\cap I_{j-1}|=O(m^{2/3}n^{2/3}(\mathrm{log}^{(i)}q)^4)\). Hence, for some constant \(c'>0\),<tbc>

\(|S_1\cap I_{j-1}|\le c'm^{2/3}n^{2/3}(\mathrm{log}^{(i)}q)^4.\)

<tbc>Combining this with the assumption on \(|S\cap I_{j-1}|\) yields

\(|S_1\cap I_{j-1}|\le\frac{c'}{c^*}|S\cap I_{j-1}|.\) (12)

Observe that _S_<sub>1</sub> plays exactly the role of the distances of the unresolved pairs in the symmetric analysis.

For the bicliques in \(\Gamma\) and in all collections \(\Gamma_p\) with \(p\in P_2\), we construct expander graphs and form a weighted distance set _E_ exactly as in Section 5.1. The total size of the bicliques in \(\Gamma\) is _O(n_log_m_), while the total size of all bicliques in \(\Gamma_p\) over all \(p\in P_2\) is \(O(r^2)\cdot O(q^{4/3}/(\mathrm{log}^{(i)}q)^2)=O(m^{2/3}n^{2/3}/(\mathrm{log}^{(i)}q)^2)\). Hence, constructing all expander graphs and the set _E_ takes _O(n_log_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>/(log<sup>(_i_)</sup>_q_)<sup>2</sup>) time.

Finally, we test the values of _E_ exactly as in Section 5.1, using Lemma 15 in place of Theorem 2. This yields an interval _I<sub>j</sub>_.

Since only _O_(1) quasi-decision calls are required, the total running time of the iteration remains _O(n_log_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>/(log<sup>(_i_)</sup>_q_)<sup>2</sup>).

<sup>2</sup>Note that for _i_=1, the number of candidate distances decreases from _O(m_<sup>2</sup>) to _O(m_<sup>2/3</sup>_n_<sup>2/3</sup>(log_q_)<sup>4</sup>). Since _m_<sup>2</sup>/(_m_<sup>2/3</sup>_n_<sup>2/3</sup>(log_q_)<sup>4</sup>)=_q_<sup>2/3</sup>/(log_q_)<sup>4</sup>, this requires only _O_(log_q_) iterations.

