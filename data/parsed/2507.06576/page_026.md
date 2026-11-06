<tbc>_Proof._ Since the edge between _v_<sub>0</sub>_,v<sub>j</sub>_ is not included in _F_, \(E_2\cap E(H''_j)\subseteq F\) or equivalently, all the edges with cost 2 of \(H''_j\) are included in _F_. On the other hand, let _H<sub>i</sub>_ be one of the attached copies of _H_ to _v<sub>j</sub>_. Note that we have already showed that \(E_2\cap E(H_i)\in F\). If \(E_3\cap E(H_i)\cap F=\varnothing\), then there is a source-sink pair at distance 4 in _H<sub>i</sub>_ which is not disconnected. Therefore, in each _H<sub>i</sub>_, _F_ picks edges of total weight at least 5.

Therefore we obtain,

\(c(F)\ge t\cdot(5k-4)+(k-1-t)\cdot(5k)=5k^2-5k-4t\ge 5k^2-9k.\)

Even when _t_=0_,k_, one can use the same arguments as above to obtain the same lower bound on the cost of _F_. This concludes the proof of the theorem.

## 9 Conclusions and Future Work

We improve upon a decade-old lower bound on the multiflow-multicut gap for planar graphs and, in doing so, develop new techniques. The main question our work raises is whether tight gap results can be obtained, even for the class of cactus and series-parallel graphs, and more generally, for planar graphs. Proving such a result likely requires new techniques, making it an interesting and challenging problem.

**Acknowledgment**: We would like to thank Joseph Cheriyan for many helpful discussions throughout the course of this project.

## References

[Abr+19] Ittai Abraham, Cyril Gavoille, Anupam Gupta, Ofer Neiman, and Kunal Talwar. "Cops, robbers, and threatening skeletons: Padded decomposition for minor-free graphs". In: _SIAM Journal on Computing_ 48.3 (2019), pp. 1120- 1145.

[CF25] Jonathan Conroy and Arnold Filtser. "How to protect yourself from threatening skeletons: Optimal padded decompositions for minor-free graphs". In: _Proceedings of the 57th Annual ACM Symposium on Theory of Computing_. 2025, pp. 2281–2292.

[Cha+08] Amit Chakrabarti, Alexander Jaffe, James R Lee, and Justin Vincent. "Embeddings of topological graphs: lossy invariants, linearization, and 2-sums". In: _49th Annual IEEE Symposium on Foundations of Computer Science, 2008_. IEEE. 2008, pp. 761–770.

[CSW13] Chandra Chekuri, F Bruce Shepherd, and Christophe Weibel. "Flow-cut gaps for integer and fractional multiflows". In: _Journal of Combinatorial Theory, Series B_ 103.2 (2013), pp. 248–273.

[CV02] Robert Carr and Santosh Vempala. "Randomized metaroounding". In: _Probabilistic Methods in Combinatorial Optimization_ 20 (3 2002), pp. 342–352.

[FF56] Lester Randolph Ford and Delbert R Fulkerson. "Maximal flow through a network". In: _Canadian journal of Mathematics_ 8 (1956), pp. 399–404.

[Fil+24] Arnold Filtser, Tobias Friedrich, Davis Issac, Nikhil Kumar, Hung Le, Nadym Mallek, and Ziena Zeif. "Optimal padded decomposition for bounded treewidth graphs". In: _arXiv preprint arXiv:2407.12230_ (2024).

[Fri+23] Tobias Friedrich, Davis Issac, Nikhil Kumar, Nadym Mallek, and Ziena Zeif. "Approximate max-flow min-multicut theorem for graphs of bounded treewidth". In: _Proceedings of the 55th Annual ACM Symposium on Theory of Computing_. 2023, pp. 1325–1334.

