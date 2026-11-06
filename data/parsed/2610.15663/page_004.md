### Proof idea.

We first construct a small matrix multiplication rule in which outputs use six products from the same shared collection minus one private product per output. We apply this rule recursively to blocks of larger matrices, following only the intermediate entries needed for the requested outputs. We count these requests by their pattern of private and shared steps. Each shared step generates at most six requests per incoming request, but the count is capped by the total number of output positions in the corresponding products. The base case is an outer product, whose requested entries each require one multiplication. Padding the input dimensions lets us apply this count directly to the given matrices.

## 2.1 The multiplication rule

For a matrix product _UV_ , call _U_ the left input and _V_ the right input. A _product of linear forms_ multiplies an integer linear combination of entries of _U_ by an integer linear combination of entries of _V_ . We count the additions and subtractions needed to form these combinations separately from their multiplication.

**Lemma 2.3** (A shared multiplication rule)**.** _Let_ \(k\ge 2\) _and set R=k_2<sup>_k_-1</sup> _and S_=3<sup>_k_-1</sup>_. We construct a multiplication rule for matrices_ \(U\in\mathbb{Z}^{R\times 2}\) _and_ \(V\in\mathbb{Z}^{2\times S}\) _as follows:_

1. **_Products:_** _There is a common collection of_ 6_<sup>k</sup>_ shared _products and one_ private _product for each entry of UV_.<tbc>

2. **_Linear forms:_** _Every product multiplies a linear form in U by a linear form in V. Each form is a sum of at most_ 6_k signed entries of its respective matrix._<tbc>

_3._ **_Reconstruction:_** _Each entry of UV is the sum of six shared products minus its private product._

We count products by their labels, even if two formulas happen to be identical. The multiplication has _RS=k_6<sup>_k_-1</sup> outputs, but only 6_<sup>k</sup>_ shared products. Thus

\(\frac{\text{number of shared products}}{\text{number of outputs}}=\frac{6^k}{RS}=\frac{6}{k}.\)

As _k_ increases, the shared collection becomes small relative to the number of outputs. This is the reuse that our recursive algorithm will exploit.

### A cancellation identity.

The construction follows the Schönhage-Coppersmith approach used by Alman and Vassilevska Williams \[1\]. We first give a cancellation identity, then construct shared linear forms whose restriction to each output has exactly this pattern. The identity is the \(2\times 3\) instance of Schönhage’s inner/outer-product cancellation \[2\].

For the desired dot product _p_<sub>1</sub>_q_<sub>1</sub>+_p_<sub>2</sub>_q_<sub>2</sub>, we add a third coordinate with _p_<sub>3</sub>=0 and _q_<sub>3</sub>=-_q_<sub>1</sub>-_q_<sub>2</sub>. The first relation preserves the dot product, while the zero sum of the _q<sub>j</sub>_ cancels a mixed term. The remaining unwanted terms are removed by one private product. Figure 1 illustrates the identity.

**Claim 2.4** (Cancellation)**.** _Let x_<sub>1</sub>_,x_<sub>2</sub>_,p_<sub>1</sub>_,p_<sub>2</sub> _be left variables and y_<sub>1</sub>_,y_<sub>2</sub>_,y_<sub>3</sub>_,q_<sub>1</sub>_,q_<sub>2</sub> _be right variables. Put p_<sub>3</sub>=0 _and q_<sub>3</sub>=-_q_<sub>1</sub>-_q_<sub>2</sub>_. Then_

\(\sum_{j=1}^3[(x_1+p_j)(y_j+q_j)+(x_2-p_j)y_j]-(x_1+x_2)(y_1+y_2+y_3)=p_1q_1+p_2q_2.\) (4)

