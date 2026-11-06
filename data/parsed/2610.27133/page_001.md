Counterexamples to a conjecture and improved bounds for bipanchromatic colorings

We study the bipanchromatic number \(\chi_B\), introduced by Lalou et al. [1] as the maximum number of colors in a panchromatic hypergraph coloring where every color appears at least twice. They show that merging uniquely occurring colors in a maximum panchromatic coloring gives the lower bound \(\beta=\chi_P-\lceil\alpha/2\rceil\le\chi_B\), where \(\chi_P\) is the panchromatic number and \(\alpha\) is the minimum number of such colors among maximum panchromatic colorings. They conjectured that \(\chi_B=\beta\) and subsequently disproved it [5]. We identify the smallest counterexample, with six vertices and three hyperedges, both minimum possible. We show that the ratio bound \(\chi_B/\beta<2\) is asymptotically sharp and prove minimality results for the order and hyperedge count. For \(3\le\alpha<\chi_P\) we show that every integer from \(\beta\) to \(\chi_P-1\) occurs as \(\chi_B\) while \(\chi_P\) and \(\alpha\) are held fixed. Furthermore, we discover that the values \(|V|,\chi_P,\alpha\) directly decide whether the conjectured equality holds except when \(\alpha=4\), where a matching reduction resolves the ambiguity. We derive the optimal universal lower bound _L_ depending only on \(|V|,\chi_P,\alpha\) in the nontrivial regime \(0<2\alpha<|V|\). Finally, we prove \(\chi_B/L\le 5/4\) and \(\chi_B/L\le 6/5+1/(5L)\), with 5/4 sharp and 6/5 asymptotically sharp as \(L\rightarrow\infty\).

## 1 Introduction

A _panchromatic_ coloring [1, 2, 3, 4] uses every color in every hyperedge, with maximum \(\chi_P\) colors. Lalou et al. [1] introduced bipanchromatic colorings to study completely independent spanning trees in split graphs. These colorings use each color at least twice overall, with maximum \(\chi_B\). Let \(\alpha\) be the minimum number of colors occurring once in a \(\chi_P\)-coloring. Their conjecture [1, Conjecture 1] predicts \(\chi_B=\chi_P-\lceil\alpha/2\rceil\) by merging those colors.

The same authors subsequently disproved this conjecture [5]. They construct counterexamples as three-hyperedge sunflowers with a common set of 6_d_ vertices and three disjoint petals of size _q_, where \(d\ge 1\) and \(q\ge 2d\). Their parameters are \(\chi_P=6d+q\), \(\alpha=6d\), and \(\chi_B=4d+q\). Thus the conjectured value is exceeded by exactly _d_, on \(6d+3q\ge 12d\) vertices.

Our three-hyperedge construction uses 12_d_-6 vertices for the same excess (Proposition 2). Without restricting the number of hyperedges, we prove that the minimum order is 4_d_+2 and classify all examples attaining it (Theorem 6). Their family has actual-to-conjectured ratio at most \(\frac{6}{5}\). We determine the sharp worst-case ratio over all hypergraphs, proving that it is strictly below two and can approach two (Theorem 5). We develop the coloring bounds and equality criteria suggested in their concluding remarks [5, Section 5].

Sections 2-3 introduce the colorings and counterexamples. Section 4 establishes sharp bounds and characterizes minimum-size counterexamples. Section 5 determines, with minimum order, all possible \(\chi_B\) values with fixed \(\chi_P\) and \(\alpha\), showing that no formula depending only on \(\chi_P\) and \(\alpha\) can determine \(\chi_B\) for every hypergraph. Section 6 shows that the hypergraph order, \(\chi_P\) and \(\alpha\) determine if the conjectured equality holds, except when \(\alpha=4\) which is resolved by maximum matching. In Section 7, the optimal lower bound _L_ for \(\chi_B\) is determined from |_V_|, \(\chi_P\) and \(\alpha\), with \(\chi_B/L\le 5/4\) and \(\chi_B/L\le 6/5+1/(5L)\), where 5/4 is sharp and 6/5 is asymptotically sharp as \(L\rightarrow\infty\).

Stefan Novaković Faculty of Electrical Engineering University of Banja Luka stefan.novakovic@etf.unibl.org

Duško Jojić Faculty of Natural Sciences and Mathematics University of Banja Luka dusko.jojic@pmf.unibl.org

arXiv:2610.27133v1 [math.CO] 19 Oct 2026

