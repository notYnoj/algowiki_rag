### 3.3 Black-Box Calls to Existing ED and LCS Algorithms

We will use an _O_(1)-approximate ED algorithm, e.g., the following tradeoff proved in \[GRS20\]<sup>12</sup>:

**Lemma 3.2.** _Given two strings X and Y with lengths that sum to n, there is a randomized algorithm that computes a 4-approximation of_ ED(_X,Y_) _in O(n_<sup>1.61</sup>) _time._

We also use Ukkonen’s algorithm \[Ukk85\] for exact ED when the ED is small<sup>13</sup>:

**Lemma 3.3.** _Given two strings X and Y with lengths that sum to n and an upper bound k, there is an algorithm running in O(nk_) _time that can:_

• _Decide whether_ \(\mathrm{ED}(X,Y)\le k\);<tbc>

• _If_ \(\mathrm{ED}(X,Y)\le k\)_, compute_ ED(_X,Y_) _exactly._

When the LCS is small, the following result has been known since the 70s \[Hir77\]:

**Lemma 3.4.** _Given two strings X and Y with lengths that sum to n and an upper bound k, there is an algorithm running in O(nk+n_log(_n_)) _time that can:_

• _Decide whether_ \(\mathrm{LCS}(X,Y)\le k\);<tbc>

• _If_ \(\mathrm{LCS}(X,Y)\le k\)_, compute_ LCS(_X,Y_) _exactly_<sup>14</sup>.

### 3.4 Rounding

To avoid fractional results after divisions, for \(\lambda=2^{\lfloor 0.99\mathrm{log}(n)\rfloor}=\Theta(n^{0.99})\), we ensure that the lengths of two input strings are multiples of \(\lambda\) by padding them with arbitrary characters. The error we introduce with this rounding is \(O(\lambda)\), which is within (1+_o_(1)) when the ED/LCS is \(\omega(\lambda)\). When the ED/LCS is \(O(\lambda)\), we can use Lemma 3.3 or Lemma 3.4 to compute the answer exactly in \(O(n\lambda)=O(n^{1.99})\) time. Thus we can assume that input strings both have a length that is a multiple of a power of 2 of order \(\Omega(n^{0.99})\).

## 4 Tree Total Deviation

In this section we will introduce the notion of tree total deviation, which will be an important tool in analyzing our main algorithm for Edit Distance and LCS. We first introduce it in its basic form (Section 4.1). We then study a scaled variant of it (Section 4.2).

<sup>12</sup>We note that the choice of using \[GRS20\] is arbitrary. Since neither the running time nor the exact approximation factor is the bottleneck for our analysis, any of the truly sub-quadratic _O_(1)-approximation algorithms, starting with \[CDG<sup>+</sup>20\] and including \[CDG<sup>+</sup>20, And20, BR20, KS20b, AN20, RSSS25\] would suffice for our purpose. <sup>13</sup>There are faster algorithms for this problem, e.g., \[LMS98\]. However the difference would not translate to a qualitative improvement for our purposes. It is interesting that Ukkonen’s algorithm \[Ukk85\] also works for the more general setting of shortest paths on grids with diagonal shortcuts. Thus the only part in our algorithm for Edit Distance that requires actual strings is the _O_(1)-approximation algorithm from Lemma 3.2. <sup>14</sup>The original result states that there is an algorithm running in _O(n_LCS(_X,Y_)+_n_log(_n_)) time, this can easily be applied to the decision problem here by simply testing if the algorithm terminates within _O(nk+n_log(_n_)) time.

