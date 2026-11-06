<tbc>Let us assume for now that _n_ is even; the case of _n_ odd is almost identical and described later. The key observation to understand this state is that (for _n_ even) the product can be rearranged as<tbc>

\(\underbrace{\big((T_{i_1})_{j_1,k_1}(B_{i_2}(v_2))_{k_1,j_3}\dots(T_{i_{n-1}})_{j_{n-1},k_{n-1}}(B_{i_n}(v_n))_{k_{n-1},j_1}\big)}_\text{all the}\underbrace{\text{with odd}p}_\text{with odd}p\cdot\)<br>
\(\underbrace{\big((T_{i_2})_{j_2,k_2}(B_{i_3}(v_3))_{k_2,j_4}\dots(T_{i_n})_{j_n,k_n}(B_{i_1}(v_1))_{k_n,j_2}\big)}_\text{all the}\underbrace{\text{with even}p}_\text{with even}p\)

<tbc>Therefore \(\langle v_1,v_2,\dots,v_n|C|u,u,\dots,u\rangle\) factorizes as<tbc>

\(\sum_{i_1,\dots,i_n\in[r]}\left(\sum_{j_p,k_p}\sum_\text{with}p\text{odd}(T_{i_1})_{j_1,k_1}(B_{i_2}(v_2))_{k_1,j_3}\dots(T_{i_{n-1}})_{j_{n-1},k_{n-1}}(B_{i_n}(v_n))_{k_{n-1},j_1}\right)\cdot\)<br>
\(\left(\sum_{j_p,k_p}\text{with}p\text{even}(T_{i_2})_{j_2,k_2}(B_{i_3}(v_3))_{k_2,j_4}\dots(T_{i_n})_{j_n,k_n}(B_{i_1}(v_1))_{k_n,j_2}\right)\)

<tbc>Since each term of the product is a trace, \(\langle v_1,\dots,v_n|C|u,\dots,u\rangle\) is<tbc>

\(\sum_{i_1,\dots,i_n\in[r]}\text{Tr}(T_{i_1}B_{i_2}(v_2)\dots T_{i_{n-1}}B_{i_n}(v_n))\text{Tr}(B_{i_1}(v_1)T_{i_2}\dots B_{i_{n-1}}(v_{n-1})T_{i_n})\)

<tbc>Using that \((A\otimes B)P(C\otimes D)P=AD\otimes BC\), one can prove by induction that

\(\text{Tr}\left(\prod_{p=1}^nL(v_p)\right)=\sum_{i_1,\dots,i_n\in[r]}\text{Tr}\left(\prod_{p=1}^n(T_{i_p}\otimes B_{i_p}(v_p))P\right)\)<br>
\(=\sum_{i_1,\dots,i_n\in[r]}\text{Tr}\big(T_{i_1}B_{i_2}(v_2)\dots T_{i_{n-1}}B_{i_n}(v_n)\otimes B_{i_1}(v_1)T_{i_2}\dots B_{i_{n-1}}(v_{n-1})T_{i_n}\big)\)<br>
\(=\langle v_1,v_2,\dots,v_n|C|u,u,\dots,u\rangle,\)

which concludes the proof of Lemma 5.1 for even values of _n_. For _n_ odd, the analysis is almost identical except that one obtains the following single trace

\(\sum_{i_1,\dots,i_n\in[r]}\text{Tr}(T_{i_1}B_{i_2}(v_2)\dots T_{i_n}B_{i_1}(v_1)\cdot T_{i_2}B_{i_3}(v_3)\dots B_{i_n}(v_n)).\)

One can then prove by induction that \(\text{Tr}\left(\prod_{p=1}^nL(v_p)\right)\) has this form when _n_ is odd, thereby proving Lemma 5.1 for odd values of _n_.

## 5.2. Proof of Lemma 5.2.

Now we prove that the image of _L_ has the claimed block structure. For intuition, suppose that _V_ is a matrix space of dimension one, spanned by _A_. For any \(M\in\text{Mat}_d(\mathbb{C})\) and \(|x,y\rangle\in\mathbb{C}^d\otimes\mathbb{C}^d\), we have that \((A\otimes M)P|x,y\rangle=A|y\rangle\otimes M|x\rangle\). In particular, when \(y\in\text{ker}(A)\) this is always zero, and the first factor of the tensor always belong to im(_A_). Lemma 5.2 extends this reasoning to the general case by using the sum of the im(_A_) and the intersection of the ker(_A_).

**Lemma 5.2.** _Let_ \(d\in\mathbb{N}\backslash\{0\}\) _and V be a subspace of_ Mat_<sub>d</sub>_(C) _with_ \(0<dim(V)\le d\)_. Call_ \(S=(V\otimes\text{Mat}_d(\mathbb{C}))P\) _and S<sup>k</sup>_=span{_M_<sub>1</sub>_M_<sub>2</sub>_...M<sub>k</sub>:M_<sub>1</sub>_,M_<sub>2</sub>_,...,M<sub>k</sub>_\(\in S\}\)_. There exists a subspace E of_ \(\mathbb{C}^d\otimes\mathbb{C}^d\) _and a map_ \(\tau:\text{Mat}_{d^2}(\mathbb{C})\rightarrow\text{End}(E)\) _with the following properties:_

(_T1)_ \(\tau(MN)=\tau(M)\tau(N)\) _for all_ \(M,N\in\bigcup_{k\ge 1}S^k\),<tbc>

(_T2)_ \(\text{Tr}(M)=\text{Tr}(\tau(M))\) _for all_ \(M\in\bigcup_{k\ge 1}S^k\),<tbc>

_(T3)_ _for all_ \(X\in\text{End}(E)\)_, there exists_ \(M\in S^2\) _such that_ \(\tau(M)=X\).

