# A MATRIX-FREE NEWTON METHOD

**Abstract.** A modification of Newton’s method for solving systems of _n_ nonlinear equations is presented. The new matrix-free method relies on a given decomposition of the invertible Jacobian of the residual into invertible sparse local Jacobians according to the chain rule of differentiation. It is motivated in the context of local Jacobians with bandwidth 2_m_+1 for \(m\checkmark n\). A reduction of the computational cost by \(\mathcal{O}(\frac{n}{m})\) can be observed. Supporting run time measurements are presented for the tridiagonal case showing a reduction of the computational cost by O(_n_).

Generalization yields the combinatorial Matrix-Free Newton Step problem. We prove NP- completeness and we present algorithmic components for building methods for the approximate solution. Inspired by adjoint Algorithmic Differentiation, the new method shares several challenges for the latter including the DAG Reversal problem. Further challenges are due to combinatorial problems in sparse linear algebra such as Bandwidth or Directed Elimination Ordering.

**Key words.** Newton method, matrix-free, algorithmic differentiation, adjoint

**MSC codes.** 49M15, 47A05, 68N99

**1. Introduction.** We revisit Newton’s method [18, 25] for computing roots \(x\in\mathbb{R}^n\) of differentiable multivariate vector functions \(F:\mathbb{R}^n\rightarrow\mathbb{R}^n:y=F(x)\) with invertible dense Jacobians

\(F'(x)\equiv\left(\frac{dy_j}{dx_i}\right)_{i,j=1,\dots,n}\in\mathbb{R}^{n\times n},\)

and where _x_=(_x<sub>i</sub>_) and _y_=(_y<sub>i</sub>_) for _i_=1_,...,n_. Approximate solutions for which _F(x_)≈0 are computed iteratively as

(1.1) \(\Delta x:=-F'(x)^{-1}\cdot F(x)x:=x+\Delta x\)

for given starting points \(x\in\mathbb{R}^n\). Convergence after \(p\ge 0\) iterations is typically defined as the norm of the residual _F(x_) falling below some given threshold \(0<\epsilon\checkmark 1\). See, for example, [3, 13] for further information on Newton’s method.

We use = to denote mathematical equality, \(\equiv\) in the sense of "is defined as" and := to represent assignment according to imperative programming. Approximate equality if denoted as ≈. We distinguish between partial \((\partial)\) and total (_d_) derivatives. Multiplication is denoted by a dot. The dot may also be omitted in favor of a more compact notation.

The residual _F_ is usually given as a differentiable program written in some high- level programming language. Equation (1.1) implies that the two main ingredients of Newton’s method are the evaluation of the Jacobian \(F'(x)\) and the solution of the linear Newton system \(F'(x)\cdot\Delta x=-F(x)\). Algorithmic Differentiation (AD) [10] of _F_ yields \(F'(x)\) with machine accuracy at a computational cost of \(\mathcal{O}(n)\cdot\mathrm{Cost}(F)\). Subsequent direct solution of the linear Newton system yields the Newton steps \(\Delta x\in\mathbb{R}^n\) at the computational cost of O(_n_<sup>3</sup>). The overall computational cost can be dominated by either of the two parts depending on the ratio \(\frac{\mathrm{Cost}(F)}{\mathcal{O}(n^2)}\) .

Exploitation of special structure of _F_ can yield a significant reduction in computational cost. Consequently, this article proposes a _matrix-free Newton method_

<sup>∗</sup>Software and Tools for Computational Engineering, RWTH Aachen University, Aachen, Germany, naumann@stce.rwth-aachen.de

arXiv:2305.01669v2 [math.NA] 5 May 2023

UWE NAUMANN<sup>∗</sup>

