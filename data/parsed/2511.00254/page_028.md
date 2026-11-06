## B Randomized Rounding for Maximization

In this section, we prove Theorem 4.4.

_Proof._ Let \(\nu,\gamma\in(0,1)\) be constants, sufficiently small so that \(\frac{1-\gamma}{1+\nu}\ge 1-\epsilon\) (for example, \(\nu=\gamma=\epsilon^2\) suffices).

Let P be the set of support paths of _f_. We first proceed with some assumptions about the input data. By scaling _w_, we may assume \(w(h)\le 1\) for each \(h\in E(H)\) and _w_<sub>max</sub>=1. Finally, observe that we may assume \(f(P)<\frac{1}{\mathrm{log}^2n}\) for each \(P\in\mathcal{P}\). Otherwise we can decompose _f=f_<sub>1</sub>+_f_<sub>2</sub> where _f_<sub>2</sub>(_P_) is some multiple of \(\frac{1}{\mathrm{log}^2n}\) and \(f_1(P)<\frac{1}{\mathrm{log}^2n}\) (for each _P_, let _k<sub>P</sub>_ be the maximum positive integer such that \(f(P)-\frac{k_P}{\mathrm{log}^2n}\ge 0\) and define \(f_2(P)=\frac{k_P}{\mathrm{log}^2n}\) ). Then we can apply the lemma to _f_<sub>1</sub> to obtain \(\hat{f}_1\), and \(\hat{f}=\hat{f}_1+f_2\) satisfies the desired properties for the original flow _f_.

Proceeding under the above assumptions, define an integral flow \(\bar{f}\) by independently assigning each \(\hat{f}(P)\) to 1 with probability \(\mathrm{log}^2n\cdot f(P)\in[0,1)\) and otherwise assigning it 0. We use the following Chernoff bounds.

**Lemma B.1** (Chernoff Bounds)**.** _Let X_<sub>1</sub>_,...,X<sub>k</sub> be mutually independent random variables where_ \(X_i\in[0,1]\)_. Let_ \(X=\sum_iX_i\) _and let_ \(\mu_\mathrm{max}\ge\mathbb{E}\left[X\right]\ge\mu_\mathrm{min}\)_. The following inequalities hold:_

1. _For any_ \(\delta\ge 1\) _we have_<tbc>

<tbc>\(\mathrm{Pr}\left[X\ge(1+\delta)\mu_\mathrm{max}\right]\le\mathrm{exp}(-\delta\mu_\mathrm{max}/3).\)<tbc>

_2._ _For any_ \(\delta\le 1\) _we have_<tbc>

<tbc>\(\mathrm{Pr}\left[X\le(1-\delta)\mu_\mathrm{min}\right]\le\mathrm{exp}(-\delta^2\mu_\mathrm{min}/2).\)<tbc>

<tbc>How much does \(\bar{f}\) congest an edge _e_? We have that \(\mathbb{E}\left[\sum_{P\unknown e}\bar{f}(P)\right]=\mathrm{log}^2n\cdot\sum_{P\unknown v}f(P)\le\mathrm{log}^2n\) since _f_ is feasible. Let B_<sub>e</sub>_ be the (bad) event that \(\sum_{P\unknown e}f(P)\ge(1+\nu)\mathrm{log}^2n\). Setting \(\mu_\mathrm{max}=\mathrm{log}^2n\) and \(\delta=\nu\) in Theorem B.1, we obtain:<tbc>

\(\mathrm{Pr}\left[\mathcal{B}_v\right]\le\mathrm{exp}(-\nu\mathrm{log}^2n)=n^{-\nu\mathrm{log}n}.\)

<tbc>What value does \(\bar{f}\) achieve? We have that \(\mathbb{E}\left[w(f)\right]=\sum_h\sum_{P\in\mathcal{P}_h}w(P)\mathbb{E}\left[\bar{f}(P)\right]=\mathrm{log}^2n\cdot\sum_h\sum_{P\in\mathcal{P}_h}w(h)f(P)=\mathrm{log}^2n\cdot w(f)\). Let B_<sub>w</sub>_ be the (bad) event that \(w(f')\le(1-\gamma)\mathrm{log}^2n\cdot w(f)\). Setting \(\mu_\mathrm{min}=\mathrm{log}^2n\cdot w(f)\) and \(\delta=\epsilon\) in Theorem B.1, we obtain:

\(\mathrm{Pr}\left[w(f')\le(1-\gamma)\mathrm{log}^2n\cdot w(f)\right]\le\mathrm{exp}(-\gamma^2\mathrm{log}^2n\cdot w(f)/2)=n^{-\gamma^2w(f)/2}\le n^{-\gamma^2/2}\)

where the last inequality follows from \(w(f)\ge w_\mathrm{max}=1\).

Thus by the union bound, the probability that one of the events \((\mathcal{B}_v:v\in E(G))\) or B_<sub>w</sub>_ occurs is at most \(\frac{n^2}{n^{\upsilon logn}}+\frac{1}{n^{\gamma^2/2}}\), which converges to 0. Thus with high probability, we obtain an outcome \(f'\) that avoids all of these bad events.

Now let \(\hat{f}=\frac{1}{(1+\nu)\mathrm{log}^2n}f'\). Since \(f'\) avoids B_<sub>e</sub>_ for each edge _e_, \(\hat{f}\) is feasible. Additionally, since \(f'\) avoids B_<sub>w</sub>_, we have that \(w(\hat{f})=\frac{1}{(1+\nu)}w(f')\ge\frac{(1-\gamma)}{(1+\nu)}w(f)\ge(1+\epsilon)w(f)\).

This procedure can be de-randomized to obtain a deterministic algorithm using pessimistic estimators \[26\].

## C NP-Completeness of Fractional Uncrossed Multiflow

In this section we prove the NP-completeness of deciding the existence of a fractional uncrossed flow satisfying all demands. The proof is reminiscent of a reduction by Middendorf and Pfeiffer \[23\], for the node-disjoint paths problem when _G+H_ is planar. We remark that this shows NP-completeness even for leaf instances of multiflows. We refer to a fractional uncrossed flow which satisfies all demands as a _solution_.

In the first subsection, we show the problem is in NP (which is not necessarily obvious, given that uncrossed fractional multiflow is not a linear program). In the next subsection, we introduce the key gadgets which are used in the proof of NP-hardness, and in the subsection after we present the main proof of NP-hardness.

