_Proof._ (of Theorem 8). The constraints \(\alpha_a\ge-1\) for all \(a\in U_A\backslash U^*\) are valid inequalities for C<sub>_G_<sup>∗</sup></sub>, thus \(\mathcal{C}_{G^*}\cap\{\alpha_a=-1:a\in U_A\backslash U^*\}\) defines a face of C<sub>_G_<sup>∗</sup></sub>. This face is the polytope F<sub>_G_<sup>∗</sup></sub>. Since C<sub>_G_<sup>∗</sup></sub> is integral, so is F<sub>_G_<sup>∗</sup></sub>. Every extreme point of F<sub>_G_<sup>∗</sup></sub> has the form \((I_N,\unknown)\) where _N_ is a dominant matching and \(\unknown\) is a dominant witness of _N_ along with the extra condition that \(\gamma_a=-1\) for \(a\in U_A\backslash U^*\). Thus _N_ is an extra-dominant matching (see Definition 3) and \(\unknown\) is an _extra-dominant witness_ of _N_.

Since \((I_M,\unknown)\in\mathcal{C}_{G^*}\) for every dominant matching _M_ and every dominant witness \(\unknown\) of _M_, we have \((I_N,\unknown)\in\mathcal{F}_{G^*}\) for every extra-dominant matching _N_ and every extra-dominant witness \(\unknown\) of _N_. Thus F<sub>_G_<sup>∗</sup></sub> is an extension of the extra-dominant matching polytope of _G_<sup>∗</sup>. \(\square\)

## 4 Quasi-Popular Matching via the Popular Fractional Matching Polytope

In this section we will show another proof of Theorem 2. In fact, our algorithm in this section computes a quasi-popular matching of cost at most that of a min-cost popular fractional matching. We will first devise an understanding of _witness_ for quasi-popular matchings.

### 4.1 Witness for Quasi-Popular Matchings

Let \(G=(A\cup B,E)\) be a marriage instance and let _M_ be any matching in _G_. Recall the edge labels in \(\{(\pm,\pm)\}\) from Section 2. Based on these labels, we will now define an edge weight function _g<sub>M</sub>_ in _G_ as follows:

\(g_M(e)=\left\{\begin{array}{ c c }
+2 & \text{if}e\text{is labeled}(+,+) \\
-4 & \text{if}e\text{is labeled}(-,-) \\
-1 & \text{if}e\text{is labeled}(+,-)\text{or}(-,+) \\
0 & \text{if}e\in M.
\end{array}\right.\) (15)

Note that in the above edge weight function, a vote of "-" gets scaled by a factor of 2 to become a -2 while a vote of "+" remains a +1. This is because in an election between _M_ and a rival matching, a "-" is a vote for _M_ and against the rival matching while a "+" is a vote for the rival matching. Also, _g<sub>M</sub>(e_)=0 for all \(e\in M\) since both vertices vote "0" for each other: both endpoints of _e_ are indifferent between _M_ and the rival matching since each of them gets assigned the same partner in both the matchings.

Let \(\tilde{G}\) be the graph _G_ augmented with self-loops, i.e., each vertex is assumed to be its own last choice neighbor. Thus any matching _M_ in _G_ becomes a perfect matching \(\tilde{M}\) in \(\tilde{G}\) by including self-loops at all vertices left unmatched in _M_. The edge weight function _g<sub>M</sub>_ can be extended to self-loops as well: let _g<sub>M</sub>(u,u_)=0 if _u_ is matched to itself in \(\tilde{M}\), else _g<sub>M</sub>(u,u_)=-2.

Thus _g<sub>M</sub>_ is an edge weight function in \(\tilde{G}\) and Claim 2 follows easily from the definition of _g<sub>M</sub>_.

**Claim 2** _For any matching N in G, we have_ \(g_M(\tilde{N})=\phi(N,M)-2\phi(M,N)\).

Hence, a matching _M_ in _G_ satisfies \(u(M)\le 2\) if and only if every perfect matching in \(\tilde{G}\) has weight at most 0 with respect to the _g<sub>M</sub>_. Consider the max-weight perfect matching LP in \(\tilde{G}=(A\cup B,\tilde{E})\): this is (LP3) given below in variables _x<sub>e</sub>_ for \(e\in\tilde{E}\); recall that \(\tilde{\delta}(u)=\delta(u)\cup\{(u,u)\}\). The linear program (LP4) is the dual of (LP3). The dual variables are \(\alpha_u\) for \(u\in A\cup B\).

\(\text{maximize}\sum_{e\in\tilde{E}}g_M(e)\cdot x_e\) (LP3)

\(\text{subject to}\sum_{e\in\tilde{\delta}(u)}x_e=1\forall u\in A\cup B\)<br>
\(x_e\ge 0\forall e\in\tilde{E}.\)

