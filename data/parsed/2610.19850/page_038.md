<tbc>\(X'=X\backslash\{x\}\). Set \(X'\) contains \(T\cup\{a\}\) so no native connected component from _G_\\_X_ is a full component of \(X'\). Moreover, the connected component of \(G\backslash X'\) which contains _x_ does not admit \(y\in X'\) in its neighborhood. In brief, \(X'\) does not have any full component: it is a shy set. If \(X'\) is a PMC, then the theorem holds. Naturally, we assume that conflictual pairs remain in \(X'\). We will then remove all other conflicts for _y_, and pursue the execution of conflict-greedy with non-arbitrary selections, detailed below.

First, let us state some nice properties satisfied by \(X'\) in terms of reachability. Concretely, we show that pairs in \(\{a\}\times T\), \(T\times T\), \(S\times T\) and \(\{a\}\times S\) are not conflictual for \(X'\).

• \(T\subseteq R_G(a,X')\): _a_ is indeed adjacent to \(x\in\overline{X'}\) and, as \(\Omega\) is a PMC of _G_, there is a path from _x_ to any \(t\in T\) whose internal vertices belong to \(\overline{\Omega}\cap C_G(T,S)\subseteq\overline{X'}\).<tbc>

• For any \(t\in T\), \(T\subseteq R_G(t,X')\): as \(\Omega\) is a PMC, there exists a path from _t_ to any \(t'\in T\)<tbc>

S
x
D
y
a
T
t1
t2
t3
z
w

y
z
x
w

Ω
x
Ωa
a
y
t1
t2
t3
z
w

(a) Repetition of Figure 10 where _D_={_a_} is an _a_-shutter of an _a_-nice PMC \(\Omega=S\cup T\). Pairs (_x,z),(x,w),(y,z_) are separated.

(b) Illustration of set _S<sub>D</sub>_ via graph \(H(\Omega,D)\): vertices _x_, _y_ and _z_ are in blue since they are fully adjacent to _D_. A minimal blue vertex cover of \(H(\Omega,D)\) is _S<sub>D</sub>_={_x,y_} for example.

(c) The PMC \(\Omega_a\) (surrounded by yellow) obtained, given the _a_-nice PMC \(\Omega\) (surrounded by red), its _a_-shutter _D_={_a_} and the shutter-close set _S<sub>D</sub>_={_x,y_}. In this example, \(S\backslash\widehat{S}=S_D\).

Figure 12: An example of shutter-close set _S<sub>D</sub>_={_x,y_} for the _a_-shutter presented in Figure 10, together with the PMC \(\Omega_a\) obtained according to Theorem 9.

