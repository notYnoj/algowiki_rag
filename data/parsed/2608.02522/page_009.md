_of size_<tbc>

\(B_j:=|\mathcal{P}_j|\ge\frac{\genfrac(){pt}{2}{t}{t}^{jt}}{\sum_{d=0}^{s-1}\genfrac(){pt}{2}{t}{d}\genfrac(){pt}{2}{(j-1)t}{d}}\ge\frac{j^t}{s\left(e^2j\lceil logH\rceil^2\right)^s},\)

<tbc>_such that distinct_ \(P,Q\in\mathcal{P}_j\) _satisfy_

\(|P\backslash Q|=|Q\backslash P|\ge s.\)

These are the only auxiliary results from [Ope26] that we shall need. In the next section, we give a self-contained proof of Theorem 1.7 based on these statements.

## 3.2 Proof of Theorem 1.7

In this section, we prove Theorem 1.7. As mentioned previously, the construction is a modification of the construction for the triangle-case from [Ope26], and the main change comes from refining their recursive colorings by a second coordinate, which allows us to successively increase the odd-girth of the color classes by 2 with every application of the construction. Despite the large overlap with OpenAI’s proof, we chose to give a self-contained proof of Theorem 1.7 here (quoting only Lemmas 3.1, 3.2 and repeating large parts of the arguments from [Ope26]). The reason is that various properties of their colorings will be needed that are not explicitly stated outside of proofs in [Ope26].

Put \(\mathcal{O}_0=\varnothing\). For \(r\ge 0\) and \(n\ge 1\), let _a<sub>r</sub>(n_) be defined as the least integer \(a\in\mathbb{N}\) such that there is an edge-coloring of _K<sub>n</sub>_ in _a_ colors with no monochromatic member of O_<sub>r</sub>_ (this can be seen as an integer inverse function of the multicolor Ramsey number of O_<sub>r</sub>_). Thus _a_<sub>0</sub>(_n_)=1, and _a<sub>r</sub>(n_) is nondecreasing in _n_. The central new step to proving Theorem 1.7 is captured by the recursion stated in the key lemma 3.3 below. It essentially shows that one can construct, starting from an edge-coloring of a small complete graph without a monochromatic odd cycle of length at most 2_r_+1, an edge-coloring of a much larger complete graph without a monochromatic odd cycle of length at most 2_r_+3 and which does not use many more colors than the original coloring.

**Lemma 3.3.** _Fix an integer_ \(r\ge 0\)_. Let H be a sufficiently large integer, and define_<tbc>

\(m=\lceil 2HlogH\rceil,s=m(m+1)+1,t=s\lceil logH\rceil\)

<tbc>_as well as_<tbc>

\(N_H=\left\lceil\frac{(H!)^{t-s}}{s^H\left(e^2\lceil logH\rceil^2\right)^{sH}}\right\rceil.\)

<tbc>_Then_

\(a_{r+1}(N_H)\le Hta_r(H+1).\) (1)

Before starting the formal proof, let us give a high-level and informal description of the construction from OpenAI [Ope26] for the triangle case and where the modification lies.

The construction of OpenAI builds an edge-coloring without monochromatic triangles of larger and larger complete graphs recursively through several stages, which are<tbc>

