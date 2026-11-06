## 7.3 The sparse selection algorithm

We now give the actual selection algorithm based on WSHForestElim. The idea is to iteratively call WSHForestElim with an appropriate value of _m_, each time removing the returned nodes \(D'\) (which are a constant fraction of the _k_ smallest nodes). We find the appropriate value of _m_ by starting with _m_=2 and doubling _m_ until WSHForestElim no longer returns `FAIL`, or _m_ reaches a constant fraction of _k_, at which point we may call WSHselect.

We call our algorithm WSHSparseForestSelect, with "sparse" referring to the forest having only few relevant high-degree nodes if \(OPT\checkmark k\). See algorithm 3 for pseudocode. WSHForestSelect in the code refers to the extension of WSHTreeSelect to forests. We additionally record the largest value for _m_ encountered during the various calls to WSHForestElim as _m_<sup>∗</sup>, and stop once _m_<sup>∗</sup> is linear in _k_. This ensures the number of iterations is no more than O(log(_k/m_<sup>∗</sup>)).

**Algorithm 3** Selection in forests by repeated elimination.

procedure WSHSparseForestSelect(F,k)<br>
   loop<br>
   \(m^*\leftarrow 2\)<br>
   for m=2,4,8,16,... do<br>
   if \(m^*>\frac{1}{2}\delta k\) then<br>
**return**<br>
WSH<br>
Forest<br>
Select<br>
(<br>
_F,k_<br>
)<br>
   else<br>
   \(D'\leftarrow WSHForestElim(F,k,m)\)<br>
   if \(D'\neq\text{\texttt{FAIL}}\) then<br>
   \(F\leftarrow F-D'\)<br>
   \(k\leftarrow k-|D'|\)<br>
   \(m^*\leftarrow max\{m^*,m\}\)<br>
   break from the for loop

In the following, fix some input _F,k_. Let _t_ be the number of outer loop iterations. For each \(i\in[t]\), let _F<sub>i</sub>_ and _k<sub>i</sub>_ be the values for _F_ and _k_ at the start of the _i_-th iteration, and let _m<sub>i</sub>_ be the final value of _m_ in the _i_-th iteration. Observe that at the end we have \(m^*=max_{i\in[t]}m_i\).

For \(i\in[t-1]\), let \(D'_i\) be the set of nodes returned by the final WSHForestElim in the _i_-th iteration, and let \(\tilde{D}'_i=D'_1\cup D'_2\cup\cdots\cup D'_{i-1}\). Observe that \(F_i=F-\tilde{D}'_i\) and \(k_i=k-|\tilde{D}'_i|\).

Proving correctness of WSHSparseForestSelect is now straight-forward. In the _i_-th iteration, we remove a set of nodes \(D'_i\) from _F<sub>i</sub>_ that all have rank strictly less than _k<sub>i</sub>_. Clearly, the problem reduces to finding the nodes of rank \(k_i-|D'_i|\) in _F_<sub>_i_+1</sub>. The final iteration returns the correct result via a call to WSHForestSelect, so by induction WSHSparseForestSelect is correct, too.

We now bound the number of comparisons, starting with a single outer loop iteration.

**Lemma 42.** _For each_ \(i\in[t-1]\)_, the i-th outer loop iteration of_ WSHSparseForestSelect _takes_ O(_m<sub>i</sub>_) _comparisons and_ O(_k<sub>i</sub>_log_m<sub>i</sub>_) _time._

