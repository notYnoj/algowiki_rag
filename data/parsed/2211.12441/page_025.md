## Generic lower bound.

Our approach is based on Yao’s minimax principle \[Yao77\], which lower bounds worst-case complexity against randomized algorithms with bounded error by average-case complexity against deterministic algorithms with bounded distributional error. We view a deterministic algorithm with small distributional error for a problem \(\Pi\) as an exact deterministic algorithm for a slightly modified problem \(\Pi'\). The idea is to then apply the sensitivity approach to \(\Pi'\), and capitalize on the closeness of the average sensitivities of \(\Pi\) and \(\Pi'\) to obtain a lower bound in terms of the sensitivity of \(\Pi\). By using the Sensitivity Lemma as a black-box, the approach yields a lower bound on the query complexity of bounded-error algorithms that is worst-case with respect to the input and with respect to the randomness, i.e., the lower bound holds for some input and some computation path on that input. By delving into the proof of the Sensitivity Lemma, we are able to obtain a lower bound that is worst-case with respect to the input but average-case with respect to the randomness, i.e., the lower bound holds for the expected number of queries on some input.<sup>1</sup>

We first define the notions of randomized complexity and distributional complexity.

**Definition 38 (randomized query complexity,** \(\mathrm{RQ}.(\cdot)\)**, and distributional query complexity,** \(\mathrm{DistQ}.(\cdot,\cdot)\)**).** _Let_ \(\Pi\) _be a problem in the comparison-query model and_ \(\varepsilon\in[0,1]\).

_A randomized algorithm R for_ \(\Pi\) _is said to have error_ \(\varepsilon\) _if on every input_ \(\rho\)_, the algorithm outputs_ \(\Pi(\rho)\) _with probability at least_ \(1-\varepsilon\)_. The query complexity of R is the maximum, over all inputs_ \(\rho\)_, of the expected number of queries that R makes on input_ \(\rho\)_. The_ \(\varepsilon\)-error randomized query complexity _of_ \(\Pi\)_, denoted_ \(\mathrm{RQ}_\varepsilon(\Pi)\)_, is the minimum query complexity of R over all_ \(\varepsilon\)_-error randomized algorithms R for_ \(\Pi\).

_Let_ D _be a probability distribution on the inputs_ \(\rho\)_. A deterministic algorithm A for_ \(\Pi\) _has error_ \(\varepsilon\) _with respect to_ D _if the probability that_ \(A(\rho)=\Pi(\rho)\) _is at least_ \(1-\varepsilon\) _where the input_ \(\rho\) _is chosen according to_ D_. The query complexity of A with respect to_ D _is the expected number of queries that A makes on input_ \(\rho\) _when_ \(\rho\) _is chosen according to_ D_. The_ \(\varepsilon\)-error distributional query complexity _of_ \(\Pi\) _with respect to_ D_, denoted_ \(\mathrm{DistQ}_\varepsilon(\Pi,\mathcal{D})\)_, is the minimum query complexity of A with respect to_ D _over all deterministic algorithms A for_ \(\Pi\) _that have error_ \(\varepsilon\) _with respect to_ D.

The relationship between randomized complexity and distributional complexity is described by Yao’s principle.

**Lemma 39 (Yao’s minimax principle \[Yao77\]).** _Let_ \(\Pi\) _be a problem in the comparison-query model,_ \(\varepsilon\in[0,1/2]\)_, and_ D _a distribution on the inputs_ \(\rho\).

\(\mathrm{RQ}_\varepsilon(\Pi)\ge\frac{1}{2}\mathrm{DistQ}_{2\varepsilon}(\Pi,\mathcal{D}).\) (17)

We now prove lower bounds on the distributional query complexity, and thus on randomized query complexity, of comparison-query problems \(\Pi\) based on average sensitivity bounds. For these bounds, we always set D to be the uniform distribution, the distribution underlying the notion of average sensitivity.

We start by studying average-case query complexity, i.e., zero-error distributional query complexity, and its relationship to the average sensitivity. We follow a strategy similar to the one in the<tbc>

<sup>1</sup>In fact, the approach yields a lower bound that is average-case with respect to the input (chosen uniformly at random) as well as the randomness. This follows because the proof of Yao’s minimax principle allows us to replace the left-hand side of (17) by the average of the expected number of queries with respect to the distribution D, which we pick to be uniform in our application of the principle.

