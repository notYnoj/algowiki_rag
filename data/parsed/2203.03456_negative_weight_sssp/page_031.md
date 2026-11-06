## Appendix B Proof of Lemma 3.2 (FixDAGEdges)

Relabel the sets V<sub>1</sub>,V<sub>2</sub>,... so that they are in topological order in G. That is, after relabeling, if \((u,v)\in E\), with \(u\in V_i\) and \(v\in V_j\), then \(i\le j\).<br>
Define \(\mu_j=min\{w(u,v)|(u,v)\in E^{neg}(G),u\notin V_j,v\in V_j\}\); here, let \(min\{\emptyset\}=0\).<br>
// \(\mu_j\) is min negative edge weight entering V<sub>j</sub>, or 0 if no such edge exists.<br>
Define \(M_1\leftarrow\mu_1=0\).<br>
for j=2 to q do // make edges into each V<sub>2</sub>,...,V<sub>q</sub> non-negative<br>
  \(M_j\leftarrow M_{j-1}+\mu_j\) ;<br>
  \(M_j=\sum_{k\le j}\mu_k\)<br>
   Define \(\phi(v)\leftarrow M_j\) for every \(v\in V_j\)<br>
return \(\phi\)

<tbc>See Algorithm 5 for pseudocode. Let us first consider the running time. Note that computing each \(\mu_j\) requires time proportional to O(1) + \[the number of edges in E entering V<sub>j</sub>\]; since the V<sub>j</sub> are disjoint, the total time to compute all of the \(\mu_j\) is O(m+n). Similarly, it is easy to check that the for loop in Line 4 only considers each vertex once, so the total runtime of the loop is O(n).

To prove correctness, we need to show that \(w_\phi(u,v)\ge 0\) for all \((u,v)\in E\). Say that \(u\in V_i\) and \(v\in V_j\) and note that because the algorithm labels the sets in topological order, we must have i\<j. Moreover, by definition of \(\mu_j\) we have \(\mu_j\le w(u,v)\). Thus, we have

\(w_\phi(u,v)=w(u,v)+\phi(u)-\phi(v)=w(u,v)+M_i-M_j=w(u,v)-\sum_{k=i+1}^j\mu_k\ge w(u,v)-\mu_j\ge 0.\)

## Appendix C Proof of Theorem 1.1 via a Black-Box Reduction

Recall from the preliminaries that W<sub>G</sub> is defined as the absolute value of the most negative edge weight in the graph. Formally, \(W_G:=max\{2,-min_{e\in E}\{w(e)\}\}\). (We take the max with 2 so that log(W<sub>G</sub>) is well defined.)

In this section, we show how to obtain the Las Vegas algorithm of Theorem 1.1. We start by showing how to use SPmain as a black box to obtain the following Monte Carlo algorithm.

**Theorem C.1.** _There exists a randomized algorithm_ SPMonteCarlo(G<sub>in</sub>,s<sub>in</sub>_) _that takes O(m_log<sup>6</sup>(n)log(W<sub>G<sub>in</sub></sub>)) _time for an m-edge input graph G<sub>in</sub> and source s<sub>in</sub> and behaves as follows:_

• _if G<sub>in</sub> contains a negative-weight cycle, then the algorithm always returns an error message,_<tbc>

• _if G<sub>in</sub> contains_ no _negative-weight cycle, then the algorithm returns a shortest path tree from s<sub>in</sub> with high probability, and otherwise returns an error message._

_Note that the algorithm always outputs either an error message, or a (correct) shortest path tree._

_Proof._ Let T<sub>_spmain_</sub> be the expected runtime of SPmain. The algorithm simply runs Clog(n) versions of SPmain for some large constant C, where each version runs for 2T<sub>_spmain_</sub> time steps. If any of the versions returns distances, then SPmain guarantees that these distances are correct, so we simply return them. If all the versions never terminate, then the algorithm also returns an error. To bound the failure probability, note that if the graph contains a negative-weight cycle then returning an error message is what the algorithm is supposed to do; if it does not contain a negative-weight cycle,<tbc>

**Algorithm 5:** Algorithm for FixDAGEdges(G=(V,E,w),P={V<sub>1</sub>,V<sub>2</sub>,...})

