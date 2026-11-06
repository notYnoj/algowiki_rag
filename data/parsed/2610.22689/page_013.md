## A. Local Canonical Coordinates and Stabilization Depth

A central tool for establishing the existence of the aforementioned local parametrization, we employ the product-of-exponentials map, defining _canonical coordinates of the second kind_ on the dynamical Lie group, a foundational tool in geometric control theory and variational quantum circuit design.

Given an ordered basis {_b_<sub>1</sub>_,...,b<sub>n</sub>_} of g (where _n_=dimg), this map is defined as

\(\varphi_\mathfrak{g}:\mathfrak{g}\rightarrow G,\varphi_\mathfrak{g}(x):=e^{x_1b_1}\cdots e^{x_nb_n},\) (30)

where \(x=\sum_{i=1}^nx_ib_i\in\mathfrak{g}\).

**Remark VI.1.** The map \(\varphi_\mathfrak{g}\) provides a factorized local parametrization around the identity in terms of a product of one-parameter subgroups, in contrast to the standard exponential map \(x\mapsto e^x\). By construction, \(\varphi_\mathfrak{g}\) maps the origin of the Lie algebra to the group identity, i.e., \(\varphi_\mathfrak{g}(0)=I\).

As a finite product of smooth exponential maps, \(\varphi_\mathfrak{g}\) is smooth. Furthermore, its differential at the origin is the identity transformation, \((d\varphi_\mathfrak{g})_0=\mathrm{id}_\mathfrak{g}\). By the Inverse Function Theorem, there exist open neighborhoods \(V_0\subseteq\mathfrak{g}\) containing 0 and \(U_{I,\varphi_\mathfrak{g}}\subseteq G\) containing _I_ such that

\(\varphi_\mathfrak{g}:V_0-\rightarrow^\cong U_{I,\varphi_\mathfrak{g}}\) (31)

is a smooth local diffeomorphism. Consequently, any element \(g\in U_{I,\varphi_\mathfrak{g}}\) can be uniquely factorized into the product form (30).

Following the framework of \[9, Section 2\], we represent elements of the open neighborhood \(U_{I,\varphi_\mathfrak{g}}\subseteq G\) (see (31)) in the parameterized circuit form as in (5). To analyze and bound the resulting circuit depth _L_, we leverage an ascending vector space filtration that stratifies g according to the minimal bracket depth required to generate its elements from the set of original generators **a**={_a_<sub>1</sub>_,...,a<sub>k</sub>_} of g (here we assume that the generators are linearly independent over R).

More precisely, let g be a finite-dimensional (real) Lie algebra presented by a set of generators. It is natural to organize the elements of g according to the minimum bracket depth required to generate them. This induces an ascending vector space filtration on g:

\(\{0\}=\mathcal{F}_0^\mathbf{a}\subseteq\mathcal{F}_1^\mathbf{a}\subseteq\mathcal{F}_2^\mathbf{a}\subseteq\cdots\subseteq\mathcal{F}_j^\mathbf{a}\subseteq\cdots\subseteq\mathfrak{g},\) (32)

defined recursively as follows.

• **Base layer:** the subspace spanned by the generators, \(\mathcal{F}_1^\mathbf{a}:=\mathrm{span}_\mathbb{R}\{a_1,\dots,a_k\}\).<tbc>

• **Higher layers:** \(\mathcal{F}_j^\mathbf{a}:=\mathcal{F}_{j-1}^\mathbf{a}+[\mathcal{F}_1^\mathbf{a},\mathcal{F}_{j-1}^\mathbf{a}]\) for \(j\ge 2\), which ensures the bracket compatibility condition

\([\mathcal{F}_{d_1}^\mathbf{a},\mathcal{F}_{d_2}^\mathbf{a}]\subseteq\mathcal{F}_{d_1+d_2}^\mathbf{a}.\) (33)

As g is finite-dimensional, this ascending filtration of subspaces must eventually stabilize at g. This allows us to formalize the notion of _stabilization depth_.

**Definition VI.2.** Let **a**={_a_<sub>1</sub>_,...,a<sub>k</sub>_} be a set of generators. The _stabilization depth_ of **a** is the minimal index at which the filtration sequence (32) stabilizes:

\(\mathcal{D}_\mathbf{a}:=\mathrm{min}\{j\in\mathbb{N}|\mathcal{F}_j^\mathbf{a}=\mathcal{F}_{j+1}^\mathbf{a}\}.\) (34)

Equivalently, D**<sub>a</sub>** is the minimal integer _j_ such that any Lie word of length greater than _j_ lies within the linear span of Lie words of length at most _j_.

To express every element \(g\in U_{I,\varphi_\mathfrak{g}}\subseteq G\) (see (31)) in the circuit form (5), we construct an ordered basis {_b_<sub>1</sub>_,...,b<sub>n</sub>_} of g from nested conjugates of the original generators **a**={_a_<sub>1</sub>_,...,a<sub>k</sub>_}. We initialize the construction by setting

\(b_i=a_i,1\le i\le k.\)

