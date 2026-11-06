**Definition 4** (\[DMNS06\])**.** _A mechanism_ \(\mathcal{M}:\mathcal{X}^n\rightarrow\mathcal{R}\) _is_ \((\varepsilon,\delta)\)-differentially private _if for every pair of neighboring databases_ \(D,D'\in\mathcal{X}^n\) _and for every subset of outputs_ \(\mathcal{S}\subseteq\mathcal{R}\),

\(Pr[\mathcal{M}(D)\in\mathcal{S}]\le exp(\varepsilon)Pr[\mathcal{M}(D')\in\mathcal{S}]+\delta.\)

For the class of problems we consider, elements in both the domain and the range of the mechanism are partitioned into _n_ components, one for each player. In this setting, _joint differential privacy_ \[KPRU14\] is a more natural constraint: For all _i_, the _joint_ distribution on outputs given to players \(j\neq i\) is differentially private in the input of player _i_. Given a vector _x_=(_x_<sub>1</sub>_,...,x<sub>n</sub>_), we write _x_<sub>-_i_</sub>=(_x_<sub>1</sub>_,...,x_<sub>_i_-1</sub>_,x_<sub>_i_+1</sub>_,...,x<sub>n</sub>_) to denote the vector of length (_n_-1) which contains all coordinates of _x_ except the _i_-th coordinate.

**Definition 5** (\[KPRU14\])**.** _A mechanism_ \(\mathcal{M}:\mathcal{X}^n\rightarrow\mathcal{R}^n\) _is_ \((\varepsilon,\delta)\)-jointly differentially private _if for every i, for every pair of i-neighbors_ \(D,D'\in\mathcal{X}^n\)_, and for every subset of outputs_ \(\mathcal{S}\subseteq\mathcal{R}^{n-1}\),

\(Pr[\mathcal{M}(D)_{-i}\in\mathcal{S}]\le exp(\varepsilon)Pr[\mathcal{M}(D')_{-i}\in\mathcal{S}]+\delta.\)

_If_ \(\delta=0\)_, we say that_ M _is_ \(\varepsilon\)_-differentially private. The case of_ \(\delta>0\) _is sometimes referred to as_ approximate _differential privacy._

Note that this is still a very strong privacy guarantee; the mechanism preserves the privacy of any player _i_ against arbitrary coalitions of other players. It only weakens the constraint of differential privacy by allowing player _i_’s output to depend arbitrarily on her _own_ input.

An important class of jointly differentially private algorithms - particularly amenable to our purposes - are those that work in the so-called _billboard model_. Algorithms in the billboard model compute a differentially private signal as a function of the input database; then each player _i_’s portion of the output is computed as a function only of this private signal and the private data of player _i_. The following lemma shows that algorithms operating in the billboard model satisfy joint differential privacy.

**Lemma 10** (\[HHR<sup>+</sup>14\])**.** _Suppose_ \(\mathcal{M}:\mathcal{X}^n\rightarrow\mathcal{R}\) _is_ \((\varepsilon,\delta)\)_-differentially private. Consider any set of functions_ \(f_i:\mathcal{X}\times\mathcal{R}\rightarrow\mathcal{R}'\)_. Then the mechanism_ \(\mathcal{M}'\) _that outputs to each player i: f<sub>i</sub>(D<sub>i</sub>,_M(_D_)) _is_ \((\varepsilon,\delta)\)_-jointly differentially private._

Note the similarity between algorithms operating in the billboard model and coordination complexity protocols: a signal is computed by a central party, and then the action of each agent is a function only of this signal and of their own portion of the problem instance. Thus, the following lemma is immediate:

**Lemma 11.** _A coordination protocol_ \((\sigma,\pi)\) _satisfies_ \((\varepsilon,\delta)\)_-joint differential privacy if the coordinator’s encoding function_ \(\sigma\) _satisfies_ \((\varepsilon,\delta)\)_-differential privacy._

_Proof._ Follows from Lemma 10.

## 5.2 A Generic Private Coordination Protocol

Next, we give a general way to convert any coordination protocol to a jointly differentially private algorithm - and the lower the coordination complexity of the protocol, the better the utility guarantee of the private algorithm. The tool we use is the _exponential mechanism_ of \[MT07\], one of the most basic tools in differential privacy. To formally define this mechanism, we consider some arbitrary range R and some quality score function \(q:\mathcal{X}^n\times\mathcal{R}\rightarrow\mathbb{R}\), which maps database-output pairs to quality scores.

