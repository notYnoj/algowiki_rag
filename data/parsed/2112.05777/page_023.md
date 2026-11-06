of changes have been applied) exhibit a weaker correlation than the collection of all points. In fact, for Reorder, while for instances with a change between \[0,0.05\] the correlation coefficient is 0.62, it is only 0.44 for instances from the interval (0.05,0.1\], 0.39 for (0.1,0.15\], and 0.42 for (0.15,0.2\]. It is quite remarkable that for all four groups the correlation coefficient is (significantly) below the overall correlation coefficient and, so far, we have no explanation for this. For the two other types of changes a similar but less strong effect is present.

## 6.4 Almost Stable Marriage

As featured in Section 4, we now analyze the trade-off between the number of pairs that are allowed to block _M_<sub>2</sub> and the minimum symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub>.

### Experimental Setup I.

For our three different types of changes, for \(r\in\{0,0.01,0.02,\cdots,0.3\}\), and for \(\beta\in\{0,0.005,0.05\}\), as in Section 6.2.1 we prepared 200 instances consisting of 50 men and 50 women with random preferences collected in P<sub>1</sub> and P<sub>1</sub> and P<sub>2</sub> differ in an uniformly at random sampled _r_-fraction of all possible changes. Then, we computed the minimum symmetric difference between _M_<sub>1</sub> and a matching _M_<sub>2</sub> in P<sub>2</sub> for which at most a \(\beta\)-fraction of all \(50\cdot 50\) man-woman pairs is blocking. Figure 8 shows the results of this experiment.<sup>6</sup>

### Evaluation I.

We observe that independent of the type and fraction of change, allowing for few blocking pairs for _M_<sub>2</sub> enables a significantly larger overlap of _M_<sub>2</sub> with _M_<sub>1</sub>. That is, allowing for a 0.005 fraction of pairs to be blocking decreases the average normalized symmetric difference by around 0.2. We also examined the effect of doubling the fraction of blocking pairs and allowing for a 0.01 fraction, which gives an additional decrease by 0.1. If we allow for a 0.05 fraction of pairs to be blocking, then, for Swap and Reorder, until a 0.2 fraction of changes, _M_<sub>2</sub> can be chosen to be almost identical to _M_<sub>1</sub>.

<sup>6</sup>The _y_-axis in Figure 8 is labeled differently than in the previous figures: Here, we divide \(|M_1\triangle M_2|\) by the size of a stable matching in P<sub>1</sub> plus the size of a stable matching in P<sub>2</sub>. As all stable matchings have the same size, this is the same as \(\frac{|M_1\triangle M_2|}{|M_1|+|M_2|}\) if _M_<sub>2</sub> is a stable matching; however, different almost stable matchings may have different sizes.

Reorder Delete Swap
No blocking pairs Almost 0.005 Almost 0.05
0.8
0.6
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

Reorder Swap
Delete
0.6
0.5
0.4
0.3
0.2
0.1
0.0
0.0
0.2
0.4
0.6
0.8
1.0
fraction of allowed blocking pairs

Figure 8: Average normalized symmetric difference between _M_<sub>1</sub> and a matching _M_<sub>2</sub> in P<sub>2</sub> with at most a given number of blocking pairs for a varying fraction of change between P<sub>1</sub> and P<sub>2</sub>.

Figure 9: Relationship between (x) the fraction of the number of pairs that block _M_<sub>1</sub> in P<sub>2</sub> that are allowed to block _M_<sub>2</sub> and (y) the symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub>.

