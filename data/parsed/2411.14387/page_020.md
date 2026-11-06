So every side switch between consecutive points of the external funnel gives at least one side switch in the combined funnel, and so does every side switch between consecutive points of the internal funnel, and there is no double counting.

So the number of times the funnel points switch sides is at least the number of times the funnel points switch sides in \(\widetilde{X}\) and _X_<sup>(_j<sub>x</sub>_)</sup> combined. Thus

\(\mathsf{Funnel}(X)\ge\mathsf{Funnel}\big(\widetilde{X}\big)+\sum_j\mathsf{Funnel}\big(X^{(j)}\big),\)

and we don’t even suffer an _O(m_) loss.<sup>12</sup>

## References

**1** Brian Allen and Ian Munro. Self-organizing binary search trees. _J. ACM_, 25(4):526-535, oct 1978. URL: `http://doi.acm.org/10.1145/322092.322094`, `doi:10.1145/322092.322094`.

**2** Boaz Barak, Mark Braverman, Xi Chen, and Anup Rao. Direct sums in randomized communication complexity. _Electron. Colloquium Comput. Complex._, TR09-044, 2009. URL: `https://eccc.weizmann.ac.il/report/2009/044`, `arXiv:TR09-044`.

**3** Benjamin Aram Berendsohn, László Kozma, and Michal Opler. Optimization with pattern- avoiding input. _CoRR_, abs/2310.04236, 2023. `doi:10.48550/arXiv.2310.04236`.

**4** Guy E. Blelloch and Magdalen Dobson. The geometry of tree-based sorting. In _ICALP_, volume 261 of _LIPIcs_, pages 26:1-26:19. Schloss Dagstuhl - Leibniz-Zentrum für Informatik, 2023. `doi:10.4230/LIPIcs.ICALP.2023.26`.

**5** Prosenjit Bose, Karim Douüeb, Vida Dujmovic, and Rolf Fagerberg. An _O_(log log _n_)- competitive binary search tree with optimal worst-case access times. In _Algorithm Theory - SWAT 2010, 12th Scandinavian Symposium and Workshops on Algorithm Theory, Bergen, Norway, June 21-23, 2010. Proceedings_, pages 38-49, 2010. `doi:10.1007/978-3-642-13731-0\ \_5`.

**6** Parinya Chalermsook, Julia Chuzhoy, and Thatchaphol Saranurak. Pinning down the strong wilber 1 bound for binary search trees. In _APPROX-RANDOM_, volume 176 of _LIPIcs_, pages 33:1-33:21. Schloss Dagstuhl - Leibniz-Zentrum für Informatik, 2020. `doi:10.4230/LIPIcs. APPROX/RANDOM.2020.33`.

**7** Parinya Chalermsook, Mayank Goswami, László Kozma, Kurt Mehlhorn, and Thatchaphol Saranurak. Greedy is an almost optimal deque. In _WADS_, volume 9214 of _Lecture Notes in Computer Science_, pages 152-165. Springer, 2015. `doi:10.1007/978-3-319-21840-3\_13`.

**8** Parinya Chalermsook, Mayank Goswami, László Kozma, Kurt Mehlhorn, and Thatchaphol Saranurak. Pattern-avoiding access in binary search trees. In Venkatesan Guruswami, editor, _IEEE 56th Annual Symposium on Foundations of Computer Science, FOCS 2015, Berkeley, CA, USA, 17-20 October, 2015_, pages 410-423. IEEE Computer Society, 2015. `doi:10.1109/ FOCS.2015.32`.

**9** Parinya Chalermsook, Mayank Goswami, László Kozma, Kurt Mehlhorn, and Thatchaphol Saranurak. The landscape of bounds for binary search trees. _arXiv preprint arXiv:1603.04892_, 2016.

**10** Parinya Chalermsook, Manoj Gupta, Wanchote Jiamjitrak, Nidia Obscura Acosta, Akash Pareek, and Sorrachai Yingchareonthawornchai. Improved pattern-avoidance bounds for greedy bsts via matrix decomposition. In _SODA_, pages 509-534. SIAM, 2023. `doi:10.1137/ 1.9781611977554.ch22`.

<sup>12</sup>A _O(m_) loss could have arisen depending on the precise definition of the funnel bound, e.g. if as in [27] we had counted the number of _consecutive streaks_ of one side instead of counting the number of times the funnel _flips_ sides.

