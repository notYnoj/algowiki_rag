<tbc>of the proper path cover, because _i\<j\<t_. Therefore, \(E(X)\cap(\mathrm{Inv}(e_i)\backslash\mathrm{Inv}(e_j)\backslash\mathrm{Inv}(S_{i-1}))=\emptyset\). Consequently:

\(\mathbf{w}(X')\ge\mathbf{w}(X)-\mathbf{w}(e_i)+\mathbf{w}(e_j)\)<br>
\(+\mathbf{w}(\mathrm{Inv}(e_i)\backslash\mathrm{Inv}(e_j)\backslash\mathrm{Inv}(S_{i-1}))\)<br>
\(-\mathbf{w}(\mathrm{Inv}(e_j)\backslash\mathrm{Inv}(e_i)\backslash\mathrm{Inv}(S_{i-1}))\)

Let _I_:=Inv(_e<sub>i</sub>_)\\Inv(_S_<sub>_i_-1</sub>) and _J_:=Inv(_e<sub>j</sub>_)\\Inv(_S_<sub>_i_-1</sub>). From the lemma statement we have<tbc>

\(0\le\mathbf{rp}(S_{i-1},e_i)-\mathbf{rp}(S_{i-1},e_j)=(\mathbf{w}(I)-\mathbf{w}(e_i))-(\mathbf{w}(J)-\mathbf{w}(e_j))\)

<tbc>Define _W_ as \(I\cap J\). Since \(W\subseteq I\) and \(W\subseteq J\), we have **w**(_I_)-**w**(_J_)=**w**(_I_\\_W_)-**w**(_J_\\_W_). Substituting this into the inequality yields:<tbc>

\((\mathbf{w}(I\backslash W)-\mathbf{w}(e_i))-(\mathbf{w}(J\backslash W)-e_j)\ge 0\)

<tbc>Observe that _I_\\_W_=Inv(_e<sub>i</sub>_)\\Inv(_e<sub>j</sub>_)\\Inv(_S_<sub>_i_-1</sub>) and _J_\\_W_=Inv(_e<sub>j</sub>_)\\Inv(_e<sub>i</sub>_)\\Inv(_S_<sub>_i_-1</sub>). Plugging this into the inequality for \(\mathbf{w}(X')\), we obtain:

\(\mathbf{w}(X')\ge\mathbf{w}(X)+(\mathbf{w}(I\backslash W)-\mathbf{w}(e_i))-(\mathbf{w}(J\backslash W)-e_j)\ge\mathbf{w}(X)\)

Therefore, \(X'\) is also a valid solution for I. \(\lrcorner\)

We exhaustively apply modifications of these three types to _X_ in an arbitrary order. Note that this process is finite, because each modification strictly decreases the value of \(\sum_{i=1}^{n-1}i\cdot[e_i\in S]\). Indeed, modifications of the first two types remove an edge from _S_, and modifications of the third type replace an edge from \(e_j\in S\) with \(e_i\notin S\), where _i\<j_. In the end, we obtain a solution for I that satisfies all the required properties.

Let us demonstrate the power of Lemma 4. First, it follows that there is a solution to I, where only at most |P| tree edges with non-positive remaining profits are removed iteratively. Second, Observation 6 guarantees that _k_ positive remaining profits are enough to obtain a solution. Therefore, it is enough to consider edge subsets \(S\subseteq E(T)\) of size at most |P|+_k_.

On the other hand, Lemma 4 gives us a limited number of choices of what edge to remove next. Indeed, when we have to remove an edge, we know that its remaining profit is in \[-**w**(_A),k_\]. The third point of Lemma 4 guarantees that we can always choose the earliest (with respect to the ordering) edge that belongs to \(P_\ell\) with the value of remaining profit equal to _p_, for small integer values of _p_ and \(\ell\).

## 4.4 Solution when the removed tree edges are fixed

It comes naturally from Lemma 4 that we have to solve the following special version of the problem. We have a fixed edge set \(S\subseteq E(T)\) of bounded size, and we have to find a solution \(G'\) to (_G,_**w**_,k_) that contains all edges in _E(T-S_) and contains no edge of _S_. The following lemma shows that we are able to solve this subproblem efficiently.

**Lemma 5.** _There is an algorithm with the running time_ \(2^{(\mathbf{w}(A))^{\mathcal{O}(1)}}\cdot n^{\mathcal{O}(1)}\) _that, given an instance_ I=(_G,_**w**_,k_) _of_ \(MAS/\mathrm{MaxST}(\mathbb{Z}_{\ge 1})\)_, and given a tree edge set_ \(S\subseteq E(T)\)_, either_

