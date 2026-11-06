3.2. _(Many Heavy Edges)_ The remaining case is that there are more than _n_<sub>1</sub>_n_<sub>2</sub>_/t_ heavy pairs. Let _H_ denote the set of heavy pairs (_i,k_), and let _A<sub>H</sub>_ be the matrix _A_ restricted to the entries in _H_ (where all other entries are set to \(\perp\)). Our strategy is to solve the entire instance (_A<sub>H</sub>,B,C_) in this step (by means of the reduction), and afterwards to remove all heavy entries from _A globally_. To this end, construct matrices \(A'\) and \(C'\) by<tbc>

\(A'[i,k]=A[i,k]-U[i,\ell]\text{if}(i,k)\in H,\)<br>
\(A'[i,k]=\perp\text{otherwise,}\)

and<tbc>

<tbc>\(C'[i,j]=C[i,j]-U[i,\ell].\)<tbc>

<tbc>By definition \((A',B,C')\) is a potential-adjusting restriction of (_A,B,C_) that retains all the exact triangles involving heavy edges. Moreover, we claim that each column in \(A'\) contains at most _rt_ distinct entries. Indeed, by construction \(A'\) coincides with \(A_\ell\) on the non-\(\perp\) (i.e., heavy) entries, and by definition each heavy entry appears at least _n_<sub>1</sub>/(_rt_) times in its column in \(A_\ell\). It follows that the instance \((A',B,C')\) is _rt_-slice-uniform. We now further reduce \((A',B,C')\) to _t_ instances that are _r_-slice-uniform (in the trivial way) and insert these instances into the collection I.

Afterwards, we remove all entries in _H globally_, i.e., we set \(A[i,k]\leftarrow\perp\) for all \((i,k)\in H\) for all future iterations.

Regarding the correctness, observe that each exact triangle (_i,k,j_) with \((i,k)\in H\) and \(S[i,j]=\ell\) is preserved in \((A',B,C')\). In fact, we have dealt with _all_ exact triangles with \((i,k)\in H\) (irrespective of _S_\[_i,j_\]), so we can indeed safely remove all pairs in _H_ from _A_ for the future iterations.

_Running Time:_ The construction of _H_ and of the _t_ equivalent instances takes linear time \(\tilde{O}((n_1n_2+n_1n_3+n_2n_3)t)\) per iteration. Moreover, with each execution of step 3.2 we increase the size of I by at most _t_. Notably, however, we execute this step 3.2 at most _t_ times in total, as after each iteration we replace \(|H|\ge n_1n_2/t\) non-\(\perp\) entries in _A_ by \(\perp\). It follows that the total running time is \(\tilde{O}((n_1n_2+n_1n_3+n_2n_3)t^2)\) and that \(|\mathcal{I}|\le t^2\) throughout.

This completes the proof. The correctness should be clear from the in-text explanations, and the total running time as analyzed before is \(\tilde{O}(n_1n_2n_3/t+(n_1n_2+n_1n_3+n_2n_3)rt^2)\) as claimed. (Here we only loosely bound the dependence on _t_.)

## 4.2 Reduction from Slice-Uniform to Uniform Exact Triangle

The second step is captured by the following lemma. Its proof can be fully attributed to \[4\]--no new ideas are necessary. We include a complete proof here only because we need the more general rectangular version, and to point out that the reduction is potential-adjusting. Readers familiar with \[4\] can safely skip this section.

**Lemma 4.5** (Reduction from Slice-Uniform to Uniform Exact Triangle \[4\])**.** _For any parameter_ \(t\ge 1\) _there is a potential-adjusting reduction from any d_-slice-uniform _Exact Triangle instance to O(t_<sup>41</sup>log<sup>2</sup>(_n_<sub>1</sub>_n_<sub>2</sub>_n_<sub>3</sub>)) _d_-uniform _instances. The reduction runs in deterministic time_ \(\tilde{O}(n_1n_2n_3/t+(n_1n_2+n_2n_3+n_1n_3)dt^{41})\)_. In particular:_

\(\mathrm{ExactTri}(n_1,n_2,n_3|d)\le\tilde{O}\big(t^{41}\cdot\mathrm{ExactTri}(n_1,n_2,n_3|D\le d)+\frac{n_1n_2n_3}{t}+(n_1n_2+n_2n_3+n_1n_3)dt^{41}\big).\)

The proof of Lemma 4.5 requires some setup. Recall that _r<sub>X+Y</sub>(z_) denotes the multiplicity of _z_ in the sumset _X+Y_ , i.e., the number of representations of the form _z=x+y_ for \((x,y)\in X\times Y\) .

