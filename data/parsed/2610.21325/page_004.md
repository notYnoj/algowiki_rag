_survivors._

The right half of Figure 2(b) shows the fovea, which takes over after the retina pass. For each survivor, the fovea reads the original vector in full precision and computes the exact distance between that vector and the query. As a result, the _k_ survivors with the smallest exact distances are the exact _k_ nearest neighbors of **q**, marked #1 and #2 for _k_=2 in the figure.

## 3.2 Certified Exclusion

Consider a database \(\mathcal{X}:=\{\mathbf{x}_1,\dots,\mathbf{x}_N\}\subset\mathbb{R}^D\) and a query \(\mathbf{q}\in\mathbb{R}^D\). Exact kNN search returns the index set \(\mathcal{N}_k(\mathbf{q}):=argmin_{\mathcal{S}\subseteq[N],|\mathcal{S}|=k}\sum_{i\in\mathcal{S}}\|\mathbf{q}-\mathbf{x}_i\|\), whose farthest member lies at the distance _r<sub>k</sub>_(**q**) from **q**. However, computing N_<sub>k</sub>_(**q**) requires exact distances only for the vectors that may be neighbors. Definition 1 therefore formalizes what a test that excludes the other vectors must guarantee, whatever arithmetic it uses.

**Definition 1** (Certified exclusion)**.** A test \(T(\mathbf{q},\mathbf{x},U)\in\{\text{keep},\text{exclude}\}\) is a _certified exclusion test_ if its computed output keeps every vector **x** with \(\|\mathbf{q}-\mathbf{x}\|\le U\), for every query **q**, vector **x**, and threshold \(U\ge 0\).

Definition 1 constrains only the direction of the errors of a test. Specifically, a certified exclusion test may keep a vector farther than _U_ at the cost of one exact distance, but it never excludes a vector within _U_.

**Proposition 1** (Exact search by certified exclusion)**.** _For a certified exclusion test T and a threshold_ \(U\ge r_k(\mathbf{q})\)_, the k vectors with the smallest exact distances among the vectors that T keeps form_ N_<sub>k</sub>_(**q**).

_Proof._ Every \(\mathbf{x}\in\mathcal{N}_k(\mathbf{q})\) satisfies \(\|\mathbf{q}-\mathbf{x}\|\le r_k(\mathbf{q})\le U\) and is therefore kept by Definition 1. The _k_ smallest exact distances among a superset of N_<sub>k</sub>_(**q**) are the _k_ smallest over X.

## 3.3 Lifted Lower Bound

Proposition 1 leaves open which certified exclusion test to use. CertEx needs a test that reads few bytes, because the retina pass reads every database vector and its cost grows with the number of bytes per vector. CertEx therefore keeps a few principal coordinates of each vector and one more coordinate that summarizes the rest, which together still give a lower bound on the distance. Specifically, consider a center \(\mathbf{c}\in\mathbb{R}^D\) and a matrix \(\mathbf{V}\in\mathbb{R}^{m\times D}\) whose orthonormal rows are the _m_ leading principal directions of a sample of X. We call _m_ the _width_ of the retina. The _lifted projection_ of a vector keeps its _m_ principal coordinates and summarizes the remaining _D-m_ coordinates by their norm:

\(\ell(\mathbf{x}):=\left[\begin{array}{ c }
\mathbf{V}(\mathbf{x}-\mathbf{c}) \\
\|(\mathbf{I}-\mathbf{V}^\top\mathbf{V})(\mathbf{x}-\mathbf{c})\|
\end{array}\right]\in\mathbb{R}^{m+1}.\) (1)

**Proposition 2** (Lower bound)**.** _For all_ \(\mathbf{q},\mathbf{x}\in\mathbb{R}^D\), \(\|\ell(\mathbf{q})-\ell(\mathbf{x})\|\le\|\mathbf{q}-\mathbf{x}\|\).

_Proof._ The entry (_i,j_) of \(\mathbf{V}\mathbf{V}^\top\) is the inner product of rows _i_ and _j_ of **V**, which is 1 for _i=j_ and 0 otherwise because the rows are orthonormal. Hence \(\mathbf{V}\mathbf{V}^\top=\mathbf{I}_m\). We write \(\unknown:=\mathbf{V}^\top\mathbf{V}\) and prove the claim in five steps.

Step 1 splits the centered vectors. We define **u**:=**q**-**c**, **v**:=**x**-**c**, \(\mathbf{u}_1:=\unknown\mathbf{u}\), \(\mathbf{u}_2:=\mathbf{u}-\mathbf{u}_1\), \(\mathbf{v}_1:=\unknown\mathbf{v}\), and \(\mathbf{v}_2:=\mathbf{v}-\mathbf{v}_1\). Two facts follow. First, with \(\mathbf{a}:=\mathbf{V}(\mathbf{u}-\mathbf{v})\in\mathbb{R}^m\),

