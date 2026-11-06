## 4 The Algorithm

We present an algorithm that colors _k_-colorable graphs online with _O(k_<sup>3</sup>log<sup>2</sup>_k_log<sup>4</sup>_n_) colors in the random-order model. The intuition is already given in Subsection 1.5. Note that, in the subsequent sections, we use _G_=(_V,E_) to denote the current graph for the algorithm and _G_<sup>∗</sup>=(_V_<sup>∗</sup>_,E_<sup>∗</sup>) to denote the final graph, as in Definition 5.

### 4.1 Basic Strategy

We consider developing an algorithm that colors the last _n/_2 vertices using _O(k_<sup>3</sup>log<sup>2</sup>_k_log<sup>3</sup>_n_) colors, given that the first _n/_2 vertices have already arrived and have been colored. If this can be done, we can recursively apply the same algorithm to the first _n/_2 vertices. Then, we can color the entire graph with _O(k_<sup>3</sup>log<sup>2</sup>_k_log<sup>4</sup>_n_) colors.

However, for convenience in the analysis, we do not exactly divide them into _n/_2 vertices each. Instead, we sample _m_ from a binomial distribution \(\mathsf{Binomial}(n,\frac{1}{2})\), and we color the last _n-m_ vertices, given that the first _m_ vertices have already arrived. We note that _m_ is very close to _n/_2 (with \(\pm\widetilde{O}(\sqrt{n})\) error), so this does not fundamentally change the algorithm. We use disjoint colors for the first _m_ vertices and the last _n-m_ vertices. Let _S_ be the set of the first _m_ vertices. Under this framework, \(S\subseteq V^*\) is uniformly distributed over the 2_<sup>n</sup>_ subsets of _V_<sup>∗</sup>, as shown below.

**Lemma 13.** _Let_ \(m\sim\mathsf{Binomial}(n,\frac{1}{2})\)_. Let S be the set of the first m vertices. Then, each subset of V_<sup>∗</sup> _appears as S with probability exactly_ 2<sup>-_n_</sup>.

_Proof._ The probability that |_S|=m_ is \(2^{-n}\cdot\genfrac(){pt}{2}{n}{m}\) by the binomial distribution. Also, there are \(\genfrac(){pt}{2}{n}{m}\) possible subsets of _V_<sup>∗</sup> with size _m_, and all of them have equal probabilities of appearing as _S_ because of the random-order model. Hence, Lemma 13 holds. □

### 4.2 Algorithm Details

Now, we consider an algorithm to color the last _n-m_ vertices _V_<sup>∗</sup>\\_S_. The algorithm consists of two phases: (1) the _learning phase_, which learns and extracts the structure of the first _m_ vertices, and (2) the _output phase_, which actually colors the last _n-m_ vertices by exploiting the learned structure. The two phases are described as follows.

#### (1) The Learning Phase.

The core idea is that, if we sample an independent set \(I\subseteq S\), many vertices in _V_<sup>∗</sup>\\_S_ are likely to have no neighbor in _I_ thanks to the random arrivals (Subsection 1.5). Such a set of vertices can be colored efficiently, as we prove in Section 5. However, a single sampled independent set _I_ does not cover all vertices in _V_<sup>∗</sup>\\_S_. Therefore, we need to sample multiple independent sets.

In the algorithm, we sample a sequence of independent sets _I_<sub>1</sub>_,I_<sub>2</sub>_,..._, each from a hierarchy \((S=)A_1\unknown A_2\unknown\cdots\) . We start with _A_<sub>1</sub>=_S_. For _i_=1,2_,..._ in this order, we sample an independent set _I<sub>i</sub>_ from \(\mathsf{IS}_\lambda(G[A_i])\), and then we let _A_<sub>_i_+1</sub>:=_N<sub>A<sub>i</sub></sub>(I<sub>i</sub>_). See Figure 6 for an example. Eventually, _I<sub>i</sub>_ becomes empty; we let _r_ be the first index such that \(I_r=\emptyset\). When coloring the remaining _n-m_ vertices, we use independent sets _I_<sub>1</sub>_,...,I<sub>r</sub>_. It can be proven that _r=O(k_log_k_log_n_) with high probability (Lemma 16), regardless of the value of the parameter \(\lambda\in(0,1]\).

