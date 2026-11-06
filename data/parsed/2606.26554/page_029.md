the path \(\pi'=v_0,\dots,v_i,v_j,\dots,v_\ell\) of hop length at most \(2\beta/3+1\). Furthermore, \(\text{wt}(v_i,v_j)=\widehat{\text{d}}(v_i,v_j)=\text{dist}(v_i,v_j)\) by correctness of the MSSP algorithm.

To analyze the time, sampling requires _O(n_) time, MSSP requires \(Bn^{o(1)}\mathsf{T}_\text{MUL}(n/\beta,n,n)\) time by Theorem 1.3, and constructing _F_ requires _O_(|_S_|<sup>2</sup>) time. We thus conclude by bounding |_S_|. By a Chernoff bound, we have with high probability \(|S|=O\left(\frac{nlogn}{\beta}\right)\) so that \(|S|^2=\widetilde{O}\left(n^2/\beta^2\right)\), as desired.

### 5.3.2 Additive Emulator Construction

We give a simple, efficient algorithm for constructing a +4-emulator on undirected graphs.

**Theorem 5.24.** _There is a randomized_ \(O(Bn^{\omega(1,2/3,1)+o(1)})=O\left(Bn^{2.1321}\right)\) _time algorithm to construct_ +4_B-emulators of size O(n_<sup>4/3</sup>log_n_) _on undirected graphs with integer weights at most B._

_Proof._ Elkin, Gitlitz, and Neiman \[EGN23, Section 7\] present the following algorithm for obtaining a +4- emulator.

Since we follow the algorithm exactly, we omit the proof of correctness. To analyze the running time, note that the first two steps require _O(n_<sup>2</sup>log_n_) time. By Theorem 1.3, MSSP requires \(Bn^{\omega(1,2/3,1)+o(1)}\), which bounds the running time of our algorithm.

## 6 Reachability and Shortest Paths on Directed Graphs

We give a simple recursive scheme that obtains optimal running time for directed reachability.

**Definition 6.1** (Multiple Source Reachability)**.** _Given directed graph G_=(_V,E_) _and a set of sources_ \(S_\text{in}\subseteq V\)_, compute_ reach(_s,v_) _for all_ \(s\in S_\text{in}\) _and_ \(v\in V\) .

**Theorem 1.5.** _Multiple Source Reachability is equivalent to_ BMM(|_S_in|_,n,n), up to_ polylog(_n_) _factors. In particular, there is a deterministic algorithm computing Multiple-Source Reachability in_ \(\widetilde{O}\left(\mathsf{T}_\text{BMM}\left(|S_\text{in}|,n,n\right)\right)\) _time._

_Proof._ Without loss of generality, we may assume that the graph _G_ is a directed acyclic graph (DAG) and _G_ is topologically sorted. In particular, we first decompose the graph into strongly connected components (SCC) and apply a topological sort to the remaining DAG. After this transformation, let _S_in denote all the strongly connected components of the input graph that intersect the input _S_in. Note that both the SCC decomposition (which preserves reachability) and topological sort can be computed in linear time.

Given the assumption, we let \(a\le b\) denote comparison in the topological order. Let \([a,b]\subseteq V\) denote all vertices between _a_ and _b_ (inclusive) in the topological order. Furthermore, given \(s,v\in V\) , let pred(_s,v_) denote the minimum vertex _a_ (in topological order) such that reach(_s,a_)=1 and \((a,v)\in E\). That is, there is a path from _s_ to _v_ such that _a_ is the vertex immediately preceding _v_.

With our assumptions, consider the following recursive procedure.

Input: Graph G.
1. Initialize H \(\leftarrow\emptyset\) and \(S\subseteq V\) a random set chosen by sampling each vertex independently with probability n-1/3.
2. Add the O(n 1/3 log n) lightest edges incident to every vertex to H.
3. Compute MSSP from S and add S S to H with weights wt(s1,s2)=dist(s1,s2).
Since we follow the algorithm exactly, we omit the proof of correctness. To analyze the running time, note that the first two steps require O(n2 log n) time. By Theorem 1.3, MSSP requires Bn (1,2/3,1)+o(1), which bounds the running time of our algorithm.
We give a simple recursive scheme that obtains optimal running time for directed reachability.
Definition 6.1 (Multiple Source Reachability). Given directed graph G=(V,E) and a set of sources Sin V, compute reach(s,v) for all s in Sin and v V.
Theorem 1.5.
Multiple Source Reachability is equivalent to BMM(|Sin|,n,n), up to polylog(n) factors. In particular, there is a deterministic algorithm computing Multiple-Source Reachability in O (T BMM (|Sin|,n,n)) time.
Proof. Without loss of generality, we may assume that the graph G is a directed acyclic graph (DAG) and G is topologically sorted. In particular, we first decompose the graph into strongly connected components (SCC) and apply a topological sort to the remaining DAG. After this transformation, let Sin denote all the strongly connected components of the input graph that intersect the input _S_in. Note that both the SCC decomposition (which preserves reachability) and topological sort can be computed in linear time.
Given the assumption, we let a b denote comparison in the topological order. Let [a,b] V denote all vertices between a and b (inclusive) in the topological order. Furthermore, given \(s,v\in V\) , let pred(s,v) denote the minimum vertex a (in topological order) such that reach(s,a)=1 and \((a,v)\in E\). That is, there is a path from _s_ to _v_ such that _a_ is the vertex immediately preceding _v_.
With our assumptions, consider the following recursive procedure.
complete(G,Sin,L,R):
Input: Topologically sorted DAG G, sources Sin, and interval endpoints L R.
(Assume reach(s,v) is computed for S in and v where either v L or pred(s,v) L.)

