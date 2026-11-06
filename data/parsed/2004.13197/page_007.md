Thus we get that the total number of permutations is at least \(\genfrac(){pt}{2}{n}{k}S(n,k)\), which is at least (_n/k)<sup>k</sup>k_<sup>_n-k_</sup>. Since red elements are already sorted, comparisons of cost _a_ are useless, and the cheapest available comparisons are those costing _b_. Thus we get a lower bound of \(\Omega(b(klog(n/k)+(n-k)logk))\), which equals \(\Omega(b(klogn+nlogk-2klogk))\) .

If \(k\le n/3\), \(nlogk-2klogk\ge\frac{n}{3}logk\), and we get the claimed lower bound. If _k\>n/_3, we claim that _bn_log_n_ is a lower bound, which matches our lower bound for this case. Consider the instance where red elements are sorted, _k_ blue representatives of each stripe are given (unsorted) and one is told that the remaining _n-k_ blue elements are all larger than the largest red elements. To finish the batched predecessor problem, there are at least \(\genfrac(){pt}{2}{n}{k}k!\) permutations to check (find where to place the representatives, find the order in which representatives should go). No comparison between red elements are useful, the cheapest available comparison costs _b_, so we get a lower bound of \(blog(\genfrac(){pt}{2}{n}{k}k!)\), which since _k\>n/_3, is \(\Omega(bnlogn)\).

Since we derived the lower bound on a constant number of instances of 2RAMSORT, we can claim a lower bound of the maximum complexity of these instances, which in turn is the same as the sum of the complexities in \(\Omega(.)\) notation, since we only have constantly many such instances.

**Upper bounds for the case** _a\<b\<c_**.** The algorithm proceeds in a similar fashion:

1. Sort the _n_ red elements using cost _a_ comparisons.<tbc>

2. Build a binary tree T_<sub>r</sub>_ on the sorted red elements. The algorithm also maintains a binary tree T_<sub>b</sub>_ (initially empty) on the set of discovered âĂIJborderâĂİ of red elements, i.e., the red elements which immediately precede and succeed a discovered stripe. A blue element is first sent down T_<sub>b</sub>_ to find whether it belongs to an already discovered stripe. If it does not belong to an already discovered stripe, it is bound to discover a new stripe, and it is sent down T_<sub>r</sub>_. The new bordering red elements are then inserted into T_<sub>b</sub>_. It is clear that only _k_ blue elements go down T_<sub>r</sub>_, whereas every blue element may go down T_<sub>b</sub>_, which has at most _k_ leaves. All the comparisons in this step are cost _b_.<tbc>

3. Sort the stripes of blue elements using type c comparisons.

One can easily verify that the running time of this algorithm matches the one in the theorem statement.

