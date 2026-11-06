**Case 2:** Whenever _r_ and _n_ are not coprime, they have the greatest divisor _d_=gcd(_n,r_) in common. In that case, there exist _d_ cycles with _n/d_ elements each. Regardless of where cycles are started, elements from different cycles are always distinct. **Example:** If the array contains again 12 elements but should be rotated by a different offset of 3, then there are gcd(12,3)=3 cycles with 12/3=4 elements each, namely (0369)(14710)(25811). Such an example is visualized in Figure 1.

Since we have _d_ cycles with _n/d_ elements, each and all elements are different, so we rotate \(d\times n/d=n\) elements in total. Therefore, all elements are rotated correctly in optimal time and space. This algorithm was presented by Fletcher and Silver in 1965 and is often referred to as the “juggling algorithm” [13, p. 209].

There are several other rotation algorithms, such as the “triple reversal rotation” and more complex variations of it (e.g., Gries-Mills rotation, the Grail rotation, the Helix rotation or the Trinity rotation), which improve locality but at the cost of touching every element usually three times instead of only once. Although this sounds bad in theory, it can be beneficial in terms of practical performance on some architectures or certain input distributions. The presented rotation algorithm was chosen because it is not only simpler but also gives recurring good enough performance regardless of the architecture or given data distribution.

## 2.1.3 Optimizations

Although useful for a simplified understanding, we do not need to calculate this greatest common divisor for an efficient implementation. It should be pointed out that any cycle always ends at its starting position _s_. Thus, we can simply increase the starting position whenever we detect such a cycle’s end and proceed to the next cycle. We also do not need to calculate the number of cycles in advance because we know that all array elements are moved exactly once, either directly or indirectly through a single temporary variable (here `first`), to their final destination. A simple loop over all elements, only with an adjusted starting

r = 3 input: a
b c
d e
f g
h i
j k
1 0
1 5
n first cycle 1: a
b c
d e
f g
h i
j k
1 2
3 4
first cycle 2: d
b c
g e
f j
h i
a k
first cycle 3: d
e c
g h
f j
k i
a b
1 output: d
e f
g h
i j
k 1
a b
C

**Figure 1** Optimal algorithm to rotate a given array with 12 elements by an offset of 3

