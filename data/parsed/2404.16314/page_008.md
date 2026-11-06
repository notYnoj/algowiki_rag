<tbc>_Proof._ As discussed above, the prefix doubling scheme may attempt to process up to \(h'\) states, where \(h'\le 2h\). For each such state, we may binary search in _B_ to find _s<sub>j</sub>_ in _O_(log_n_) cost, and check the condition on Line 15 in _O_(1) cost. Therefore, FindCordon has work _O(h_log_n_) and span _O_(log<sup>2</sup>_n_). □

### 4.2.2 Generating New Best-Decision Array.

The efficiency of the algorithm relies on maintaining an ordered data structure _B_ for all best decision triples. We will store _B_ as an array of all such triples in sorted order, such that the binary search in Line 15 can be performed efficiently. Therefore, after we get the newly finalized states _D_\[_now_+1_...cordon_-1\], we need to update _B_ accordingly to get the new best decision for all states in \[_cordon,n_\].

We use a divide-and-conquer approach to do this. Function FindIntervals(_j<sub>l</sub>,j<sub>r</sub>,i<sub>l</sub>,i<sub>r</sub>_) finds all best decision triples for states in range \[_i<sub>l</sub>,i<sub>r</sub>_\], with best decisions in range \[_j<sub>l</sub>,j<sub>r</sub>_\]. Note that we only need the best decisions for all states after _cordon_. All these states must have their current best decisions within \[_now_+1_,cordon_-1\] (if their best decisions are before _now_, they must have been ready in this round and been included in the frontier). Therefore, at the root level, we call FindIntervals(_now_+1_,cordon_-1_,cordon,n_).

In FindIntervals, we first compute _j<sub>m</sub>=best_\[_i<sub>m</sub>_\] where _i<sub>m</sub>_=(_i<sub>l</sub>+i<sub>r</sub>)/_2, i.e., the best decision of the state in the middle. By (convex) DM, the best decisions of \(i\in[i_l,i_m-1]\) are in \[_j<sub>l</sub>,j<sub>m</sub>_\], and the best decisions of \(i\in[i_m+1,i_r]\) are in \[_j<sub>m</sub>,j<sub>r</sub>_\]. We will deal with the two subproblems in parallel. To collect all (\[_l,r_\]_,j_) triples in parallel, we build a tree-based structure bottom-up in the recursion. Finally, we flatten the tree to an array and merge the adjacent intervals if they have the same value of _j_.

Lemma 4.2. _The function UpdateBest has O(h_log_n_) _work and O_(log<sup>2</sup>_n_) _span, where h=cordon-now_-1 _is the frontier size._

_Proof._ Flattening and removing duplicates can be performed by simple parallel primitives on trees and arrays in _O(h_) work and _O_(log_n_) span. Below we will focus on the more complicated FindIntervals function. The span of FindIntervals comes from 1) _O_(log_n_) levels recursions and 2) _O_(log_n_) span to check all states in \[_j<sub>l</sub>,j<sub>r</sub>_\] in parallel. For the work, each recursive call in FindIntervals deals with a range of states \[_i<sub>l</sub>,i<sub>r</sub>_\] using best decision candidates in range<tbc>

<tbc>\[_j<sub>l</sub>,j<sub>r</sub>_\]<tbc>

<tbc>. The algorithm first finds \(i_m\in[i_l,i_r]\) and its best decision \(j_m\in[j_l,j_r]\). This can be done by comparing all possible decisions in \[_j<sub>l</sub>,j<sub>r</sub>_\], which is _O(j<sub>r</sub>-j<sub>l</sub>_) work. split the ranges into two subproblems and recurse. Let _N_=|_i<sub>r</sub>-i<sub>l</sub>_+1| and _M_=|_j<sub>r</sub>-j<sub>l</sub>_+1| denoting the sizes of the two ranges. The work of FindIntervals indicates the following recurrence:

\(W(N,M)=W(N/2,M_1)+W(N/2,M_2)+O(M)\)

where _M_<sub>1</sub>+_M_<sub>2</sub>=_O(M_). This solves to _O(M_log_n_). On the root level, _M=cordon-now_-1=_h_. This proves that the work is _O(h_log_n_) for frontier size _h_. □

## 4.3 Parallel Concave GLWS

To extend the algorithm to the concave case, we need a few modifications. In FindCordon, by the concavity, if _j_ can update _i_, then _j_ must be able to update _j_+1. Therefore, in Line 15 in Alg. 1, we check whether _j_ can update _j_+1. If so, we put a sentinel at _j_+1. The other modifications are in FindIntervals. First, due to concavity, when we find _j<sub>m</sub>_ as the best decision of _i<sub>m</sub>_ in Line 27, we need to swap the last two parameters in the first and second recursive calls, i.e., the best decision range for states _i<sub>m</sub>_+1 to _i<sub>r</sub>_ must be before _j<sub>m</sub>_, and those in _i<sub>l</sub>_ to _i<sub>m</sub>_-1 must be after _j<sub>m</sub>_.

