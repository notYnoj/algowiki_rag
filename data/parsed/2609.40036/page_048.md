<tbc>constraints gives _O(mq_<sup>2</sup>) variables and constraints in total. Each flow variable occurs in only two node equations and one marginal equation, so the number of nonzero scalar coefficients is also _O(mq_<sup>2</sup>). The field entries _h<sub>ve</sub>_ determine which nodes a directed edge connects; the real-valued LP constraints themselves have coefficients \(0,\pm 1\), as does the nonconstant part of the objective. Rational LP optimization thus takes time polynomial in _n_, _q_, and _D_. A fixed lexicographic rule on the symbol marginals can be implemented by a polynomial number of further LP optimizations, making the decoder deterministic in either formulation. This removes the exponential degree dependence in the implementation; it does not change the parameter regimes of the recovery results.

## References

\[Big93\] N.L. Biggs. _Algebraic graph theory_. Algebraic Graph Theory. Cambridge University Press, 1993. url: `https://books.google.com/books?id=WO6inQEACAAJ`.

\[Bol01\] B. Bollobás. _Random Graphs_. Cambridge Studies in Advanced Mathematics. Cambridge University Press, 2001. isbn: 9780521797221. url: `https://books.google. com/books?id=o9WecWgilzYC`.

\[CLZ22\] Yilei Chen, Qipeng Liu, and Mark Zhandry. "Quantum algorithms for variants of average-case lattice problems via filtering". In: _Annual international conference on the theory and applications of cryptographic techniques_. Springer. 2022, pp. 372–401.

\[Com08\] Giacomo Como. "Ensembles of codes over Abelian groups". PhD thesis. Politecnico di Torino, Mar. 2008. url: `https://archive.control.lth.se/media/Staff/ GiacomoComo/ComoThesis.pdf`.

\begin{tabular}{cc}
Assignment (_b_<sub>1</sub>_,b_<sub>2</sub>_,b_<sub>3</sub>) & Running sums (_z_<sub>0</sub>_,z_<sub>1</sub>_,z_<sub>2</sub>_,z_<sub>3</sub>) \\
(0,0,0) & (0,0,0,0) \\
(0,1,1) & (0,0,1,0) \\
(1,0,1) & (0,1,1,0) \\
(1,1,0) & (0,1,0,0) \\
\end{tabular}

Layer 0 start
Layer 1
Layer 2
Layer 3 required end
0
0
(1,0)
(2,0)
0
(3,0)
1
1
1
1
1
1
1
(0,1)
(1,1)
(2,1)
(3,1)
0
0
0
unused initial state
wrong final sum

**Figure 2:** Full trellis for _b_<sub>1</sub>+_b_<sub>2</sub>+_b_<sub>3</sub>=0 over F<sub>2</sub>. An edge label gives the chosen symbol value, and (_i,z_) records the running sum after _i_ choices. The table lists all four paths from the required start to the required end. Dashed nodes and edges are included in the full construction but lie on no such path; they carry zero flow in the LP. Crossings of edges are not nodes.

