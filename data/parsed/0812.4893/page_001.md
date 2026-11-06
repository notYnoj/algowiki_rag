Almost Stable Matchings in Constant Time

**Abstract**

We show that the ratio of matched individuals to blocking pairs grows linearly with the number of propose-accept rounds executed by the Gale-Shapley algorithm for the stable marriage problem. Consequently, the participants can arrive at an almost stable matching even without full information about the problem instance; for each participant, knowing only its local neighbourhood is enough. In distributed- systems parlance, this means that if each person has only a constant number of acceptable partners, an almost stable matching emerges after a constant number of synchronous communication rounds. This holds even if ties are present in the preference lists.

We apply our results to give a distributed \((2+\epsilon)\)-approximation algorithm for maximum-weight matching in bicoloured graphs and a centralised randomised constant-time approximation scheme for estimating the size of a stable matching.

## 1 Introduction

The social networking boom brings up computational challenges unforeseen in the past. In a modern large-scale network, gathering full information about the whole network in one place is practically impossible. This motivates design and analysis of _local algorithms_ [23, 27, 32] in which the output of a node depends only on the input within a constant number of edges (hops) from the node.

In this paper we study a local version of the classical Gale-Shapley algorithm [8] for the _stable marriage problem_. We show that early termination of the algorithm leads to a matching with relatively few unstable edges.

<sup>∗</sup>Helsinki Institute for Information Technology HIIT, Helsinki University of Technology and University of Helsinki. _Address_: P.O. Box 68, FI-00014 University of Helsinki, Finland. _Email addresses_: patrik.floreen@cs.helsinki.fi, petteri.kaski@cs.helsinki.fi, valentin. polishchuk@cs.helsinki.fi, jukka.suomela@cs.helsinki.fi.

Patrik Floréen, Petteri Kaski,<br> Valentin Polishchuk, and Jukka Suomela<sup>∗</sup>

December 2008

