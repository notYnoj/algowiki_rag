In our work, we will specifically work with rectangular matrices, and thus require the following simple lemma. We use T<sub>MUL</sub>(_a,b,c_) to denote the time required to compute the (min,+) product between arbitrary \(a\times b\) integer matrices and \(b\times c\) integer matrices.

**Lemma 3.15.** _Suppose_ \(n\ge m\)_. Then,_

\(\mathcal{O}(\mathsf{T}_{MUL}(n,m,m))=\mathcal{O}(\mathsf{T}_{MUL}(m,n,m))=\mathcal{O}(\mathsf{T}_{MUL}(m,m,n))=\mathcal{O}(n/m\cdot\mathsf{T}_{MUL}(m))\text{\textit{and}}\)<br> \(\mathcal{O}(\mathsf{T}_{MonMUL}(n,m,m,m))=\mathcal{O}(\mathsf{T}_{MonMUL}(m,n,m,m))=\mathcal{O}(\mathsf{T}_{MonMUL}(m,m,n,m))=\mathcal{O}(n/m\cdot\mathsf{T}_{MonMUL}(m)).\)

We require the following bound on (min,+)-product between monotone matrices where the entries are bounded by D.

**Lemma 3.16** ([Dür23])**.** \(\mathsf{T}_{MonMUL}(n,n,n,\mathrm{D})=\tilde{\mathcal{O}}(\sqrt{\mathrm{D}}n^{(2+\omega)/2})\).

## 4 Reduction from Forest Edit Distance to APSP

In this section, we focus on proving Main Theorem 4 which we restate here and its unweighted version Theorem 4.1.

**Main Theorem 4.** _Suppose there exists an algorithm computing the min-plus product of two_ \(m\times m\) _matrices in time_ T<sub>MUL</sub>(_m). Then, there is an algorithm for FED running in time_ O(T<sub>MUL</sub>(_n_)+_n_<sup>2+_o_(1)</sup>)_, where_ \(n=\mathrm{max}(|\mathbf{F}|,|\mathbf{F}'|)\).

**Theorem 4.1.** _There is an_ O(T<sub>_MonMUL_</sub>(_n_)+_n_<sup>2+_o_(1)</sup>_g(n_)) _time algorithm for unweighted FED where_ \(n=\mathrm{max}(|\mathbf{F}|,|\mathbf{F}'|)\) _and_ T<sub>_MonMUL_</sub>(_n,n,n,_D)=O(_f(n)g_(D)) _for some functions f,g._

To approach FED, we adopt a conceptual shift, viewing it as a graph problem. Our perspective extends the computation of border-to-border distances in the alignment graph for string edit distance [LMS98, Tis06, ACS08, Kle05]. These distances precisely capture the edit distance between the prefix of one string and the suffix of the other, as well as between the entire string and all infixes of the second.

In this section, we denote by dist<sub>G</sub>(_u,v_) the longest distance (rather than shortest distance) from \(u\in\mathbf{G}\) to \(v\in\mathbf{G}\) in a directed weighted acyclic graph **G**. If _v_ is not reachable from _u_, then \(\mathsf{dist}_\mathbf{G}(u,v)=-\infty\). This shift in definition is merely a notational change, given that we are working with a directed acyclic graph (by simply inverting the sign of the weights, one can switch between shortest and longest distances).

Throughout this section, we will give algorithms for the general setting of weighted tree edit distance, adding where appropriate optimizations that can be made for the unweighted tree edit distance problem. In Section 4.6, we describe how to compute FED efficiently on unbalanced instances, i.e. when one forest is significantly larger than the other. While Section 4.6 is necessary to obtain Main Theorem 2 for unweighted TED, readers interested only in Main Theorem 4 may skip it.

### 4.1 Generalizing alignment graphs

In this (sub)section, we extend the concept of the alignment graph for two strings to a broader framework capable of representing FED. Similar to the string case, the alignment graph we examine has a grid as its vertex set. This grid includes directed edges of zero weight, connecting every grid point to its upper and right neighbour. Moreover, from each grid point (_i,j_), there is an additional edge connecting to a subgrid, whose lower-left corner is (_i_+1_,j_+1) and whose top-right corner coincides with that of the entire grid.

