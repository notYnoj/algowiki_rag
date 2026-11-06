form, the resulting constraint is not convex.

We can now introduce some relevant notation for the convexity analysis of functions. Given a bounded real-valued function _f_ defined on a compact nonempty set X, the convex envelope of _f_ over X is the function \(\breve{f}:\mathcal{X}\unknown x\mapsto\breve{f}(x)=inf\{u:(x,u)\in conv(epi(f))\}\), where epi(_f_)={(_x,u_):\(f(x)\le u\}\) and conv(.) of a set represents its convex hull. In other words, \(\breve{f}\) is the highest convex under-estimator of _f_ over X.

If this is not clear from the context, the subscript X can be added to emphasize that we are considering the convex envelope over X, thus leading to the notation \(\breve{f}_\mathcal{X}\).

One can also express \(\breve{f}(x)\) by considering a convex combination over X representing _x_ and minimizing the combination of \(f'\)s values:

\(\breve{f}_\mathcal{X}(x)=inf_{\lambda_i}\sum_{v_i\in\mathcal{X}}\lambda_if(v_i)\)<br>
\(\sum_{v_i\in\mathcal{X}}\lambda_iv_i=x,\sum_{v_i\in\mathcal{X}}\lambda_i=1,\lambda_i\ge 0.\)

## 1.1 Related work

### Maximum concurrent flow

The maximum concurrent flow problem without delay constraints can be formulated as a linear program and, in principle, solved using standard optimization tools [1]. Nevertheless, even this version--without delay constraints--is known to give rise to challenging computational problems (see, e.g., [6, 7]). This led many researchers to design approximation algorithms for the problem [7, 11, 14, 19, 21, 24]. Furthermore, several decomposition methods are proposed in [2] to improve computational efficiency. In the special case where all commodities share a common source, a strongly polynomial-time combinatorial algorithm is also presented in [2].<br>
Regarding the theoretical significance of the maximum concurrent flow problem, it can be interpreted as the dual of the linear programming relaxation of the sparsest cut problem. A sparsest cut is defined as a cut that minimizes the ratio between the capacity of the cut and the total demand<tbc>

