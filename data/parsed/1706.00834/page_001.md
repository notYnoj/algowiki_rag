# Online Dynamic Programming

**Abstract**

We propose a general method for combinatorial online learning problems whose offline optimization problem can be solved efficiently via a dynamic programming algorithm defined by an arbitrary min-sum recurrence. Examples include online learning of Binary Search Trees, Matrix-Chain Multiplications, _k_-sets, Knapsacks, Rod Cuttings, and Weighted Interval Schulings. For each of these problems we use the underlying graph of subproblems (called a _multi-DAG_) for defining a representation of the solutions of the dynamic programming problem by encoding them as a generalized version of paths (called _multipaths_). These multipaths encode each solution as a series of successive decisions or components over which the loss is linear. We then show that the dynamic programming algorithm for each problem leads to online algorithms for learning multipaths in the underlying multi- DAG. The algorithms maintain a distribution over the multipaths in a concise form as their hypothesis. More specifically we generalize the existing Expanded Hedge (Takimoto and Warmuth, 2003) and Component Hedge (Koolen et al., 2010) algorithms for the online shortest path problem to learning multipaths. Additionally, we introduce a new and faster prediction technique for Component Hedge which in our case directly samples from a distribution over multipaths, bypassing the need to decompose the distribution over multipaths into a mixture with small support.

### 1. Introduction

We consider the problem of repeatedly solving the same dynamic programming problem in successive trials. The set of subproblems must remain unchanged but the losses/costs of the solutions change in each trial. We can handle any dynamic programming problem specified by arbitrary min-sum recurrence relations. The original well-studied problem of this type is to learn paths in a given fixed directed acyclic graph (DAG) with designated source and sink nodes. In this case, the minimum loss paths are related by rudimentary min sum recurrence and the loss of each path from the source to the sink is _additive_, that is, it is the sum of the losses of the edges along that path. For the explanation purposes, we start with this path learning problem and will introduce the online learning setup with this example problem. However this will be generalized later to handle dynamic programming problems defined by arbitrary min-sum recurrence relations.

The path learning problem is specified by a DAG _G_=(_V,E_). For every node \(v\in V\) in the given DAG, we let OPT(_v_) denote the loss of the best path from _v_ to the sink. We<tbc>

**Holakou Rahmanian**<br> _Amazon_<br> **Manfred K. Warmuth**<br> _Google Research_<br> **S.V.N. Vishwanathan**<br> _Amazon_

holakou@amazon.com

manfredwarmuth57@gmail.com

vishy@amazon.com

