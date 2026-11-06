<tbc>Consider a solution \(\mathbf{x}(t)=\mathbf{V}\alpha(t)\) on the attractor M as in Definition 2. Component-wise, the embedding \(\unknown(\mathbf{x}(t))\) is:

\((\unknown(\mathbf{x}(t)))_k=\mathbf{h}^T(\unknown^{\tau_k}\mathbf{x}(t))=\mathbf{h}^T(\unknown^{\tau_k}\mathbf{V}\alpha(t))\)<br>
\(=\mathbf{h}^T(\mathbf{VD}^{\tau_k}\alpha(t))=\mathbf{g}_{\tau_k}^H\alpha(t)\)

where \(\mathbf{g}_{\tau_k}^H:=\mathbf{h}^T\mathbf{VD}^{\tau_k}\) expressed element-wise is:

\(\mathbf{g}_{\tau_k}^H=\big[\mathbf{v}_1^T\mathbf{h}e^{-i\theta_1\tau_k},\mathbf{v}_1^H\mathbf{h}e^{i\theta_1\tau_k},\cdots,\mathbf{v}_d^T\mathbf{h}e^{-i\theta_d\tau_k},\mathbf{v}_d^H\mathbf{h}e^{i\theta_d\tau_k}\big]\)

Concatenating the vectors \(\mathbf{g}_{\tau_k}^H\) for \(k\in\{1,\dots,\ell\}\) gives rise to the following matrix **G**, which maps from the space of coefficients \(\alpha\in\mathbb{C}^{2d}\) specifying solutions evolving on the attractor to the output delay-coordinate space in \(\mathbb{C}^\ell\):

\(\mathbf{G}=\left[\begin{array}{ c }
\mathbf{g}_{\tau_1}^H \\
\mathbf{g}_{\tau_2}^H \\
\vdots \\
\mathbf{g}_{\tau_\ell}^H
\end{array}\right]=\mathbf{T}\mathbf{H}\in\mathbb{C}^{\ell\times 2d}\) (9)

For details about the derivation of **G**, see the proofs of Theorem III.1 and Theorem III.2 in \[6\]. **G** can be partitioned into two matrices: a Vandermonde matrix **T** capturing the temporal information, and a diagonal matrix **H** containing the observed spatial information:

\(\mathbf{T}=\left[\begin{array}{ c c c c c }
e^{-i\theta_1\tau_1} & e^{i\theta_1\tau_1} & \dots & e^{-i\theta_d\tau_1} & e^{i\theta_d\tau_1} \\
e^{-i\theta_1\tau_2} & e^{i\theta_1\tau_2} & \dots & e^{-i\theta_d\tau_2} & e^{i\theta_d\tau_2} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
e^{-i\theta_1\tau_\ell} & e^{i\theta_1\tau_\ell} & \dots & e^{-i\theta_d\tau_\ell} & e^{i\theta_d\tau_\ell}
\end{array}\right]\in\mathbb{C}^{\ell\times 2d}\)<br>
\(\mathbf{H}=\mathrm{diag}(\mathbf{v}_1^T\mathbf{h},\mathbf{v}_1^H\mathbf{h},\dots,\mathbf{v}_d^T\mathbf{h},\mathbf{v}_d^H\mathbf{h})\in\mathbb{C}^{2d\times 2d}\)

Only **T** is time-dependent, so in analyzing the effect of unevenly-spaced time-delays on the existence and stability of the time-delay embedding, we must consider generalized Vandermonde matrices **T** that involve non-consecutive, non- integer powers \(\{\tau_k\}_{k=1}^\ell\), which we turn to in the next section.

## B. Generalized Vandermonde Matrices and Times Series

Given points \(\{z_p\}_{p=1}^m\in\mathbb{C}\), the Vandermonde matrix \(\mathbf{T}\in\mathbb{C}^{m\times m}\) \[21\], \[22\] is defined as:

\(\mathbf{T}=\left[\begin{array}{ c c c c c }
z_1^0 & z_2^0 & \cdots & z_m^0 \\
z_1^1 & z_2^1 & \cdots & z_m^1 \\
\vdots & \vdots & \ddots & \vdots \\
z_1^{m-1} & z_2^{m-1} & \cdots & z_m^{m-1}
\end{array}\right]\) (10)

and its determinant is:

\(\mathrm{det}(\mathbf{T})=\prod_{1\le p\le q}^m(z_p-z_q)\) (11)

