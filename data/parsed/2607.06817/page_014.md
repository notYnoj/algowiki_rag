The ordered and reflective Ramsey numbers of start-central stars versus start-central stars are straightforward to determine, as shown in the following proposition, which directly extends an earlier result by Balko, Cibulka, Král and Kynčl \[3, Observation 12\].

**Proposition 4.10.** _For any_ \(k\in\mathbb{N}\) _and_ \(n_1,n_2,\dots,n_k\ge 2\)_, we have_

\(R_\mathrm{ord}(S_{n_1}^\mathrm{sc},S_{n_2}^\mathrm{sc},\dots,S_{n_k}^\mathrm{sc})=R_\mathrm{ref}(S_{n_1}^\mathrm{sc},S_{n_2}^\mathrm{sc},\dots,S_{n_k}^\mathrm{sc})=\sum_{j=1}^k(n_j-2)+2.\)

_Proof._ Let \(\Gamma_1,\Gamma_2,\dots,\Gamma_k\) be the permutation groups associated with \(S_{n_1}^\mathrm{sc},S_{n_2}^\mathrm{sc},\dots,S_{n_k}^\mathrm{sc}\), respectively, in the considered permutational Ramsey number \(R_\mathrm{type}(S_{n_1}^\mathrm{sc},S_{n_2}^\mathrm{sc},\dots,S_{n_k}^\mathrm{sc})\) with type \(\in\{\mathrm{ord},\mathrm{ref}\}\). First, we establish the upper bound. Let \(n=\sum_{j=1}^k(n_j-2)+2\), and consider a _k_-edge-coloring of _K<sub>n</sub>_. Let _G<sub>j</sub>_ denote the spanning subgraph of _K<sub>n</sub>_ comprising the edges of color _j_, for \(j\in\{1,2,\dots,k\}\). By the pigeonhole principle, vertex 0 is incident to at least _n<sub>j</sub>_-1 edges of color _j_, for some \(j\in\{1,2,\dots,k\}\). Thus, there exists an increasing injective homomorphism from \(S_{n_j}^\mathrm{sc}\) to _G<sub>j</sub>_. Therefore, \(S_{n_j}^\mathrm{sc}\) is \(\Gamma_j\)-embeddable in _G<sub>j</sub>_, which implies that \(R_\mathrm{type}(S_{n_1}^\mathrm{sc},S_{n_2}^\mathrm{sc},\dots,S_{n_k}^\mathrm{sc})\le\sum_{j=1}^k(n_j-2)+2\).

Now, we establish the lower bound. Let \(n=\sum_{j=1}^k(n_j-2)+1\), and consider the _k_-edge-coloring of _K<sub>n</sub>_ in which the edge between any two distinct vertices \(u,v\in V(K_n)\) is colored with the smallest \(\ell\in\{1,2,\dots,k\}\) such that \(|v-u|\le\sum_{j=1}^\ell(n_j-2)\). Let _G_<sub>1</sub>_,G_<sub>2</sub>_,...,G<sub>k</sub>_ be defined as above, and by way of contradiction, suppose that, for some \(j\in\{1,2,\dots,k\}\), \(S_{n_j}^\mathrm{sc}\) is \(\Gamma_j\)-embeddable in _G<sub>j</sub>_. Then there exists a strictly monotone injective homomorphism \(\varphi:S_{n_j}^\mathrm{sc}\rightarrow G_j\). Therefore, in _G<sub>j</sub>_, vertex \(\varphi(0)\) has at least _n<sub>j</sub>_-1 smaller neighbors or at least _n<sub>j</sub>_-1 larger neighbors, which is impossible. We conclude that \(R_\mathrm{type}(S_{n_1}^\mathrm{sc},S_{n_2}^\mathrm{sc},\dots,S_{n_k}^\mathrm{sc})\ge\sum_{j=1}^k(n_j-2)+2\).

We note that the cyclic Ramsey numbers of start-central stars versus start-central stars coincide with the corresponding standard Ramsey numbers, which were determined by Burr and Roberts \[8\].

The reflective Ramsey numbers of start-central stars versus monotone paths are fully determined by Corollary 4.3, and they coincide with the corresponding ordered Ramsey numbers; see  2. As for start-central stars versus monotone cycles, the ordered and cyclic Ramsey numbers were recently determined \[4\], as follows.

**Theorem 4.11** (\[4, Theorem 4.18 and Corollary 4.19\])**.** _For any_ \(a\in\mathbb{N}\) _and_ \(b\ge 2\)_, we have_ \(R_\mathrm{ord}(S_a^\mathrm{sc},C_b^\mathrm{mon})=R_\mathrm{cyc}(S_a^\mathrm{sc},C_b^\mathrm{mon})=1+(a-1)(b-1)\).

The reflective Ramsey numbers can now easily be determined as shown in the following proposition.

**Proposition 4.12.** _For any_ \(a\in\mathbb{N}\) _and_ \(b\ge 2\)_, we have_ \(R_\mathrm{ref}(S_a^\mathrm{sc},C_b^\mathrm{mon})=1+(a-1)(b-1)\).

_Proof._ Since \(P_b^\mathrm{mon}\) is a subgraph of \(C_b^\mathrm{mon}\), Corollary 4.3 yields<tbc>

\(R_\mathrm{ref}(S_a^\mathrm{sc},C_b^\mathrm{mon})\ge R_\mathrm{ref}(S_a^\mathrm{sc},P_b^\mathrm{mon})=1+(a-1)(b-1).\)

<tbc>By Corollary 2.3 and Theorem 4.11, we obtain

\(R_\mathrm{ref}(S_a^\mathrm{sc},C_b^\mathrm{mon})\le R_\mathrm{ord}(S_a^\mathrm{sc},C_b^\mathrm{mon})=1+(a-1)(b-1).\)

Therefore, \(R_\mathrm{ref}(S_a^\mathrm{sc},C_b^\mathrm{mon})=1+(a-1)(b-1)\).

Hence, the ordered, reflective, cyclic and dihedral Ramsey numbers all coincide when one of the arguments is a start-central star, while the other is a monotone cycle.

We now turn to the reflective Ramsey numbers of start-central stars versus complete graphs. By Proposition 2.4, the cyclic and dihedral Ramsey numbers for this combination of graphs coincide with the standard Ramsey numbers. We recall the following well-known result of Chvátal \[9\].

\begin{tabular}{ccccccccccc}
_a_ & _b_ & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 \\
3 & 5 & 7 & 9 & 11 & 13 & 15 & \(\ge 17\) & \(\ge 19\) & \(\ge 21\) \\
4 & 7 & 10 & 13 & \(\ge 16\) & \(\ge 19\) & \(\ge 22\) & & & & \\
5 & 9 & 13 & \(\ge 17\) & \(\ge 21\) & \(\ge 25\) & & & & & \\
6 & 11 & 16 & \(\ge 21\) & & & & & & & \\
7 & 13 & \(\ge 19\) & \(\ge 25\) & & & & & & & \\
8 & 15 & \(\ge 22\) & & & & & & & & \\
9 & \(\ge 17\) & \(\ge 25\) & & & & & & & & \\
10 & \(\ge 19\) & & & & & & & & & \\
11 & \(\ge 21\) & & & & & & & & & \\
\end{tabular}

13: Dihedral Ramsey numbers \(R_\mathrm{dih}(P_a^\mathrm{alt},K_b)\) with \(3\le a\le 11\) and \(3\le b\le 11\).

