**Proposition 3.12.** _Given two forests_ \(\mathbf{F},\mathbf{F}'\) _and a node_ \(v\in\mathbf{F}\)_, let_ **P** _be the set of nodes contained in the path going from the virtual root of_ **F** _to v (virtual root and v excluded). Then, for each pair of subforests_ **F**[_x...y_] _and_ \(\mathbf{F}'[x'..y'\) _) such that_ \(\mathrm{sub}(v)\subseteq\mathbf{F}[x..y\) _) at least one of the two following cases holds:_

(**a**) _There exists a node_ \(u\in\mathbf{P}\) _such that_ \(\mathrm{sim}(\mathbf{F}[x..y\) ),\mathbf{F}'[x'..y'\) )) _aligns_ sub(_u_) _to a subtree of_ \(\mathbf{F}'\).

(**b**) \(\mathrm{sim}(\mathbf{F}[x..y\) ),\mathbf{F}'[x'..y'\) )) = sim(**F**[_x..._l(_v_)) +**F**[l(_v)..y_ ),\(\mathbf{F}'\)).

**Proof.** We show that whenever (a) does not hold, then (b) does. To this end, note that **F**[_x..._l(_v_)) +**F**[l(_v)..y_ ) corresponds to **F**[_x..y_ ) with all the nodes from **P** taken out. Moreover, the pre-order of **F**[_x..._l(_v_)) +**F**[l(_v)..y_ ) equals to the pre-order of **F**[_x..y_ ) with the nodes of **P** taken out.

Next, let us compare the computations done by Shasha and Zhang’s recurrence scheme [SZ89] for the two similarities \(\mathrm{sim}(\mathbf{F}[x..y\) ),\mathbf{F}'[x'..y'\) )) and \(\mathrm{sim}(\mathbf{F}[x..l(v)\) +**F**[l(v)..y\) ),\(\mathbf{F}'\)). When computing \(\mathrm{sim}(\mathbf{F}[x..y\) ),\mathbf{F}'[x'..y'\) )) note that each time the recurrence scheme arrives to consider as next node of **F**[_x..y_ ) some \(u\in\mathbf{P}\), we can ignore the case where sub(_u_) is aligned to the subtree of the current node in \(\mathbf{F}'[x'..y'\) ). As a consequence, we can assume that _u_ is always deleted. We conclude that we obtain the same computations as in the recurrence scheme for \(\mathrm{sim}(\mathbf{F}[x..l(v)\) +**F**[l(v)..y\) ),\(\mathbf{F}'\)).

Spines. Let **F** be a forest. We define a _spine_ as a path that starts at the root of one of the trees in **F** and ends in a leaf within that tree.

Now, consider a spine \(\mathbf{S}\subseteq\mathbf{F}\). For \(s,q\in\mathbf{S}\), we write _s\<q_ if _s_ appears before _q_ in the root-to-leaf path, and we say _s precedes q_. Furthermore, we say that _s immediately precedes q_ if there is no \(r\in\mathbf{S}\) such that _s\<r\<q_.

Lastly, suppose a spine \(\mathbf{S}\subseteq\mathbf{F}\) is a path of the form _s_<sub>1</sub>_,...,s<sub>m</sub>_. We observe that for all \(i\in[1..m\) ), a bi-order traversal enters _s<sub>i</sub>_ before it enters _s_<sub>_i_+1</sub>, and leaves _s_<sub>_i_+1</sub> before it leaves _s<sub>i</sub>_. Consequently,

\(l(s_1)<l(s_2)<\cdots<l(s_m)<r(s_m)<\cdots<r(s_2)<r(s_1).\)

Moreover, l(_s<sub>m</sub>_)=r(_s<sub>m</sub>_)-2, since _s<sub>m</sub>_ is a leaf and the bi-order traversal leaves _s<sub>m</sub>_ right after it enters it.

## 3.1 Min-Plus Products and Structured Instances

While Min-plus Matrix Multiplication (MUL) of \(n\times n\) matrices is commonly conjectured to require _n_<sup>3-_o_(1)</sup> time, there have been several structured instances in which faster algorithms have been obtained, e.g. bounded entries [AGM97], (row/column) bounded-difference matrices [BGSV19], and (row/column) monotone matrices [VX20, GPVX21, CDXZ22] . Specifically, we focus on the class of monotone matrices.

**Definition 3.13.** _An_ \(n\times n\) _matrix is row-monotone if all entries are non-negative integers bounded by_ O(_n_) _and each row of this matrix is non-decreasing. Similarly, we may define a column-monotone matrix._

When at least one of the matrices is row-monotone or column-monotone, there are sub-cubic algorithms for min-plus matrix multiplication [VX20, GPVX21, CDXZ22].

**Theorem 3.14** ([CDXZ22])**.** _There is a (randomized) algorithm that computes the min-plus product A∗B in expected running time_ \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\)_, where A is an_ \(n\times n\) _integer matrix and B is a_ \(n\times n\) _row-monotone matrix. The result holds also when B is a_ \(n\times n\) _column-monotone matrix._

The above result holds also when the rows or columns of the matrix are non-increasing.

We let T<sub>MonMUL</sub>(_n_) denote the time required to multiply an \(n\times n\) integer matrix with a \(n\times n\) monotone matrix. Furthermore, let T<sub>MonMUL</sub>(_a,b,c,d_) be the time required to multiply an \(a\times b\) integer matrix with a \(b\times c\) monotone matrix with all entries bounded by _d_.

