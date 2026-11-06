`#define sort2(a,b) if ((t = (a) - (b)) \< 0) { (b) += t; (a) -= t); }`

`With 3-ops, an exchange of the central element will slide possible swaps by the outlying "wings"`

`#define op3(a,b,c,d) if (sort2(b,c)) else { sort2(a,b); sort2(c,d); }`

`These macros expand as in-line code, removing subroutine overhead and form the basic primitives used in software implementations of NICE networks.`

## 6 Higher Order Networks

`For` _N_ `odd, we explore methods of median finding, for` _N_ `even, we consider fully sorting networks.`

### 6.1 Sorting` _N_=5

`An efficient method for` _N_=5 `is elusive: network sizes which are a power of two show a high degree of symmetry, sizes` 2_<sup>n</sup>_+1 `must accommodate the new addition. Theory prescribes 7 comparisons (as` 5!=120_\<_128=2<sup>7</sup>`), and is realizable in careful practice. For CE implementations, a worst case figure of 10 links is an upper bound, this is the _triangle number T_(4)=4(4+1)/2 enumerating all pairwise comparisons of five elements. In practice, nine links is the minimum CE implementation. Exhaustive searching reveals that a simple elimination of one maximal element (four steps) followed by a sort4 (five links) gives the best sorting statistics:`

`Note that the final sort is of the style of that one in Figure 12(a), and not the one in Figure 13.`

9
6
3.133
0
1
X
2
X
3
X
4
X
5
X

`Figure 16: A 9-link network to sort 5 elements. The probabilities of swapping are:` <sup>1/2</sup> `at link 1,` <sup>1/3</sup> `at link 2,` <sup>1/4</sup> `at link 3,` <sup>1/5</sup> `at link 4,` <sup>1/3</sup> `at link 5,` <sup>5/12</sup> `at link 6,` <sup>2/5</sup> `at link 7,` <sup>2/5</sup> `at link 8,` <sup>3/10</sup> `at link 9. This results in` \(3^2/15=3.1\overline{3}\) `swaps on average.`

