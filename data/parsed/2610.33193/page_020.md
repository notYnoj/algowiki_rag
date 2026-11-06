This is well motivated. Theorem 2 of Turgut \[Tur09\] shows how, in an idealized model, it is possible to implement any fixed mapping from _D_ to _R_ where the expected released heat on every input exactly matches any valid _Q_. If one wishes to reject this assumption, then they should interpret all of our upper bounds on Q and EP as theoretical limits on the best possible lower bounds for these quantities that could be proven in our model. All of our lower bounds on EP and Q hold independently of this axiom.

Excess heat released by a physical process is called the entropy production \[Sei12\]. More formally (recall Definition 2.2 of \(f_\uparrow\)),

**Definition 2.24** (gate entropy production)**.** _Let_ C _be a W-wire circuit and g be a gate in_ C _computing a function f with domain_ \(D=\Sigma^I\) _for_ \(I\subseteq[W]\) _that is assigned heat function Q. The_ entropy production EP_<sub>g</sub> of g on distribution_<sup>23</sup> D _over_ \(\Sigma^W\) _is given by:_

\(\mathsf{EP}_g(\mathcal{D})=\mathcal{S}(f_\uparrow(\mathcal{D}))-\mathcal{S}(\mathcal{D})+\mathbb{E}_{x\sim\mathcal{D}}[Q(x_I)]\)

Note \(\mathcal{S}(f_\uparrow(\mathcal{D}))\) is used in Definition 2.24 instead of S(_f_(D)) since D is a distribution on all _W_ wires. Note that \(\mathcal{S}(f_\uparrow(\mathcal{D}))-\mathcal{S}(\mathcal{D})\) is the _negation_ of the Landauer cost of _f_ on D (Definition 2.19), thus is nonpositive by Definition 2.5. E<sub>_x_∼D</sub>\[_Q(x<sub>I</sub>_)\] is the _entropy flow/heat released_ (see Section 1 for discussion of this term in the broader field of stochastic thermodynamics) in the context of circuits that exchange heat with the environment through their gates.

It is necessary to define EP_<sub>g</sub>_ in the context of the larger circuit, since \(\mathcal{S}(f_\uparrow(\mathcal{D}))-\mathcal{S}(\mathcal{D})\) is a global property of the circuit, while E<sub>_x_∼D</sub>\[_Q(x<sub>I</sub>_)\] is a property of the marginal distribution of D on the coordinates in _I_. We can also define a local equivalent, termed \(\mathsf{EP}_g^\mathsf{Loc}\), to EP_<sub>g</sub>_, which gives a lower bound on the actual entropy production EP_<sub>g</sub>_. In Appendix D we show how these two quantities are related (Proposition D.1).

**Definition 2.25** (local gate entropy production)**.** _Let g be a gate computing a function f with domain D that is assigned a heat function Q. The_ local entropy production \(\mathsf{EP}_g^\mathsf{Loc}\) _of g on input distribution_ D _over D is given by:_

\(\mathsf{EP}_g^\mathsf{Loc}(\mathcal{D})=\mathcal{S}(f(\mathcal{D}))-\mathcal{S}(\mathcal{D})+\mathbb{E}_{x\sim\mathcal{D}}[Q(x)].\)

We are ultimately interested in characterizing the entropy production of a circuit. When a circuit receives some distribution D over its inputs, this could in principal be a marginal distribution where the circuit’s inputs are only a subset of the variables in a larger system, with which the inputs may have mutual information that would call for different heat functions for "globally optimal" heat release for each gate. We give the following definition for the entropy production of a circuit under the assumption that its input distribution D is independent from the outside world.

**Definition 2.26** (circuit entropy production)**.** _Let_ C _be a thermodynamic circuit with gates_ \(g\in G\) _that cleanly computes a function f with domain D. Let_ D _be a distribution over D and_ D_<sub>g</sub> be the induced marginal distribution over inputs for gate g which has heat function Q<sub>g</sub>. The_ circuit entropy production _of_ C _on distribution_ D _is given by_

\(\mathsf{EP}_\mathcal{C}(\mathcal{D})=\mathcal{S}(f(\mathcal{D}))-\mathcal{S}(\mathcal{D})+\sum_{g\in G}\mathbb{E}_{x\sim\mathcal{D}_g}[Q_g(x)]\)

<sup>23</sup>Note D is not the input distribution to the whole circuit, but the induced distribution on all _W_ wires _just prior_ to applying gate _g_.

