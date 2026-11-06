We now use the principle of deferred randomness to analyze this version of the algorithm. Let _E<sub>t</sub>_ be the "evolving set" of elements in \(\{x_i\}_{1\le i\le t}\) that are not eliminated by the modified algorithm after it has seen the elements _x_<sub>1</sub>_,x_<sub>2</sub>_...,x<sub>t</sub>_ in that order. Remember that \(\sigma_t\) is the subsequence of (_x_<sub>1</sub>_,...,x<sub>t</sub>_) corresponding to elements that are sampled. We can simulate the process of generating the sets _E<sub>t</sub>_ and \(\sigma_t\) in the following way:

1. Start with \(E_0,\sigma_0=\langle\rangle\).<tbc>

2. At step \(1\le t\le N\), toss a biased coin with success probability 2_k/N_. Update<tbc>

<tbc>\(\sigma_t=\left\{\begin{array}{ c c }
\sigma_{t-1}\circ x_t, & \text{if coin flip succeeds at t} \\
\sigma_{t-1}, & \text{otherwise.}
\end{array}\right.\)<tbc>

<tbc>and<tbc>

<tbc>\(E_t=\left\{\begin{array}{ c c }
E_{t-1}\circ x_t, & \text{if}x_t-y\notin\text{env}(B(\sigma_{t-1})) \\
E_{t-1}, & \text{otherwise.}
\end{array}\right.\)<tbc>

<tbc>where _y_ is the first element sampled.

Observing that

\(|B(\sigma_t)|-|B(\sigma_{t-1})|=\unknown[x_t-y\notin\text{env}(B(\sigma_{t-1}))\wedge\text{coin flip succeeds at}t]\)<br>
\(=(|E_t|-|E_{t-1}|)\cdot\unknown[\text{coin flip succeeds at}t].\)

Taking expectations on both sides gives<tbc>

\(\mathbb{E}[|E_t|-|E_{t-1}|]=\frac{N}{2k}\cdot\mathbb{E}[|B(\sigma_t)|-|B(\sigma_{t-1})|].\)

<tbc>Summing this over \(1\le t\le N\) gives

\(\mathbb{E}[|E_N|]=\frac{N}{2k}\cdot\mathbb{E}[|B(\sigma)|]\le\frac{N}{2k}\cdot k=\frac{N}{2}.\)

## A.2 The conic dimension of the Boolean Point Sets

An important special case is that of point sets consisting of Boolean vectors in {0,1}_<sup>d</sup>_, i.e., of subsets of the hypercube. For completeness, we present a repackaging of the bound on the conic dimension from \[KLMZ17\]. To begin, we recall the fact that all subset sums of any linearly independent set of vectors are distinct, and extend this fact to the case of conic independence. The bound on the conic dimension of Boolean point sets then follows by a counting argument.

**Lemma A.5.** _If_ \(\sigma=(y_1,y_2,\dots,y_{k+1})\) _is a conically independent sequence, then all subset sums_<tbc>

\(\sum_{i\in S}(y_{i+1}-y_i),S\subseteq[k],\)

<tbc>_are distinct._

