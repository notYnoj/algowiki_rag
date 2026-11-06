contribute _C_<sup>-</sup> edit distance (the 3 symbols match perfectly and thus have no contribution to the edit distance). So these give a contribution of 2_f(x(Q+v_)+_C_<sup>-</sup>). Finally, we have \(M=(d-1)n^\ell+1\) real gadgets which line up with other real gadgets and these contribute _xQ+C_<sup>-</sup> edit distance each. So our total edit distance is

\(C=zfk(k+5)/2+fp_{k-1}+\sum_{i=1}^{k-1}2fp_i+2f(x(Q+v)+C^-)+M(xQ+C^-).\)

What happens if we don’t have a set of \((k-1)\ell\) vectors which are orthogonal to _v_<sub>1</sub>_,...,v<sub>k</sub>_? If we similarly line up gadgets in a valid way, as above, then we have at least one of the real _k_-tuples of \(CGED'\) gadgets where the internal _CGED_ gadgets contribute _C_<sup>+</sup>, increasing the above cost by _C_<sup>+</sup>-_C_<sup>-</sup>. What if we instead don’t do a valid alignment? If we skip aligning a coordinate gadget we skip some 3_<sup>y</sup>_ symbols, these then cost an additional _y_ in the edit distance. If we instead align some of the _M_ real gadgets of string _k_ to fake gadgets we miss out on matches of the _SCSG_ gadgets, costing _xv_ in the edit distance. So if there is no set of \((k-1)\ell\) vectors which are orthogonal to _v_<sub>1</sub>_,...,v<sub>k</sub>_ then the edit distance is higher than _C_.

First, we can generate the SLP for _FAKE<sub>i</sub>_ and _UNMA<sub>i</sub>_. The size of _F<sub>i</sub>_ and %_<sub>i</sub>_ are both _O_(1) (assuming _k_ is a constant). So, we simply need to handle many repetitions. This requires an SLP of size lg(_f(k_+1-_i_)) and one of size lg((_i_+1)_zf_) for each \(i\in[1,k]\). Luckily for us, in total this SLP will have size \(O(\ell lg(n))\). We additionally need to represent the various values for _REAL<sub>i</sub>_. First note that \(CGED'_i\) gadgets can be represented with size _O_(1) SLPs (when _k_ is constant). For _REAL<sub>k</sub>_ this is easy from this point on. There are long strings of zero gadgets with only _d_ instances of non zeros. The total representation is \(O(d+\ell lg(n))\). So we just need _REAL<sub>i</sub>_ for \(i\in[1,k-1]\). Now note that we can use the same structure we used in the _k_-LCS SLP for these interleave gadgets. We can build the structures for different values of \(\ell\).

For convenience let \(REAL_i^\ell\) be the real gadget for \(IED'_i(L,\ell,v_i)\). Now note that \(REAL_i^1\) has an SLP of size _O(dn_) trivially, it only has length _O(dn_) in the first place. Now consider separating out the parts that correspond to each of the _d_ dimensions of the vector. Next note that we can form these _d_ parts of \(REAL_i^{j+1}\) by concatenating _n_ instances of the parts of either \(REAL_i^j\) or _n<sup>j</sup>_ zero coordinate gadgets. So, given an SLP for \(REAL_i^j\) we can create an SLP for \(REAL_i^{j+1}\) with an additional size of _n+j_lg(_n_). This gives a total size of \(O(\ell^2lg(n)+\ell dn)\), as \(\ell\) is a constant we have have that the size is _O(dn_).

So the total size of the SLP will be _O(dn+dx+lg(n_)).

Notice that we can get away without having the same type of $_<sub>i</sub>_ interleaved symbols that we used in _k_-LCS. This is due to the cost of edits varying even when only some subset of the _k_ strings match on a symbol. We can guarantee we don’t skip characters because it will cost us in edits, even if those characters could only be matched up to one other string. However, we aren’t quite done. We want to wrap this so that the value is either a match or one higher than a match. We don’t want to have the final interleave gadgets give variable outputs depending on how orthogonal vectors are. We want the same value no matter what.

**Lemma 6.26.** _We are given as input a list L of n vectors each of length d, where d=n_<sup>_o_(1)</sup>_. Let_ \(\ell\) _be a constant. Let v_<sub>1</sub>_,...,v<sub>k</sub> be_ {0,1} _vectors each of dimension d. Then there are gadgets IED<sub>i</sub>(L,v<sub>i</sub>_) _and EED(v<sub>k</sub>_) _such that for some constants D and w:_<tbc>

\(\delta_E(IED_1(L,\ell,v_1),\dots,IED_{k-1}(L,\ell,v_{k-1}),EED(v_k))=D\)

<tbc>_if there are_ \((k-1)\ell\) _vectors in L such that are orthogonal with v_<sub>1</sub>_,...,v<sub>k</sub>. If there do not exist_ \((k-1)\ell\) _vectors in L that are orthogonal with v_<sub>1</sub>_,...,v<sub>k</sub> then_

\(\delta_E(IED_1(L,\ell,v_1),\dots,IED_{k-1}(L,\ell,v_{k-1}),EED(v_k))=D+w.\)

_Additionally we can compress x strings_ \(IED_i(L,\ell,v_1),\dots,IED_i(L,\ell,v_x)\)<br>
_or EED(v_<sub>1</sub>)_,...,EED(v<sub>x</sub>_) _with a total compression size of O(xd+nd+x_lg(_n_)).

_The strings IED and EED have length_ \(n^{\ell+o(1)}\).

_Proof._ Let _u_ be an all zero vector of length _d_. Let \(v'_i\) be the vector _v<sub>i</sub>_ but with an added last index \(v'_i[d+1]=1\) if \(i\in[1,k]\). Let \(u'\) be the all zeros vector except for an added last index _u_\[_d_+1\]=0. Let \(v_k^*\)<tbc>

