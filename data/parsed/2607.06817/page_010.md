Next, we establish the lower bound by constructing a 2-edge-coloring of _K<sub>n</sub>_ with _n_=(_a_-1)(_b_-1) containing no forbidden embeddings. Let \(f:\{0,1,2,\dots,n-1\}\rightarrow\{0,1,2,\dots,b-2\}\) be the function defined by \(f(x):=\lfloor\frac{x}{a-1}\rfloor\), and consider the 2-edge-coloring of _K<sub>n</sub>_ in which the edge between any two distinct vertices \(u,v\in V(K_n)\) is colored with color 1 if and only if _f(u_)=_f(v_). Let _G_<sub>1</sub> and _G_<sub>2</sub> be defined as above. By way of contradiction, suppose that _H_ is \(\Gamma\)-embeddable in _G_<sub>1</sub>. Then there exists an injective homomorphism from _H_ to _G_<sub>1</sub>. Since _H_ is connected, this means that some component of _G_<sub>1</sub> contains at least _a_ vertices, which yields a contradiction because all components of _G_<sub>1</sub> are isomorphic to _K_<sub>_a_-1</sub>.

Now, by way of contradiction, suppose that \(P_b^\mathrm{mon}\) is \(\Lambda\)-embeddable in _G_<sub>2</sub>. Then there exists an increasing injective homomorphism \(\varphi\) from \(P_b^\mathrm{mon}\) to _G_<sub>2</sub>. Since _f_ is nondecreasing, and \(f(\varphi(v))\neq f(\varphi(v+1))\) holds for every \(v\in\{0,1,2,\dots,b-2\}\), it follows that the function \(f\circ\varphi:\{0,1,2,\dots,b-1\}\rightarrow\{0,1,2,\dots,b-2\}\) is strictly increasing, which is clearly impossible. Therefore, \(R\left(H^\Gamma,(P_b^\mathrm{mon})^\Lambda\right)\ge 1+(a-1)(b-1)\).

The following results are immediate from Theorem 4.1, Proposition 2.4 and the fact that \(P_b^\mathrm{mon}\) has reflection symmetry.

**Corollary 4.2.** _For any_ \(a,b\in\mathbb{N}\)_, we have_ \(R_\mathrm{ref}(P_a^\mathrm{alt},P_b^\mathrm{mon})=1+(a-1)(b-1)\).

**Corollary 4.3.** _For any_ \(a,b\in\mathbb{N}\)_, we have_ \(R_\mathrm{ref}(S_a^\mathrm{sc},P_b^\mathrm{mon})=1+(a-1)(b-1)\).

We proceed by studying the reflective and dihedral Ramsey numbers of alternating paths versus alternating paths. Our computational results are given in s 3 and 4. As it turns out, the reflective Ramsey numbers are similar, but not identical, to the corresponding ordered Ramsey numbers, and they exhibit a pattern that is difficult to discern. On the other hand, the dihedral Ramsey numbers appear to coincide with the cyclic Ramsey numbers, leading to the following conjecture.

**Conjecture 4.4.** _For any_ \(a,b\ge 2\)_, we have_ \(R_\mathrm{dih}(P_a^\mathrm{alt},P_b^\mathrm{alt})=a+b-2-(ab\mathrm{mod}2)\).

Now, consider the computational results for the reflective and dihedral Ramsey numbers of alternating paths versus start-central stars; see s 5 and 6. Once again, the reflective Ramsey numbers appear to be similar, but not identical, to the corresponding ordered Ramsey numbers, and their structure seems difficult to understand. An interesting observation about the dihedral Ramsey numbers is that exact values were obtained for all the numbers in the first row of  6 with \(b\le 18\), whereas in the second row exact values were obtained for all \(b\le 30\). The results suggest that Kissat unexpectedly struggles with the case _a_=3 and odd \(b\ge 19\). Nonetheless, the dihedral Ramsey numbers appear to coincide with the cyclic Ramsey numbers, which leads to the following conjecture.

**Conjecture 4.5.** _For any_ \(a,b\ge 2\)_, we have_ \(R_\mathrm{dih}(P_a^\mathrm{alt},S_b^\mathrm{sc})=a+b-2-(ab\mathrm{mod}2)\).

