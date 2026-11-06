(Almost) Ruling Out SETH Lower Bounds for All-Pairs Max-Flow

Ohad Trabelsi<sup>∗</sup> <sup>1</sup>

<sup>1</sup>Toyota Technological Institute at Chicago. Email: `ohadt@ttic.edu`

November 12, 2024

**Abstract**

The All-Pairs Max-Flow problem has gained significant popularity in the last two decades, and many results are known regarding its fine-grained complexity. Despite this, wide gaps remain in our understanding of the time complexity for several basic variants of the problem, including for directed or undirected input graphs that are edge- or node-capacitated, and where the capacities are unit or arbitrary. In this paper, we aim to bridge these gaps by providing algorithms, conditional lower bounds, and non-reducibility results. Notably, we show that for most problem settings, deterministic reductions based on the Strong Exponential Time Hypothesis (SETH) cannot rule out \(O(n^{4-\varepsilon})\) time algorithms for some small constant \(\varepsilon>0\), under a hypothesis called NSETH.

To obtain our results for undirected graphs with unit node-capacities (aka All-Pairs Vertex Connectivity), we design a new _randomized Las Vegas_ \(O\big(m^{2+o(1)}\big)\) time combinatorial algorithm. This is our main technical result, improving over the recent \(O\big(m^{11/5+o(1)}\big)\) time _Monte Carlo_ algorithm [Huang et al., S 2023] and matching their _m_<sup>2-_o_(1)</sup> lower bound (up to subpolynomial factors), thus essentially settling the time complexity for this setting of the problem.

<sup>∗</sup>Partially supported by the NWO VICI grant 639.023.812.

