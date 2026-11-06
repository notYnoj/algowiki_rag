Each call to Solve in line 4 has running time \((2^\sqrt{\mathrm{log}n})^{O(\mathrm{log}(2^\sqrt{\mathrm{log}n}))}\), which is a polynomial in _n_. The same holds for each call in line 8 because, by Lemma 6.4, \(\xi(T^*)\) has at most \(4\left\lceil\frac{n}{\alpha}\right\rceil=O(2^\sqrt{\mathrm{log}n})\) vertices. Thus, procedure Rec has polynomial running time and it remains to bound the cost of the search strategy R computed by Rec.

To bound the recursion depth of Rec, note that each time a recursive call is made, the size of instance (input tree) decreases \(2^\sqrt{\mathrm{log}n}\) times. Thus, the depth is bounded by \(\mathrm{log}_{(2^\sqrt{\mathrm{log}n})}n=\sqrt{\mathrm{log}n}\). In the search strategy computed by procedure Rec, at each level of the recursion we execute the search strategy computed by one call to Solve and one vertex of the \((n/2^\sqrt{n})\)- separating tree is queried. This follows from the definition of \((\mathcal{A}_{T^*},\{\mathcal{R}_{r(T^\prime)}\big|T'\in\mathcal{C}(T\backslash V^*)\})\)- strategy. By Lemma 6.2,

\(\mathtt{COST}_{\mathcal{A}_{T^*}}(T^*)\le c'\cdot\mathtt{OPT}(T^*)\)

for some constant \(c'\). By Lemma 6.1 and since \(\mathtt{OPT}(T^*)\le\mathtt{OPT}(T)\), the cost of R at each recursion level is bounded by \((c'+1)\mathtt{OPT}(T)\). This gives that \(\mathtt{COST}_\mathcal{R}(T)\le c'\sqrt{\mathrm{log}n}\cdot\mathtt{OPT}(T)\) as required.

Noting that the existence of a constant-approximation procedure with _n_<sup>_O_(log_n_)</sup> running time follows from Theorem 3.3 (by taking \(\varepsilon=1\)), the claim of Theorem 3.4 follows directly from Lemma 6.5.

## Acknowledgment

The authors thank Jakub Łącki for preliminary discussions on the studied problem.

## References

