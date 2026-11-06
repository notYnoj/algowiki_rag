where P<sub>1</sub> and P<sub>2</sub> differ by _x_ changes of type X can be transformed in linear time to an equivalent instance \(\mathcal{I}'=(A',\mathcal{P}'_1,\mathcal{P}'_2,M'_1,k')\) of ISM(-T) with \(\mathcal{P}'_1\) and \(\mathcal{P}'_2\) differing by O(_x_) changes of type Y. We call two change types X and Y _linearly equivalent_ if both X linearly reduces to Y and Y linearly reduces to X.

**Theorem 1.** _Swap, Replace, Delete, and Add are linearly equivalent for_ ISM _and_ ISM-T.

We show the equivalence of all considered different types of changes using a circular reasoning. First, we observe that Swap is a special case of Replace since every swap can be performed by a Replace operation.

**Observation 1.** _Swap can be linearly reduced to Replace._

Next, we show how Delete can be linearly reduced to Swap.

**Lemma 1.** _Delete can be linearly reduced to Swap._

_Proof._ Let I=(_A,_P<sub>1</sub>,P<sub>2</sub>_,M_<sub>1</sub>_,k_) be an instance of ISM(-T) for Delete. Let _A_delete be the set of agents with empty preferences in P<sub>2</sub> and non-empty preferences in P<sub>1</sub> (i.e., the set of "deleted" agents). We create an instance \(\mathcal{I}'=(A',\mathcal{P}'_1,\mathcal{P}'_2,M'_1,k')\) for Swap as follows. To create \(A'\), for each agent \(a\in A\), we add an agent \(a'\) and set \(a'\)’s preferences in both \(\mathcal{P}'_1\) and \(\mathcal{P}'_2\) to _a_’s preferences in P<sub>1</sub>. For each \(a\in A_\text{delete}\), we further add two agents \(a''\) and \(a'''\) to \(A'\). In \(\mathcal{P}'_1\), agent \(a''\) prefers agent \(a'''\) to \(a'\), while \(a'''\) only considers \(a''\) acceptable. Moreover, we modify the preferences of agent \(a'\) such that it prefers \(a''\) to all other agents in \(\mathcal{P}'_1\) and \(\mathcal{P}'_2\). In \(\mathcal{P}'_2\), agent \(a''\) performs a swap in its preferences and now prefers \(a'\) to \(a'''\). We set \(M'_1:=\{\{a',b'\}:\{a,b\}\in M_1\}\cup\{\{a'',a'''\}:a\in A_\text{delete}\}\) and \(k':=k+2|A_\text{delete}|\).

The correctness easily follows from the observation that every stable matching for \(\mathcal{P}'_1\) contains edge \(\{a'',a'''\}\) for every \(a\in A_\text{delete}\), while every stable matching for \(\mathcal{P}'_2\) contains edge \(\{a',a''\}\) for every \(a\in A_\text{delete}\), and \(a'''\) is unmatched.

We continue by observing that Add can be linearly reduced to Delete.

**Lemma 2.** _Add can be linearly reduced to Delete._

_Proof._ Let I=(_A,_P<sub>1</sub>,P<sub>2</sub>_,M_<sub>1</sub>_,k_) be an instance of ISM(-T) for Add. Let _A_add be the set of agents with empty preferences in P<sub>1</sub> and non-empty preferences in P<sub>2</sub> (i.e., the set of "added" agents). We create an instance \(\mathcal{I}'=(A',\mathcal{P}'_1,\mathcal{P}'_2,M'_1,k')\) for Delete as follows. To create \(A'\), for each agent \(a\in A\), we add an agent \(a'\) and set \(a'\)’s preferences in both \(\mathcal{P}'_1\) and \(\mathcal{P}'_2\) to _a_’s preferences in P<sub>2</sub>. For each \(a\in A_\text{add}\), we add an agent \(a''\) to _A_. Agent \(a''\) only finds \(a'\) acceptable in \(\mathcal{P}'_1\), while the preferences of \(a''\) in \(\mathcal{P}'_2\) are empty (\(a''\) gets deleted). In \(\mathcal{P}'_1\) and \(\mathcal{P}'_2\), we modify the preferences of \(a'\) by adding \(a''\) at the first position. We set \(M'_1:=\{\{a',b'\}:\{a,b\}\in M_1\}\cup\{\{a',a''\}:a\in A_\text{add}\}\) and \(k':=k+|A_\text{add}|\). The correctness of the reduction follows from the observation that every stable matching in \(\mathcal{P}'_1\) contains edge \(\{a',a''\}\) for every \(a'\in A_\text{add}\), while \(a''\) is unmatched in every stable matching in \(\mathcal{P}'_2\) (and cannot form a blocking pair in any matching).

Finally, we show that Replace can be reduced to Add.

**Lemma 3.** _Replace can be linearly reduced to Add._

_Proof._ Let \(\mathcal{I}=(A=U\cup W,\mathcal{P}_1,\mathcal{P}_2,M_1,k)\) be an instance of ISM(-T) for Replace. From this, we construct an instance \(\mathcal{I}'=(A'=U'\cup W',\mathcal{P}'_1,\mathcal{P}'_2,M'_1,k')\) of ISM(-T) for Add as follows. Let _A_repl be the set of agents with different preferences in P<sub>1</sub> and P<sub>2</sub>, and let \(A_\text{repl}^*:=A_\text{repl}\cup\{M_1(a):a\in A_\text{repl}\wedge M_1(a)\neq\emptyset\}\) be the set of these agents and their partners in _M_<sub>1</sub>. To construct \(\mathcal{I}'\), we start by adding all agents from _A_ to \(A'\) and set the preferences of all agents in \(\mathcal{P}'_1\) and \(\mathcal{P}'_2\) to be their preferences<tbc>

