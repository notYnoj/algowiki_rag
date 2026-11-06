**Lemma 26.** _After each iteration of the main loop in_ WSHTreeSelect_, we have_ \(W(C)\le 2W(D)\) _and_ \(|S^*|\le 8W(D)\)_, where S_<sup>∗</sup> _is the current value of S, D is the set of nodes deleted from Q so far, and C is the set of corrupted nodes currently in Q._

_Proof._ Let _S_<sup>∗</sup> be the value of _S_ after the current iteration. Observe that |_S_<sup>∗</sup>| is precisely the set of all nodes ever inserted into _Q_. By the corruption invariant of the WSH (lemma 17), we have

\(W(C)\le\varepsilon(|S^*|+W(D))=\frac{1}{6}(|S^*|+W(D)).\) (1)

We now determine |_S_<sup>∗</sup>|. At the start, we insert one node into _S_ (the root, line 4). Afterwards, whenever a node is deleted from or corrupted in _Q_, we insert some of its children into _S_ (line 22). Since all the inserted children are marked at the end of the iteration, by lemma 25, there can be no more than three such children. Thus, we have \(|S^*|\le 3(|D|+|C|)+1\). Since clearly \(|C|\le W(C)\) and \(|D|\le W(D)\), we can combine this with eq. (1) to obtain

\(|S^*|\le 3|D|+\frac{1}{2}(|S^*|+W(D))+1\Longrightarrow|S^*|\le 7\cdot W(D)+2\le 9\cdot W(D)\)<br>
\(\Longrightarrow W(C)\le\frac{10}{6}W(D)\le 2W(D).\)

**Lemma 27.** _The first i iterations of_ WSHTreeSelect _perform_ \(\mathcal{O}(W(D))\le\mathcal{O}(i+c(T_0,D))\) _comparisons, where D is the set of i nodes deleted from Q so far._

_Proof._ Let _C_ be the set of nodes corrupted in _Q_, but not deleted so far. We first analyze the time spend by heapification. Note that we call Heapify always on the unmarked children of a node _v_ that has just been deleted or corrupted, that is, \(v\in D\cup C\). By lemma 25, there are no more than \(\mathrm{deg}(T_0,v)\le w(v)\) many unmarked children, so the total cost of Heapify is O(_W(C_)+_W(D_)). Other than that, our algorithm clearly spends constant time for every node in _S_, so the total running time is O(_W(C_)+_W(D_)+|_S_|).

By lemma 26, this is bounded by O(_W(D_)). Observe now that \(W(D)=\sum_{v\in D}(1+\mathrm{deg}(T_0,D))\). Since _D_ is a prefix by lemma 21, we have \(\sum_{v\in D}\mathrm{deg}(T_0,D)=|D|-1+c(T_0,D)\). Since |_D_|=_i_, we have \(W(D)\le 2i-1+c(T_0,D)\le\mathcal{O}(i+c(T_0,D))\), as desired.

## Running time.

Ignoring the loop of line 8, the running time of the algorithm is:

• The time for the heapifications, which is asymptotically bounded by the number of comparisons in the heapifications, which is O(_k_+OPT) as proved above.<tbc>

• The time spend within _Q_, which is again O(_k_+OPT).<tbc>

• O(1) for each element in _S_ in the end, which is O(_k_+OPT) by lemmas 26 and 27.

We now discuss the loop of line 8. As written, it may actually require \(\Theta(k^2)\) time in total, since nodes _Q_ may induce paths of length \(\Omega(k)\) (see fig. 4).

We fix this as follows. When line 9 is executed one or more times, record all traversed nodes _x_. They form a directed (ancestor-to-descendant) path (_x_<sub>1</sub>_,x_<sub>2</sub>_,...,x<sub>t</sub>_) in _T_, and we will have _x=x_<sub>1</sub> in this iteration. For the next _t_-1 iterations, skip the \(x\leftarrow Q.\text{\texttt{find-min}}()\) call (line 7) and instead assign \(x\leftarrow x_2\), \(x\leftarrow x_3\), and so on.

