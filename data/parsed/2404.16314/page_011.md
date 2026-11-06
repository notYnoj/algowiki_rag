<tbc>In addition to the diagonal edges as in LCS (see Fig. 2), for rows and columns, there also exist effective (red) edges (see Fig. 4(a)). Here for simplicity we only draw a subset of these edges, and every state _D_\[_i,j_\] always have one vertical effective edge (to compute _Q_\[_i,j_\]), one horizontal effective edge (to compute _P_\[_i,j_\]), and may have a diagonal edge if _A_\[_i_\]=_B_\[_j_\]. All these edges imply the sentinels, which form the cordon and imply the regions for ready states, as shown in Fig. 4(b). The cordon is still a staircase as in LCS.

However, finding the cordon in GAP is sophisticated. We cannot directly use a tournament tree as in LIS, since the vertical and horizontal edges are computed on-the-fly and not known ahead of time. Meanwhile, in a 2D table where the cordon is a staircase, we cannot simply use prefix-doubling as in GLWS in Sec. 4. We propose a unique solution here to use prefix-doubling on a 2D table and computes the staircase cordon efficiently. This approach will consider each row separately, but for all rows, we run prefix doubling synchronously and try to see if the next ranges are available. First, we put a sentinel on state (_x,y_) with a diagonal edge if (_x_-1_,y_-1) is not finalized. We will maintain the best-decision structure for each row and column, in the same way as the GLWS algorithm. For this region to be checked, we will use the same approach as in Alg. 1 to compute _P_ and _Q_, take the minimum as _D_, and use _D_ to check their readiness. If a state (_x,y_) obtains the best decision from another tentative state, we will put a sentinel on (_x,y_), which will block the other states \((x',y')\) with \(x'\ge x\) and \(y'\ge y\). The work to put the sentinels is proportional to the number of states we checked in the prefix-doubling, and the span is polylogarithmic.

Finally we discuss how to handle the sentinels placed as above. We store all sentinels based on the row index on increasing order. After this, applying a prefix-min on these sentinels gives part of the cordon (if they exist), and we will merge it with the previous cordon. Then, for all tentative states, we check whether they are on the correct side, and invalidate those across the cordon. Since we are using prefix doubling, the wasted work for the invalid states can be amortized. In the next prefix doubling step, we will also use the cordon to limit the search region. Once all states within the cordon are checked for readiness, we can move to the next round. Due to prefix doubling, we only need _O_(log_n_) steps in each round.

Theorem 5.2. _The Cordon Algorithm for the GAP problem has O(mn_log_n_) _work and O(k_log<sup>2</sup>_n_) _span, where n and_ \(m\le n\) _are the input size and k is the effective depth of the_ \(\Gamma_{gap}\)_-optimized DAG for the sequential algorithm_ \(\Gamma_{gap}\) _introduced in Sec. 5.2._

Recall that the sequential GAP algorithm \(\Gamma_{gap}\) gets the DP value for each state _s_=(_i,j_) by solving the GLWS problems in row _i_ and column _j_, respectively, and the diagonal edge \((i-1,j-1)\rightarrow(i,j)\) if applicable. Therefore, the optimal DAG \(G_{\Gamma_{gap}}\) contains three types of edges

