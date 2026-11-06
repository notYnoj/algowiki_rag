<tbc>bishop this number is known, obtained from Theorem I.5.8). We consequently take the point of view that bishops formulas, like those for other pieces, call for a quasipolynomial analysis via Ehrhart theory, so there is room for further work.

## 4.2. The semibishop.

We now come to the third piece known to have period 1. The _semibishop_ Q<sup>01</sup> has just one of the bishop’s moves, say (_c,d_)=(1,1). Thus, it is an example of a one-move rider (Section II.6). As such it has counting functions

\(u_{\mathbb{Q}^{01}}(1;n)=n^2,\)<br>
\(u_{\mathbb{Q}^{01}}(2;n)=\frac{1}{2}n^4-\frac{1}{3}n^3-\frac{1}{6}n,\)<br>
\(u_{\mathbb{Q}^{01}}(3;n)=\frac{1}{6}n^6-\frac{1}{3}n^5+\frac{1}{6}n^4-\frac{1}{6}n^3+\frac{1}{6}n^2,\)<br>
\(u_{\mathbb{Q}^{01}}(4;n)=\frac{1}{24}n^8-\frac{1}{6}n^7+\frac{2}{9}n^6-\frac{11}{60}n^5+\frac{2}{9}n^4-\frac{1}{6}n^3+\frac{1}{72}n^2+\frac{1}{60}n,\)

from Proposition II.6.1 (in which \(\bar{n}=0\)). All of these are polynomials in _n_.

**Theorem 4.3.** _The counting function for nonattacking unlabelled semibishops on the square board is_

\(u_{\mathbb{Q}^{01}}(q;n)=(-1)^q\sum_{k=0}^qs(n+1,n+1-k)s(n,n-(q-k)),\)

_which is a polynomial function of n of degree_ 2_q._

_Proof._ This is an immediate consequence of Proposition 4.4 below. Alternatively, it can be proved similarly to that proposition. □

Explicit formulas for the coefficients \(\gamma_i\) for \(i\le 3\) are in Theorem III.3.1 and s III.3.1 and III.3.2.

Kotˇcešovec independently proposed this same formula in [12, fourth ed., p. 155; sixth ed., p. 265] and verified it for \(n\le 20\) and some values of _q_, without a proof.

We prepare for the proof of Theorem 4.3 by changing the board. The _right triangle board_ (_triangular board_ for short) has legs parallel to the axes and hypotenuse in the direction of the semibishop’s move; thus, it is the set \(\EuScript{T}:=\{(x,y)\in\mathbb{R}^2:0\le x\le y\le 1\}\). The \(n\times n\) _triangular board_ is the set of integral points in the interior of the dilation by _n_+2, i.e.,

\((n+2)\EuScript{T}^\circ\cap\mathbb{Z}^2=\{(x,y)\in\mathbb{Z}^2:1\le x\le y-1\le n\}.\)

Write \(u_{\mathbb{Q}^{01}}^\EuScript{T}(q;n)\) for the counting function of nonattacking placements of _q_ unlabelled semibish ops on an \(n\times n\) triangular board. Most of our theory for the square board applies equally well to the triangular board; we omit details.

**Proposition 4.4.** _The counting function for nonattacking unlabelled semibishops on the triangular board is_ \(u_{\mathbb{Q}^{01}}^\EuScript{T}(q;n)=(-1)^qs(n+1,n+1-q)\).

**Proposition 4.5.** _The Stirling number of the first kind, s(n_+1_,n_+1-_q), is a polynomial function of n of degree q. The coefficient of n_<sup>2_q-i_</sup> _in q_!(-1)_<sup>q</sup>s(n_+1_,n_+1-_q_) _is a polynomial function of q of degree_ 2_i._

