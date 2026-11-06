Since the hard instances of the independent set polytope from Theorem 14 come from graphs of bounded degree, the number of clauses in the 2SAT instance we create is linear in the number of variables.

Now apply the sequence of reductions from Section 5, transforming the 2SAT instance \(\psi\) with _n_ variables and \(\Theta(n)\) clauses into an equivalent 2SAT instance with \(\Theta(n)\) variables and clauses, and then defining the min-cost quasi-popular matching instance \(G_\psi\) on \(\Theta(n)\) vertices and \(\Theta(n)\) edges defined in Section 5. The reduction from Section 5 assumed that \(\psi\) was a 3SAT instance but it clearly applies to a 2SAT instance as well.

Recall the edge cost function cost defined in Section 5. Consider the following face _F_ of the quasi-popular matching polytope Q of \(G_\psi\), where \(F=\{z\in\mathcal{Q}:\text{cost}(z)=0\}\). Our goal is to define a linear surjective map _h_ from the face _F_ defined above to \(C(\psi)\). Hence, given an extension T for Q, we obtain that

\(C(\psi)=\{x:x=h(z),(z,y)\in\mathcal{T},\text{cost}(z)=0\}.\)

Therefore, an extension of small size for Q would imply the existence of an extension of small size for \(C(\psi)\). The lower bound on the extension complexity of \(C(\psi)\) will therefore imply the claimed bound.

We will need the following properties:

1. Let _M_ be a matching that belongs to _F_. Thus cost(_M_)=0. Let _S_ be the following true/false assignment to the variables in \(\psi\). For \(i\in[n]\):<tbc>

<tbc>\(S(x_i)=\left\{\begin{array}{ c c }
\text{false} & \text{if}(c_i,d'_i)\in M; \\
\text{true} & \text{otherwise}.
\end{array}\right.\)<tbc>

<tbc>It follows from Lemma 8 that _S_ satisfies \(\psi\).<tbc>

2. Let _S_ be a satisfying assignment for \(\psi\). As shown in the proof of Theorem 13, there is a matching \(M\in F\) with the following properties:<tbc>

<tbc>\(\text{for}i\in[n]:(c_i,d'_i)\in M\Longleftrightarrow S(x_i)=\text{false}.\)<tbc>

<tbc>Define the mapping _h_ from _F_ to \(C(\psi)\) as: for \(z\in F\), let _h_(**_z_**)=**_x_** where \(x_i=1-z_{(c_i,d_i^\prime)}\) for \(i\in[n]\). Part 1 above implies that, if **_z_** is a vertex of _F_, then _h_(**_z_**) is a satisfying assignment. Together with part 2, we deduce \(h(F)=C(\psi)\). Thus we can conclude that \(xc(\mathcal{Q})\ge 2^{\Omega(n/\mathrm{log}n)}\). Since the number of edges of \(G_\psi\) is \(\Theta(n)\), the bound follows.

## 7 The Dominant Matching Polytope

We now prove Theorem 4. Section 7.1 shows a compact extended formulation for the dominant matching polytope. In Section 7.2, we formulate it in the original space R_<sup>m</sup>_ and Section 7.3 shows a lower bound on the number of its facets.

### 7.1 A New Extended tion for the Dominant Matching Polytope

We now show how to modify Theorem 9 so as to obtain an extended formulation for D_<sub>G</sub>_ that holds for _any_ marriage instance \(G=(A\cup B,E)\). Let _U_ be the set of unpopular vertices of _G_.

Consider the following variant \(\mathcal{E}'_G\) of the extended formulation E_<sub>G</sub>_ for the popular fractional matching polytope of _G_ \[31\] recalled in Section 2.1:

\(\sum_{u\in A\cup B}\alpha_u=0\) (19)

\(\alpha_a+\alpha_b\ge c_x(a,b)\forall(a,b)\in E\) (20)

\(\alpha_u\ge-\sum_{e\in\delta(u)}x_e\forall u\in A\cup B\) (21)

\(\sum_{e\in\tilde{\delta}(u)}x_e=1\forall u\in A\cup B\) (22)

\(x_e\ge 0\forall e\in\tilde{E},\) (23)

