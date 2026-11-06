<tbc>_w_. In each of these triangles, the edge (_u,v_) appears first, followed by the edge (_v,w_) and finally the edge (_w,u_). Further, all three edges occur within an hour of each other. What this means is that there exist temporal edges _e_<sub>1</sub>=(_u,v,t_<sub>1</sub>), _e_<sub>2</sub>=(_v,w,t_<sub>2</sub>) and _e_<sub>3</sub>=(_v,w,t_<sub>3</sub>) such that the triangle (_e_<sub>1</sub>_,e_<sub>2</sub>_,e_<sub>3</sub>) is an instance of the temporal motif _H_ specified in the predicate \(\phi\). In this case, predicate is given by the gambling triangle in Figure-1c. Therefore, for a pair (_u,v_) to be solution to this query, there must exist a temporal edge _e_=(_u,v,t_) that forms an instance of the gambling triangle with at least half of _v_’s neighbors. In this case, we can say that the temporal edge _e_=(_u,v,t_) certifies that the pair (_u,v_) is indeed a solution to the given \(\exists u\exists v\forall_{1/2}w\in N(v)\) query. _In this work, we develop algorithms, which allow us to enumerate all certificates to an_ \(\exists\exists\forall\) _query i.e. instead of just one, we find all temporal edges on_ (_u,v_) _that satisfy the input predicate_. We will often refer to a certificate _e_=(_u,v,t_) as a solution to the \(\exists\exists\forall_T\) query.

As another example, consider the following query: \(\exists u\forall_{1/2}v\in N(u)\forall_{1/3}w\in N(v)\), edge (_u,v_) appears first, then edge (_u,w_), and finally edge (_v,w_), and all occur in 40 minutes. (The predicate \(\phi(u,v,w)\) is the entire sentence after the quantifiers.) This means that we are looking for a vertex _u_ such that for at least half of its neighbors _v_, at least one third of the neighbors _w_ of _v_ form the desired triangle specified. In particular, for at least half of _u_’s neighbors _v_, there exists a temporal edge _e_=(_u,v,t_) such that _e_ forms the desired temporal triangle with a third of _v_’s neighbors _w_. So, for at least a one-third neighbors _w_ of _v_, _G_ contains temporal edges _e_<sub>2</sub>=(_u,w,t_<sub>2</sub>) and _e_<sub>3</sub>=(_v,w,t_<sub>3</sub>) such that \(t\le t_2\le t_3\le t+\delta\), where \(\delta\) is 40 mins.

Observe that thresholded FOL queries provide rich semantics for pattern mining in graphs. While we typically consider the universe for with the last quantifier as the neighborhood of the previous<tbc>

<tbc>vertex, similar techniques can be developed for cases in which the universe happens to be, say the intersection of the neighborhoods of the previous two vertices.

It is straightforward to define the notion of a solution to the thresholded FOL query. Figure-2 gives an example.

Definition 1.2. _The_ solution _to the FOL query Q_<sub>1</sub>_u Q_<sub>2</sub>_v Q_<sub>3</sub>_w_ \(\phi(u,v,w)\) _is the set of vertices whose assignment to the_ prefix _of existential quantis makes the statement true._

_Specifically, for_ \(\exists u\exists v\exists w\) _queries, a solution is a triple of vertices. For_ \(\exists u\exists v\forall w\)_, a solution is a pair_ (_u,v). For_ \(\exists u\forall v\forall w\) _and_ \(\exists u\forall v\exists w\) _queries, a solution is a single vertex._

We do not consider queries that begin with a universal quantifier, since there is no notion of a solution. (Using negation and de Morgan’s laws, one can convert it to one of the queries in definition-1.2.) Thus, we have four kinds of thresholded FOL queries, denoted as \(\exists\exists\exists\), \(\exists\exists\forall\), \(\exists\forall\exists\), and \(\exists\forall\forall\). The meaning of these should be clear from the above definition.

We now come to the main computational problem. Given a thresholded FOL query, we wish to count and enumerate the number of solutions of these queries. As explained earlier, in the case of \(\exists\exists\exists\) queries, this is simply the problem of temporal triangle counting. In this work, we focus on _Triadic Queries_ i.e. FOL queries, in which predicate is a temporal triangle. The main technical question we resolve is the following.

_Is there an efficient algorithm to count/enumerate solutions of a thresholded FOL triadic query, whose theoretical running time is comparable to the best temporal triangle counters?_

In this paper, we present our techniques by taking the example of the predicate, which is given by the temporal triangle of Figure-2a. However, our techniques can be generalized to deal with alternate temporal triangles as well.

## 1.3 Contributions

Our main result is a theoretical algorithm, First Order Logic Triadic Yielder (FOLTY), that can exactly compute and enumerate the number of solutions to any thresholded FOL triadic query. As we explain below, the running time matches the best known temporal triangle counter [39], based on the best possible complexity known for triangle counting [8]. We give an efficient, practical implementation of FOLTY that can process temporal graphs with tens of millions of edges. We list out the important contributions of our work.

**Defining thresholded FOL queries.** To the best of our knowledge, this is the first work that sets up the notion of thresholded FOL queries for temporal networks. While the notion of FOL queries for databases has been studied before [15, 22], there is no work in the data mining literature that sets up the problems given in 1.1 and 1.2. We believe that these definitions set up a new research direction in motif analysis. This work also initiates the use of orientation-based methods for analyzing first-order logic (FOL) queries on attributed networks, a question which was posed in [45].

**An algorithm with provable runtime guarantees.** FOLTY has the best possible theoretical running time up to log factors, assuming the forty year old bound of Chiba-Nishizeki for sparse triangle counting [8]. We prove that FOLTY also has a running time<tbc>

W
X
W
2
3
20
5
8
25
55
u
V
u
V
1
10
10
(a) Predicate for FOL for (b) Example of a solution for (b) query
X
W
20
5
8
25
55
u
V
10
(c) Example of a non- solution for (b) query

**Figure 2: Consider the query** \(\exists u\exists v\forall w\in N(u)\)**, the edges** (_u,v_)**,** (_u,w_)**, and** (_v,w_) **occur within 20 timesteps. In the left figure, the edge** (_u,v_) **is a solution. In the right figure, it is not a solution. Triangle** (_u,v,x_) **violations the timestamp constraint, while triangle** (_u,v,w_) **violates the directions.**

