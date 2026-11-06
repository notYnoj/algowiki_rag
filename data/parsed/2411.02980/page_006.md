<tbc>Definition 1.8 essentially states that the events \(\sigma(v_1)=\text{True}\) and \(\sigma(v_2)=\text{True}\) are asymptotically independent for large _n_, therefore indicating the absence of long-range correlations in a relatively weak sense, as the typical distance between _v_<sub>1</sub> and _v_<sub>2</sub> is \(\Omega(logn)\). Replica symmetry is conjectured to hold up to the condensation threshold \(\alpha_\mathrm{cond}\), which has been verified on a few other models; see e.g. \[COKPZ17, COEJ<sup>+</sup>18\] and the references therein. For random _soft-constraint k_-SAT, it has been shown that replica symmetry is sufficient for the success of the Belief Propagation algorithm \[CMR22\].

While the replica symmetry condition has been extensively discussed in the literature, this property is rarely proved rigorously. In this work, we show replica symmetry holds under the considered densities, which follows immediately from Theorem 1.7.

**Theorem 1.9** (replica symmetry of random _k_-SAT)**.** _Under the condition of Theorem 1.2, the random k-SAT model with density_ \(\alpha\) _is replica symmetric._

Another important property that arises from the study of the random _k_-SAT by statistical physicists is the _(non-)reconstruction_ property \[MM06\], which informally requires one being able to estimate the value of one variable given "far away" observations \[GM07, MRT11\].

For an SAT instance \(\Phi=(V,C)\), we use vbl(_c_) to denote the set of variables involved in _c_ for each clause \(c\in C\). We let \(H_\Phi=(V,\mathcal{E})\) denote the hypergraph where _V_ is the set of variables in \(\Phi\) and \(\mathcal{E}=\{\mathrm{vbl}(c)|c\in C\}\). For a hypergraph _H_, we use \(d_H(\cdot,\cdot)\) to denote the graph-theoretic distance in _H_. Finally, for a hypergraph _H_=(_V,_E), a vertex \(v\in V\) , and any \(r\ge 1\), we let \(\bar{B}_H(v,r)\unknown\{u\in V|d_H(u,v)\ge r\}\) to denote the set of vertices in _V_ with distance to _v_ at least _r_. We then follow \[MRT11\] to give the following formal definition of the non-reconstruction property.

**Definition 1.10** (non-reconstruction)**.** Given \(k,\alpha\), we say that a random _k_-SAT model with density \(\alpha\) is _non-reconstructible_ if, for \(\Phi=(V,C)\sim\Phi(k,n,\lfloor\alpha n\rfloor)\) with the uniform distribution over satisfying assignments \(\mu=\mu_\Phi\) and the induced hypergraph \(H=H_\Phi\), the following holds for any \(v\in V\) :

\(\mathrm{lim}_{r\rightarrow\infty}\mathrm{limsup}_{n\rightarrow\infty}\mathbb{E}\left[d_\mathrm{TV}\left(\mu_{\{v\}\cup\bar{B}_H(v,r)},\mu_v\otimes\mu_{\bar{B}_H(v,r)}\right)\right]=0.\)

We say that the model is _reconstructible_ otherwise. Here, \(\mu_v,\mu_{\bar{B}_H(v,r)},\mu_{\{v\}\cup\bar{B}_H(v,r)}\) denote the marginal distributions induced from \(\mu\) on the subset of variables \(\{v\},\bar{B}_H(v,r),\{v\}\cup\bar{B}_H(v,r)\), respectively.

The non-reconstruction property, which also reflects the absence of long-range correlations, is a stronger condition than replica symmetry \[CMR22\]. In fact, non-reconstructibility is a necessary condition for the rapid mixing of Glauber dynamics or other local Markov chains \[BKMP05\]. Furthermore, non-rigorous statistical mechanics calculations \[MPZ02\] and approximations up to the second order \[MRT11\] strongly suggest that the threshold for non-reconstruction aligns with the clustering threshold \(\alpha_\mathrm{clust}\). However, there is no rigorous proof of this as far as we know. In this work, we demonstrate that non-reconstruction holds under the considered densities, which is again a direct corollary of Theorem 1.7.

**Theorem 1.11** (non-reconstruction of random _k_-SAT)**.** _Under the condition of Theorem 1.2, the random k-SAT model with density_ \(\alpha\) _is non-reconstructible._

We further establish _looseness_ of variables under the considered densities, an intuitive way of characterizing the connectivity of the solution space \[AC08, CGG<sup>+</sup>24\]; see Definition 4.12 and Theorem 4.13 for details.

## 1.3. Technique Overview.

We establish all of the results mentioned above in the context of atomic CSPs. A CSP is considered atomic if each constraint is violated by exactly one assignment in its domain. Any constraint with a constant number _N_ of violating configurations can be decomposed into _N_ atomic constraints. Both SAT and hypergraph coloring instances fall under this category of atomic CSPs.

Our algorithm for counting and sampling atomic CSP solutions is inspired by the recently developed recursive coupling procedure for bounded-degree atomic CSPs in \[WY24\]. Through the novel recursive coupling procedure, \[WY24\] successfully dispenses with the freezing paradigm equipped by the previous approaches \[Bec91, Moi19, FHY21, JPV21\], therefore bypassing the technical barrier and achieving a \(q^k\unknown d^{2+o_q(1)}\) bound for counting/sampling bounded-degree CSPs, where _d_ is the maximum degree of<tbc>

