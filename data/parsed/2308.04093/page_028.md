## 4.2 Helper lemmas for problem decomposition

In this section, we show several helper lemmas for the HintedKnapsackExtend<sup>+</sup> problem (Problem 1). To get some intuition, one may first consider Problem 1 without the relaxation based on hints, which is a standard dynamic programming problem that obeys some kind of composition rule: namely, if we update a DP table _q_\[\] with items from \(U_1\cup U_2\) (for some disjoint _U_<sub>1</sub> and _U_<sub>2</sub>), it should have the same effect as first updating _q_\[\] with _U_<sub>1</sub> to obtain an intermediate DP table, and then updating this intermediate table with _U_<sub>2</sub>. The goal of this section is to formulate and prove analogous composition properties for the HintedKnapsackExtend<sup>+</sup> problem, which will be useful for our decomposition-based algorithms to be described later in Section 4.3. The proofs of these properties are quite mechanical and are similar to the arguments in the proof of Lemma 3.3 in Section 3.3, and can be safely skipped at first read.

Using the notations from Problem 1, we denote an instance of HintedKnapsackExtend<sup>+</sup> as<tbc>

\(K=\big(U,\{Q_w\}_{w\in U},S[-L..L],q[-L..L]\big),\)

<tbc>where \(S[i]\subseteq U\) for all _i_. And we denote a solution to _K_ as<tbc>

\(Y=(x[-L..L],z[-L..L],r[-L..L]).\)

<tbc>where \(z[i]=i-\sum_{w\in U}w\cdot x[i]_w\) by Eq. (16), and

\(r[i]:=q\big[z[i]\big]+\sum_{w\in V}Q_w(x[i]_w)\)

is the objective value. We say a solution _correctly solves K_ if it satisfies the definition of Problem 1 (with the relaxation based on hints _S_\[\]).

Now we define several operations involving the instance _K_. In the following we omit the array index range \[-_L..L_\] for brevity.

**Definition 4.2** (Restriction)**.** The _restriction_ of instance _K_ to a set \(V\subseteq U\) is defined as the instance

\(K|_V:=\big(V,\{Q_w\}_{w\in V},S_V[],q[]\big)\)

where \(S_V[i]:=S[i]\cap V\) .

**Definition 4.3** (Updating)**.** Suppose _Y<sub>V</sub>_=(**_x_**\[\]_,z_\[\]_,r_\[\]) is a solution to _K|<sub>V</sub>_, then we define the following updated instance<tbc>

\(K^{(V\leftarrow Y_V)}:=(U\backslash V,\{Q_w\}_{w\in U\backslash V},S'[],q'[])\)

<tbc>where

\(S'[i]:=S\big[z[i]\big]\backslash V,\) (20)

and

\(q'[i]:=r[i].\)

**Definition 4.4** (Composition)**.** Let \(V,V'\subseteq U,V\cap V'=\varnothing\). Suppose _Y<sub>V</sub>_=(**_x_**\[\]_,z_\[\]_,r_\[\]) is a solution to _K|<sub>V</sub>_, and \(Y_{V^\prime}=(x'[],z'[],r'[])\) is a solution to \(K^{(V\leftarrow Y_V)}|_{V^\prime}\). We define the following composition of solutions,<tbc>

\(Y_{V^\prime}\circ Y_V:=(x''[],z''[],r'[])\)

