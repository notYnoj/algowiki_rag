Input: problem size n,D\[0\], cost function \(w(\cdot,\cdot)\)<br>
Output: D\[1..n\]: the DP table<br>
Maintains: B: an sorted array storing triples of (\[_l,r_\],j), meaning that<br>
for all \(l\le i\le r\), the current best decision best\[i\]=j<br>
now \(\leftarrow 0\)<br>
while now\<n do<br>
  \(cordon\leftarrow\) FindCordon(now)<br>
   UpdateBest(now, cordon)<br>
   now \(\leftarrow\) cordon-1<br>
return D\[1..n\]<br>
Function FindCordon(now)<br>
   \(cordon\leftarrow n+1\)<br>
   for \(t\leftarrow 1\) to logn do<br>
   \(l\leftarrow now+2^{t-1}\)<br>
   \(r\leftarrow min(n,now+2^t-1)\)<br>
   ParallelForEach \(j\in[l,r]\) do<br>
   Let best\[j\] be the current best decision of j recorded by B<br>
   \(D[j]\leftarrow E[best[j]]+w(best[j],j)\) // relax j<br>
   Binary search in B and find<br>
   s<sub>j</sub>=min{i:E\[j\]+w(j,i)\<E\[best\[i\]]+w(best\[i\],i)},<br>
   i.e., i is the first state that can be successfully relaxed by j<br>
   \(cordon\leftarrow min(cordon,min_{l\le j\le r}s_j)\)<br>
   if \(cordon\le r+1\) then break<br>
   return cordon<br>
Function UpdateBest(now, cordon)<br>
   Tree \(T\leftarrow\) FindIntervals(now+1, cordon-1, cordon,n)<br>
   Flatten T into array B<br>
   Merge adjacent intervals with the same best decision in B<br>
Function FindIntervals(j<sub>l</sub>,j<sub>r</sub>,i<sub>l</sub>,i<sub>r</sub>)// use D\[j<sub>l</sub>..j<sub>r</sub>\] to update best\[i<sub>l</sub>..i<sub>r</sub>\]<br>
   if i<sub>l</sub>\>i<sub>r</sub> then return null<br>
   if j<sub>l</sub>=j<sub>r</sub> then return a leaf node(\[i<sub>l</sub>,i<sub>r</sub>\],j<sub>l</sub>)<br>
   \(i_m\leftarrow(i_l+i_r)/2\)<br>
   \(j_m\leftarrow argmin_{j_l\le j\le j_r}(E[j]+w(j,i_m))\)<br>
   \(x\leftarrow node([i_m,i_m],j_m)\)<br>
   In Parallel:<br>
   \(T_l\leftarrow\) FindIntervals(j<sub>l</sub>,j<sub>m</sub>,i<sub>l</sub>,i<sub>m</sub>-1)<br>
   \(T_r\leftarrow\) FindIntervals(j<sub>m</sub>,j<sub>r</sub>,i<sub>m</sub>+1,i<sub>r</sub>)<br>
   return node x with left child as T<sub>l</sub> and right child as T<sub>r</sub>

<tbc>as long as its best decision has been finalized. For the convex case, we will use the fact as shown below.

Fact 4.1. _In convex GLWS, let_ \(S=\{j:j>i\wedge best[j]\le i\}\)_, which is the set of states with best decisions no later than state i; then S is a consecutive range of states starting from i_+1.

This is a known fact in the sequential setting (can be proved by induction). It suggests that the frontier of each round in the phase-parallel algorithm is a consecutive range of states. Based on this idea, we will maintain _now_ as the last finalized state in each round. Then in the next round, ideally, the algorithm should find the cordon at _cordon_, where all states \[_now_+1_,cordon_-1\] are ready and can compute their true DP value from (i.e., have their best decisions at) states no later than _now_. We show an example of the post-office problem to illustrate the phase-parallel framework in Fig. 3. Based on the discussions above, ideally, in round _i_, the ready states in the frontier are those where the best solution contains _i_<tbc>

<tbc>post offices. This is because their best decision must have _i_-1 post offices, and must be finalized in the previous round.

This high-level idea is presented in the main function of Alg. 1. Starting from _now_=0, given the current finalized states \[0_,now_\], we will find all ready states \[_now_+1_,cordon_-1\] using the Cordon Algorithm, which essentially will find the cordon at _cordon_. We explain this part with more details in Sec. 4.2.1. Similar to the sequential algorithm, we also maintain a data structure _B_ to store all triples (\[_l,r_\],_j_) in order, which indicates that all states between _l_ and _r_ have best decisions at _j_. This data structure is essential to guarantee the efficiency of finding the next frontier, and also has to be updated after each round with the new DP values (Line 4).

## 4.2.1 Finding the Cordon.

To find the ready states in each round, we use the Cordon Algorithm. Namely, with all states up to _now_ finalized, we can attempt to use the tentative states after _now_ to update other tentative DP values. Once we find any _j_ that can update _i_, we put a sentinel at _i_. Among all sentinels, the smallest (leftmost) one will give the final position of the cordon.

However, note that we cannot afford exhaustive checking for all pairs of states (_j,i_). First of all, checking all possible _j\>now_ may incur large overhead in work, since most of the later states are unready anyway. Ideally, the algorithm should check up to exactly the position of _cordon_, but this would be a chicken-and-egg problem. To handle this, our idea is to use _prefix-doubling_, a common idea in parallel algorithm design (e.g., \[19, 33, 47, 49, 81\]) to achieve work-efficiency and high parallelism. Here, prefix-doubling is used in function FindCordon in Alg. 1, which attempts to extend the cordon by a batch of 2<sup>_t_-1</sup> states for increasing _t_ in each substep _t_. If the entire batch is ready-i.e., no states in \[_now_+1_,now_+2_<sup>t</sup>_) can be relaxed by each other, and all sentinels are outside the batch-we try a larger step and extend the cordon to _now_+2<sup>_t_+1</sup>. During the process, we will maintain _cordon_ as the leftmost sentinel so far. Once we find _cordon_ is inside the batch, it means that this batch is not fully ready. Therefore, the process stops and returns the current value of _cordon_ to the main algorithm.

Using prefix doubling, the parallel algorithm may check more states than the ready ones, but the number of "wasted" states is at most twice of the "useful" ones which will be finalized in this round. Hence, the total number of processed states is _O(n_).

We then discuss the way to avoid checking all states _i\>j_ when _j_ puts sentinels. By DM, if _j_ can successfully relax _i_, then _j_ can also successfully relax all states _i..n_. Therefore, we only need to put a sentinel at the first such state _i_. Recall that we maintain all best decision triples in a data structure _B_ in sorted order. By DM, we can simply binary search (_O_(log_n_) cost) in _B_ to find _s<sub>j</sub>_ as the first tentative state that can be updated by _j_, and put a sentinel there.

The FindCordon in Alg. 1 gives the full process as described above. Each iteration of the while-loop at Line 9 is a substep, which processes a batch of states in \[_now_+2<sup>_t_-1</sup>_,now_+2_<sup>t</sup>_) in substep _t_. Then for each state _j_ in this batch (in parallel), we use _B_ to find the first state that can be updated by _j_ and put a sentinel at this position _s<sub>j</sub>_. Finally, the leftmost sentinel so far forms the cordon. When the cordon is within the current batch, the algorithm returns. We also show an illustration of this process in Fig. 3.

Lemma 4.1. _The function FindCordon has O(h_log_n_) _work and O_(log<sup>2</sup>_n_) _span, where h=cordon-now_-1 _is the frontier size._

**Algorithm 1:** Parallel Convex GLWS

