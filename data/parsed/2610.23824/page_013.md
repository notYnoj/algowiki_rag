## 5.2 Maximum Degrees

Next, we analyze the maximum degrees of the subgraphs _G_<sup>∗</sup>\[_J<sub>i</sub>_\]. Specifically, we show that the maximum degrees of _G_<sup>∗</sup>\[_J_<sub>1</sub>\]_,...,G_<sup>∗</sup>\[_J<sub>r</sub>_\] are _O(k_<sup>2</sup>log_k_log<sup>2</sup>_n_) with high probability.

### 5.2.1 Introducing the History Sequence

Here, for a given graph _G_<sup>∗</sup>=(_V_<sup>∗</sup>_,E_<sup>∗</sup>), we need to analyze all possibilities for the first _m_ vertices and the sampled independent sets. The outcome of Algorithm 1 in terms of coloring the last _n-m_ vertices, i.e., _J_<sub>1</sub>_,...,J<sub>r</sub>_, is determined by (_A_<sub>1</sub>_,I_<sub>1</sub>_,...,A<sub>r</sub>,I<sub>r</sub>_). To this end, we define _history sequences_ as follows.

**Definition 17** (History Sequence)**.** _Let_ \(t\ge 1\) _be an integer. Given a graph G_<sup>∗</sup>=(_V_<sup>∗</sup>_,E_<sup>∗</sup>)_, the "history sequence up to level t" is defined as a sequence_ H:=(_A_<sub>1</sub>_,I_<sub>1</sub>_,...,A<sub>t</sub>,I<sub>t</sub>). This is defined even when r\<t; in this case, A<sub>i</sub>=I<sub>i</sub>_=0 _when i\>r. The set of all possible history sequences up to level t is denoted as_

\(\mathbb{H}_t:=\{(A_1,I_1,\dots,A_t,I_t):A_1\subseteq V^*,I_i\in\mathcal{I}(G^*[A_i])(1\le i\le t),\)<br>
\(A_{i+1}=N_{A_i}(I_i)(1\le i<t)\}.\)

_It is easy to see that_ H_<sub>t</sub> indeed enumerates all history sequences with positive probability._

**Proposition 18.** _Let_ \(t\ge 1\) _be an integer. The probability that the history sequence up to level t equals_ \(\mathcal{H}=(A_1,I_1,\dots,A_t,I_t)\in\mathbb{H}_t\) _is given by_

\(p(\mathcal{H}):=2^{-n}\cdot\prod_{i=1}^t\frac{\lambda^{|I_i|}}{Z_\lambda(G^*[A_i])}.\)

_Proof._ The probability that _S=A_<sub>1</sub> is chosen is 2<sup>-_n_</sup> by Lemma 13. The probability that _I<sub>i</sub>_ is chosen from \(\mathsf{IS}_\lambda(G^*[A_i])\) is \(\frac{\lambda^{|I_i|}}{Z_\lambda(G^*[A_i])}\) by the definition of the hardcore model (note that this probability is 1 for _i\>r_). Thus, Proposition 18 holds. □

### 5.2.2 Degree Analysis with Double-Counting Method

To establish the maximum degree bound, we prove the following lemma using the double-counting method on history sequences.

**Lemma 19.** _Let_ \(\lambda>0\) _be the parameter of the hardcore model. Suppose G_<sup>∗</sup>=(_V_<sup>∗</sup>_,E_<sup>∗</sup>) _is a fixed k-colorable graph. For every vertex_ \(v\in V^*\) _and every integer_ \(t\ge 1\),

\(\mathbb{E}\left[\left\{1+\frac{\lambda}{(1+\lambda)^t}\right\}^{|N(v)\cap J_t|/k}\text{\textit{if}}v\in J_t\text{\textit{, otherwise}}0\right]\le 1.\)

_Proof._ Let \(\mathbb{H}'\subseteq\mathbb{H}_t\) be the set of all history sequences up to level _t_ in which the vertex _v_ is put into _J<sub>t</sub>_. For each \(\mathcal{H}=(A_1,I_1,\dots,A_t,I_t)\in\mathbb{H}'\), define the following:

• Let \(X(\mathcal{H})\subseteq V^*\) be the set of vertices adjacent to _v_ in _G_<sup>∗</sup>\[_J<sub>t</sub>_\].<tbc>

• Let \(Y(\mathcal{H})\subseteq V^*\) be an arbitrary maximum independent set of _G_<sup>∗</sup>\[_X_(H)\].<tbc>

