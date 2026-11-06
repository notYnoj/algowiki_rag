• _A\>B_, where \(A,B\in\mathbb{K}^{n\times n}\), means that _A-B_ is positive definite. Likewise, _A\<B_ means that _A-B_ is negative definite.<tbc>

• _A∼B_, where \(A,B\in\mathbb{K}^{n\times n}\), denotes that _A_ and _B_ are similar matrices (i.e., there exists an invertible _P_ such that _A=PBP_<sup>-1</sup>).<tbc>

• \(\|\cdot\|_p\): denotes the standard _p_-norm of a vector or matrix, \(1\le p\le\infty\).<tbc>

• \(\|\cdot\|\): denotes the spectral norm (largest singular value), coincides with \(\|\cdot\|_\infty\). If the matrix is normal, the spectral norm coincides with the spectral radius.<tbc>

• \(\otimes\): Kronecker (tensor) product. For \(A\in\mathbb{C}^{p\times q}\), \(B\in\mathbb{C}^{r\times s}\),<tbc>

<tbc>\(A\otimes B=\left[\begin{array}{ c c c c }
a_{11}B & \cdots & a_{1q}B \\
\vdots &  & \vdots \\
a_{p1}B & \cdots & a_{pq}B
\end{array}\right]\in\mathbb{C}^{pr\times qs}\)<tbc>

• _L<sup>p</sup>(D_): Space of _p_-integrable functions on domain _D_.<tbc>

• _C_(\[_a,b_\]): Space of continuous functions on \[_a,b_\].<tbc>

• \(\mathcal{O}(\cdot)\), \(o(\cdot)\): Big-_O_ and little-_o_ notation.<tbc>

• C_<sub>c</sub>_(R), C_<sub>c</sub>_(C): The set of continuous, complex-valued functions with compact support on R or C.<tbc>

• \(\partial D\): boundary of a set \(D\subseteq\mathbb{R}^d\); in particular, \(\partial\Omega\) denotes the boundary of the spatial domain \(\Omega\).

**Multi-index notation:**

• **_i_** denotes a multi-index \((i_1,\dots,i_d)\in\mathbb{Z}^d\). Its size will be clear from context.<tbc>

• **0,1,2**_,..._ are vectors of all zeros, ones, twos, etc.<tbc>

• **_h_**+**_k_** is the multi-index whose components are _h<sub>r</sub>+k<sub>r</sub>_ for _r_=1_,...,d_. More generally, operations between multi-indices such as subtraction, multiplication, division, and so on, are performed componentwise.<tbc>

• \(h\le k\) means that \(h_r\le k_r\) for all _r_=1_,...,d_. More generally, relations between multi-indices are evaluated componentwise.<tbc>

• **_h_**_,...,**k**_ denotes the multi-index range \(\{\ell\in\mathbb{Z}^d:h\le\ell\le k\}\). With \(\ell=h,\dots,k\) we mean that \(\ell\) varies in this range from **_h_** to **_k_** according to the standard lexicographic ordering:<tbc>

<tbc>\(\left[\cdots\left[[(\ell_1,\dots,\ell_d)]_{\ell_d=h_d,\dots,k_d}\right]_{\ell_{d-1}=h_{d-1},\dots,k_{d-1}}\cdots\right]_{\ell_1=h_1,\dots,k_1}.\)<tbc>

• \(m\rightarrow\infty\) means that \(min(m)=min_{r=1,\dots,d}m_r\rightarrow\infty\), or equivalently, that all the components tend to infinity.<tbc>

• _N_(**_m_**) is the product of all the components of **_m_**, i.e., \(N(m):=\prod_{r=1}^dm_r\).<tbc>

