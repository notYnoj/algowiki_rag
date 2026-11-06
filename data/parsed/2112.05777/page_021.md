experiment from Figure 2a for these two types of changes and display the results in Figure 5. The reason why we do not explicitly consider these two types of changes in our other experiments is that Reorder (inverse) produces results similar to Reorder (typically and intuitively requiring few more adjustments) and Add produces results similar to Delete. This effect is also visible in Figure 5.

## 6.3 Correlation Between the Number of Blocking Pairs of _M_<sub>1</sub> in P<sub>2</sub> and the Symmetric Difference Between _M_<sub>1</sub> and _M_<sub>2</sub>

Motivated by the hypothesis that in practice a once implemented matching may not be changed even if the instance slightly changes, we ask the following question:

### Research Question I.

By how many pairs is matching _M_<sub>1</sub> blocked in P<sub>2</sub> if more and more changes are performed?

### Experimental Setup I.

For each of the three considered types of changes, for \(r\in\{0,0.01,0.02,\dots,0.3\}\), we sampled 1000 STABLE MARRIAGE instances with 50 men and 50 women with random preferences collected in P<sub>1</sub>. For each of these instances, we computed as _M_<sub>1</sub> the men- optimal matching and applied an _r_-fraction of all possible changes of the considered type to P<sub>1</sub> to obtain preference profile P<sub>2</sub>. Subsequently, we computed the set bp(_M_<sub>1</sub>,P<sub>2</sub>) of pairs that block matching _M_<sub>1</sub> in instance P<sub>2</sub>. In Figure 6, we depict the average and 90th quantile of the fraction of man-woman pairs that block _M_<sub>1</sub> in P<sub>2</sub> depending on the fraction of applied changes.

### Evaluation I.

Comparing the results from Figure 6 to the results from Figure 2a, several things stand out. First, examining the range \[0,0.05\] of changes, there are only "few" blocking pairs (around a 0.02 fraction of all pairs), which (as observed in Section 6.2.1 ) are nevertheless in most cases enough to make it necessary to fundamentally restructure the given matching _M_<sub>1</sub>. Second, the ordering of Delete and Swap is reversed here compared to the needed adjustments. Third, while the fraction of pairs that block _M_<sub>1</sub> in P<sub>2</sub> constantly grows--nevertheless always staying on a surprisingly low level--the minimum symmetric difference between _M_<sub>1</sub> and a stable matching in P<sub>2</sub> grows significantly slower after a certain fraction of changes have been applied (see Figure 2a).

Reorder
Best
Reorder (Inverse)
Gale-Shapley
Delete
Worst
Add
1.0
0.8
0.6
M1 M2
M1 + M2
0.4
0.2
0.0
0.00
0.05
0.10
0.15
0.20
0.25
0.30
fraction of changes

Figure 5: For different types of changes and ways to compute _M_<sub>2</sub>, average normalized symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub> for a varying fraction of change between P<sub>1</sub> and P<sub>2</sub> when agents have random preferences.