The reflective Ramsey numbers of alternating paths versus monotone paths are fully determined by Corollary 4.2, and they coincide with the corresponding ordered Ramsey numbers; see  2. The dihedral Ramsey numbers also appear to coincide with the cyclic Ramsey numbers, as suggested by the computational results in  7. Thus, we pose the following conjecture.

**Conjecture 4.6.** _For any_ \(a\ge 3\) _and_ \(b\ge 4\)_, we have_ \(R_\mathrm{dih}(P_a^\mathrm{alt},P_b^\mathrm{mon})=1+(a-1)(b-2)\).

\begin{tabular}{cccccccccccccccccccccccccccccccccccc}
_a_ & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 20 & 21 & 22 & 23 & 24 & 25 & 26 & 27 \\
3 & 4 & 6 & 7 & 8 & 9 & 11 & 12 & 13 & 14 & 15 & 16 & 18 & 19 & 20 & 21 & 22 & 23 & 24 & 25 & 27 & 28 & 29 & \(\ge\) 30 & \(\ge\) 31 & \(\ge\) 32 \\
4 & & 7 & 8 & 10 & 11 & 12 & 14 & 15 & 16 & 17 & 18 & 20 & 21 & 22 & \(\ge\) 23 & \(\ge\) 24 & \(\ge\) 25 & & & & & & & & & & & & & & \\
5 & & 9 & 11 & 12 & 14 & 15 & 17 & 18 & 19 & \(\ge\) 20 & \(\ge\) 21 & \(\ge\) 23 & & & & & & & & & & & & & & & & & & & \\
6 & & & 12 & 13 & 15 & 16 & 18 & \(\ge\) 19 & \(\ge\) 21 & \(\ge\) 22 & & & & & & & & & & & & & & & & & & & & & \\
7 & & & & 14 & 16 & 18 & \(\ge\) 19 & \(\ge\) 21 & \(\ge\) 22 & & & & & & & & & & & & & & & & & & & & & & & \\
8 & & & & & 17 & \(\ge\) 19 & \(\ge\) 20 & \(\ge\) 22 & & & & & & & & & & & & & & & & & & & & & & & & \\
9 & & & & & & \(\ge\) 20 & \(\ge\) 21 & \(\ge\) 23 & & & & & & & & & & & & & & & & & & & & & & & & \\
\end{tabular}

\begin{tabular}{cccccccccccccccccccccccccccccccccccc}
_a_ & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 20 & 21 & 22 & 23 & 24 & 25 & 26 \\
3 & 3 & 5 & 5 & 7 & 7 & 9 & 9 & 11 & 11 & 13 & 13 & 15 & 15 & 17 & 17 & 19 & 21 & 21 & 23 & \(\ge\) 23 & 25 & \(\ge\) 25 & \(\ge\) 27 \\
4 & & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 & 16 & \(\ge\) 17 & \(\ge\) 18 & \(\ge\) 19 & & & & & & & & & & & & & \\
5 & & 7 & 9 & 9 & 11 & 11 & 13 & \(\ge\) 13 & \(\ge\) 15 & \(\ge\) 15 & & & & & & & & & & & & & & & & & & & \\
6 & & & 10 & 11 & 12 & 13 & \(\ge\) 14 & \(\ge\) 15 & \(\ge\) 16 & & & & & & & & & & & & & & & & & & & & \\
7 & & & & \(\ge\) 11 & 13 & \(\ge\) 13 & \(\ge\) 15 & & & & & & & & & & & & & & & & & & & & & & \\
\end{tabular}

3: Reflective Ramsey numbers \(R_\mathrm{ref}(P_a^\mathrm{alt},P_b^\mathrm{alt})\) with \(3\le a\le b\), \(a\le 9\) and \(b\le 27\).

4: Dihedral Ramsey numbers \(R_\mathrm{dih}(P_a^\mathrm{alt},P_b^\mathrm{alt})\) with \(3\le a\le b\), \(a\le 7\) and \(b\le 26\).

