To a first approximation, this means that every string _x_ either has a long imbalanced subinterval or else behaves like the periodic string \((0^\ell 1^\ell)^{w/2\ell}\) for some \(\ell\).

Now we return to summarizing the proof of Theorem 1.2. By prior results \[RS20, AW21\] (see also \[Akm21\]), it suffices to consider the "perfectly balanced case," where the shorter string _x_ has an equal number of zeros and ones.

**Theorem 3.2.** _For all_ \(\varepsilon>0\)_, there exists an absolute constant_ \(\delta=\delta(\varepsilon)>0\) _and a deterministic algorithm that, on input strings x and y with_ \(0(x)=1(x)\le min(0(y),1(y))\)_, gives a_ \((\frac{1}{2}+\delta)\)_-approximation of the longest common subsequence in time_ \(O(n^{1+\varepsilon})\).

Theorem 1.2 follows from Theorem 3.2 by prior work \[RS20, AW21\]; for completeness include the details in Section 6. In the rest of this section, we sketch the proof of Theorem 3.2.

Our algorithm for Theorem 3.2, which is described in pseudocode in Algorithms 1 and 2, is a modification of the standard quadratic time DP algorithm for LCS, which we formulate as follows. The standard DP algorithm computes LCS(_x,y_) by computing the full array \(\mathsf{DP}[i][j]:=\mathsf{LCS}(x_{[i]},y_{[j]})\), \(0\le i\le|x|\), \(0\le j\le|y|\) via the recursion

\(\mathsf{DP}[i][j]=\left\{\begin{array}{ c c }
max\left(\mathsf{DP}[i][j-1],\mathsf{DP}[i-1][j],\mathsf{DP}[i-1][j-1]+1\right) & \text{if}x_i=y_i \\
max\left(\mathsf{DP}[i][j-1],\mathsf{DP}[i-1][j]\right) & \text{otherwise.}
\end{array}\right.\)

In total this takes \(O(|x|\cdot|y|)\) applications of the recursion. To prove Theorem 3.2, we don’t need to compute the exact value of LCS(_x,y_), rather, we only need to output a value between \((1/2+\delta)\mathsf{LCS}(x,y)\) and LCS(_x,y_). To estimate the LCS efficiently, we modify the DP above by recursing over large subrectangles instead of one bit at a time. We compute a collection of large rectangles \(I\times J\) (where _I_ and _J_ are long subintervals of \[|_x_|\] and \[|_y_|\], respectively) and estimates \(\kappa(I\times J)\) for their LCS (we call these _certified rectangles_). We guarantee that \(\kappa(I\times J)\le\mathsf{LCS}(x_I,y_J)\) in every rectangle, and we desire that many of these \(\kappa(I\times J)\) are good estimates of LCS(_x<sub>I</sub>,y<sub>J</sub>_). (For readers familiar with \[CDG<sup>+</sup>20\], finding these rectangles is analogous to their "Covering Phase").

The large rectangles under consideration are \(\theta w\)-aligned subrectangles of \([|x|]\times[|y|]\), where _w_≈|_x_|/log|_x_| is a typical length of the _x_-intervals and \(\theta\) is a small constant discretization parameter (in the real proof, we discretize _x_-intervals and _y_-intervals slightly differently, but ignore that here for sake of illustration). Our modified DP algorithm is then

\(\mathsf{DP}[i][j]=max\left(\mathsf{DP}\left[startI-\theta w\right]\left[startJ\right],\mathsf{DP}\left[startI\right]\left[startJ-\theta w\right],\right.\)<br>
\(\left.\mathsf{DP}\left[startI\right]\left[startJ\right]+\kappa(I\times J)\text{over}I\times J\in\mathcal{R}\text{s.t. end}I=i,\text{end}J=j\right),\) (1)

where \(\kappa(I\times J)\) denotes the lower bound for LCS(_x<sub>I</sub>,y<sub>J</sub>_) guaranteed by our certification algorithm. Observe that by induction DP\[_i_\]\[_j_\] is still a lower bound for LCS(_x_<sub>\[_i_\]</sub>_,y_<sub>\[_j_\]</sub>). Because of our discretization, we only need to consider _i_ and _j_ a multiple of \(\theta w\), so the number of dynamic programming states drops from \(O(|x|\cdot|y|)\) to \(O(\frac{|x|\cdot|y|}{(\theta w)^2})\le\tilde{O}(\frac{|y|}{|x|})\). Thus it remains to show we can quickly certify a collection of rectangles for which the dynamic program (1) outputs a \((\frac{1}{2}+\delta)\)-approximation.

The main step is find a significant fraction of "good" rectangles for which \(\kappa(I\times J)>(1/2+\gamma)\mathsf{LCS}(x_I,y_J)\). We look for good rectangles in three different ways, as shown in Algorithm 1. (1) First, we check for the "trivial" rectangles where \(\mathsf{Trivial}(x_I,y_J)>(1/2+\gamma)|x_I|\) (\(\gamma>0\) chosen very small). (2) Next, we black-box the equal-length LCS algorithm of Rubinstein and Song, and efficiently check for squares \(I\times J\) with |_I_|=|_J_| and \(\mathsf{LCS}(x_I,y_J)>(1/2+\gamma)|x_I|\). (3) Finally -- and this is the main technical contribution of our work -- we use the algorithmic structure lemma, Lemma 4.1, to efficiently compute "oscillation frequencies" for the intervals _I_ and _J_. For any given rectangle \(I\times J\) where |_J_| is longer than |_I_|, they can then be certified quickly by checking if _J_ has the same oscillation frequency as _I_. For technical reasons, for this last type of rectangle we<tbc>

