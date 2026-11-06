<tbc>so that \(\mathcal{T}_h=\mathcal{T}_h^\mathrm{in}\cup\mathcal{T}_h^\Gamma\) and \(\mathcal{T}_h^\mathrm{in}\cap\mathcal{T}_h^\Gamma=\emptyset\). Correspondingly, we introduce the open domains

\(\Omega_h^\mathrm{in}:=\big(\bigcup_{T\in\mathcal{T}_h^\mathrm{in}}T\big)^\circ,\Omega_h^\Gamma:=\big(\bigcup_{T\in\mathcal{T}_h^\Gamma} T\big)^\circ,\text{and}\Omega_h:=\big(\bigcup_{T\in\mathcal{T}_h}T\big)^\circ,\)

which satisfy \(\Omega_h^\mathrm{in}\cap\Omega_h^\Gamma=\emptyset\) and \(\Omega_h=\big(\overline{\Omega_h^\mathrm{in}}\cup\overline{\Omega_h^\Gamma}\big)^\circ\). To account for the overlapping supports of the spline basis functions, we further introduce an extended domain \(\widetilde{\Omega}_h\), defined as the union of the supports of all basis functions that intersect \(\Omega_h\), so that \(\Omega_h\subset\widetilde{\Omega}_h\subset\hat{\Omega}\).

Let \(\mathcal{F}_h^\Gamma\) denote the set of interior facets of T_<sub>h</sub>_ that are either intersected by the discrete interface \(\Gamma_h\) or are incident to a cut element. For the hierarchical T-mesh, we denote the diameter of a cell \(T\in\hat{\mathcal{T}}_h\) by _h<sub>T</sub>_, and define the minimum and maximum mesh sizes as

\(h_m:=\mathrm{min}_{T\in\hat{\mathcal{T}}_h}h_T,h_M:=\mathrm{max}_{T\in\hat{\mathcal{T}}_h}h_T,\)

respectively. Throughout the analysis, we set \(h:=h_M=\mathrm{max}_{T\in\hat{\mathcal{T}}_h}h_T\). Figure 1 illustrates the hierarchical T-mesh and the domain partitioning.

**Assumption 2.1.** _We assume that the level-set function_ \(\phi\)_, its approximation_ \(\phi_h\in V_h\)_, and the hierarchical T-mesh satisfy the following properties:_

(P1) \(\phi\in C^{k+1}(\hat{\Omega})\) _and the exact interface is given by_ \(\Gamma:=\{\mathbf{x}\in[0,1]^d:\phi(\mathbf{x})=0\}\)_. There exist constants_ \(\delta_0,c_d,C_d>0\)_, independent of h, such that_<tbc>

<tbc>\(|\nabla\phi(\mathbf{x})|\ge c_d,c_d\mathrm{dist}(\mathbf{x},\Gamma)\le|\phi(\mathbf{x})|\le C_d\mathrm{dist}(\mathbf{x},\Gamma),\)<tbc>

<tbc>_for all_ \(\mathbf{x}\in U_{\delta_0}(\Gamma)\).<tbc>

(P2) \(\phi_h\in V_h\) _satisfies the following approximation estimates:_<tbc>

\(\|\phi-\phi_h\|_{L^2(\Omega_h)}\le Ch^{k+1}\|\phi\|_{H^{k+1}(\widetilde{\Omega}_h)},\) \(\text{(2.3)}\)

\(\|\phi-\phi_h\|_{H^1(\Omega_h)}\le Ch^k\|\phi\|_{H^{k+1}(\widetilde{\Omega}_h)}.\) \(\text{(2.4)}\)

_In addition, the approximation is assumed to satisfy_

\(\|\phi-\phi_h\|_{L^\infty(\hat{\Omega})}+h\|\nabla(\phi-\phi_h)\|_{L^\infty(\hat{\Omega})}+h^2\|D_h^2(\phi-\phi_h)\|_{L^\infty(\hat{\Omega})}\le Ch^{k+1}\|\phi\|_{W^{k+1,\infty}(\hat{\Omega})},\) \(\text{(2.5)}\)



Figure 1. Schematic of the computational domain \(\hat{\Omega}\) and the associated background mesh \(\hat{\mathcal{T}}_h\). The green and pink cells represent the interior cells \(\mathcal{T}_h^\mathrm{in}\) and cut cells \(\mathcal{T}_h^\Gamma\), respectively. The solid red line denotes \(\Gamma_h\). Furthermore, green and orange edges indicate the boundary edges in \(\partial\Omega_h\) and the interface

associated facets in \(\mathcal{F}_h^\Gamma\), respectively.

