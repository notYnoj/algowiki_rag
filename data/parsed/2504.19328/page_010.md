and 4 see an increase in composition time as compared to iterations 1 and 2. Larger substructures (in higher iterations) have more vertex IDs that they can be expanded on, requiring more computational work. This leads to a steady increase in the reduce time from iteration 2 onwards as expansion is done in the reducer. The map time only slightly increases, as the mapper solely handles the routing of substructures based on vertex IDs. This implies that the map time is solely dependent on the number of substructure instances received by the mapper, irrespective of their size. It is essential to note that the dip from iteration 1 to iteration 2 is due to the beam being applied after the first iteration. In other words, all the edges in the graph are processed in the first iteration, but only the top beam substructures are processed starting from the second iteration. This greatly reduces the number of substructures considered for expansion. Thus, a significant dip is observed between iteration 1 and iteration 2.

**LiveJournal (4.9MV69ME)**: Here, trends are similar to those seen in the Amazon data set. This data set is **notably larger at 4.9 Million Vertices and 69 Million Edges** than the previous data sets. The average speedup while varying the number of partitions and mappers/reducers is greater than that observed in the Amazon data set.

Specifically, a consistent decrease of nearly **50%** is observed in transitions from 8 to 16 and 16 to 32 partitions. However, from 32 to 64 partitions, the speedup diminishes to 39%, but it remains higher compared to other data sets. This can be attributed to the larger size of the graph, which helps alleviate the added overhead from adding more tasks/processors. Having a large overhead due to a higher number of tasks for a small data set would diminish the speedup, but for a sufficiently large data set like LiveJournal, doubling the processors results in nearly double speedup (_approx. 50% reduction in time_).

## E. Response Time for All Experiments Performed

Figure 14 shows all the experiments that were performed for all the data sets shown in  VI.

## IX. CONCLUSIONS AND FUTURE WORK

This paper introduces a scalable algorithm for substructure discovery for HoMLNs, using a decoupling-based strategy. A<tbc>

<tbc>composition algorithm was presented and implemented using Map/Reduce, demonstrating its correctness and scalability.

Future work includes further improving efficiency by skipping composing after each iteration, still preserving accuracy. This seems to be a challenge as it is a trade-off among efficiency, accuracy, and graph characteristics.

## REFERENCES

[1] A. P. F. Miguel E. Coimbra and L. Veiga, "An analysis of the graph processing landscape," _Journal of Big Data_, 2021.

[2] N. G. de Bruijn, "A combinatorial problem," _Proc. Akad. Wet. Amsterdam_, vol. 49, pp. 758-764, 1946.

[3] A. T. Balaban, "Applications of graph theory in chemistry," _Journal of Chemical Information and Computer Sciences_, vol. 25, no. 3, pp. 334- 343, 1985. [Online]. Available: https://doi.org/10.1021/ci00047a033

[4] S. Wasserman and K. Faust, _Social network analysis: Methods and applications_. Cambridge university press, 1994.

[5] M. D. Domenico, V. Nicosia, A. Arenas, and V. Latora, "Layer aggregation and reducibility of multilayer interconnected networks," _CoRR_, vol. abs/1405.0425, 2014.

[6] A. Berenstein, M. P. Magarinos, A. Chernomoretz, and F. Aguero, "A multilayer network approach for guiding drug repositioning in neglected diseases," _PLOS_, vol. 10, no. 1, p. e0004300, 2016.

[7] M. Kivelä, A. Arenas, M. Barthelemy, J. P. Gleeson, Y. Moreno, and M. A. Porter, "Multilayer networks," _CoRR_, vol. abs/1309.7233, 2013.

[8] M. De Domenico, A. Solé-Ribalta, S. Gómez, and A. Arenas, "Navigability of interconnected networks under random failures," _Proc. of Ntl. Acad. of Sciences_, 2014.

[9] J. D. Wilson, J. Palowitch, S. Bhamidi, and A. B. Nobel, "Community extraction in multilayer networks with heterogeneous community structure," _J. Mach. Learn. Res._, vol. 18, no. 1, pp. 5458-5506, 2017.

[10] A. Santra, F. A. Irany, K. Madduri, S. Chakravarthy, and S. Bhowmick, "Efficient community detection in multilayer networks using boolean compositions," _Frontiers Big Data_, vol. 6, 2023. [Online]. Available: https://doi.org/10.3389/fdata.2023.1144793

[11] A. Santra, S. Bhowmick, and S. Chakravarthy, "Efficient community re-creation in multilayer networks using boolean operations," in _International Conference on Computational Science, ICCS 2017, 12-14 June 2017, Zurich, Switzerland_, ser. Procedia Computer Science, P. Koumoutsakos, M. Lees, V. V. Krzhizhanovskaya, J. J. Dongarra, and P. M. A. Sloot, Eds., vol. 108. Elsevier, 2017, pp. 58-67. [Online]. Available: https://doi.org/10.1016/j.procs.2017.05.246

[12] H. R. Pavel, A. Roy, A. Santra, and S. Chakravarthy, "Closeness centrality detection in homogeneous multilayer networks," in _Proceedings of the 15th International Joint Conference on Knowledge Discovery, Knowledge Engineering and Knowledge Management, IC3K 2023, Volume 1: KDIR, Rome, Italy, November 13-15, 2023_, A. L. N. Fred, F. Coenenen, and J. Bernardino, Eds. SCITEPRESS, 2023, pp. 17-29. [Online]. Available: https://doi.org/10.52220/0012159500003598

[13] K. Mukunda, A. Roy, A. Santra, and S. Chakravarthy, "Stress centrality in heterogeneous multilayer networks: Heuristics-based detection," in _IEEE Ninth International Conference on Big Data Computing Service and Applications, BigDataService 2023, Athens, Greece, July 17-20, 2023_. IEEE, 2023, pp. 103-110. [Online]. Available: https://doi.org/10.1109/BigDataService58306.2023.00021

[14] A. Santra, K. S. Komar, S. Bhowmick, and S. Chakravarthy, "From base data to knowledge discovery - _A life cycle approach_ - using multilayer networks," _Data Knowl. Eng._, vol. 141, p. 102058, 2022. [Online]. Available: https://doi.org/10.1016/j.datak.2022.102058

[15] D. J. Cook and L. B. Holder, "Substructure discovery using minimum description length and background knowledge," _Journal of Artificial Intelligence Research_, vol. 1, pp. 231-255, 1994.

[16] J. Rissanen, "A Universal Prior for Integers and Estimation by Minimum Description Length," _The Annals of Statistics_, vol. 11, no. 2, pp. 416 – 431, 1983. [Online]. Available: https://doi.org/10.1214/aos/1176346150

[17] R. Agrawal and R. Srikant, "Fast Algorithms for Mining Association Rules," in _Very Large Data Bases_, 1994, pp. 487-499.

[18] M. Deshpande, M. Kuramochi, and G. Karypis, "Frequent Sub- Structure-Based Approaches for Classifying Chemical Compounds," in _IEEE International Conference on Data Mining_, 2003, pp. 35-42.

