## A.10 Proof of Lemma 2.10

_Proof._ Using the loads \(y_{(s,v_j)}=1\), \(y_{(v_j,t)}=\frac{W}{m}+1\), and \(y_{(v_j,v_j^1)}=W\frac{(n+1)(n-3)}{n}\) for any \(j\in J\) established in Lemmas 2.5 and 2.8 we have, by flow conservation at node _v<sub>j</sub>_:

\(y_{(s,v_j)}+\sum_{i\in I}y_{(u_i,v_j)}=y_{(v_j,t)}+y_{(v_j,v_j^1)}\)<br>
\(1+\sum_{i\in I}y_{(u_i,v_j)}=\left(\frac{W}{m}+1\right)+W\frac{(n+1)(n-3)}{n}\)<br>
\(\sum_{i\in I}y_{(u_i,v_j)}=\frac{W}{m}+W\frac{(n+1)(n-3)}{n}=W\left(\frac{3}{n}+\frac{n^2-2n-3}{n}\right)=W\left(\frac{n^2-2n}{n}\right)=W(n-2)\)<br>
\(\sum_{i\in I}y_{(u_i,v_j)}=\sum_{i\in I}w_i+W(n-3).\)

The only commodities crossing arcs (_u<sub>i</sub>,v<sub>j</sub>_) are _k<sub>L</sub>_ and _k<sub>H</sub>_. Let _l_ be the number of arcs entering _v<sub>j</sub>_ that carry commodity _k<sub>L</sub>_; from Lemma 2.9, commodity _k<sub>H</sub>_ is carried by the remaining _n-l_ arcs. For every \(i\in I\), the load of arc (_u<sub>i</sub>,v<sub>j</sub>_) is exactly _w<sub>i</sub>_ if it is crossed by commodity _k<sub>L</sub>_, and exactly _w<sub>i</sub>+W_ if it is crossed by commodity _k<sub>H</sub>_.

The total load on the _n_ arcs (_u<sub>i</sub>,v<sub>j</sub>_) can be expressed as:

\(\sum_{i\in I}y_{(u_i,v_j)}=\sum_{\text{arcs carrying}k_L}w_i+\sum_{\text{arcs carrying}k_H}(w_i+W)=\sum_{i\in I}w_i+(n-l)W.\)

Hence, we have \(\sum_{i\in I}w_i+W(n-3)=\sum_{i\in I}w_i+W(n-l)\), which implies _l_=3. Therefore, commodity _k<sub>L</sub>_ is carried by exactly 3 arcs in \(\{(u_i,v_j)\}_{i\in I}\) for every \(j\in J\).

## A.11 Proof of Proposition 2.2

_Proof._ Lemma 2.9 establishes that for every \(i\in I\), commodity _k<sub>L</sub>_ is routed through exactly one arc (_u<sub>i</sub>,v<sub>j</sub>_). For each \(j\in J\), let \(T_j\subset I\) denote the subset of objects _i_ for which commodity _k<sub>L</sub>_ uses the arc (_u<sub>i</sub>,v<sub>j</sub>_). Lemma 2.10 proves that each subset _T<sub>j</sub>_ contains exactly 3 elements. Because every object \(i\in I\)<tbc>

