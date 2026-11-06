## 5.2.2 Arbitrary inputs

We now consider using Batcher’s odd even mergesort for sorting a random permutation of the set {0_,...,n_-1}. This case is actually sufficient to upper bound the minimal heat dissipation for sorting arbitrary list of _n_ distinct items from an ordered set _D_.

**Lemma 5.5.** _Let_ C _be a sorting network on n inputs. Let_ D_<sub>n</sub> be the uniform distribution over permutations of_ {0_,...,n_-1} _and_ D_<sub>D</sub> be the distribution obtained by sampling n elements of D uniformly at random without replacement. Then the minimum expected heat released by any gate g in_ C _on input distribution_ D_<sub>n</sub> is at most the minimum expected heat released by g in_ C _on input distribution_ D_<sub>D</sub>._

_Proof._ Let _X<sub>g</sub>_ be a random variable over the inputs to gate _g_ induced by C receiving input _X_ sampled from D_<sub>D</sub>_ and _V(X_) be the unordered set of values in _X_. Using Lemma 3.1, the optimal heat function for _g_ would give a minimum expected heat release of

\(\sum_{x_1,x_2}\mathrm{Pr}[X_g=(x_1,x_2)]Q(X_g)=\sum_{x_1,x_2}\mathrm{Pr}[X_g=(x_1,x_2)]\mathrm{log}\left(\frac{\mathrm{Pr}[\mathrm{Comp}(X_g)=\mathrm{Comp}(x_1,x_2)]}{\mathrm{Pr}[X_g=(x_1,x_2)]}\right)\)<br>
\(=\mathcal{S}(X_g|\mathrm{Comp}(X_g))\)<br>
\(\ge\mathcal{S}(X_g|\mathrm{Comp}(X_g),V(X)).\)

After conditioning on _V(X_), we can re-label the elements in _D_ so that the elements in _V(X_) get mapped to 0_,...,n_-1 in their relative rank order and all remaining elements get mapped to distinct values that are all at least _n_. After this relabeling, _X<sub>g</sub>_ conditioned on _V(X_) is just a random variable for the induced marginal input distribution when C has input distribution D. Thus the expected minimum heat dissipation on D_<sub>D</sub>_ is at least that on D_<sub>n</sub>_.

Thus we will be assuming input distribution D_<sub>n</sub>_ in the rest of this section. By Lemma 3.1 the optimal heat function for our comparator gates on marginal induced input distribution D when \(x_1\neq x_2\) is given by:

\(Q(x_1,x_2)=\mathrm{log}\left(\mathrm{Pr}_{\mathrm{Comp}(\mathcal{D})}[\mathrm{Comp}(x_1,x_2)]/\mathrm{Pr}_\mathcal{D}[(x_1,x_2)]\right)\)

Layer 1
Layer 2
Layer 3
X1
y1
X2
y2
X3
y3
X4
y4

Figure 3: The _n_=4 base case of Batcher’s odd-even mergesort.

