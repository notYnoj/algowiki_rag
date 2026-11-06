has no two points with the same _x_-coordinate. We will say that such a set has "distinct _x_- and _y_-coordinates".

\(\blacktriangleright\) **Definition 8** (_x_- and _y_-coordinates)**.** _For a point_ \(p\in\mathbb{R}^2\)_, we will denote its x- and y- coordinates as p.x and p.y. Similarly, we define_ \(P.x:=\{p.x|p\in P\}\) _and_ \(P.y:=\{p.y|p\in P\}\).

We start by defining the _mixing value_ of two sets: a notion of how many two sets of numbers are interleaved. It will be useful in defining both the alternation bound and the funnel bound. We define it in a few steps.

\(\blacktriangleright\) **Definition 9** (mixing string)**.** _Given two disjoint finite sets of real numbers L,R, let_ mix(_L,R_) _be the string in_ {L,R}<sup>∗</sup> _that is obtained by taking the union_ \(L\cup R\) _in increasing order and replacing each element from L by_ L _and each element from R by_ R_. For example,_ mix({2,3,8},{1,5})=`RLLRL`.

\(\blacktriangleright\) **Definition 10** (number of switches)**.** _Given a string_ \(s\in\{\mathtt{L},\mathtt{R}\}^*\)_, we define_ #switches(_s_) _as the number of side switches in s. Formally,_

\(\#\text{switches}(s):=\#\{t|s_t\neq s_{t+1}\}.\)

_For example,_ #switches(`LLLRLL`)=2_. Note that if we insert characters into s,_ #switches(_s_) _can only increase._

\(\blacktriangleright\) **Definition 11** (mixing value)**.** _Let_ mixValue(_L,R_):=#switches(mix(_L,R_)) _(see Figure 2)._

The mixing value has some convenient properties, which we will use later:

\(\blacktriangleright\) **Fact 12** (properties of mixValue)**.** _Function_ mixValue(_L,R_) _is:_

**(a)** _symmetric:_ mixValue(_L,R_)=mixValue(_R,L_);

**(b)** _monotone: if_ \(L_1\subseteq L_2\) _and_ \(R_1\subseteq R_2\)_, then_ \(\text{mixValue}(L_1,R_1)\le\text{mixValue}(L_2,R_2)\);

**(c)** _superadditive under concatenation: if_ \(L_1,R_1\subseteq(-\infty,x]\) _and_ \(L_2,R_2\subseteq[x,+\infty)\)_, then_ \(\text{mixValue}(L_1\cup L_2,R_1\cup R_2)\ge\text{mixValue}(L_1,R_1)+\text{mixValue}(L_2,R_2)\).

_Finally,_ \(\text{mixValue}(L,R)\le 2\cdot\text{min}(|L|,|R|)+1\).

\begin{tabular}{cccc}
\multicolumn{4}{c}{\(X=(4,1,3,5,4,2)\longrightarrow\)} \\
\multicolumn{4}{c}{time} \\
\multicolumn{4}{c}{\(x(3,3)\times(1,2)\times(4,1)\)} \\
\multicolumn{4}{c}{keys} \\
\end{tabular}

1
3
7
L
R
4
6
8
9





**Figure 1** transforming _X_ into its geometric view _G<sub>X</sub>_

**Figure 2** a visualization of mixValue({1,3,7},{4,6,8,9})=3

