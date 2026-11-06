_Proof._ We first invoke the standard subroutine in _O(n_log_m_) time, obtaining a collection \(\Gamma\) of bicliques. All distances recorded by \(\Gamma\) are then reported explicitly, requiring constant time per output distance.

For each recursive subproblem _T(q,q_) in Recurrence (11), it is associated with a subset \(A'\subseteq A\) and \(B'\subseteq B\) with \(|A'|\le q\) and \(|B'|\le q\). By Corollary 2, all distances between \(A'\) and \(B'\) lying in _I_ can be enumerated in _O(q_<sup>4/3</sup>) time, in addition to constant time per output distance. Since there are _O(r_<sup>2</sup>) subproblems, the total time spent on all subproblems is _O(r_<sup>2</sup>_q_<sup>4/3</sup>)=_O(m_<sup>2/3</sup>_n_<sup>2/3</sup>), again in addition to constant time per output distance.

Combining the contributions of \(\Gamma\) and all recursive subproblems proves the lemma.

Applying the above lemma and using the bound \(|S\cap I|=O(m^{2/3}n^{2/3})\), all distances in \(S\cap I\) can be enumerated in _O(n_log_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>) time. A final linear-time selection then computes \(\delta^*\) within the same asymptotic bound.

### 6.2.4 Wrapping things up

We have shown that, for the case _n\<m_<sup>2</sup>, the first main procedure requires _O(n_log<sup>2</sup>_m_) time, the second main procedure requires _O(n_log<sup>2</sup>_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>) time, and the distance-reporting procedure requires _O(n_log_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>) time. Therefore, the overall running time is _O(n_log<sup>2</sup>_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>). This establishes Theorem 6 for the case \(m\le n<m^2\).

Combining this with the case \(n\ge m^2\), we conclude that if \(m\le n\), then the distance selection problem can be solved in _O(n_log<sup>2</sup>_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>) time.

If _m\>n_, the roles of _A_ and _B_ can be exchanged, yielding a running time of _O(m_log<sup>2</sup>_n+m_<sup>2/3</sup>_n_<sup>2/3</sup>).

Combining the two bounds proves Theorem 6.

## References

