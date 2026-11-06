• _if_ \(w'(v)>c\omega\)_, (v is heavy), then the starting time t of any job_ (_v,t_) _in the schedule_ \(\hat{S}(u)\) _of any_ \(u\in V\) _is an integer multiple of_ \(\omega\) _(aligned to a box),_<tbc>

• _if_ \(w'(v)\le c\omega\)_, (v is light), then the starting time t of any query_ (_v,t_) _in the schedule_ \(\hat{S}(u)\) _of any_ \(u\in V\) _is an integer multiple of_ \(\frac{1}{cn}\) _(aligned to a slot)._

_Proof._ We consider an optimal consistent schedule assignment \(\hat{\Sigma}\) for tree \(T'\), \(|\hat{\Sigma}|=\mathtt{OPT}(T')\). Fix \(u\in V\) arbitrarily, and let (_v<sub>u,i</sub>,t<sub>u,i</sub>_) be the _i_-th query job in \(\hat{\Sigma}(u)\). Consider now the schedule \(\hat{\Sigma}^*(u)\) for _T_ based on the same sequence assignment, in which the job (_v<sub>u,i</sub>,t<sub>u,i</sub>_) is replaced by the job \((v_{u,i},t_{u,i}^*)\) with \(t_{u,i}^*=(1+\frac{2}{c})t_{u,i}\). We have for any two consecutive jobs at _u_:

\(t_{u,i+1}^*-t_{u,i}^*=\left(1+\frac{2}{c}\right)(t_{u,i+1}-t_{u,i})\ge\left(1+\frac{2}{c}\right)w(v_{u,i}),\) (4.2)

where we assume by convention that for the last job index _i<sub>max</sub>_, \(t_{u,i_{max}+1}=|\hat{\Sigma}(u)|\). We now observe that schedule assignment \(\hat{\Sigma}^*\) on tree _T_ can be directly converted into schedule assignment \(\hat{S}\) on tree \(T'\) as follows. The query sequence of each vertex is preserved unchanged. If _v<sub>u,i</sub>_ is a heavy vertex, then within time interval \([t_{u,i}^*,t_{u,i+1}^*]\) we allocate to vertex _v<sub>u,i</sub>_ an interval of full boxes, starting at time \(\lceil t_{u,i}^*\rceil_\omega\). Indeed, by (4.2) we have:

\(t_{u,i+1}^*-\lceil t_{u,i}^*\rceil_\omega>t_{u,i+1}^*-t_{u,i}^*-\omega>\left(1+\frac{2}{c}\right)w(v_{u,i})-\omega>w(v_{u,i})+\omega>w'(v_{u,i}).\)

Since no two jobs overlap and the time transformation is performed identically for all vertices, the validity and consistency of schedule assignment \(\hat{S}\) for tree \(T'\) follows. We also have \(|\hat{S}|\le(1+\frac{2}{c})|\hat{\Sigma}|=(1+\frac{2}{c})\mathtt{OPT}(T')\).

To obtain the second part of the claim (alignment for light vertices) it suffices to round up the starting time of query times of all (light) vertices to an integer multiple of \(\frac{1}{cn}\). Since all weights in \(T'\) are integer multiples of \(\frac{1}{cn}\), and so are the starting times of queries to heavy vertices in \(\hat{S}\), the correctness and consistency of the obtained schedule again follows directly. This final transformation increases the duration by at most \(\frac{1}{c}\le\frac{1}{c}\mathtt{OPT}(T')\), and combining the bounds for both the transformations finally gives the claim.

A schedule on tree \(T'\) satisfying the conditions of Lemma 4.2, and the resulting search strategy, are called _aligned_. Subsequently, we will design an aligned strategy on tree \(T'\), and compare the quality of the obtained solution to the best aligned strategy for \(T'\).

The intuition between the separate treatment of heavy vertices (aligned to boxes) and light vertices (aligned to slots) in aligned schedules is the following. Whereas the time ordering of boxes is essential in the design of the correct strategy, in our dynamic programming approach we will not be concerned about the order of slots within a single box (i.e., the order of queries to light vertices placed in a single box). This allows us to reduce the state space of a node. Whereas the ordering of slots in the box will eventually have to be repaired to provide a correct strategy, this will not affect the quality of the overall solution too much (except for the issue of light down queries pointed out earlier, which are handled separately in Section 5).

## 4.2 Dynamic Programming Routine for Fixed Box Size

Let the values of parameter _c_ and box size \(\omega\) be fixed as before. Additionally, let \(L\in\mathbb{N}\) be a parameter representing the time limit for the duration of the considered vertex schedules when measured in boxes, i.e., the longest schedule considered by the procedure will be of length \(L\omega\) (we will eventually choose an appropriate value of _L=O_(log_n_) as required when showing Theorem 3.3).

