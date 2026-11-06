### Software Implementation

Reduction in total exchanges without the use of conditional directives is the greatest benefit of CONEX techniques. In the case of 2-ops and 3-ops a simple software addition can reduce the explicit cost of an unnecessary comparison:

`#define sort2(a,b) if ((a) < (b)) { (a) ^= (b); (b) ^= (a); (a) ^= (b) }`

`#define op2(a,b,c) if (sort2(a,b)) else sort2(b,c)`

`#define sort3(a,b,c) sort2(a,c); op2(a,b,c)`

in which the "else" elides a non-interfering CE element. The form shown above provides exchanges without resort to additional variables / registers. If we allow their inclusion the difference implicit in the first comparison can be retained to speed the body of the exchange, as shown elsewhere [PaehGems]:

`#define sort2(a,b) if ((t = (a) - (b)) < 0) { (b) += t; (a) -= t); }`

With 3-ops, an exchange of the central element will slide possible swaps by the outlying "wings"

`#define op3(a,b,c,d) if (sort2(b,c)) else { sort2(a,b); sort2(c,d); }`

These macros expand as inline code, removing subroutine overhead and form the basic primitives used in software implementations of NICE networks.

### Higher Order Networks

For N odd, we explore methods of median finding, for N even, we consider fully sorting networks.

### Sorting N=5

An efficient method for N=5 is elusive: network sizes which are a power of two show a high degree of symmetry, sizes 2^N+1 must accommodate the new addition. Theory prescribes 7 comparisons, as (5! = 120) < (128 = 2^7) and is realizable in careful practice. For CE implementations, a worst case figure of 10 links is an upper bound, this is the triangle number T(4) enumerating all pairwise comparisons of five elements. In practice, nine links is the minimum CE implementation. Exhaustive searching reveals that a simple elimination of one maximal element (four steps) followed by a sort4 (five links) gives the best sorting statistics:

`+------------------------------+` `|9 6 3.133` `|` `+------------------------------+` `| 1 >+----------------------------+-----------------------------> x` `|` `| 2 >-|+-----------------------------|++-----------------------------> x` `|` `| 3 >-|--|+-----------------------------|+------------+-> x` `|` `| 4 >-|--|--|+----------------------------+-------------> x` `|`

