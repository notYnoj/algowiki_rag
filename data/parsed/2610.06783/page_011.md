_k_-Clique to triangle detection, our new Exact Triangle algorithm immediately implies _the first algorithms running in_ \(O(n^{k-\varepsilon})\) _time for an_ \(\varepsilon>0\) (Section 5.3), refuting the weighted _k_-Clique hypotheses \[AL13, LVW18, BDT16\].<tbc>

• **3XOR.** Given three lists of _n_ vectors in \(\mathbb{F}_2^d\), where _d=O_(log_n_), decide whether there are vectors _a_, _b_, and _c_, one from each list, with \(a\oplus b\oplus c=0\), where \(\oplus\) denotes the bitwise XOR. This is a well-studied variant of 3SUM \[JV16, DSW18\]. It is not known to reduce to 3SUM, but the same approach works for it as well, so _we give the first truly subquadratic algorithm_ (Remark 23).<tbc>

• **Counting versions.** Counting the zero-weight triangles of an Exact Triangle instance, or the solutions of a 3SUM instance, is equivalent to the decision problem \[CVX23\], and for 3SUM the equivalence also holds under deterministic reductions \[FJX25\]. Similarly, counting the witnesses of each entry of the (min,+)-product is equivalent to computing the (min,+)-product \[CVX23\]. _We give the first truly subcubic algorithms for #Exact Triangle and for counting the witnesses of the_ (min,+)_-product, and the first truly subquadratic algorithm for #3SUM._ See \[CVX23, FJX25\] for applications.

For problems that are only known to be 3SUM-hard or APSP-hard, such as many of the geometric problems of \[GO95\] and the dynamic problems of \[Păt10, AV14, KPP16\], we get no faster algorithms, since the reductions go the other way. For instance, it is now open whether one can find three collinear points among _n_ points in the plane in truly subquadratic time.

## Relationships to some unaffected conjectures.

While we refute various hypotheses, their underlying problems are all similar in nature. We outline how a few other important problems with fine-grained hypotheses differ from 3SUM, Exact Triangle, and APSP, signaling that refuting them might require other techniques.

We begin with CNF-SAT and Orthogonal Vectors (OV). Neither of these problems is known to reduce to All-Edges Sparse Triangle or similar problems. CNF-SAT and Exact Triangle are known to both reduce to certain triangle problems (Matching Triangles and Triangle Collection \[AVY15\]), but these triangle problems concern the triangles in each of about _n_<sup>3</sup> color triples in dense node-colored graphs, and our techniques do not appear to work there.

Unlike CNF-SAT and Orthogonal Vectors, 3SUM, APSP, and Exact Triangle have long been known to have fast algorithms in certain more powerful models.

3SUM (and more generally _k_-SUM) and also Exact Triangle have very efficient _linear decision trees_. Following a long line of work \[Mey84, Eri99, AC05, GS17, ES17, CIO16, GP18, KLM19\], it is now known \[KLM19\] that for every \(k\ge 3\), _k_-SUM has 2_k_-linear decision trees of depth _O(n_log<sup>2</sup>_n_), and Exact Triangle in _m_-edge graphs has 6-linear decision trees of depth _O(m_log<sup>2</sup>_m_). APSP has decision trees of depth \(\tilde{O}(n^{2.5})\) \[Fre76\]. No such results are known for CNF-SAT and OV.

3SUM, Exact Triangle, and APSP also all have fast _nondeterministic and co-nondeterministic algorithms_. A nondeterministic algorithm for a decision problem verifies a proof for YES, and a co-nondeterministic algorithm verifies a given proof for NO. Carmosino et al. \[CGI<sup>+</sup>16\] showed that 3SUM can be solved nondeterministically and co-nondeterministically in \(\tilde{O}(n^{1.5})\) time, and Exact Triangle and APSP in \(\tilde{O}(n^{(3+\omega)/2})\) time. The best known co-nondeterministic algorithms for CNF-SAT and OV are no better than the known deterministic ones, and \[CGI<sup>+</sup>16\] postulate NSETH, the hypothesis that CNF-SAT requires \(2^{n-\alpha(n)}\) time even for co-nondeterministic algorithms. They then prove that if NSETH is true, then there cannot be a deterministic (or<tbc>

