**Definition 6.1.** The _k_-CNF Satisfiability (_k_-SAT) problem takes as input a formula \(\phi\) with _m_ clauses and _n_ variables. The formula is in conjunctive normal form (CNF) which requires that the formula be the and of _m_ clauses. Each clause is the or of at most _k_ variables. Return true if \(\phi\) has a satisfying assignment and false otherwise.

**Definition 6.2** (The strong exponential time hypothesis (SETH) \[IP01\])**.** For all constants \(\epsilon>0\) there is some constant _k_ such that _k_-SAT requires \(\omega(2^{n(1-\epsilon)})\) time.

We can re-frame this as _k_-SAT requiring 2<sup>_n_(1-_o_(1))</sup> time, as long as _k_ is an arbitrarily large constant. Next we define the _k_-OV problem.

**Definition 6.3** (_k_-OV \[Wil07\])**.** Take as input a list, _L_, of _n_ zero one vectors of dimension _d=n_<sup>_o_(1)</sup>. Return true if there are _k_ vectors \(v_i\in L\) for \(i\in[1,k]\) such that for all \(jv_1[j]\cdot v_2[j]\cdots v_k[j]=0\).

The _k_-OV hypothesis states that for constant _k_, _k_-OV requires _n_<sup>_k-o_(1)</sup> time. The _k_-OV hypothesis is implied by SETH.

We use the _k_-OV hypothesis to generate our lower bounds. As the _k_-OV hypothesis is implied by SETH, SETH also implies our lower bounds.

## _k_-LCS lower bound

Assuming the well-studied Strong Exponential Time Hypothesis (SETH), in Section 6.2 we show a lower bound for the _k_-LCS problem in the compressed setting. Intuitively, SETH states that CNF-satisfiability requires 2<sup>_n-o(n_)</sup> time \[IP01\]. Even more specifically, we use the _k_-Orthogonal Vectors problem (_k_- OV) \[Vas18\]. At a high level, _k_-OV takes as input a list _L_ with _n_ zero-one vectors of dimension _d_. We must return YES if there exist _k_ vectors that, when multiplied element-wise, form the all zeros vector. The _k_-OV conjecture, which is implied by SETH, states that _k_-OV cannot be solved in \(O(n^{k-\Omega(1)})\) time.

**Reminder of Theorem 1.1.** _If the_ \(k'\)_-OV hypothesis is true for all constants_ \(k'\)_, then for any constant_ \(\epsilon\in(0,1]\) _grammar-compressed k-LCS requires_ \(\left(M^{k-1}m\right)^{1-o(1)}\) _time when the alphabet size is_ \(|\Sigma|=\Theta(k)\) _and_ \(m=M^{\epsilon\pm o(1)}\)_. Here, M denotes the total length of the k input strings and m is their total compressed size._

Our lower bound relies on two primary tools. First, we use a very compressible representation of _a_-OV instances. Specifically, given a list _L_ of _n_ zero-one vectors of dimension _d_, consider a new list **List**(_L)<sub>a</sub>_ of _n<sup>a</sup>_ zero-one vectors of dimension _d_, with every vector in **List**(_L)<sub>a</sub>_ representing the element wise multiplication of _a_ vectors from _L_. Formally, **List**(_L)<sub>a</sub>_ is indexed by _a_-tuples of indices from \[1_..n_\], and each vector \(\vec{v}=\mathbf{List}(L)_a[j_1][j_2]\cdots[j_a]\) is defined, for every coordinate \(i\in[1..d]\), with:

\(\mathbf{List}(L)_a[j_1][j_2]\cdots[j_a][i]=\vec{v}[i]=L[j_1][i]\cdot L[j_2][i]\cdots L[j_a][i]\)

Notably, **List**(_L)<sub>a</sub>_ contains an all zeros vector if and only if _L_ is a YES-instance of the _a_-OV problem.

In the 2-LCS lower bound of \[ABBK17\], an (_a_+2_b_)-OV instance _L_ is first transformed into _A_=**List**(_L)<sub>a</sub>_, _B_=**List**(_L)<sub>b</sub>_, and _C_=**List**(_L)<sub>b</sub>_. Then, the following strings are defined for every \(\vec{v}_b\in B\) and \(\vec{v}_c\in C\):

\(x_{\vec{v}_b}=\underbrace{v_{a_1}^{\vec{v}_b}[1]\vec{v}_b[1]v_{a_2}^{\vec{v}_1}[1]\vec{v}_b[1]\cdots v_{a_{n^a}}^{\vec{v}_b}[1]\vec{v}_b[1]}_{\text{first bit}}\cdots\underbrace{v_{a_1}^{\vec{v}_b}[d]\vec{v}_b^{\vec{v}_1}[d]v_{a_2}^{\vec{v}_2}[d]\vec{v}_b[d]\cdots v_{a_{n^a}}^{\vec{v}_b}[d]\vec{v}_b[d]}_{\text{dth bit}},\)<br>
\(y_{\vec{v}_c}^{\vec{v}_c}=\vec{v}_c[1]\underbrace{0000000}_{n^a-1}\vec{v}_c[2]\cdots\underbrace{0000000}_{n^a-1}\vec{v}_c[d].\)

The string \(x_{\vec{v}_b}\) that interleaves \(\vec{v}_b\) with bits of _n<sup>a</sup>_ vectors \(v_{a_i}^{\vec{v}_i}\in A\), referred to as "interleaved" representation, is highly compressible, to an SLP of size _O(nd_). Moreover, if there exists a vector \(v_{a_i}^{\vec{v}_i}\in A\) such that \((v_{a_i}^{\vec{v}_i},\vec{v}_b^{\vec{v}_c})\) is orthogonal, Abboud et al. \[ABBK17\] show (using the structural alignment gadget of \[BK15\]) how to perfectly align \((v_{a_i}^{\vec{v}_i}[l],\vec{v}_b^{\vec{v}_i}[l],\vec{v}_c^{\vec{v}_c}[l])\) for all \(l\in[1..d]\). Finally, the gadgets \(x_{\vec{v}_b}\) for all \(\vec{v}_b\in B\) are concatenated with extra padding to generate _X<sub>B</sub>_, and the gadgets \(y_{\vec{v}_c}^{\vec{v}_c}\) for all \(\vec{v}_c\in C\) are concatenated with extra padding to generate _Y<sub>C</sub>_. This leads to the (_Mm_)<sup>1-_o_(1)</sup> lower bound since the uncompressed and compressed lengths of _X<sub>B</sub>_ and _Y<sub>C</sub>_ are (roughly) _O(n_<sup>_a+b_</sup>) and _O(n<sup>b</sup>_), respectively, and we are solving an (_a_+2_b_)-OV instance.

We may extend the above construction to the compressed _k_-LCS setting by transforming an (_a+kb_)- OV instance _L_ into lists _A_=**List**(_L)<sub>a</sub>_, _B_=**List**(_L)<sub>b</sub>_, and _C<sub>h</sub>_=**List**(_L)<sub>b</sub>_ for \(h\in[1..k-1]\). We then create _X<sub>B</sub>_ and _Y<sub>C<sub>h</sub></sub>_ for \(h\in[1..k-1]\). Since the strings _Y<sub>C<sub>h</sub></sub>_ are zero-padded, we can easily adapt the<tbc>