\(\mathbf{u}_1-\mathbf{v}_1=\mathbf{V}^\top\mathbf{V}\mathbf{u}-\mathbf{V}^\top\mathbf{V}\mathbf{v}=\mathbf{V}^\top\mathbf{V}(\mathbf{u}-\mathbf{v})=\mathbf{V}^\top\mathbf{a}.\) (2)

Second, since \(\mathbf{V}\mathbf{V}^\top=\mathbf{I}_m\),

\(\mathbf{V}\mathbf{u}_2=\mathbf{V}\mathbf{u}-\mathbf{V}\mathbf{V}^\top\mathbf{V}\mathbf{u}=\mathbf{V}\mathbf{u}-\mathbf{V}\mathbf{u}=\mathbf{0}\) (3)

and likewise **Vv**<sub>2</sub>=**0**.

Step 2 writes the lifted projections in these parts. Eq. (1) applied to **q** reads \(\ell(\mathbf{q})=[\mathbf{V}\mathbf{u};\|(\mathbf{I}-\mathbf{V}^\top\mathbf{V})\mathbf{u}\|]\), because **q**-**c**=**u**. Its first block is **Vu**=**V**(**u**<sub>1</sub>+**u**<sub>2</sub>)=**Vu**<sub>1</sub>+**Vu**<sub>2</sub>=**Vu**<sub>1</sub> by Eq. (3). Its last coordinate is \(\|\mathbf{u}_2\|\), because \((\mathbf{I}-\mathbf{V}^\top\mathbf{V})\mathbf{u}=\mathbf{u}-\unknown\mathbf{u}=\mathbf{u}-\mathbf{u}_1=\mathbf{u}_2\). The same computation for **x** gives

\(\ell(\mathbf{q})=\left[\begin{array}{ c }
\mathbf{V}\mathbf{u}_1 \\
\|\mathbf{u}_2\|
\end{array}\right],\ell(\mathbf{x})=\left[\begin{array}{ c }
\mathbf{V}\mathbf{v}_1 \\
\|\mathbf{v}_2\|
\end{array}\right],\)

and subtracting the two gives

\(\ell(\mathbf{q})-\ell(\mathbf{x})=\left[\begin{array}{ c }
\mathbf{V}(\mathbf{u}_1-\mathbf{v}_1) \\
\|\mathbf{u}_2\|-\|\mathbf{v}_2\|
\end{array}\right].\)

The squared norm of a stacked vector is the sum of the squared norms of its blocks, so that

\(\|\ell(\mathbf{q})-\ell(\mathbf{x})\|^2=\|\mathbf{V}(\mathbf{u}_1-\mathbf{v}_1)\|^2+(\|\mathbf{u}_2\|-\|\mathbf{v}_2\|)^2.\) (4)

Step 3 shows that **V** keeps the norm of **u**<sub>1</sub>-**v**<sub>1</sub>. By Eq. (2), \(\mathbf{V}(\mathbf{u}_1-\mathbf{v}_1)=\mathbf{V}\mathbf{V}^\top\mathbf{a}=\mathbf{a}\) and \(\|\mathbf{u}_1-\mathbf{v}_1\|^2=\mathbf{a}^\top\mathbf{V}\mathbf{V}^\top\mathbf{a}=\|\mathbf{a}\|^2\). Hence

\(\|\mathbf{u}_1-\mathbf{v}_1\|^2=\|\mathbf{V}(\mathbf{u}_1-\mathbf{v}_1)\|^2.\) (5)

Step 4 applies the Pythagorean theorem. The center cancels in the difference, **q**-**x**=(**q**-**c**)-(**x**-**c**)=**u**-**v**, which splits as **y**+**z** with **y**:=**u**<sub>1</sub>-**v**<sub>1</sub> and **z**:=**u**<sub>2</sub>-**v**<sub>2</sub>. By Eqs. (2) and (3), the two parts are orthogonal:

\(\langle\mathbf{y},\mathbf{z}\rangle=\langle\mathbf{V}^\top\mathbf{a},\mathbf{z}\rangle=\mathbf{a}^\top\mathbf{V}\mathbf{z}=\mathbf{a}^\top(\mathbf{V}\mathbf{u}_2-\mathbf{V}\mathbf{v}_2)=0.\)

Expanding \(\|\mathbf{y}+\mathbf{z}\|^2=\|\mathbf{y}\|^2+2\langle\mathbf{y},\mathbf{z}\rangle+\|\mathbf{z}\|^2\) therefore gives

\(\|\mathbf{q}-\mathbf{x}\|^2=\|\mathbf{u}_1-\mathbf{v}_1\|^2+\|\mathbf{u}_2-\mathbf{v}_2\|^2.\) (6)

Step 5 applies the reverse triangle inequality. The triangle inequality gives \(\|\mathbf{u}_2\|\le\|\mathbf{u}_2-\mathbf{v}_2\|+\|\mathbf{v}_2\|\) and \(\|\mathbf{v}_2\|\le\)<tbc>

