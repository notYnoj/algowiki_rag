<tbc>are slightly better than the ones we present here, but which are significantly more complicated. We intentionally did not include them in this paper. See also the discussion in Section 6 and footnote 10.

### Organization.

In Section 2 we give the main matrix algorithm. In Section 3 we derive the algorithms for Exact Triangle, 3SUM, and APSP from it, by using or slightly modifying known reductions. In Section 4 we give the data structure version of our matrix algorithm, proving Theorems 1 and 3. In Section 5 we present reductions to achieve the other algorithmic results discussed above. Finally, in Section 6 we discuss future directions.

## 2 Quickly computing certain entries of a thin matrix product

We now present our main new algorithm, for computing a subset of the output entries of a thin matrix product. We call such a matrix product _thin_ since the input matrices are highly rectangular. We work in the standard word RAM model with _O_(log_N_)-bit words, and thus count operations on _O_(log_N_)-bit integers.

**Theorem 5.** _Let_ \(D\ge 4\) _be a power of four and_ \(N\ge D^{18}\)_. Given as input matrices_ \(X\in\mathbb{Z}^{N\times D}\) _and_ \(Y\in\mathbb{Z}^{D\times N}\)_, whose entries are integers of absolute value at most N_<sup>_O_(1)</sup>_, as well as a set W of at most_ \(N^2/\sqrt{D}\) _positions of an_ \(N\times N\) _matrix, the entries_ (_XY_)\[_I,J_\], \((I,J)\in W\)_, can be computed deterministically in time O(N_<sup>2</sup>log<sup>2</sup>_D/D_<sup>1/18</sup>).

We call the positions in _W_, and the entries of _XY_ at them, _wanted_. We emphasize that _X,Y_ , and _XY_ may be arbitrary dense matrices, and no structure is assumed about the set _W_ other than its size \(|W|\le N^2/\sqrt{D}\).

We have aimed to present this section in a way that is accessible to nonexperts. Some details in Theorem 5, such as the exponent 18, are chosen to simplify the presentation in this section while still proving a version sufficient to refute the 3SUM and APSP hypotheses. Later, in Section 4, we present a stronger data structure version that has improved parameter trade-offs.

Notably, while the language of tensors and bilinear complexity naturally describes much of our algorithm and the prior work it builds on, we deliberately avoid that language here. This is in part so that a reader unfamiliar with that background may still follow, but also because our arguments here will focus on sparsity and combinatorial properties of our algorithms and algebraic identities that are often intentionally abstracted away in tensor language.

Sections 2.1-2.3 present an exposition of the relevant prior work that we directly build on, especially Strassen \[Str69\], Schönhage \[Sch81\], and Coppersmith \[Cop82\], and no prior understanding of those works is assumed. The main new idea of this paper is then presented in Section 2.4.

### Technique overview.

Strassen’s algorithm multiplies matrices by applying a small identity (seven products for multiplying \(2\times 2\) matrices) recursively. In that algorithm, the multiplications happen at the leaves of a recursion tree, and the additions that prepare the leaves (the "encoding phase") and assemble the result (the "decoding phase") are comparatively cheap. We do the same with an identity of Schönhage that computes, simultaneously, two small rectangular matrix products. Applied at _L_ levels of recursion, the identity computes 2_<sup>L</sup>_ matrix products at once. In order to multiply _X_ and _Y_ using this, we cut them into smaller blocks, and then simultaneously multiply many pairs of blocks using Schönhage’s identity (Section 2.3).

