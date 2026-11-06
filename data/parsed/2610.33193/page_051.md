Due to the linearity of expectation, the total expected heat released during compaction is exactly

\(\sum_{k\le n}\mathrm{Pr}[|b|_1=k]\mathrm{log}\frac{n!}{k!(n-k)!}.\) (12)

Since the drop in entropy (11) and the expected heat release (12) are identical, we can conclude that EP<sub>C</sub>=0.

**Remark 6.2.** _The analysis in Theorem 6.1 has a natural extension to compaction on k-bit keys by instead applying Lemma 3.1 to pick heat functions where, for every_ \(d\in\{0,1\}^k\)_, the chosen distribution over inputs has_ \(\mathrm{Pr}[b_i=d]=|b_{\le i}|_d/i\) _where_ |_x|<sub>d</sub> denotes the count of key d in x._

## 6.2 A clean sorting circuit with zero entropy production

Our method of zero circuit entropy production erasure in Section 6.1 can be extended to give a circuit with zero entropy production for sorting. As we are now doing general sorting, we can always assume that payloads are just low order bits of the keys and therefore ignore them altogether. Thus the task is now, given an input _x=x_<sub>1</sub>_,...,x<sub>n</sub>_ with each \(x_i\in\{0,1\}^m\), output Sort(_x_)=_y_<sub>1</sub>_,...,y<sub>n</sub>_ where the _y<sub>i</sub>_ are a permutation of the _x<sub>i</sub>_ such that, for every _i_, \(y_i\le y_{i+1}\). For simplicity, we will assume that our larger keys can be compared with a single comparator gate, which is implemented using multiple constant-arity gates.

**Theorem 6.3.** _Let_ D _be any exchangeable distribution over_ ({0,1}_<sup>m</sup>)<sup>n</sup>. There exists a polynomial sized (in terms of n and m) circuit that sorts n inputs that are each m bits with zero circuit entropy production._

_Proof._ We will use the same circuit as in Section 6.1 to map input _x_ to the state (_x,_Sort(_x_)) using only logically reversible gates. Now, the task is to erase the copy of _x_ with zero circuit entropy production. For \(b=b_1,\dots,b_\ell\), and \(b_i,v\in\{0,1\}^k\), we use |_b|<sub>v</sub>_ to denote the number of _b<sub>i</sub>_ such that _b<sub>i</sub>=v_.

We will erase the highest order bit of every _x<sub>i</sub>_ before moving on to the next highest order bit and so on. In other words, the order in which we erase bits will be \(x_1^1,x_2^1,\dots,x_n^1,x_1^2,x_2^2,\dots,x_n^m\). Let \(x_i^j\) denote the _j_’th bit of _x<sub>i</sub>_. Analogous to before, we now use \(x_{\le i}^{\ge j}\) to denote the suffixes starting on the _j_’th bit of \(x_{i^\prime}\) for all \(i'\le i\). When erasing \(x_i^j\), we will use the optimal heat function, per Lemma 3.1, for the distribution with:

\(\mathrm{Pr}[x_i^j=1]=\frac{\left|x_{\le i}^{\ge j}\right|_{1\cdot x_i^{\ge j+1}}}{\left|x_{\le i}^{\ge j+1}\right|_{x_i^{\ge j+1}}},\)

where \(1\cdot x_i^{\ge j}\) denotes the suffix of _x<sub>i</sub>_ beginning with index _j_ with a 1 appended to the front. In other words, the probability of a 1 is exactly the probability one would get a 1 by sampling uniformly at random the _j_’th bit of any \(x_{i^\prime}\) with \(i'\le i\) that shares its suffix after index _j_ with _x<sub>i</sub>_. While it would be unfeasible to track these counts for every possible suffix, this probability can be computed on the fly for each erasure by paying a polynomial cost in the depth of the circuit and the number of gates. This follows from the fact that these counts can be computed (and uncomputed) in a<tbc>

