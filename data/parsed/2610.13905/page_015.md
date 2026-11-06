## 3.2 Symbolic Sparsification

One question remains: how do we obtain the symbolic basis transformations \(\phi_\varepsilon\), \(\psi_\varepsilon\) and \(\nu_\varepsilon\)? In this work, we use a symbolic version of the greedy sparsification algorithm first proposed by Holtz et al. \[32\], which, in the context of fast exact matrix multiplication, is capable of producing optimal (in terms of resulting sparsity) basis transformations and has been shown to reduce the leading coefficient of an algorithm’s arithmetic complexity by up to 89%. Our symbolic version is shown here as Algorithm 3. For simplicity we restrict our focus to \(U(\varepsilon)\), but the algorithm applies identically to \(V(\varepsilon)\) and \(W(\varepsilon)\).

**Algorithm 3** Symbolic Sparsification Algorithm

**Input:** \(U(\varepsilon)\in\mathbb{C}[\varepsilon,\varepsilon^{-1}]^{m_0k_0\times t}\) with \(\mathrm{rank}_{\mathbb{C}(\varepsilon)}(U(\varepsilon))=m_0k_0\) and a constant \(r\in\mathbb{R}^+\).

**Output:** Invertible \(\phi_\varepsilon^{-1}\in\mathbb{C}[\varepsilon,\varepsilon^{-1}]^{m_0k_0\times m_0k_0}\) such that \(U_\phi(\varepsilon)=\phi_\varepsilon^{-1}U(\varepsilon)\) is as sparse as possible.

1: \(\phi_\varepsilon^{-1}=\emptyset\)

2: \(w_c=\mathbf{Generate-Constraints}(\phi_\varepsilon^{-1})\)

3: **for** \(i=1:r\cdot t\) **do**

4: **while** \(\mathbf{Next-Vector}(i,w_c)\neq\emptyset\) **do**

5: _v_=**Next-Vector**(_i,w<sub>c</sub>_)

6: \(\phi_\varepsilon^{-1}=[\phi_\varepsilon^{-1};v^T]\)

7: _w<sub>c</sub>_=**Generate-Constraints** (\(\phi_\varepsilon^{-1}\))

8: **if** \(\mathrm{size}(\phi_\varepsilon^{-1},1)=m_0k_0\) **then**

9: **return** \(\phi_\varepsilon^{-1}\)

10: **end if**

11: **end while**

12: **end for**

Algorithm 3 progressively constructs a set of vectors \(\phi_\varepsilon^{-1}\) in \(\mathbb{C}[\varepsilon,\varepsilon^{-1}]^{m_0k_0}\) according to the following rules: (1) each newly added vector _v_ should be linearly independent to the current collection and (2) \(v^TU(\varepsilon)\) should be as sparse as possible. This is done via the following subroutines:

1. **Generate-Constraints**\((\phi_\varepsilon^{-1})\) - returns a set of constraints _w<sub>c</sub>_ that, when satisfied by a vector \(v\in\mathbb{C}[\varepsilon,\varepsilon^{-1}]^{m_0k_0}\), implies that it is linearly independent to every (row) vector in \(\phi_\varepsilon^{-1}\).<tbc>

2. **Next-Vector**(_i,w<sub>c</sub>_) - returns a vector \(v\in\mathbb{C}[\varepsilon,\varepsilon^{-1}]^{m_0k_0}\) that satisfies both the constraints _w<sub>c</sub>_ and \(\mathrm{weight}(v^TU(\varepsilon))=i\).<tbc>

<tbc>For the latter, the function \(\mathrm{weight}(\cdot)\) is a measure of sparsity defined as

\(\mathrm{weight}(v^TU(\varepsilon)):=\mathrm{nnz}(v^TU(\varepsilon))+\mathrm{nns}(v^TU(\varepsilon))+\mathrm{nnc}(v^TU(\varepsilon))\cdot p,\) (3.4)

where nnz is the number of nonzero entries, nns is the number of constant, nonsingleton entries (that is, not -1, 0, or 1), and nnc is the number of variable entries, i.e., that contain \(\varepsilon\), for _p_ a tunable parameter. (3.4) naturally extends to the matrix \(U(\varepsilon)\) as follows

\(\mathrm{weight}(U(\varepsilon)):=\mathrm{nnz}(U(\varepsilon))+\mathrm{nns}(U(\varepsilon))+\mathrm{nnc}(U(\varepsilon))\cdot p-\mathrm{ncols}(U(\varepsilon)),\) (3.5)

where ncols is the number of columns.<sup>11</sup> By repeatedly calling **Next-Vector** for increasing values of _i_, Algorithm 3 promotes optimal sparsity; that is, each newly added vector _v_ has the smallest value of \(\mathrm{weight}(v^TU(\varepsilon))\) possible. Accordingly, the constant _r_ should be chosen so that \(r\cdot t\) is the maximum possible value of \(\mathrm{weight}(v^TU(\varepsilon))\), specifically to guarantee that the algorithm terminates.

Importantly, we have made several simplifications here both for convenience and to accelerate Algorithm 3. We summarize them below.

1. First, we assume that the encoding matrix \(U(\varepsilon)\) belongs to \(\mathbb{C}[\varepsilon,\varepsilon^{-1}]^{m_0k_0\times t}\), equivalently that its entries are Laurent polynomials in \(\varepsilon\) as opposed to arbitrary rational functions in \(\varepsilon\). Similarly, **Next-Vector** returns \(v\in\mathbb{C}[\varepsilon,\varepsilon^{-1}]^{m_0k_0}\). We focus on Laurent polynomials for the following reasons: (1) essentially all<tbc>

<sup>11</sup>In the case of \(\mathrm{weight}(W(\varepsilon))\), ncols is replaced by nrows, the number of rows in \(W(\varepsilon)\).

