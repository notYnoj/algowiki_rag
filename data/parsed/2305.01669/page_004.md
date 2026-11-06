<tbc>yields the DAG in Figure 1(a), where, \(\partial_{1,-1}=\mathrm{x}[1]\), \(\partial_{3,1}=\mathrm{cos}(\mathrm{x}[0])\), and so forth. The Jacobian

\(F'=\left(\begin{array}{ c c } \partial_{3,1}\partial_{1,-1} & \partial_{3,1}\partial_{1,0} \\ \partial_{4,1}\partial_{1,-1} & \partial_{4,1}\partial_{1,0}+\partial_{4,2}\partial_{2,0} \end{array}\right)=\left(\begin{array}{ c c } \partial_{3,1} & 0 \\ \partial_{4,1} & \partial_{4,2} \end{array}\right)\left(\begin{array}{ c c } \partial_{1,-1} & \partial_{1,0} \\ 0 & \partial_{2,0} \end{array}\right)\)

can be represented as the bipartite DAG in Figure 1(b). Both options for evaluating the adjoint

\(\left(\left(\begin{array}{ c c } \partial_{3,1} & 0 \\ \partial_{4,1} & \partial_{4,2} \end{array}\right)\left(\begin{array}{ c c } \partial_{1,-1} & \partial_{1,0} \\ 0 & \partial_{2,0} \end{array}\right)\right)^T\left(\begin{array}{ c } \bar{y}_0 \\ \bar{y}_1 \end{array}\right)=\left(\begin{array}{ c c } \partial_{1,-1} & 0 \\ \partial_{1,0} & \partial_{2,0} \end{array}\right)\left(\left(\begin{array}{ c c } \partial_{3,1} & \partial_{4,1} \\ 0 & \partial_{4,2} \end{array}\right)\left(\begin{array}{ c } \bar{y}_0 \\ \bar{y}_1 \end{array}\right)\right)\)

(with \(\bar{y}=(01)^T\) and \(\bar{y}=(10)^T\) giving the rows of the Jacobian) yield the same result. Note that the evaluation of the expression on the left-hand side requires 12fma<sup>2</sup> (O(_qn_<sup>3</sup>); here _q=n_=2) while the right-hand-side expression take only 8fma (O(_qn_<sup>2</sup>)). The same effect due to associativity of the chain rule of differentiation (equivalently, of matrix multiplication)<sup>3</sup> is exploited by _backpropagation_ in the context of training of artificial neural networks \[7\]. The adjoint can be visualized as the DAG in Figure 1(c).

A discussion of the numerous aspects of AD and of its implementation are beyond the scope of this article. The interested reader is referred to \[10\] for further information on the subject. Moreover, the AD community’s Web portal `www.autodiff.org` contains a comprehensive bibliography as well as links to various AD research and tool development efforts.

**2.2. Lesson.** How can Newton’s method benefit from lessons learned in adjoint AD? Working towards an answer to this question, the given implementation of _F_ as a differentiable program is assumed to be composed of elemental functions \(F_i:\mathbb{R}^n\rightarrow\mathbb{R}^n:x^i=F_i(x^{i-1})\) for _i_=1_,...,q_ as

(2.4) \(y=x^q=F(x^0)=(F_q\circ\dots\circ F_1)(x^0)\)

where _x_<sup>0</sup>=_x_. Application of the chain rule of differentiation to Equation (2.4) yields

(2.5) \(F'(x^0)=F'_q(x^{q-1})\cdot\dots\cdot F'_1(x^0)\)

implying

(2.6) \(\Delta x=-F'(x)^{-1}\cdot y=-(F'_q(x^{q-1})\cdot\dots\cdot F'_1(x^0))^{-1}\cdot y=-F'_1(x^0)^{-1}\cdot\dots\cdot F'_q(x^{q-1})^{-1}\cdot y.\)

2fused multiply-add floating-point operations 3assuming infinite precision arithmetic

x [ i %2]*=x [( i + 1)%2]; x [( i + 1)%2]=sin (x [( i + 1)%2]); }
yields the DAG in Figure 1(a), where, 1,-1 = x[1], 3,1 = cos(x[0]), and so forth. The Jacobian

yo y1 d
f e
a c
b

FIG. 2. _Inverse DAG_

