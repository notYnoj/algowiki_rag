<tbc>**Theorem 1.2.** _For every integer k\>_3_, worst-case k_-SUM _can be solved in quantum time_ \(\widetilde{O}(n^{\Psi_k})\)_, where_<sup>5</sup>

\(\Psi_k=\underbrace{\frac{2k-\lfloor k/7\rfloor-\lfloor(k+3)/7\rfloor}{6}_{\Phi_k}}_{-\frac{[k\equiv 3\mathrm{mod}7]}{9}}-\frac{[k\equiv 6\mathrm{mod}7]}{18}.\)

## 3.1 Partition

Let _k_<sub>1</sub>_,k_<sub>2</sub>_,k_<sub>3</sub>_,k_<sub>4</sub> be positive integer parameters satisfying _k_<sub>1</sub>+_k_<sub>2</sub>+_k_<sub>3</sub>+_k_<sub>4</sub>=_k_; their values will be chosen at the end of the proof. Group the _k_ input lists into four consecutive blocks of sizes (_k_<sub>1</sub>_,k_<sub>2</sub>_,k_<sub>3</sub>_,k_<sub>4</sub>), numbered 1, 2, 3, and 4. Thus, block 1 consists of the first _k_<sub>1</sub> input lists, and blocks 2, 3, and 4 consist of the next _k_<sub>2</sub>, _k_<sub>3</sub>, and _k_<sub>4</sub> input lists, respectively.

The index tuples of the four blocks range over the product domains

\(\mathcal{X}_i=[n]^{k_i}\text{for every}i\in[4],\)

and we write \(\alpha_i\in\mathcal{X}_i\) for an index tuple of block _i_. For each \(i\in[4]\), let \(\Sigma_i:\mathcal{X}_i\rightarrow\mathbb{Z}\) map a tuple of block _i_ to its sum. For example, if \(\alpha_1\in\mathcal{X}_1\), then \(\Sigma_1(\alpha_1)=\sum_{j\in[k_1]}A_j[\alpha_1[j]]\).

## 3.2 Construction

### Searching in a random subspace.

The straightforward approach would construct complete lists of sums for the blocks used in the search. Instead, we retain only a small sample of tuples from some of the blocks and use a quantum walk to find the appropriate subset of tuples.

Let \(r\in(0,\mathrm{min}\{k_2,k_4\}]\) be a parameter, whose value is fixed at the end of the proof, and set<tbc>

\(m=\lfloor n^r/2\rfloor.\)

<tbc>We perform a quantum walk on the graph<tbc>

\(\mathcal{G}=J(\mathcal{X}_2,m)\times J(\mathcal{X}_4,m),\)

<tbc>whose vertices are of the form

\(v=(S_2,S_4)\in\genfrac(){pt}{2}{\mathcal{X}_2}{m}\times\genfrac(){pt}{2}{\mathcal{X}_4}{m}.\)

We will choose _k_<sub>2</sub>=_k_<sub>4</sub>, so |X<sub>2</sub>|=|X<sub>4</sub>| and G is isomorphic to \(J(\mathcal{X},m)\times J(\mathcal{X},m)\) for a set X of that cardinality. Each X_<sub>i</sub>_ is the set of all index tuples for block _i_; for \(i\in\{2,4\}\), \(S_i\subseteq\mathcal{X}_i\) is the _m_-element sample stored at the vertex, and \(x\in S_i\) denotes a single sampled tuple. One step of the walk chooses \(i\in_R\{2,4\}\), \(x\in_RS_i\), and \(x'\in_R\mathcal{X}_i\). If \(x'\notin S_i\), the step replaces _x_ by \(x'\) in that coordinate; otherwise it remains at _v_.

Fix a particular _k_-SUM solution and denote its four tuples of selected indices, one for each block, by \(\alpha^*=(\alpha_1^*,\alpha_2^*,\alpha_3^*,\alpha_4^*)\). For \(i\in\{2,4\}\), a uniformly random _m_-subset of X_<sub>i</sub>_ contains a fixed tuple with probability _m/n<sup>k<sub>i</sub></sup>_. Consequently, the fraction of vertices _v_=(_S_<sub>2</sub>_,S_<sub>4</sub>) with \(\alpha_2^*\in S_2\) and \(\alpha_4^*\in S_4\) is<tbc>

\(\mathrm{Pr}_{v=(S_2,S_4)\in_RV(\mathcal{G})}[\alpha_2^*\in S_2\text{and}\alpha_4^*\in S_4]=\frac{m^2}{n^{k_2+k_4}}.\)

<sup>5</sup>\([\cdot]\) is the Iverson bracket: for a condition E, \[E\]=1 if E holds, and \[E\]=0 otherwise.

