We now continue by analyzing whether the number of pairs that block _M_<sub>1</sub> in P<sub>2</sub> and the number of necessary adjustments are correlated:

## Research Question II.

Is there a correlation between the number of blocking pairs of _M_<sub>1</sub> in P<sub>2</sub> and the minimum symmetric difference between _M_<sub>1</sub> and a stable matching in P<sub>2</sub>?

## Experimental Setup, Results, and Evaluation II.

For each of the three types of changes, we sampled 2000 STABLE MARRIAGE instances with 50 men and 50 women with random preferences collected in preference profile P<sub>1</sub>. For each such instance, we uniformly at random sampled a value \(r\in[0,0.2]\) and applied an _r_-fraction of changes to P<sub>1</sub> to obtain P<sub>2</sub>. Subsequently, we computed the men-optimal matching _M_<sub>1</sub> in P<sub>1</sub>, the set of pairs bp(_M_<sub>1</sub>,P<sub>2</sub>) that block _M_<sub>1</sub> in P<sub>2</sub>, and the stable matching _M_<sub>2</sub> in P<sub>2</sub> with minimum symmetric difference to _M_<sub>1</sub>.

After that, for each of the three types of changes, we computed the Pearson correlation coefficient between the fraction of pairs that block _M_<sub>1</sub> in P<sub>2</sub> and the minimum normalized symmetric difference between _M_<sub>1</sub> and a stable matching _M_<sub>2</sub> in P<sub>2</sub> for all 2000 instances created for this type of change. The Pearson correlation coefficient is a measure for the linear correlation between two quantities _x_ and _y_, where 1 means that _x_ and _y_ are perfectly linearly correlated, i.e., the relationship between _x_ and _y_ is _y=mx+b_ with _m\>_0. In contrast, -1 means that the relationship can be described as _y=mx+b_ with _m\<_0, while 0 means that there is no linear correlation between _x_ and _y_. Typically, a correlation between 0.4 and 0.69 is considered as a moderate correlation, while a correlation between 0.7 and 0.89 is considered as a strong correlation and a correlation between 0.9 and 1 as a very strong correlation \[Schober et al., 2018\]. For Reorder, the correlation coefficient is 0.8, for Delete the correlation coefficient is 0.55, and for Swap the correlation coefficient is 0.81. Thus, for all three types of changes there is a noticeable correlation, which is particularly strong for Swap and Reorder and a bit weaker for Delete. To get a feeling for the correlation, in Figure 7, for Reorder, we represent each instance by a point whose _x_-coordinate is the fraction of pairs that block _M_<sub>1</sub> in P<sub>2</sub>, whose _y_-coordinate is the minimum normalized symmetric difference between _M_<sub>1</sub> and a stable matching _M_<sub>2</sub> in P<sub>2</sub>, and whose color reflects the applied _r_-fraction of changes.

Examining Figure 7, it seems that the points in one color (that is, instances where a similar number<tbc>

Reorder
Mean
Delete
90th quantile
Swap
0.18
fraction of pairs that block M1 in P2
0.16
0.14
0.12
0.10
0.08
0.06
0.04
0.02
0.00
0.00
0.05
0.10
0.15
0.20
0.25
0.30
fraction of changes

[0,0.05]
(0.05,0.1]
(0.1,0.15]
(0.15,0.2]
0.8
0.6
M1 M2
0.4
0.2
0.0
0.00
0.01
0.02
0.03
0.04
0.05
10-2
fraction of blocking pairs

Figure 6: Fraction of man-woman pairs with non- empty preferences that block _M_<sub>1</sub> in P<sub>2</sub> for a varying fraction of change between P<sub>1</sub> and P<sub>2</sub>.

Figure 7: Relationship between (x) the fraction of man-woman pairs that block _M_<sub>1</sub> in P<sub>2</sub> and (y) the minimum symmetric difference between _M_<sub>1</sub> and a stable matching _M_<sub>2</sub> in P<sub>2</sub> for Reorder. Each point corresponds to one of 2000 instances and its color to the applied fraction of changes.

