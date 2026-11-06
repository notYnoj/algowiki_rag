_Proof._ Assume that for every vertex \(v\in V\) , there exists a path from _s_ to _v_ and from _v_ to _t_, since otherwise no _s-t_ walk can pass through _v_, and we may ignore such vertices. For each \(v\in V\) , fix an arbitrary _v-t_ walk _t<sub>v</sub>_. Let \(s_v^{(k)}\) denote the shortest _s-v_ walk with at most _k_ edges, where \(s_v^{(0)}=\emptyset\).

Define the recurrence:

\(s_v^{(k+1)}=min_{u\in V}\left(s_u^{(k)}\circ(u,v)\right),\) (34)

where ties are broken arbitrarily. We can compute this because for any two walks \(s_{u_1}^{(k)}\circ(u_1,v)\) and \(s_{u_2}^{(k)}\circ(u_2,v)\), we can compare them by extending each with _t<sub>v</sub>_ and comparing total weights.

If _w_ has no negative cycles, then \(s_t^{(n-1)}\) is the shortest _s-t_ path. To detect a negative cycle, check whether \(w(s_u^{(n)})<w(s_u^{(n-1)})\) for any \(u\in V\) .

Since there are _O(n_<sup>2</sup>) entries \(s_u^{(k)}\), and each is computed by comparing _O(n_) candidate walks, the total number of comparisons is _O(n_<sup>3</sup>). Although each comparison naively takes _O(n_) time, we can amortize this using shared subwalks, leading to _O(n_) time per table entry and total runtime _O(n_<sup>3</sup>).

## References

