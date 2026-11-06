<tbc>deviation opportunity. Thus, in such settings, there may be less of a practical need to minimise the instability of these agents. Specifically, in situations where full stability is not achievable, for example due to the presence of additional constraints on the size of the matching, or due to restrictive preference cycles, it may be feasible to simply enforce that no _deviator_ (i.e., the agents that are likely to deviate when given a beneficial opportunity) has a beneficial opportunity to deviate, while placing no such requirement on the _conformists_ (i.e., the agents that are unlikely to initiate deviations). In this paper, we focus on the following natural question and its extensions across a variety of different settings.

**Question:** Does there exist a _desirable_ matching in which no _deviator_ is blocking?

### 1.1 Our Contributions

In this paper, we outline the computational landscape surrounding the computation of (maximum- cardinality) matchings that minimise the instability of a given subset of _deviator agents_ in terms of their numbers and sets of blocking pairs. Unfortunately, we derive strong intractability results: even deciding whether there exists a matching (maximum-cardinality matching) in which no deviator agent is in any blocking pair is NP-complete for sri (respectively smi). On the positive side, we present efficient parametrised algorithms (with respect to the number of deviators and the preference list length) and polynomial-time algorithms for instances with short preference lists. We also extend our results to the minimisation of blocking deviator agents and resolve some further open questions from the literature.

### 1.2 Structure of the Paper

In Section 2, we give formal definitions and discuss relevant related work. Deviator-stability in terms of blocking pairs is introduced and investigated in Section 3, followed by parametrised algorithms in Section 4. In Section 5, we extend the results to an alternative blocking agent perspective. Section 6 contains flexible, efficient algorithms for instances with very short lists that can minimise blocking pairs involving deviator agents, or the number of blocking deviators. In Section 7 we resolve some further open cases from the literature. Finally, we summarise new and known complexity results in  1 and pose open questions in Section 8.

## 2 Background

### 2.1 Formal Definitions

In Section 1, we introduced the smi and sri problems informally. Now, we will provide formal definitions of these problem instances that apply throughout this paper.

**Definition 2.1** (sri Instance)**.** _A_ Stable Roommates with Incomplete Lists (sri) instance, _denoted by_ \(I=(A,\succ)\)_, consists of a set of_ \(n\in\mathbb{N}\) _agents A_={_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>n</sub>_} _and a tuple_ \(\succ\) _of n_ preference rankings \(\succ_i\) _(where i is the index of corresponding agent a<sub>i</sub>) over a subset of A_\\{_a<sub>i</sub>}. We say that a<sub>i</sub>_ prefers _a<sub>j</sub> to a<sub>k</sub> if_ \(a_j\succ_ia_k\)_. If_ \(a_j\succ_ia_k\) _or j=k, we will write_ \(a_j\unknown_ia_k\)_. Two agents a<sub>i</sub> and a<sub>j</sub> are referred to as_ acceptable _if they appear in each other’s preference rankings. Throughout, we assume that acceptability is symmetric._

Note that any sri instance \(I=(A,\succ)\) can be modelled as a graph _G_=(_A,E_), where every agent is a vertex and every acceptable pair of agents induces an edge in _E_. From hereon, _G_ is referred to as the _acceptability graph_ of _I_. If _G_ is isomorphic to a complete graph on |_A_| vertices, then we say that _I_ has _complete preferences_. Otherwise, we say that _I_ has _incomplete preferences_. The restriction of sri instances to instances that have bipartite acceptability graphs is the class of Stable Marriage with Incomplete Lists (smi) instances. Given a bipartition of _A_ into mutually exclusive but collectively exhaustive subsets _A_<sub>1</sub> and _A_<sub>2</sub>, we say that an smi<tbc>

