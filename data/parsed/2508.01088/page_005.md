**Definition 3.2.** _Let_ \(v\in\mathbb{R}^{T(n)}\) _be a vector for_ \(n\in\mathbb{N}\)_. The positive rotation and the negative rotation of v are denoted by v_<sup>+</sup> _and v_<sup>-</sup>_, respectively, and are defined as follows_

\(v_{(i,j)}^+=v_{(n-i+j,n-i+1)}\text{\textit{and}}v_{(i,j)}^-=v_{(n-i+1,i-j+1)}.\)

**Remark 3.3.** _Note that, considering the representation of the vectors in_ T_<sub>n</sub>, v_<sup>+</sup> _and v_<sup>-</sup> _correspond to a_ \(120^\circ\) _and a_ \(-120^\circ(240^\circ)\) _rotation of v, respectively. So, these transformations fulfill the same properties as rotations of order_ 3_. For example_ (_v_<sup>+</sup>)<sup>-</sup>=_v,_ (_v_<sup>+</sup>)<sup>+</sup>=_v_<sup>-</sup>, ((_v_<sup>+</sup>)<sup>+</sup>)<sup>+</sup>=_v. In Figure 4, an example of these vector rotations is presented._

Consider the following proposition which states a relation between the eigenvalues and eigenvectors of a graph _G_, and an automorphism of _G_.

**Proposition 3.4.** \[10, Corollary 2.9\] _Let x be an eigenvector of A associated with_ \(\lambda\) _and P a permutation matrix corresponding to an automorphism of G. Then Px is also an eigenvector of A associated with_ \(\lambda\).

**Corollary 3.5.** _If_ \(v\in\mathbb{R}^{T(n)}\)_, for_ \(n\in\mathbb{N}\)_, is an eigenvector of_ T(_n), then their two rotations, v_<sup>+</sup> _and v_<sup>-</sup>_, are also eigenvectors associated with the same eigenvalue._

_Proof._ Considering Definition 3.2 and Proposition 3.4, the result follows.

Consider the vectors \(R_{n,r},C_{n,c},D_{n,d}\in\mathbb{R}^{T(n)}\), with \(n\in\mathbb{N}\), \(r,c\in[n]\) and \(d\in[0,n-1]\), defined as follows.

\(R_{n,r}(i,j)=\delta_{ir},C_{n,c}(i,j)=\delta_{jc},\text{and}D_{n,d}(i,j)=\delta_{(i-j)d}\) (1)

where \(\delta\) is the Kronecker delta.

We call these vectors _RCD-vectors_. See Figure 5.

For a vector \(v\in\mathbb{R}^{T(n)}\), \(n\in\mathbb{N}\), the vectors \(S_v^r\), \(S_v^c\), \(S_v^d\in\mathbb{R}^n\) represent the sum of the components of _v_ by rows, columns, and diagonals, respectively, and could be defined as follows.

\(S_v^r(\ell_1)=\sum_{j=1}^{\ell_1}v(\ell_1,j),\ell_1\in[n]S_v^c(\ell_2)=\sum_{i=\ell_2}^nv(i,\ell_2),\ell_2\in[n]S_v^d(\ell_3+1)=\sum_{j=1}^{n-\ell_3}v(j+\ell_3,j),\ell_3\in[0,n-1]\text{(2)}\)

10
1
7
6
9
2
3
8
4
3
5
8
4
5
6
9
5
2
1
2
4
7
7
8
9
10
10
6
3
1
v+
v
v

Figure 4: A vector _v_ and its positive (in green) and negative (in magenta) rotations.

