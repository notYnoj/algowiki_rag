**Theorem 4.13** (\[9\])**.** _For any_ \(a,b\in\mathbb{N}\) _and tree T of order a, we have R(T,K<sub>b</sub>_)=1+(_a_-1)(_b_-1).

As an immediate consequence of Theorem 4.13, we obtain the following corollary.

**Corollary 4.14.** _For any_ \(a,b\in\mathbb{N}\)_, we have_ \(R_\mathrm{cyc}(S_a^\mathrm{sc},K_b)=R_\mathrm{dih}(S_a^\mathrm{sc},K_b)=1+(a-1)(b-1)\).

The ordered Ramsey numbers of start-central stars versus complete graphs were also recently computed \[4\].

**Theorem 4.15** (\[4, Theorem 4.24\])**.** _For any_ \(a,b\in\mathbb{N}\)_, we have_ \(R_\mathrm{ord}(S_a^\mathrm{sc},K_b)=1+(a-1)(b-1)\).

We now obtain the following proposition from Theorem 4.15, Corollary 4.14 and Proposition 2.2.

**Corollary 4.16.** _For any_ \(a,b\in\mathbb{N}\)_, we have_ \(R_\mathrm{ref}(S_a^\mathrm{sc},K_b)=1+(a-1)(b-1)\).

Therefore, the ordered, reflective, cyclic and dihedral Ramsey numbers all coincide for start-central stars versus complete graphs.

We conclude this section by considering the reflective Ramsey numbers of start-central stars versus nested matchings. In this case, the reflective Ramsey numbers appear to behave in a complicated manner; see  14. Nonetheless, these numbers seem to be close to the corresponding ordered Ramsey numbers.

## 5 Conclusion

We have shown how the SAT-based approach originally proposed by Poljak \[23\] for ordered Ramsey numbers and recently extended to cyclic Ramsey numbers \[4\] can be generalized to cover permutational Ramsey numbers with arbitrary associated permutation groups. Using this approach, we have computed small two-color reflective and dihedral Ramsey numbers for the following graph classes: monotone and alternating paths, monotone cycles, start-central stars, complete graphs and nested matchings. The extensive computation was automated through a pipeline of four `Python` modules based on the source code from \[5\], with significant optimizations made to improve the API and remove redundancy. We have also established several general results and formulated conjectures motivated by the computational findings.

As it turns out, although capable of obtaining lower bounds for small Ramsey numbers of both reflective and dihedral types, the SAT-based approach appears to be more efficient at providing upper bounds for reflective Ramsey numbers than for dihedral Ramsey numbers. This can be explained by the fact that the generated SAT<tbc>

\begin{tabular}{cccccccccccccccc}
_b_ & 4 & 6 & 8 & 10 & 12 & 14 & 16 & 18 & 20 & 22 & 24 & 26 & 28 & 30 \\
_a_ & & & & & & & & & & & & & & & \\
3 & 6 & 8 & 11 & 13 & 15 & 18 & 20 & 22 & 24 & 27 & 29 & 31 & 33 & 35 \\
4 & 7 & 10 & 12 & 15 & 18 & 20 & 22 & 25 & \(\unknown\) 27 & \(\unknown\) 29 & \(\unknown\) 31 & & & \\
5 & 8 & 11 & 14 & 17 & 20 & 22 & \(\unknown\) 24 & \(\unknown\) 27 & \(\unknown\) 29 & & & & & & \\
6 & 10 & 13 & 16 & 19 & 21 & \(\unknown\) 24 & \(\unknown\) 26 & \(\unknown\) 28 & & & & & & & \\
7 & 11 & 14 & 17 & 20 & \(\unknown\) 23 & \(\unknown\) 25 & \(\unknown\) 28 & & & & & & & & \\
8 & 12 & 15 & 19 & 22 & \(\unknown\) 24 & & & & & & & & & & \\
9 & 13 & 17 & 20 & \(\unknown\) 23 & \(\unknown\) 26 & & & & & & & & & & \\
10 & 15 & 18 & 22 & \(\unknown\) 25 & & & & & & & & & & & \\
11 & 16 & 20 & 23 & \(\unknown\) 26 & & & & & & & & & & & \\
12 & 17 & 21 & \(\unknown\) 24 & & & & & & & & & & & & \\
13 & 18 & 22 & \(\unknown\) 25 & & & & & & & & & & & & \\
14 & 19 & 23 & \(\unknown\) 27 & & & & & & & & & & & & \\
15 & 21 & 25 & & & & & & & & & & & & & \\
16 & 22 & 26 & & & & & & & & & & & & & \\
17 & 23 & 27 & & & & & & & & & & & & & \\
18 & 24 & \(\unknown\) 28 & & & & & & & & & & & & & \\
19 & 25 & \(\unknown\) 29 & & & & & & & & & & & & & \\
20 & 26 & \(\unknown\) 30 & & & & & & & & & & & & & \\
21 & 28 & & & & & & & & & & & & & & \\
22 & 29 & & & & & & & & & & & & & & \\
23 & 30 & & & & & & & & & & & & & & \\
24 & 31 & & & & & & & & & & & & & & \\
25 & 32 & & & & & & & & & & & & & & \\
26 & 33 & & & & & & & & & & & & & & \\
27 & 34 & & & & & & & & & & & & & & \\
28 & \(\unknown\) 36 & & & & & & & & & & & & & & \\
29 & \(\unknown\) 37 & & & & & & & & & & & & & & \\
30 & \(\unknown\) 38 & & & & & & & & & & & & & & \\
\end{tabular}

14: Reflective Ramsey numbers \(R_\mathrm{ref}(S_a^\mathrm{sc},M_b^\mathrm{nest})\) with any \(3\unknown a\unknown 30\) and even \(4\unknown b\unknown 30\).

