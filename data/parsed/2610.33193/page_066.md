By Lemma 2.12, we know that (G_<sub>Q</sub>_)<sub>|_f_<sup>-1</sup>(_y_)</sub> is the distribution that minimizes this quantity. When (G_<sub>Q</sub>_)<sub>|_f_<sup>-1</sup>(_y_)</sub> is undefined, it must be the case that \(Q(x)=\infty\) for every \(x\in f^{-1}(y)\). In such cases, any distribution over these inputs must release infinite expected heat.

**Corollary C.2.** _Let f be an arbitrary function with domain D and_ \(Q:D\rightarrow\mathbb{R}_{\ge 0}\cup\{\infty\}\) _be a valid heat function for computing f such that_ \(Q(x)\in\mathbb{R}_{\ge 0}\) _for some_ \(x\in D\)_. Then any input distribution_ D<sup>∗</sup> _over D that minimizes the entropy production of applying a gate computing f with heat function Q must have conditional distributions_ \(\mathcal{D}_{|f^{-1}(y)}^*=(\mathcal{G}_Q)_{|f^{-1}(y)}\) _and the distribution f_(D<sup>∗</sup>) _must only have support on the y where_ (G_<sub>Q</sub>_)<sub>|_f_<sup>-1</sup>(_y_)</sub> _is defined and that minimize_ EP_<sub>g</sub>_((G_<sub>Q</sub>_)<sub>|_f_<sup>-1</sup>(_y_)</sub>).

_Proof._ The entropy production on an input distribution D is given by:

\(\mathsf{EP}_g(\mathcal{D})=\mathbb{E}_{x\sim\mathcal{D}}[Q(x)]+\mathcal{S}(f(\mathcal{D}))-\mathcal{S}(\mathcal{D})\)<br>
\(=\mathbb{E}_{y\sim f(\mathcal{D})}\left[log(1/\mathrm{Pr}_{f(\mathcal{D})}[y])+\mathbb{E}_{x\sim\mathcal{D}_{|f^{-1}(y)}}\left[Q(x)-\mathrm{log}(1/\mathrm{Pr}_\mathcal{D}[x])\right]\right]\)<br>
\(=\mathbb{E}_{y\sim f(\mathcal{D})}\left[\mathbb{E}_{x\sim\mathcal{D}_{|f^{-1}(y)}}\left[Q(x)\right]-\mathcal{S}(\mathcal{D}_{|f^{-1}(y)})\right]\)<br>
\(=\mathbb{E}_{y\sim f(\mathcal{D})}[\mathsf{EP}_g(\mathcal{D}_{|f^{-1}(y)})]\)

The entropy production can be expressed as a convex combination of the entropy production for the different conditional distributions. Lemma C.1 exactly characterizes what these conditional distributions look like. Due to convexity, any optimal distribution must have all of its probability mass on _x_ where EP_<sub>g</sub>_(D<sub>|_f_<sup>-1</sup>(_f(x_))</sub>) is minimized.

We now use heat functions to reprove the decomposition of entropy production into the sum of terms first presented in \[WK20\]. Intuitively, in Proposition C.3, D<sup>∗</sup> represents the distribution on inputs to gate _g_ for which the heat function G is optimal (i.e., that minimizes entropy production), and D represents the true distribution, incurring a higher entropy production. The difference is known as the _mismatch cost_. The significance of Proposition C.3 is that this mismatch cost can be characterized purely information theoretically in terms of D and D<sup>∗</sup> (specifically by the KL-divergence terms _D_<sub>KL</sub>(D||D<sup>∗</sup>)-_D_<sub>KL</sub>(_f_(D)||_f_(D<sup>∗</sup>)). In other words the way the physics of the device implementing the gate influences the extra entropy production is entirely contained in its optimal distribution D<sup>∗</sup>. Our proof of this result uses the language of heat functions, but is similar to that in \[WK20\].

**Proposition C.3** (\[WK20\])**.** _Let g be a gate computing function f with domain D, and valid heat function Q. Let_ D _be any input distribution over D, and_ D<sup>∗</sup> _be another input distribution over D where_ \(\mathrm{supp}(f(\mathcal{D}))\subseteq\mathrm{supp}(f(\mathcal{D}^*))\) _and_ \(\mathcal{D}_{|f^{-1}(y)}^*=(\mathcal{G}_Q)_{|f^{-1}(y)}\) _for every y where both of these distributions are defined. If_ (G_<sub>Q</sub>_)<sub>|_f_<sup>-1</sup>(_y_)</sub> _is undefined for some_ \(y\in\mathrm{supp}(f(\mathcal{D}))\) _then_ \(\mathsf{EP}_g(\mathcal{D})=\infty\)_. Otherwise, the entropy production of applying g on_ D _is:_<tbc>

\(\mathsf{EP}_g(\mathcal{D})=\mathbb{E}_{y\sim f(\mathcal{D})}[\mathsf{EP}_g((\mathcal{G}_Q)_{|f^{-1}(y)})]+D_\mathrm{KL}(\mathcal{D}||\mathcal{D}^*)-D_\mathrm{KL}(f(\mathcal{D})||f(\mathcal{D}^*))\)

<tbc>_Proof._ If \(\mathrm{supp}(\mathcal{D})\unknown\subseteq\mathrm{supp}(\mathcal{D}^*)\) then there must be some \(x\in\mathrm{supp}(\mathcal{D})\) where \(Q(x)=\infty\). We would immediately have that \(\mathsf{EP}_g(\mathcal{D})=\infty\) and also \(D_\mathrm{KL}(\mathcal{D}||\mathcal{D}^*)=\infty\) while the remaining terms on the right-hand side of the equality would be finite. Thus, we can assume without loss of generality that \(\mathrm{supp}(\mathcal{D})\subseteq\mathrm{supp}(\mathcal{D}^*)\).

\(\mathsf{EP}_g(\mathcal{D})=\mathcal{S}(f(\mathcal{D}))-\mathcal{S}(\mathcal{D})+\mathbb{E}_{x\sim\mathcal{D}}[Q(x)]\) (16)

