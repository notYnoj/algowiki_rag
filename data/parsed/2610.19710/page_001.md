# Dynamic 3-Coloring of Bipartite Graphs with Optimal Locality

**Yann Bourreau**<br>
CISPA Helmholtz Center for Information Security, Saarbrücken, Germany

**Filippo Casagrande**<br>
Gran Sasso Science Institute, L’Aquila, Italy

**Tim Göttlicher**<br>
Aalto University, Espoo, Finland

**Ananth Narayanan Karunattillam**<br>
CISPA Helmholtz Center for Information Security, Saarbrücken, Germany

**Abstract**

We give a dynamic graph algorithm which maintains a 3-coloring in bipartite graphs under edge insertions such that the coloring only changes within a radius of _O_(log_n_) around an inserted edge. In the context of locality theory in distributed graph algorithms, this gives an upper bound on the locality under the dynamic-LOCAL model. Our bound on the locality is tight, as the problem admits a matching \(\Omega(logn)\) lower bound in the stronger online-LOCAL model, by a result of Chang et al. [PODC 2024]. Thus, our result closes the gap between dynamic and online locality of this problem.

**2012 ACM Subject Classification** Theory of computation \(\rightarrow\) Distributed algorithms

**Keywords and phrases** dynamic-LOCAL model, upper bound, 3-coloring, bipartite graphs

**Acknowledgements** This work was conceived during the Research Workshop on Distributed Algorithms (RW-DIST 2026). We especially thank Augusto Modanese for proposing the topic during the workshop. We also thank Sebastian Brandt, Jukka Suomela, and Jara Uitto for their helpful feedback on the final version of this work.

### 1 Introduction

Over the past decade, the theory of locality developed in distributed graph algorithms has broadened beyond the classic LOCAL model. Understanding more generally how locality changes under different computational models has become a new research perspective. In particular, new connections have been made to locality in dynamic and online graph algorithms, formalized as the dynamic-LOCAL and online-LOCAL models [2]. The study of these variants has led to a more complete landscape of locality, in which other models of computation can be classified. For example, research on lower bounds for online-LOCAL also transferred to the notoriously challenging quantum-LOCAL model [1, 9], which is used to study quantum advantage in distributed networks.

The _dynamic locality_ of a graph labeling problem is the radius in which an algorithm needs to update the labeling to maintain a correct solution to a problem as new edges are inserted. There is no restriction requiring communication to happen locally; an algorithm in this model operates as a centralized entity that has access to the entire graph.

Designing algorithms with minimal dynamic locality can be interesting for a variety of reasons: making modifications to the solution in a large radius might be costly, or it may be undesirable to leak information about the insertion to the entire graph. An output that remains stable if the local neighborhood is unchanged provides reliability in many cases.

Still, many fundamental questions studied in the theory of locality and in distributed









