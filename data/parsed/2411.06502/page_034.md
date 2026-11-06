For Output (2), we obtain the desired similarity value by the distance from \((1,x')\) to \((y,n'+1)\).

For Output (3), we obtain the desired similarity value via reverse symmetry. In particular, we can begin by reversing **F** and \(\mathbf{F}'\) and consider Output (2) in the reversed instance.

## 4.6.1 Handling the Recursive Case

**Lemma 4.11.** _Suppose we are given a_ \((\mathbf{w},\mathbf{F},\mathbf{F}')\)_-LRBBD instance of size_ \((n,n')\) _such that_ **F**=**F**<sub>1</sub>+**F**<sub>2</sub>.

_Then, given the outputs of the_ \((\mathbf{w},\mathbf{F}_1,\mathbf{F}')\)_-LRBBD instance and the_ \((\mathbf{w},\mathbf{F}_2,\mathbf{F}')\)_-LRBBD instance, we can solve the_ \((\mathbf{w},\mathbf{F},\mathbf{F}')\)_-LRBBD instance in time_ \(\mathcal{O}(\mathsf{T}_\text{\textit{MUL}}(n',n',n))\).

_Furthermore, if the LRBBD instance has diameter_ \(\mathcal{O}(n')\)_, we can solve the_ \((\mathbf{w},\mathbf{F},\mathbf{F}')\)_-LRBBD instance in time_ \(\mathcal{O}(\mathsf{T}_\text{\textit{MonMUL}}(n',n',n,n'))\).

**Proof.** We proceed with a similar argument as in Lemma 4.6, using the same notation as before. Let _n_<sub>1</sub>=|**F**<sub>1</sub>|, _n_<sub>2</sub>=|**F**<sub>2</sub>|, _n_=|**F**|=_n_<sub>1</sub>+_n_<sub>2</sub>, and set _i_<sub>2</sub>=_n_<sub>1</sub>+1. Consider the pre-order traversal _v_<sub>1</sub>_,...,v<sub>n</sub>_ of **F**, and observe that _v_<sub>1</sub>_,...,v_<sub>_n_<sub>1</sub></sub> corresponds to the pre-order of **F**<sub>1</sub> and that _v_<sub>_i_<sub>2</sub></sub>_,...,v<sub>n</sub>_ corresponds to the pre-order traversal of **F**<sub>2</sub>. Further, consider the alignment graph \(\bar{\mathbf{G}}\) w.r.t. \((\mathbf{w},\mathbf{F},\mathbf{F}')\). The alignment graph \(\bar{\mathbf{G}}_1\) w.r.t. \((\mathbf{w},\mathbf{F}_1,\mathbf{F}')\) corresponds to \(\bar{\mathbf{G}}[1..i_2][1..(n'+1)]\), and the alignment graph \(\bar{\mathbf{G}}_2\) w.r.t. \((\mathbf{w},\mathbf{F}_2,\mathbf{F}')\) corresponds to \(\bar{\mathbf{G}}[i_2..(n+1)][1..(n'+1)]\).

We now show how to compute the outputs of the \((\mathbf{w},\mathbf{F},\mathbf{F}')\)-LRBBD instance. As before, we decompose \(\mathsf{B}^\top(1,1,n+1,n'+1)\) into \(I_1^\top\) and \(I_2^\top\). See Figure 9 for a visualization of the alignment graph and the computed distances.

We proceed by case analysis on \(\bar{v}\).

For \(\bar{v}\in I_1^\top\), we obtain the outputs \(\mathsf{dist}_\bar{\mathbf{G}}(\bar{u},\bar{v})\) using the output of the \((\mathbf{w},\mathbf{F}_1,\mathbf{F}')\)-LRBBD instance.

For \(\bar{v}\in I_2^\top\), notice that for every \(i\in[1..i_2]\) we have \(\pi_\mathbf{F}(i)\le i_2\) as **F**=**F**<sub>1</sub>+**F**<sub>2</sub>. As a consequence, a path from \(\bar{u}\) to \(\bar{v}\) must pass through a node contained in the set \(i_2\times[1..(n'+1)]\), and we can write

\(\mathsf{dist}_\bar{\mathbf{G}}(\bar{u},\bar{v})=max_{\bar{w}\in i_2\times[1..(n^\prime+1)]}\left\{\mathsf{dist}_\bar{\mathbf{G}}(\bar{u},\bar{w})+\mathsf{dist}_\bar{\mathbf{G}}(\bar{w},\bar{v})\right\}.\)

As before, the two summands that appear in the latter maximization are a subset of the output of the \((\mathbf{w},\mathbf{F}_1,\mathbf{F}')\)-LRBBD instance and of the \((\mathbf{w},\mathbf{F}_2,\mathbf{F}')\)-LRBBD instance. Moreover, note that we may rewrite the computation of \(\mathsf{dist}_\bar{\mathbf{G}}(\bar{u},\bar{v})\) for all such \(\bar{u}\) and \(\bar{v}\) as a max-plus product _A=B⋆C_, where _B_ is a matrix of size \((n'+1)\times(n'+1)\) and _C_ is a matrix of size \((n'+1)\times(n_2+n'+1)\) Thus, we spend at most \(\mathcal{O}(\mathsf{T}_\text{MUL}(n',n',n))\) time in the computation of these distances.

As argued in Lemma 4.6, the matrix _C_ is a column-monotone matrix with entries in both matrices bounded by \(\mathcal{O}(n')\) if the diameter is bounded by \(O(n')\), so that we can compute the required distances in time \(\mathcal{O}(\mathsf{T}_\text{MonMUL}(n',n',n,n'))\).

