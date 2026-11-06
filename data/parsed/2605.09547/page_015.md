For the query complexity \(\mathcal{T}(\cdot)\) of the transcript (Definition 4.2), we prove in Section 4.7 that a transcript can be computed with the following query complexity:

**Proposition 4.17.** \(\mathcal{T}(t-1)=T_0+\widetilde{O}(t)\)_, where T_<sub>0</sub> _is the time complexity of querying any_ \(x_e^1\).

Note that the _t_-transcript is just a collection of most objects constructed within the first _t_-1 iterations of the interior point method (ShortStep in Algorithm 1). Hence the name _transcript_, as it stores the values of previous iterations. The main technical result is to show that we can perform iteration _t_ using the _t_-transcript. By storing the resulting (_t_+1)-transcript, this then inductively implies that we can perform the interior point method for any number of iterations.

The aim of the rest of this section is to show that we can indeed compute a _t_-transcript in low space under the streaming model. The _t_-transcript requires us to compute the following values explicitly: \((\delta_y^t,\delta_c^t,y^t,\mu^t)\), and we need to implicitly maintain _x<sup>t</sup>_, _s<sup>t</sup>_, \(\tau^t\) and _g<sup>t</sup>_.

In this analysis, many variables depend on other variables, either from this iteration or from the previous iteration of the transcript. To clarify the relationships as well as to confirm we have no circular dependencies, the following Figure 1 is a diagram of the order of variables calculated to arrive at the _t_+1-transcript from the _t_-transcript.

## 4.2 Recap of IPM

We start by reviewing the important definitions and lemmas that \[BLL<sup>+</sup>21\] uses in their interior point method.

The barrier function \[BLL<sup>+</sup>21\] uses is given by \(\phi(x)=-log(x-l)-log(u-x)\). Note \(\phi'(x)=-\frac{1}{x-l}+\frac{1}{u-x}\) and \(\phi''(x)=\frac{1}{(x-l)^2}-\frac{1}{(u-x)^2}\).

During the IPM, we maintain tuples \((x,s,\mu)\). Given a current point \((x,s,\mu)\), we define a _weight function_ \(\tau:\mathbb{R}^m\rightarrow\mathbb{R}_{>0}^m\). We use regularized Lewis weights.

**Definition 4.3** (Lewis weights)**.** _For_ \(p=1-\frac{1}{4log(4m/n)}\) _define the Lewis weights for x to be the solution to_

\(\tau(x)=\sigma(\mathbf{T}^{\frac{1}{2}-\frac{1}{p}}\Phi''(x)\mathbf{A})+\frac{n}{m}\text{\textit{where}}\mathbf{W}:=diag(\tau).\)

We now formally define the notion of following the central path. We say our current iterate are \(\epsilon\)-centered if the following condition holds. Throughout the algorithm, the points will stay \(\epsilon\)-centered. In particular, the initial point must be \(\epsilon\)-centered.

yt
u
8t y
xt
(t - 1)-transcript
gt
st
Tt
8t c

Figure 1: Variable dependencies. E.g., querying \(x_e^t\) requires the value of \(\tau_e^t\).

