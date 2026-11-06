sample. Summing the preceding bound over all strings and block choices therefore gives, by (12),

\(Pr[G[S]\text{is}k\text{-colorable}]\le\sum_{t=1}^T(4k)^te^{-\alpha tq/4}\)<br>
\(\le\sum_{t=1}^T(4k)^t(16k)^{-t}\)<br>
\(=\sum_{t=1}^T4^{-t}\le\frac{1}{3}.\)

Thus the induced subgraph is non-_k_-colorable with probability at least 2/3. Finally, \(T=O(k/\varepsilon)\), \(\frac{1}{\alpha}=\frac{4(k+1)}{\varepsilon}\) , and log(16_k_)=_O_(log_k_), proving (13).

## 8 Concluding remarks

The proof combines the container method with a palette-based coloring process tailored to _k_- colorability.

The reason we can improve upon the bound of [7, 19] is that our method allows us to introduce a structure to choose _t_ blocks out of 2_t_ blocks. By contrast, the fingerprint in [7, 19] is effectively enumerated by a factor of the form \(\genfrac(){pt}{2}{q}{t}\), together with the corresponding color assignments. Without nontrivial modifications, their mechanism does not support a \(\genfrac(){pt}{2}{2t}{t}\)-type encoding like the one used in our algorithm. In the Kushnir-Shapira construction, the container at round _t_ does not depend on the entire independent set _I_; it depends only on the fingerprint from the first _t_ rounds. However, every vertex in vert(_F<sub>t</sub>_) must be assigned a color in order to determine _F<sub>t</sub>_. If one instead starts with a subset \(V\subseteq\text{vert}(I)\) without specifying the colors of all vertices in _V_ , different choices of colors can lead to different processes and hence to different projected containers vert(_C<sub>t</sub>_). See Appendix A for a concrete example illustrating the algorithms.

A second important ingredient is how the assumption that the original graph is \(\varepsilon\)-far from _k_-colorable forces some properties. Intuitively, call a vertex "bad" at a given stage if the process is unwilling to assign it a color. If the sampled subgraph is _k_-colorable, the process can preserve its proper coloring and continue; conversely, if too few vertices become bad throughout the process, the reconstruction lemma produces a coloring of the original graph with fewer than \(\varepsilon n^2\) monochromatic edges, contradicting \(\varepsilon\)-farness. Moreover, a coloring process in which many such "bad" vertices appear occurs with very low probability if the subgraph _S_ is _k_-colorable.

## Statement on AI usage

The author had early discussions with ChatGPT about how to approach the palette system. The author then conceived how palettes could be used within the proof and wrote out the complete argument. ChatGPT was subsequently used to edit the author’s first draft of the proof into a form conforming to standard conventions of mathematical exposition. After this, the author reviewed the draft in full and polished the exposition to obtain the final version of this paper. The author takes full responsibility for all content in this paper.

