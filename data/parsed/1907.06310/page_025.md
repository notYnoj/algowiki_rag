**Theorem B.2.** \(\Lambda(X,T)\le 44\mathrm{OPT}(X,T)\).

_Proof._ Let _P_=postorder(_T_) and \(T'=\mathrm{BST}(P\oplus X)\) and note that \(T'=\mathrm{BST}(P)\) since _P_ contains every key in _T_. Let _A_ and _B_ respectively be optimal executions for _P_ and \(P\oplus X\) starting from _T_, let _U_ be the sequence comprising the first |_T_|-1 transition trees of _A_, let _V_ be the sequence comprising the final |_X_| transition trees in _B_, and let \(T''\) be the after-tree for request |_T_| in _B_. The transition tree sequence \(U\oplus(T'')\oplus V\) is an execution for \(P\oplus X\) starting from _T_ with cost at most \(\mathrm{OPT}(P,T)+|T|+\mathrm{OPT}(X,T'')\). By \[47, Theorem 4\], \(\mathrm{cost}(P,T')\le 7|T|\). Splay’s cost and initial tree size respectively upper bound and lower bound optimum cost, meaning \(\mathrm{OPT}(P,T)\le\mathrm{OPT}(P,T')+|T|\le 8|T|\) and \(\mathrm{OPT}(X,T'')\le\mathrm{OPT}(X,T)+|T|\). Combining these inequalities establishes \(\mathrm{OPT}(P\oplus X,T)\le\mathrm{OPT}(X,T)+10|T|\le 11\mathrm{OPT}(X,T)\). By Theorem 7.2, _T_ is the final tree in Move-to-Root’s execution of _P_ starting from \(T'\). Hence, \(\Lambda(P\oplus X,T')=\Lambda(P,T')+\Lambda(X,T)\). By Theorem B.1, \(\Lambda_2(P\oplus X)=\Lambda(P\oplus X,T')-|T'|+1\) and \(\Lambda_2(P)=\Lambda(P,T')-|T'|+1\). Therefore, \(\Lambda(X,T)=\Lambda(P\oplus X,T')-\Lambda(P,T')=\Lambda_2(P\oplus X)-\Lambda_2(P)\le\Lambda_2(P\oplus X)\). Finally, by \[67, Theorem 7\] and Theorem A.1, \(\Lambda_2(P\oplus X)\le 2\mathrm{OPT}_\mathrm{rot}(P\oplus X,T)\le 4\mathrm{OPT}(P\oplus X,T)\le 44\mathrm{OPT}(X,T)\).

## Acknowledgments

We thank Luís Russo for suggesting improvements to Figure 3, Kurt Mehlhorn for simplifying our proof of Theorem 4.3, Amit Halevi for comments that clarified the presentation of our execution model, and Siddhartha Sen and Bernard Chazelle for editorial feedback. The high-level presentation of Sections 3 and 4 benefited from informal discussions with Daniel Cooney. We are indebted to John Iacono for his guidance in understanding the equivalence between Wilber’s bound and Move-to- Root’s crossing nodes, along with corroborating our empirical comparisons between the behaviors of Splay and Wilber’s bound. Finally, we found David Galles’ “Data Structure Visualizations” website instrumental for prototyping our proofs \[27\]. Research at Princeton University partially supported by an innovation research grant from Princeton and a gift from Microsoft.

## References

\[1\] Georgy Adel’son-Vel’skii and Evgenii Landis. “An algorithm for the organization of information”. Trans. by F. M. Goodspeed. In: _Soviet Mathematics Doklady_ 3 (1962), pp. 1259– 1263.

\[2\] Yehuda Afek, Haim Kaplan, Boris Korenfeld, Adam Morrison, and Robert Tarjan. “The CB tree: a practical concurrent self-adjusting search tree”. In: _Distributed Computing_ 27.6 (2014), pp. 393–417. doi: `10.1007/s00446-014-0229-0`.

\[3\] Brian Allen and Ian Munro. “Self-organizing binary search trees”. In: _Journal of the ACM_ 25.4 (1978), pp. 526–535. doi: `10.1145/322092.322094`.

\[4\] Arne Andersson. “General balanced trees”. In: _Journal of Algorithms_ 30.1 (1999), pp. 1–18. doi: `10.1006/jagm.1998.0967`.

\[5\] Rudolf Bayer and Edward McCreight. “Organization and maintenance of large ordered indexes”. In: _Acta Informatica_ 1.3 (1972), pp. 173–189. doi: `10.1007/bf00288683`.

\[6\] Michael Bender, Martín Farach-Colton, and William Kuszmaul. “What does dynamic optimality mean in external memory?” In: _Innovations in Theoretical Computer Science_. Dagstuhl, Germany: Schloss Dagstuhl, 2022, pp. 1–23. doi: `10.4230/LIPICS.ITCS.2022.18`.

