# Fault-Tolerant Bounded Flow Preservers

**Shivam Bansal** \(\unknown\)

Department of Computer Science and Engineering, IIT Delhi, India

**Keerti Choudhary** \(\unknown\)

Department of Computer Science and Engineering, IIT Delhi, India

**Harkirat Dhanoa** \(\unknown\)

Department of Computer Science and Engineering, IIT Delhi, India

**Harsh Wardhan** \(\unknown\)

Department of Electrical Engineering, IIT Delhi, India

**Abstract**

Given a directed graph G=(_V,E_) with _n_ vertices, _m_ edges and a designated source vertex \(s\in V\) , we consider the question of finding a sparse subgraph H of G that preserves the flow from _s_ up to a given threshold \(\lambda\) even after failure of _k_ edges. We refer to such subgraphs as \((\lambda,k)\)-fault-tolerant bounded-flow-preserver \(((\lambda,k)\)-FT-BFP). Formally, for any \(F\subseteq E\) of at most _k_ edges and any \(v\in V\) , the (_s,v_)-max-flow in H\\_F_ is equal to (_s,v_)-max-flow in G\\_F_, if the latter is bounded by \(\lambda\), and at least \(\lambda\) otherwise. Our contributions are summarized as follows:

1. We provide a polynomial time algorithm that given any graph G constructs a \((\lambda,k)\)-FT-BFP of G with at most \(\lambda 2^kn\) edges.

2. We also prove a matching lower bound of \(\Omega(\lambda 2^kn)\) on the size of \((\lambda,k)\)-FT-BFP. In particular, we show that for every \(\lambda,k,n\ge 1\), there exists an _n_-vertex directed graph whose optimal \((\lambda,k)\)-FT-BFP contains \(\Omega(min\{2^k\lambda n,n^2\})\) edges.

3. Furthermore, we show that the problem of computing approximate \((\lambda,k)\)-FT-BFP is NP-hard for any approximation ratio that is better than \(O(log(\lambda^{-1}n))\).

**2012 ACM Subject Classification** Theory of computation \(\rightarrow\) Data structures design and analysis; Mathematics of computing \(\rightarrow\) Graph algorithms

**Keywords and phrases** Fault-tolerant Data-structures, Max-flow, Bounded Flow Preservers

### 1 Introduction

We address the problem of computing single-source fault-tolerant bounded-flow-preservers for directed graphs. The objective is to construct a sparse subgraph that preserves the flow value up to a parameter \(\lambda\) from a given fixed source _s_, even after failure of up to _k_ edges.

The following definition provides a precise characterization of this subgraph.

\(\blacktriangleright\) **Definition 1.** _Let_ G=(_V,E_) _be a directed graph and_ \(s\in V\) _be a designated source vertex. A_ \((\lambda,k)\)_-Fault-Tolerant Bounded-Flow-Preserver_ \(((\lambda,k)\)_-FT-BFP_) _for_ G _is a subgraph_ \(\mathcal{H}=(V,E_\mathcal{H}\subseteq E)\) _of_ G _satisfying that for every_ \(F\subseteq E\) _of at most k edges, and every_ \(t\in V\) ,

\(max_{-flow}(s,t,\mathcal{H}-F)=\left\{\begin{array}{ c c }
max_{-flow}(s,t,\mathcal{G}-F) & \text{\textit{if}}max_{-flow}(s,t,\mathcal{G}-F)\le\lambda, \\
\text{\textit{At least}}\lambda, & \text{\textit{otherwise.}}
\end{array}\right.\)

For the special case of \(\lambda=1\), the problem is referred to as _k_-Fault-Tolerant Reachability Subgraph (_k_-FTRS) in the literature. Here the goal is to preserve reachability from _s_ after _k_ edge failures. Baswana et al. [4] showed that there exists a _k_-FTRS with at most 2_<sup>k</sup>n_ edges. Lokshtanov et al. [17] presented an algorithm for computing a \((\lambda,k)\)-FT-BFP for directed graphs. Their algorithm runs in time \(O(4^{k+\lambda}(k+\lambda)^2(m+n)\cdot m)\), and each vertex of the

