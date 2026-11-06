We now define the weight of triangle (_ijk_):

\(w(ijk)=max\{0,max_lf(l)\}.\)

This concludes the definition of triangle weights.

## 5 Verifying the constraints

### 5.1 The triangulation has weight 2_n_-6

The graph _T_ has 2_n_ triangles and _n_+2 vertices. Every triangle of _T_ has weight 1 except in the neighborhood of vertices of degree less than 6: there are 4 vertices of degree 4, adjacent to 4 vertices of degree 5; in the neighborhood of each of these 4 pairs, there are 6 triangles of weight 3/4, each accounting for a weight deficit of 1/4. There is a total of 24 triangles of weight 3/4 and the total weight is thus 2_n_-24/4=2_n_-6.

### 5.2 Weights of large triangles

We want to check that each flip decreases the weight by at most 1, that is, that each quadruple {_i,j,k,l_} (viewed as a tetrahedron with all triangles oriented outwards) satisfies

\(|w(ijl)+w(jkl)+w(kil)+w(kji)|\le 1.\)

We will first show the following lemmas.

**Lemma 2.** _If_ {_i,j,k_} _is not a triangle of T, then_ \(|w(ijk)|\le 1/2\).

**Proof.** If {_i,j,k_} has two edges in _T_, the proof is by inspection. If it has one edge in _T_, the result follows from the fact that all capacities are at most 1/2. If it has no edge in _T_, its weight, if non-zero, is determined by some fourth vertex _l_. By induction _ijl,jlk,lki_ all have weight at most 1/2, so _f(l_) is at most \(1/2+1/2+1/2-1\le 1/2\). Hence the lemma.

We will show that all large triangles have weight 0.

**Lemma 3.** _If d(i,j)\>c_+2 _and both vertices i and j are at distance greater than c from the sink, then the weight of_ (_ijk_) _is_ \(|w(ijk)|\le 1/4\).

