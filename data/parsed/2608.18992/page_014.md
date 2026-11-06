and thus

\(\mathbf{E}[\alpha]\ge\frac{1}{2}\sum_{i=1}^{\ell-1}\mathbf{E}[\alpha_i]=\Omega\big(\frac{(\ell-1)\cdot I}{d_{cut}logn}\big),\)

and the claimed bound on the expected node-averaged complexity follows.

The most prominent instance of a function _f_ in communication complexity is the _set disjointness_ function (DISJ<sub>_m_</sub>): Alice and Bob each get a subset of some universe of size _m_, represented as the corresponding _m_-length characteristic vectors, and they must communicate to decide whether these sets are disjoint. Numerous lower bound reductions employ the hardness result of set disjointness (e.g., [11, 5]), which says that the players need to communicate \(\Omega(m)\) bits. For the subsequent applications, we require a stronger property, namely that any set disjointness protocol must leak a linear amount of information:

\(\blacktriangleright\) **Fact 3.1** (Information cost of set disjointness [19])**.** _The set disjointness function on input vectors of length m has_ \(\text{IC}(\text{DISJ}_m,\epsilon)=\Omega(m)\)_, for a suitable small constant_ \(\epsilon>0\).

Next, we state a corollary that allows a streamlined application of Theorem 4 for several important graph problems. That is, it enables us to directly obtain energy complexity bounds by reusing existing lower bound constructions in the CONGEST model.

\(\blacktriangleright\) **Corollary 6.** _Consider a graph predicate P, and suppose that there exists an_ \(\ell\)_-separated graph family_ G _with respect to_ DISJ<sub>_m_</sub> _and P, where_ \(m=\Theta\big(n^2\big)\)_, and where d<sub>cut</sub> denotes the maximum cut degree and s denotes the cut set size of_ G_. Then, the worst case energy complexity of any distributed algorithm that decides P is_ \(\Omega\big(\frac{n^2}{d_{cut}\cdot s\cdot logn}\big)\)_, whereas its expected node-averaged energy complexity is_ \(\Omega\big(\frac{\ell-1}{n}\cdot\frac{n^2}{d_{cut}logn}\big)\)_. These bounds hold independently of the time complexity of the algorithm._

**Proof.** The claim on the worst-case energy complexity is immediate from Fact 3.1 and Theorem 4(b). For applying Theorem 4(a), we need to argue that the support of Alice’s input _X_ and Bob’s input _Y_ are bounded from above by \(2^{c\cdot n^2}\), which holds since \(m=\Theta\big(n^2\big)\). \(\blacktriangleleft\)

## 4 Applications

We now demonstrate how to obtain lower bounds for a diverse range of graph problems via the framework from Section 3. For showing a lower bound on the energy complexity of listing all triangles in the graph, we directly apply Lemma 1, whereas, subsequently, we use Corollary 6 for graph problems, whose hardness is based on a reduction from set disjointness.

\(\blacktriangleright\) **Corollary 7** (Triangle Listing)**.** _For_ triangle listing, _where every triangle in the graph is output by at least one of its nodes, the worst case energy complexity is_ \(\Omega\big(n^{1/3}/logn\big)\) _rounds for algorithms that fail with some small constant probability_ \(\epsilon>0\)_. For_ local triangle listing, _which requires every node to output all triangles that it is part of, we obtain a lower bound of_ \(\Omega(n/logn)\) _that holds even for the expected node-averaged energy complexity._

**Proof.** We make use of the existing lower bounds for the CONGEST model of [34, 42]. In more detail, we adapt the proof of Theorem 4.1 in [34], where they show that the node who outputs the maximum number of triangles needs to learn \(\Omega\big(n^{4/3}\big)\) bits (on average) about the edges _E_ of an Erdös-Renyi random graph _G_<sub>_n,_1/2</sub>.

