times by (i), so a box only contains leaves of order at least _t_. By (ii), a box is obtained from a leaf of order at least _t_ by replacing its _e_ lowest symbols _P_<sub>0</sub> (rather than an arbitrary subset of them) by stars. Therefore, each leaf yields at most _m_+1 boxes, one for each value of _e_, which keeps their total number small, as we will show in Lemma 29. Boxes of this shape suffice: we will prove in Lemmas 27 and 28 that the leaves of order at least _t_ of an output string can be split among \(\alpha_t\) of them. (We will see below that the boxes of an output string all have exactly _m-t_ symbols that are _P_<sub>0</sub> or stars. We nonetheless allow fewer in the definition of a box, since boxes with fewer such symbols will arise as intermediate values in the dynamic program of Lemma 29.)

It is important here that a star stands for all ten terms, _P_<sub>0</sub> included, so that one box collects leaves of several orders (from _m-f_ to _m-f+e_, for a box with _e_ stars and _f-e_ symbols _P_<sub>0</sub>). This is needed for fast queries. If a star stood only for the nine terms _P<sub>ij</sub>_, then every box would fix the set of levels at which its leaves choose _P_<sub>0</sub>, so an output string would need a separate box for each subset of _Q_ of size at most _m-t_. That would be about \(2^m=\sqrt{D}\) boxes when _t_ is small, so a query would take about \(\sqrt{D}\) time, which gives no saving below _N_<sup>2</sup> when there are \(N^2/\sqrt{D}\) queries.

## The boxes of an output string.

We now make precise the informal rule above for finding the box of a leaf, and describe all the boxes of an output string _w_ with inner set _Q_. Let \(\tau\) be a leaf of order at least _t_ contributing to _w_, whose box we found above by going through the levels of _Q_ from the highest down (Figure 10). In symbols, let

\(Z:=\{\ell\in Q:\tau_\ell=P_0\}\text{(the levels at which}\tau\text{chooses}P_0\text{),}\)<br>
\(V:=Z\cup\{\text{the}m-t-|Z|\text{lowest levels of}Q\backslash Z\}\text{(}Z\text{padded from the bottom),}\)<br>
\(F_V:=\{\ell\in Q:\ell<\text{min}(Q\backslash V)\}\text{(the levels that we have not reached).}\)

Since the order of \(\tau\) is \(m-|Z|\ge t\), the set _V_ has exactly _m-t_ levels, namely, all the levels of _Q_ except the _t_ at which we saw a term other than _P_<sub>0</sub>. We define _F<sub>V</sub>_ by the same formula for every \(V\subseteq Q\), with _F<sub>V</sub>_:=_Q_ if _V=Q_. It is the longest initial segment of _Q_ contained in _V_. (_Z_ stands for _zero_, since these are the levels where \(\tau\) chooses _P_<sub>0</sub>, and _F_ stands for _free_, since these are the levels where the box has a star.)

For \(V\subseteq Q\) with |_V_|=_m-t_, let B_<sub>V</sub>_ be the set of the 9_<sup>t</sup>_ cubes \(\pi\) with

\(\pi_\ell=\left\{\begin{array}{ c c }
* & \text{if}\ell\in F_V, \\
P_0 & \text{if}\ell\in V\backslash F_V, \\
\text{one of the nine terms}P_{ij} & \text{if}\ell\in Q\backslash V, \\
\text{the term}P_{ij}\text{with}w_\ell=z_{ij} & \text{if}\ell\notin Q.
\end{array}\right.\)

Every cube in B_<sub>V</sub>_ is a box: it satisfies condition (i) of the definition because it has |_V_|=_m-t_ symbols _P_<sub>0</sub> or stars, and condition (ii) because its stars are below its symbols _P_<sub>0</sub>, since _F<sub>V</sub>_ is an initial segment of _Q_. When _V_ is the set defined above from a leaf \(\tau\), the box of \(\tau\) is the one in B_<sub>V</sub>_ with the terms of \(\tau\) at the levels of _Q_\\_V_ . Since a box of B_<sub>V</sub>_ has stars at the levels of _F<sub>V</sub>_, it contains the leaves with any terms there, of which there are 10<sup>|_F<sub>V</sub>_|</sup>. Notice that the set B_<sub>V</sub>_ depends on _w_ (since it depends on _Q_ and on the terms at the levels outside _Q_), but we omit this from the notation since _w_ will always be clear from context. We call the boxes in these sets, over all \(V\subseteq Q\) with |_V_|=_m-t_, the **_boxes of_** _w_.

There is another way to describe the boxes of _w_, in terms of the leaves of order exactly _t_ contributing to _w_. For such a leaf, consider the lowest level of _Q_ at which it chooses a term other<tbc>

