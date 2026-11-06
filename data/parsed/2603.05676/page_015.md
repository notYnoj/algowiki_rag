# Entropy-Sensitive Strictly In-Place Sorting

M
A
F
L
m2
m1 m2
F
p

Fig.9: Transforming the run to apply marker-encoding. We copy the block _L_ to just after _F_, with the remaining entries belonging to _M_. As in pivot-encoding, we use _p_ and the last \(\lambda\) entries of the array to encode **_b_**. However, this time it is done via our markers _m_<sub>1</sub> and _m_<sub>2</sub>, rather than the elements of _F_ and _L_. We replace _p_’s element with _m_<sub>2</sub> to make the decoding process identical to that of pivot-encoding.

