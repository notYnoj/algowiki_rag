### 4.4. Complexity

In order to effectively evaluate the relationship between the index complexity and the size of dataset, we split the original datasets into subsets with different size and build indices on them with same parameters. Later, we use indexes above to conduct search using Algorithm 1 with same query set and equal size of result pool. We carried out the above experiments on three datasets with very similar scales: Sift, Gist and Glove. We record the time cost for indexing and searching. The result is showed in Figure 9.

The result shows that the index complexity of TBSG fits well with _O(n_). The search complexity fits well with _O_((log_n)<sup>v</sup>_) where _v_ is a small constant.

## 5. Conclusions

In this paper, we analyse and find that the current MSNET designs did not optimize the probability of the monotonic search, and the lower bound of the probability is only 50%. To better match the query scenarios, we propose (_r,p_)- MSNET, which achieves monotonic search with the probability at least _p_ when the distance between query point and nearest neighbor is smaller than _r_. By adjusting the value of _p_, we can balance the length of search path and average out-degree of nodes to further improve the efficiency. Due to the high index complexity of a strict (_r,p_)-MSNET, we propose TBSG. Experiment conducted on several million-scaled datasets show that TBSG yields better or comparable search performance than all recent state-of-the-art algorithms.

## 6. Appendix

### 6.1. Proof1

We define the point set \(\{Q:Q\in R_d\cap\delta(B,Q)\le r\cap\Pi_\overrightarrow{AC}\overrightarrow{BQ}>-rcos\frac{\varphi}{2}\}\) as _PS_<sub>1</sub>, and the corresponding region as _Reg_<sub>1</sub>. Define the point set \(\{Q:Q\in R_d\cap\delta(B,Q)\le r\cap<\overrightarrow{AC},\overrightarrow{BQ}><\pi-\frac{\varphi}{2}\}\) as _PS_<sub>2</sub> where \(<\overrightarrow{AC},\overrightarrow{BQ}>\) is the angle between \(\overrightarrow{AC}\) and \(\overrightarrow{BQ}\), and the corresponding region as _Reg_<sub>2</sub>. Define the<tbc>

