# Round-Competitive Algorithms for Uncertainty Problems with Parallel Queries

**Abstract**

The area of computing with uncertainty considers problems where some information about the input elements is uncertain, but can be obtained using queries. For example, instead of the weight of an element, we may be given an interval that is guaranteed to contain the weight, and a query can be performed to reveal the weight. While previous work has considered models where queries are asked either sequentially (adaptive model) or all at once (non-adaptive model), and the goal is to minimize the number of queries that are needed to solve the given problem, we propose and study a new model where _k_ queries can be made in parallel in each round, and the goal is to minimize the number of query rounds. We use competitive analysis and present upper and lower bounds on the number of query rounds required by any algorithm in comparison with the optimal number of query rounds. Given a set of uncertain elements and a family of _m_ subsets of that set, we present an algorithm for determining the value of the minimum of each of the subsets that requires at most \((2+\varepsilon)\cdot\mathrm{opt}_k+\mathrm{O}\left(\frac{1}{\varepsilon}\cdot\mathrm{lgm}\right)\) rounds for every \(0<\varepsilon<1\), where opt_<sub>k</sub>_ is the optimal number of rounds, as well as nearly matching lower bounds. For the problem of determining the _i_-th smallest value and identifying all elements with that value in a set of uncertain elements, we give a 2-round-competitive algorithm. We also show that the problem of sorting a family of sets of uncertain elements admits a 2-round-competitive algorithm and this is the best possible.

**2012 ACM Subject Classification** Theory of Computation \(\rightarrow\) Design and analysis of algorithms; Mathematics of computing \(\rightarrow\) Discrete mathematics; Theory of computation \(\rightarrow\) Theory and algorithms for application domains

**Keywords and phrases** online algorithms, competitive analysis, explorable uncertainty, parallel algorithms, minimum problem, selection problem

**Related Version** An extended abstract is to appear in the proceedings of the 38th International Symposium on Theoretical Aspects of Computer Science (STACS 2021).

**Funding** This research was supported by EPSRC grant EP/S033483/1.

**Acknowledgements** We would like to thank Markus Jablonka for helpful discussions.

### 1 Introduction

Motivated by real-world applications where only rough information about the input data is initially available but precise information can be obtained at a cost, researchers have considered a range of **uncertainty problems with queries** [7, 13, 14, 15, 16, 19, 26]. This research area has also been referred to as **queryable uncertainty** [12] or **explorable uncertainty** [17]. For example, in the input to a sorting problem, we may be given for each input element, instead of its precise value, only an interval containing that point. Querying

<sup>1</sup> Corresponding author.

Thomas Erlebach School of Informatics, University of Leicester, UK

Michael Hoffmann School of Informatics, University of Leicester, UK

Murilo Santos de Lima<sup>1</sup> School of Informatics, University of Leicester, UK

