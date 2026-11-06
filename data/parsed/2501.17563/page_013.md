\(P_1=\frac{1}{2}\cdot\left[\begin{array}{ c c c c c c }
. & 2 & 0 & 0 & 0 & 0 \\
0 & . & 1 & 0 & 0 & 2 \\
2 & 1 & . & 1 & 1 & 0 \\
1 & 1 & 1 & . & 1 & 2 \\
1 & 0 & 0 & 1 & . & 2 \\
0 & 0 & 2 & 0 & 0 & .
\end{array}\right]444226\) (3)

## 2.3 Integrality Gap - Lower Bounds

A lower bound of \(\frac{60}{59}\) on the integrality gap of the LP follows from Theorem 2.2. For a tighter lower bound on the integrality gap, we can study all the non-integer vertices in all seven small topologies that have such vertices.

**Lemma 2.8.** Given a fixed topology _U_, let D={_D_<sup>1</sup>_,...,D<sup>N</sup>_} be all the _D_-space vertices induced by STTs, and let S={_S_<sup>1</sup>_,...,S<sup>M</sup>_} be additional vertices of the _D_-space projection of the LP polytope, where each _S<sup>i</sup>_ is found by solving the LP in the primary directions _h_<sup>_i,_1</sup>_,...,h_<sup>_i,k<sub>i</sub>_</sup> for some \(k_i\ge 1\). Denote \(\Delta\equiv max\{min_{A\in conv^+(\mathbb{D})}(A\cdot f)-min_{B\in conv^+(\mathbb{D}\cup\mathbb{S})}(B\cdot f)|\forall i:f_i\ge 0\wedge\sum_{i=1}^nf_i=1\}\) (the largest additive gap), where _conv_<sup>+</sup> is a convex combination over a set of points, and positive rays. Then if \(\Delta>0\), it is achieved for some _i,j,k_ such that _B=S<sup>i</sup>_, \(f=\hat{h}^{i,j}\) and _A=D<sup>k</sup>_, where hat represents normalization to a sum of one, and _D<sup>k</sup>_ is on the false facet of _conv_<sup>+</sup>(D) whose normal is _h_<sup>_i,j_</sup>. (Recall Section 2.2.)

_Proof._ Let _f_ be a direction (vector) that maximizes \(\Delta\). The scalar product with _f_ projects the polytope _conv_<sup>+</sup>(D) to one dimension, therefore the minimum has a pre-image that is a vertex, this is _A=D<sup>k</sup>_. Similarly, by arguing for \(conv^+(\mathbb{D}\cup\mathbb{S})\) we get that _B_ can be chosen as either some _D<sup>i</sup>_ or _S<sup>i</sup>_. However, \(D^k\cdot f\le D^i\cdot f\) for every \(1\le i\le N\), so it must be that _B=S<sup>i</sup>_ (or else \(\Delta=0\)).

Now fix _A_ and _B_, denote _C=A-B_, and let us show that we can replace _f_ by some \(\hat{h}^{i,j}\), without decreasing \(\Delta\) which will conclude the proof. Since _f_ is a (normal to a) separating plane that intersects _A_, in a problem of covering form,<sup>7</sup> by strong-duality we get that \(f=\sum_j\alpha_j\cdot\hat{h}^j\) for non-negative coefficients \(\alpha_j\), where _h<sup>j</sup>_ are all the normals to facets of _conv_<sup>+</sup>(D) that contain _A_. Moreover, \(\sum_j\alpha_j=1\) because all of _f_ and \(\hat{h}^j\) have coordinate sum of 1. We get that: \(C\cdot f=\sum_j\alpha_j\cdot(C\cdot\hat{h}^j)\le C\cdot\hat{h}^{j*}\) by choosing _j_<sup>∗</sup> that maximizes the scalar product. However, since _f_ is a maximizer, we get equality, and conclude that \(\hat{h}^{j*}\) is a primary direction that maximizes \(\Delta\). Finally, it must be that \(\hat{h}^{j*}\) is a normal to a false facet that contains _A_. Otherwise, it does not imply a separating plane, and therefore \(A\cdot\hat{h}^{j*}-B\cdot\hat{h}^{j*}\le 0\), which is a contradiction.

By Lemma 2.8 it suffices to consider only vertices and primary directions to maximize the additive gap, and in particular only check for gaps of the form: \((D^k-S^i)\cdot h^{i,j}\). By choosing for each topology the vertices _S<sup>i</sup>_ and _D<sup>k</sup>_, and the primary direction _h<sup>i,j</sup>_ that maximize \(\Delta\), we get  2. Anecdotally, the largest gap for _U_<sub>(7,3)</sub> is due to the primary direction which we studied in Theorem 2.2. Based on the small topologies we studied, the integrality gap is at least \(\frac{95}{93}\approx 1.0215\), which is much closer to 1 (almost optimal) than to the proven upper bound of 2. Note that maximizing the difference does not necessarily maximize the integrality gap (ratio).

Another interesting note is that the topology _U_<sub>(8,11)</sub> extends _U_<sub>(7,3)</sub> (Definition 3.11), and it happens to be that the direction that maximizes the difference for _U_<sub>(8,11)</sub> is an extension of the direction that maximizes the difference for _U_<sub>(7,3)</sub>.

<sup>7</sup>An LP problem of the form minimize \(c\cdot x\) where \(Ax\ge b\), \(x\ge 0\), \(c\ge 0\) for vectors _x,b,c_ and matrix _A_.

