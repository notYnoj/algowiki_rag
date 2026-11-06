**Reminder of Theorem 8.** There is a Las Vegas algorithm that, given a graph with _n_ vertices and \(n^{3/2+\delta}\) edges for \(\delta\in(0,\frac{1}{2})\), returns a 4-cycle and runs in expected \(O(n^{5/4-\delta/2})\) time.

**Proof of Theorem 8.** For simplicity, let the vertex set _V_=[_n_]. We assume access to two orales with information about the graph. The first takes queries of the form \((v,i)\in[n]\times[n]\), and outputs either the _i_-th neighbor of \(v\in V\), or \(\perp\) if _i\>_deg(_v_). The second is a degree oracle that takes \(v\in V\) as input and outputs deg(_v_). We repeat the following procedure until we find a 4-cycle:

1. Sample a vertex \(v\leftarrow V\) uniformly at random.

2. Make at most _n_-1 queries to the neighbor oracle to construct a list of all of _v_’s neighbors. Query the degree oracle for each neighbor.

3. If _v_ has at least \(\sqrt{n}+1\) neighbors, each of which also has degree at least \(\sqrt{n}+1\), then by the pigeonhole principle, _v_ participates in a 4-cycle with two of these neighbors (the total number of distinct 2-paths to _v_ is at least \((\sqrt{n}+1)\cdot\sqrt{n}>n\), so some node has two distinct 2-paths to _v_). Enumerate the first \(\sqrt{n}+1\) neighbors of each of the neighbors of _v_ by querying the neighbor oracle, and output the 4-cycle once it is found.

4. If this condition does not hold, repeat.

We claim that if we sample a vertex _v_ in the \((\sqrt{n}+1)\)-core of _G_, we will satisfy the condition in step 3. This is because by definition, _v_ is in a subgraph such that all vertices have at least \(\sqrt{n}+1\) neighbors. Since the size of the \((\sqrt{n}+1)\)-core is at least \(\Omega(n^{3/4+\delta/2})\), we expect to sample a vertex in the core in \(O(n^{1/4-\delta/2})\) iterations. Each iteration takes _O(n_) time, so our overall expected runtime is \(O(n^{5/4-\delta/2})\).

## 7 Conclusion

In this paper, we have shown how a variety of ideas can be applied to achieve faster algorithms for some tricky triangle problems at the heart of fine-grained complexity. We conclude with some of the most significant questions left open by our work.

We have shaved log(_n_) and word factors from the running times of sparse graph problems, assuming a bound on the maximum degree. Can we still improve the running times of these algorithms in the more general case of sparse graphs without a degree bound? For example, is there an algorithm for All-Edges Sparse Triangle running in _o(m_<sup>4/3</sup>) time on _m_-edge graphs, assuming optimal matrix multiplication? Our approach requires at least two of the nodes in the triangle to have low degree, which is not enough to apply low-degree/high-degree tricks such as those in [6].

Are there _deterministic_ algorithms for these triangle problems that have similar running times? All of our algorithms rely on the use of randomness. Note that since all of our algorithms use _O_(log_n_)-wise independent hash functions and linear hashing for small _k_, we only require at most poly(log_n_) bits of randomness.

The All-Edges Sparse Triangle problem cannot be solved much faster than the obvious running time, under the 3SUM and APSP hardness hypotheses. Is there a fine- grained reduction from All-Edges Sparse Triangle to Sparse Triangle Detection, so that detecting a triangle faster on sparse (or low-degree) graphs would yield a faster algorithm for the all-edges case? Such a reduction is well-known in the dense case [37].

Can 4-cycle detection be solved in _O(n_<sup>2</sup>log_n)/w_ time on the Word RAM for \(w\gg\Omega(logn)\)? Is there any reason to believe that such an algorithm may not exist?

