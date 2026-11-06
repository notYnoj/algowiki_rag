### Encoding.

Compress this array one variable at a time, in the order _z_<sub>1</sub>_,...,z_<sub>2_d_</sub>. For _d_=1, write _x=z_<sub>1</sub> and _y=z_<sub>2</sub>. Write the inputs as _B<sub>i,j</sub>(x,y_), where _i_ labels a primal output and _j_ a dual output. Fix _j_, and expand \(B_{i,j}(x,y)=\sum_vB_{i,j,v}(x)y^v\). For each _v_, apply the primal encoder to the _c_+2 polynomials _B_<sub>1_,j,v_</sub>(_x),...,B_<sub>_c_+2_,j,v_</sub>(_x_). If the results are _U_<sub>1_,j,v_</sub>(_x),...,U_<sub>_c,j,v_</sub>(_x_), reassemble \(U_{r,j}(x,y)=\sum_vU_{r,j,v}(x)y^v\). Then expand each _U<sub>r,j</sub>_ in powers of _x_, apply the dual encoder to its lists of _y_-polynomials, and reassemble again.

For more variables, use their monomials in place of _y<sup>v</sup>_ in this same operation. At step _k_, denote the resulting list by **B**<sup>(_k_)</sup>, with **B**<sup>(0)</sup> the original array. Each step replaces one list index of size _c_+2 by one of size _c_. A processed variable has length _b+t_ if it is among the first _d_, and _s+t_ if it is among the last _d_. All other length bounds remain unchanged: they depend only on their own list indices, which are fixed while the current encoder runs. Thus every subsequent encoder receives lists with exactly the lengths required by its univariate packing. After 2_d_ steps there are _u_ right inputs, all in the domain of \(F_{a,b+t}^{(d)}\).

### Computation and decoding.

For two variables, let _E<sub>x</sub>,E<sub>y</sub>_ be the primal and dual encoders, and _D<sub>x</sub>,D<sub>y</sub>_ their decoders. Let _S_ denote the list of _c_<sup>2</sup> source products, and let _F<sub>i,j</sub>_ request the Full/Mid ranges specified by position (_i,j_). Lemma 2.3 combines the two univariate correctness identities to give

\([D_x(D_y(S(A,E_y(E_x(\mathbf{B}))))]_{i,j}\equiv F_{i,j}(A,B_{i,j})(\mathrm{mod}\varepsilon).\)

Thus encoding in _x_ and then _y_, computing the source products, and decoding in reverse order recovers the requested product at each position.

For 2_d_ variables, apply the same argument successively. Writing _E<sub>k</sub>,D<sub>k</sub>_ for the maps of step _k_, set

\(E=E_{2d}\circ\cdots\circ E_1,D=D_1\circ\cdots\circ D_{2d}.\)

Now let _S_ denote the list of _u_ source products. Compute _S(A,E_(**B**)) and apply _D_. Every requested output is recovered modulo \(\varepsilon\).

### Counting targets of the common shape.

Each recovered output is indexed by one word. Its Full set _I_ consists of the positions occupied by Full letters. Thus the outputs with |_I_|=_d_ correspond exactly to the words counted in Lemma 2.6, which gives at least (_c_+2)<sup>2_d_</sup>/(_d_+1) such outputs. Order each alphabet as displayed in that lemma, enumerate these words in lexicographic order, and keep the first _w_. Their Full sets are _I_<sub>1</sub>_,...,I<sub>w</sub>_; different words may have the same Full set. Put the prescribed _B<sub>i</sub>_ in these positions and zero in all other positions, then return the corresponding decoded outputs. The enumeration depends only on _c,d_.

The source Full set is always _I_<sub>0</sub>, but the target Full sets _I<sub>i</sub>_ may differ. Renaming a target into canonical form would also rename _A_. We therefore separate the left inputs before making these individual changes of variables.

## 2.4 Independent left inputs and a common target

We next give each target its own left input. We encode all left inputs in one univariate polynomial and each group of right inputs in its own univariate polynomial. The right inputs in group _i_ are encoded at the points \(i+\varepsilon j\). At each of these points, the left polynomial evaluates to _A<sub>i</sub>_ modulo \(\varepsilon\). This lets one interpolated product recover the entire group modulo \(\varepsilon\). Each target right input<tbc>

