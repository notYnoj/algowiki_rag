## 12 Asteroidal Triples and Friends in (Likely Necessary) Matrix Multiplication Time

(**i)** For each \(i\in[1..B]\), we construct two Boolean \(|\mathcal{S}|\times n\) matrices \(M_i^b\) for \(b\in\{0,1\}\), indexed by sets in S (rows) and by nodes in _V_ (columns), defined as follows:

\(M_i^b[S,u]:=\left\{\begin{array}{ c c } 1 & \text{if}f_S(u)\neq\perp\text{and the}i\text{-th bit of}f_S(u)\text{is}b\text{,} \\ 0 & \text{otherwise.}
\end{array}\right.\)

(**ii)** For each \(i\in[1..B]\), we use Theorem 3.1 to compute the two BMM products \(M_i^0A\) and \(M_i^1A\) in time O(MM(|S|_,n,n_)), where _A_ denotes the adjacency matrix of **G**. We also compute witnesses for all non-zero entries in these products.

(**iii)** To find a suitable _u_ for each _S_ and _w_ such that \(f_S(w)\neq\perp\), we iterate as follows: for each \(i\in[1..B]\), let _b<sub>i</sub>_ be the _i_-th bit in the binary representation of _f<sub>S</sub>(w_). If for any \(i\in[1..B]\) we have \((M_i^{1-b_i}A)[S,w]=1\), we report the corresponding witness node of the product \((M_i^{1-b_i}A)[S,w]\) as the node _u_ for _S,w_.

Regarding correctness, fix _S_ and _w_ such that \(f_S(w)\neq\perp\), and let _b<sub>i</sub>_ be defined as above. Note that for each \(i\in[1..B]\), we have \((M_i^{1-b_i}A)[S,w]=1\) if and only if there exists a node _u_ such that \(\{u,w\}\in E\), \(f_S(u)\neq\perp\), and the _i_-th bit of _f<sub>S</sub>(u_) differs from the _i_-th bit of _f<sub>S</sub>(w_). From this, the correctness is immediate: we only report a node _u_ if \(f_S(u)\neq f_S(w)\). Conversely, if such a _u_ exists, then _f<sub>S</sub>(u_) and _f<sub>S</sub>(w_) must differ in at least one bit, ensuring that we find such _u_.

Regarding the runtime, we use O(log_n_) many times Theorem 3.1; all other operations can be implemented altogether in time O(|S|_n_log_n_). \(\sqcap\sqcup\)

Our algorithm. With the subroutine setup in place, we now give the full algorithm.

(**i)** For each \(S\in\mathcal{S}\), initialize a union-find (disjoint-set) data structure<sup>10</sup> _D<sub>S</sub>_ over _V_ (equivalently, over the universe **[1_..n_]**). The invariant we maintain is that every set in _D<sub>S</sub>_ is contained in a connected component of **G**[_S_] (or is a singleton corresponding to a node not in **G**[_S_]).

(**ii)** We run for \(\Theta(logn)\) rounds. In the _i_-th round, for each \(S\in\mathcal{S}\) and \(w\in V\) , we define

\(f_S(w)=\left\{\begin{array}{ c c } \text{Find}_{D_S}(w), & w\in\mathbf{G}[S], \\ \perp, & w\notin\mathbf{G}[S].
\end{array}\right.\)

We then invoke the subroutine from Claim 4.1 to find, for each _S_ and _w_, a witness _u_ as specified there (or determine that no such _u_ exists). Whenever we obtain such a witness, we perform \(\text{Union}_{D_S}(u,w)\). The invariant is preserved because Claim 4.1 guarantees that \((u,w)\in E\) and that both \(u,w\in\mathbf{G}[S]\). After processing all such unions, we proceed to the next round.

(**iii)** For each \(S\in\mathcal{S}\), output all sets in _D<sub>S</sub>_ except singleton sets corresponding to nodes \(w\notin\mathbf{G}[S]\); these are the connected components of **G**[_S_].

**Correctness.** It remains to show that after \(\Theta(logn)\) rounds we have that the sets we maintain are equal to the connected components. For each \(S\in\mathcal{S}\), let _m<sub>S</sub>_ denote the number of sets in _D<sub>S</sub>_ that are strict subsets of connected components of **G**[_S_]. In each round, _m<sub>S</sub>_ decreases by at least a factor of 2: every set counted by _m<sub>S</sub>_ has at least one outgoing edge to another set in the same connected component, and the corresponding merge ensures that in the next round it is combined with another set. Hence after \(\Theta(logn)\) rounds, _m<sub>S</sub>=_0 for every _S_, so each set in _D<sub>S</sub>_ exactly matches a connected component of **G**[_S_].

**Runtime.** In each of the \(\Theta(logn)\) rounds we use Claim 4.1 and perform at most O(|S|_n_) union operations. This gives an overall runtime of \(\tilde{\mathcal{O}}(\text{MM}(|\mathcal{S}|,n,n))\).

<sup>10</sup> A union-find (disjoint-set) data structure _D_ maintains a partition of a universe into disjoint sets, supporting Find_<sub>D</sub>(x_) (returns the representative of _x_’s set) and Union_<sub>D</sub>(x,y_) (merges the two sets), with near-constant amortized time \(\mathcal{O}(\alpha(n))\) using union-by-rank and path compression \[Tar75\]. Here \(\alpha(n)\) denotes the inverse-Ackermann function.

