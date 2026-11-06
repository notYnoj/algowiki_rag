## A Supplementary Material

### A.1 Discussion on the Invertibility Assumption

Let \(J^\star:=\partial_\theta F(\theta^\star,X_0)\). A sufficient condition for the invertibility assumption in Assumption 1 is local contractivity of the EM map at the limiting fixed point, i.e. \(\|J^\star\|<1\). Moreover, since _F_ is continuously differentiable, \(I-\partial_\theta F(\theta,X)\) remains invertible in a neighbourhood of \((\theta^\star,X_0)\). It is therefore invertible at \((\theta_T,X)\) for sufficiently large _T_ when \(\theta_T\rightarrow\theta^\star\) and _X_ remains in this neighbourhood. The AI method nevertheless requires the corresponding linear system to be nonsingular at every pair \((\theta_T,X)\) where it is evaluated.

The link with identifiability can be seen in a symmetric two-component example, where the component means are \(\pm\mu\) and the weights and covariances are fixed. The EM update then reduces to \(\mu_{t+1}=F(\mu_t)\). When the modes are well separated, Fig. 12a shows that _F_ is strongly contracting around \(\mu^\star\) and that the iterates converge rapidly. When the modes overlap, Fig. 12b shows that \(\partial_\mu F(\mu^\star)\) approaches 1: EM converges slowly and \(1-\partial_\mu F(\mu^\star)\) becomes poorly conditioned.

The invertibility assumption does not hold in specific pathological cases. For instance, let \(\mathcal{I}\subset\mathbb{R}\) be an interval containing 0, and suppose that a differentiable curve \(s\in\mathcal{I}\mapsto\theta(s)\) of fixed points satisfies \(\theta(0)=\theta^\star(\theta_0,X_0)\) and \(\theta'(0)\neq 0\). Differentiating \(F(\theta(s),X_0)=\theta(s)\) at _s_=0 gives \((I-\partial_\theta F(\theta^\star(\theta_0,X_0),X_0))\theta'(0)=0\), so this matrix is singular. For example, consider the dataset _X_<sub>0</sub>=(-1,1) and the Gaussian mixture \((\frac{1}{2}-s)\mathcal{N}(0,1)+(\frac{1}{2}+s)\mathcal{N}(0,1)\). Then \(s\in(-\frac{1}{2},\frac{1}{2})\mapsto\theta(s):=(w(s):=\frac{1}{2}-s,\mu(s):=0,\Sigma(s):=1)\) is such a curve of fixed points.

-μ
0
+μ
updated mean F(μ)
F(μ)
μ
μ
μ
current mean μ
μ
μ
μ
μ
μ
(a) Well-separated modes.
(b) Overlapping modes.

Figure 12: Local behaviour of the EM map in a symmetric two-component example. The grey dashed line is the identity map.

