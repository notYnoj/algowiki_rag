**Lemma 6.1.** _There exist constants_ \(\eta_\mathrm{lin},c_\mathrm{lin}>0\) _and an explicit family_ \(\{I(m)\}_{m\in\{0,1\}^k}\) _of satisfiable bounded-occurrence Max E3LIN2 instances on_ \(n=\Theta(k)\) _variables such that every randomized algorithm B satisfying_<tbc>

\(\mathbb{E}_R\big[\#\text{\textit{equations of}}I(m)\text{\textit{satisfied by}}B(I(m);R)\big]\ge(1-\eta_\mathrm{lin})|I(m)|\forall m\in\{0,1\}^k\)

<tbc>_obeys_

\(\mathbb{E}_{m\in\{0,1\}^k}\mathbb{E}_{i\in[k]}\big[\text{EMD}_{d_\mathrm{H}}\big(B(I(m)),B(I(m^{\oplus i}))\big)\big]\ge c_\mathrm{lin}n,\)

_where_ \(m^{\oplus i}\) _denotes m with its ith bit flipped._

_Proof._ This is exactly the averaged earth-mover lower bound obtained from Lemma 3.7 using the binary LRCC family from Section 4.1. Since the rate, distance, detection probability, and variable degree are all absolute constants, the right-hand side of Lemma 3.7 is bounded below by a positive constant for sufficiently small \(\eta_\mathrm{lin}\). Multiplying by the block length converts the normalized Hamming metric to _d_<sub>H</sub>, and the resulting Max E3LIN2 instances have \(\Theta(n)\) output coordinates. Hence the averaged instability is \(\Omega(n)\).

We now pass from E3LIN2 to E3SAT using the standard four-clause gadget. Because the E3LIN2 family already comes with a fixed ordered list of equation scopes, this step preserves a common template: varying _m_ changes only the right-hand-side bits of _O_(1) equations, hence only the sign patterns in _O_(1) gadgets. For each equation

\(x\oplus y\oplus z=b,\)

let _G<sub>b</sub>(x,y,z_) denote the standard 4-clause gadget on the same variable triple with the property that any assignment satisfies all four clauses iff it satisfies the equation, and otherwise it satisfies exactly three clauses.

**Theorem 6.2** (One-sided endpoint instability for ordinarily encoded satisfiable Max E3SAT)**.** _There exist constants_ \(\eta,c,\Delta>0\)_, an integer L=O_(1)_, and an explicit family_ \(\{\Phi(m)\}_{m\in\{0,1\}^k}\) _of satisfiable bounded-occurrence_ 3_-CNF formulas on the same variable set_ \[_n_\] _with the same number M=O(n_) _of clauses, where_ \(n=\Theta(k)\)_, such that the following holds._

_Let A be any randomized algorithm that is one-sided_ \((1-\eta)\)_-approximate for Max E3SAT. Then:_

1. **_Endpoint instability._**<tbc>

<tbc>\(\mathbb{E}_{m\in\{0,1\}^k}\mathbb{E}_{i\in[k]}\big[\text{EMD}_{d_\mathrm{H}}\big(A(\Phi(m)),A(\Phi(m^{\oplus i}))\big)\big]\ge cn.\)<tbc>

_2._ **_Single-clause path version._** _For every_ \(m\in\{0,1\}^k\) _and_ \(i\in[k]\)_, there exists a sequence_<tbc>

<tbc>\(\Phi(m)=\Psi_0^{m,i},\Psi_1^{m,i},\dots,\Psi_L^{m,i}=\Phi(m^{\oplus i})\)<tbc>

<tbc>_such that each consecutive pair_ \(\Psi_{t-1}^{m,i},\Psi_t^{m,i}\) _differs by replacing a single clause by another clause on the same variable triple, and_<tbc>

<tbc>\(\mathbb{E}_{m\in\{0,1\}^k}\mathbb{E}_{i\in[k]}\big[\sum_{t=1}^L\text{EMD}_{d_\mathrm{H}}\big(A(\Psi_{t-1}^{m,i}),A(\Psi_t^{m,i})\big)\big]\ge cn.\)<tbc>

