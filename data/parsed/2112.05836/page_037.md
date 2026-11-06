_some constant Q if all characters match or Q+v (where v is a positive integer) if one character does not match._

_Proof._ First let us define the gadget in terms of two free variables we will set later, _a_ and _b_:<tbc>

\(SCSG_i(c)=\#^{ib}c^a\#^{(k-1-i)b}\)

<tbc>Now note that if we match the characters _c_ together we must fail to match many # characters. Specifically these induce an edit distance of:

\(\left\{\begin{array}{ c c }
bk^2/4 & \text{if}k\text{is even} \\
b(k^2-1)/4 & \text{if}k\text{is odd}
\end{array}\right.\)

Now note that if we instead match the # characters then we have an edit distance of _ak_, as we have to delete the characters input to the gadget.

Also note that if we match the characters _c_ and one or more symbols are off the edit distance will be **at least**:

\(\left\{\begin{array}{ c c }
bk^2/4+a & \text{if}k\text{is even} \\
b(k^2-1)/4+a & \text{if}k\text{is odd}
\end{array}\right.\)

So if we can choose an _a_ and _b_ such that:

\(\left\{\begin{array}{ c c }
bk^2/4<ak\le bk^2/4+a & \text{if}k\text{is even} \\
b(k^2-1)/4<ak\le b(k^2-1)/4+a & \text{if}k\text{is odd}
\end{array}\right.\)

then, if all characters match we get an edit distance of _bk_<sup>2</sup>/4, otherwise, we get an edit distance of _ak_.

Next we will note the existence of coordinate gadgets from previous work. Then we will combine the coordinate gadgets with our selector gadgets to make interleave gadgets.

## 6.11 Coordinate Gadgets

We will use the coordinate gadgets from the \[HBGT20\] in our reduction.

**Lemma 6.24** (Coordinate Gadget Lemma From \[HBGT20\])**.** _Let b_<sub>1</sub>_,...,b<sub>k</sub> be in_ {0,1}_. Let C_<sup>-</sup>=2(_k_-1)<sup>2</sup> _and let C_<sup>+</sup>=_C_<sup>-</sup>+_k_-1=(2_k_-1)(_k_-1)_. Then,_

\(\delta_E(CGED_1(b_1),\dots,CGED_k(b_k))=\left\{\begin{array}{ c c }
C^- & \text{\textit{if}}b_1\cdots b_k=0 \\
C^+ & \text{\textit{otherwise}}
\end{array}\right.\)

We will use these inside our interleave vector gadgets.

## 6.12 Interleave Vector Gadget

We are given a (_a(k_-1)+_bk_)-OV with a list of _n_ vectors each of length _d_. We want to take every vector _v<sub>j</sub>_=**List**(_L)<sub>b</sub>_\[_j_\] for \(j\in[0,n^b]\) and combine them with the interleave representation of _a_ lists. Recall that in Definition 6.8 we define **VecS**<sub>**I**<sub>_a_</sub></sub>(_L,v<sub>j</sub>_) as the explicit distribution of the interleave representation of _a_ lists mixed with a single vector. So, we want to have _k_-1 strings that hold representations of **VecS**<sub>**I**<sub>_a_</sub></sub>(_L,v<sub>j</sub>_) for all \(j\in[0,n^b]\). Finally, we need one string that is full of representations of vectors _v<sub>j</sub>_ for all \(j\in[0,n^b]\), padded with many zeros. If we do this and we can force a perfect alignment of these gadgets. We will use an altered version of the sliding pyramids from previous work \[HBGT20\] (see Figure 1).

**Lemma 6.25.** _Treat_ \(k,\ell\) _as constants. We are given as input a list L of n vectors each of length d. Where d=n_<sup>_o_(1)</sup>_. Let v_<sub>1</sub>_,...,v<sub>k</sub> be_ {0,1} _vectors each of dimension d. Then there are gadgets_ \(IED'_i(L,v_i)\) _and_ \(EED'(v_k)\) _such that:_<tbc>

\(\delta_E(IED'_1(L,\ell,v_1),\dots,IED'_{k-1}(L,\ell,v_{k-1}),EED'(v_k))=C\)

<tbc>_if there are_ \((k-1)\ell\) _vectors in L such that are orthogonal with v_<sub>1</sub>_,...,v<sub>k</sub>. If there do not exist_ \((k-1)\ell\) _vectors in L that are orthogonal with v_<sub>1</sub>_,...,v<sub>k</sub> then_

\(\delta_E(IED'_1(L,\ell,v_1),\dots,IED'_{k-1}(L,\ell,v_{k-1}),EED'(v_k))\ge C+1.\)

_Additionally we can compress x strings_ \(IED'_i(L,\ell,v_1),\dots,IED'_i(L,\ell,v_x)\)<br>
_or_ \(EED'(v_1),\dots,EED'(v_x)\) _with a total compression size of O(xd+nd_+lg(_n_)).

