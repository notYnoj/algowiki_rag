<tbc>\(w_\ell\) is nonzero for some \(1\le\ell\le m\). On choosing _w(a<sub>j</sub>_)=_w<sub>j</sub>_ for \(1\le j\le m\), we have<tbc>

\(\sum_{j=1}^mw(a_j)a_j^i=0\)

<tbc>for all \(0\le i\le m-2\), and

\(\sum_{j=1}^mw(a_j)a_j^{m-1}=1.\)

According to the definition of _e<sub>A</sub>(w_), we have _e<sub>A</sub>(w_)=_m_-1=|_A_|-1. This completes the proof. □

## 3. Main Results

In this section, we state our main results, including the general lower bound for restricted sumsets (the Alon-Nathanson-Ruzsa theorem) and its direct corollary, the Erdős-Heilbronn theorem. We continue to work over the finite field Z_/p_Z for a fixed prime _p_, with all sumset notation consistent with Section 1.

**Theorem 3.1** (Main Theorem)**.** _Let A and B be nonempty subsets of_ Z_/p_Z _with_ \(|A|\neq|B|\)_. Then the cardinality of the restricted sumset satisfies_

\(|A\dot{+}B|\ge min\{p,|A|+|B|-2\}.\)

This main theorem directly implies the classical Erdős-Heilbronn conjecture, which we state formally as a corollary below.

**Corollary 3.1** (Erdős-Heilbronn Theorem)**.** _Let A be a nonempty subset of_ Z_/p_Z_. Then_<tbc>

\(|A\dot{+}A|\ge min\{p,2|A|-3\}.\)

<tbc>_Proof._ Fix any element \(a_0\in A\), and define \(A'=A\backslash\{a_0\}\). Then \(|A|\neq|A'|\), and it is straightforward to verify that \(A\dot{+}A=A\dot{+}A'\): any sum _a+b_ with \(a,b\in A\) and \(a\neq b\) can be written as a sum of an element from _A_ and an element from \(A'\) with distinct summands, and vice versa. Applying the Main Theorem to the pair \((A,A')\), we get

\(|A\dot{+}A|=|A\dot{+}A'|\ge min\{p,|A|+|A'|-2\}\)<br>
\(=min\{p,|A|+(|A|-1)-2\}\)<br>
\(=min\{p,2|A|-3\},\)

which completes the proof. □

