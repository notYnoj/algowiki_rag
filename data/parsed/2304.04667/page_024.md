the total \(\tilde{O}(n)\) instances in all recursion trees, the probability of having at least one instance that takes more than 4log_n_ attempts until a successful choice of _p_ is bounded by 1_/n_<sup>2</sup>.

We now turn our attention to bounding the total number of Max-Flow queries. The total number of queries performed for pairs in step 1, i.e. where both nodes have degrees at least \(n'/(20log_{4/3}n)\), in a single instance \(V'\) is at most:

\(|V'_H|^2=|\{u\in V':\alpha(u)>|V'|/(20log_{4/3}n)\}|^2\le\sum_{u\in V'_H}\alpha(u)20log_{4/3}n\le\alpha(V'_H)\cdot 20log_{4/3}n.\)

The total number of queries performed in steps 3 and 6 in one instance \(V'\) is at most<tbc>

\(|V'|+\sum_{u\in V^\prime}\alpha(p,u)=|V'|+\alpha(V').\)

<tbc>Thus, the total number of queries performed in one depth _i_ is

\(\sum_{V^\prime\text{in depth}i}\left(\alpha(V'_H)\cdot 20log_{4/3}n+|V'|+\alpha(V')\right)\le\alpha(V)\cdot 20log_{4/3}n+n+\alpha(V)\le\tilde{O}(\alpha(V)),\)

and summing over all depths, repetitions, and trees, we get a total number of Max-Flow queries of \(t_{pq}(m)=\tilde{O}(\alpha(V))\). Note that most of the time spent outside of Max-Flow calls is in steps 3 and 4, and it is bounded by _O(n_) per cut computed, thus a total of \(t_{po}(m)=\tilde{O}(\alpha(V)n)\), as required.

### Space usage

We aim to bound the total space used by the data structure, focusing on the more demanding steps and beginning with item 1 of Theorem 3.1.

• To bound the space occupied by cuts in both step 1 and step 6, we focus on a \[_k,_2_k_) range of separator sizes each time, incurring an _O_(log_n_) factor in the space bound. On one hand, at most \((\alpha(V)/k)^2\) node pairs can have separators with size in \[_k,_2_k_), and on the other hand, as demonstrated earlier, at most \(\tilde{O}(\alpha(V))\) reinforcement queries are made throughout the algorithm. This yields a space bound of<tbc>

<tbc>\(\tilde{O}\left(min\left\{(\alpha(V)/k)^2,\alpha(V)\right\}\cdot 2k\right)\le\tilde{O}(\alpha(V)^{3/2}).\)<tbc>

• For cuts in step 3, the occupied space is at most \(\tilde{O}\left(\sum_{V^\prime}\alpha(V')+|V'|\right)\le\tilde{O}(\alpha(V))\).

Altogether, the bound is \(\tilde{O}(\alpha(V)^{3/2})\), as required.

In order to obtain the data structure 2 of Theorem 3.1, we do not keep the separators from steps 1 and 6 as they were only used as witnesses. The total space bound is thus at most \(\tilde{O}(\alpha(V))\), as required.

## 3.2 Our Reinforced Tree-Like Data Structure: A Las Vegas Version

In this section, we present a Las Vegas version of our algorithm, focusing on the differences from the Monte Carlo version presented above.

