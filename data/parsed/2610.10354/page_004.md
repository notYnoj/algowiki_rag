(3) Then, suppose that we aim to design a fine-grained reduction from _P_ to some other problem _Q_. Given any instance of _P_, we first repeatedly extract structured subinstances, and solve these subinstances with the fast algorithm from step 2. Once there is no more structured subinstance, we regard the remaining instance as _pseudo-random_, and exploit the pseudo- randomness in the reduction to _Q_.

Of course, successfully implementing this approach hinges crucially on the choice of the structure notion. It has to be weak enough so that structured instances can be solved efficiently, but strong enough so that the corresponding pseudo-random instances can be exploited in the reduction.

In Fischer’s setup, _P_ is the APSP problem (or rather, for technical reasons, the equivalent _Min- Plus Product_ problem), and the relevant notion of structure is a matrix rank parameter known as _select-plus rank_<sup>2</sup>. A major technical contribution is a fast algorithm for instances of low rank, from which the universe reduction and further lower bounds follow via the general framework.

Let us return to Min-Plus Convolution. As the analogy to Min-Plus Product is strong, a priori one may hope that Fischer’s techniques can be extended to Min-Plus Convolution without too much difficulty. However, our situation is quite the exception. Obtaining the analogous results for Min-Plus Convolution poses several substantially new obstacles that are not present in the matrix world. First, it is entirely unclear what the appropriate notion of structure should be for sequences or sets. This naturally falls into the realm of additive combinatorics; however, any such notion must capture _extremely weak_ additive structure, far from the commonly used strong structure measures. This leads to a second major challenge: the existing tools from additive combinatorics are not well suited for this regime, and we need to invent our own structural results. All in all, our route involves three steps, each of which is interesting in its own right:

• We develop a new additive structure theorem that can be viewed as a "higher-order" substitute of the Balog-Szemerédi-Gowers theorem (Section 1.2).<tbc>

• We then identify the appropriate structure notion, called _rank_ in analogy to \[Fis26\], and show that low-rank instances of Min-Plus Convolution can be solved in subquadratic time, based on the new structure theorem. In fact, we directly work with the harder 3SUM problem (Section 1.3).<tbc>

• Equipped with this new algorithm, we derive the aforementioned universe reduction and strong lower bounds from Min-Plus Convolution in analogy to Fischer’s proof (Sections 1.4 and 1.5).

## 1.2 A New Additive Structure Theorem

Using additive combinatorics in fine-grained algorithm design and complexity is an exciting recent trend \[CL15, BW21, BN20, BN21, ABF23, JX23, CVX23, Jin24, Bri24, CLMZ24, BFN25, FJX25, AFJ<sup>+</sup>25, CMZ26, Fis26\]. This was pioneered by Chan and Lewenstein \[CL15\], who introduced the celebrated Balog-Szemerédi-Gowers (BSG) Theorem to our community, and derived various strong algorithmic consequences of it. The BSG Theorem has since found many more applications \[CL15, ABF23, JX23, CVX23, FJX25, AFJ<sup>+</sup>25\], notably also in Fischer’s work \[Fis26\], and became an important part of the fine-grained toolkit. To understand both the strengths and the limitations<tbc>

<sup>2</sup>The _select-plus rank_ of an \(n\times n\) integer matrix _A_ is the smallest number _r_ such that there exist matrices _U,V_ of sizes \(n\times r\) and \(r\times n\), respectively, so that \(A[i,j]\in\bigcup_{k=1}^r\{U[i,k]+V[k,j]\}\).

