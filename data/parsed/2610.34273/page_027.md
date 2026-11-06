_Proof._ Every polynomial multiplication tensor is nonzero, and a spectral point has value at least one on a nonzero tensor. Thus each factor in the definition of \(P_\phi\) is positive, and so is \(P_\phi\).

Let \(\sigma\) permute the first _n_-1 tensor legs and fix leg _n_. By the defining coefficient formula, permuting the input lengths of C_<sub>n</sub>_ by \(\sigma\) gives \(\sigma\mathcal{C}_n\). The map \(\pi\mapsto\pi\sigma\) is a bijection of _S<sub>n</sub>_. Hence replacing C_<sub>n</sub>_ by \(\sigma\mathcal{C}_n\) reindexes the factors defining \(P_\phi\) and does not change their product. This proves symmetry.

The tensor \(\mathcal{C}_n(1,\dots,1,b)\) equals \(E_{n-1,n}^{(b)}\). Using (2), we obtain<tbc>

\(P_\phi(1,\dots,1,b)=\left(\prod_{\pi\in S_n}b_{n-1,n}^{p_{n-1,n}^{(\phi_\pi)}}\right)^{1/(n!t_\phi)}=b.\)

<tbc>For the upper bound, a spectral point is at most tensor rank, and tensor rank is unchanged by a permutation of the legs. Thus Lemma 4.2 gives, for every \(\pi\in S_n\),

\(\phi_\pi\big(\mathcal{C}_n(a_1,\dots,a_{n-1})\big)\le 1+\sum_{j=1}^{n-1}(a_j-1).\)

There are _n_! factors in the profile. Multiplying their bounds and then taking the power \(1/(n!t_\phi)\) proves the result.

**Remark 4.7.** The profile \(P_\phi\) is a numerical function of input lengths. The geometric mean defining it is not asserted to be a spectral point. In the next two subsections, every tensor comparison is applied separately to each \(\phi_\pi\); only the resulting numerical inequalities are multiplied together.

## 4.2 Discrete concavity

The first comparison concerns three consecutive values of one input length. We will retain a quotient part and a kernel part of a doubled multiplication tensor. Both parts use the same coordinates on the first _n_-2 input legs, so Corollary 3.2 applies to them. This construction and the shifted tripling construction in Subsection 4.3 extend the determinant filtration and three-sector decomposition of OpenAI \[Ope26a, Section 4\]. Averaging their spectral inequalities over all leg permutations gives inequalities for the profile from Subsection 4.1.

The following inequality extends \[Ope26a, Lemma 4.1\]. We give the coordinate action of the kernel and quotient maps explicitly, so that their compatibility with every tuple of shared inputs can be checked without combining those inputs into one leg.

**Lemma 4.8** (discrete concavity)**.** _Let_ \(n\ge 3\) _be an integer, let_ \(\phi\in\Phi_n\)_, and let_ \(P_\phi\) _be the profile in Definition 4.5. For all positive integers a_<sub>1</sub>_,...,a_<sub>_n_-2</sub> _and every integer_ \(b\ge 2\),

\(2P_\phi(a_1,\dots,a_{n-2},b)\ge P_\phi(a_1,\dots,a_{n-2},b+1)+P_\phi(a_1,\dots,a_{n-2},b-1).\)

_By symmetry, the same inequality holds in every input coordinate._

_Proof._ Put \(S=\sum_{j=1}^{n-2}(a_j-1)\). For every integer \(e\ge 0\), let _V<sub>e</sub>_ be the vector space of homogeneous polynomials of degree _e_ in the variables _u,v_, with ordered basis \((u^{e-i}v^i)_{i=0}^e\). The coefficient vector of \(\sum_{i=0}^ec_ix^i\) is thus also the coefficient vector of \(\sum_{i=0}^ec_iu^{e-i}v^i\). Multiplication of these homogeneous forms has the same coefficient tensor as univariate polynomial multiplication.

