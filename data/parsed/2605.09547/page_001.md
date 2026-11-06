# Computing Flows in Subquadratic Space

Jan van den Brand<sup>∗</sup>

Zhao Song<sup>†</sup>

Albert Weng<sup>‡</sup>

**Abstract**

Space complexity is a critical factor in various computational models, including streaming, parallel/distributed computing, and communication complexity. We study the space complexity of the minimum-cost flow problem, a generalization of the st-max flow problem, focusing on computing flows in subquadratic space. In the general case with arbitrary capacities, minimum cost and _st_-maximum flows can use up to \(\Omega(n^2)\) edges, so computing the flow on each edge (rather than just the size/cost) seems impossible in subquadratic space. Indeed, there are lower bounds proving quadratic space is needed to store the flow on every edge, which has been used to prove lower bounds on streaming algorithms. However, we show that these lower bounds can be circumvented, opening up improvements for streaming and communication complexity.

For a directed graph with integer capacities and costs bounded by _W_, we provide a \(\widetilde{O}(n^{1.5}log(W/\epsilon))\)- space \(\widetilde{O}(\sqrt{n}log(W/\epsilon))\)-pass streaming algorithm, which during the last pass returns the flow on each edge up to an additive error of \(\epsilon\). Crucially, the algorithm does not return the flow at the end of the last pass but returns the flow on an edge, as the edge is read in the stream. This allows us to circumvent existing \(\Omega(n^2)\) space lower bounds. In the 2-party communication model, our algorithm implies \(\widetilde{O}(n^{1.5}log^2W)\) bits of communication.

<sup>∗</sup>Georgia Institute of Technology, `vdbrand@gatech.edu` <sup>†</sup>`magic.linuxkde@gmail.com` <sup>‡</sup>Georgia Institute of Technology, `albweng@gatech.edu`

