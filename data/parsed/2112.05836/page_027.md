the full length of string representations of 0 and 1.

\(S_X=ZX[0]ZX[1]Z\dots ZX[m]Z\) (26)

\(S_{Y_i}=Z^{m-n}Y_i[0]ZY_i[1]Z\dots ZY_i[m]Z^{m-n}\) (27)

Now, if there is a sub-string of _X_ that is orthogonal to _Y_<sub>1</sub>_,...,Y_<sub>_k_-1</sub> then the optimal LCS will match all the _Z_s in _X_ and match each character _Y<sub>i</sub>_\[_j_\] with some character in _X_. If we spread out our matches of _Y<sub>i</sub>_ and don’t match to a sub-string of _X_ but instead to a subsequence, we will miss out on some _Z_ characters. So, if there isn’t a match that corresponds to an OV we will lose out. And this works with many strings at once.

This gadget is forcing not just any alignment of the underlying strings in _X_<sub>1</sub>_,...,X_<sub>_k_-1</sub>_,Y_ , but a _perfect_ alignment. We will use this structure to build a perfect alignment gadget.

## 6.5 Reduction

We will prove lemmas building up the gadgets for this construction. We will describe the details of our gadgets and reductions here. The intuition described above of both why we care about perfect alignment and how to achieve it is used in the next subsection on our alignment gadget.

### 6.5.1 Alignment Gadget

Now we will prove that the alignment gadget works as desired. First let us define what an alignment and perfect alignment are.

**Definition 6.9.** We will generalize the Structured Alignment Cost definition of previous work \[ABBK17\]. We are given as input _k_ lists of strings _X_<sub>1</sub>_,...,X_<sub>_k_-1</sub>_,Y_ . Where |_X<sub>i</sub>_|=_n_, |_Y_|=_m_, and _m\<n_.

An alignment, \(\Lambda\) is a list of _tk_-tuples:

\(((i_{1,1},i_{1,2},\dots,i_{1,k}),\dots,(i_{t,1},i_{t,2},\dots,i_{t,k}))\)

where \(i_{j,p}<i_{j^\prime,p}\) if \(j<j'\). We call an alignment perfect if _i<sub>j,p</sub>_+1=_i_<sub>_j_+1_,p_</sub> and _t=m_.

Now we will create some gadgets to maintain alignment. We will define them here and then below prove the various properties we care about.

**Definition 6.10** (Perfect Alignment Gadget)**.** We are given as input _k_ lists of strings _X_<sub>1</sub>_,...,X_<sub>_k_-1</sub>_,Y_ . Where |_X<sub>i</sub>_|=_n_, |_Y_|=_m_, and _m\<n_.

We will add _k_ new symbols $<sub>1</sub>_,...,_$_<sub>k</sub>_. We will define \(A=\$_1^{2\ell}\circ\dots\circ\$_k^{2\ell}\) where \(\circ\) is the concatenation operator. Let \(A_{-i}=\$_1^{2\ell}\circ\dots\circ\$_{i-1}^{2\ell}\circ\$_{i+1}^{2\ell}\circ\dots\circ\$_k^{2\ell}\). Note that this is just _A_ with all the $_<sub>i</sub>_ symbols removed. We also add a character % which we use to pad out our strings to give them more value. Let \(B=\%_0^{2\ell}\) (note that the % character is serving the purpose of the 5 character in our earlier example). We define _f=n-m_. Then the generalized structured alignment gadget would produce strings:

\(AG_i(X_i)=A_{-i}^f\circ A\circ X_i[1]\circ B\circ A\circ X_i[2]\circ B\circ\dots\circ A\circ X_i[n]\circ B\circ A_{-i}^f\) (28)

\(AG_y(Y)=A_{-k}^f\circ A\circ Y[1]\circ B\circ A\circ Y[2]\circ B\circ\dots\circ A\circ Y_m\circ B\circ A_{-k}^f\) (29)

We also want gadgets to be a selector around the alignment gadget. We add a new character @. We will leave _D_ unset for now. We define our _SAG_ gadgets:

\(SAG_i(X_i)=@^{D-1}AG_i(X_i)\)<br>
\(SAG_y(Y)=AG_y(Y)@^{D-1}.\)

We will now prove that these work as perfect alignment gadgets. This setup requires that we are trying to detect if there is a perfect alignment in which all strings match as much as they can.

**Theorem 6.11.** _We are given as input k lists of strings X_<sub>1</sub>_,...,X_<sub>_k_-1</sub>_,Y. Where_ |_X<sub>i</sub>_|=_n,_ |_Y_|=_m, and m\<n. Furthermore all strings_ \(S\in X_i\) _and_ \(S'\in Y\) _have length_ \(|S|=|S'|=\ell\).

_Additionally, given any set of k strings_ \(S_i\in X_i\) _and_ \(S_y\in Y\) _the LCS distance is either z or z_+1 _for some constant z._

_Let_ \(\Lambda\) _be a perfect alignment which is a list of m k-tuples:_ (_i_<sub>1,1</sub>_,i_<sub>1,2</sub>_,...,i_<sub>1_,k_</sub>)_. Where i<sub>j,h</sub>_+1=_i_<sub>_j_+1_,h_</sub>.<tbc>

