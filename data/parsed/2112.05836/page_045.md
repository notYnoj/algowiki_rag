## 8 Shift Distance: Lower Bound & Upper Bound

In this section we will explore a problem where we can get tight upper and lower bounds, but there is no efficiency to be gained by having compressible strings in your input. The problem is _k_-Shift Distance. When _k_=2 this problem is (basically) equivalent to the Hamming distance substring problem mentioned in \[ABBK17\]. This problem is a natural extension of pattern matching. This problem asks, given a set of _k_ strings, how can we best line them up to maximize the number of matched characters? So, the alignment that minimizes the Hamming Distance between all the strings. This problem was studied in the average-case for _k_=2 by \[AIKH13\]. They called the problem "shift finding". We give the natural generalization of this problem to _k_ strings and present upper bounds and lower bounds. We also present an approximation algorithm. We present these results in part because they give an example of a _k_-string comparison problem where there is no efficiency to be gained from having a compressible input.

The core of this section is showing tight upper and lower bounds for this problem of finding the ideal alignment of strings that minimizes Hamming distance. We show that in cyclic shift there is no advantage to be gained from compression. The upper and lower bounds are tight and unchanged even with compression. We are also able to use FFT to get a fast algorithm for the problem of finding the best alignment with respect to Hamming distance.

We will now re-state the definition of _k_-Shift Distance, with more commentary.

**Reminder of Definition** _k_**-Shift Distance (k-SD).** _We are given k strings as input: X_<sub>1</sub>_,...,X<sub>k</sub>. These strings have characters from the alphabet_ \(\Sigma\)_. Each string has length N and compresses via SLP to a length of n. For convenience of notation let X<sub>j</sub>_\[_i_\] _when_ \(i\notin[0,n-1]\) _refer to_ \(X_j[i']\) _where_ \(i'\in[0,n-1]\) _and_ \(i'\equiv imodn\) _(so we let indices "wrap around")._

_We must return the best alignment of the k strings. The alignment where in the maximum num ber of locations all strings have the same symbol. We will give a precise definition below. Let_ \(\hat{\Delta}=max(\Delta_1,\dots,\Delta_{k-1})\)_. And let_ \(\unknown\cdot\unknown\) _be an operator that turns True to a_ 1 _and False to a_ 0.

\(k\text{\textit{-}}SD(X_1,\dots,X_k)=max_{\Delta_1,\dots,\Delta_{k-1}\in[0,N-1]}\sum_{i=1}^N\left\unknown X_1[i+\Delta_1]=X_2[i+\Delta_2]=\cdots=X_{k-1}[i+\Delta_{k-1}]=X_k[i]\right\unknown\)

_So, we want the offsets such that the maximum number of characters are all shared between all k strings._

_We will also define the term of the offset score. Given strings X_<sub>1</sub>_,...,X<sub>k</sub> and a particular set of deltas_ \(\Delta_1,\dots,\Delta_{k-1}\) _we will call the value:_

\(\sum_{i=1}^N\left[X_1[i+\Delta_1]=X_2[i+\Delta_2]=\cdots=X_{k-1}[i+\Delta_{k-1}]=X_k[i]\right]\)

_the offset score of the strings X_<sub>1</sub>_,...,X<sub>k</sub> and the deltas_ \(\Delta_1,\dots,\Delta_{k-1}\).

### 8.1 The Algorithm

We will use FFT to get a fast algorithm here. We start by showing how to do this when _k_=2.

**Lemma 8.1** (From \[ABBK17\])**.** _There is an_ \(O\left(|\Sigma|Nlg\left(N|\Sigma|\right)\right)\) _algorithm for 2-SD with an alphabet_ \(\Sigma\) _(k-SD when k_=2_)._

We can then generalize to _k_ by making calls to 2-SD.

**Theorem 8.2.** _There is an_ \(O(|\Sigma|N^{k-1}lg(|\Sigma|N))\) _algorithm for k-Shift Distance._

_Proof._ Let our _k_ input strings be: _X_<sub>1</sub>_,...,X<sub>k</sub>,_ each of length _N._

We are going to reduce k-SD with alphabet \(\Sigma\) and strings of length _N_ to 2-SD with alphabet \(\Sigma\cup\{@\}\) and strings of length _N_. First, we will try all _N_<sup>_k_-2</sup> possible offsets \(\Delta_2,\dots,\Delta_{k-1}\). Now, for each of these we will Create a new string _Y_ which will be a "merge" of the strings _X_<sub>2</sub>_,...,X<sub>k</sub>_. The string _Y_ will have length _N_. The _i<sup>th</sup>_ bit of _Y_ is:

\(Y[i]=\left\{\begin{array}{ c c }
X_k[i] & \text{if}[X_2[i+\Delta_2]=\cdots=X_{k-1}[i+\Delta_{k-1}]=X_k[i]] \\
@ & \text{else}
\end{array}\right..\)

If all the strings agree given our choice of offset we set it to the agreed character. Otherwise, we use the new special character @ which does not appear in _X_<sub>1</sub> (as @ is not in \(\Sigma\)). Note that we can produce _Y_ in _kN_ time, so over all offsets we take _N_<sup>_k_-1</sup> time to produce the inputs _X_<sub>1</sub>_,Y_ .

