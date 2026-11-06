Again, the algorithm and the proof of the above lemma remain the same as in \[Gup25\]. The only change is that we run the algorithm of \[Gup25\] for fewer iterations. After we have run the above two algorithms, we run our algorithm ENSUREBALLPROXIMITY, which is also present in \[Gup25\] in a similar form.

The algorithm ENSUREBALLPROXIMITY has three parts. The first two parts call UPDATEFROM(_w_) for every \(w\in A_\alpha\). This two-pass approach is intentional: the first pass discovers and updates intermediate distance estimates, while the second pass leverages these newly updated estimates to find even shorter paths. The last part calls TRIANGULATE(_s_) for every \(s\in V\), and estimates the distance from _s_ to t using \(\text{pivot}_\alpha(s)\).

