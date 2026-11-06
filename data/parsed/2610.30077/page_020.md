## A Proofs and derivations

This appendix gives a complete and self-contained details of the proof and derivation that the main text presents only in brief: the exact equivalence of the SAV reformulation, the proof of Proposition 2.1, the G-stability identity used in Theorem 4.1, the complete proof of Theorem 4.1 itself, the filtered-scheme stability extension of Remark 4.2, and the complete proof of Theorem 5.1.

Almost every step below uses one recurring trick, standard in the weak or variational treatment of differential equations: rather than solving an equation like \(\partial_t\phi=\) (some expression) pointwise, we multiply both sides by a chosen function _g_ (a test function) and integrate over \(\Omega\), writing the result as the inner product \(\left(\partial_t\phi,g\right):=\int_\Omega(\partial_t\phi)g\mathrm{d}x\) (Section 3.1). Below, "testing equation (X) with _g_" always means exactly this: multiply equation (X) by _g_ and integrate over \(\Omega\). Choosing _g_ well (often \(g=\mu\), _g=q_, or the constant _g_=1) lets a derivative move off the unknown and onto _g_ by integration by parts, with no leftover boundary term, because \(\Omega\) is periodic and has no boundary at all: these are identities (6a) and (6b) of Section 3.1. We prove them here, since they are used in essentially every computation below. For any scalar field _g_ and vector field _F_, the product rule for the divergence gives<tbc>

\(\nabla\cdot(gF)=\left(\nabla g\right)\cdot F+g\left(\nabla\cdot F\right),\text{i.e.}g\left(\nabla\cdot F\right)=\nabla\cdot(gF)-\left(\nabla g\right)\cdot F.\)

<tbc>Integrating both sides over \(\Omega\),<tbc>

\(\int_\Omega g\left(\nabla\cdot F\right)\mathrm{d}x=\int_\Omega\nabla\cdot(gF)\mathrm{d}x-\int_\Omega(\nabla g)\cdot F\mathrm{d}x.\)

<tbc>By the divergence theorem, \(\int_\Omega\nabla\cdot(gF)\), \(\mathrm{d}x=\oint_{\partial\Omega}(gF)\cdot n,\mathrm{d}S\), where _n_ denotes the outward unit normal to \(\partial\Omega\). For a periodic domain \(\Omega\), the boundary integral vanishes because opposite faces are identified. By periodicity, the values of _g_ and _F_ agree at corresponding points on opposite faces. However, the outward unit normals at these points have opposite directions. Consequently, the corresponding flux contributions cancel pairwise, yielding \(\oint_{\partial\Omega}(gF)\cdot n,\mathrm{d}S=0\). Thus, the integral of \(\nabla\cdot(gF)\) over \(\Omega\) vanishes for any periodic fields _g_ and _F_. Hence<tbc>

\(\int_\Omega g\left(\nabla\cdot F\right)\mathrm{d}x=-\int_\Omega(\nabla g)\cdot F\mathrm{d}x,\text{i.e.}\left(\nabla\cdot F,g\right)=-\left(F,\nabla g\right),\)

<tbc>which is exactly (6a). Identity (6b) follows at once by taking \(F=\nabla u\) for a scalar field _u_, since then \(\nabla\cdot F=\nabla\cdot(\nabla u)=\Delta u\):<tbc>

\(\left(\Delta u,g\right)=\left(\nabla\cdot(\nabla u),g\right)=-\left(\nabla u,\nabla g\right).\)

