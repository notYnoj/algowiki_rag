\(\forall a'\in\{1..a\},f_{a^\prime}^{(\mathrm{in})}=\widehat{f}_{a^\prime}^{(\mathrm{in})}\sqrt{\frac{\sum_{b^{\prime\prime}=1}^b\widehat{w}_{b^{\prime\prime}}^{(\mathrm{out})}}{\sum_{a^{\prime\prime}=1}^a\widehat{w}_{a^{\prime\prime}}^{(\mathrm{in})}}}.\)

This indicates that to enforce the flow conservation property at each internal node, the weights must be multiplicatively scaled up/down so that the new outflow and inflow is the geometric average of the old outflow and inflow. \(\blacksquare\)

## Prediction.

In this step, the algorithm needs to randomly predict with a multipath \(\unknown\) from a distribution D such that \(\mathbb{E}_\mathcal{D}[\unknown]=\mathbf{f}\). In Component Hedge and similar algorithms (Helmbold and Warmuth, 2009; Koolen et al., 2010; Yasutake et al., 2011; Warmuth and Kuzmin, 2008), D is constructed by decomposing **_f_** into a convex combination of small number of solutions. In this section, we give a new and more direct prediction method for multipaths. We construct a distribution D with the right expectation in Stochastic Product Form (see Definition 8) by defining a new set of weights **_w_** using the flow values **_f_**. For each multiedge \(m=(v,U)\in M\), we set the weight _w<sub>m</sub>=f<sub>m</sub>/f_in(_v_). The induced distribution will be in Stochastic Product Form with the right expectation \(\mathbb{E}_\mathcal{D}[\unknown]=\mathbf{f}\). This gives us a faster prediction method as the decomposition is avoided. Lemma 13 shows the correctness and time complexity of our method.

**Lemma 13** _For each multiedge_ \(m=(v,U)\in M\)_, define the weight w<sub>m</sub>=f<sub>m</sub>/f_in(_v). Let the distribution_ D _over the multipaths be_ \(\mathcal{D}(\unknown):=\prod_{m\in M}(w_m)^{\pi_m}\)_. Then:_

1. D _is in Stochastic Product Form._<tbc>

2. \(\mathbb{E}_\mathcal{D}[\unknown]=\mathbf{f}\).<tbc>

_3. Constructing_ D _from the flow values **f** can be done in_ O(_c|M_|) _time where c is an upper-bound on the branching factor of each multiedge (i.e. for all_ \(m=(v,U)\in M\), |_U|\<c)._

## Proof.

\(\mathcal{D}(\unknown)\) is in product form by construction. The weights are also stochastic since for each non-sink vertex _v_:

\(\sum_{m\in M_v^{(\mathrm{out})}}w_m=\sum_{m\in M_v^{(\mathrm{out})}}\frac{f_m}{f_\mathrm{in}(v)}=\frac{1}{f_\mathrm{in}(v)}\sum_{m\in M_v^{(\mathrm{out})}}f_m=\frac{1}{f_\mathrm{in}(v)}f_\mathrm{out}(v)=1\)

Thus the D is in Stochastic Product Form (Definition 8). Now we show that D will result in the desired expectation. Let \(\widehat{\mathbf{f}}:=\mathbb{E}_\mathcal{D}[\unknown]\) be the flow induce by D. Denote \(\widehat{f}_\mathrm{in}(v):=\sum_{m\in M_v^{(\mathrm{in})}}\widehat{f}_m\). Let _v_<sub>1</sub>_,...,v<sub>n</sub>_ be a topological order of the vertices in the underlying DAG. We use strong induction on _n_ to show that \(\widehat{f}_\mathrm{in}(v)=f_\mathrm{in}(v)\) for all \(v\in V\) . For _v_<sub>1</sub>=_s_<tbc>

