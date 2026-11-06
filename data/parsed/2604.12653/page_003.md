<tbc>We can compute the transitive closure of a directed acyclic graph in \(O(n^\omega)\) time, where \(\omega<2.372\) is the exponent of fast matrix multiplication. Since \(\omega<2.5\), this additional step does not increase the running time of the above algorithms. But for the algorithms below, this does make a difference.

If _G_ is given as a partial order in memory, Van der Hoog and Rutschmann \[19\] achieve \(O(n^{1+\varepsilon})\) preprocessing time and \(O(\varepsilon^{-1}loge(G))\) sorting time, which is tight for this input model. If _G_ is given as a DAG, then we first compute the transitive closure, and then run their algorithm. In the two phase algorithmic framework, this implies an algorithm with \(O(n^\omega)\) preprocessing time that then sorts _X_ in _O_(log_e(G_)) comparisons and time. If we insist on _O_(log_e(G_)) sorting time, then this is the fastest known preprocessing time.

Haeupler, Hladík, Iacono, Rozhoň, Tarjan and Tětek \[14\] and van der Hoog, Rotenberg and Rutschmann \[30\] study the model where _G_ is given as a DAG. They design an algorithm with _O(m_) preprocessing time and _O_(log_e(G_)+_m_) sorting time. This is tight in terms of the _overall running time_. However, compared to previous algorithms, this does not achieve a sorting time of _O_(log_e(G_)). In this paper, we close this gap. We design an algorithm that preprocesses _G_ in _O(m_) time and then sorts _X_ in _O_(log_e(G_)) comparisons and time, which is tight. See  1.

## Further related work

In the geometric setting, algorithms with separate preprocessing and sorting phases have been extensively studied under the _preprocessing model of uncertainty_. Van der Hoog, Kostitsyna, Löffler and Speckmann \[28\] show that you can preprocess a set of intervals in _O(n_log_n_) time, and then, given an item from each interval, sort these items in _O_(log_e(G_)) time, where _G_ is the DAG induced by the intervals. Their result could be seen as the geometric analogue of sorting under partial information. They generalize this to two dimensions \[29\]. Held and Mitchell \[15\] show that you can preprocess a set of disjoint disks in _O(n_log_n_) time, and then, given a point from each disk compute some triangulation in linear time. In the same setting, you can also compute the Gabriel graph, Euclidean MST, Delaunay triangulation (Löffler and Snoeyink \[25\], Devillers \[8\]), or quad tree (Löffler and Mulzer \[23\]) in linear time after preprocessing; or a _k_- layer onion decomposition (Löffler and Mulzer \[24\]) in _O(n_log_k_) time after preprocessing. There are further generalizations to overlapping regions \[1\], regions of arbitrary shape \[32\], or points on lines \[11\].

\begin{tabular}{cccc}
Preprocessing _G_ & \multicolumn{2}{c}{Sorting _X_} & Source \\
Time & Comparisons & Time & \\
exponential & log_e(G_)+_O(n_) & _O_(log_e(G_)+_n_) & \[12, TCS’76\] \\
exponential & _O_(log_e(G_)) & _O_(log_e(G_)) & \[21, Order’84\] \\
_O(m_) & _O_(log_e(G_)) & poly(_n_) & \[20, S’92\] \\
_O(n_<sup>2.5</sup>) & _O_(log_e(G_)) & _O_(log_e(G_)+_n_) & \[4, S’10\] \\
\(O(n^\omega)\) & _O_(log_e(G_)) & _O_(log_e(G_)) & \[19, FOCS’24\] \\
_O(m_) & _O_(log_e(G_)) & _O_(log_e(G_)+_m_) & \[14, SODA’25\] \\
_O(m_) & _O_(log_e(G_)) & _O_(log_e(G_)+_m_) & \[30, SOSA’25\] \\
_O(m_) & _O_(log_e(G_)) & _O_(log_e(G_)) & This work \\
\end{tabular}

1: Previous algorithms for sorting under partial information, and our contribution. Non- optimal running times in red.

