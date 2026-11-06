As stated previously, to achieve the desired running time, we will not be able to maintain the exact solution descendants for an (unknown) optimal solution C for \(\Pi_\mathcal{P}(\alpha,h)\), and instead will be working with their representatives. This makes the (recursive) computation of \(\Pi_\mathcal{P}(\alpha,h)\) way more tedious, as for instance, if \(\gamma\) is a representative for \(\beta\in\mathcal{C}\), we do not know how \(\beta\) intersects with other cycles from C, when \(\gamma\neq\beta\). We need a way by which we can still account for contributions of edges in the selected cycles to \(\Pi_\mathcal{P}(\alpha,h)\), and we will see how we can still do it using the representatives, by carefully going over the following scenarios. Let \(\{\beta_i|i\in[b]\}\) be the set of solution descendants of \(\alpha\) in C, where for \(i\in[b]\), \(\gamma_i\) is the representative of \(\beta_i\) (see Observation 5.3 (1)). Furthermore, let \(R=\{\gamma_i|i\in[b]\}\) and for \(i\in[b]\), let \(\Gamma_i=\Gamma_{\alpha,R,\gamma_i}\). For each \(i\in[b]\), we will maintain a state \(\theta_i\) which (intuitively discussed below) will help capture the unknown intersections of \(\beta_i\) with cycles from \(\Gamma_i\), which will be enough for our purpose due to Lemma 5.2.

1. If \(\gamma_i=\beta_i\), we will denote this by \(\theta_i=\mathsf{e}\), where, intuitively, e will stand for "equal".<tbc>

2. If \(\gamma_i\neq\beta_i\) and the cycle \(\beta_i\) does not share an edge with any cycle in \(\Gamma_i\) (or its descendants), we will maintain this state by n, where n will stand for no intersection.<tbc>

3. Now we need to worry about the case when \(\gamma_i\neq\beta_i\) and the cycle \(\beta_i\) intersects with some cycles in \(\Gamma_i\). Recall from Proposition 5.1 that if two shortest cycles share an edge, then their intersection is a path. Moreover, such a path due to intersection of \(\beta_i\) with some cycle in \(\Gamma_i\), must be a subpath of \(\gamma_i\) from Lemma 5.2. Consider the path \(P_i=\beta_i\cap\gamma_i\). We will now look at the intersections of \(\gamma_i\) with cycles in \(\Gamma_i\), and let \(\iota_i^1,\iota_i^2,\cdots\iota_i^{q_i}\) be the ordering of elements in \(\Gamma_i\) based on how the paths \(\gamma_i\cap\iota_i^j\) appear in the clockwise order of \(\gamma_i\) (see Figure 16). Note _P<sub>i</sub>_ (if at all it intersects cycles from \(\Gamma_i\)), must start intersecting the stated path sequence at some \(\psi_i=\iota_i^s\) and ends the intersection at some \(\tau_i=\iota_i^t\) (see Figure 5). We will maintain these first and last paths of intersections in the state \(\theta_i\). We will exploit planarity to ensure the above can be done in the desired amount of time (using Observation 5.5).

To formalize the above we introduce some notations and prove some useful properties.

## Useful Notations.

Consider \(\delta\in V(\mathcal{T})\), and a \(\delta\)-lineage-free set \(R\subseteq\mathcal{M}_\delta\). Recall for \(\gamma\in R\), the set \(\Gamma_{\delta,R,\gamma}=\{\gamma'|\gamma'\in(R\cup\{\delta\})\backslash\{\gamma\},E(\gamma')\cap E(\gamma)\neq\emptyset\}\) is the \((\delta,R,\gamma)\)-relevant subset of<tbc>

1
2
i
yi
qi
3
i
i
i

Figure 16: Illustration of \(\gamma_i\) and its intersections with cycles in \(\Gamma_i\), for \(i\in[b]\).

