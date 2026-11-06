<tbc>as a solution to \(K|_{V\cup V^\prime}\), where

\(z''[i]:=z\big[z'[i]\big],\)<br>
\(\mathbf{x}''[i]:=\mathbf{x}'[i]+\mathbf{x}\big[z'[i]\big].\)

Note that \(\circ\) is associative.

Now we are ready to state the composition lemma for HintedKnapsackExtend<sup>+</sup>.

**Lemma 4.5** (Composition lemma for HintedKnapsackExtend<sup>+</sup>)**.** _Let_ \(V,V'\subseteq U,V\cap V'=\varnothing\)_. If Y<sub>V</sub> correctly solves K|<sub>V</sub>, and_ \(Y_{V^\prime}\) _correctly solves_ \(K^{(V\leftarrow Y_V)}|_{V^\prime}\)_, then_ \(Y_{V^\prime}\circ Y_V\) _correctly solves_ \(K|_{V\cup V^\prime}\).

_Proof._ Recall \(K=\big(U,\{Q_w\}_{w\in U},S[],q[]\big)\). Denote the solutions \(Y_V=(\mathbf{x}[],z[],r[])\), \(Y_{V^\prime}=(\mathbf{x}'[],z'[],r'[])\), and \(Y_{V^\prime}\circ Y_V:=(\mathbf{x}''[],z''[],r''[])\).

Suppose for contradiction that for some _i_, \(\mathbf{x}''[i]\) is incorrect for the instance \(K|_{V\cup V^\prime}\). By definition of HintedKnapsackExtend<sup>+</sup>, this means that all maximizers \((\bar{\mathbf{x}},\bar{z})\) (where \(\bar{\mathbf{x}}\in\mathbb{Z}_{\ge 0}^{V\cup V^\prime}\)) of the objective value<tbc>

\(\bar{r}=q[\bar{z}]+\sum_{w\in V\cup V^\prime} Q_w(\bar{x}_w)\)

<tbc>(subject to \(\bar{z}+\sum_{w\in V\cup V^\prime} w\cdot\bar{x}_w=i\)) should satisfy the support containment condition,<tbc>

\(\text{supp}(\bar{\mathbf{x}})\subseteq S[\bar{z}].\)

<tbc>Take any such maximizer \((\bar{\mathbf{x}},\bar{z})\), and write \(\bar{\mathbf{x}}=\bar{\mathbf{x}}_V+\bar{\mathbf{x}}_{V^\prime}\) such that \(\text{supp}(\bar{\mathbf{x}}_V)\subseteq V\) and \(\text{supp}(\bar{\mathbf{x}}_{V^\prime})\subseteq V'\). Let<tbc>

\(i_V:=\bar{z}+\sum_{w\in V}w\cdot\bar{x}_w\)

<tbc>and

\(r_V:=q[\bar{z}]+\sum_{w\in V}Q_w(\bar{x}_w).\)

Note that in instance _K|<sub>V</sub>_, \((\bar{\mathbf{x}}_V,\bar{z},r_V)\) should be a valid solution for _i<sub>V</sub>_ with objective value _r<sub>V</sub>_. We now compare it with _r\[i<sub>V</sub>_\] from the correct solution _Y<sub>V</sub>_ to the instance _K|<sub>V</sub>_, and we claim that _r_\[_i<sub>V</sub>_\]=_r<sub>V</sub>_ must hold. Otherwise, by the definition of the HintedKnapsackExtend<sup>+</sup> instance _K|<sub>V</sub>_, there can only be two possibilities:

• Case 1: \((\bar{\mathbf{x}}_V,\bar{z},r_V)\) is not a maximizer solution for index _i<sub>V</sub>_ in _K|<sub>V</sub>_.<tbc>

<tbc>This means there is some solution (**_x_**_<sup>⋆</sup>,z<sup>⋆</sup>,r<sup>⋆</sup>_) for index _i<sub>V</sub>_ in _K|<sub>V</sub>_ that achieves a higher objective _r<sup>⋆</sup>\>r<sub>V</sub>_. We will use an exchange argument to derive contradiction: Consider the solution \((\mathbf{x}^\star+\bar{\mathbf{x}}_{V^\prime},z^\star)\) to the instance \(K|_{V\cup V^\prime}\). It has the same total weight \(z^\star+\sum_{w\in V}w\cdot x_w^\star+\sum_{w\in V^\prime} w\cdot\bar{x}_w=i_V+\sum_{w\in V^\prime} w\cdot\bar{x}_w=i\), but has a higher objective value \(r^\star+\sum_{w\in V^\prime} Q_w(\bar{x}_w)>r_V+\sum_{w\in V^\prime} Q_w(\bar{x}_w)=\bar{r}\), contradicting the assumption that \((\bar{\mathbf{x}},\bar{z})\) is a maximizer for _i_ in instance \(K|_{V\cup V^\prime}\).<tbc>

• Case 2: \((\bar{\mathbf{x}}_V,\bar{z},r_V)\) is a maximizer solution for index _i<sub>V</sub>_ in _K|<sub>V</sub>_, but there is another maximizer solution (**_x_**_<sup>⋆</sup>,z<sup>⋆</sup>,r<sub>V</sub>_) for index _i<sub>V</sub>_ in _K|<sub>V</sub>_ that does not satisfy the support containment condition \(\text{supp}(\mathbf{x}^\star)\subseteq S[z^\star]\) for instance _K|<sub>V</sub>_.<tbc>

<tbc>In this case, again consider the solution \((\mathbf{x}^\star+\bar{\mathbf{x}}_{V^\prime},z^\star)\) to the instance \(K|_{V\cup V^\prime}\). This time it has the same objective value \(\bar{r}\), so it is a maximizer for index _i_ in the instance \(K|_{V\cup V^\prime}\).<tbc>

