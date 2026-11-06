# Algorithms for new types of fair stable matchings

**Frances Cooper**<br> School of Computing Science, University of Glasgow, Glasgow, Scotland, UK<br> `https://www.francescooper.net`<br> f.cooper.1@research.gla.ac.uk

**David Manlove**<br> School of Computing Science, University of Glasgow, Glasgow, Scotland, UK<br> `http://www.dcs.gla.ac.uk/~davidm`<br> david.manlove@glasgow.ac.uk

**Abstract**

We study the problem of finding "fair" stable matchings in the _Stable Marriage problem with Incomplete lists_ (smi). For an instance _I_ of smi there may be many stable matchings, providing significantly different outcomes for the sets of men and women. We introduce two new notions of fairness in smi. Firstly, a _regret-equal stable matching_ minimises the difference in ranks of a worst-off man and a worst-off woman, among all stable matchings. Secondly, a _min-regret sum stable matching_ minimises the sum of ranks of a worst-off man and a worst-off woman, among all stable matchings. We present two new efficient algorithms to find stable matchings of these types. Firstly, the _Regret-Equal Degree Iteration Algorithm_ finds a regret-equal stable matching in _O(d_<sub>0</sub>_nm_) time, where _d_<sub>0</sub> is the absolute difference in ranks between a worst-off man and a worst-off woman in the man-optimal stable matching, _n_ is the number of men or women, and _m_ is the total length of all preference lists. Secondly, the _Min-Regret Sum Algorithm_ finds a min-regret sum stable matching in _O(d<sub>s</sub>m_) time, where _d<sub>s</sub>_ is the difference in the ranks between a worst-off man in each of the woman-optimal and man-optimal stable matchings. Experiments to compare several types of fair optimal stable matchings were conducted and show that the Regret-Equal Degree Iteration Algorithm produces matchings that are competitive with respect to other fairness objectives. On the other hand, existing types of "fair" stable matchings did not provide as close an approximation to regret-equal stable matchings.

**2012 ACM Subject Classification** Theory of computation \(\rightarrow\) Design and analysis of algorithms

**Keywords and phrases** Stable marriage; Algorithms; Optimality; Fair stable matchings; Regret- equality; Min-regret sum

**Related Version** arxiv.org/abs/2001.10875

**Supplement Material** zenodo.org/record/3630383 and zenodo.org/record/3630349

**Funding** _Frances Cooper_: Supported by an Engineering and Physical Sciences Research Council Doctoral Training Account EP/N509668/1

_David Manlove_: Supported by Engineering and Physical Sciences Research Council grant EP/P028306/1

## 1 Introduction

### 1.1 Background

The Stable Marriage problem (sm) was first introduced by Gale and Shapley [5] in their seminal paper "College Admissions and the Stability of Marriage", and comprises a set of men and a set of women, where each man has a strict preference over all women and vice versa. A _matching_ in this setting is an assignment of men to women such that no man or woman is multiply assigned. A _stable matching_ is then a matching in which there is no man-woman pair who would rather be assigned to each other than to their assigned partners.





