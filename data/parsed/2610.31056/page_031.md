Now, consider the following matrices

\(\mathbf{U}_{ijlk}^{(L)}:=\left[\mathbf{u}_i^{(L)}\mathbf{u}_j^{(L)}\mathbf{u}_l^{(L)}\mathbf{u}_k^{(L)}\right],\)<br>
\(\mathbf{U}_{ijlk}^{(R)}:=\left[\mathbf{u}_i^{(R)}\mathbf{u}_j^{(R)}\mathbf{u}_l^{(R)}\mathbf{u}_k^{(R)}\right],\)<br>
\(\mathbf{U}_{ijlk}:=\left[\mathbf{u}_i\mathbf{u}_j\mathbf{u}_l\mathbf{u}_k\right]=\left[\mathbf{U}_{ijlk}^{(L)}\mathbf{U}_{ijlk}^{(R)}\right],\)

where the vectors \(\mathbf{u}_t\forall t\in\{i,j,l,k\}\) are considered as column vectors. For the following analysis, matrices \(\mathbf{U}_{ijlk}^{(L)}\) and \(\mathbf{U}_{ijlk}^{(R)}\) are consider over the ring Z_<sub>p</sub>_, and the matrix **U**_<sub>ijlk</sub>_ over the ring Z_<sub>q</sub>_. Then, we split the set _S_ based on the rank of the above matrices. Let _B_<sub>_t_<sub>1</sub>_,t_<sub>2</sub>_,t_<sub>3</sub></sub> be the set of 4-tuple (**u**_<sub>i</sub>,_**u**_<sub>j</sub>,_**u**_<sub>l</sub>,_**u**_<sub>k</sub>_) such that _i\<j_, _l\<k_, \((i,j)\neq(l,k)\), rank (**U**_<sub>ijlk</sub>_)=_t_<sub>3</sub>, \(\mathsf{rank}\left(\mathbf{U}_{ijlk}^{(L)}\right)=t_1\), and \(\mathsf{rank}\left(\mathbf{U}_{ijlk}^{(R)}\right)=t_2\).

Now, using linear algebra techniques, we prove the following lemma that gives us an upper bound on the size of the set _B_<sub>_t_<sub>1</sub>_,t_<sub>2</sub>_,t_<sub>3</sub></sub>.

**Proposition 6.0.1.** _For any_ \(1\le t_1,t_2,t_3\le 4\)_, the following holds_

\(|B_{t_1,t_2,t_3}|=\mathcal{O}\left(2^\frac{(t_1+t_2)n}{2}\right).\)

_And, since_ \(t_3\ge\mathrm{max}\{t_1,t_2\}\)_, we have_ |_B_<sub>_t_<sub>1</sub>_,t_<sub>2</sub>_,t_<sub>3</sub></sub>|=O\(\left(2^{t_3n}\right)\).

_Proof._ To upper bound |_B_<sub>_t_<sub>1</sub>_,t_<sub>2</sub>_,t_<sub>3</sub></sub>|, we count the number of matrices \(\mathbf{U}_{ijlk}^{(L)}\) and \(\mathbf{U}_{ijlk}^{(R)}\) such that<tbc>

\(\mathsf{rank}\left(\mathbf{U}_{ijlk}^{(L)}\right)=t_1,\mathsf{rank}\left(\mathbf{U}_{ijlk}^{(R)}\right)=t_2.\)

<tbc>**Proposition 6.0.2.** _Let_ \(\mathsf{M}_t:=\{\mathbf{M}\in\mathbb{Z}_s^{n\times m}|\mathsf{rank}(\mathbf{M})=t,\mathbf{M}_{ij}\in\{0,1\}\}\) _where_ \(n\ge m\) _and s is a prime. Then_

\(|\mathsf{M}_t|=\mathcal{O}\left(\left(t^{t^2}\right)^{m-t}\cdot 2^{tn}\cdot m!\right).\)

_In particular, if m is a constant, then_ |M_<sub>t</sub>_|=O(2<sup>_tn_</sup>).

_Proof._ refer to Section D.3.

Considering all concatenations of such matrices yields a set that contains all valid **U**_<sub>ijlk</sub>_, by Proposition 6.0.2, the number of \(\mathbf{U}_{ijlk}^{(L)}\) with rank _t_<sub>1</sub> is O(2<sup>_t_<sub>1</sub>_n/_2</sup>), and similarly the number of \(\mathbf{U}_{ijlk}^{(R)}\) with rank _t_<sub>2</sub> is O(2<sup>_t_<sub>2</sub>_n/_2</sup>). Therefore, \(|B_{t_1,t_2,t_3}|=\mathcal{O}\left(2^\frac{(t_1+t_2)n}{2}\right)\).

Now that we have a good upper bound on the size of the set _B_<sub>_t_<sub>1</sub>_,t_<sub>2</sub>_,t_<sub>3</sub></sub>, in the following lemma, we give a relation between the desired probability

\(\mathbb{P}_{\mathbf{a}^{(pq)}}(\mathcal{D}_{ij}=1\wedge\mathcal{D}_{lk}=1)\)

and the rank of the matrices **U**_<sub>ijlk</sub>_, \(\mathbf{U}_{ijlk}^{(L)}\) and \(\mathbf{U}_{ijlk}^{(R)}\). This is a crucial lemma since it allows us to compute bounds on the probabilities using simple linear algebra.

**Lemma 6.0.4.** _For any_ \(\left(\mathbf{u}_i,\mathbf{u}_j,\mathbf{u}_l,\mathbf{u}_k\right)\in B_{t_1,t_2,t_3}\)_, the following holds_

\(\mathbb{P}_{\mathbf{a}^{(pq)}}(\mathcal{D}_{ij}=1\wedge\mathcal{D}_{lk}=1)\le\frac{1}{p^{t_1}\cdot p^{t_2}\cdot q^{t_3}}.\)

