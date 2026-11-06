<tbc>and has length _r_. Since A by assumption has no monochromatic _r_-block, the _a(p_) part of the outputs of B on this central interval cannot be monochromatic. The second behaviour happens if, for some \(t\in[T]\), Eq (9) fails for some pair of vertices inside _J<sub>s</sub>_. Then two adjacent vertices in _J<sub>s</sub>_ have different wishful teleportation keys. Since these keys are included in the output of B, the interval _J<sub>s</sub>_, which has length 2_T+r_, cannot be monochromatic.

## 6.3. Proof of Theorem 3.

Let \(s\in[n]\) and recall that A is assumed to have no monochromatic _r_-block in its support. Fix an interval<tbc>

\(J_s=[s,s+2T+r-1]\)

<tbc>of 2_T+r_ consecutive vertices where \(T\unknown\lfloor\frac{n-r}{2}\rfloor\), hence the interval does not overlap with itself. We prove that _J<sub>s</sub>_ is monochromatic at the end of B with probability zero: for all output labels

\(\lambda=\underbrace{(\kappa_{1,L},\kappa_{1,R},\dots,\kappa_{T,L},\kappa_{T,R},a)}_\kappa\in([d^2])^{2T}\times\Sigma\)

the probability that \(\lambda_p=\lambda\) for every \(p\in J_s\) is zero (recall that \(\lambda_p\) is the output of nodes _p_ in B, see Eq (8)). A union bound on _s_ then implies that none of the _J<sub>s</sub>_ are monochromatic w.p. one, hence that B has no monochromatic (2_T+r_)-block w.p. one.

For \(0\unknown t\unknown T\), define<tbc>

\(I_s(t)=[s+t,s+2T+r-1-t].\)

<tbc>At each round, _I<sub>s</sub>(t_) shrinks by removing one boundary vertex from each side. In particular, _I<sub>s</sub>_(0)=_J<sub>s</sub>_, and _I<sub>s</sub>(T_) has length _r_.

Let \(C_{\kappa,t}(J_s)\) be the event that, for all \(1\unknown\tau\unknown t\) and all \(p\in I_s(\tau)\),

(10) \(k_{\tau,L}(p)=k_{\tau,L}(p+1)=\kappa_{\tau,L}\text{and}k_{\tau,R}(p)=k_{\tau,R}(p-1)=\kappa_{\tau,R}.\)

Equivalently, in each of the first _t_ rounds, the keys needed to simulate the teleportations into all vertices \(p\in I_s(\tau)\) are equal to the corresponding entries of \(\kappa\). We also set \(C_{\kappa,0}(J_s)\) to be the trivial event.

Suppose that the outputs of the nodes in _J<sub>s</sub>_ are monochromatic, that is, \(\lambda_p=\lambda=(\kappa,a)\) for every \(p\in J_s\). Then each teleportation key in the output of each \(p\in J_s\) is equal to the corresponding component of \(\kappa\). Moreover, for every \(1\unknown\tau\unknown T\) and every \(p\in I_s(\tau)\), we have \(p-1,p,p+1\in I_s(\tau-1)\subseteq J_s\), and thus Eq (10) is satisfied. Therefore, a monochromatic _J<sub>s</sub>_ implies that \(C_{\kappa,T}(J_s)\) occurs for some value of \(\kappa\).

To rule out this monochromatic output in _J<sub>s</sub>_, we will show that after conditioning on \(C_{\kappa,T}(J_s)\), the state of B in _I<sub>s</sub>(T_) is the same as the state of A in this interval. Then, since by assumption A outputs no monochromatic _r_-block, it will follow that B cannot have the monochromatic 2_T+r_ block _J<sub>s</sub>_.

Let \(\rho_t^{(\mathscr{A})}(I)\) be the reduced state of A (see Definition 3.1) on an interval _I_ after _t_ rounds of A , which is obtained by tracing out all registers except<tbc>

\(\otimes_{p\in I}\mathsf{L}(p)\otimes\mathsf{M}(p)\otimes\mathsf{R}(p).\)

<tbc>Similarly, let \(\rho_t^{(\mathscr{B})}(I|C_{\kappa,t}(J_s))\) be the reduced state of B after _t_ simulated rounds, conditioned on \(C_{\kappa,t}(J_s)\), on the registers<tbc>

\(\otimes_{p\in I}\mathsf{L}_{t+1}(p)\otimes\mathsf{M}(p)\otimes\mathsf{R}_{t+1}(p).\)

<tbc>We claim that for every \(0\unknown t\unknown T\),

(11) \(\rho_t^{(\mathscr{B})}(I_s(t)|C_{\kappa,t}(J_s))=\rho_t^{(\mathscr{A})}(I_s(t)).\)

