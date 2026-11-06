<tbc>**Lemma 4.8.** _k_-ED-Alg _outputs_ \(\tilde{D}\) _such that_<tbc>

\(\delta_E(X_1,X_2,\dots X_k)\le\tilde{D}\le(1+19\epsilon k)\delta_E(X_1,X_2,\dots X_k).\)

<tbc>_Proof._ Consider any window-respecting alignment for which _f(W_<sub>1_,j_</sub>)=(_W_<sub>1_,j_</sub>_,W_<sub>2_,j_</sub>_,...,W<sub>k,j</sub>_). If \(\delta_E(W_{1,j},W_{2,j},\dots,W_{k,j})>0\), let _d<sub>j</sub>_ be the smallest value in D such that \(d_j\ge\delta_E(W_{1,j},W_{2,j},\dots,W_{k,j})+\epsilon kd_j\). By Lemma 4.6, for every _j_ and if \(\epsilon\) is sufficiently small, by triangle inequality we have:

\(\delta_E(W_{1,j},W_{2,j},\dots,W_{k,j})\le[\tilde{\delta}_E(\text{\texttt{shift}}_{d_j}(W_{1,j}),\text{\texttt{shift}}_{d_j}(W_{2,j}),\dots,\text{\texttt{shift}}_{d_j}(W_{k,j}))]+\epsilon kd_j\)<br>
\(\le\delta_E(W_{1,j},W_{2,j},\dots,W_{k,j})+2\epsilon kd_j\)<br>
\(\le(1+5\epsilon k)\delta_E(W_{1,j},W_{2,j},\dots,W_{k,j}).\)

The first inequality implies that any path through the DP table for _c_ has total cost at least that of some window-respecting alignment, which by Lemma 4.5 gives the first inequality in the lemma statement. The second inequality implies that for the best window-respecting alignment, there is a path through the DP table such that the cost of the path through the DP table is no more than \((1+5\epsilon)\) times the cost of the window-respecting alignment. Furthermore, this path only goes through points in the DP table such that \(|x_i-x_1|\le 4D\) for all _i_, i.e., is considered by _k_-ED-Alg. Combined with Lemma 4.5 this gives the second inequality in the lemma statement if \(\epsilon\) is sufficiently small.

We can now compute a \((1+\epsilon)\)-approximation of the edit distance by rescaling \(\epsilon\) appropriately and running _k_-ED-Alg for all _D_ that are powers of 2, giving Theorem 4.2. One could also extract the alignment achieving this edit distance by using standard techniques to retrieve a path through the DP table, and applying these same techniques to the DP tables used in invocations of Lemma 4.7 as a subroutine; we omit the details here.

## 5 FPTAS For Center Distance

The center distance problem is defined as follows:

**Definition 5.1.** The center (edit) distance \(\delta_{CE}(X_1,\dots,X_k)\) of _k_ strings _X_<sub>1</sub>_,...,X<sub>k</sub>_ is defined as \(\delta_{CE}(X_1,\dots,X_k)=min_{X^*}max_i\delta_E(X_i,X^*)\). That is, it is the smallest value _D_ such that by making at most _D_ edits to each _X<sub>i</sub>_, we can transform them all into the same string _X_<sup>∗</sup>.

In this section we prove Theorem 5.2:

**Theorem 5.2.** _Given k=O_(1) _straight-line programs_ **G**_<sub>X<sub>i</sub></sub> of total size n generating strings X<sub>i</sub> of total length N\>_0 _and a parameter_ \(\epsilon\in(0,1]\)_, an integer between_ \(\delta_{CE}(X_1,\dots,X_k)\) _and_ \((1+\epsilon)\delta_{CE}(X_1,\dots,X_k)\) _can be computed in_ \(O\left(\epsilon^{-O(k)}n^{k/2}N^{k/2+o(1)}\right)\) _time._

Prior to our work, the best known algorithm result for the center distance problem was the exact _O(N_<sup>2_k_</sup>)-time algorithm of \[NR05\]. Our framework for the algorithm is similar to the framework from the previous section which uses window-respecting alignments.

Our algorithm will actually solve a more general problem of computing an approximation of a set of values which we call the _edit tuples_. We again assume \(\delta_{CE}(X_1,\dots,X_k)\) lies between _D_ and 2_D_ for some known (power of 2) _D_.

**Definition 5.3.** Given strings _X_<sub>1</sub>_,X_<sub>2</sub>_,...,X<sub>k</sub>_, an edit tuple of these strings is a vector \(v\in\mathbb{Z}_{\ge 0}^k\) such that there exists _X_<sup>∗</sup> for which \(\delta_E(X_i,X^*)\le v_i\) for all _i_. We denote the set of all edit tuples in {0,1_,...,D}<sup>k</sup>_ of _X_<sub>1</sub>_,X_<sub>2</sub>_,...X<sub>n</sub>_ by `tup`_<sub>D</sub>(X_<sub>1</sub>_,X_<sub>2</sub>_,...X<sub>k</sub>_).

We say that _S_ is a \(\Delta\)-approximation of `tup`_<sub>D</sub>(X_<sub>1</sub>_,X_<sub>2</sub>_,...X<sub>k</sub>_) if for each \(v\in S\), there is a vector \(v'\in\text{\texttt{tup}}_D(X_1,X_2,\dots X_k)\) such that \(v'\le v\), and for each \(v\in\text{\texttt{tup}}_D(X_1,X_2,\dots X_k)\), there is a vector \(v'\in S\) such that \(v'\le v+\Delta\cdot\mathbf{1}\). Here \(a\le b\) denotes \(a_i\le b_i\) for all _i_ and **1** denotes the all ones vector.

We will use again use the window-respecting alignment framework. However, our algorithm is now recursive, and thus we need to be careful about choosing the windows to operate with in each level of recursion. Let \(\ell=O(loglogN)\) be a parameter and \(\tau_0=N>\tau_1>\cdots>\tau_\ell=N^{1/loglogN}\) be a sequence such that for all \(i<\ell\), \(\tau_m/\tau_{m-1}=\Theta(N^{1/loglogN})\) and is integer (that is, these ratios are not<tbc>

