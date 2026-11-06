## Height Profile:

A _height profile_ \(\pi\) assigns, to every column \(C_i\in\mathcal{C}\), a value \(\pi(C_i)\in\{1,\dots,n,\infty\}\). Let \(\Pi\) be the set of all possible height profiles, so \(|\Pi|\le n^{O(n)}\). For a profile \(\pi\in\Pi\), we denote by \(M(\pi)\) the largest value of \(\pi(C_i)\) for any column \(C_i\in\mathcal{C}\) that is not \(\infty\). Given a height profile \(\pi\), let \(\mathcal{C}(\pi)\subseteq\mathcal{C}\) be the set of columns _C<sub>i</sub>_ with \(\pi(C_i)<\infty\), and let \(\mathcal{C}'(\pi)=\mathcal{C}\backslash\mathcal{C}(\pi)\). We can then naturally associate an ordering \(\rho_\pi\) of the columns in \(\mathcal{C}(\pi)\) with \(\pi\) as follows: for columns \(C_i,C_j\in\mathcal{C}(\pi)\), _C<sub>i</sub>_ appears before _C<sub>j</sub>_ in \(\pi\) iff either (i) \(\pi(C_i)<\pi(C_j)\); or (ii) \(\pi(C_i)=\pi(C_j)\) and _i\<j_.

Consider now any point set _Z_, where every point lies on a column of C. Let \(Z'=\mathrm{top}(Z)\), and let \(\sigma(Z)\) denote the ordering of the points in \(Z'\), such that _p_ appears before \(p'\) in \(\sigma\) iff either (i) \(p.y<p'.y\); or (ii) \(p.y=p'.y\) and \(p.x<p'.x\). Consider now any profile \(\pi\in\Pi\). We say that point set _Z_ is _consistent with profile_ \(\pi\) (see Figure 8 for an illustration) iff the following hold:

• For every column \(C_i\in\mathcal{C}\), if \(\pi(C_i)=\infty\), then no point of _Z_ lies on _C<sub>i</sub>_; and<tbc>

• For all \(1\le i\le|Z'|\), the _i_th point in \(\sigma(Z)\) lies on the _i_th column of \(\rho_\pi\).

## Dynamic Programming .

Consider some integer \(1\le t\le m\) and some height profile \(\pi\); recall that \(M(\pi)\) is the largest value of \(\pi(C_j)\) for \(C_j\in\mathcal{C}\) that is not \(\infty\). We say that \(\pi\) is a _legal profile_ for _t_ iff \(M(\pi)\le t\), and, if _C<sub>i</sub>_ is the column containing the input point _p<sub>t</sub>_, then \(\pi(C_i)=M(\pi)\) (that is, column _C<sub>i</sub>_ has the largest value \(\pi(C_i)\) that is not \(\infty\); we note that it is possible that other columns \(C_j\neq C_i\) also have \(\pi(C_j)=M(\pi)\)).

For every integer \(1\le t\le m\), and every height profile \(\pi\) that is legal for _t_, there is an entry \(T[t,\pi]\) in the dynamic programming table. The entry is supposed to store the minimum-cardinality set _Z_ of points with the following properties:

• \(X_{\le t}\subseteq Z\);<tbc>

• all points of _Z_ lie on rows _R_<sub>1</sub>_,...,R<sub>t</sub>_;<tbc>

• _Z_ is a satisfied point set; and<tbc>

1
2
3
4
5

Figure 8: An illustration of height profile that is consistent with a set _Z_ of points. The set top(_Z_) is shown by dark points. The height profile is \(\pi(C_1)=1,\pi(C_2)=\pi(C_5)=2\) and \(\pi(C_3)=h_Z(C_4)=3\).

