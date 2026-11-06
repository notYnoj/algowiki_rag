where

\((S''[i],q''[i]):=\left\{\begin{array}{ c c }
(S[i],q[i]) & q[i]>q'[i], \\
(S'[i],q'[i]) & q[i]<q'[i], \\
(S[i]\cap S'[i],q[i]) & q[i]=q'[i],
\end{array}\right.\)

and denote this instance by \(max(K,K')\). We naturally extend this definition to the entry-wise maximum of possibly more than two instances.

We also define the entry-wise maximum of two solutions \(Y=(x[],z[],r[]),Y'=(x'[],z'[],r'[])\), by \(max(Y,Y')=(x''[],z''[],r''[])\), where

\((x''[i],z''[i]):=\left\{\begin{array}{ c c }
(x[i],z[i]) & r[i]>r'[i], \\
(x'[i],z'[i]) & \text{otherwise},
\end{array}\right.\)

and objective \(r''[i]\) can be uniquely determined from \((x''[i],z''[i])\). Note that \(r''[i]\ge max(r[i],r'[i])\) obviously holds.

Naturally, we have the following lemma for HintedKnapsackExtend<sup>+</sup>.

**Lemma 4.7** (Entry-wise maximum lemma)**.** _If Y correctly solves K, and_ \(Y'\) _correctly solves_ \(K'\)_, then_ \(max(Y,Y')\) _correctly solves_ \(max(K,K')\).

_Proof._ Denote \(K=\left(U,\{Q_w\}_{w\in U},S[],q[]\right)\), \(K'=\left(U,\{Q_w\}_{w\in U},S'[],q'[]\right)\), \(Y=(x[],z[],r[]),Y'=(x'[],z'[],r'[])\). Let \(max(K,K')=\left(U,\{Q_w\}_{w\in U},S''[],q''[]\right)\) and \(max(Y,Y')=(x''[],z''[],r''[])\).

Suppose for contradiction that for some _i_, \(x''[i]\) is incorrect for the instance \(max(K,K')\). By definition of HintedKnapsackExtend<sup>+</sup>, this means that all maximizers \((\bar{x},\bar{z})\) (where \(\bar{x}\in\mathbb{Z}_{\ge 0}^U\)) of the objective value<tbc>

\(\bar{r}=q''[\bar{z}]+\sum_{w\in U}Q_w(\bar{x}_w)\)

<tbc>(subject to \(\bar{z}+\sum_{w\in U}w\cdot\bar{x}_w=i\)) should satisfy the support containment condition,

\(supp(\bar{x})\subseteq S''[\bar{z}].\)

Take any such maximizer \((\bar{x},\bar{z})\). Since \(q''[\bar{z}]=max(q[\bar{z}],q'[\bar{z}])\), without loss of generality we assume \(q''[\bar{z}]=q[\bar{z}]\) by symmetry. Then, in instance _K_, \((\bar{x},\bar{z})\) is a valid solution for index _i_, achieving objective value \(q[\bar{z}]+\sum_{w\in U}Q_w(\bar{x}_w)=\bar{r}\). If in solution _Y_ , the found objective _r_\[_i_\] satisfies \(r[i]\ge\bar{r}\), then in the entry-wise maximum solution we would have \(r''[i]\ge max(r[i],r'[i])\ge\bar{r}\), which contradicts the assumption that \(x''[i]\) is incorrect. Hence, \(r[i]<\bar{r}\) holds. Then, since _Y_ is a correct solution to instance _K_, we know from the definition of HintedKnapsackExtend<sup>+</sup> instance _K_ that there can only be two possibilities:

• Case 1: \((\bar{x},\bar{z})\) is not a maximizer solution for index _i_ in _K_.<tbc>

<tbc>This would immediately mean that the actual maximum objective for index _i_ in instance \(max(K,K')\) is also greater than \(\bar{r}\), a contradiction.<tbc>

• Case 2: \((\bar{x},\bar{z})\) is a maximizer solution for index _i_ in _K_, but there is another maximizer solution (**_x_**_<sup>⋆</sup>,z_<sup>∗</sup>) for index _i_ that does not satisfy the support containment condition \(supp(x^\star)\subseteq S[z^\star]\) for instance _K_.<tbc>

<tbc>Then, there are two cases:<tbc>

