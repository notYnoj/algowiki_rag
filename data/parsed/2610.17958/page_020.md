<tbc>70% or above (STRING’s high confidence threshold).  C.1 shows the input parameters for the selected datasets before edge filtering.

We selected the datasets from the STRING database because they are publicly available and are relatively big for modern standards in this application domain, making them well suited for our experiments.

For all datasets in  C.1, we removed nodes containing sequences with non-amino-acid letters (it is customary to denote an unknown amino acid by the capital letter `X`) along with their incident edges and isolated nodes. The resulting datasets of this procedure are shown in  5.1, and these were the datasets used in our experiments. Note that all networks in  C.1 and  5.1 are sparse.

_Artificial networks._ For RQ3, RQ4, and RQ5, we generated smaller artificial networks by sampling sequences from the H. sapiens I network, which contains the largest sequences on average. We then added edges uniformly at random until an edge-density threshold was satisfied and ensured that the constructed instances had no isolated nodes.

**C.2 Results for RQ2.**  C.2 shows the coverage of _S_<sub>Exact</sub> by _S_<sub>SEQ-SLIDER</sub> and _S_<sub>M-SLIDER</sub> across all datasets. We omitted the density plots for S. cerevisiae I and D. melanogaster in Figure 5.4 because _S_<sub>Exact</sub> was fully covered by _S_<sub>SEQ-SLIDER</sub> for these datasets (which can be verified in  C.2).

**C.3 Results for RQ3.**  C.3 shows the running time and peak RAM usage per thread of our exact algorithm on the datasets of  5.1.

\begin{tabular}{cccc}
Dataset & |_V_| & |_E_| & _N_ \\
E. coli & 4140 & 492,380 & 1,312,010 \\
S. cerevisiae I & 6538 & 1,412,421 & 2,906,015 \\
D. melanogaster & 13,577 & 2,516,980 & 7,423,206 \\
A. thaliana & 25,739 & 6,278,747 & 10,843,854 \\
H. sapiens I & 19,622 & 6,857,702 & 11,283,623 \\
S. cerevisiae II & 1620 & 9060 & 862,281 \\
H. sapiens II & 10,381 & 69,542 & 5,608,861 \\
\end{tabular}

C.1: Top: Parameters of datasets from STRING database. Bottom: Parameters of datasets from \[1\].

