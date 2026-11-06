and output subspaces are

and all registers incident to an XOR gate have the same subspace there. There are nine additional copy episodes. Each starts with an intermediate XOR sum retained in a register at a seven- dimensional subspace. It copies that value, changes the copy’s subspace label to zero, XORs the copy into specified target registers at subspace zero, and discards the copy. The retained original is unchanged during that episode. The sum of the nine dimension decreases is \(c=9\cdot 7=63\); equation (7) below identifies each decrease with the rank of the corresponding projection difference.

There is also a permutation \(\pi\) of \[_v_\] satisfying \(\ell_t\perp\ell_{\pi(t)}\) for every _t_.

_Proof._ The properties of this finite circuit are verified by exact algebraic computation. Represent the initial bit in register _r_ by a distinct formal basis vector _e<sub>r</sub>_ over F<sub>2</sub>, and apply the circuit’s XOR updates to these vectors. The resulting expressions are _e<sub>x<sub>t</sub></sub>_, _e<sub>y<sub>t</sub></sub>+e<sub>x<sub>t</sub></sub>_, and _e<sub>z<sub>r</sub></sub>_. By linearity, the circuit therefore maps every input to (_x,y+x,z_), including arbitrary initial values of the auxiliary registers.

Exact rational row reduction verifies the subspace inclusions, the input and output labels in the table, and equality of the labels at each gate. Each retained XOR sum has a seven-dimensional label, so the nine copy operations contribute a total dimension decrease of \(9\cdot 7=63\). Each final target space is seven-dimensional and orthogonal to its associated line, hence equals \(\ell_t^\perp\). Finally, the pairing \(\pi\) uses each index once, and the dot product of every paired pair of spanning vectors is zero. This gives the required orthogonal permutation.

## The reverse invocation.

Reverse the XOR schedule, exchange the names _x,y_, and replace every local space _U_ by \(U^\perp\). The action on the register bits is then \((x,y,z)\mapsto(x+y,y,z)\), with the same input and output subspace labels as in Lemma 5.1. Reversal changes an inclusion into a reverse inclusion; taking complements changes it back. A copy episode is inverted by copying the same unchanged XOR sum again and undoing its additions to the target registers. The discarded copy is recreated from the retained value. If _U_ is the original seven-dimensional subspace, the new copy’s label changes from \(U^\perp\) to _E_, a dimension increase of dim_U_=7. Thus both invocations have the same additional cost _c_.

## Three tensor rounds.

Put \(\mathcal{H}=E_1\otimes E_2\otimes E_3\), where each _E<sub>i</sub>_ is a copy of _E_. This tensor product has a basis indexed by triples of basis vectors of _E_, so _m_=dimH=8<sup>3</sup>=512. Tensor products are used to construct the labels; each circuit register still stores one bit. For \(a=(a_1,a_2,a_3)\in[v]^3\), set<tbc>

\(U_a=\ell_{a_1}\otimes\ell_{a_2}\otimes\ell_{a_3}.\)

<tbc>First consider two collections of registers \((X_a)_{a\in[v]^3}\) and \((Y_a)_{a\in[v]^3}\). In rounds 1,2,3, vary the first, second, and third coordinate, respectively, fixing the other two within each local invocation. Use the forward, reverse, and forward schedule, in that order. Each round contains _v_<sup>2</sup> local invocations, and the register values change as follows<tbc>

\((X,Y)\longmapsto(X,Y+X)\longmapsto(Y,Y+X)\longmapsto(Y,X).\)

\begin{tabular}{ccc}
register & input & output \\
_x<sub>t</sub>_ & \(\ell_t\) & _E_ \\
_y<sub>t</sub>_ & 0 & \(\ell_t^\perp\) \\
_z<sub>r</sub>_ & 0 & _E_ \\
\end{tabular}

