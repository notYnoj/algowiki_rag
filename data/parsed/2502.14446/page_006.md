The above high level intuition is complicated by the fact that we have to deal with multidimensional subsequences whose dimensions are hashed independently. In the following we thus detail the algorithm with reference to the pseudocode in Algorithm 1.

The algorithm proceeds in rounds from _K_ to 1: in round _i_ hash prefixes of length _i_ are considered. In each round _i_ then all repetitions \(1\le j\le L\) are considered, and each such iteration is comprised of three steps: counting the number of collisions, computing distances, and checking the stopping condition.

The first step (line 6 to 13) counts for each pair of subsequences the number of dimensions in which they share a prefix of length _i_. Note that retrieving the pairs of subsequences colliding in each dimension (line 8) is done efficiently by leveraging the fact that hash values are stored in lexicographically sorted arrays. By the end of the first step the algorithm has built a set _E_ of pairs of subsequences that collided in at least one dimension, and for each pair \((a,b)\in E\) the function _W(a,b_) reports the number of dimensions on which **T**_<sub>a</sub>_ and **T**_<sub>b</sub>_ collided.

In the second step the focus (lines from 14 to 18) is on the pairs that share prefixes in at least _d_ dimensions out of _D_, where _d_ is the target number of dimensions spanned by the motifs. The intuition is that a motif pair (**T**_<sub>a</sub>,_**T**_<sub>b</sub>_), being similar in at least _d_ dimensions, will have \(W(a,b)\ge d\). For each such pair, the algorithm computes the distance and updates the priority queue of candidates, keeping only the top-_k_ in memory.

Finally, if the priority queue contains _k_ candidates then the algorithm checks the stopping condition (Algorithm 2), which considers the pair at maximum distance in the priority queue. In particular, for this pair (**T**_<sub>a</sub>,_**T**_<sub>b</sub>_) the stopping condition focuses on \(\mathrm{dist}_d^\mathrm{max}\left(\mathbf{T}_a,\mathbf{T}_b\right)\) as defined in Equation (2). This distance is used to compute an upper bound _p_ to the probability of the two subsequences colliding in _d_ dimensions at the same time independently (line 2). This probability _p_ is then used to compute the probability that a pair of subsequences with a smaller pairwise distance was missed by the algorithm in all the previous iterations. If this probability is smaller than the user-defined \(\delta\), then the algorithm can successfully terminate. In particular, line 3 is evaluated when the full hashes are being considered, and only the first _j_ repetition have been executed. Line 4 is executed when prefixes shorter than _K_ are under consideration, and takes into account the fact that the algorithm executed _L-j_ iterations with prefixes of length _i_+1.

Note that the iterative process of lines 4 to 15 inherently exhibits _anytime_ properties, as the priority queue only allows the insertion of better solutions. The user can stop at any time the discovery to retrieve the candidate motifs with their error probabilities.

_Example 4.1._ Consider the time series shown in Figure 1, let **T**_<sub>a</sub>,_**T**_<sub>b</sub>_ be the names of the subsequences belonging to the first motif (in red) and **T**_<sub>c</sub>,_**T**_<sub>d</sub>_ to the second (in blue), TOP be the queue where we store the top motif with _k_=1, _K_=4, _L_=2 and \(\delta=0.1\). Let us assume that there exist no other collisions other than the two motifs. During the iteration at _i_=4, _j_=1 we will scan the hashes for each dimension and update our weights (lines 7-13), we find _W_(**T**_<sub>a</sub>,_**T**_<sub>b</sub>)=W_(**T**_<sub>c</sub>,_**T**_<sub>d</sub>)=_2. The first couple will be stored in the queue since it has a lower distance (lines 14-18). At this point (line 19), \(\mathrm{STOP}(\mathrm{dist}_d\left(\mathbf{T}_a,\mathbf{T}_b\right),4,1)\ge\delta\) so the condition is not satisfied. This happens again for _j_=2, when we find (**T**_<sub>c</sub>,_**T**_<sub>d</sub>_) we evaluate<tbc>

