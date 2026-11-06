Bringmann \[6\], which runs in \(\widetilde{O}(n+t)\) time. An alternative randomized algorithm with almost the same running time is given by Jin and Wu \[20\].

### 1.4 Paper Outline

In Section 2, we introduce necessary terminology and preliminaries. In Section 3, we prove two exchange arguments that are crucial to our algorithms. In Section 4, we present a simpler algorithm to illustrate our main idea. The \(\widetilde{O}(n+w_\mathrm{max}^{12/5})\)-time algorithm for Knapsack is presented in Section 5. In Section 6, we give two algorithms for Subset Sum. Omitted proofs can be found in the appendix.

## 2 Preliminaries

### 2.1 Notation

We use I={1_,...,n_} to denote the set of all items, each with weight _w<sub>i</sub>_ and profit _p<sub>i</sub>_. We assume that items are labeled in decreasing order of efficiency. That is, \(p_1/w_1\ge\dots\ge p_n/w_n\). Item _i_ has _u<sub>i</sub>_ copies. Let \(W=\{w_i:i\in\mathcal{I}\}\) be the set of all item weights. The maximum weight is denoted by _w_<sub>max</sub>.

Let _i_ be some item. We denote the set of item {1_,...,i_-1} as I_<sub>\<i</sub>_ and {_i,...,n_} as \(\mathcal{I}_{\ge i}\). Let _i_ and _j_ be two items with _i\<j_, we say _i_ is to the left of _j_, and _j_ is to the right.

For \(w\in W\), we denote the set of items with weight _w_ as

\(\mathcal{I}^w=\{i\in\mathcal{I}:w_i=w\}.\)

For any subset \(W'\) of _W_, we write \(\bigcup_{w\in W^\prime}\mathcal{I}^w\) as \(\mathcal{I}^{W^\prime}\). We also write \(\mathcal{I}^{W^\prime}\cap\mathcal{I}_{<i}\) as \(\mathcal{I}_{<i}^{W^\prime}\), and \(\mathcal{I}^{W^\prime}\cap\mathcal{I}_{\ge i}\) as \(\mathcal{I}_{\ge i}^{W^\prime}\). Basically, the superscript restricts the weights of items in the set, while the subscript restricts the indices.

For any subset \(\mathcal{I}'\) of items, we refer to the multiset \(\{w_i:i\in\mathcal{I}'\}\) as the weight multiset of \(\mathcal{I}'\).

A solution to Bounded Knapsack can be represented by a vector **x** where _x<sub>i</sub>_ is the number of selected copies of item _i_.

### 2.2 The Previous Proximity Result

Let **g** be a maximal prefix solution that can be obtained greedily as follows. Starting with an empty knapsack, we process items in increasing order of index (i.e., in decreasing order of efficiency). If the knapsack has enough room for all copies of the current item, we select all these copies, and process the next item. Otherwise, we select as many copies as possible, and then stop immediately. The item at which we stop is called the _break item_, denoted by _b_. Without loss of generality, we assume that no copies of the break item _b_ are selected by **g** (i.e., _g<sub>b</sub>_=0). If \(g_b\neq 0\), we can view those copies selected by **g** as a new item \(i'\) with \(u_{i^\prime}=g_b\), and set _u<sub>b</sub>=u<sub>b</sub>-g<sub>b</sub>_. It is easy to observe that _g<sub>i</sub>=u<sub>i</sub>_ for all _i\<b_ and that _g<sub>i</sub>_=0 for all \(i\ge b\).

The following proximity result states that there is an optimal solution **z** that differs from **g** only in a few items.

Lemma 2.1. (\[16, 26\]) _Let_ **g** _be a maximal prefix solution of Knapsack. There exists an optimal solution_ **z** _such that_<tbc>

\(\|\mathbf{z}-\mathbf{g}\|_1=\sum_{i=1}^n\left|z_i-g_i\right|\le 2w_\mathrm{max}.\)

<tbc>Throughout the rest of the paper, we fix **g** to be a maximal prefix solution and **z** to be an optimal solution that minimizes \(\|\mathbf{z}-\mathbf{g}\|_1\). For any subset \(\mathcal{I}'\) of items, we define the weighted \(\ell_1\)-distance from **g** to **z** on \(\mathcal{I}'\) to be

\(\Delta(\mathcal{I}')=\sum_{i\in\mathcal{I}^\prime} w_i|g_i-z_i|.\)

### 2.3 Proximity-based (min,+)-Convolution Framework

Both the algorithm of Polak et al. \[26\] and our algorithm use the proximity-based (min,+)-convolution framework. We present a general form of the framework through the following Lemma. Recall that _W_ is the set of all item weights.

Lemma 2.2. _Let_ **g** _be a maximal prefix solution to Bounded Knapsack. Let_ \(W_1\cup\cdots\cup W_k\) _be a partition of the set W. For_ \(j\in\{1,\dots,k\}\)_, let U<sub>j</sub> be an upper bound for_ \(\Delta(\mathcal{I}^{W_j})\)_. Then Bounded Knapsack can be solved in_ \(\widetilde{O}(n+k\sum_{j=1}^k\left|W_j\right|\cdot U_j)\) _time._

We only give a sketch of the proof. The complete proof is deferred to Appendix A.

