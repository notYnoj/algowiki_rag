of the circuit. This leads to a source of entropy production due to the locality of operations that are not injective. This source of entropy production was first identified in \[WK20\], where it was shown that the entropy production of applying a gate in a circuit is at least the drop in mutual information between the wires in this gate and the state of the remaining wires of the circuit. We prove essentially the same result, showing that it is an immediate consequence of the locality of valid heat functions.

**Proposition D.1** (\[WK20\])**.** _Let_ C _be a thermodynamic circuit with W wires, and let X,Y be a partition of_ \[_W_\] _and_ C<sub>_t_-1</sub>\[_X_\],C<sub>_t_-1</sub>\[_Y_\]∼D<sub>_t_-1</sub> _be random variables for the state of the wires in X,Y after applying gate t_-1 _in_ C_. Let_ D_<sub>X</sub> be the marginal distribution of random variable_ C<sub>_t_-1</sub>\[_X_\] _according to distribution_ D<sub>_t_-1</sub>_. Then if gate g<sub>t</sub> computes the function_ \(f^{g_t}:\Sigma^X\rightarrow\Sigma^X\) _and has valid heat function Q<sub>g<sub>t</sub></sub>, the entropy production of applying g<sub>t</sub> as the next gate in_ C _is_ \(\mathsf{EP}_{g_t}^\mathsf{Loc}(\mathcal{D}_X)+\mathcal{I}(\mathcal{C}_{t-1}[X];\mathcal{C}_t[Y])-\mathcal{I}(\mathcal{C}_t[X];\mathcal{C}_t[Y])\).

_Proof._ By Definition 2.25,<tbc>

\(\mathbb{E}_{x\sim\mathcal{D}_X}[Q_{g_t}(x)]=\mathsf{EP}_{g_t}^\mathsf{Loc}(\mathcal{D}_X)+\mathcal{S}(\mathcal{C}_{t-1}[X])-\mathcal{S}(\mathcal{C}_t[X])\)

<tbc>Let D_<sub>t</sub>_ be the distribution over states of the circuit after applying _g<sub>t</sub>_. Since C<sub>_t_-1</sub>\[_Y_\] is the same as C_<sub>t</sub>_\[_Y_\], we know that according to Definition 2.24:

\(\mathsf{EP}_{g_t}(\mathcal{D}_{t-1})=\mathbb{E}_{x\sim\mathcal{D}_{t-1}}[Q_{g_t}(x_X)]+\mathcal{S}(\mathcal{D}_t)-\mathcal{S}(\mathcal{D}_{t-1})\)<br>
\(=\mathbb{E}_{x\sim\mathcal{D}_X}[Q_{g_t}(x)]+\mathcal{S}(\mathcal{D}_t)-\mathcal{S}(\mathcal{D}_{t-1})\)<br>
\(=\mathsf{EP}_{g_t}^\mathsf{Loc}(\mathcal{D}_X)+\mathcal{S}(\mathcal{C}_{t-1}[X])-\mathcal{S}(\mathcal{C}_t[X])+\mathcal{S}(\mathcal{D}_t)-\mathcal{S}(\mathcal{D}_{t-1})\)<br>
\(=\mathsf{EP}_{g_t}^\mathsf{Loc}(\mathcal{D}_X)+\mathcal{S}(\mathcal{C}_{t-1}[X])-\mathcal{S}(\mathcal{C}_t[X])+\mathcal{S}(\mathcal{C}_t[X],\mathcal{C}_t[Y])-\mathcal{S}(\mathcal{C}_{t-1}[X],\mathcal{C}_t[Y])\)<br>
\(=\mathsf{EP}_{g_t}^\mathsf{Loc}(\mathcal{D}_X)+\mathcal{S}(\mathcal{C}_{t-1}[X])-\mathcal{S}(\mathcal{C}_t[X])+\mathcal{S}(\mathcal{C}_t[X]|\mathcal{C}_t[Y])-\mathcal{S}(\mathcal{C}_{t-1}[X]|\mathcal{C}_t[Y])\)<br>
\(=\mathsf{EP}_{g_t}^\mathsf{Loc}(\mathcal{D}_X)+\mathcal{I}(\mathcal{C}_{t-1}[X];\mathcal{C}_t[Y])-\mathcal{I}(\mathcal{C}_t[X];\mathcal{C}_t[Y])\)

as desired.

Thus we can decompose entropy production into a term based off of sub-optimal computation on the marginal input distribution plus the drop in mutual information caused by the locality constraint on heat functions.

