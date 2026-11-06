# Faster Algorithms for Induced Patterns

7

Here, \(\phi\) is any homomorphism from _G_\[_B_\] to _H_. We say that \(\phi'\) is _compatible_ with \(\phi\), denoted by \(\phi'\sim\phi\), iff

\(\phi'(v)=\phi(v)\text{for every}v\text{where}\phi(v)\text{and}\phi'(v)\text{are defined.}\)

Let _B_ be any non-root bag with a parent \(B'\). We add gates \(h_{B,\phi}\), where \(\phi\) is a homomorphism from \(G[B\cap B']\) to _H_. These gates will compute the following polynomial:

\(h_{B,\phi}=\sum_{\phi^\prime:G[B]\mapsto H\phi^\prime\sim\phi} g_{B,\phi^\prime}.\) (2)

We now construct the circuit by traversing the tree decomposition _T_ in a bottom-up fashion.

#### Leaf bags:

Suppose that _B_ is a leaf of _T_. Then _G<sub>B</sub>=G_\[_B_\]. There are no child bags, and hence all vertices of _G<sub>B</sub>_ that are local to _B_ can be introduced directly. For every \(\phi:G[B]\mapsto G\), we create the product gate

\(g_{B,\phi}=\prod_{v\in V(G[B])v\text{is local to}B}y_{\phi(v)}.\)

Note that we can enumerate all such \(\phi\) in _O(n<sup>p</sup>m<sup>q</sup>_) time by enumerating all possible images of the (_p,q_)-witness _u_<sub>1</sub>_,...,u<sub>i</sub>_ and _e_<sub>1</sub>_,...,e<sub>j</sub>_ of the bag _B_ where \(i\le p\) and \(j\le q\). This can be done by enumerating all elements of \(V(H)^i\times E(H)^j\).

#### Non-leaf bags:

Now suppose that _B_ is a non-leaf bag with children _B_<sub>1</sub>_,...,B<sub>r</sub>_. For every homomorphism \(\phi:G[B]\mapsto H\), we add the following gate:

\(g_{B,\phi}=\left(\prod_{i=1}^rh_{B_i,\phi|_{B\cap B_i}}\right)\cdot\left(\prod_{v\in V(G[B])v\text{is local to}B}y_{\phi(v)}\right).\) (3)

#### The gates \(h_{B,\phi}\):

The gates \(h_{B,\phi}\) can be constructed as follows: When we construct a gate \(g_{B,\phi^\prime}\) for some \(\phi':G[B]\mapsto H\), we compute \(\phi\sim\phi'\) such that \(\phi:G[B\cap B']\mapsto H\) and then add the gate \(g_{B,\phi^\prime}\) as an input to the +-gate \(h_{B,\phi}\).

#### The output gate:

Finally, the output gate of our circuit is a +-gate that adds all \(g_{R,\phi}\), where _R_ is the root bag in _T_.

#### Correctness:

We prove that the gates \(g_{B,\phi}\) compute the polynomial in Equation 1 using induction. Note that _G<sub>R</sub>=G_ and therefore our output gate will correctly compute Hom<sub>_G,H_</sub> given that all \(g_{B,\phi}\) and \(h_{B,\phi}\) are as claimed.

In the base case, _B_ is a leaf bag and the construction directly computes the required polynomial.

