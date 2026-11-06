<tbc>**Remark 3.4.** Although we generally suppress floors and ceilings throughout the analysis, Definition 3.3 is one location where a brief clarification is helpful. When \(\alpha b\notin\mathbb{N}\), the collection of standardized near- equipartitions NE<sub>std</sub>(_y_) should be defined by assigning either \(\lfloor\alpha b\rfloor\) or \(\lceil\alpha b\rceil\) to each superscript _i_. This is done in such a way that for every _k_, the sum of the first _k_ block lengths differs from \(\alpha bk\) by at most 1. Since \(\alpha b\) is fixed, such a choice can be made once and for all. These adjustments do not affect the asymptotic estimates in the proof, and we suppress the corresponding routine modifications, both here and in all other instances where floors and ceilings are omitted. \(\triangle\)

Induced near-equipartitions of _y_ correspond to ways of partitioning _y_ into _B_ blocks so that very few of these blocks are multiplicatively far from \(\alpha b\), and they should (in light of Remark 3.2) importantly be thought of as capturing the _induced_ block structure of a typical outcome of a string drawn from the planted model. On the other hand, owing to our choice of definitions and the strict restriction that "good blocks" _y_<sup>(_i_)</sup> must have size \(\alpha b\), the collection of standardized near-equipartitions of _y_ is far smaller. This will be crucial in Section 3.3, where we establish an approximation-type result for the following notion of total agreement when substituting NE<sub>ind</sub>(_Y_) for NE<sub>std</sub>(_Y_) via the _standardization_ algorithm.

**Definition 3.5** (Induced and standardized total alignment)**.** Given \(y\in\{0,1\}^*\), we respectively define its _induced total alignment_ and its _standardized total alignment_ with the string \(x=\left(x^{(1)},\dots,x^{(B)}\right)\in\{0,1\}^N\) via

\(T_\mathrm{ind}(x,y):=\mathrm{sup}_{\left(y^{(1)},\dots,y^{(B)}\right)\in\mathcal{N}\mathcal{E}_\mathrm{ind}(y)}\frac{1}{B}\sum_{i=1}^BA_\mathrm{loc}\left(x^{(i)},y^{(i)}\right);\) (3.5)

\(T_\mathrm{std}(x,y):=\mathrm{sup}_{\left(y^{(1)},\dots,y^{(B)}\right)\in\mathcal{N}\mathcal{E}_\mathrm{std}(y)}\frac{1}{B}\sum_{i=1}^BA_\mathrm{loc}\left(x^{(i)},y^{(i)}\right).\) (3.6)

The individual _local alignment_ terms (i.e., the summands) on the RHS of (3.5) and (3.6) are defined via

\(A_\mathrm{loc}\left(x^{(i)},y^{(i)}\right):=\left\{\begin{array}{ c c }
0 & \mathrm{maj}(x^{(i)})\neq\mathrm{maj}(y^{(i)}) \\
1\wedge\delta\Delta(y^{(i)}) & \mathrm{maj}(x^{(i)})=\mathrm{maj}(y^{(i)})
\end{array};\Delta(y^{(i)}):=\left|\sum_{j=1}^{\left|y^{(i)}\right|}\left(2(y^{(i)})_j-1\right)\right|,\) (3.7)

where \(\mathrm{maj}(z)\in\{0,1\}\) denotes the majority bit of \(z\in\{0,1\}^*\), taken to be 1 in the case of a tie.

Corresponding the binary string _y_<sup>(_i_)</sup> to a realization of a simple random walk with Rademacher increments in the natural way, we note that the expression \(\Delta(y^{(i)})\) in (3.7) is the absolute value of the random walk at time |_y_<sup>(_i_)</sup>|. In particular, we may equivalently write the local alignment via (with sign(0)=1)

\(A_\mathrm{loc}\left(x^{(i)},y^{(i)}\right)=\left\{\begin{array}{ c c }
0 & \mathrm{sign}\left(\sum_{j=1}^{\left|x^{(i)}\right|}\left(2(x^{(i)})_j-1\right)\right)\neq\mathrm{sign}\left(\sum_{j=1}^{\left|y^{(i)}\right|}\left(2(y^{(i)})_j-1\right)\right); \\
1\wedge\delta\Delta(y^{(i)}) & \mathrm{sign}\left(\sum_{j=1}^{\left|x^{(i)}\right|}\left(2(x^{(i)})_j-1\right)\right)=\mathrm{sign}\left(\sum_{j=1}^{\left|y^{(i)}\right|}\left(2(y^{(i)})_j-1\right)\right).
\end{array}\right.\) (3.8)

We mention in passing that the notions of local alignment and total alignment that we introduce here are loosely reminiscent of recent ideas in the trace reconstruction literature. For instance, \[HPP18\] introduced robust alignment tests motivated by this correspondence, together with the appropriate scaling needed to make the consequences of such tests transparent.

Our next definition introduces the collection of _N_-bit strings that we restrict our attention to.

**Definition 3.6** (Typical ambient strings)**.** We say that \(x\in\{0,1\}^N\) is _typical_ if at least _B/_10 of the blocks _x_<sup>(_i_)</sup> are such that \(\Delta(x^{(i)})\ge\sqrt{b}\).

