**Theorem 2.3.** _There is an algorithm for unweighted UFED running in time_ \((n/n')^{1+o(1)}\cdot\left(\mathsf{T}_{MonMUL}(n')+n'^{2+o(1)}g(n')\right)\) _where n_=|**F**|, \(n'=|\mathbf{F}'|\), \(n\ge n'\) _and_ \(\mathsf{T}_{MonMUL}(n',n',n',\mathrm{D})=\mathcal{O}(f(n')g(\mathrm{D}))\) _for some functions f, g._

In the remainder of the technical overview of the unweighted algorithm, we give an overview of the proof of Theorem 2.3. Further simplifying under Assumption B, our previous discussion shows that it is enough to only compute the third FED output. To this end, consider the alignment graph \(\bar{\mathbf{G}}\) of two forests \(\mathbf{F},\mathbf{F}'\) with vertices \(\mathbf{F}\times\mathbf{F}'\) arranged in a grid where both trees are ordered in pre-order traversal.

The grid contains horizontal and vertical edges of weight 0 (corresponding to vertex deletions) and edges from \((v,v')\) to \((w,w')\) of weight \(\mathrm{sim}(\mathrm{sub}(v),\mathrm{sub}(v'))\) where _w_ (resp. \(w'\)) is the first vertex after sub(_v_) (resp. \(\mathrm{sub}(v')\)) in pre-order traversal i.e. the first vertices that can be aligned after aligning sub(_v_) and \(\mathrm{sub}(v')\). The desired output of FED then corresponds to computing all distances from the left border to the right border of the grid. In contrast, the general FED problem asks to compute all distances from the left and bottom borders to the right and top borders.

The alignment graph **G** has dimension \(n\times n'\), so ideally we hope to be able to breaking the it into \(\mathcal{O}(n/n')\) subgraphs, each of size \(\mathcal{O}(n')\times\mathcal{O}(n')\). Then, we can compute FED on each subgraph and combine the results using \(\mathcal{O}(n/n')\) bounded monotone max-plus products, thus computing the desired FED output in total time \(\mathcal{O}((n/n')\cdot\mathsf{T}_{MonMUL}(n'))\). However, in reality, it is not simple to decompose **G** to \(\mathcal{O}(n/n')\) subgraphs and combine the results, as there can be edges connecting two nodes that are far away in the alignment graph. Hence, in our actual algorithm, we apply a divide-et-impera scheme utilizing Mao’s tree decomposition \[Mao22\], which incurs an additional \((n/n')^{o(1)}\) factor. Still, we obtain the desired almost-linear dependence on the size of the larger forest _n_=|**F**|. In particular, at least under Assumption B, both FED and SED can be computed in time \(\mathcal{O}(\mathrm{min}(m,m')^{(1+\omega)/2}\mathrm{max}(m,m')^{1+o(1)})\).

To remove Assumption B, we must be able to additionally compute distances from the left border to the top border in BBD instances, corresponding to the second and fourth outputs of the FED problem (see Section 4.6). In the SED instance we then proceed by careful case analysis to ensure that we consider all possible alignments between the two forests (see Section 5.5). Applying Lemma 2.1 then yields an \(n^{1+o(1)}n'^{(1+\omega)/2}\)-time algorithm for unweighted tree edit distance between forests of size \(n,n'\) and \(n\ge n'\), proving Corollary 1.2.

r'
(r(si+1, z')
Si
Si+1
(r(si, y')
(l(si), x')
x'
w'
q'
z'
y'

**Figure 5** The alignment whose value is computed in Equation (2) visualized as a Border-to-Border (BBD) distance computation. The value of the orange path corresponds to the first summand, or the alignment between **F**\[l(_si_)_.._l(_si_+1) and \(\mathbf{F}'[x'..w'\) ). The value of the blue path corresponds to the last summand, or the alignment between **F**\[r(_si_+1)_.._r(_si_) and \(\mathbf{F}'[z'..y'\) ). For every pair of points on the right border, we have the optimal alignment between sub(_si_+1) and \(\mathbf{F}'[w'..z'\) ).

