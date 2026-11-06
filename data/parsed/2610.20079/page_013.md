The local spaces lift without increasing their difference ranks. At a round whose preceding coordinates form \(A=E^{\otimes(j-1)}\), let _L_ be their original tensor line, let \(K=L^\perp\subseteq A\), and let _Q_ be the tensor line of the unprocessed coordinates. An empty tensor product is Q. Lift a local subspace \(V\subseteq E\) to

\(\phi(V)=\left[(K\otimes E)\oplus(L\otimes V)\right]\otimes Q.\) (5)

The sum is orthogonal and dim_L_=dim_Q_=1, so inclusions and differences of dimensions are preserved. At entry the data spaces are \(A\otimes\ell_{a_j}\otimes Q\) and \(K\otimes\ell_{a_j}\otimes Q\). Raise them to \(\phi(\ell_{a_j})\) and \(\phi(0)\), respectively, then run the lifted local schedule. The output spaces are \(A\otimes E\otimes Q\) and its part orthogonal to _U<sub>a</sub>_. These are precisely the next round’s starting spaces. In the reverse middle round, _X_ is the updated target at \(\phi(\ell_{a_j})\), and _Y_ is the control at \(\phi(0)\); reversing which register is updated does not interchange the subspace labels assigned to those registers.

## Sharing auxiliary registers among three copies.

We use three independent data copies _C_<sub>1</sub>_,C_<sub>2</sub>_,C_<sub>3</sub>, with coordinate orders (1,2,3), (2,3,1), and (3,1,2). Execute all first rounds before any second round, and all second rounds before any third round. Indices on copy and coordinate names are cyclic modulo three.

For every \(i\in\{1,2,3\}\) and \(b,c\in[v]\), allocate one pool _P<sub>i</sub>(b,c_) of _R_ independent auxiliary registers. Its three uses are:

(1) Round one of _C<sub>i</sub>_: vary coordinate _i_, fixing coordinates _i_+1_,i_+2 at _b,c_.<tbc>

(2) Round two of _C_<sub>_i_+2</sub>: vary coordinate _i_, fixing coordinates _i_+1_,i_+2 at \(b,\pi(c)\).<tbc>

(3) Round three of _C_<sub>_i_+1</sub>: vary coordinate _i_, fixing coordinates _i_+1_,i_+2 at \(\pi(b),\pi(c)\).

These assignments are bijections on the local blocks of each round. Each pool is used once per round, and its local register number is unchanged. Since every invocation restores all auxiliary bit values, this reuse does not require an auxiliary register to start at zero.

The subspace labels of each auxiliary register continue to grow by inclusion across the three uses. Displaying tensor factors in order (_i,i_+1_,i_+2), the boundary chain is

\(0\subseteq E_i\otimes\ell_b\otimes\ell_c\subseteq E_i\otimes\ell_b\otimes\ell_{\pi(c)}^\perp\subseteq E_i\otimes\ell_b\otimes E_{i+2}\subseteq E_i\otimes(\ell_{\pi(b)}\otimes\ell_{\pi(c)})^\perp\subseteq\mathcal{H}.\text{(6)}\)

The nontrivial inclusions follow from \(\ell_c\perp\ell_{\pi(c)}\) and \(\ell_b\perp\ell_{\pi(b)}\). The dimensions are 0,8,56,64,504,512. Together with the nested paths inside each invocation, each auxiliary register’s label grows from the zero subspace to H. Its dimension increases sum to _m_, which is also the total projection-difference rank by (7).

**Lemma 5.2** (Permutation of the input bits)**.** The three-copy schedule exchanges the _X_ and _Y_ register collections in each copy and restores every auxiliary initial value. It has

\(W=6v^3+3v^2R=24,432,543\)

independent inputs. Temporary copies are not independent inputs or additional sessions.

_Proof._ The displayed three-round identity holds for every data pair in every copy. Each auxiliary pool is restored before its next use. There are 6_v_<sup>3</sup> data inputs and 3_v_<sup>2</sup>_R_ auxiliary inputs; their sum gives _W_.

