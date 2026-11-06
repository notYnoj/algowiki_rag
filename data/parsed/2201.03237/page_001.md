# Tree-based Search Graph for Approximate Nearest Neighbor Search

**Abstract**

Nearest neighbor search supports important applications in many domains, such as database, machine learning, computer vision. Since the computational cost for accurate search is too high, the community turned to the research of approximate nearest neighbor search (ANNS). Among them, graph-based algorithm is one of the most important branches. Research by Fu et al. shows that the algorithms based on Monotonic Search Network (MSNET), such as NSG and NSSG, have achieved the state-of-the-art search performance in efficiency. The MSNET is dedicated to achieving monotonic search with minimal out-degree of nodes to pursue high efficiency. However, the current MSNET designs did not optimize the probability of the monotonic search, and the lower bound of the probability is only 50%. If they fail in monotonic search stage, they have to suffer tremendous backtracking cost to achieve the required accuracy. This will cause performance problems in search efficiency. To address this problem, we propose (r,p)-MSNET, which achieves guaranteed probability on monotonic search. Due to the high building complexity of a strict (r,p)-MSNET, we propose TBSG, which is an approximation with low complexity. Experiments conducted on four million-scaled datasets show that TBSG yields better or comparable search performance than all recent state-of-the-art algorithms. Our code has

<sup>∗</sup>Corresponding author <sup>1</sup>Hunan University, Changsha, 410082, China; E-mail: fanxbin@hnu.edu.cn, xp- wang@hnu.edu.cn, xuelei@hnu.edu.cn <sup>2</sup>National University of Defense Technology, Changsha, 410073, China; E-mail: kailu@nudt.edu.cn <sup>3</sup>National Key Laboratory of Science and Technology on Information System Security, Beijing, China

Xiaobin Fan<sup>1</sup>, Xiaoping Wang<sup>1,∗</sup>, Kai Lu<sup>2</sup>, Lei Xue<sup>1</sup>, Jinjing Zhao<sup>3</sup>

