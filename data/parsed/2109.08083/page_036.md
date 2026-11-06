<tbc>(0,1,3)_<sub>i</sub>_ or (0,0,4)_<sub>i</sub>_ for some _i_. Given that we are considering configurations containing _e_ with negative sign, we have that if _e_ is of type (0,1,3)_<sub>i</sub>_, the vertex \(v\in e\) such that \(v\in J_i\backslash K_i\) must also lie precisely in an _i_-bad edge of positive sign (as opposed to an edge of type (0,1,3)_<sub>i</sub>_ or any other type). So in either case exactly one vertex \(v\in e\) will also be in a bad edge of positive sign in any _i_-legal zero-sum configuration containing _e_ with negative sign. Since \(v\in I_{t_1}\backslash K_i\), in order to ensure the bad edge \(e'\) contains a vertex in _K<sub>i</sub>_ one degree of freedom can take at most _O(k<sub>i</sub>_) values. Once such a pair \(e,e'\) is fixed, in order that the vertex \(v'\in e'\cap K_i\) lies in a (positive) edge of type \((\alpha,\beta,0)_i\), as required to dictate an _i_-legal zero-sum configuration for _e_, there are at most _O(j<sub>i</sub>_) possibilities. This gives a total of _O(j<sub>i</sub>k<sub>i</sub>_) _i_-legal zero-sum configurations containing such an edge _e_ of negative sign.

It remains to consider the lower bound in the cases where _e_ is either a bad edge of positive sign or an edge of type \((\alpha,\beta,0)\) of negative sign, where \(\alpha\neq 0\). We show the lower bounds are satisfied by giving specific possibilities for the degrees of freedom in each case. In particular, given _e_ is fixed, we list sufficiently many pairs which each dictate a distinct _i_-legal zero-sum configuration for _e_ as follows:

(1) if _e_=(_a,b+s,a+b+s,a-b-s_) is bad and _a_ is small and _b+s_ is positive with \(b+s\le\frac{t_1}{2}\) or negative with \(|b+s|\ge\frac{t_1}{2}\) , then pairs (_c,s_) with \(c\in[\frac{t_1}{12},\frac{t_1}{10}]\) and \(s\in[-c-\frac{j_i}{2},-c+\frac{j_i}{2}]\) ‘work’ (i.e. dictate an _i_-legal zero-sum configuration containing _e_),<tbc>

(2) if _e_=(_a,b+s,a+b+s,a-b-s_) is bad and _a_ is small and _b+s_ is positive with \(b+s\ge\frac{t_1}{4}\) or negative with \(|b+s|\le\frac{t_1}{4}\) , then pairs (_c,s_) with \(c\in[-\frac{t_1}{10},-\frac{t_1}{12}]\) and \(s\in[-c-\frac{j_i}{2},-c+\frac{j_i}{2}]\) work.<tbc>

(3) Similarly, if _e_=(_a,b+s,a+b+s,a-b-s_) is bad, _a+b+s_ is small and _a_ is positive with \(a\le\frac{t_1}{4}\) or negative with \(|a|\ge\frac{t_1}{4}\) , then pairs (_c,s_) with \(c\in[2a+\frac{t_1}{12},2a+\frac{t_1}{10}]\) and \(s\in[-a-\frac{j_i}{10},-a+\frac{j_i}{10}]\) work, and<tbc>

(4) if _e_=(_a,b+s,a+b+s,a-b-s_) is bad, _a+b+s_ is small and _a_ is positive with \(a\ge\frac{t_1}{4}\) or negative with \(|a|\le\frac{t_1}{4}\) , then pairs (_c,s_) with \(c\in[-2a+\frac{t_1}{12},-2a+\frac{t_1}{10}]\) and \(s\in[-a-\frac{j_i}{10},-a+\frac{j_i}{10}]\) work.<tbc>

(5) Finally, if _e_=(_a,c+s,a+c+s,a-c-s_) is of type \((\alpha,\beta,0)\) with \(\alpha\neq 0\), then pairs (_b,s_) with \(b\in[\frac{t_1}{8},\frac{t_1}{6}]\) and \(s\in[\frac{t_1}{12},\frac{t_1}{10}]\) work.

By symmetry between _X_ and _Y_ , and between _X+Y_ and _X-Y_ , this covers all cases. □

We shall wish to check that the properties of zero-sum configurations as listed in Fact 3.24 remain closely related (in a quasi-random sense) to their values in T as we run the random greedy edge removal process. More details of this will be covered in Chapter 5.

## 3.4. Degree-type conditions

As usual we shall write _d<sub>G</sub>(v_) for the number of edges containing _v_ in _G_, also known as the _degree of v in G_. For a weight function _w_ defined on _E(G_), we shall also write \(d_{w,G}(v):=\sum_{e\unknown v,e\in G}w(e)\) and refer to this as the _weighted degree of v in G_.

Our proof strategy relies on the fact that throughout the random greedy edge removal process and the iterative matching process, the subgraphs we obtain continue to have quasi-random properties. The precise nature of the structure that

