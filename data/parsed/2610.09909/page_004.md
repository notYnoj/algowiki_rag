and demonstrate through numerical experiments that it provides an effective refinement criterion on hierarchical T-meshes.

The remainder of this paper is organised as follows. Section 2 introduces the hierarchical T-spline spaces and presents the proposed least-squares UnCut FEM scheme. Section 3 establishes stability and derives _a priori_ error estimates. In Section 4, we construct a residual- based _a posteriori_ error indicator and prove its reliability and efficiency. Section 5 reports numerical experiments that confirm the optimal convergence rates and illustrate the performance of the adaptive mesh refinement strategy. Finally, concluding remarks are given in Section 6.

## 2. UnCut FEM for the Poisson equation

We consider a hierarchical T-mesh \(\hat{\mathcal{T}}_h\) as the computational background mesh over the rectangular domain \(\hat{\Omega}=[0,1]^d\). A T-mesh facilitates local refinement by permitting T- junctions, which are grid-line endpoints terminating at the midpoint of an adjacent element edge. Following the notation established in \[32\], we define the PHT-spline space over \(\hat{\mathcal{T}}_h\) as

\(\mathcal{S}(p,q,\alpha,\beta,\hat{\mathcal{T}}_h):=\left\{s\in C^{\alpha,\beta}(\hat{\Omega})|s|_T\in\mathbb{P}_{p,q}\forall T\in\hat{\mathcal{T}}_h\right\},\) (2.1)

where P_<sub>p,q</sub>_ denotes the space of bivariate tensor-product polynomials of bi-degree (_p,q_) on each element, and \(C^{\alpha,\beta}(\hat{\Omega})\) encodes the prescribed inter-element smoothness. For simplicity, we focus on the symmetric case _p=q_. To ensure global _C_<sup>1</sup> continuity and maintain the nestedness of the basis functions during local refinement, it is mathematically required that \(p,q\ge 3\) \[33\]. In this work, we employ the spline space \(\mathcal{S}(k,k,\alpha,\beta,\hat{\mathcal{T}}_h)\), where _k_ denotes the polynomial degree and we set \(p=q=k\ge 3\), ensuring at least _C_<sup>1</sup> continuity with \(\alpha,\beta\ge 1\). Some intermediate estimates below are valid already for \(k\ge 2\); however, they are used only under this standing assumption and do not yield a _k_=2 version of the main results.

Following the standard hierarchical construction \[2,15\], one obtains a set of global basis functions \(\{R_a\}_{a=1}^{N_a}\subset\mathcal{S}(3,3,1,1,\hat{\mathcal{T}}_h)\), where the dimension _N<sub>a</sub>_ is directly associated with the number of crossing vertices and T-vertices. For efficient numerical implementation, these basis functions are constructed element-wise via Bézier extraction. Specifically, for each leaf element \(T\in\hat{\mathcal{T}}_h\), there exists an extraction matrix **C**_<sub>T</sub>_ such that the restriction of the basis functions to _T_ is expressed as a linear combination of the local tensor-product Bernstein basis \(\{B_j\}_{j=1}^{(k+1)^2}\) defined on the reference square \(\hat{T}=[-1,1]^2\). Based on these, we define the discrete space as

\(V_h:=\left\{v_h:\hat{\Omega}\rightarrow\mathbb{R}:v_h(\mathbf{x})=\sum_{a=1}^{N_a}v_aR_a(\mathbf{x}),v_a\in\mathbb{R}\right\}.\) (2.2)

The space _V<sub>h</sub>_ inherits several critical properties for adaptive analysis. First, for \(k\ge 3\), _V<sub>h</sub>_ is globally _C_<sup>1</sup>-continuous, which is particularly advantageous for Galerkin formulations involving second-order operators. Second, the hierarchical structure enables truly local mesh adaptivity while preserving the linear independence of the basis. Consequently, T-junctions do not introduce independent degrees of freedom (DOFs); instead, the extraction operator **C**_<sub>T</sub>_ implicitly enforces the necessary _C_<sup>1</sup> constraints across interfaces of differing refinement levels, ensuring a seamless coupling of the global solution.

### 2.1. Unfitted mesh.

Let \(\phi\) be a smooth level-set function, and let \(\phi_h\in V_h\) be a high-order approximation of \(\phi\). We define the discrete interface as \(\Gamma_h:=\{\mathbf{x}:\phi_h(\mathbf{x})=0\}\). Let T_<sub>h</sub>_ be the submesh of \(\hat{\mathcal{T}}_h\) obtained by discarding all elements whose closures lie entirely outside the discrete domain \(\{\mathbf{x}:\phi_h(\mathbf{x})<0\}\). We define the sets of interior cells and cut (strip) cells by

\(\mathcal{T}_h^\mathrm{in}:=\{T\in\mathcal{T}_h:T\cap\Gamma_h=\varnothing\},\)<br>
\(\mathcal{T}_h^\Gamma:=\{T\in\mathcal{T}_h:T\cap\Gamma_h\neq\varnothing\},\)

