# Multidimensional Stable Roommates with Master List<sup>‡</sup>

**Abstract**

Since the early days of research in algorithms and complexity, the computation of stable matchings is a core topic. While in the classic setting the goal is to match up two agents (either from different "gender" (this is Stable Marriage) or "unrestricted" (this is Stable Roommates)), Knuth [1976] triggered the study of three- or multidimensional cases. Here, we focus on the study of Multidimensional Stable Roommates, known to be NP-complete since the early 1990’s. Many NP-completeness results, however, rely on general input instances that do not occur in at least some of the specific application scenarios. With the quest for identifying islands of tractability for Multidimensional Stable Roommates, we study the case of master lists. Here, as natural in applications where agents express their preferences based on "objective" scores, one roughly speaking assumes that all agent preferences are "derived from" a central master list, implying that the individual agent preferences shall be similar. Master lists have been frequently studied in the two-dimensional (classic) stable matching case, but seemingly almost never for the multidimensional case. This work, also relying on methods from parameterized algorithm design and complexity analysis, performs a first systematic study of Multidimensional Stable Roommates under the assumption of master lists.

**Keywords.** Stable matching, partially ordered sets, NP-hardness, parameterized complexity, distance-from-triviality parameterization

### 1 Introduction

Computing stable matchings is a core topic in the intersection of algorithm design, algorithmic game theory, and computational social choice. It has numerous applications such as higher education admission in several countries [3, 6], kidney exchange [44], assignment of dormitories [40], P2P-networks [18], wireless three-sided networks [9], and spatial crowdsourcing [33]. The research started in the 1960’s with the seminal work of Gale and Shapley [19], introducing the Stable Marriage problem: given two different types of agents, called "men" and "women", each agent of one gender has preferences (i.e., strict orders aka rankings) over the agents of the

<sup>∗</sup>Main work done while all authors were affiliated with TU Berlin. <sup>†</sup>An extended abstract of this work appears in the _Proceedings of the 16th International Conference on Web and Internet Economics_ [7]. This full version now contains full proofs of all results.

Robert Bredereck<sup>1</sup>, Klaus Heeger<sup>2</sup>, Dušan Knop<sup>3</sup>, and Rolf Niedermeier<sup>2</sup>

<sup>1</sup> Humboldt-Universität zu Berlin, Institut für Informatik, Algorithm Engineering, Germany `robert.bredereck@hu-berlin.de`

<sup>2</sup> Technische Universität Berlin, Fakultät IV, Algorithmics and Computational Complexity, Germany `{heeger,rolf.niedermeier}@tu-berlin.de`

<sup>3</sup> Czech Technical University in Prague, Prague, Czech Republic `dusan.knop@fit.cvut.cz`

