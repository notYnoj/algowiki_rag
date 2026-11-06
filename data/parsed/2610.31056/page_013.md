We denote vectors in boldface, e.g., **v**, and matrices in uppercase, e.g., **A**. For a vector **v**, we denote its _i<sup>th</sup>_ coordinate by _v<sub>i</sub>_ and its \(\ell_2\)-norm by \(\|\mathbf{v}\|_2\). For any matrix \(\mathbf{B}\in\mathbb{R}^{n\times m}\), we denote \(\|\mathbf{B}\|_2=max_{i\in[m]}\{\|\mathbf{b}_i\|_2\}\).

**Theorem 3.1** (Prime Number Theorem)**.** _For any_ \(x\ge 2\) _the number of primes less than or equal to x is given by_ \(\pi(x)=\Theta\left(\frac{x}{log(x)}\right)\).

## 3.1 Lattices

A lattice L is the set of all integer combinations of linearly independent vectors \(\mathbf{b}_1,\mathbf{b}_2,\dots,\mathbf{b}_n\in\mathbb{R}^d\):

\(\mathcal{L}=\left\{\sum_{i=1}^nz_i\mathbf{b}_i|z_i\in\mathbb{Z}\right\}\)

where _n_ is called the rank of the lattice, and _d_ is the dimension. The vectors **b**<sub>1</sub>,**b**<sub>2</sub>_,...,_**b**_<sub>n</sub>_ form a basis of the lattice, and the matrix **B** with columns **b**<sub>1</sub>,**b**<sub>2</sub>_,...,_**b**_<sub>n</sub>_ is called a basis matrix.

**Definition 1** (Shortest Vector Problem (SVP))**.** _Given a lattice_ L_, the Shortest Vector Problem (SVP) asks for a shortest non-zero vector in the lattice, i.e.,_

\(\text{SVP}(\mathcal{L})=\text{argmin}\{\|\mathbf{v}\|_2|\mathbf{v}\in\mathcal{L},\mathbf{v}\neq\mathbf{0}\}\)

A standard notation for the length of the shortest vector in a lattice L is denoted by \(\lambda_1(\mathcal{L})\). In fact, a generalization of \(\lambda_1\) known as successive minima is defined as follows.

**Definition 2** (Successive minima)**.** _Given a lattice_ L _and_ \(i\in[n]\)_, the i<sup>th</sup> successive minima_ \(\lambda_i(\mathcal{L})\) _is defined as_

\(\lambda_i(\mathcal{L})=min\{r\in\mathbb{R}|\text{dim}(\text{span}(\mathcal{L}\cap\text{Ball}_{\ell_2}(0,r)))\ge i\}\)

Throughout the remainder of this section, unless stated otherwise, all norms are with respect to the \(\ell_2\)-norm.

**Definition 3** (Approximate Shortest Independent Vector Problem (SIVP))**.** _Given an n-dimensional lattice_ L _and an approximation function_ \(\gamma:\mathbb{N}\rightarrow\mathbb{R}\)_, the_ \(\gamma\)_-approximate SIVP asks for n linearly independent vectors_ \(\mathbf{v}_1,\dots,\mathbf{v}_n\in\mathcal{L}\) _such that_ \(\|\mathbf{v}_i\|_2\le\gamma(n)\lambda_n(\mathcal{L})\) _for all_ \(i\in[n]\).

We consider the following variant of the above problem, which asks for a single vector.

**Definition 4** (Approximate _n<sup>th</sup>_-Successive Minima Problem (nSMP))**.** <sup>_10_</sup> _Given a lattice_ L _and an approximation function_ \(\gamma:\mathbb{N}\rightarrow\mathbb{R}\)_, the_ \(\gamma\)_-approximate n<sup>th</sup> Successive Minima Problem (nSMP) asks for a non-zero vector_ **v** _in the lattice_ L _such that_ \(\|\mathbf{v}\|\le\gamma(n)\lambda_n(\mathcal{L})\).

Using Theorem B.3, one can show that any algorithm for \(\gamma(n)\)-approximate nSMP can be used to solve \(\sqrt{n}\gamma(n)\)-approximate SIVP.

<sup>10</sup>There is a well-studied lattice problem, called the _Successive Minima Problem_ (SMP) \[Mic08\], which asks for _n_ linearly independent lattice vectors **v**<sub>1</sub>_,...,_**v**_<sub>n</sub>_ such that \(\|\mathbf{v}_i\|=\lambda_i(\mathcal{L})\) for every \(i\in[n]\).

