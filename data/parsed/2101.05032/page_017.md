query the final interval of the form (0,5) to decide the problem. Then the adversary sets the value of that interval to 4, and querying only that interval would be sufficient for determining that 3 is the _i_-th smallest value. Hence any deterministic algorithm makes at least _i_ queries, while opt<sub>1</sub>=1.

## 5.2 Finding all Elements with Value _v_<sup>∗</sup>

Now we focus on the task of finding _v_<sup>∗</sup> as well as identifying all intervals in I whose precise value equals _v_<sup>∗</sup>. For ease of presentation, we assume that all the intervals in I are closed. The result can be generalized to arbitrary intervals without any significant new ideas, but the proofs become longer and require more cases. A complete proof is included in Appendix B.

Let us begin by observing that the optimal query set is easy to characterize.

\(\blacktriangleright\) **Lemma 5.2.** _Every feasible query set contains all non-trivial intervals that contain v_<sup>∗</sup>_. The optimal query set_ OPT<sub>1</sub> _contains all non-trivial intervals that contain v_<sup>∗</sup> _and no other intervals._

**Proof.** If a non-trivial interval _I<sub>j</sub>_ containing _v_<sup>∗</sup> is not queried, one cannot determine whether the precise value of _I<sub>j</sub>_ is equal to _v_<sup>∗</sup> or not. Thus, every feasible query set contains all non-trivial intervals that contain _v_<sup>∗</sup>.

Furthermore, it is easy to see that the non-trivial intervals containing _v_<sup>∗</sup> constitute a feasible query set: Once these intervals are queried, one can determine for each interval whether its precise value is smaller than _v_<sup>∗</sup>, equal to _v_<sup>∗</sup>, or larger than _v_<sup>∗</sup>. \(\blacktriangleleft\)

Let _I_<sub>_j_<sub>1</sub></sub> be the interval with the _i_-th smallest left endpoint, and let _I_<sub>_j_<sub>2</sub></sub> be the interval with the _i_-th smallest right endpoint. Then it is clear that _v_<sup>∗</sup> must lie in the interval \([\ell_{j_1},u_{j_2}]\), which we call the **target area**. The following lemma was essentially shown by Kahan [22]; we include a proof for the sake of completeness.

\(\blacktriangleright\) **Lemma 5.3** (Kahan, 1991)**.** _Assume that the current instance of_ Selection _is not yet solved. Then there is at least one non-trivial interval I<sub>j</sub> in_ I _that contains the target area, i.e., satisfies_ \(\ell_j\le\ell_{j_1}\) _and_ \(u_j\ge u_{j_2}\).

**Proof.** First, assume that the target area is trivial, i.e., \(\ell_{j_1}=u_{j_2}=v^*\). If there is no non-trivial interval in I that contains _v_<sup>∗</sup>, then the instance is already solved, a contradiction.

Now, assume that the target area is non-trivial. Assume that no interval in I contains the target area. Then all intervals _I<sub>j</sub>_ with \(\ell_j\le\ell_{j_1}\) have _u<sub>j</sub>\<u_<sub>_j_<sub>2</sub></sub>. There are at least _i_ such intervals (because \(\ell_{j_1}\) is the _i_-th smallest left endpoint), and hence the _i_-th smallest right endpoint must be strictly smaller than _u_<sub>_j_<sub>2</sub></sub>, a contradiction to the definition of _u_<sub>_j_<sub>2</sub></sub>. \(\blacktriangleleft\)

For _k_=1, there is therefore an online algorithm that makes opt<sub>1</sub> queries: In each round, it determines the target area of the current instance and queries a non-trivial interval that contains the target area. (This algorithm was essentially proposed by Kahan [22] for determining all elements with value equal to _v_<sup>∗</sup>, without necessarily determining _v_<sup>∗</sup>.) For larger _k_, the difficulty is how to select additional intervals to query if there are fewer than _k_ intervals that contain the target area.

The intervals that intersect the target area can be classified into four categories:

(1) _a_ non-trivial intervals \([\ell_j,u_j]\) with \(\ell_j\le\ell_{j_1}\) and \(u_j\ge u_{j_2}\); they **contain** the target area;

(2) _b_ intervals \([\ell_j,u_j]\) with \(\ell_j>\ell_{j_1}\) and _u<sub>j</sub>\<u_<sub>_j_<sub>2</sub></sub>; they **are strictly contained** in the target area and contain neither endpoint of the target area;

(3) _c_ intervals \([\ell_j,u_j]\) with \(\ell_j\le\ell_{j_1}\) and _u<sub>j</sub>\<u_<sub>_j_<sub>2</sub></sub>; they intersect the target area on the **left**;

