can be explained.

• **True Positives**(TP): Number of positions in both known sites as well as predicted sites.<tbc>

• **False Positives**(FP): Number of positions in predicted sites which are not present in known sites<tbc>

• **True Negatives**(TN): Number of positions which are neither in known sites nor in predicted sites.<tbc>

• **False Negatives**(FN): Number of positions that are in known sites but not in predicted sites.<tbc>

• **Sensitivity**(Sn): It represents the fraction of sites that were correctly predicted.<tbc>

• **Sensitivity**(Sp): It represents the fraction of non-sites that were correct<tbc>

• **Positive Predictive Value**(PPV): It represents the fraction of predicted sites that are known.

The Sn, Sp and PPV measures are computed as follows (x can either be n for nucleotide or s for site):

**1** \(xSn=\frac{xTP}{xTP+xFN}\)

**2** \(xSp=\frac{xTN}{xTP+xFP}\)

**3** \(xPPV=\frac{xTP}{xTP+xFP}\)

To compute the value for _sSn_, we label a site to be a true positive if there is at least a 25% overlap between the predicted and the known sites.

Nucleotide level **Performance Coefficient** is defined as:

**4** \(nPC=\frac{nTP}{nTP+nFN+nFP}\)

Nucleotide level **Correlation Coefficient** is defined as:

**5** \(NCC=\frac{nTP.nTN-nFN.nFP}{(nTP+nFN)(nTN+nFP)(nTP+nFP)(nTN+nFN)}\)

In this paper we compare the performance of PMSprune with the above 13 algorithms (indirectly) and the DME algorithm on the Benchmark datasets in \[TLB<sup>+</sup>\]. Since a comparison of the above 13 algorithms are already available, a comparison of PMSprune with these 13 algorithms has been done using the results reported in \[TLB<sup>+</sup>\]

**Definition 2.1.** \(d(x,S_i)=min_{\forall y\in S_i}d(x,y)\)_, where y is an_ \(\ell\)_-mer in S<sub>i</sub> and d(x,y_) _is Hamming Distance between x and y._

**Step 1** Find PMS Motifs.

Let _M_ be the list of predicted Motifs from PMS algorithm such that length of _M_, |_M_|=_m_.<tbc>

