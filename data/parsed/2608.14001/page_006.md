<tbc>_Conjecture 1:_ Let \(\mathbf{T}_{m,\ell}\in\mathbb{C}^{\ell\times m}\) be as (14). Let \(\{\tau_k\}_{k=1}^\ell\) be a set of strictly-positive, distinct powers in the sense that \(\tau_a\neq\tau_b\) for any \(a,b\in\{1,\dots,\ell\}\), and let \(\{z_p\}_{p=1}^m\subseteq S^1\) be a distinct set points with associated angles \(\{\theta_p\}_{p=1}^m\) in the interval \((-\pi,\pi]\) in the sense that \(\theta_p\neq\theta_q\) for \(p,q\in\{1,\dots,m\}\). Then with probability 1, \(\mathrm{rank}(\mathbf{T}_{m,\ell})=\mathrm{min}\{m,\ell\}\).

_Proof:_ The conjecture is trivially true when _m_=1 and \(\ell=1\) as the matrix \(\mathbf{T}_{1,1}=[z_1^{\tau_1}]\) is non-singular provided \(z_1\neq 0\), a condition which is valid when assuming \(z_1\in S^1\). When extending the number of time samples used, so that we consider \(\mathbf{T}_{1,\ell}=[z_1^{\tau_1},\dots,z_1^{\tau_\ell}]^T\in\mathbb{C}^{\ell\times 1}\), it follows that \(\mathrm{rank}(\mathbf{T}_{1,\ell})=1\) for all \(\ell\in\mathbb{N}\) because the sub-matrix consisting of the first row is always non-trivial.

The case when _m_=2 and \(\ell\ge 2\) is also relatively straightforward to establish. For _m_=2 and \(\ell=2\):<tbc>

\(\mathbf{T}_{2,2}=\left[\begin{array}{ c c }
z_1^{\tau_1} & z_2^{\tau_1} \\
z_1^{\tau_2} & z_2^{\tau_2}
\end{array}\right]\) (15)

<tbc>the determinant of which is:

\(\mathrm{det}(\mathbf{T}_{2,2})=z_1^{\tau_1}z_2^{\tau_1}(z_2^{\tau_2-\tau_1}-z_1^{\tau_2-\tau_1})\) (16)

Letting \(z_1=e^{i\theta_1}\) and \(z_2=e^{i\theta_2}\) with \(\theta_1,\theta_2\in(-\pi,\pi]\) and \(\delta_1:=\tau_2-\tau_1\), then, to ensure **T**<sub>2,2</sub> is non-singular by showing \(\mathrm{det}(\mathbf{T}_{2,2})\neq 0\), we require that \(z_1,z_2\neq 0\), which is trivially true when \(z_1,z_2\in S^1\), and also that \(\theta_2-\theta_1\neq 2\pi\left(k_1+\frac{k_2}{\delta_1}\right)\) for \(k_1,k_2\in\mathbb{Z}\)-a condition accounting for the multi-valued nature of the functions. This condition for unevenly-spaced time delay samples for generalized Vandermonde matrix is analogous to the condition for Fourier Vandermonde matrices with evenly-spaced delay powers that requires \(\theta_2-\theta_1\neq 2\pi k\) for \(k\in\mathbb{Z}\), albeit with slightly more restrictions.

If \(\delta_1\) is a rational number expressed in lowest terms- that is, \(\delta_1=p/q\) where \(p,q\ge 1\) are co-prime-then the condition reduces to \(\theta_2-\theta_1\neq\frac{2\pi k}{p}\) for \(k\in\mathbb{Z}\). Note that for \(\theta_1,\theta_2\in(-\pi,\pi]\), the interval of interest for \(\theta_2-\theta_1\) is then \((-2\pi,2\pi]\), meaning increasing _p_ begins to increase the number of values that can introduce aliasing on \((-2\pi,2\pi]\), suggesting that non-uniformly-spaced powers can actually be more prone to aliasing than using evenly-spaced powers.

