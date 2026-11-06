<tbc>with polynomial preprocessing and query times in the Isomorphic-Priors model? Can we obtain near- linear preprocessing time per prior instance and near-linear query time for global minimum vertex cuts in weighted directed graphs \[CMT26, LNP<sup>+</sup>25\], or for generalized Büchi games \[CDHL16\]?<sup>17</sup>

## 4 Related Works

### A Possible Connection to Graph Machine Learning.

While machine learning (ML) is not a focus of this work, we briefly discuss a conceptual connection between our model and graph learning. This discussion is exploratory: our results have formal implications for abstract isomorphism-invariant predictors, but whether these implications can inform the design or training of practical ML models remains to be established.

Consider an ML model _M_ that takes a graph _G_ as input and outputs some value _M(G_). We call such a model _isomorphism-invariant_ if, for every pair of isomorphic input graphs \(G\cong H\), we have _M(G_)=_M(H_). Isomorphism-invariance is a natural requirement for graph-level prediction tasks in which vertex identifiers carry no semantic meaning, and is a standard design principle in graph representation learning \[MBSL19, KP19\]. Examples of isomorphism-invariant prediction targets include structural graph quantities such as triangle counts, diameter, and chromatic number, as well as the optimal values of combinatorial optimization problems such as Maximum Cut or Traveling Salesman Problem. Many commonly used graph-learning architectures satisfy this symmetry by design: message-passing Graph Neural Networks (GNNs), when equipped with a permutation- invariant graph-level readout, yield isomorphism-invariant predictors \[XHLJ19, MRF<sup>+</sup>19\]; higher- order invariant GNN architectures have been developed as well \[MBSL19, KP19\]. Several Graph Transformer architectures similarly incorporate isomorphism-respecting structural or positional encodings \[KBH<sup>+</sup>21\]. The following observation gives a concrete connection between our model and the construction of isomorphism-invariant graph predictors.

**Observation 4.1.** _Let P be an isomorphism-invariant function on graph instances that does not admit an algorithm with preprocessing and query times polynomial in n and k in the Isomorphic-Priors model. Then there is no training procedure that, for every correctly labeled training set_

\(\mathcal{S}=\{(G_1,P(G_1)),\dots,(G_k,P(G_k))\},\)

_constructs an isomorphism-invariant predictor M_<sub>S</sub> _satisfying all of the following:_

• Efficiency: _The training time, inference time, and description length of M_<sub>S</sub> _are each polynomial in n and k._<tbc>

• Training completeness: _The predictor answers correctly on every training example: M_<sub>S</sub>(_G<sub>i</sub>_)=_P(G<sub>i</sub>_) _for every_ \(i\in[k]\).<tbc>

• Soundness: _The predictor never returns an incorrect answer: For every query graph H,_ \(M_\mathcal{S}(H)\in\{P(H),\perp\}\)_, where_ \(\perp\) _denotes abstention._

_Proof._ Suppose such a training procedure exists. We use it to compute _P_ in the Isomorphic-Priors model.

During preprocessing, given the prior graphs _G_<sub>1</sub>_,...,G<sub>k</sub>_ together with _P(G_<sub>1</sub>)_,...,P(G<sub>k</sub>_), we run the training procedure on the corresponding training set S and store the resulting predictor _M_<sub>S</sub>.

Given a query graph _H_, we evaluate _M_<sub>S</sub>(_H_). If the output is not \(\perp\), we return it; otherwise, we report that _H_ is not isomorphic to any prior graph. Soundness guarantees that every non-abstaining answer is correct. To justify the report upon abstention, suppose that \(H\cong G_i\) for some \(i\in[k]\). Then<tbc>

\(M_\mathcal{S}(H)=M_\mathcal{S}(G_i)=P(G_i)=P(H),\)

<sup>17</sup>For strict definitions and discussions of Rabin games and generalized Büchi games in the Isomorphic-Priors model, see Section A.2.

