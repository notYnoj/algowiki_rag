## 8 Appendix. Catalog of One-Cycle Chord Diagrams

This section contains a comprehensive graphical atlas of representative one-cycle signed chord diagrams generated for \(g\in\{-5,-4,\dots,3\}\). New figures can be inserted into the template structures below.

### 8.1 From the computational code to the drawing code

For computations a one-cycle chord diagram with _k_ chords is stored as a word _w_=(_w_<sub>1</sub>_,...,w_<sub>2_k_</sub>) in which every label \(m\in\{1,\dots,k\}\) occurs exactly twice (the two ends of chord _m_), together with a sign \(\varepsilon_m\in\{+1,-1\}\) for each chord. The word is normalised by first occurrence, so the labels first appear in the order 1,2_,...,k_. Orientable diagrams (\(g\ge 0\), _k_=2_g_) have all \(\varepsilon_m=+1\); non-orientable ones (_g\<_0, _k_=-_g_) have at least one \(\varepsilon_m=-1\).

The drawing code used by the macro \\cd is a list of triples a/b/c, where _a\<b_ are the cyclic numbers of the ends of a chord on the circle with _n_=2_k_ points, and c is its colour. The conversion is:

1. Number the ends cyclically 1_,...,n_ in the order of the word; position _i_ is drawn at the polar angle \(90^\circ-360^\circ i/n\), i.e. clockwise starting just after the top point.<tbc>

2. For each label _m_ let _a<sub>m</sub>\<b<sub>m</sub>_ be the two positions with _w<sub>a<sub>m</sub></sub>=w<sub>b<sub>m</sub></sub>=m_.<tbc>

3. Put _c<sub>m</sub>_=`B` (blue) if \(\varepsilon_m=+1\) and _c<sub>m</sub>_=`R` (red) if \(\varepsilon_m=-1\).<tbc>

4. Output the triples _a<sub>m</sub>/b<sub>m</sub>/c<sub>m</sub>_ for _m_=1_,...,k_ separated by commas. Because of the normalisation \(a_1<a_2<\cdots<a_k\), no extra sorting is needed.

The diagram is then inserted as \\cd\[s\]{n}{list}, with _n_=2_k_ and scale _s_ (we use 0.62-0.65). For example, the word 12123434 (all signs +1) gives \\cd\[0.62\]{8}{1/3/B,2/4/B,5/7/B,6/8/B}. The empty diagram of the sphere is drawn as \\cd\[0.62\]{2}{}}.

### 8.2 Order, numbering, duality

Within each genus the diagrams are the representatives of the equivalence classes under rotation, reflection and relabelling, one per class: the representative is the lexicographically smallest normalised word in its class, and the classes are listed in increasing order of this word. The number under a diagram is the counter cdn, reset at the start of each genus and continued across figures if the list of one genus does not fit into one figure.

The dual diagram is obtained by traversing the unique face of the diagram: starting at an arc of the circle, we move along the circle to the next chord end, cross the chord to its other end, and continue along the circle in the same direction if the chord is untwisted and in the opposite direction if it is twisted, until we return to the starting arc. The sequence of chords crossed along the way is the word of the dual diagram. The dual chord _m_ is untwisted if the two crossings of chord _m_ go in opposite directions (from its smaller end to its larger one and back), and twisted if both go the same way. The dual is then reduced to its canonical form and found in the same list; a diagram is self-dual if it coincides with its own dual, otherwise it forms a dual pair. After each list we state the numbers of the self-dual diagrams and of the dual pairs.

### 8.3 Orientable Surfaces

1

1

Figure 1: One-cycle chord diagrams for the sphere (_g_=0, _k_=0).

Figure 2: One-cycle chord diagrams for the torus (_g_=1, _k_=2).

