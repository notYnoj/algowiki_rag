\(\text{Pruned}_{\tau_1\cdots\tau_k}(S)\), for a set _S_ of output strings of length _L-k_, returns the array returned by the vertex \(\tau_1\cdots\tau_k\) of Full, restricted to the strings in _S_:

(1) If _k=L_, then look up \(\Phi_\tau(a)\) and \(\Psi_\tau(b)\) from the precomputed encodings (Section 2.4.1) and return \(\Phi_\tau(a)\Psi_\tau(b)\) for the leaf \(\tau=\tau_1\cdots\tau_L\).<tbc>

(2) For each term \(\lambda\) of Schönhage’s identity, let \(S_\lambda\) be the union of the slices _S<sub>z</sub>_ over the _z_ to which \(\lambda\) contributes, i.e., \(S_{P_{ij}}:=S_{z_{ij}}\cup S_{z_0}\) and _S_<sub>_P_<sub>0</sub></sub>:=_S_<sub>_z_<sub>0</sub></sub>.<tbc>

(3) For each term \(\lambda\) of Schönhage’s identity with \(S_\lambda\neq\emptyset\), compute \(C_\lambda:=\text{Pruned}_{\tau_1\cdots\tau_k}\lambda(S_\lambda)\), an array on \(S_\lambda\).<tbc>

(4) Return the array _c_ on _S_ whose slices are _c<sub>z<sub>ij</sub></sub>_:=_C<sub>P<sub>ij</sub></sub>_ and \(c_{z_0}:=\sum_\lambda C_\lambda\), restricted to _S<sub>z<sub>ij</sub></sub>_ and to _S_<sub>_z_<sub>0</sub></sub>. (These restrictions make sense, since \(S_{z_{ij}}\subseteq S_{P_{ij}}\) and \(S_{z_0}\subseteq S_\lambda\) for every \(\lambda\), by step (2).)

Let us confirm which leaves Pruned visits. Recall from (2) that Mult(_a,b_)\[_w_\] is the sum of \(\Phi_\tau(a)\Psi_\tau(b)\) over the leaves contributing to _w_ (as defined in Section 2.3.2), i.e., those that choose _P<sub>ij</sub>_ at every level where _w_ has _z<sub>ij</sub>_, and may choose any term at levels where _w_ has _z_<sub>0</sub>. For a set _U_ of output strings of length _L_, we write Leaves(_U_) for the set of leaves that contribute to some output string of _U_.

**Lemma 10.** _Let a and b be input arrays, and let U be a set of output strings of length L. Called at the root,_ Pruned(_U_) _returns_ Mult(_a,b_) _restricted to U. The leaves it visits are exactly those of_ Leaves(_U), and the sets passed to the calls it makes have total size at most_ (_L_+1)|Leaves(_U_)|.

_Proof._ The values are correct by induction on _L-k_: each \(C_\lambda\) is the array of the corresponding child of Full restricted to \(S_\lambda\), so step (4) is step (4) of Full restricted to _S_.

Recall that \(S_\lambda\) consists of the last _L-k_-1 variables of each string in _S_ such that \(\lambda\) contributes to the first variable of that string. Thus, an induction on _k_ shows that the set passed to the vertex \(\tau_1\cdots\tau_k\) consists of the suffixes \(w_{k+1}\cdots w_L\) of the strings _w_ of _U_ to which the vertex contributes, and furthermore that the vertex is called if and only if this set is nonempty. This means a leaf is visited if and only if it contributes to some string of _U_.

For the total size, map each suffix in the set passed to a vertex \(\tau_1\cdots\tau_k\) to the leaf that extends \(\tau_1\cdots\tau_k\) by picking _P<sub>ij</sub>_ at the levels where the suffix has _z<sub>ij</sub>_ and by picking _P_<sub>0</sub> where it has _z_<sub>0</sub>. By the previous paragraph, the vertex contributes to some string _w_ of _U_ with this suffix, and then so does this leaf, so the leaf is in Leaves(_U_). The leaf determines the vertex and the suffix. This means the sets passed to the vertices at each of the _L_+1 depths have total size at most |Leaves(_U_)|.

In other words, each call is made at most once, no matter how many strings of _U_ depend on it, and the running time depends on the size of the union of the sets of leaves contributing to the strings of _U_, rather than the sum of their sizes. It remains to bound this union.

## 2.4.3 Few leaves contribute to a sparse set of entries

In our final algorithm, which we present below in Section 2.4.4, the set _U_ passed to Pruned will consist only of the output strings we have been focusing on, i.e., output strings of length _L_ whose inner sets (defined in Section 2.3.3) have exactly _m_ elements, so that they index the entries of the products _X<sub>Q</sub>Y<sub>Q</sub>_ (Lemma 9). There are \(M=\genfrac(){pt}{2}{L}{m}9^{L-m}=KN_0^2\) such output strings (with _M_ as defined in Section 2.3.4), and in this subsection all output strings are of this kind.

Our focus in this subsection is on counting how many leaves the Pruned algorithm visits. A single output string has 10_<sup>m</sup>=D_<sup>log<sub>4</sub>10</sup>≈_D_<sup>1.66</sup> leaves contributing to it. This may appear<tbc>

