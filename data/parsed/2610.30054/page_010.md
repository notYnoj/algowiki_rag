proves the barrier, since a relation \(\langle n,n,n\rangle\unknown\langle r\rangle\) gives \(n^{9/4}=F^\star(\langle n,n,n\rangle)\le F^\star(\langle r\rangle)=r\). The same argument applies if new degenerations \(T\unknown S\) are added as rules, as long as \(F^\star(\pi\cdot T)\le F^\star(\pi\cdot S)\) for every permutation \(\pi\) of the legs (Proposition 5.7). So a new degeneration can lead to a bound below 9/4, together with the ingredients, only if it violates one of these inequalities. For all real numbers \(a\ge b\ge c\ge 0\), other functions in \(\Delta_\unknown\) of the same kind show in the same way that no derivation gives a better upper bound on \(\omega_\mathbb{F}(a,b,c)\) than Theorem 1.2.

We do not know whether _F<sup>⋆</sup>_ agrees with a spectral point on the tensors \(\pi\cdot\mathsf{P}_{a,b}\) and the matrix multiplication tensors. If it did, the first inequality in (1.7) would be an equality as well, and \(\omega_\mathbb{F}=9/4\).

### 1.5 Organisation of the paper

In Section 2 we will define tensors, restrictions and degenerations. In Section 3 we will construct the degenerations of ingredients (D1)-(D4). In Section 4 we will introduce spectral points, obtain \(\omega_\mathbb{F}<2.3212\) from a tensor of Strassen as a first example, and prove Theorem 1.1 and Theorem 1.2. In Section 5 we will show that the current ingredients of the proofs cannot give better bounds.

## 2 Restriction and degeneration

In this section we define tensors, restrictions and degenerations, and state the facts about them that we will use. From now on, F is a field, and all vector spaces are finite-dimensional over F. We use the convention 0<sup>0</sup>=1, and for an integer \(n\ge 0\) we write \[_n_\]={1_,...,n_}.

### 2.1 Tensors

A _tensor_ over F is an element _T_ of a tensor product \(U\otimes V\otimes W\) of three vector spaces _U,V_ and _W_, which we call the first, second and third _leg_ of _T_. For tensors \(S\in U_1\otimes V_1\otimes W_1\) and \(T\in U_2\otimes V_2\otimes W_2\), the _direct sum_ \(S\oplus T\) lies in \((U_1\oplus U_2)\otimes(V_1\oplus V_2)\otimes(W_1\oplus W_2)\), and the _tensor product_ \(S\otimes T\) lies in \((U_1\otimes U_2)\otimes(V_1\otimes V_2)\otimes(W_1\otimes W_2)\), after regrouping the factors.

We define a version of the direct sum in which the first leg is shared. For an integer \(m\ge 1\), vector spaces _U_, _V_<sub>1</sub>_,...,V<sub>m</sub>_ and _W_<sub>1</sub>_,...,W<sub>m</sub>_, and tensors \(T_i\in U\otimes V_i\otimes W_i\) for \(i\in[m]\), their _partial direct sum_ is

\(T_1\oplus_1\cdots\oplus_1T_m:=T_1+\cdots+T_m\in U\otimes(V_1\oplus\cdots\oplus V_m)\otimes(W_1\oplus\cdots\oplus W_m).\)

Figure 2 compares the partial direct sum with the direct sum.

Let S<sub>3</sub> be the group of permutations of {1,2,3}. For a tensor \(T\in U\otimes V\otimes W\) and a permutation \(\pi\in\mathfrak{S}_3\), let \(\pi\cdot T\) be the tensor obtained from _T_ by permuting the factors, so that, for every \(i\in\{1,2,3\}\), the _i_th leg of _T_ is the \(\pi(i)\)th leg of \(\pi\cdot T\), as in \[Str87, Section 2\].

For an integer \(n\ge 0\), let _e_<sub>1</sub>_,...,e<sub>n</sub>_ be the standard basis of F_<sup>n</sup>_. The _unit tensor_ is \(\langle n\rangle:=\sum_{i=1}^ne_i\otimes e_i\otimes e_i\). For integers \(n_1,n_2,n_3\ge 1\), the _matrix multiplication tensor_ is

\(\langle n_1,n_2,n_3\rangle:=\sum_{i=1}^{n_1}\sum_{j=1}^{n_2}\sum_{k=1}^{n_3}E_{ij}\otimes E_{jk}\otimes E_{ki}\in\mathbb{F}^{n_1\times n_2}\otimes\mathbb{F}^{n_2\times n_3}\otimes\mathbb{F}^{n_3\times n_1},\)

where _E<sub>ij</sub>_ denotes the matrix with entry 1 at (_i,j_) and 0 elsewhere.

Generally, the tensor of a bilinear map \(\mu:U\times V\rightarrow W\) is \(T=\sum_{i,j}e_i^*\otimes e_j^*\otimes\mu(e_i,e_j)\) in \(U^*\otimes V^*\otimes W\), where the sums run over bases of _U_ and _V_ and \(e_i^*\) is the dual basis element of _e<sub>i</sub>_. We get \(\mu\) back from _T_ by evaluating the first two factors: \(\mu(u,v)=\sum_{i,j}e_i^*(u)e_j^*(v)\mu(e_i,e_j)\) for all \(u\in U\) and \(v\in V\) .

