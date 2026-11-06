_Proof._ Fix an algorithm A for OracleNoisyBinarySearch(_n_). WLOG, we can assume that A exits as soon as it sees a query that returns _P_ or _S_, i.e., it sees at most one such query result. Also, we assume \(\delta\le 1-\Omega(1)\), as otherwise the lower bound is trivially 0.

Let \(X\in\{0,\dots,n\}\) be the index of the true predecessor of _x_. Let _m_ be the (random) number of queries made. Let _Q<sup>m</sup>_ be the queries made. Let _Y<sup>m</sup>_ be the returned values of the queries. Let \(\hat{X}\) be the most probable _X_ given all query results. Note that \(\hat{X}\) is a function of (_Q<sup>m</sup>,Y<sup>m</sup>_).

Clearly, _H(X_)=log(_n_+1). By Fano’s inequality, \(H(X|\hat{X})\le 1+\delta log(n)\). Thus,<tbc>

\(I(X;Q^m,Y^m)\ge I(X;\hat{X})=H(X)-H(X|\hat{X})\ge(1-\delta-o(1))logn.\)

<tbc>On the other hand, we also have

\(I(X;Q^m,Y^m)\le\sum_{i\ge 1}\mathbb{P}[m\ge i]\left(H(Y_i|m\ge i)-H(Y_i|X,Q_i,m\ge i)\right)\)

using the same inequalities in the proof of Lemma 27.

Let \(q_i=\mathbb{P}[Y_i=P|m\ge i]\) and \(r_i=\mathbb{P}[Y_i=S|m\ge i]\). Because A exits as soon as it sees _P_ or _S_ we have<tbc>

\(\sum_{i\ge 1}\mathbb{P}[m\ge i](q_i+r_i)\le 1.\)

<tbc>Then<tbc>

\(H(Y_i|m\ge i)\le h\left(q_i,r_i,\frac{1-q_i-r_i}{2},\frac{1-q_i-r_i}{2}\right)\le h\left(\frac{q_i+r_i}{2},\frac{q_i+r_i}{2},\frac{1-q_i-r_i}{2},\frac{1-q_i-r_i}{2}\right)\)

<tbc>and

\(H(Y_i|X,Q_i,m\ge i)=0\cdot(q_i+r_i)+h(p)(1-q_i-r_i).\)

Note that \(H(Y_i|m\ge i)\le 2\) trivially, so \(I(X;Q^m,Y^m)\le 2\sum_{i\ge 1}\mathbb{P}[m\ge i]=2\mathbb{E}[m]\). Combining with \(I(X;Q^m,Y^m)\ge(1-\delta-o(1))logn\), we have \(\mathbb{E}[m]=\Omega(logn)\) (as we can assume \(\delta\le 1-\Omega(1))\).

Note that \(g(x):=h(\frac{x}{2},\frac{x}{2},\frac{1-x}{2},\frac{1-x}{2})\) is concave in _x_, so

\(\sum_{i\ge 1}\mathbb{P}[m\ge i]H(Y_i|m\ge i)\le\left(\sum_{i\ge 1}\mathbb{P}[m\ge i]\right)g\left(\frac{\sum_{i\ge 1}\mathbb{P}[m\ge i](q_i+r_i)/2}{\sum_{i\ge 1}\mathbb{P}[m\ge i]}\right)\) (Jensen’s inequality)<br>
\(\le\mathbb{E}[m]\cdot g\left(min\left\{\frac{1}{2},\frac{1/2}{\mathbb{E}[m]}\right\}\right)\)<br>
(_g_ is increasing on \([0,\frac{1}{2}]\) and is maximum at \(\frac{1}{2}\))<br>
\(=(1+o(1))\cdot\mathbb{E}[m]\). ( \(\frac{1/2}{\mathbb{E}[m]}=o(1)\))

On the other hand,

\(\sum_{i\ge 1}\mathbb{P}[m\ge i]H(Y_i|X,Q_i,m\ge i)=\sum_{i\ge 1}\mathbb{P}[m\ge i]h(p)(1-q_i-r_i)\)<br>
\(=h(p)\left(\sum_{i\ge 1}\mathbb{P}[m\ge i]-\sum_{i\ge 1}\mathbb{P}[m\ge i](q_i+r_i)\right)\)<br>
\(\ge h(p)(\mathbb{E}[m]-1)\)<br>
\(=(1-o(1))h(p)\mathbb{E}[m].\)

