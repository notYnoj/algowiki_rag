### 2.4.2. TBSG

In order to approximate a (_r,p_)-MSNET and reduce the time complexity, we need to construct a KNNG (K Nearest Neighbor Graph) of high quality and efficiency. There are many algorithms for fast construction of approximate KNNG, we adopt the algorithm in Efanna[33], the complexity of which is about _O(n_<sup>1.16</sup>). Finally, we combine Cover Tree and KNNG to get TBSG, and adopt our edge selection strategy to make the graph close to a (_r,p_)-MSNET. The detail can be seen in Algorithm 3.

### 2.5. Complexity Analysis

The time cost for the construction of TBSG contains three parts: 1) establishing Cover Tree, 2) building an approximate KNNG, 3) building TBSG based on Cover Tree and approximate KNNG. The complexity of part 1) is _O(c_<sup>6</sup>_n_log_nd_), where _c_ is the bounded expansion constant, _n_ is the cardinality and _d_ is the dimension. The cost of building Cover Tree is small in experiment. For part 2), we adopt the algorithm in Efanna[33], the complexity of which is _O(n_<sup>1.16</sup>). The time cost of part 3) is mainly used for neighbor(edge) selection. According to Algorithm 2, the complexity of determining whether a candidate node is a neighbor is _O(md_), where _m_ is the maximum of neighbor size. The total candidate set size is 2_Kn_, where _K_ is the neighbor size of KNNG. Therefore, the complexity of part 3) is _O(Kmdn_). The overall complexity of TBSG is _O(c_<sup>6</sup>_n_log_nd+n_<sup>1.16</sup>+_Kmdn_).

It is hard to estimate the search complexity of TBSG accurately, but according to our empirical study, the complexity is close to _O_(log_nd_).

## 3. Experiment

In this part, we discuss the details of the experiment, including datasets, compared algorithms and the method for evaluation.

