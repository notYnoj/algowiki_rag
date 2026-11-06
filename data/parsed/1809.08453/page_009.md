<tbc>_Proof_ We make a reduction from Minimum 2-Satisfiability, which is strongly NP-hard \[Kohli _et al._, 1994\].

**Minimum 2-Satisfiability (Min 2-SAT):**

_INSTANCE:_ A set _V_ of variables, a collection _C_ of disjunctive clauses of at most 2 literals, where a literal is a variable or a negated variable in _V_ .

_SOLUTION:_ A truth assignment for _V_ .

_MEASURE:_ Number of clauses satisfied by the truth assignment (to minimize).

To illustrate the reduction, we will use the following 2-SAT instance:

\(V=\{v_1,v_2,v_3,v_4,v_5,v_6\}\) (5)

\(C=\{(v_1\vee v_2),(\neg v_2\vee\neg v_4),(\neg v_1\vee v_3),(v_3\vee\neg v_4),v_2,(v_5\vee v_6)\}\) (6)

As a preliminary step, note that we can get rid of variables that are present in only one clause. Such a variable is set to true if it is present as a negative literal in the clause and to false otherwise. It can then be removed from the instance. Furthermore, we can make sure that there are exactly two literals in each clause (by duplicating literals). For example, the instance described by Equations 5 and 6 can be modified to:

\(V=\{v_1,v_2,v_3,v_4\}\) (7)

\(C=\{(v_1\vee v_2),(\neg v_2\vee\neg v_4),(\neg v_1\vee v_3),(v_3\vee\neg v_4),(v_2\vee v_2)\}\) (8)

In the following we will denote by _n<sub>v</sub>_=|_V_| the number of variables and by _n<sub>c</sub>_=|_C_| the number of clauses. In the previous example _n<sub>v</sub>_=4 and _n<sub>c</sub>_=5. Furthermore, we will denote by _c<sub>i</sub>_ the _i<sup>th</sup>_ clause in _C_.

We are now going to create an instance of the GGISM problem such that:

- There is a one-to-one correspondence between the stable marriages and the truth assignments for _V_ .<tbc>

**-** A stable marriage minimizing the GGI of the agent’s disutilities corresponds to a truth assignment of _V_ minimizing the number of clauses that are satisfied.

In order to create a one-to-one correspondence between the stable marriages and the truth assignments for _V_ , we are going to create a rotation \(\rho_i\) for each variable \(v_i\in V\) . Each of these rotations will be exposed in the shortlists from the man-optimal stable marriage for the instance under construction. Additionally, we will ensure that these rotations will be the only ones of the stable marriage instance. In other words, the rotation poset will have one vertex per variable and no edge, as illustrated in Figure 2.

We now give the "meaning" of these rotations. Let’s recall that in a stable marriage there is a one-to-one correspondence between the closed subsets of nodes of the rotation poset and the stable marriages. Now let **x** be a stable marriage corresponding to a closed subset _R_ of rotations, then the corresponding truth assignment over _V_ consists in setting _v<sub>i</sub>_=1 if \(\rho_i\in R\) and _v<sub>i</sub>_=0 otherwise. Thus in the generated stable marriage instance, the man-optimal stable marriage (i.e., \(R=\emptyset\)) corresponds to a truth assignment where all variables in _V_ are set to 0 while the woman-optimal stable marriage (i.e., \(R=\{\rho_i|v_i\in V\}\)) corresponds to a truth assignment where all variables in _V_ are set to 1.

We now describe more precisely the fashion in which rotations \(\rho_i\) are generated. For each variable _v<sub>i</sub>_, we create a man-woman pair (_m<sub>ij</sub>,w<sub>ij</sub>_) for each clause _c<sub>j</sub>_ that involves

