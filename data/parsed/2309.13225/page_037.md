<tbc>to obtain the same approximation. To utilize fast matrix multiplication, let _x_ be some parameter to be optimized. Since \(P\subset E_3\) is handled by `SparseAPASP`, we decompose the graph _G<sub>x</sub>_=(_V,E<sub>n<sup>x</sup></sub>_) into 3 levels. Then, for \(1\le j\le(1-x)logn\) thresholds \(t_j=\frac{n}{2^j}\), we compute a dominating set _C<sub>j</sub>_ and edge set _F<sub>j</sub>_. For each _j_, we construct matrix _A<sub>j</sub>_ of dimension \(D_4\times C_j\) and matrix _B<sub>j</sub>_ of dimension \(C_j\times V\) where we ensure _B<sub>j</sub>_ is a monotone matrix by using the Euler tour distance matrix construction and the transformation `BDtoMonotone`. Filling in these matrices with the results computed by `BFS` from _C<sub>j</sub>_ on the graph (_V,F<sub>j</sub>_), we compute the correct distance estimate required in Section 5.2. Since overall the `BFS` require time \(\tilde{O}(n^2)\), the running time of (min,+) matrix multiplication dominates.

We have already discussed +6 approximation in Section 3.2.

For general \(+\beta\) approximation, let \(k=\frac{3\beta-2}{2}\) and \(k_0=k-\lfloor k/3\rfloor-2\). By Lemma A.3, if any path \(P\subset E_{k_0+1}\), then we already obtain a \(+\beta\)-approximation as in `SparseAPASP`. Then, to ensure a \(+\beta\) approximation for paths containing a higher degree vertex, we need to ensure that we have a +5 approximation after the (_k_<sub>0</sub>+3)-th iteration, we can follow the arguments of Lemma A.3 to obtain a \(+\beta\) additive approximation from this point.

We demonstrate this case in Figure 6. In this example, _a_ is a vertex on the shortest path _P_ between _u,v_ such that \(\ell(a)=k_0+3\). While the diagram only shows \(\hat{\delta}(a^*,v)\le\delta(a,v)+5\), a similar argument holds for all \(x\in P\).

Let _b_ be the vertex closest to _a_ such that \(P_{b,v}\subset E_{k_0+3}\). Let _z_ be the highest degree vertex in _P<sub>a,b</sub>_. Suppose \(\frac{n}{2^j}\le deg(z)<\frac{n}{2^{j-1}}\). Then, after computing the (min,+) product _A<sub>j</sub>∗B<sub>j</sub>_, we have an estimate<tbc>

\(\hat{\delta}(a^*,b^*)\le\delta(a,b)+4\)

<tbc>given by the blue arrows. In particular from _a_<sup>∗</sup>, the path \((a^*,b^*,b)\circ P_{b,v}\subset G_{k_0+3,a^*}\) so that

\(\hat{\delta}(a^*,v)\le\delta(a,v)+5\)

We next argue that our algorithm has an improved running time. Suppose we use naive matrix multiplication. Then, the time exponent to compute a `MonotoneMinPlus` combinatorially is,

We use a (min, +) product to replace the edge set D2xD4.
From z*, we compute 8(z*, v) 8(z, v) + 1 and 8(z*, y*) + 2
The (min, +) product yields 8(v, y*) 8(v, y) + 3
Then, (v, y*, y) P{y,u} C G{5,v} so 8(v, u) 8(v, u) + 4
y*
Z*
u
y
z
v
l(u) = 5
l(y) = 4
l(z) = 2
l(v) = 5

Figure 5: Using (min,+) product to replace edge set \(D_2\times D_4\). Solid lines represent eges in _G_. Dotted black lines represent paths in _G_. Dashed blue arrows represent distance estimates used in the (min,+) product. Dashed black arrows represent edges \(w\times V\) in the graph _G<sub>j,w</sub>_.

