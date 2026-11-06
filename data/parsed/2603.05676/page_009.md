<tbc>merges. To do so, we next develop a stopping condition for walk-back PowerSort. We begin with the following observations about powers.

**Observation 2.** _Each power p is evenly spaced in the sequence. Two indices with the same power p\>_0 _are separated by at least n/_2_<sup>p</sup> elements._5

**Observation 3.** _The distance between any index with power p and the closest index with power less than p is n/_2<sup>_p_+1</sup> _on either side. Consequently, any range of n/_2<sup>_p_+1</sup> _indices contains either a power p or a power less than p._

Both follow directly from our description of powers implicitly held at indices.

**Observation 4.** _Any run with size at least n/_2_<sup>p</sup> has a power of at most p._

This observation follows from the fact that the right half of this run, which is at least size _n/_2<sup>_p_-1</sup>, is part of its power interval, and from the second part of Observation 3. Rearranging, we obtain the following.

**Observation 5.** _A run of size r must have power at most_ \(p\le log\frac{n}{r}\).

It would be convenient if we could show that long runs always have small powers and short runs always have large powers. However, short runs can have arbitrarily small powers if they appear at indices of small power. Such "lucky" short runs may incur a disproportionate walk-back cost for failed merge comparisons since their eventual merge cost could fail to be proportional to this walk-back cost. Despite this, we show that the overall walk-back cost over the entire main loop is small.

**Observation 6.** _Consider a merge of runs R_<sub>3</sub> _and R_<sub>2</sub> _in the merge step of the algorithm. The distance between the midpoints of R_<sub>3</sub> _and R_<sub>1</sub> _is at least n/_2<sup>_p_<sub>3</sub>+1</sup>_, where p_<sub>3</sub> _was the power of R_<sub>3</sub> _before the merge._

5 The distance here and in other observations may be off by at most one depending on the exact input size _n_.

R4
R3
R2
R1
I4
I3
I2
R3
R2
R1
I'4
I'2

Fig.4: Merging runs _R_<sub>2</sub> and _R_<sub>3</sub> causes _I_<sub>2</sub> and _I_<sub>4</sub> to extend into what used to be _I_<sub>3</sub>. Nevertheless, when _R_<sub>2</sub> and _R_<sub>3</sub> are merged, _p_<sub>3</sub>_\>p_<sub>2</sub> and \(p_3\ge p_4\). Therefore, the powers of \(I'_4\) and \(I'_2\) do not change.

