### Setup.

For simplicity, here, we assume that the input integer bound/modulus _M=pqr_, where \(2^{n-1}\le M\le 2^n\), \(p,q\in[2^{n/4-1},2^{n/4}]\), and _p_, _q_, and _r_ are pairwise co-prime integers. Refer to Problem 6 and 7 for the formal definition of the problems. We will investigate the case of unstructured \(M\neq pqr\) in detail in the main section.

From now on, we will only use the variable **a** for both cases. From the context, the reader can understand the support of the variables.

A natural question is why we do not work directly with a modulus of the form _M=pq_. The reason lies in the complexity of the different levels of our algorithm (see below), which is proportional to the sizes of the integers _p_ and _q_ used in the filtering steps. To balance this complexity, the modulus must contain two distinct prime factors of size approximately _M_<sup>1/4</sup>. The remaining factor, denoted by _r_, accounts for the rest of the modulus. Moreover, requiring the factors to be pairwise coprime is essential to apply the Chinese Remainder Theorem.

### Filtering Algorithm.

The algorithm behind Theorem 1.3 and Theorem 1.4 has two levels. First, we start by partitioning the input elements into four equal blocks of size _n/_4, and then enumerating all subset sums inside each block. Let _L_<sub>1</sub>_,L_<sub>2</sub>_,L_<sub>3</sub>, and _L_<sub>4</sub> denote these four lists consisting of 2<sup>_n/_4</sup> elements. We merge these four lists to store subsets that collide over low-order bits.

Formally, at the first level, we merge lists _L_<sub>1</sub> and _L_<sub>2</sub> to get a list _L_<sub>12</sub> such that this list contains all the subsets of the first _n/_2 elements that agree on mod _p_ bits. We merge _L_<sub>3</sub> and _L_<sub>4</sub> similarly to get another list _L_<sub>34</sub>. This merging can be achieved by a dynamic programming approach that finds solutions modulo _p_ (see \[JW24, JWZ25\]). Then, at the second level, we merge these two lists such that all the subset sums agree on mod _q_ bits. The algorithm searches the final list for the desired collision. If one is found, it outputs the collision; otherwise, it outputs \(\perp\). We represent this algorithm schematically in Figure 1.

\begin{tabular}{ccc}
 & **Modular** & **Integer** \\
Input & \(\mathbf{a}\in\mathbb{Z}_M^n\) & \(\mathbf{b}\in[M]^n\) \\
Problem & Find \(\mathbf{u}_i\neq\mathbf{u}_j\) in {0,1}_<sup>n</sup>_\\{0_<sup>n</sup>_}, & Find \(\mathbf{u}_i\neq\mathbf{u}_j\) in {0,1}_<sup>n</sup>_\\{0_<sup>n</sup>_} \\
 & \(\mathbf{a}\cdot\mathbf{u}_i\equiv_M\mathbf{a}\cdot\mathbf{u}_j\) & \(\mathbf{b}\cdot\mathbf{u}_i=\mathbf{b}\cdot\mathbf{u}_j\) \\
Input Split & \(a_i^{(pq)}:=a_imodpq;a_i^{(r)}:=a_imodr\) & \(b_i=b_i^{(pq)}+pq\cdot b_i^{(r)}\) such that \\
 & \(a_i^{(pq)}\in\mathbb{Z}_{pq}\), \(a_i^{(r)}\in\mathbb{Z}_r\) & \(b_i^{(pq)}\in[0,pq)\), \(b_i^{(r)}\in[0,r]\) \\
Distribution & \(a_i^{(pq)},a_i^{(r)}\) independent & \(b_i^{(pq)},b_i^{(r)}\) independent \\
 & and uniform over their support & and uniform over their support \\
\end{tabular}

L1
L2
L3
L4
P
P
L12
L34
q
L1234

2: Setup for Modular and Integer problem

Figure 1: Schematic diagram of the filtering algorithm.

