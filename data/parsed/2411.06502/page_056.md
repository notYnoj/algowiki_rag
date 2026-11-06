**Lemma 2.1.** _Suppose there exists an algorithm for SED on two forests_ \(\mathbf{H},\mathbf{H}'\) _running in time_ \(\mathsf{T}_{SED}(m,m')=\mathcal{O}(f(m)g(m'))\)_, where_ \(m=|\mathbf{H}|,m'=|\mathbf{H}'|\) _and_ \(f(m)=\Omega(m)\), \(g(m')=\Omega(m')\) _are some functions. Then, there is an algorithm for TED on two forests_ \(\mathbf{F},\mathbf{F}'\) _running in time_ \(\mathcal{O}(f(n)g(n')log^2max(n',n))\)_, where_ \(n=|\mathbf{F}|,n'=|\mathbf{F}'|\).

We will first reduce the following variant of SED to SED:

Utilizing the above reduction, we further reduce All-Subtrees-TED to SED, which we define as a more general problem than TED.

Our reduction is based on a tree decomposition similar to the well-known _heavy path decomposition_ introduced by Harel and Tarjan [HT84]. For our purposes, we can formulate this decomposition as follows.

**Proposition 6.1.** _Let_ **F** _be a forest. Then, there exists a spine_ \(\mathbf{S}\subseteq\mathbf{F}\) _ending at leaf v satisfying_

\(|\mathbf{F}[0..\mathsf{l}(v)\mathbf{)}|\le|\mathbf{F}|/2\text{\textit{and}}|\mathbf{F}[\mathsf{r}(v)..2|\mathbf{F}|+1\mathbf{)}|\le|\mathbf{F}|/2.\)

_Here,_ **F[**0**_.._l(_v_)**)** _and_ **F[r(_v).._2|**F**|+1**)** _are exactly the nodes right and left w.r.t._ **S**_, respectively._

**Proof.** Attach to **F** a new root such that **F** becomes a tree. We start by walking from the (new) root of **F** to a leaf. At each node _u_, we continue the walk to the rightmost child _w_ of _u_ that satisfies \(|\mathbf{F}[0..\mathsf{l}(w)\mathbf{)}|\le|\mathbf{F}|/2\).

We aim to maintain the invariant \(|\mathbf{F}[0..\mathsf{l}(u)\mathbf{)}|\le|\mathbf{F}|/2\) and \(|\mathbf{F}[\mathsf{r}(u)..2|\mathbf{F}|+1\mathbf{)}|\le|\mathbf{F}|/2\). This invariant clearly holds at the beginning, and ultimately, the walk traces out a spine **S** with the properties stated.

For the inductive step, observe that, by the definition of this walk, moving from _u_ to the next node _w_ ensures \(|\mathbf{F}[0..\mathsf{l}(w)\mathbf{)}|\le|\mathbf{F}|/2\). We must show that \(|\mathbf{F}[\mathsf{r}(w)..2|\mathbf{F}|+1\mathbf{)}|\le|\mathbf{F}|/2\). To do this, we consider two cases. If _w_ has a right sibling \(w'\), then \(|\mathbf{F}[0..\mathsf{r}(w)\mathbf{)}|=|\mathbf{F}[0..\mathsf{l}(w')\mathbf{)}|\ge|\mathbf{F}|/2\), which leads to \(|\mathbf{F}[\mathsf{r}(w)..2|\mathbf{F}|+1\mathbf{)}|=|\mathbf{F}|-|\mathbf{F}[0..\mathsf{r}(w)\mathbf{)}|\le|\mathbf{F}|/2\). On the other hand, if _w_ is the rightmost child of _u_, then \(|\mathbf{F}[\mathsf{r}(w)..2|\mathbf{F}|+1\mathbf{)}|=|\mathbf{F}[\mathsf{r}(u)..2|\mathbf{F}|+1\mathbf{)}|\le|\mathbf{F}|/2\).

**Definition 6.2.** _For each forest_ **F**_, fix an arbitrary spine_ **S** _ending in a leaf v satisfying Proposition 6.1. Define_ **L(F)**:=**F[**0**_.._l(_v_)**)** _and_ **R(F)**:=**F[r(_v).._2|**F**|+1**)**_, for the subforest containing the nodes on the left and right w.r.t. the fixed spine_ **S**_, respectively. If_ \(\mathbf{F}=\emptyset\) _is empty, then, we set_ \(\mathbf{L}(\mathbf{F})=\mathbf{R}(\mathbf{F})=\emptyset\).

We are now ready to show the reduction from SASED to SED.

**Lemma 6.3.** _Suppose there exists an algorithm for SED on two forests_ \(\mathbf{H},\mathbf{H}'\) _running in time_ \(\mathsf{T}_{SED}(m,m')=\mathcal{O}(f(m)g(m'))\)_, where_ \(m=|\mathbf{H}|,m'=|\mathbf{H}'|\) _and_ \(f(m)=\Omega(m)\), \(g(m')=\Omega(m')\) _are some functions. Then, there is an algorithm for SASED on two forests_ \(\mathbf{F},\mathbf{F}'\) _running in time_ \(\mathcal{O}(f(n)g(n')logn')\)_, where_ \(n=|\mathbf{F}|,n'=|\mathbf{F}'|\).

**Proof.** In the base case, if \(n'=0\), we can trivially return an empty set.

In general, we find a spine \(\mathbf{S}'\subseteq\mathbf{F}'\) using Proposition 6.1, and obtain \(\mathbf{L}(\mathbf{F}')\) and \(\mathbf{R}(\mathbf{F}')\) according to Definition 6.2. Then we recursively solve SASED on \((\mathbf{F},\mathbf{L}(\mathbf{F}'))\) and \((\mathbf{F},\mathbf{R}(\mathbf{F}'))\).

Spine to All-Subtree Tree Edit Distance (SASED) Input: Two forests \(\mathbf{F},\mathbf{F}'\), a spine \(\mathbf{S}\subseteq\mathbf{F}\), and sim(sub(_v_), sub(_v_<sup>∗</sup>)) for all \((v,v')\in(\mathbf{F}\backslash\mathbf{S})\times\mathbf{F}'\) Output: sim(sub(_v_), sub(_v_<sup>∗</sup>)) for all \((v,v')\in\mathbf{F}\times\mathbf{F}'\).

All Subtrees Tree Edit Distance (All-Subtrees-TED) Input: Two forests \(\mathbf{F},\mathbf{F}'\). Output: sim(sub(_v_), sub(_v_<sup>∗</sup>)) for all \((v,v')\in\mathbf{F}\times\mathbf{F}'\).

