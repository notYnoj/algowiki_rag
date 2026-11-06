## 5.3 Performance comparison

In each configuration, we calculate the average result across 100 instances for each algorithm. Specifically, for each algorithm and under each configuration, the average performance metrics reported in this study are computed over 100 instances using the following equations:

\(\text{Average number of singles / unassigned positions}=n-\frac{1}{|S|}\sum_{M_i\in S}|M_i|\) (1)

\(\text{Average SECost}=\frac{1}{|S|}\sum_{M_i\in S}\text{SECost}(M_i)\) (2)

\(\text{Average execution time}=\frac{1}{|I|}\sum_{i=1}^{|I|}\text{time}(i)\) (3)

where _I_ is the set of instances in the configuration, _M<sub>i</sub>_ is the resulting matching produced by the algorithm when solving instance _i_, and _S_ denote the set of stable matchings among these, i.e., \(S=\{M_i|M_i\text{is stable for}i=1,2,\cdots,|I|\}\).

Note that all local search algorithms used to compare the quality of the solution produced stable matches on all small-sized and large-sized instances, except that MCA solved only 99 of 100 instances in one configuration. For this reason, we did not report the percentage of stable matchings in the results.

An algorithm is deemed the "winner" in a configuration if its result is not worse than that of any other algorithm. To compare the performance of different algorithms, we count the number of wins and compute the overall average result across all configurations. Calculating the overall average result of an algorithm involves two steps. First, the result for each configuration is calculated by averaging the outcomes of 100 instances. Then, the results for each configuration are averaged to obtain the final overall result. These two metrics--the number of wins and the overall average--offer a comprehensive basis for comparing the performance of the algorithms across different configurations.

For the MAX-SMTI problem, we evaluate the solution quality of TBLS and TBLS- E by examining the matching size and the sex equality cost (SECost). These results are compared against those of AS, GSA2, GSM, LTIU, MCS, and PDB. Specifically, LTIU is built upon the SML2 algorithm detailed in Gelain et al (2013), and PDB is applied to obtain a stable matching after randomly breaking all the ties. Additionally, we compare the execution time of TBLS and TBLS-E with that of AS, LTIU, and MCS, as they are all heuristic search methods. For the MAX-HRT problem, we assess the solution quality of TBLS, focusing on the matching size, in comparison with ASBM, HA, HPA, HR, and MCA. Furthermore, we compare the execution time of TBLS with that of HR and MCA, since they all employ heuristic techniques. For both problems, we do not include approximation algorithms such as GSA2, HA, etc., in the execution time comparison, since they operate under fundamentally different assumptions and performance objectives compared with heuristic algorithms. The detailed results for each configuration presented in Sections 5.3.1 and 5.3.2 are provided in<tbc>

