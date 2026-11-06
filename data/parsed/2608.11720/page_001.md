# DISTRIBUTED QUANTUM ALGORITHMS CANNOT COLOR CYCLES WITH PROBABILITY 1

Abstract. We prove that any _distributed quantum algorithm_ that finds a 3-coloring with probability 1 in a cycle of anonymous identical computers has to be global, that is, it needs \(\Omega(n)\) communication rounds. It follows that quantum computation and communication does not help with this problem.

All prior lower bounds on quantum advantage in distributed graph algorithms use arguments related to physical causality. However, it is known that such arguments cannot rule out fast quantum advantage for 3-coloring cycles. In particular, any causality-based argument would rule out the existence of _finitely dependent coloring_, but Holroyd and Liggett (2016) showed that such colorings do exist.

Hence to tackle this problem, we need a "genuinely quantum" lower-bound technique that can distinguish between (1) distributions that do not violate physical causality vs. (2) distributions that can be realized with a quantum strategy. We present the first such lower-bound technique in this context. First, we show that 1-round quantum algorithms cannot break symmetry with probability 1. Second, we present a _wishful teleportation_ strategy that can be used to turn _T_-round quantum 3-coloring algorithms into 1-round quantum algorithms breaking symmetry, while preserving success probability 1. Put together, the lower bound follows.

### 1. Introduction

In this work, we present the first "genuinely quantum" lower bound that puts limits on quantum advantage in distributed symmetry breaking and coloring of cycle. In particular, we show that no distributed quantum algorithm can color cycles with probability 1 in a sublinear number of rounds. Previous lower bounds were established only for _finitely dependent distributions_, a computational model that contains distributed quantum algorithms while remaining easier to analyse. However, finitely dependent colorings of cycles are known to exist [HL16]. Hence, our work is the first inherently quantum lower bound that separates distributed quantum algorithms from finitely dependent distributions.

#### 1.1. Quantum Advantage for Distributed Symmetry Breaking.

One of the biggest open questions related to distributed quantum advantage is whether quantum computation and communication help with distributed symmetry-breaking problems [GKM09; ACdLLMMPRRS25; Suo24; dAm25]. The canonical symmetry-breaking primitive is 3-coloring directed paths and cycles; if this problem can be solved efficiently, all other symmetry-breaking tasks can also be solved efficiently.

The main formalism where this question has been studied is the LOCAL model of distributed computing [Lin92; Pel00]: we have a cycle formed by _n_ computers; they are initially labeled with poly(_n_)-sized unique identifiers; computation proceeds in synchronous rounds; in each round, each node can send a message to each neighbor and update its state based on the messages it receives; and eventually, after some _T_ rounds, each node must stop and announce its own color.

<sup>1</sup> Institute for Quantum Science and Technology, University of Calgary, Canada <sup>2</sup> Aalto University, Finland <sup>3</sup> Inria Paris-Saclay, CPHT, CNRS, Ecole Polytechnique, Institut Polytechnique de Paris, France

XAVIER COITEUX-ROY<sup>1</sup>, MAXIME FLIN<sup>2</sup>, CARLOS DE GOIS<sup>3</sup>, MARC-OLIVIER RENOU<sup>3</sup>, JUKKA SUOMELA<sup>2</sup>, AND ISAADORA VEEREN<sup>3</sup>

arXiv:2608.11720v1 [cs.DS] 12 Aug 2026