This is further confirmed if \(\delta_1\) is irrational. Since Z and \(\frac{1}{\delta_1}\mathbb{Z}\) are linearly independent over the rational numbers, for irrational \(\delta_1\) the set \(2\pi\left(k_1+\frac{k_2}{\delta_1}\right)\) is Lebesgue measure zero but dense on \((-2\pi,2\pi]\), meaning that non-uniform time sampling that have irrational spacing may be even more prone to aliasing than when using spacings involving rational numbers. Notably, while there is a dense set of choices of \(\theta_1\) and \(\theta_2\) for which **T**<sub>2,2</sub> will fail to be full rank, since the set is Lebesgue measure zero generic choices of \(\theta_1\) and \(\theta_2\) will ensure that **T**<sub>2,2</sub> is full rank with probability one.

For \(\mathbf{T}_{2,\ell}\) with \(\ell>2\) to be non-singular, a necessary and sufficient condition is to require at least one **T**<sub>2,2</sub> sub-matrix consisting of two rows of \(\mathbf{T}_{2,\ell}\) to be non-singular: that is, \(\mathbf{T}_{2,\ell}\) must have at least two rows that are linearly independent. We could form such a **T**<sub>2,2</sub> sub-matrix using any choice of two rows of \(\mathbf{T}_{2,\ell}\), say with rows raised to time powers \(\tau_a\) and \(\tau_b\), where \(a,b\in\{1,\dots,\ell\}\). The condition for \(\mathrm{rank}(\mathbf{T}_{2,\ell})=2\)<tbc>

<tbc>would then be that there exists at least one set of time pairings \(\tau_a,\tau_b\) such that \(\theta_2-\theta_1\neq 2\pi\left(k_1+\frac{k_2}{\tau_a-\tau_b}\right)\). Since only one of the \(\genfrac(){pt}{2}{\ell}{2}\) possible row pairings of \(\mathbf{T}_{2,\ell}\) needs to satisfy the above condition, we need

\(\frac{\theta_2-\theta_1}{2\pi}\in(-1,1)\backslash\{0\}\cup\cap_{1\le b<a\le\ell}\left\{\alpha\in\frac{1}{\delta_{a,b}}\mathbb{Z}:\alpha\in(-1,1]\right\}\)

As \(\ell\) increases, the intersection of the sets of aliased points between the \(\genfrac(){pt}{2}{\ell}{2}\) pairs of time samples becomes smaller and smaller; thus, increasing lags can mitigate aliasing.

To show the compounding difficulty of proving the statement for \(\ell\ge 3\), we also consider \(\ell=3\). Let \(z_1=e^{i\theta_1},z_2=e^{i\theta_2}\), and \(z_3=e^{i\theta_3}\in S^1\), with \(\theta_1,\theta_2,\theta_3\in(-\pi,\pi]\). Then,<tbc>

\(\mathbf{T}_{3,3}=\left[\begin{array}{ c c c }
z_1^{\tau_1} & z_2^{\tau_1} & z_3^{\tau_1} \\
z_1^{\tau_2} & z_2^{\tau_2} & z_3^{\tau_2} \\
z_1^{\tau_3} & z_2^{\tau_3} & z_3^{\tau_3}
\end{array}\right]\) (17)

<tbc>Letting \(\delta_1:=\tau_2-\tau_1\) and \(\delta_2:=\tau_3-\tau_2\), the determinant of **T**<sub>3,3</sub> can be computed first by subtracting \(z_1^{\delta_1}\) times row 1 from row 2 and by subtracting \(z_1^{\delta_2}\) times row 2 from row 3:<tbc>

\(\mathrm{det}(\mathbf{T}_{3,3})=\left|\begin{array}{ c c c c }
z_1^{\tau_1} & z_2^{\tau_1} & z_3^{\tau_1} \\
z_1^{\tau_2}-z_1^{\delta_1}z_1^{\tau_1} & z_2^{\tau_2}-z_1^{\delta_1}z_2^{\tau_1} & z_3^{\tau_2}-z_1^{\delta_1}z_3^{\tau_1} \\
z_1^{\tau_3}-z_1^{\delta_2}z_1^{\tau_2} & z_2^{\tau_3}-z_1^{\delta_2}z_2^{\tau_2} & z_3^{\tau_3}-z_1^{\delta_2}z_3^{\tau_2}
\end{array}\right|\)

