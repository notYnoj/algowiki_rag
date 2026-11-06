the desired contradiction<sup>4</sup>. This shows that indeed, _G_ must have a subgraph of odd-girth at least _g_ on which _f_ takes a value of at least _k_, concluding the proof.

## 3 Multicolor Ramsey numbers of odd cycles

In this section, we present the proof of our Ramsey-theoretic result, namely Theorem 1.7. To prove this lower bound, we draw from the ideas of the recent recursive construction of triangle-free edge-colorings of large complete graphs by OpenAI [Ope26] which they used for the superexponential lower bound on _R<sub>k</sub>(C_<sub>3</sub>), and modify this construction for the purpose of avoiding short monochromatic odd cycles. In the next subsection, we first collect the key auxiliary results from [Ope26] that we shall be reusing. In the second subsection we then present our modified construction-first on a high level, explaining the rough structure of our new edge-coloring, how it relates to OpenAI’s construction, and where the new idea for extending from the exclusion of triangles to the exclusion of short odd cycles lies. Afterwards, we then formally prove a key technical recursion (Lemma 3.3) which can be easily used to prove the desired lower bound on _R<sub>K</sub>_(O_<sub>p</sub>_) by induction on _p_.

### 3.1 Auxiliary results

In this preliminary section we recall two auxiliary results that were also used in the proof of the lower-bound for multicolor Ramsey numbers by OpenAI [Ope26]. The following two statements correspond exactly to Lemma 2.2 and Lemma 2.3 in the OpenAI paper (cf. [Ope26], Chapter 9). The first lemma originates from lower bounds on the hat guessing numbers of complete bipartite graphs (cf. [ABEST20]), while the second lemma is a simple statement about the existence of a large family of equal-size subsets of a finite ground set with pairwise large differences.

**Lemma 3.1.** _Let H be a sufficiently large integer, and set_<tbc>

\(m=\lceil 2HlogH\rceil,s=m(m+1)+1.\)

<tbc>_Then there are fixed maps_<tbc>

\(f,g:[H]^s\longrightarrow[H]^s\)

<tbc>_such that, for every_ \(x,y\in[H]^s\)_, there is a_ \(d\in[s]\) _for which_<tbc>

\(x_d=(f(y))_d\text{\textit{or}}y_d=(g(x))_d.\)

<tbc>**Lemma 3.2.** _Let H be a sufficiently large integer, and set_<tbc>

\(m=\lceil 2HlogH\rceil,s=m(m+1)+1,t=s\lceil logH\rceil,M_j=jt(0\le j\le H).\)

<tbc>_Then, for every_ \(1\le j\le H\)_, there is a family of_ palettes<tbc>

\(\mathcal{P}_j\subseteq\left(\begin{array}{ c }
\lfloor jt\rfloor \\
t
\end{array}\right)\)

<sup>4</sup>The final inequality holds for all sufficiently large _k_: when _p_=1, it follows from the inequality \((3+\varepsilon/2)(1+\varepsilon/100)<3+\varepsilon\), while for \(p\ge 2\) a fixed power of \(exp^{(p-1)}(k^{3+\varepsilon/2})\) is asymptotically dominated by \(exp^{(p-1)}(k^{3+\varepsilon})\).

