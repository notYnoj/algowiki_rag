# Negative-Weight Single-Source Shortest Paths in Near-linear Time

**Abstract**

We present a randomized algorithm that computes single-source shortest paths (SSSP) in _O(m_log<sup>8</sup>(_n_)log_W_) time when edge weights are integral and can be negative.<sup>1</sup> This essentially resolves the classic negative-weight SSSP problem. The previous bounds are \(\tilde{O}((m+n^{1.5})logW)\) [BLNPSSSW FOCS’20] and _m_<sup>4/3+_o_(1)</sup>log_W_ [AMV FOCS’20]. Near-linear time algorithms were known previously only for the special case of planar directed graphs [Fakcharoenphol and Rao FOCS’01].

In contrast to all recent developments that rely on sophisticated continuous optimization methods and dynamic algorithms, our algorithm is simple: it requires only a simple graph decomposition and elementary combinatorial tools. In fact, ours is the first combinatorial algorithm for negative-weight SSSP to break through the classic \(\tilde{O}(m\sqrt{n}logW)\) bound from over three decades ago [Gabow and Tarjan SICOMP’89].

<sup>∗</sup>Rutgers University <sup>†</sup>Max Planck Institute for Informatics and KTH. Work done while at BARC, University of Copenhagen. <sup>‡</sup>Work done while at BARC, University of Copenhagen. <sup>1</sup>Throughout, _n_ and _m_ denote the number of vertices and edges, respectively, and \(W\ge 2\) is such that every edge weight is at least -_W_. \(\tilde{O}\) hides polylogarithmic factors.

Aaron Bernstein<sup>∗</sup> Danupon Nanongkai<sup>†</sup> Christian Wulff-Nilsen<sup>‡</sup>

