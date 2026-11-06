design appropriate clause gadgets for each case:

1. For _socially and locally stable matching_ we add a vertex _y<sub>Cj</sub>_ to _W_ and an edge {_x<sub>Cj</sub>,y<sub>Cj</sub>_} of benefit _j_ to _E_ for every clause _C<sub>j</sub>_. Further we also add all the edges {_x<sub>Cj</sub>,y<sub>Cj</sub>_} to the starting state _M_<sub>0</sub> but keep _M_<sup>∗</sup>. Note that we did no add any social links for _y<sub>Cj</sub>_. Thus _M_<sup>∗</sup> is stable and can be reached if and only if we rematch every _y<sub>Cj</sub>_ at least once (and hence delete {_x<sub>Cj</sub>,y<sub>Cj</sub>_}).<tbc>

2. For _considerate matching_ we add two vertices _y<sub>Cj</sub>_ and \(y'_{Cj}\) to _W_ and edges {_x<sub>Cj</sub>,y<sub>Cj</sub>_} of benefit \(j-\frac{1}{2}\) and \(\{x_{Cj},y'_{Cj}\}\) of benefit _j_ to _E_ for every clause _C<sub>j</sub>_. Further we also add all the edges {_x<sub>Cj</sub>,y<sub>Cj</sub>_} to the starting state _M_<sub>0</sub> and all the edges \(\{x_{Cj},y'_{Cj}\}\) to _M_<sup>∗</sup>. Finally we introduce a social link between _y<sub>Cj</sub>_ and \(y'_{Cj}\). Now _x<sub>Cj</sub>_ cannot switch from _y<sub>Cj</sub>_ to \(y'_{Cj}\) as \(y'_{Cj}\) is friends with _y<sub>Cj</sub>_ and would thus reject _x<sub>Cj</sub>_. But, if _x<sub>Cj</sub>_ is single, \(y'_{Cj}\) does not reject _x<sub>Cj</sub>_. Hence again we need to make sure that for every clause _x<sub>Cj</sub>_ is matched to some vertex outside the clause-gadget and dropped to reach _M_<sup>∗</sup>.<tbc>

3. For _friendship matching_ we add two vertices _y<sub>Cj</sub>_ and \(y'_{Cj}\) to _W_ and edges {_x<sub>Cj</sub>,y<sub>Cj</sub>_} of benefit \(j-\frac{1}{2}\) and \(\{x_{Cj},y'_{Cj}\}\) of benefit _j_ to _E_ for every clause _C<sub>j</sub>_. The only friendship value \(\neq 0\) is \(\alpha_{x_{Cj},y_{Cj}}=\frac{1}{2j-1}\). Again we add all the edges {_x<sub>Cj</sub>,y<sub>Cj</sub>_} to the starting state _M_<sub>0</sub> and all the edges \(\{x_{Cj},y'_{Cj}\}\) to _M_<sup>∗</sup>. Note that by the choice of \(\alpha_{x_{Cj},y_{Cj}}\) the perceived value for _x<sub>Cj</sub>_ from {_x<sub>Cj</sub>,y<sub>Cj</sub>_} now is \((1+\alpha_{x_{Cj},y_{Cj}})(j-\frac{1}{2})=j-\frac{1}{2}+(j-\frac{1}{2})\frac{1}{2j-1}=j=b(\{x_{Cj},y'_{Cj}\})\), that is, there is a tie in _x<sub>Cj</sub>_’s preference list regarding _y<sub>Cj</sub>_ and \(y'_{Cj}\). Hence _M_<sup>∗</sup> is stable but _x<sub>Cj</sub>_ will not switch directly from _y<sub>Cj</sub>_ to \(y'_{Cj}\). But once _x<sub>Cj</sub>_ is single we can match it with \(y'_{Cj}\) as desired.<tbc>

4. For _correlated matching with ties_ we add two vertices _y<sub>Cj</sub>_ and \(y'_{Cj}\) to _W_ and edges {_x<sub>Cj</sub>,y<sub>Cj</sub>_} and \(\{x_{Cj},y'_{Cj}\}\), both of benefit _j_, to _E_ for every clause _C<sub>j</sub>_. Further we also add all the edges {_x<sub>Cj</sub>,y<sub>Cj</sub>_} to the starting state _M_<sub>0</sub> and all the edges \(\{x_{Cj},y'_{Cj}\}\) to _M_<sup>∗</sup>. Then _x<sub>Cj</sub>_ does not switch from _y<sub>Cj</sub>_ to \(y'_{Cj}\) as it yields no improvement. But, if _x<sub>Cj</sub>_ is single, we can choose to match to \(y'_{Cj}\).<tbc>

uz
uT
uy
uT
uz
uT
wx
wx + k
wy
wy + k
wz
wz + k
wx + 2k
wx + 3k
wy + 2k
wy + 3k
wz + 2k
wz + 3k
wz
wT
wy
wT
wz
wT
2l + j
1 + j
3l + j
XCj

**Fig.2.** Central gadget with variables _x_, _y_, _z_ and clause \(C_j=x\vee\overline{y}\vee z\)

