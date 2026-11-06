such as (software) early termination as when reaching the threshold of maximum exchange are not cost effective: they must both count and test in order to detect this condition at a cost often greater than a few additional link comparisons.

The network depicted in Figure 13 also sheds light into the subtleties of conditional probability. While there are 4! = 24 possible inputs permutations, the first four links cannot each successively half the size of the solution space: 24 is not divisible by 2<sup>4</sup> = 16. While links 3 and 4 both execute independently with 50/50 exchange statistics, they are nonetheless conditionally bound. If link 3 does execute, then there is a <sup>2/3</sup> chance that link 4 does not, and vice versa. In effect, when "double winner" (max of all four) is found by exchanging element 2 with 3, previous losers to this element may be ascribed less demotion; they are more apt to retain a superior position and not trigger a link 4 exchange. Intuition aside, careful analysis of exchange statistics bears this all out.

Finally, we compare the network in Figure 13 to the following one found in [4, Figure 44]:

Note that this network does not compare as well as the one in Figure 13; it requires 5 swaps and the average number of swaps is higher as well.

## 5 Software Implementation

Reduction in total exchanges without the use of conditional directives is the greatest benefit of CONEX techniques. In the case of 2-ops and 3-ops a simple software addition can reduce the explicit cost of an unnecessary comparison:

`#define sort2(a,b) if ((a) < (b)) { (a) ^= (b); (b) ^= (a); (a) ^= (b) }`

`#define op2(a,b,c) if (sort2(a,b)) else sort2(b,c)`

`#define sort3(a,b,c) sort2(a,c); op2(a,b,c)`

in which the "else" elides a non-interfering CE element. The form shown above provides exchanges without resort to additional variables / registers. If we allow their inclusion the difference implicit in the first comparison can be retained to speed the body of the exchange, as shown elsewhere [5].

5
5
2.667
0
1
X
2
X
3
X
4
X

Figure 15: A 5-link sorting network for 4 elements taken from [4, Figure 44]. The last link has swap probability of <sup>2</sup>/3; all other links have swap probability of <sup>1</sup>/2.

