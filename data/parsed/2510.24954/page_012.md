### Noisy Version of G_<sub>k</sub>_.

We now introduce a noisy variant of the graph family G_<sub>k</sub>_, which we call \(\widetilde{\mathcal{G}}_k(c,d,p)\). It is defined as \(\widetilde{\mathcal{G}}_k(c,d,p)=\{\widetilde{G}(p)|G\in\mathcal{G}_k(c,d)\}\), where \(\widetilde{G}(p)\) denotes the (random) graph obtained from a given _G_ when deleting each edge independently with probability _p_. \(\widetilde{\mathcal{G}}_k(c,d,p)\) is thus a family of random graphs that we obtain from the elements of G_<sub>k</sub>(c,d_) by deleting each edge independently with probability _p_. Here _p_ should not be thought of as an absolute constant, but a function of _c,d,r_ that is inversely proportional to the diameter of _G_.

Intuitively, the problem with G_<sub>k</sub>_ is that it has an extremely rigid structure that can be exploited by Steiner shortcuts. By randomly deleting edges, \(\widetilde{\mathcal{G}}_k(c,d,p)\) destroys this structure. We highlight the following open problem, the resolution of which would either refute Conjecture 2 or contribute a significant step toward computing almost optimal Steiner shortcuts, either of which would be very exciting.

**Question 3.2.** _Are there parameters_ \(k\ge 2,c,d,p\) _for which any Steiner shortcut for an m-edge graph_ \(G\in\widetilde{\mathcal{G}}_k(c,d,p)\) _cannot simultaneously have size m_<sup>1+_o_(1)</sup> _and diameter m_<sup>_o_(1)</sup> ?

We report some partial progress towards answering Question 3.2 by showing, in a formal sense, that \(\widetilde{\mathcal{G}}_k(c,d,p)\) is indeed harder to shortcut than G_<sub>k</sub>(c,d_). The following theorem, which will be proved in Section 3.3, shows that \(\widetilde{\mathcal{G}}_k(c,d,p)\) requires _t_-thick Steiner shortcuts for \(t>(1+\Omega(1))k\). In contrast, Theorem 3.1 applies only when \(t\le 0.99k\).

**Theorem 3.3.** _For_ \(k\ge 2\)_, there are parameters c,d,p such that with probability_ 1-1/poly(_m), every t-thick Steiner shortcut for the m-edge graph_ \(G\in\widetilde{\mathcal{G}}_k(c,d,p)\) _requires either diameter_ \(m^{\Omega(1/k)}\) _or_ \(m^{1+\Omega(1/k)}\) _edges, provided that_ \(1.01t\le\frac{8}{7}k\) _and_ \(m=2^{\omega(k\mathrm{log}k)}\).

## 3.1 Basic Properties

We begin with some basic properties of G_<sub>k</sub>_ that are helpful for proving lower bounds. Let \(G\in\mathcal{G}_k\) be a graph in this graph family with the parameters \(r,\ell\), etc. defined as usual; see Definition 2.6.

Suppose \(G_+=(V\cup V_+,E\cup E_+)\) is a Steiner shortcut graph for _G_. For each critical pair \((s,t)\in P\), designate one shortest _s-t_ path in _G_<sub>+</sub> a _critical shortest path_.<sup>5</sup> We call the shortcut edge set _E_<sub>+</sub> _normalized_ if it is contained in \((L_i\times V_+)\cup(V_+\times V_+)\cup(V_+\times L_j)\), for two layers _L<sub>i</sub>,L<sub>j</sub>_, \(i+k\le j\). Lemma 3.4 shows that any shortcut edge set _E_<sub>+</sub> can be replaced by the union of \(O((k\ell)^2)\) normalized shortcut sets, without increasing the diameter too much.

**Lemma 3.4.** _Let_ \(G\in\mathcal{G}_k\) _and G_<sub>+</sub> _be a t-thick Steiner shortcut for G with M edges and diameter h. There is a t-thick Steiner shortcut_ \(G'=(V\cup V',E\cup E')\) _for G such that_ \(E'\) _is the union of less than_ \((\ell k)^2\) _normalized t-thick shortcut sets, each with at most M edges. The diameter of_ \(G'\) _is less than hk._

_Proof._ For _i,j_ such that \(i+k\le j\), let \(E'_{i,j}\) be a copy of _E_<sub>+</sub> restricted to \((L_i\times V_+)\cup(V_+\times V_+)\cup(V_+\times L_j)\). Let \(E'\) be the union of all such \(E'_{i,j}\), where each uses a disjoint copy of the Steiner vertices _V_<sub>+</sub>. Every path in _G_<sub>+</sub> from _L<sub>i</sub>_ to _L<sub>j</sub>_ via _V_<sub>+</sub> is preserved by an equivalent path in \(G'\), so long as \(i+k\le j\). Thus, given a length-_h_ path in _G_<sub>+</sub>, we can find a corresponding length-_h(k_-1) path in \(G'\), as every subpath from _L<sub>i</sub>_ to _L<sub>j</sub>_, via zero or more hops in _V_<sub>+</sub>, with _j\<i+k_ may need to be replaced by a length-(_j-i_) path.

### Efficiency.

Let \(G\in\mathcal{G}_k\) and \(G'=(V\cup V',E\cup E')\) be a Steiner shortcut for _G_ such that \(E'=\bigcup E'_{i,j}\) is the union of disjoint normalized shortcut sets \(E'_{i,j}\). We say that a critical shortest path \(\Pi\) in \(G'\) is \(E'_{i,j}\)_-respecting_ if a subpath of \(\Pi\) from _L<sub>i</sub>_ to _L<sub>j</sub>_ is contained in \(E'_{i,j}\).

<sup>5</sup>Note that _G_ contains a unique critical path from _s_ to _t_ whereas _G_<sub>+</sub> may contain many _s-t_ paths.

