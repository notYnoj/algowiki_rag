subsequences of length _w_ in **T**, ensuring no trivial matches between all possible pair of indices that are part of the motif pairs (i.e., no motif overlaps with another).

_Example 3.1._ Figure 1 reports an example of multidimensional motif discovery: readings of different sensors from an industrial evaporator [17]. We highlight the top-3 motifs of length _w=_75 and dimensionality _d=_2. Notice how the middle signal does not participate in the motifs.

## 3.2 Locality Sensitive Hashing

A powerful technique for approximate similarity search in high- dimensional space is Locality Sensitive Hashing (LSH for short), which we briefly introduce here. Given that the subsequences of length _w_ of a time series can be seen as vectors in R<sup>w</sup>, this will prove a useful tool in this setting as well. For an in-depth discussion of LSH, refer to [3, 39]. We provide, as online supplemental material, a short interactive LSH primer<sup>1</sup>.

Intuitively, LSH partitions a set of vectors randomly in such a way that close vectors are more likely to end in the same part than far away vectors. To formalize this intuition, the definition below introduces a distance threshold _R_: vectors that are closer to each other than _R_ are considered close, and vectors farther than _cR_ are considered far away.

**Definition 3.11** (Locality Sensitive Hashing [3])**.** Let (X, dist) be a metric space and H be a family of functions \(h:\mathcal{X}\rightarrow U\) for some set _U_. For a distance threshold _R_ and a constant _c\>_1 the family H is called (_R,cR,p_<sub>1</sub>_,p_<sub>2</sub>)_-locality sensitive_ if \(\forall x,y\in\mathcal{X}\) and for _h_ sampled from H:

\(\text{if dist}(x,y)\le R\text{then Pr}_{h\sim\mathcal{H}}\left[h\left(q\right)=h\left(p\right)\right]\ge p_1\text{if dist}(x,y)\ge cR\text{then Pr}_{h\sim H}\left[h\left(q\right)=h\left(p\right)\right]\le p_2.\) (3)

The event of two vectors having the same hash value is called a _collision_. A key quantity to assess the performance of LSH families is

\(\rho=\frac{log1/p_1}{log1/p_2}\)

A small \(\rho\) value entails that the LSH family is effective at discerning close vectors from far-away ones.

For the common case of the Euclidean distance considered in this paper a widely used LSH family is that of _Discretized Random Projections_ [14]. For a vector \(x\in\mathbb{R}^\text{w}\) and quantization parameter \(r\in\mathbb{R}^+\) the hash function is

\(h(x)=\left\lfloor\frac{a\cdot x+b}{r}\right\rfloor\) (4)

where \(a\in\mathbb{R}^\text{w}\) is a vector with random components following the N(0,1) Gaussian distribution, and \(b\in\mathbb{R}\) is chosen uniformly at random in the interval [0_,r_].

The probability that two vectors _x,y_ at Euclidean distance _R_ collide is:

\(Pr_{h\sim\mathcal{H}}\left[h(x)=h(y)\right]=1-2\cdot norm\left(-\frac{r}{R}\right)-\frac{2}{\sqrt{2\pi}r/R}\left(1-e^{-\left(\frac{r^2}{2R^2}\right)}\right)\) (5)

where _norm_ is the cumulative distribution function of a _Standard normal distribution_ [14]. For this family of LSH functions we have \(\rho=1/c\) [2], a fact that we will use in the analysis of the complexity of our algorithm.

As a notational shorthand, for two vectors _x_ and _y_ at distance dist (_x,y_) we define

\(P(\text{dist}\left(x,y\right))=Pr_{h\in\mathcal{H}}\left[h(x)=h(y)\right].\)

In order to _amplify_ the gap between the collision probability of close vectors (at distance \(\le R\)) and far vectors (at distance \(\ge cR\)) a common strategy is to create a _composite_ hash function by sampling _K_ hash functions and concatenating their outputs in a tuple of length _K_:

\(h'(x)=\langle h_1(x),h_2(x),\dots,h_K(x)\rangle\)

The resulting LSH family is \((R,cR,p_1^K,p_2^K)\)-locality sensitive. Using larger values of _K_ lowers the probability for both close and far points to collide, with a more marked effect on the latter. Repeating this process with _L_ independent composite hash functions implies that points at distance smaller than _R_ collide in at least one of the repetitions with probability at least \(1-\left(1-p_1^K\right)^L\).

Setting the parameters _K_ and _L_ requires the knowledge of the distance threshold _R_, which in our setting is the distance of the top-_k_ motif. Of course we do not know this distance beforehand, therefore in the following we describe an algorithm that automatically tunes them based on the input.

<sup>1</sup>https://www.dei.unipd.it/~ceccarello/MOMENTI-supplemental/



**Figure 1: Multidimensional time series from an industrial evaporator [17]. The top-3 two dimensional motifs are highlighted.**

