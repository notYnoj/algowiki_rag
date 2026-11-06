<tbc>Now, checking the boundedness hypotheses, note that _np_<sup>3</sup> is decreasing, _e<sub>d</sub>_ is increasing and _d<sub>v</sub>_ is non-increasing. Thus we have that \(d_v(i+1)-d_v(i)\le\Delta d_v^-(i)\le n(p(i)^3-p(i+1)^3)+(e_d(i+1)-e_d(i))\). Now

\(e_d(i+1)-e_d(i)=8b^{2/3}n(log(p(i+1))-log(p(i)))\)<br>
\(=8b^{2/3}n\left(log\left(1-\frac{4i}{|V(0)|}\right)-log\left(1-\frac{4(i+1)}{|V(0)|}\right)\right)=\Theta(b^{2/3})=o(1),\)

_n(p(i_)<sup>3</sup>-_p(i_+1)<sup>3</sup>)=_O_(1) and \(\Delta d_v(i)\ge-4\). Thus there is some absolute constant _c_ such that we may take \(\theta=c\) and \(\Theta=10c\), and we have \(\theta\Theta nplog^2(n)=O(nplog^2(n))\checkmark b^{4/3}n^2\), as required.

Similarly, the supermartingale details for the trend and boundedness hypotheses for _Q_ are given in \[**6**\]. We get that<tbc>

\(\mathbb{E}'(\Delta Q(i))=-\frac{16Q(i)}{|V(0)|p}\pm\frac{2|V(0)|pe_d^2}{Q(i)}+O(1).\)

<tbc>Thus letting _f<sub>q</sub>=bn_<sup>2</sup>, and assuming at step _i_ that we are in the lower critical interval, we find that

\(\mathbb{E}'(\Delta Q^-(i))\ge-\frac{16(n^2p^4-e_q+f_q)}{|V(0)|p}-\frac{2|V(0)|pe_d^2}{Q(i)}+\frac{16n^2p^3}{|V(0)|}+\frac{e'_q}{|V(0)|}\)<br>
\(+O\left(1+\frac{n^2p^2}{|V(0)|^2}+\frac{e''_q}{|V(0)|^2}\right).\)

Then we get that

\(\mathbb{E}'(\Delta Q^-(i))\ge\frac{16bn^2}{|V(0)|p}-\frac{8bn^2log(p)}{|V(0)|p}-\frac{8|V(0)|b^{4/3}n^2p(1-4log(p))^2}{Q(i)}+\frac{32bn^2}{|V(0)|p}\)<br>
\(+O\left(1+\frac{n^2p^2}{|V(0)|^2}+\frac{e''_q}{|V(0)|^2}\right)\)

Noting that \(log(p)\le 0\) we have that

\(\mathbb{E}'(\Delta Q^-(i))\ge\frac{48bn^2}{|V(0)|p}-\frac{8|V(0)|b^{4/3}n^2p(1-4log(p))^2}{Q(i)}+O\left(1+p^2+\frac{b}{p^2}\right)\)

Since \(p^2\gg b^{1/3}\) and \(\frac{48bn^2}{|V(0)|p}=\Theta\left(\frac{bn}{p}\right)\), we have that \(\frac{8|V(0)|b^{4/3}n^2p(1-4log(p))^2}{Q(i)}=O\left(\frac{b^{4/3}nlog(n)}{p^3}\right)=o\left(\frac{bn}{p}\right)\), and the ‘big-O’ terms are all also \(o\left(\frac{bn}{p}\right)\). Thus we have that \(\mathbb{E}'(\Delta Q^-(i))\ge 0\) as required.

For the supermartingale we have

\(\mathbb{E}'(\Delta Q^+(i))\le-\frac{16(n^2p^4+e_q-f_q)}{|V(0)|p}+\frac{2|V(0)|pe_d^2}{Q(i)}+\frac{16n^2p^3}{|V(0)|}-\frac{e'_q}{|V(0)|}\)<br>
\(+O\left(1+p^2+\frac{b}{p^2}\right),\)

and it is clear the same arguments for the submartingale follow through with the switched signs, so that \(\mathbb{E}'(\Delta Q^+(i))\le 0\), as required.

Then verifying boundedness hypotheses, by assumption, for each _i_ we are considering we have _i\<T_ and may use our bounds on degrees to consider \(\Delta Q^\pm(i)^2\). In

