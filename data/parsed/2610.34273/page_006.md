<tbc>Theorem 1.1 settles one explicit question from \[CVZ19\] and resolves a family of cases of another. First, Question 1.3.1 asks whether \(\tau(K_n)<2/3\) for some \(n\ge 5\). Our bound proves this for every \(n\ge 5\); the formal statement and proof appear in Corollary 4.13. Second, Question 1.3.2 asks whether the maximum-cut lower bound is always tight. We prove that it is tight for every even complete graph: for every positive integer _s_,

\(\mathrm{log}_2\widetilde{\text{R}}\big(\mathsf{GT}_2(K_{2s})\big)=s^2=\mathrm{MaxCut}(K_{2s}).\)

Corollary 4.12 records this consequence. The question for general graphs remains open, as does equality with the maximum cut for odd complete graphs.

**Relation to recent polynomial methods.** Several works have developed the polynomial approach after the OpenAI release. Uzna ́nski \[Uzn26\] derived rectangular matrix multiplication bounds, including exponent 2 for multiplying an \(N\times\lceil N^k\rceil\) matrix by a \(\lceil N^k\rceil\times N\) matrix whenever \(0\le k\le 1/2\). Lü \[Lü26\] improved the finite shared-leg separation construction and extended the argument to arbitrary characteristic. Pass \[Pas26\] gave a constructive elementary proof of \(\omega\le 9/4\) by polynomial packings and block recursion. Amanov, van den Berg, and Zuiddam \[ABZ26\] gave an exposition over every field, treated rectangular shapes, and proved an operational barrier for the degeneration ingredients and combination rules used in the three-leg argument. Separately, Zadeh \[Zad26\] reported a further optimization within the Coppersmith- Winograd framework; its exponent does not improve on 9/4. Solomonik and Bl ́ser \[SB26\] study explicit rank and border-rank constructions for several independent matrix products, together with their finite-precision behavior. Their focus is on finite-size aggregation, whereas our result bounds the asymptotic rank of a tensor with one separate leg for every graph vertex.

## 1.3 The polynomial method in higher order

The proof uses the additional input directions while keeping their tensor legs separate. Its central construction separates _n_-2 shared legs at once; the resulting inequalities then control a polynomial tensor with _n_-1 independent inputs. The spectral framework remains Strassen’s. Work of Christandl, Vrana, and Zuiddam \[CVZ23\] and Alman, Li, and Pratt \[ALP26\] places it<tbc>

\begin{tabular}{ccccc}
Graph & CVZ \[CVZ19\] & Brand et al. \[BCK<sup>+</sup>26\] & Triangle cover & Our result \\
\multicolumn{5}{c}{_Upper bounds on_ \(\mathrm{log}_2\widetilde{\text{R}}(\mathsf{GT}_2(K_n))\)} \\
_K_<sub>4</sub> & 4.637658 & 4.633908 & 9/2 & 4 \\
_K_<sub>5</sub> & 7.729429 & 7.723180 & 15/2 & 25/4 \\
_K_<sub>6</sub> & 11.594144 & 11.584770 & 45/4 & 9 \\
_K_<sub>7</sub> & 16.231801 & 16.218678 & 63/4 & 49/4 \\
_K_<sub>8</sub> & 21.642401 & 21.624904 & 21 & 16 \\
\multicolumn{5}{c}{_Upper bounds on the exponent per edge_ \(\tau(K_n)\)} \\
_K_<sub>4</sub> & 0.772943 & 0.772318 & 3/4 & 2/3 \\
_K_<sub>5</sub> & 0.772943 & 0.772318 & 3/4 & 5/8 \\
_K_<sub>6</sub> & 0.772943 & 0.772318 & 3/4 & 3/5 \\
_K_<sub>7</sub> & 0.772943 & 0.772318 & 3/4 & 7/12 \\
_K_<sub>8</sub> & 0.772943 & 0.772318 & 3/4 & 4/7 \\
\end{tabular}

2: Comparison of the cited uniform complete-graph bounds. The CVZ column uses \(\genfrac(){pt}{2}{n}{2}\mathrm{log}_7(9/2)\); displayed decimals are rounded upward. The Brand et al. column uses \(0.772318\genfrac(){pt}{2}{n}{2}\). The triangle-cover column uses \(\omega\le 9/4\) from \[Ope26a\]. The last column is Theorem 1.1; its logarithmic bound is exact for even _n_.

