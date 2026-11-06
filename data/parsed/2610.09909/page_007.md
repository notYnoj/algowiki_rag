<tbc>global mesh parameter _h_:=_h<sub>M</sub>_ throughout Section 3. The locally refined hierarchical T- meshes considered in Section 4 are investigated from the viewpoint of adaptive computation and are not required to satisfy this global mesh-ratio condition.

## 3. Proof of Theorem 2.4

In this section, we present a detailed error analysis of the proposed scheme (1.3). We first establish several technical preliminaries, including stability and approximation results. We then prove the coercivity and continuity of the associated bilinear form, which ensures the well-posedness of the discrete problem. Finally, in Subsection 3.3, we combine these results to derive the optimal _a priori_ error estimates.

### 3.1. Technical results.

**Lemma 3.1** ( \[19, Lemma 3.6\])**.** _For any integer s with_ \(1\le s\le k+1\) _and any_ \(v\in H^s(\Omega_h)\) _that vanishes in_ \(\Omega\)_, it holds that_<tbc>

\(\|v\|_{L^2(\Omega_h\backslash\Omega)}\le Ch^s\|v\|_{H^s(\Omega_h\backslash\Omega)}.\) (3.1)

<tbc>**Lemma 3.2.** _For any_ \(v_h\in S_h\)_, and two neighboring elements K_<sup>+</sup> _and K_<sup>-</sup> _sharing_ \(F\in\mathcal{F}_h^\Gamma\)_, we have the local estimate_<tbc>

\(\|v_h\|_{H^2(K^+)}^2\le C\big(\|v_h\|_{H^2(K^-)}^2+\sum_{j=2}^{2k}h_F^{2j-3}\|\left[\left[\partial_n^jv_h\right]\right]\|_{L^2(F)}^2\big).\) (3.2)

<tbc>_Proof._ By affine changes of variables, it suffices to establish the estimate on each of the finitely many fixed reference macro-elements \(\widehat{K}=\widehat{K}^+\cup\widehat{K}^-\) arising from the 1-regular hierarchical T-mesh, where \(\widehat{K}^+\) and \(\widehat{K}^-\) share a common edge segment \(\widehat{F}\). Let \(\widehat{n}\) be a fixed unit normal to \(\widehat{F}\). We define the finite-dimensional broken polynomial space of degree 2_k_ on \(\widehat{K}\) as:<tbc>

\(X_k(\widehat{K}):=\{\widehat{p}\in L^2(\widehat{K}):\widehat{p}|_{\widehat{K}^\pm}\in\mathbb{Q}_{2k}(\widehat{K}^\pm)\}.\)

<tbc>For any \(\widehat{p}\in X_k(\widehat{K})\), consider the following functional:

\(N(\widehat{p})^2:=\|\widehat{p}\|_{H^2(\widehat{K}^-)}^2+\sum_{j=0}^{2k}\|\left[\left[\partial_n^j\widehat{p}\right]\right]\|_{L^2(\widehat{F})}^2.\)

We first show that \(N(\cdot)\) defines a norm on \(X_k(\widehat{K})\). Suppose \(N(\widehat{p})=0\). The vanishing of the first term implies \(\widehat{p}\equiv 0\) on \(\widehat{K}^-\), which further ensures that all its derivative traces vanish on \(\widehat{F}\) from the side of \(\widehat{K}^-\). The vanishing of the jump terms \(\left[\left[\partial_n^j\widehat{p}\right]\right]=0\) for _j_=0_,...,_2_k_ then strictly forces \(\partial_n^j\widehat{p}^+=0\) on \(\widehat{F}\) for _j_=0_,...,_2_k_. Since \(\widehat{p}|_{\widehat{K}^+}\) has degree at most 2_k_ in the direction normal to \(\widehat{F}\), and we have 2_k_+1 homogeneous conditions on the normal derivatives along the edge \(\widehat{F}\), the factor theorem implies that \(\widehat{p}\) must be identically zero on \(\widehat{K}^+\). Thus \(N(\cdot)\) is a valid norm on \(X_k(\widehat{K})\).

By the equivalence of norms in finite-dimensional spaces, \(N(\cdot)\) dominates the \(H^2(\widehat{K}^+)\)- norm. For our specific discrete function \(v_h\in S_h\), the global _C_<sup>1</sup>-continuity implies \(\left[\left[\partial_n^0v_h\right]\right]=0\) and \(\left[\left[\partial_n^1v_h\right]\right]=0\), which allows the jump summation to effectively start from _j_=2.

Finally, using \(h_{K^+}\simeq h_{K^-}\simeq h_F\) and the affine scaling relations

\(|v_h|_{H^m(K)}^2\simeq h_F^{d-2m}|\widehat{v}_h|_{H^m(\widehat{K})}^2,\left[\left[\left[\partial_n^jv_h\right]\right]\right]\left|\right|_{L^2(F)}^2\simeq h_F^{d-1-2j}\left[\left[\left[\partial_n^j\widehat{v}_h\right]\right]\right]\left|\right|_{L^2(\widehat{F})}^2,\)

we obtain the factor \(h_F^{2j-3}\) and hence (3.2). □

**Lemma 3.3** (Stability property)**.** _For any_ \(v_h\in S_h\)_, we have the following stability estimate_

\(\|v_h\|_{H^2(\Omega_h)}^2\le C\big(\|\Delta v_h\|_{L^2(\Omega_h)}^2+j_h(v_h,v_h)\big).\) (3.3)

