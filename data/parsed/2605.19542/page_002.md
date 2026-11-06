<tbc>The Erdős-Heilbronn conjecture states that for any nonempty subset _A_ of Z_/p_Z,<tbc>

\(|A\dot{+}A|\ge min\{p,2|A|-3\}.\)

<tbc>This conjecture remained open for 30 years, until it was first proven by Dias da Silva and Hamidoune in 1994, using tools from exterior algebra and representation theory [4]. In 1995, Alon, Nathanson and Ruzsa developed the polynomial method, specifically the Combinatorial Nullstellensatz [2, 1], to give a simpler proof of a more general result: for nonempty subsets _A,B_ of Z_/p_Z with \(|A|\neq|B|\),

\(|A\dot{+}B|\ge min\{p,|A|+|B|-2\}.\)

This general result directly implies the original Erdős-Heilbronn conjecture as a corollary.

In the decades since, multiple new proofs of the Cauchy-Davenport theorem and the Erdős-Heilbronn conjecture have been developed, using tools ranging from harmonic analysis to the uncertainty principle on finite cyclic groups [6]. In 2004, Das introduced a linear algebraic method to give a new proof of the Cauchy-Davenport theorem, relying only on elementary linear algebra over finite fields [3]. In this note, we extend Das’s linear algebraic approach to give a new, elementary proof of the Alon-Nathanson-Ruzsa theorem for restricted sumsets. Compared with existing proofs, our method requires no advanced algebraic or combinatorial machinery, only standard undergraduate-level linear algebra, including Vandermonde matrices and the solvability of linear systems over finite fields.

The rest of this paper is organized as follows. Section 2 collects the preliminary definitions and auxiliary lemmas that form the foundation of our proof. Section 3 states our main results, including the main theorem and its direct corollary, the Erdős-Heilbronn theorem. The complete proof of the main theorem is presented in Section 4. We conclude with some brief remarks and directions for future work in Section 5.

## 2. Preliminaries

In this section, we introduce the core definitions and auxiliary lemmas used throughout the paper. All sets are assumed to be nonempty subsets of Z_/p_Z, where _p_ is a fixed prime number. For a finite set _S_, we write |_S_| for the cardinality (number of elements) of _S_.

Let _A_={_a_<sub>1</sub>_,...,a<sub>m</sub>_} be a subset of Z_/p_Z with _a_<sub>1</sub>_,...,a<sub>m</sub>_ pairwise distinct. Let _w(a_<sub>1</sub>)_,...,w(a<sub>m</sub>_) be a sequence in Z_/p_Z satisfying \(w(a_\ell)\) is nonzero in Z_/p_Z for some \(1\le\ell\le m\). We shall say a sequence

