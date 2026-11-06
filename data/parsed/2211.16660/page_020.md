• There is a natural question that arises from another possible approach to proving Theorem 1.2. Define the _directed edit distance_ of two strings _x,y_ to be the number of edits needed to get from _x_ to _y_, where insertions cost 0 and deletions (and substitutions) cost 1. Equivalently, \(\vec{\Delta}_\text{edit}(x,y):=|x|-\text{LCS}(x,y)\). When the strings are equal length, the directed edit distance is simply half the edit distance. A constant-factor approximation of directed edit distance in almost-linear time would immediately imply Theorem 3.2 and thus Theorem 1.2. This suggest the following question, which may be of independent interest.<tbc>

<tbc>**Question 7.1.** Is there an almost-linear time constant-factor approximation of the directed edit distance?<tbc>

<tbc>We note that \(\vec{\Delta}_\text{edit}(x,y)\) is _not_ a metric. Indeed, it is not even symmetric<sup>3</sup>, and it does not satisfy the triangle inequality. Thus, the existing edit distance approximation algorithms \[CDG<sup>+</sup>20, BR20, KS20, AN20\], which rely heavily on the triangle inequality, do not seem to immediately apply to directed edit distance. On the other hand, directed edit distance does satisfy a "directed triangle inequality": for strings _x,y,z_, we have \(\vec{\Delta}_\text{edit}(x,z)\le\vec{\Delta}_\text{edit}(x,y)+\vec{\Delta}_\text{edit}(y,z)\). This gives some hope that fast approximation algorithms exist.

## 8 Acknowledgements

We thank Saeed Seddighin for introducing us to the question of approximating binary LCS and for suggesting its potential connection to the deletion codes bound \[GHL22\]. We thank Negev Shekel Nosatzki for helpful discussions about edit-distance algorithms. We thank Shyan Akmal and Virginia Vassilevska-Williams for helpful discussions on their work \[AW21\]. We thank Aviad Rubinstein for helpful feedback. We thank Venkatesan Guruswami for helpful feedback and encouragement.

## References

<sup>3</sup>\(\vec{\Delta}_\text{edit}(0011,00)=2\text{but}\vec{\Delta}_\text{edit}(00,0011)=0\)

