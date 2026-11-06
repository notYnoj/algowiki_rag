Now we can show the following structural statement about the agents \(x_i^1\), \(x_i^2\), and \(x_i^3\), essentially stating that if one of these agents is matched to a 2-set {_c<sub>j</sub>,d<sub>j</sub>_} (corresponding to setting variable _x<sub>i</sub>_ to true), then all three of them are. From this statement, the backward direction of the correctness proof for the reduction will then easily follow.

**Lemma 3.6.** _Let M be any stable matching. Then for all_ \(i\in[n+1]\)_, the following holds:_

_For all i_<sup>∗</sup>_\<i either_ \(\{x_{i^*}^1,x_{i^*}^2,x_{i^*}^3\}\in M\) _or for each_ \(k\in[3]\)_, there exists some_ \(j\in[m]\) _such that_ \(\{x_{i^*}^k,c_j,d_j\}\in M\)_. Furthermore, for each_ \(k\in[3]\)_, matching M contains two 3-sets t_<sub>1</sub> _and t_<sub>2</sub> _with_ \(t_1,t_2\subseteq\{z_{i^*}^{k,p}:p\in[6]\}\).

_Proof._ We prove the lemma by induction on _i_. For _i_=1, there is nothing to show.

By the induction hypothesis, for every _q\<i_, no agent \(x_q^k\) or \(z_q^{k,p}\) is matched to a 2-set containing an agent \(x_q^r\) or \(z_q^{r,s}\) with \(r\neq q\), and by Lemma 3.4, no agent \(z_i^{k,p}\) is matched to a 2-set containing an agent _c<sub>j</sub>_ or _d<sub>j</sub>_.

Let \(S:=\{k\in[3]:\exists j\in[m]\text{s.t.}\{x_i^k,c_j,d_j\}\in M\}\) be the set of indices \(k\in[3]\) such that \(x_i^k\) is matched to a 2-set of the form {_c<sub>j</sub>,d<sub>j</sub>_}.

**Case 1:** |_S_|=\[3\].

By induction on _k_, we can apply Lemma 3.5 for every \(k\in[3]\), showing that _M_ contains two 3-sets \(t_1,t_2\subseteq\{z_i^{k,p}:p\in[6]\}\).

**Case 2:** \(S=\emptyset\).

Then _M_ contains \(\{x_i^1,x_i^2,x_i^3\}\), as all 2-sets before sublist C_<sub>i</sub>_ contain an agent which is not matched to an agent \(x_i^k\) in _M_. As in Case 1, induction on _k_ together with Lemma 3.5 implies that for every \(k\in[3]\), matching _M_ contains two 3-sets _t_<sub>1</sub> and _t_<sub>2</sub> with \(t_1,t_2\subset\{z_i^{k,p}:p\in[6]\}\).

**Case 3:** \(|S|\in\{1,2\}\).

We show that this case leads to a contradiction and, therefore, cannot occur.

**Case 3 (a):** No 3-set in _M_ contains two agents of the form \(x_i^k\) for \(k\in[3]\).

If there is no \(j\in[m]\) such that \(\{x_i^1,c_j,d_j\}\in M\), then the agents \(x_i^1\), \(z_i^{1,1}\), ..., \(z_i^{1,5}\) have to be matched to two 3-sets, as all agents appearing in a 2-set before \(\mathcal{B}_i^1\) in the master list cannot be matched to \(x_i^1\) or \(z_i^{1,p}\) because of Lemma 3.4 and the induction hypothesis. By Lemma 3.3, this implies that _M_ contains a blocking 3-set inside \(x_i^1,z_i^{1,1},\dots,z_i^{1,5}\), contradicting the stability of _M_. Thus, there exists some \(j\in[m]\) such that \(\{x_i^1,c_j,d_j\}\in M\). Then _M_ contains two 3-sets _t_<sub>1</sub> and _t_<sub>2</sub> with \(t_1,t_2\subseteq\{z_i^{1,p}:p\in[6]\}\) by Lemma 3.5.

We can conclude then by the same argument that \(x_i^2\) is matched to a 2-set \(\{c_{j^\prime},d_{j^\prime}\}\) for some \(j'\in[m]\), and from this that \(x_i^3\) is matched to a 2-set \(\{c_{j^{\prime\prime}},d_{j^{\prime\prime}}\}\) for some \(j''\in[m]\), a contradiction.

**Case 3 (b):** There is a 3-set \(\{x_i^{k_1},x_i^{k_2},z\}\in M\) with \(z\notin\{x_i^k\}\).

If \(\{x_i^1,c_j,d_j\}\in M\) for some \(j\in[m]\), then _M_ contains two tuples inside \(z_i^{1,1},\dots,z_i^{1,6}\) by Lemmas 3.4 and 3.5 and the induction hypothesis. It follows that there exists a blocking 3-set inside \(x_i^2,z_i^{2,1},\dots,z_i^{2,5}\) by Lemma 3.3.

Consequently, we can assume in the following that \(\{x_i^1,c_j,d_j\}\notin M\) for all \(j\in[m]\). We may also assume that _k_<sub>1</sub>=1 or _k_<sub>2</sub>=1, since otherwise \(\{x_i^1,x_i^2,x_i^3\}\) was a blocking 3-set. Then \(x_i^1\) prefers to be matched to the 2-set \(\{z_i^{1,1},z_i^{1,2}\}\) or \(\{z_i^{1,3},z_i^{1,5}\}\). Every 2-set which agent \(z_i^{1,1}\) respectively \(z_i^{1,2}\) prefers to \(\{x_1^1,z_i^{1,2}\}\) respectively \(\{x_1^1,z_i^{1,1}\}\) is one of the 2-sets \(\{x_i^1,x_i^2\}\), \(\{x_i^1,x_i^3\}\), or \(\{x_i^2,x_i^3\}\), contains an agent \(x_k^j\) with _j\<i_, or contains an agent _c<sub>j</sub>_ or _d<sub>j</sub>_ for some \(j\in[m]\). Thus, unless \(z_i^{1,1}=z\) or \(z_i^{1,2}=z\) holds, \(z_i^{1,1}\) and \(z_i^{1,2}\) also prefer to be matched by \(\{x_i^1,z_i^{1,1},z_i^{1,2}\}\). If \(z=z_i^{1,1}\) or \(z=z_i^{1,2}\), then \(z_i^{1,3}\neq z\) and \(z_i^{1,5}\neq z\), and by arguments symmetrically to the above ones, \(\{x_i^1,z_i^{1,3},z_i^{1,5}\}\) is blocking.

The backward direction now easily follows.

