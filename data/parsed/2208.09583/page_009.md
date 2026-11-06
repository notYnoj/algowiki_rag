2. For the obtained totally ordered matroids \(M_1^*\), \(M_2^*\), an \((M_1^*,M_2^*)\)-kernel _A_<sup>∗</sup> is computed.<tbc>

3. The algorithm returns a set _A_ that is the projection of _A_<sup>∗</sup> to the original ground set _S_.

The first step can be done in O(|_S_|<sup>2</sup>) time as explained later, and the second step can be done in O(|_S_|<sup>2</sup>) time using Fleiner’s algorithm, which we will briefly describe later.

Here, we explain the precise construction of the totally ordered matroids \(M_1^*\) and \(M_2^*\). Let the extended ground set be \(S^*:=\cup_{u\in S}\{x_u,y_u,z_u\}\). We define \(M_i^*=(S^*,\mathcal{I}_i^*,\succ_i^*)\) for _i_=1,2 as follows. The elements _x<sub>u</sub>,y<sub>u</sub>,z<sub>u</sub>_ are parallel in each \(M_i^*\), that is,<tbc>

\(\mathcal{I}_i^*=\{I^*\subseteq S^*:\pi(I^*)\in\mathcal{I}_i,|I^*\cap\{x_u,y_u,z_u\}|\le 1(\forall u\in S)\},\)

<tbc>where \(\pi(I^*)=\{u\in S:I^*\cap\{x_u,y_u,z_u\}\neq\emptyset\}\). It is easy to see that \((S^*,\mathcal{I}_i^*)\) is a matroid for _i_=1,2. To define the total order \(\succ_1^*\) on the extended ground set _S_<sup>∗</sup>, we first define a binary relation \(\mathcal{R}_1^*\subseteq S^*\times S^*\) using \(\succ_1\) as follows:

\(\mathcal{R}_1^*=\{(x_u,z_w):u,w\in S\}\)<br>
\(\cup\{(y_u,x_w),(y_u,y_w),(y_u,z_w):u,w\in S,u\succ_1w\}\)<br>
\(\cup\{(x_w,y_u):u,w\in S,u\unknown\succ_1w\}.\)

To define \(\succ_2^*\), we define \(\mathcal{R}_2^*\) from \(\succ_2\) as follows, which is described in the same manner as \(\mathcal{R}_1^*\) but the roles of _x<sub>u</sub>_ and _z<sub>u</sub>_ are interchanged.

\(\mathcal{R}_2^*=\{(z_u,x_w):u,w\in S\}\)<br>
\(\cup\{(y_u,z_w),(y_u,y_w),(y_u,x_w):u,w\in S,u\succ_2w\}\)<br>
\(\cup\{(z_w,y_u):u,w\in S,u\unknown\succ_2w\}.\)

For each _i_=1,2, we let \(\succ_i^*\) be an arbitrary total order on _S_<sup>∗</sup> such that \(s\succ_i^*t\) holds for any \((s,t)\in\mathcal{R}_i^*\). The existence of such a total order is guaranteed by the following lemma.

**Lemma 9.** _Let D<sub>i</sub> be a digraph with vertex set S_<sup>∗</sup> _such that D<sub>i</sub> has an arc_ \((s,t)\in S^*\times S^*\) _if and only if_ \((s,t)\in\mathcal{R}_i^*\)_. Then D<sub>i</sub> is acyclic._

The proof of this lemma, which uses the fact that \(\succ_i\) is an interval order, is postponed to the end of this section. We now complete the construction of the new instance.

Since the digraph _D<sub>i</sub>_ is acyclic and has O(|_S_|<sup>2</sup>) arcs, we can define a total order \(\succ_i^*\) on _S_<sup>∗</sup> consistent to _D<sub>i</sub>_ by topological sort in O(|_S_|<sup>2</sup>) time. This \(\succ_i^*\) indeed satisfies the required condition, i.e., \(s\succ_i^*t\) holds for any \((s,t)\in\mathcal{R}_i^*\). This completes the construction of the totally ordered matroids \(M_1^*\) and \(M_2^*\).

For completeness, here we describe how Fleiner’s algorithm works for our new instance \(M_1^*\) and \(M_2^*\). The algorithm first sets _R_ to be an empty set and repeats the following three steps: set _X_ to be the optimal base of \(M_1^*\) with the ground set restricted to _S_<sup>∗</sup>\\_R_, set _Y_ to be the optimal base of \(M_2^*\) with the ground set restricted to _X_, and update _R_ with \(R\cup(X\backslash Y)\). The repetition stops if _Y=X_, and _Y_ is returned, which is an \((M_1^*,M_2^*)\)-kernel (see \[4\] for this version of the description).

Here, we show that the output of the algorithm is indeed a matroid kernel (i.e., a stable common independent set) in the original instance. The approximation ratio is shown in the next section. We use \(C_I^1(u)\) and \(C_I^2(u)\) to denote fundamental circuits in _M_<sub>1</sub> and _M_<sub>2</sub>, respectively.

**Lemma 10.** _The output of our algorithm is an_ (_M_<sub>1</sub>_,M_<sub>2</sub>)_-kernel._

