## 4 Counting Lower Bound

A natural starting place to study what can and cannot be solved with small local communication complexity is the fundamental task of counting. In more detail, we study the local communication complexity of solving (_n,k_)-counting function. Formally, we seek to identify a parameter _k_ for the counting function \(g_k^n\) (defined in the introduction), such that the local complexity of the function is strictly greater than 1. The core result of this section is a lower bound that establishes for any sufficiently large _n_, \(lcc(g_{17}^n)>1\). We emphasize that is the first known lower bound on local complexity for a concrete function (prior work \[4\] contains only existential bounds based on counting arguments).

### 4.1 Proof Summary

At a high level, our proof strategy begins by focusing on local complexity of the related (_n,k)-threshold detection_ problem, which requires the nodes to determine if at least _k_ of the input bits are 1. We prove that any protocol that solves this problem with local complexity 1 is highly constrained in its operation, generating executions that can be understood as a bit traveling in a chain, from one node to the next, with the final node making a decision.

Given such a structure, we apply a combinatorial argument to argue that for a sufficiently large constant threshold _k_, we can construct two execution chain prefixes such that: (1) the correct output is different for each chain (i.e., one chain has enough 1’s to exceed the threshold while the other does not); and (2) the node at the end of both prefixes sends the same bit to the next link, obfuscating the actual contents of its predecessors. The existence of these two prefixes can be deployed to generate an incorrect answer in at least one of the two cases, contradicting the assumption that any algorithm correctly solves threshold detection for this _k_ parameter.

Finally, once we bound threshold detection, we then use a reduction argument to obtain our final bound for the more natural counting problem.

### 4.2 Bounding Threshold Detection

We begin by proving a lower bound on the local complexity of the (_n,k)-threshold detection_ boolean function, that evaluates to 1 if and only if at least _k_ out of _n_ input bits are 1. Formally, we use \(f_k^n\) to indicate this function for a given pair of parameters _k_ and _n_, and define it as:

\(f_k^n=\left\{\begin{array}{ c c }
1 & \text{if}\#_1(a_1\dots a_n)\ge k, \\
0 & \text{else.}
\end{array}\right.\)

Our goal is to prove that the following, which establishes for sufficiently large _n_ value that threshold detection for _k=_9 requires a local complexity greater than 1.

**Theorem 4.1.** _Fix some network size n\>_9_, threshold_ \(k,9\le k\le n-8\)_. It follows:_ \(lcc(f_k^n)>1\).

Before proceeding to main proof of this theorem, we establish some useful preliminaries that formalize the constraints suffered by any threshold detection algorithm with a minimum local complexity of 1. In the following, we use the notation _P_<sub>1</sub>_,P_<sub>2</sub>_,...P<sub>n</sub>_ to represent the _n_ players. We say that _P<sub>i</sub>_ is an _initiator_ with respect to a given input bit if its initialization code for that input bit has it transmit a bit before receiving any bits. A key property of a minimal local complexity environment is that a correct protocol can only ever have one initiator:

**Lemma 4.2.** _Fix some n\>_4_, k,_ 3_\<k\<n, and protocol_ P _that computes_ \(f_k^n\) _with lcc_(P)=1_. There exists a player P<sub>i</sub> such that for every input assignment, P<sub>i</sub> is the only initiator among the n players._

