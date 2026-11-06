<tbc>Dor, Halperin and Zwick \[DHZ00\] showed that obtaining \((2-\varepsilon)\)-APSP is as hard as Boolean Matrix Multiplication. Consequently, obtaining a nearly quadratic algorithm for \(\alpha\)-APSP with \(\alpha<2\) would imply a major breakthrough in matrix multiplication (i.e., \(\omega=2\)). But what about the case when \(\alpha=2\) or 2-APSP? The only natural lower bound is the output size, which is \(\Theta(n^2)\). Thus, any 2-APSP algorithm requires \(\Omega(n^2)\) time. Since no stronger lower bound is known, an important problem is to design a 2-APSP algorithm that runs in O(n<sup>2</sup>) time.

We will see later that purely additive APSP algorithms are used to obtain 2-APSP. We now describe results for purely additive APSP. Aingworth, Chekuri, Indyk and Motwani \[ACIM99\] designed a \(\tilde{\mathcal{O}}(n^{2.5})\) time algorithm for +2-APSP. Later, Dor, Halperin and Zwick \[DHZ00\] reduced the running time to \(\tilde{\mathcal{O}}(\mathrm{min}\{n^{3/2}m^{1/2},n^{7/3}\})\). Using FMM, Deng, Kirkpatrick, Rong, Williams and Zhong \[DKR<sup>+</sup>22\] improved the running time to O(n<sup>2.259</sup>) (using an improved result of \[Dür23\]). Very recently, Jin, Kirkpatrick, Stawarz and Williams \[JKSV26\], again using FMM, improved this running time to O(n<sup>2.2255</sup>).

We now describe a simple relation that yields a 2-APSP from a purely additive approximation.

**Observation 1.1.** _A_ +k-APSP _implies a_ 2-APSP _for all pairs of vertices at distance at least_ k.

Since we can find a path of length one in O(m) time, the above observation translates the +2-APSP from the previous paragraph to 2-APSP. However, all these algorithms require \(\omega(n^2)\) time. Fortunately, there are +k-APSP algorithms with better running times. Dor, Halperin and Zwick \[DHZ00\] designed a +k-APSP algorithm with running time \(\tilde{\mathcal{O}}(\mathrm{min}\{n^{2-\frac{2}{k+2}}m^\frac{2}{k+2},n^{2+\frac{2}{3k-2}}\})\). Saha and Ye \[SY24\] recently used FMM to improve the running time. However, the worst case running time in these results remain \(\tilde{\mathcal{O}}(n^{2+\mathrm{O}(\frac{1}{k})})\). If k=logn, then the running time becomes \(\tilde{\mathcal{O}}(n^2)\) and the algorithm works for all pairs of vertices at a distance at least O(logn). Until recently, this was the best result for 2-APSP with the running time \(\tilde{\mathcal{O}}(n^2)\).

Gupta \[Gup25\] designed an algorithm for 2-APSP that runs in \(\tilde{\mathcal{O}}(n^{2+1/k})\) time and works for vertices at distance at least O(logk). If k=logn, then the running time becomes \(\tilde{\mathcal{O}}(n^2)\), and the algorithm works for all pairs at a distance at least O(loglogn). An important open problem in this field is to design a 2-APSP algorithm that works for all pairs and runs in O(n<sup>2</sup>) time or nearly optimal \(\tilde{\mathcal{O}}(n^2)\) time. We nearly resolve this problem by showing the following theorem.

**Theorem 1.2.** _There exists a randomized algorithm that, with high probability, runs in_ \(\tilde{\mathcal{O}}(n^2)\) _time and computes_ 2-APSP _for all pairs of vertices at distance at least_ c_, where_ \(\mathrm{c}\unknown 0\) _is a constant._

We do not attempt to optimize the constant, though we achieve \(\mathrm{c}\unknown 906\). Our approach builds on the combinatorial techniques developed by Gupta \[Gup25\]. Our algorithm also builds some combinatorial techniques but a crucial step of our algorithm uses FMM. The primary contribution of our work is showing how to combine these combinatorial techniques with FMM.

## 1.1 Other related results

There is another class of algorithms that do not use Theorem 1.1 and compute 2-APSP directly. These algorithms work for all pairs of vertices. Cohen and Zwick \[CZ01\] designed an \(\tilde{\mathcal{O}}(n^{3/2}m^{1/2})\) time algorithm for 2-APSP. Baswana and Kavitha \[BK06\] achieved a running time of \(\tilde{\mathcal{O}}(m\sqrt{n}+n^2)\). Roditty \[Rod23\] designed a combinatorial algorithm for 2-APSP in \(\tilde{\mathcal{O}}(n^{2.25})\) time. All of the above algorithms are combinatorial in nature. Using FMM, Dory, Forster, Kirkpatrick, Nazari, Williams, and Vos \[DFK<sup>+</sup>24\] and Saha and Ye \[SY24\] improved the running time to \(\tilde{\mathcal{O}}(n^{2.031})\). There are many combinatorial algorithms \[BK07, Som16, Knu17, PR10\] that compute a (2,1)-APSP in \(\tilde{\mathcal{O}}(n^2)\) time.

### Weighted graphs

The algorithms of \[CZ01, BK06\] work for weighted graphs. The authors \[CZ01, BK06\] also designed a 3-APSP algorithm that runs in \(\tilde{\mathcal{O}}(n^2)\) time. Kavitha \[Kav12\] designed a \((2+\varepsilon)\)-APSP algorithm for<tbc>

