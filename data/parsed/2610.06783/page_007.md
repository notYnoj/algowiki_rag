<tbc>3SUM or Exact Triangle.

**Theorem 2** (Theorems 19, 22, and 35)**.** _On a word RAM with O_(log_n)-bit words, deterministic algorithms solve the following problems, where all numbers in the input are integers of absolute value n_<sup>_O_(1)</sup>:

• _Exact Triangle on n-vertex graphs in O(n_<sup>2.9983</sup>) _time,_<tbc>

• _APSP on directed n-vertex graphs with no negative cycles in O(n_<sup>2.9995</sup>) _time,_<tbc>

• _the_ (min,+)_-product of two_ \(n\times n\) _matrices in O(n_<sup>2.9995</sup>) _time, and_<tbc>

• 3_SUM on n numbers in O(n_<sup>1.9992</sup>) _time._

_In the real RAM in which the only operations allowed on real numbers are comparisons, additions, and subtractions, Las Vegas algorithms solve the following problems on real inputs:_

• 3_SUM on n numbers in O(n_<sup>1.998</sup>) _expected time,_<tbc>

• _APSP in O(n_<sup>2.998</sup>) _expected time,_<tbc>

• _the_ (min,+)_-product in O(n_<sup>2.998</sup>) _expected time, and_<tbc>

• _Exact Triangle in O(n_<sup>2.998</sup>) _expected time._

Lower bounds are known for the above problems in some restricted models of computation: over the (min,+) semiring, straight-line programs need _n_<sup>3</sup> operations \[Ker70\] and path- comparison algorithms need \(\Omega(n^3)\) time \[KKP93\], and 3-linear decision trees for 3SUM need depth \(\Omega(n^2)\) \[Eri99, AC05\].

Our algorithms are not in these restricted models, since the known reductions remove the weights (by hashing, or by Fredman’s trick for real inputs), and we then count triangles in unweighted graphs using integer matrix multiplication.

We remark that there already was some indication that some of these models were too restricted, as for instance recent work \[KLM19\] showed that 6-linear decision trees of depth _O(n_log<sup>2</sup>_n_) suffice to solve 3SUM, and similar strong bounds are known for Exact Triangle. (See the paragraph on unaffected conjectures below for more on this.)

## Data structure version, and hinted Online Matrix-Vector.

Our algorithm for computing the wanted entries of a thin matrix product can also be converted into a data structure. We strengthen Theorem 1 as follows (Section 4):

**Theorem 3** (see Theorem 24 and Corollary 26)**.** _Let_ \(N\ge D^{18}\)_, and let_ \(X\in\mathbb{Z}^{N\times D}\), \(Y\in\mathbb{Z}^{D\times N}\) _have entries of absolute value N_<sup>_O_(1)</sup>_. The pair_ (_X,Y_) _can be preprocessed deterministically in O(N_<sup>2</sup>_/D_<sup>0.063</sup>) _time, polynomially less than the size of the product. After this, any single entry_ (_XY_)\[_I,J_\] _can be computed deterministically in O(D_<sup>0.437</sup>) _time, polynomially less than_ \(\sqrt{D}\)_. More generally, for every_ \(\varepsilon<0.1204\) _and every q\>_0 _there is a_ \(\gamma>0\) _such that, whenever_ \(D\le N^\varepsilon\)_, the pair can be preprocessed in_ \(O(N^2/D^\gamma)\) _time, after which any single entry can be computed in O(D<sup>q</sup>_) _time._