A more involved modification in the concave GLWS is that after we get the array _B_ from FindIntervals, we have to merge it with the old array _B_ before this round -- FindIntervals only considers the best decisions among \[_now_+1_,cordon_-1\], but in the concave case, these states may also have better decisions using states before _now_. Suppose we have generated the array _B<sub>new</sub>_ storing (\[_l,r_\]_,j_) triples, and we want to merge it with _B<sub>old</sub>_. Both of _B<sub>old</sub>_ and _B<sub>new</sub>_ contain the best decisions of states \[_cordon..n_\]. The difference is that the _js_ in _B<sub>old</sub>_ are from \[0_..now_\], while the _js_ in _B<sub>new</sub>_ are from \[_now_+1_..cordon_-1\]. By the concave decision monotonicity, the key is to find a cutting point _p_, where the best decisions of \[_cordon..p_\] are from _B<sub>new</sub>_, and the best decisions of \[_p_+1_,n_\] are from _B<sub>old</sub>_.

1 **ParallelForEach** (\[_l<sub>k</sub>,r<sub>k</sub>_\]_,j<sub>k</sub>_) _in B<sub>new</sub>_ **do**<br>
   \(x_k\leftarrow\) search the best decision of _l<sub>k</sub>_ from _B<sub>old</sub>_.<br>
   Binary search the last (\[_l<sub>k</sub>,r<sub>k</sub>_\]_,j<sub>k</sub>_) in _B<sub>new</sub>_ such that<br>
   E\[_j<sub>k</sub>_\]+w(_j<sub>k</sub>,l<sub>k</sub>)\<E_\[_x<sub>k</sub>_\]+w(x<sub>k</sub>,l<sub>k</sub>_).<br>
   Binary search the first (\[_l<sub>k</sub>,r<sub>k</sub>_\]_,j<sub>t</sub>_) in _B<sub>old</sub>_ such that<br>
   E\[_j<sub>t</sub>_\]+w(_j<sub>t</sub>,r<sub>t</sub>)\<E_\[_j<sub>k</sub>_\]+w(_j<sub>k</sub>,r<sub>t</sub>_).<br>
   Binary search the last _p_ in \[_l<sub>k</sub>,r<sub>t</sub>_\] such that<br>
   E\[_j<sub>k</sub>_\]+w(_j<sub>k</sub>,p)\<E_\[_j<sub>t</sub>_\]+w(_j<sub>t</sub>,p_).<br>
   return p

Here we show Alg. 2 to find _p_ in _O(h_log_n_) work and _O_(log_n_) span, where _h_=|_B<sub>new</sub>_| is the frontier size. For all _l<sub>k</sub>_ in _B<sub>new</sub>_, we preprocess its best decision stored in _B<sub>old</sub>_. This step requires _O(h_log_n_) work and _O_(log_n_) span. Then we search in _B<sub>new</sub>_ to find the interval that _p_ locates in. After this step, there is only one interval (\[_l<sub>k</sub>,r<sub>k</sub>_\]_,j<sub>k</sub>_) in _B<sub>new</sub>_ is interesting. Then we can binary search in _B<sub>old</sub>_ to find the exact _p_. Note that this method can be easily modified to merge _B<sub>old</sub>_ and _B<sub>new</sub>_ even if the cost function is convex.

## 4.4 Theoretical Analysis

In this section, we show the theoretical analysis for our parallel GLWS algorithm. We first summarize our main results as follows.

0
1
2
3
4
5
6
7
8
9
10
11
12
frontier 1
frontier 2
frontier 3
frontier 4
1 post office in solution
2 post offices in solution
3 post offices in solution
4 post offices in solution
Example of generating frontier 2
Subround 1
Process one state 4. cordon = 13.
Assume 4 cannot update any other tentative states.
Subround 2
Process next two states 5 and 6 in parallel.
Assume 5 cannot update any other tentative states.
The earliest state 6 can update is 8. So 6 puts a sentinel on 8. cordon=8.
Subround 3
Process next four states 7-10 in parallel.
7 puts a sentinel on 9; 8-10 may or may not put sentinels on other states.
cordon = 8 < 10. Return cordon(=8).

**Figure 3:** Example of applying the Cordon Algorithm to the post office problem with convex cost function. Circles (states) are villages. Arrows are best decisions between states. The final answer is four post offices serving villages 1-3, 4-7, 8-9, 10-12, respectively. The subrounds below illustrate the prefix-doubling scheme in FindCordon.

**Algorithm 2:** Find the cutting point _p_

