define the set of allowed index combinations to be:

\(S=\{s=(s_A,s_B):s_A\in S_A,s_B\in S_B,s_A\cup s_B=I,s_A\cap s_B\neq\emptyset\}\)

Assume that this set is given an order and can therefore be indexed by integers between 1 and |_S_|.

Using the above index list, we can divide \(C'\) into smaller regions \(R'_s\) indexed by the elements \(s\in S\), where

\(R'_{s=(s_A,s_B)}=\left\{\begin{array}{ c c }
a_j<u'_j<b_j & \text{if}j\in s_A\cap s_B \\
(u'_1,\cdots,u'_N):b_j<u'_j<1 & \text{if}j\in s_A\backslash s_B \\
0<u'_j<a_j & \text{if}j\in s_B\backslash s_A
\end{array}\right\}.\)

Thus, \(R'_s\) is the region of the unit hypercube in which all _X<sub>i</sub>_ for \(i\in s_A\) are greater than _A_ and all _X<sub>i</sub>_ for \(i\in s_B\) are less than _B_. It is easy to see that \(R'_{s_1}\) and \(R'_{s_2}\) are non-overlapping for \(s_1\neq s_2\) since changing any index’s presence in either set changes the allowed range of values. Additionally, the union of these regions is the total restricted region \(C'\) since there are no further combinations which give us a _k_-th order statistic in the allowed range of values.

In defining the regions \(R_s\subset C\) corresponding to the \(R'_s\), we ensure that the probability distribution after the mapping is uniform over \(C'\) to conduct inverse transform sampling. The probability densities over both _C_ and \(C'\) follow a multivariate uniform distribution. Because the density function is inversely proportional to the volume, using our mapping we can maintain the relative volumes of the regions being mapped to one another. Then the volume of the regions in _C_, _V<sub>R<sub>s</sub></sub>_, are equal to the normalized volumes in the restricted regions in \(C'\), _f<sub>s</sub>_. The normalizing of the volumes begins with the un-normalized volume of \(R'_s\), \(V_{R_s^\prime}\), which is given by

\(V_{R_s^\prime}=\prod_{l\in s_A\cap s_B}(b_l-a_l)\prod_{m\in s_A\backslash s_B}(1-b_m)\prod_{n\in s_B\backslash s_A}a_n\)

Then, the normalized volume is the fraction of the allowed volume occupied by the region \(R'_s\) and is given by \(f_s=\frac{V_{R_s^\prime}}{\sum_{\sigma\in S}V_{R_\sigma^\prime}}\).

Then, we can define the regions _R<sub>s</sub>_ in _C_ so that they have volume _f<sub>s</sub>_

\(R_s=\left\{\begin{array}{ c c }
0<u_j<1 & \text{if}j<N \\
(u_1,\cdots,u_N):\sum_{l=1}^{s-1}f_l<u_j<\sum_{l=1}^sf_l & \text{if}j=N
\end{array}\right\}\)

Clearly, our region _R<sub>s</sub>_ has volume _f<sub>s</sub>_, and, similarly to \(R'_s\), _R_<sub>_s_<sub>1</sub></sub> and _R_<sub>_s_<sub>2</sub></sub> are non-overlapping and the union of all of the _R<sub>s</sub>_ comprises the whole space _C_.

