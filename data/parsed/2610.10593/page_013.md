## A Arithmetic and representation lemmas

### A.1 Shared recursive parameters

**Lemma 1** (Unfolding shared parameters)**.** _Suppose a finite layered directed acyclic graph specifies the parameters of the combination-loss construction. Assume that every child edge has the prescribed lower level and shape, and that all distributions and leaf parameters satisfy their exact support, normalization, and range conditions. The graph defines an admissible parameter tree by giving each occurrence of a referenced node a separate copy of its parameters and descendants. Its derived distributions and exponent contributions can be evaluated on the graph, accumulating the masses of repeated occurrences before computing contributions linear in those masses._

