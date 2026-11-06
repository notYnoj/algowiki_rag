2. Otherwise, there exists _k_ with \(\alpha[k]=\beta[k]=1\). By Observation 3, \(C_2(\beta[k])=C_2(1)=\text{\texttt{222}}\) is not a CT-subsequence of \(C_1(\alpha[k])=C_1(1)=\text{\texttt{3323}}\).<tbc>

<tbc>For a Cartesian tree of a string, the path from the root to the rightmost node is called the _frontier_ of the tree. From the form of \(V_2(\beta)\), the frontier of \(CT(V_2(\beta))\) consists of (_d_+1) `1`’s and their left subtrees are of size three (see Fig. 5 for examples). We now prove Claim 1.<tbc>

<tbc>**Claim 1** _Assume that there is a subsequence S of_ \(V_1(\alpha)\) _that CT-matches_ \(V_2(\beta)\)_. The frontier of CT(S_) _consists only of character_ `1`.<tbc>

<tbc>_Proof_ Assume on the contrary that the frontier of _CT(S_) contains a character \(c\neq\text{\texttt{1}}\). By the definition of Cartesian trees, the left subtree of _c_ consists only of characters that are greater than _c_. Thus, _c_=`3` is invalid, so _c_=`2`. Further, the left subtree of `2` is _CT_(`333`) since the size of the left subtree is three. Since every coordinate gadget has at most two `3`’s, selecting `333` from \(V_1(\alpha)\) results in at least one `1` being _unavailable_ as an element of _S_. Also, the rightmost (lowest) frontier node of _CT(S_) is `2`, and thus, the rightmost `1` in \(V_1(\alpha)\) cannot be contained in _S_. Hence, there are at least _t_+1 unavailable `1`’s where _t_ is the number of `2`’s in the frontier of _CT(S_). Therefore, the number of available `1`’s is at most _d-t_ and the number of `1`’s in the frontier of _CT(S_) is _d_+1-_t_, a contradiction.

By Claim 1, each `1` in \(V_2(\beta)\) must be aligned to each `1` in \(V_1(\alpha)\). Thus, \(C_2(\beta[i])\) should be assigned to \(C_1(\alpha[i])\) for each \(1\le i\le d\). However, as mentioned before, \(C_2(\beta[k])\) is not a CT-subsequence of \(C_1(\alpha[k])\). Therefore, there is no subsequence _S_ of \(V_1(\alpha)\) that CT-matches \(V_2(\beta)\).

Now we construct text _T<sub>A</sub>_ and pattern _P<sub>B</sub>_, joining dummy vector gadget _V_<sub>1</sub>(**0**)=`1`(_C_<sub>1</sub>(0)`1`)_<sup>d</sup>_ where **0** denotes the _d_-dimensional zero vector:<tbc>

\(T_A=0\left(\prod_{i=1}^{n_A}\left(V_1(\alpha_i)0V_1(\text{\texttt{0}})0\right)\right)^2\)

B = (0, 1, 0, 0, 1)
V2(B) =
1
2
2
2
1
3
2
3
1
2
2
2
1
2
2
2
1
3
2
3
1
CT(V2(B)) :

**Fig. 5** Illustration for \(V_2(\beta)\) and \(CT(V_2(\beta))\) where \(\beta=(0,1,0,0,1)\). Since coordinate gadgets consist only of `2` and `3`, each coordinate gadget is the left subtree of some `1`, resulting in an unbalanced Cartesian tree. We call such a structure comb-like. Note that \(V_2(\beta)\) contains six `1`’s since _d_=`5` in this example.

