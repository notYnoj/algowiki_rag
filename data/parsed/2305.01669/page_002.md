<tbc>motivated by savings obtained for relevant scenarios. We present the fundamental idea behind the method and we discuss further generalization. In Section 2 we recall essential fundamentals of AD and we draw conclusions for the computation of Newton steps. The potential for reduction in computational cost is illustrated with the help of the practically relevant special case of banded local Jacobians in Section 3. Further generalization and formalization is the subject of Section 4. Conclusions are drawn in Section 5.

**2. A Lesson from Adjoint AD.** First-order AD comes in two fundamental flavors. Tangent AD yields<tbc>

(2.1) \(\dot{y}=\dot{F}(x,\dot{x})\equiv F'(x)\cdot\dot{x}\)

<tbc>and, hence, the (dense) Jacobian with machine accuracy at \(\mathcal{O}(n)\cdot\mathrm{Cost}(\dot{F})\) by letting \(\dot{x}\) range over the Cartesian basis of R_<sup>n</sup>_. Adjoint AD computes<tbc>

(2.2) \(\bar{x}=\bar{F}(x,\bar{y})\equiv F'(x)^T\cdot\bar{y},\)

<tbc>yielding the same Jacobian up to machine accuracy at \(\mathcal{O}(n)\cdot\mathrm{Cost}(\bar{F})\) by letting \(\bar{y}\) range over the Cartesian basis of R_<sup>n</sup>_. Both tangent and adjoint AD are matrix-free methods in the sense that the Jacobian is not required explicitly in order to evaluate Equations (2.1) or (2.2). Both methods can be used to accumulate \(F'\). Their costs differ according to the ratio

\(\mathcal{R}\equiv\frac{\mathrm{Cost}(\bar{F})}{\mathrm{Cost}(\dot{F})},\)

where, typically, \(\mathcal{R}\ge 1\). Hence, tangent AD is usually the method of choice for computing Jacobians of the residual in the context of Newton’s method. Sparsity of the Jacobian of the residual may change the picture \[6\].

Second-order tangent and adjoint AD follow naturally; see \[10\]. Hessians required by Newton’s method for convex optimization of objectives \(f:\mathbb{R}^n\rightarrow\mathbb{R}\) can be com puted at \(\mathcal{O}(n)\cdot\mathrm{Cost}(\dot{f})\) using second-order adjoint versions \(\dot{f}\) of _f_. Corresponding matrix-free Newton-Krylov methods \[14\] can be derived. They are based on the observation that the Hessian-vector products required by Krylov-subspace methods (e.g. Conjugate Gradients \[11\]) can be computed by a second-order adjoint \(\dot{f}\) without prior accumulation of the Hessian. The approach to be proposed in this article is different. It exploits special structure and local sparsity of _F_ instead of global propagation of tangents or adjoints.

**2.1. Terminology.** AD requires the given program _F_ to be differentiable. The notation from \[10\] is modified only slightly.

Definition 2.1 (Differentiable Program). _A_ differentiable program<tbc>

\(F:\mathbb{R}^n\rightarrow\mathbb{R}^m:y:=F(x)\)

<tbc>_decomposes into a_ single assignment code<tbc>

(2.3) \(v_j:=\varphi(v_i)_{i\in P_j}\text{\textit{for}}j=1,\dots,p+m,\)

<tbc>_where v_<sub>_i-n_</sub>=_x<sub>i</sub> for i_=1_,...,n and y<sub>k</sub>=v_<sub>_p+k_</sub> _for k_=1_,...,m and with differentiable_ elemental functions \(\varphi_j\), _j_=1_,...,p+m, featuring_ elemental partial derivatives

\(\partial_{j,i}\equiv\frac{\partial\varphi_j}{\partial v_i}\text{\textit{for}}i\in P_j.\)

_The set of arguments of_ \(\varphi_j\) _(direct predecessors of v<sub>j</sub>) is denoted by P<sub>j</sub>._

