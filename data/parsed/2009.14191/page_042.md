<tbc>\(i\in[|U|]\}\), and one agent from \(C:=\{c_{i,j},c_{i,j^\prime},c_{i,j+1},d_{i,j}^1,d_{i,j}^3\}\cup\{x_3^{a_i},x_6^{a_i}:i\in[|U|]\}\). Thus, Theorem 4.34 also shows NP-completeness for the tripartite version of 3-DSRI-ML.

By "cloning" each agent corresponding to a man _d_-3 times (and for each "acceptable 3- set", adding the cloned men to this 3-set, and adding all (_d_-1)-subsets of the resulting _d_-set at their corresponding place in the preferences), one can derive NP-completeness of _d_-DSRI-ML for any fixed \(d\ge 3\).

## 5 Conclusion

Being a fundamental problem within the fields of stable matching \[35\] and the analysis of hedonic games \[2\], our work provides a seemingly first systematic study on the parameterized complexity of the NP-hard Multidimensional Stable Roommates. Focusing on the natural and well- motivated concept of master lists with the goal to identify efficiently solvable special cases, we reported partial success. While we have one main algorithmically positive result, namely fixed-parameter tractability for the parameter "maximum number of agents incomparable to a single agent", all other (single) parameterizations led to (often surprising) hardness results (see  1).

As to challenges for future research, first, it remains open whether our fixed-parameter tractability result mentioned above also transfers to the setting of Multidimensional Stable Marriage. Second, addressing the quest for identifying more islands of tractability, the study of further, perhaps also combined parameters is a worth-while goal. One possible parameter here would be to consider the setting that there are few strictly ordered master posets, and every agent derives its preferences of one of the master lists. Third, a natural open question is whether our W\[1\]-hardness results can be accompanied by XP-algorithms, or whether 3DSR-Poset is paraNP-hard for the considered parameters.

## Acknowledgements

KH was supported by DFG Research Training Group 2434 "Facets of Complexity". DK was partially supported by DFG project NI 369/19 while at TU Berlin. We thank the anonymous reviewers of the conference version of this paper.

## References