\(\bullet\) \((i,j)\rightarrow(i',j)\) for all \(i'>i\),<tbc>

\(\bullet\) \((i,j)\rightarrow(i,j')\) for all \(j'>j\), and<tbc>

\(\bullet\) \((i-1,j-1)\rightarrow(i,j)\) if _A_\[_i_\]=_B_\[_j_\].

Among them, the effective edges include:

\(\bullet\) \((i,j)\rightarrow(i',j)\) where _i_ is the best decision for \(i'\) in the GLWS problem on row _j_,<tbc>

\(\bullet\) \((i,j)\rightarrow(i,j')\) where _j_ is the best decision for \(j'\) in the GLWS problem on column _i_, and<tbc>

\(\bullet\) \((i-1,j-1)\rightarrow(i,j)\) if _A_\[_i_\]=_B_\[_j_\].

WLOG we assume \(m\le n\) in this section. We first prove the span bound. We will show that the Cordon Algorithm finishes in _k_ rounds, where _k_ is the effective depth of \(G_{\Gamma_{gap}}\).

Lemma 5.2. _Given two sequences of sizes n and_ \(m\le n\)_, the Cordon Algorithm on GAP edit distance finishes in_ \(k=\hat{d}(G_{\Gamma_{gap}})\) _rounds._

_Proof._ The proof is similar to Lemma 4.4. We also define the effective depth of a state _s_ as \(\hat{d}s\). We will show by induction that _s_ is processed in round _r_ iff. \(\hat{d}s=r\). The base case holds trivially.

Assume the conclusion holds for all rounds up to _r_-1. We will show it is also true for round _r_. We first prove the "if" direction, i.e., if a state _s_=(_i,j_) (_i_-th row, _j_-th column) has effective depth _r_, it must be in the frontier of round _r_. This is equivalent to show that there is no sentinel that blocks _s_. For simple description, for two states _s_=(_i,j_) and \(s'=(i',j')\), we say \(s<s'\) if \(i\le i'\) and \(j\le j'\). Clearly, if a state \(s<s'\), a sentinel on _s_ will block \(s'\). Assume to the contrary that there is a state _y\<s_ with a sentinel, which is put by another tentative state _x\<y_. This means that the tentative state _x_ is a better decision than all finalized states, indicating that the best decision of _y_, denoted as _y_<sup>∗</sup>, must also be tentative. Based on the induction hypothesis, the effective depth of _y_<sup>∗</sup> must be larger than _r_-1. Therefore, \(\hat{d}(y)\ge\hat{d}(y^*)+1>r-1+1=r\), which means that \(\hat{d}(y)\) is at least _r_+1. Let \(y=(i',j')\). _y_ and _s_ can be connected by either one normal edge (when they are in the same row or column) or two normal edges \(((i',j')\rightarrow(i,j')\) and \((i,j')\rightarrow(i,j)\)). This means that the effective depth of _s_ is at least the same as _y_, which is _r_+1. This leads to a contradiction.

We then prove the "only if" condition, i.e., if a state _s_ is in the frontier of round _r_, it must have effective depth _r_. The induction hypothesis suggests that all states with effective depth smaller than _r_ have been finalized in previous rounds, so we only need to show that \(\hat{d}(s)\) cannot be larger than _r_. Assume to the contrary that \(\hat{d}(s)\ge r+1\). Let the path to _s_ with effective depth \(\hat{d}(s)\) be _x_<sub>1</sub>_,x_<sub>2</sub>_,...,s_. Since the total number of effective edges on this path is at least _r_+1, there must exist an effective edge \(x_i\rightarrow x_{i+1}\) on the path such that \(\hat{d}(x_i)=r\) and \(\hat{d}(x_{i+1})=r+1\). However, based on induction hypothesis, _x<sub>i</sub>_’s best decision must have been finalized. In round _r_, _x_ must get its true DP value, and will find itself able to update _x_<sub>_i_+1</sub>. Therefore, there will be a sentinel on _x_<sub>_i_+1</sub>_\<s_, and _s_ cannot be identified in the frontier of round _r_. □

Combining Lemma 4.1 and 4.2, the span in each round is _O_(log<sup>2</sup>_n_). This proves the span bound in Thm. 5.2.

We then prove the work bound in Thm. 5.2.

Lemma 5.3. _Given two sequences of sizes n and_ \(m\le n\)_, the Cordon Algorithm on GAP edit distance has work O(mn_log_n)._

_Proof._ As \(G_{\Gamma_{gap}}\) is a grid graph, its depth is no more than _m+n_. By Lemma 5.2 the algorithm will finish in _k=O(n_) rounds. In each round, we do prefix-doubling across all _m_ rows and try to push the frontier on each row. In each prefix-doubling step we do a prefix-min that costs _O(m_) work, so the cost of prefix-doubling is _O(m_log_n_) in each round, and _O(mn_log_n_) in total. Suppose _h_ is the frontier size in one round. Due to prefix-doubling, the number of tentative states we visited is at most 2_h_. Combining Lemma 4.1<tbc>

