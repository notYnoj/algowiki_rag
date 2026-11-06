\(S'\leftarrow\) A permutation of _S_ chosen u.a.r. from the set of all possible permutations;<br>
// The above step is only needed if the order of the elements in _S_ can depend on the errors (otherwise, it suffices to use \(S'=S\)).<br>
\(T_0,T_1,\dots,T_k\leftarrow\) a random partition of the elements in \(S'\) such that \(|T_0|=\lceil\sqrt{n}\rceil\),<br>
\(|T_i|=2^{i-1}\cdot\lceil\sqrt{n}\rceil\) for i=1,...,k-1, and \(1\le|T_k|\le 2^k\cdot\lceil\sqrt{n}\rceil\);<br>
\(\widetilde{S}_0\leftarrow\) Subsequence of \(S'\) containing the elements in T<sub>0</sub>;<br>
\(S_0\leftarrow\) BasketSort(\(\widetilde{S}_0\), \(|\widetilde{S}_0|\));<br>
for i=1,...,k do<br>
   foreach \(x\in T_i\) do<br>
   \(r_x\leftarrow\text{NoisySearch}(S_{i-1}\), x, \(\beta_\mathrm{max}\cdot\mathrm{ln}n)\);<br>
   \(\widetilde{S}_i\leftarrow\) Simultaneously insert each element \(x\in T_i\) into position r<sub>x</sub> of S<sub>i-1</sub> (break ties according to \(S'\));<br>
   \(S_i\leftarrow\) BasketSort(\(\widetilde{S}_i\), \(\gamma\cdot\beta_\mathrm{max}\cdot\mathrm{ln}n\));<br>
return S<sub>k</sub>;

<tbc>_S_<sub>_i_-1</sub> to compute an approximate rank r<sub>x</sub> for each element x in T<sub>i</sub>. These elements are simultaneously inserted into S<sub>i-1</sub> according to their approximate ranks, thus obtaining a sequence \(\widetilde{S}_i\). If ties arise (i.e., if multiple elements share the same approximate rank), they are broken according to the order of the tied elements in \(S'\). This ensures that the order of the elements in \(\widetilde{S}_i\) does not (indirectly) depend on the comparisons errors involving elements in T<sub>i+1</sub>,...,T<sub>k</sub>. Finally, BasketSort is used to re-sort \(\widetilde{S}_i\) into a new sequence S<sub>i</sub> with a smaller maximum dislocation, before moving to the next iteration. Once all iterations are complete, the algorithm returns S<sub>k</sub>.

From a high-level perspective, we have that, in each iteration, the maximum dislocation of S<sub>i-1</sub> is at most \(\beta_\mathrm{max}\cdot\mathrm{ln}n\), while inserting the elements of T<sub>i</sub> into S<sub>i-1</sub> according to the approximate ranks computed by NoisySearch increases the maximum dislocation to at most \(\gamma\cdot\beta_\mathrm{max}\cdot\mathrm{ln}n\). Finally, BasketSort decreases the maximum dislocation back to at most \(\beta_\mathrm{max}\cdot\mathrm{ln}n\), where the quantities \(\beta_\mathrm{max}\) and \(\gamma\) are constants that depend only on p and q. In particular, \(\gamma\) stems from NoisySearch and our analysis of the simultaneous insertion step of RiffleSort (see Lemma 3.3).

## 3.2 Algorithm analysis

We start by analyzing the running time of RiffleSort.

Lemma 3.1. _The worst-case running time of Algorithm 1 is O(n_log_n)._

Proof. Clearly, it takes _O(n_log_n_) time to compute \(S'\) and the random partition T<sub>0</sub>, ..., T<sub>k</sub>_.<sup>3</sup> Moreover, by Theorem 5.20, the first call to BasketSort requires \(O(|T_0|^2)=O(\lceil\sqrt{n}\rceil^2)=O(n)\) time.<tbc>

<sup>3</sup>The exact complexities of these steps depend on whether we are allowed to sample uniformly random integers in a range in _O_(1) time. Even if this is not the case, we can still independently sample _n_-1 integers, where the _i_-th such integer is sampled u.a.r. from {0,...,_n-i_}, in _O(n_log_n_) time with probability at least 1-_n_<sup>-2</sup> using a simple rejection strategy (see the proof of Lemma A.2 for details). This allows us to compute \(S'\) using, e.g., the Fisher-Yates shuffle (see, e.g., \[24\]) on _S_. Moreover, the partition T<sub>0</sub>,...,T<sub>k</sub> can be found using _O(n_) random bits with probability at least 1-_n_<sup>-2</sup> (see Section 7.1 and Appendix A). To maintain a worst-case upper bound on the running time, we can handle the unlikely event in which _O(n_log_n_) bits do not suffice by simply stopping the algorithm and returning any arbitrary permutation of _S_. This will not affect the high-probability bounds in presented in the sequel.

**Algorithm 1:** RiffleSort(_S_)

