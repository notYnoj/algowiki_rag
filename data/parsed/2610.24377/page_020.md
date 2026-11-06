We can use _O(k_log_n_) bits of additional clean space, with no asymptotic time or catalytic space loss, to _find_ the _k_-length cycle or path, not just detect it.<sup>16</sup>

## 5 Time-Space Tradeoff Lower Bounds

We now discuss how the above algorithmic results relate to time-space tradeoff _lower bounds_. Although our algorithms are stated in an output model that involves XORing into the dirty tape, we show that we can instead describe them in separate-tape-output models, where existing lower bounds imply that dirty space is provably necessary for fast algorithms.

### 5.1 Separating catalytic and non-catalytic time-and-space-bounded complexity

Recall that our catalytic algorithms are stated in the _dirty-XOR_ output model. We observe that they could equivalently be stated in the 2-output-pass output model with no asymptotic loss in space or runtime.

**Lemma 5.1.** Assume there exists a clean space _S_, catalytic space _C_, and time _T_ algorithm _A_ which computes \(f=f_n:\{0,1\}^n\rightarrow\{0,1\}^m\) in the dirty-XOR output model. Then, there exists a clean space _O(S_), dirty space _C_, time _O(T_) algorithm which given _x_ outputs _f(x_) on a 2-pass XOR output tape.

_Proof._ First, output the first _m_ bits of the catalytic tape. Then, simulate _A_ to completion. XOR in the new first _m_ bits of the catalytic tape in a second pass. Finally, simulate _A_ a second time in order to reset the dirty space.

We then show that, for algorithms without catalytic space, the 2-output-pass XOR output model is equivalent to the transducer (i.e., 1-pass) output model. In fact, the proof of Lemma 5.2 below also applies to a modified _k_-output-pass model where _both_ XOR-into and overwrite instructions are allowed.

**Lemma 5.2.** Let \(k\in\mathbb{N}\) be a constant. Given any space _S_, time _T_ algorithm _A_ which outputs \(f=f_n:\{0,1\}^n\rightarrow\{0,1\}^\star\) in the _k_-output-pass output model, there exists a space _O(kS_), time _O(T_) algorithm which computes _f_ in a single pass.

_Proof._ First, simulate _A_, ignoring its outputs. Every time _A_ begins a new pass, record its full configuration. We will thus record _k_ distinct configurations, each of which takes _O(S_) space to write down. Given these configurations, we now proceed in parallel: simulate each of them until they output their first bit, then XOR all of those bits together and output them. Proceed likewise for the second bit, and so on.

There are known \(\Omega(n^2)\) time-space-product lower bounds on DFT and sorting, and \(\Omega(n^3)\) time-space-product lower bounds on matrix multiplication, in the transducer model. By Lemma 5.2, these lower bounds also apply to the 2-output-pass output model. So, since catalytic algorithms can achieve time-clean space product _n_<sup>1+_o_(1)</sup> and \(n^{\omega+o(1)}\), respectively, in this model, this shows that dirty space is unconditionally helpful.

We also note that we can make a similar statement in the transducer model:

**Proposition 5.3.** There exists some relation \(R\subseteq\{0,1\}^*\times\{0,1\}^*\) such that,

• there exists a 1-output-pass catalytic algorithm using clean space _O_(log(_n_)), dirty space poly(_n_), and time _n_<sup>1+_o_(1)</sup>, which takes in \(x\in\{0,1\}^n\) and outputs some _y_ such that \((x,y)\in R\), but<tbc>

<sup>16</sup>As we iterate over each of the hash functions, stop when it is found that a cycle (resp. path) exists, and store the corresponding hash function. At least one of the cycles (resp. paths) of _G_ will be colorful. Now, we follow essentially the same approach as the cliques search to decision reduction. Brute-force all 2<sup>_k_+1</sup> possibilities for the _j_<sup>th</sup> bit of the nodes in each color until one of them keeps the invariant that a cycle (resp. path) exists, continuing with _j_ until all bits are filled in. This increases the runtime by a 2<sup>_O(k_)</sup> factor, and maintains the same asymptotic time (and catalytic space) complexity as Corollaries 4.14 and 4.15.