<tbc>By simplifying and expanding by the first column, and computing the resulting \(2\times 2\) determinant, we have the following:

\(\mathrm{det}(\mathbf{T}_{3,3})=\left|\begin{array}{ c c c c }
z_1^{\tau_1} & z_2^{\tau_1} & z_3^{\tau_1} \\
0 & z_2^{\tau_1}(z_2^{\delta_1}-z_1^{\delta_1}) & z_3^{\tau_1}(z_3^{\delta_1}-z_1^{\delta_1}) \\
0 & z_2^{\tau_2}(z_2^{\delta_2}-z_1^{\delta_2}) & z_3^{\tau_2}(z_3^{\delta_2}-z_1^{\delta_2})
\end{array}\right|\)<br>
\(=z_1^{\tau_1}\cdot\left|\begin{array}{ c c c }
z_2^{\tau_1}(z_2^{\delta_1}-z_1^{\delta_1}) & z_3^{\tau_1}(z_3^{\delta_1}-z_1^{\delta_1}) \\
z_2^{\tau_2}(z_2^{\delta_2}-z_1^{\delta_2}) & z_3^{\tau_2}(z_3^{\delta_2}-z_1^{\delta_2})
\end{array}\right|\) (18)

\(=z_1^{\tau_1}z_2^{\tau_1}z_3^{\tau_1}(z_2^{\delta_1}-z_1^{\delta_1})(z_3^{\delta_1}-z_1^{\delta_1})\)<br>
\(\cdot\left(z_3^{\delta_1}\frac{(z_3^{\delta_2}-z_1^{\delta_2})}{(z_3^{\delta_1}-z_1^{\delta_1})}-z_2^{\delta_1}\frac{(z_2^{\delta_2}-z_1^{\delta_2})}{(z_2^{\delta_1}-z_1^{\delta_1})}\right)\)

For **T**<sub>3,3</sub> to be non-singular, we require \(\mathrm{det}(\mathbf{T}_{3,3})\neq 0\). Similar to **T**<sub>2,2</sub>, necessarily \(z_1,z_2,z_3\neq 0\), which is true since \(z_1,z_2,z_3\in S^1\). Furthermore, the relationships between _z_<sub>1</sub>_,z_<sub>2</sub> and _z_<sub>3</sub> will impose restrictions. When working with the non-uniform delays, the multi-valued nature of functions \(z^\delta\), where \(\delta\) is potentially non-integer, yields sufficient conditions: \(\theta_1-\theta_2\neq 2\pi(k_1+\frac{k_2}{\delta_1})\) and \(\theta_1-\theta_3\neq 2\pi(k_1+\frac{k_2}{\delta_1})\) for \(k_1,k_2\in\mathbb{Z}\). Like the case of **T**<sub>2,2</sub>, if \(\delta_1\) is a rational number in lowest terms \(\delta_1=p/q\) so that \(p,q\ge 1\) are co-prime, then the condition reduces to \(\theta_1-\theta_2\neq\frac{2\pi k}{p}\) and \(\theta_2-\theta_3\neq\frac{2\pi k}{p}\) for \(k\in\mathbb{Z}\). If \(\delta_1\) is irrational, then there are a dense set of values in the interval \((-2\pi,2\pi]\) for which the differences of frequencies lead to aliasing.

The last requirement for **T**<sub>3,3</sub> to be non-singular demands a more complicated relationship between _z_<sub>2</sub> and _z_<sub>3</sub> as seen in (18). We can definitely say that if _z_<sub>2</sub>=_z_<sub>3</sub>, then the final term is zero. Thus, for the last term to be nonzero, \(\theta_2-\theta_3\neq 2\pi k\) for \(k\in\mathbb{Z}\) for \(k\in\mathbb{Z}\) is still necessary, but not sufficient. Regardless, the points at which aliasing could occur are still countably many and thus represent a measure zero set of<tbc>

