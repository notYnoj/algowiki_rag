<tbc>Definition 2.2 (Direct Acyclic Graph). _Equation (2.3) induces a_ directed acyclic graph (DAG) _G_=(_V,E),V_=(_X,Z,Y),_ \(X\cap Z\cap Y=\varnothing\),1 \(E\subseteq V\times V\) _such that X_={1-_n,...,_0}_,Z_={1_,...,p},Y=p_+1_,...,p+m and_ \((i,j)\in E\Leftrightarrow i\in P_j\)_. All edges_ (_i,j_) _are labelled with_ \(\partial_{j,i}\).

Paths connecting vertices _i_ and _j_ are denoted as (_i,...,j_).

Definition 2.3 (Layered DAG and Local Jacobians). _A DAG of a matrix chain product_

\(F'_q\cdot\dots\cdot F'_1=F'\in\mathbb{R}^{m\times n}\)

_of_ local Jacobians \(F'_i\)_,i_=1_,...,q is called_ layered DAG.

The DAG in Figure 1(a) is layered.

Definition 2.4 (Uniformly Layered DAG). _A layered DAG of a matrix chain product_

\(F'_q\cdot\dots\cdot F'_1=F'\in\mathbb{R}^{n\times n}\)

_is called_ uniformly layered DAG _if_ \(F'_i\in\mathbb{R}^{n\times n}\) _for i_=1_,...,q._

The DAG in Figure 1(a) is uniformly layered.

Definition 2.5 (Invertible DAG). _We refer to a DAG of a differentiable program with invertible Jacobian_ \(F'\in\mathbb{R}^{n\times n}\) _as an_ invertible DAG_. The_ corresponding Newton step _is defined as_ \((F')^{-1}\cdot y\) _for given_ \(y\in\mathbb{R}^n\).

Adjoint AD can be implemented by using operator and function overloading in suitable programming languages such as C++ \[9, 12, 21\]. The given implementation of _F_ as a differentiable program is run in overloaded arithmetic to augment the computation of the function value with the recording of the corresponding DAG (also referred to as _tape_). For example, for q=2 the differentiable C++ program

**for** (**int** i=0;i\<q;i++) {

1The simplest "no-op" program x=x distinguishes x as an input \((\in X)\) from x as an output \((\in Y)\) while \(Z=\varnothing\) in this case. Corresponding larger scenarios follow naturally.

yo
j1
3
4
3
4
3
4
d4,101,-1
d3,1
d4,1
d4,2
d3,1
d4,1
d4,2
1
2
1
2
d1,-1
d1,0
d2,0
d1,-1
d1,0
d2,0
d3,101,0
-1
0
-1
0
-1
0
(a)
(b)
(c)

Fig. 1. _Sample DAGs_

