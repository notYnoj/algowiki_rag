## 6.5.4 Putting it all Together

Now that we have an interleave gadget, we want to put many of these gadgets one after each other. However, we want to line up these gadgets. So, we put our interleave gadgets into the perfect alignment gadget.

**Lemma 6.15.** _Let a,b, and k be positive constant integers. Let L be a list of n vectors of length d=n_<sup>_o_(1)</sup>_. There are k strings GOV<sub>i</sub>(a,b,k,L_) _such that:_

\(\mathrm{LCS}(GOV_1(a,b,k,L),\dots,GOV_k(a,b,k,L))=\left\{\begin{array}{ c c }
D & \text{\textit{if there is a}}(bk+a(k-1))\text{\textit{-OV in}}L \\
D-1 & \text{\textit{else}}
\end{array}\right.\)

_The length of each of these strings is O(n_<sup>_a+b+o_(1)</sup>) _with an alphabet of size O(k)._

_Proof._ Unique (_bk+a(k_-1))-OV is equivalent to the normal detection problem of (_bk+a(k_-1))-OV, via a randomized reduction \[folklore\]\[Vas18\]. So, we can consider the case where a single (_bk+a(k_-1))-tuple of vectors are orthogonal.

Let _L<sub>b</sub>_=**List**(_L)<sub>b</sub>_ as defined in Definition 6.6. Now we will use these to define lists of vectors. For all \(i\in[1,k-1]\) let<tbc>

\(X_i[j]=IVG_i(L,a,L_b[j]),\)<br>
\(Y[j]=EIVG(L_b[j]).\)

<tbc>So all _X<sub>i</sub>_ and _Y_ have length _n<sup>b</sup>_. The strings inside the gadgets is _n_<sup>_a+o_(1)</sup>. All _k_-tuples of these strings have LCS values of either _C_ or _C_-1. We basically want to wrap an alignment gadget around these strings. However, we want to allow any _k_-tuple to be compared so we will double all the _X<sub>i</sub>_ lists:<tbc>

\(\hat{X}_i[j]=\hat{X}_i[j+n^b]=X_i[j].\)

<tbc>Now, for any _k_ tuple _j_<sub>1</sub>_,...,j<sub>k</sub>_ where \(j_i\in[0,n^b-1]\) there is some offset \(\Delta_i\in[0,n^b-1]\) for all \(\hat{X}_i\) such that \(j_k=j_1+\Delta_i\mathrm{mod}n^b\). So, we can align the \(\hat{X}_i\) strings with _Y_ and get any _k_-tuple lined up. So, we can now build our gadgets. For all \(i\in[1,k-1]\):

\(GOV_i(a,b,k,L)=SAG_i(\hat{X}_i)\) (30)

\(GOV_k(a,b,k,L)=SAG_y(Y)\) (31)

Now, if there is a single (_bk+a(k_-1))-OV in our unique OV instance then there is a single _k_-tuple _X_<sub>1</sub>\[_j_<sub>1</sub>\]_,...,Y_\[_j<sub>k</sub>_\] of strings that have a LCS of _C_. Otherwise, they will all have a LCS of _C_-1. By Theorem 6.12 we have that in the first case where an (_bk+a(k_-1))-OV exists<tbc>

\(\mathrm{LCS}(GOV_1(a,b,k,L),\dots,GOV_k(a,b,k,L))=D\)

<tbc>otherwise

\(\mathrm{LCS}(GOV_1(a,b,k,L),\dots,GOV_k(a,b,k,L))=D-1.\)

Note that having only two possible LCS values hinges crucially on using a unique (_bk+a(k_-1))-OV instance.

The total size of the alphabet is _O(k_) for the interleaves and another _O(k_) for the _SAG_ gadgets, with a total alphabet size of _O(k_).

The total length of the _IVG_ gadgets is _n_<sup>_a+o_(1)</sup>. We have _n<sup>b</sup>_ copies of these gadgets. Giving a total length of _n_<sup>_a+b+o_(1)</sup>.

We will now bound the size of the compressed length of these gadgets.

**Lemma 6.16.** _Let k be a constant integer and let d=n_<sup>_o_(1)</sup>_. Given the k strings GOV<sub>i</sub>(a,b,k,L_) _defined in Lemma 6.15 the size of the compression is O(n_<sup>_b+o_(1)</sup>+_n_<sup>1+_o_(1)</sup>).

_Proof._ We will start by describing the compression size of _CG<sub>i</sub>_(0)_,CG<sub>i</sub>_(1). These strings have length _O_(1), thus the total size of the compression is at most _O_(1). There are 2_k_ of these strings and _k_ is a constant. So we can have 2_k_ variables, one for each string and still the total size of the compression will be _O_(1).

Next, we need to analyze the size of the compression of the _kn<sup>b</sup>_ interleave gadgets \(IVG_i(L,\ell,v_i)\). These include the zero and one bit representations, and then are wrapped in a perfect alignment gadget.<tbc>

