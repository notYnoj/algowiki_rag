## 4.4 Patching together subproblems

**Lemma 4.6.** _Suppose we are given a_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-BBD instance of size m such that_ **F**=**F**<sub>1</sub>+**F**<sub>2</sub>.

_Then, given the outputs of the_ \((\mathrm{w},\mathbf{F}_1,\mathbf{F}')\)_-BBD instance and the_ \((\mathrm{w},\mathbf{F}_2,\mathbf{F}')\)_-BBD instance, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-BBD instance in time_ O(T<sub>_MUL_</sub>(_m_)).

_Furthermore, if the BBD instance has diameter_ D_, we can solve the_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-BBD instance in time_ O(T<sub>_MonMUL_</sub>(_m,m,m,_D)).

**Proof.** Let _n_<sub>1</sub>=|**F**<sub>1</sub>|, _n_<sub>2</sub>=|**F**<sub>2</sub>|, _n_=|**F**|=_n_<sub>1</sub>+_n_<sub>2</sub>, and set _i_<sub>2</sub>=_n_<sub>1</sub>+1. Consider the pre-order traversal _v_<sub>1</sub>_,...,v<sub>n</sub>_ of **F**, and observe that _v_<sub>1</sub>_,...,v_<sub>_n_<sub>1</sub></sub> corresponds to the pre-order of **F**<sub>1</sub> and that _v_<sub>_i_<sub>2</sub></sub>_,...,v<sub>n</sub>_ corresponds to the pre-order traversal of **F**<sub>2</sub>. Further, consider the alignment graph \(\tilde{\mathbf{G}}\) w.r.t. \((\mathrm{w},\mathbf{F},\mathbf{F}')\). The alignment graph \(\tilde{\mathbf{G}}_1\) w.r.t. \((\mathrm{w},\mathbf{F}_1,\mathbf{F}')\) corresponds to \(\tilde{\mathbf{G}}[1..i_2][1..(n'+1)]\), and the alignment graph \(\tilde{\mathbf{G}}_2\) w.r.t. \((\mathrm{w},\mathbf{F}_2,\mathbf{F}')\) corresponds to \(\tilde{\mathbf{G}}[i_2..(n+1)][1..(n'+1)]\).

We rewrite \(\mathrm{B}^\perp(1,1,n+1,n'+1)=I_1^\perp U_2^\perp\), where \(I_1^\perp=\mathrm{B}^\perp(1,1,i_2-1,n'+1)\) and \(I_2^\perp=[i_2..(n+1)]\times 1\). Similarly, we rewrite \(\mathrm{B}^\top(1,1,n+1,n'+1)=I_1^\top U_2^\top\), where \(I_1^\top=[1..i_2]\times(n'+1)\) and \(I_2^\top=\mathrm{B}^\top(i_2,1,n+1,n'+1)\). See Figure 7 for a visualization of the newly defined index sets.

We split up the indices for the output of the \((\mathrm{w},\mathbf{F},\mathbf{F}')\)-BBD instance as follows.

\(\{(\bar{u},\bar{v}):\bar{u}\in\mathrm{B}^\perp(1,1,n+1,n'+1),\bar{v}\in\mathrm{B}^\top(1,1,n+1,n'+1)\}=\)<br>
\(\{(\bar{u},\bar{v}):\bar{u}\in I_1^\perp,\bar{v}\in I_1^\top\}\) (3)

\(U\{(\bar{u},\bar{v}):\bar{u}\in I_1^\perp,\bar{v}\in I_2^\top\}\) (4)

\(U\{(\bar{u},\bar{v}):\bar{u}\in I_2^\perp,\bar{v}\in I_1^\top\}\) (5)

\(U\{(\bar{u},\bar{v}):\bar{u}\in I_2^\perp,\bar{v}\in I_2^\top\}.\) (6)

We show separately how we compute the distances for the index sets (3), (4), (5), and (6).

For (3), we can get \(\mathrm{dist}_\tilde{\mathbf{G}}(\bar{u},\bar{v})\) using the output of the \((\mathrm{w},\mathbf{F}_1,\mathbf{F}')\)-BBD instance.

For (4), we use that for every \(i\in[1..i_2]\) we have \(\pi_\mathbf{F}(i)\le i_2\) as **F**=**F**<sub>1</sub>+**F**<sub>2</sub>. As a consequence, a path goes from \(\bar{u}\) to \(\bar{v}\) must pass through a node contained in the set \(i_2\times[1..(n'+1)]\), and we can write

\(\mathrm{dist}_\tilde{\mathbf{G}}(\bar{u},\bar{v})=\mathrm{max}_{\bar{w}\in i_2\times[1..(n^\prime+1)]}\left\{\mathrm{dist}_\tilde{\mathbf{G}}(\bar{u},\bar{w})+\mathrm{dist}_\tilde{\mathbf{G}}(\bar{w},\bar{v})\right\}.\)

I 1
I 2
I 1
I 2
I 1
I 2
I 1
I 2

**Figure 7** A BBD instance can be thought as a rectangle where we need to compute distances from the lower left border to the upper right border. In Lemma 4.6 we ‘cut’ the rectangle between **F**<sub>1</sub> and **F**<sub>2</sub>, and given the answer for the instances corresponding to the two resulting rectangle halves, we show how to patch them together for the full rectangle. In order to do so, we split the lower left border \(\mathrm{B}^\perp(1,1,n+1,n'+1)\) into \(I_1^\perp\) and \(I_2^\perp\), and the upper right border \(\mathrm{B}^\top(1,1,n+1,n'+1)\) into \(I_1^\top\) and \(I_2^\top\).