The rank of **T** equals the number of distinct points in \(\{z_p\}_{p=1}^m\). That is, when \(z_p\neq z_q\) for all \(p\neq q\), i.e. all _m_ points are distinct, \(\mathrm{det}(\mathbf{T})\neq 0\), which implies that rank(**T**)=_m_ and thus **T**, as a mapping, preserves all relevant information. It is well-known that Vandermonde and Vandermonde-like matrices are ill-conditioned \[23\], and its determinant can grow quite large as additional points are added. If \(\{z_p\}_{p=1}^m\) are any set<tbc>

<tbc>of _m_ points within a compact subset \(\Omega\subset\mathbb{C}\), then the set of points that maximizes the Vandermonde determinant (11), known as the Fekete points \[24\], gives rise to:

\(d_m(\Omega)=\mathrm{max}_{\{z_1,\dots,z_m\}\in\Omega}\left(\prod_{1\le p\le q}^m|z_p-z_q|\right)^{1/\genfrac(){pt}{2}{m}{2}}\) (12)

Because the Vandermonde matrix is ill-conditioned, the expo nent \(1/\genfrac(){pt}{2}{m}{2}\), which is the number of pairwise products between the _m_ points, is used as a normalization. Normalization ensures that the limit exists as \(m\rightarrow\infty\) in (12). This limit is known as the transfinite diameter of \(\Omega\) \[25\]:

\(\tau(\Omega)=\mathrm{lim}_{m\rightarrow\infty}(d_m(\Omega))\) (13)

While explicit results for Fekete points for general \(\Omega\) are often difficult to determine explicitly, when \(\Omega\) is the unit circle in the complex plane _S_<sup>1</sup>:={_z_:|_z_|=1}, the _m_ Fekete points are the _m_th roots of unity, and \(\tau(\Omega)=1\).

The Vandermonde matrices we consider for time series involve points \(\{z_p=e^{\pm i\theta_p}\}_{p=1}^m\subseteq S^1\). These types of Vandermonde matrices are known as Fourier Vandermonde matrices and are well-studied in the case for when the time sampling rates are evenly-spaced \[26\]-\[31\]. For these matrices, the set of system frequencies is generally not uniformly-distributed on the unit circle, so a given set of system frequencies is unlikely to maximize the Vandermonde determinant (11). Furthermore, the above statements apply only to Vandermonde matrices that are square, which only corresponds to delay-coordinate maps where the number of time delays used to construct the map \(\ell\) is exactly equal to the underlying dimension of the system attractor 2_d_, and matrices that are constructed using consecutive integer powers, which implies the time series data must not be unevenly-sampled. What is helpful from (12) and (13) is the \(1/\genfrac(){pt}{2}{m}{2}\) scaling factor for the determinant of the Vandermonde matrix that ensures the determinant converges to 1 as \(m\rightarrow\infty\).

To generalize (12) and (13) to settings where more lags than attractor dimensions are used in the delay-coordinate map (i.e. \(\ell\ge 2d\)) and when the map is constructed of non-uniform lags, we use a set of coordinates \(\{z_p\}_{p=1}^m\) and powers \(\{\tau_k\}_{k=1}^\ell\) to define a generalized Vandermonde matrix, similar to that studied in \[26\], \[32\]:

\(\mathbf{T}=\mathbf{T}_{m,\ell}=\left[\begin{array}{ c c c c c }
z_1^{\tau_1} & z_2^{\tau_1} & \cdots & z_m^{\tau_1} \\
z_1^{\tau_2} & z_2^{\tau_2} & \cdots & z_m^{\tau_2} \\
\vdots & \vdots & \ddots & \vdots \\
z_1^{\tau_\ell} & z_2^{\tau_\ell} & \cdots & z_m^{\tau_\ell}
\end{array}\right]\in\mathbb{C}^{\ell\times m}\) (14)

The typical approach to prove that Vandermonde matrices **T** as in (10) are full rank involves having an explicit expression for the determinant (11) and inferring the condition that the _m_ nodes \(\{z_p\}_{p=1}^m\) must be distinct. Deriving the determinant depends on properties of polynomials of degrees {1_,...,m_}. Consequently, because the generalized Vandermonde matrix **T** as in (14) involves unevenly-spaced, non-integer powers, the original argument does not readily extend to the generalized setting. Thus, we state the following, only as a conjecture, about the rank of a generalized Vandermonde matrix.

