## 4.2 Matrix sequences with explicit or hidden (asymptotic) structure

In this section, we introduce three types of matrix structures that serve as the fundamental building blocks of the GLT ∗-algebras. Specifically, for any positive integers _d_ and _r_, we consider the set of _d_-level _r_-block GLT matrix sequences. This set forms a ∗-algebra of matrix sequences, which is both maximal and isometrically equivalent to the maximal ∗-algebra of 2_d_-variate \(r\times r\) matrix-valued measurable functions (with respect to the Lebesgue measure) that are naturally defined over \([0,1]^d\times[-\pi,\pi]^d\); see \[11, 10, 41, 42\] and references therein.<br>
The reduced version of this structure plays a crucial role in approximating integro- differential operators, including their fractional versions, particularly when defined over general (non-Cartesian) domains. This concept was initially introduced in \[124, 125\] and later extensively developed in \[8\], where GLT symbols are again defined as measurable functions over \(\Omega\times[-\pi,\pi]^d\), with \(\Omega\) being Peano-Jordan measurable and contained within \[0,1\]_<sup>d</sup>_. Additionally, the reduced versions also form maximal ∗- algebras that are isometrically equivalent to their corresponding maximal ∗-algebras of measurable functions.<br>
These GLT ∗-algebras provide a rich framework of hidden (asymptotic) structures, built upon three fundamental classes of explicit algebraic structures: _d_-level _r_-block Toeplitz matrix sequences and sampling diagonal matrix sequences (discussed in Sections 4.4 and 4.5), along with asymptotic structures described by zero-distributed matrix-sequences (see Section 4.3). Notably, the latter class serves an analogous role to compact operators in relation to bounded linear operators, forming a two-sided ideal of matrix sequences within any of the GLT ∗-algebras.

## 4.3 Zero-distributed sequences

Zero-distributed sequences are defined as matrix sequences {_A<sub>n</sub>}<sub>n</sub>_ such that \(\{A_n\}_n\sim_\sigma 0\). Note that, for any \(r\ge 1\), \(\{A_n\}_n\sim_\sigma 0\) is equivalent to \(\{A_n\}_n\sim_\sigma O_r\), where _O<sub>r</sub>_ is the \(r\times r\) zero matrix. The following theorem, taken from \[121, 41\], provides a useful characterization for detecting this type of sequence.

**Theorem 4.1** _Let_ {_A<sub>n</sub>}<sub>n</sub> be a matrix sequence, with A<sub>n</sub> of size d<sub>n</sub>, and let_ \(p\in[1,\infty]\)_, with_ \(\|X\|_p\) _being the Schatten p-norm of X, that is, the_ \(\ell^p\) _norm of the vector of its singular values. Let_ \(\|\cdot\|=\|\cdot\|_\infty\) _be the spectral norm. With the natural convention_ \(1/\infty=0\)_, we have:_

• \(\{A_n\}_n\sim_\sigma 0\) _if and only if A<sub>n</sub>=R<sub>n</sub>+N<sub>n</sub> with_ \(rank(R_n)/d_n\rightarrow 0\) _and_ \(\|N_n\|\rightarrow 0\) _as_ \(n\rightarrow\infty\);<tbc>

• \(\{A_n\}_n\sim_\sigma 0\) _if there exists_ \(p\in[1,\infty]\) _such that_<tbc>

<tbc>\(\frac{\|A_n\|_p}{(d_n)^{1/p}}\rightarrow 0\text{\textit{as}}n\rightarrow\infty.\)<tbc>

<tbc>As in Section 2.2, the same definition can be given and the corresponding result (with obvious changes) holds when the involved matrix sequences show a multi-level structure. In that case, _n_ is replaced by **_n_** uniformly in _A<sub>n</sub>_, _N<sub>n</sub>_, _R<sub>n</sub>_, _d<sub>n</sub>_.

