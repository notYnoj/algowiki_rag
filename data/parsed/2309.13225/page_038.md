\(\left(1-\frac{\beta-2}{\beta+2}x\right)+(1-x)+\left(1-\frac{\beta-4}{\beta+2}x\right)=3-\frac{3\beta-4}{\beta+2}\cdot x\)

<tbc>Then, balancing this with the \(2+\frac{2x}{\beta+2}\) exponent required to execute `SparseAPASP`,<tbc>

\(3-\frac{3\beta-4}{\beta+2}\cdot x=2+\frac{2x}{\beta+2}\)

<tbc>so that,

\(x=\frac{\beta+2}{3\beta-2}\)

and obtain running time exponent \(2+\frac{2}{\beta+2}\frac{\beta+2}{3\beta-2}=2+\frac{2}{3\beta-2}\), thus recovering the approximation algorithm of Dor, Halperin, and Zwick \[DHZ00\]. In particular, by using fast matrix multiplication instead, we obtain a faster running time for all values of \(\beta\).

## Algorithm

We are now ready to describe our algorithm. We begin our algorithm by initializing the distance estimate matrix as the adjacency matrix of the graph _G_, as well as setting parameters _x,k_. Then, we decompose our graph into \(\lfloor k/3\rfloor+3\) levels according to the degree thresholds _s_<sub>_k_<sub>0</sub></sub>_,s_<sub>_k_<sub>0</sub>+1</sub>_,...,s_<sub>_k_-1</sub>.

In Phase 1, we further decompose the top level into roughly (1-_x_)log_n_ levels. At each level, we execute `BFS` from every vertex _w_ in the dominating set _C<sub>i</sub>_ on the graph (_V,F<sub>i</sub>_). We construct two matrices _A<sub>i</sub>,B<sub>i</sub>_ encoding the computed distances between _D_<sub>_k_<sub>0</sub>+2</sub>_,C<sub>i</sub>_ and _C<sub>i</sub>,D_<sub>_k_<sub>0</sub>+3</sub> respectively.

In order to apply the `MonotoneMinPlus` algorithm of \[CDXZ22\], we define \(B'_i\) to be the Euler tour distance matrix of _C<sub>i</sub>_ on _G<sub>i</sub>_ (see Definition 5.8) observing that this is a row-bounded difference matrix. Then, we modify this matrix into a row-monotone matrix by adding _j_ to each column _j_ and taking a sub-matrix of the columns corresponding to _D_<sub>_k_<sub>0</sub>+3</sub> to obtain a monotone matrix, as discussed in Section B.2. In the pseudocode, this is contained in the invocation of `BDtoMonotone`. Then, we compute the (min,+) product of _A<sub>i</sub>,B<sub>i</sub>_ using `MonotoneMinPlus`.

In Phase 2, we execute `Dijkstra` from each _D<sub>i</sub>_ for \(i\ge k_0+1\). In each iteration, we search the graph _G<sub>j,w</sub>_ consisting of \(E_j\cup E^*\cup(w\times V)\).

We now present the algorithm and proof of Theorem 5.6.

a*
Z*
b*
u
a
Z
b
v

Figure 6: Computing a distance estimate between _u,v_. Solid black lines denote edges in _G_. Dotted black lines represent paths in _G_. Blue dashed arrows denote distance estimates used in the (min,+) product (Phase 1). Black dashed arrows denote edges \(w\times V\) in the graph _G<sub>j,w</sub>_ (Phase 2).

