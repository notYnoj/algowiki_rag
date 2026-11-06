<tbc>_fundamental circuit_ of an element \(x\in S\backslash B\) for a base _B_, denoted by _C<sub>B</sub>(x_), is the unique circuit in _B+x_. By a slight abuse of notation, we will also use _C<sub>I</sub>(x_) for an independent set _I_ and an element \(x\in S\backslash I\) to denote the unique circuit in _I+x_ if it exists. Any pair of circuits satisfies the following property.

**Proposition 4** (Strong circuit axiom)**.** _If_ \(C,C'\) _are circuits,_ \(x\in C\backslash C'\)_, and_ \(y\in C\cap C'\)_, then there is a circuit_ \(C''\subseteq C\cup C'\) _such that_ \(x\in C''\) _and_ \(y\notin C''\).

If we have a total order \(\succ\) given on _S_, then the triple \(M=(S,\mathcal{I},\succ)\) is called a _(totally) ordered matroid_. A nice property of totally ordered matroids is that for any weight vector \(w\in\mathbb{R}^S\) that satisfies \(w_x>w_y\Leftrightarrow x\succ y\), the unique maximum weight base is the same. We call this base _A_ the _optimal base_ of \((S,\mathcal{I},\succ)\); it is characterized by the property that the worst element of _C<sub>A</sub>(x_) is _x_ for any \(x\in S\backslash A\). Equivalently, a base _A_ is optimal with respect to \(\succ\) if and only if any pair of elements \(a\in A\) and \(b\in S\backslash A\) with \(A-a+b\in\mathcal{I}\) satisfies \(a\succ b\).

Here we prove the theorem that will be our main tool in proving the approximation bound for our algorithm. To our knowledge, this result on exchanges has not been previously observed in the literature. See Remark 8 for a comparison between a previously known property. We use the notation \[_r_\]={1,2_,...,r_}.

**Theorem 5.** _Let_ \(M=(S,\mathcal{I},\succ)\) _be a totally ordered matroid of rank r. Let A be the optimal base and B be a base disjoint from A. Then, there is a perfect matching_ \(a_ib_i(i\in[r])\) _between A and B such that_ \(a_i\succ b_i\) _and_ \(B+a_i-b_i\in\mathcal{I}\) _for every_ \(i\in[r]\).

_Proof._ Define \(E_A=\{ab\in A\times B:A-a+b\in\mathcal{I}\}\) and \(E_B=\{ab\in A\times B:B+a-b\in\mathcal{I}\}\).

**Claim 6.** _Let C be any circuit with_ \(C\subseteq A\cup B\)_. For any element_ \(a\in C\cap A\)_, there exists_ \(b\in C\cap B\) _with_ \(ab\in E_A\)_. For any element_ \(b\in C\cap B\)_, there exists_ \(a\in C\cap A\) _with_ \(ab\in E_B\).

_Proof._ We only show the first claim because the second one is shown symmetrically. Take any \(a\in C\cap A\). Suppose conversely that \(ab\unknown\in E_A\) for any \(b\in C\cap B\). This means that, we have \(a\unknown\in C_A(b)\) for any \(b\in C\cap B\). Set \(C'=C\) and repeatedly update it as follows while \(C'\cap B\neq\emptyset\): (1) Take any \(b\in C'\cap B\), (2) apply the strong circuit axiom to \(C',C_A(b),a\in C'\backslash C_A(b)\), and \(b\in C'\cap C_A(b)\) to obtain a circuit \(C''\) satisfying \(C''\subseteq C'\cup C_A(b)\), \(a\in C''\), and \(b\unknown\in C''\), (3) update \(C'\) by \(C''\). Then, \(C'\) always satisfies \(a\in C'\subseteq A\cup B\) and the size of \(|C'\cap B|\) decreases monotonically. We finally obtain a circuit \(C'\) with \(C'\subseteq A\), a contradiction.

Define \(E=\{ab\in E_B:a\succ b\}\). Then, showing the existence of a perfect matching in _G_=(_A,B;E_) completes the proof of the theorem. To this end, we show the following claim.

**Claim 7.** _For any circuit C with_ \(C\subseteq A\cup B\)_, there exists_ \(ab\in E\) _with_ \(\{a,b\}\subseteq C\).

_Proof._ By Claim 6, we see that there is a cycle \(Q\subseteq E_A\cup E_B\) (possibly of length two) that is contained in _C_ and uses edges in _E<sub>A</sub>_ and _E<sub>B</sub>_ alternately. (Start at any element in _C_ and apply Claim 6 repeatedly.) As _A_ is optimal, any \(a'b'\in Q\cap E_A\) satisfies \(a'\succ b'\). Then, there must exist a pair \(ab\in Q\cap E_B\) with \(a\succ b\) because otherwise the relation \(\succ\) on the elements in _Q_ would become cyclic and could not form a total order. This _ab_ belongs to _E_.

We now show the existence of a perfect matching in _G_=(_A,B;E_). Suppose, to the contrary, there is no perfect matching in _G_. By Hall’s theorem, then there exists a set \(X\subseteq A\) such that \(|X|>|\Gamma_G(X)|\), where \(\Gamma_G(X)=\{b\in B:\exists a\in X,ab\in E\}\). The size of the set \(X\cup(B\backslash\Gamma_G(X))\) is larger than that of the base _B_, and hence there exists a circuit \(C\subseteq X\cup(B\backslash\Gamma_G(X))\). By Claim 7, there exists \(ab\in E\) included in _C_, which satisfies \(a\in X\) and \(b\in B\backslash\Gamma_G(X)\), contradicting the definition of \(\Gamma_G(X)\).