<tbc>the distance again because we have no memory of the past, and discard it for its distance is greater than the couple stored in TOP. Since the hashes of length _i_=4 were unable to satisfy the stopping condition, we move to prefix length _i_=3. This time, for both _j_=1 and _j_=2, we find (**T**_<sub>a</sub>,_**T**_<sub>b</sub>_) and (**T**_<sub>c</sub>,_**T**_<sub>d</sub>_) with weight 2, we will compare them again even though they already have been evaluated during the previous step, we will later implement a way to avoid this operation and save resources. At the end of repetition _j_=2 we find that the bound on the failure probability of the pair stored in the queue is satisfied and the algorithm stops.

## 5 ANALYSIS

In this section, we derive the probabilistic guarantees for our algorithm as well as analyze its complexity.

Lemma 5.1. _Given a pair of subsequences_ **T**_<sub>a</sub>,_**T**_<sub>b</sub> and parameter d<sub>m</sub>, consider iteration i of the outer loop of Algorithm 1. Then, we have_ \(W(a,b)\ge d\) _with probability at least_ \(P\left(\mathrm{dist}_d^\mathrm{max}\left(\mathbf{T}_a,\mathbf{T}_b\right)\right)^{i\cdot d}\) _where_ \(\mathrm{dist}_d^\mathrm{max}\left(\cdot,\cdot\right)\) _is defined as in Equation_ (2).

Proof. To have \(W(a,b)\ge d\) we need the two subsequences to collide in at least _d_ dimensions.<br>
Consider the distance \(\mathrm{dist}_d^\mathrm{max}\left(\mathbf{T}_a,\mathbf{T}_b\right)\) and recall that, by definition, all dimensions \(F=\mathrm{dim}_d\left(\mathbf{T}_a,\mathbf{T}_b\right)\) will be at a closer distance.

At iteration _i_ of the outer loop of Algorithm 1 we have that the two subsequences collide in all dimensions _F_ at the same time with probability at least \(\prod_{f\in F}P\left(\mathrm{dist}\left(\mathbf{T}_a^f,\mathbf{T}_b^f\right)\right)^i\) given that \(\tilde{f}\) is the dimension of maximum distance out of the _d_ ones in _F_, each factor of the above product is lower bounded by \(P\left(\mathbf{T}_a^\tilde{f},\mathbf{T}_b^\tilde{f}\right)\), hence the statement follows. □

### 5.1 Correctness

To prove correctness we need to show that motif pairs are considered at least once before the algorithm terminates.

The following lemma bounds the probability that a given pair of subsequences at indices _a_ and _b_ never has a weight \(W(a,b)\ge d\). In other words, the following lemma bounds the probability that a pair is never considered for inclusion in the TOP priority queue.

Lemma 5.2. _Let_ (**T**_<sub>a</sub>,_**T**_<sub>b</sub>_) _be a pair of subsequences and let_<tbc>

\(p=P\left(\mathrm{dist}_d^\mathrm{max}\left(\mathbf{T}_a,\mathbf{T}_b\right)\right)^d\)

<tbc>_Consider iteration i out of K of the outer loop and iteration j out of L of the inner loop of Algorithm 1. The probability that W(a,b)\<d in all previous iterations is upper bounded by_

\(\left\{\begin{array}{ c c }
(1-p^i)^j & \text{\textit{if}}i=K \\
(1-p^i)^j\cdot(1-p^{i+1})^{L-j} & \text{\textit{otherwise}}
\end{array}\right.\) (6)

Proof. Sketch of the proof: from Lemma 5.1 we know the probability of the pair to collide in a single repetition with prefixes of length _i_. For the given pair the failure event is to have a weight _W(a,b)\<d_. Therefore, the probability of never colliding over _j_ independent repetitions is (1-_p<sup>i</sup>)<sup>j</sup>_. In the case where _i=K_, the statement follows. When _i\<K_, we consider that the first _j_ iterations performed with prefix _i_ fail independently and that the _L-j_ iterations previously run with prefix _i_+1 failed as well. □

