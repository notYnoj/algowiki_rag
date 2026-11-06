_Proof._ To compute a lower bound of the first moment of the random variable C<sup>(int)</sup>, we first look at its relation with the binary random variables \(\mathcal{C}_{ij}^{(\mathrm{int})}\) as follows<tbc>

\(\mathcal{C}^{(\mathrm{int})}\ge\sum_{1\le i<j\le N}\mathcal{C}_{ij}^{(\mathrm{int})}.\)

<tbc>The inequality comes because we work with the sufficient condition for collision, then the necessary condition in the definition of the variable \(\mathcal{C}_{ij}^{(\mathrm{int})}\). Using the linearity of expectation, we have the following

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}^{(\mathrm{int})}\right)\ge\sum_{i<j}\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{ij}^{(\mathrm{int})}\right).\)

## Expectation for overlapping vectors.

Let us make the following observation. Fix \(\mathbf{u}_i,\mathbf{u}_j\in\mathrm{A}\). Then, we split the set \[_n_\] into three parts as follows. The first part contains the indices where the vector **u**_<sub>i</sub>_ is 1 and the vector **u**_<sub>j</sub>_ is 0. Similarly, the second part corresponds to 0 and 1, and the last part corresponds to 1 and 1. This will give us three disjoint subsets of the set \[_n_\]. These are the only indices that are active for these two binary vectors.

Observe that indices at which both vectors have a 1 in the same position necessarily contribute to a collision, regardless of the specific input instance. Consequently, it suffices to analyze the remaining components. Since these components correspond to disjoint index sets, the problem effectively reduces to analyzing vectors with non-overlapping supports.

Now, we formalize this argument. Define three auxiliary binary vectors \(\mathbf{u}_{ij}^{(10)},\mathbf{u}_{ij}^{(01)}\), and \(\mathbf{u}_{ij}^{(11)}\) as follows

\(u_{ijl}^{(10)}:=\left\{\begin{array}{ c c }
1 & u_{il}=1,u_{jl}=0 \\
0 & \text{else}
\end{array}\right.\forall 1\le l\le n \\
u_{ijl}^{(01)}:=\left\{\begin{array}{ c c }
1 & u_{il}=0,u_{jl}=1 \\
0 & \text{else}
\end{array}\right.\forall 1\le l\le n \\
u_{ijl}^{(11)}:=\left\{\begin{array}{ c c }
1 & u_{il}=1,u_{jl}=1 \\
0 & \text{else}
\end{array}\right.\forall 1\le l\le n
\end{array}\right.\) (7)

and let \(w_{ij}^{(10)}\), \(w_{ij}^{(01)}\), and \(w_{ij}^{(11)}\) denote the Hamming weights of the vectors \(\mathbf{u}_{ij}^{(10)}\), \(\mathbf{u}_{ij}^{(01)}\), and \(\mathbf{u}_{ij}^{(11)}\) respectively. Let \(w_{ij}^{(10)},w_{ij}^{(01)}\in(cn,n]\) for a constant \(1/8\le c<1/4\). That implies that the non- overlapping parts have big enough weights. Now, we define another binary random variable \(\mathcal{D}_{ij}^{(int)}\) over the random choice of **a**. The variable \(\mathcal{D}_{ij}^{(int)}=1\) if the vectors **u**_<sub>i</sub>_ and **u**_<sub>j</sub>_ survive the algorithm, and the auxiliary vectors \(\mathbf{u}_{ij}^{(10)}\) and \(\mathbf{u}_{ij}^{(01)}\) collide over the carry bits and the remaining bits.

Formally, we define \(\mathcal{D}_{ij}^{(int)}=1\) if the auxiliary vectors \(\mathbf{u}_{ij}^{(10)},\mathbf{u}_{ij}^{(01)}\), and \(\mathbf{u}_{ij}^{(11)}\) satisfy the following equations

\(\mathsf{F}_{\mathsf{LS},\mathbf{a},10}^{(p)}:\mathbf{u}_{ij}^{(10)(L)}\cdot\mathbf{a}^{(p)(L)}\equiv s_0-\mathbf{u}_{ij}^{(11)(L)}\cdot\mathbf{a}^{(p)(L)}\mathrm{mod}p,\mathsf{F}_{\mathsf{LS},\mathbf{a},01}^{(p)}:\mathbf{u}_{ij}^{(01)(L)}\cdot\mathbf{a}^{(p)(L)}\equiv s_0-\mathbf{u}_{ij}^{(11)(L)}\cdot\mathbf{a}^{(p)(L)}\mathrm{mod}p,\mathsf{F}_{\mathsf{TS},\mathbf{a},10}^{(pq)}:\mathbf{u}_{ij}^{(10)}\cdot\mathbf{a}^{(pq)}\equiv\beta-\mathbf{u}_{ij}^{(11)}\cdot\mathbf{a}^{(pq)}\mathrm{mod}pq,\mathsf{F}_{\mathsf{TS},\mathbf{a},01}^{(pq)}:\mathbf{u}_{ij}^{(01)}\cdot\mathbf{a}^{(pq)}\equiv\beta-\mathbf{u}_{ij}^{(11)}\cdot\mathbf{a}^{(pq)}\mathrm{mod}pq,\)

