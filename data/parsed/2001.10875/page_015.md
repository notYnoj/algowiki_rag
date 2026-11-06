## A.2 Correctness proof

Theorem 2, with accompanying Proposition 1, shows that Algorithm REDI always produces a regret-equal stable matching. Theorem 3 shows that Algorithm REDI runs in _O(d_<sub>0</sub>_nm_) time.

\(\blacktriangleright\) **Proposition 1.** _Let I be an instance of_ smi _and let M and_ \(M'\) _be stable matchings in I where for each man_ \(m_i\in U\)_,_ \(rank(m_i,M(m_i))\le rank(m_i,M'(m_i))\) _and_ \(d_U(M)=d_U(M')\)_. Let Q and_ \(Q'\) _denote the set of rotations eliminated from M_<sub>0</sub> _to reach M and_ \(M'\) _respectively. Then stable matching_ \(M''\) _with_ \(d(M'')=d(M')\) _may be found by ensuring all rotations in_ \(R_d=c(\{\rho\in R:\exists(m,w)\in\rho\text{\textit{where}}d_W(M)\ge rank(w,m)>d_W(M')\}\backslash Q)\) _are eliminated from M. Figure 5 shows a summary of degree pairs for M,_ \(M'\) _and_ \(M''\) _in the general case._

**Proof.** First, since \(rank(m_i,M(m_i))\le rank(m_i,M'(m_i))\) and each rotation must make some man worse off, we know that each rotation in _Q_ must be eliminated to reach \(M'\) and therefore \(Q\subseteq Q'\). Second, we also know that any rotation containing a woman at rank larger than \(d_W(M')\) must be eliminated from _M_ in order to reach \(M'\) (additional rotations may also have been eliminated). But these are precisely the rotations in _R<sub>d</sub>_, hence \(R_d\subseteq Q'\). Let \(M''\) be the stable matching found when eliminating _R<sub>d</sub>_ on _M_ and let \(Q''=Q\cup R_d\) denote the unique set of rotations corresponding to \(M''\). Then \(Q''\subseteq Q'\) since \(Q\subseteq Q'\) and \(R_d\subseteq Q'\).

We observe the following.

Since \(Q\subseteq Q''\), it must be that \(d_U(M)\le d_U(M'')\), and as \(d_U(M)=d_U(M')\), it follows that \(d_U(M')\le d_U(M'')\);<tbc>

<tbc>\(Q\cup R_d\) is the set of all rotations with pairs containing women of rank larger than \(d_W(M')\). Since \(Q''=Q\cup R_d\) and all rotations in \(Q''\) are eliminated on _M_<sub>0</sub> to reach \(M''\), it must be the case that \(d_W(M'')\le d_W(M')\);<tbc>

<tbc>Since \(Q''\subseteq Q'\), it must be that \(d_U(M'')\le d_U(M')\) and \(d_W(M'')\ge d_W(M')\).<tbc>

<tbc>Hence \(d(M'')=d(M')\) as required. \(\blacktriangleleft\)

\(\blacktriangleright\) **Theorem 2.** _Let I be an instance of_ smi_. Any matching produced by Algorithm REDI is a regret-equal stable matching of I._

**Proof.** There are four points in Algorithm 1’s execution where we return a matching, namely Lines 5, 10, 24 and 29. First we show that if _M_ is a matching returned at any of these points then _M_ is stable. Next we look at each of these points where a matching may be returned and show they are regret-equal stable matchings.

\begin{tabular}{ccccccccc}
_r(M_) & \multicolumn{8}{c}{Degree pairs (_d<sub>U</sub>(M),d<sub>W</sub>(M_))} \\
_k_ & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\
_d_<sub>0</sub>=4 & (2,6) & & & & & & & \\
3 & (2,5) & (3,6) & & & & & & \\
2 & (2,4) & (3,5) & (4,6) & & & & & \\
1 & (2,3) & (3,4) & (4,5) & (5,6) & & & & \\
0 & (2,2) & (3,3) & (4,4) & (5,5) & (6,6) & & & \\
1 & (2,1) & (3,2) & (4,3) & (5,4) & (6,5) & (7,6) & & \\
2 & & (3,1) & (4,2) & (5,3) & (6,4) & (7,5) & (8,6) & \\
3 & & & (4,1) & (5,2) & (6,3) & (7,4) & (8,5) & (9,6) \\
\end{tabular}

\(\includegraphics{}\text{\textbf{Figure 4} Possible regret-equal degree tuples for men and women when}d(M_0)=(2,6)\text{and}n\ge 9\text{.}n\ge 9\)

