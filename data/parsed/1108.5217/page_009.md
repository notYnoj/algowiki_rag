<tbc>for sSn. DME is better with respect to Specificity. The difference is no more than 3.5%. PMS is better than DME based on the other 4 measures as well.

## 3.3 ChIP-Chip Results

We used the publicly available database for ChIP-Chip available at `http://bdtnp.lbl.gov/Fly-Net/browseChipp` . Since some datasets are very large we only use the datasets which have less than 500 sequences and length of motifs are less than or equal to 15. A summary of the results can be found in  7.

## 3.4 ChIP-Seq Results

We used the Human database for the ChIP-Seq results. It consisted of 24 files (Chr1 - Chr22, ChrX, ChrY). Since the datasets were large, we just sampled a small subset of sequences. 20% of the total number of sequences were chosen at random and all motifs which occur in at least half the sequences are chosen by PMS. The motif and the locations in the sequences are available and we used that information to find where the truth occurred. The comparison results are summarized in  8.

\begin{tabular}{ccccccc}
**Scoring Technique** & **nSn** & **nSp** & **sSn** & **nPPV** & **nPC** & **nCC** \\
PMS SumMin & 18 & 0 & 16 & 8 & 13 & 7 \\
DME SumMin & 0 & 3 & 0 & 3 & 2 & 2 \\
BestDME SumMin & 1 & 5 & 1 & 1 & 0 & 0 \\
PMS SumMinD & 4 & 0 & 3 & 4 & 2 & 2 \\
DME SumMinD & 0 & 7 & 0 & 0 & 1 & 1 \\
BestDMESumMinD & 0 & 8 & 0 & 2 & 1 & 2 \\
PMS SumMin500 & 18 & 1 & 20 & 13 & 20 & 11 \\
PMS SumMinD500 & 4 & 0 & 5 & 6 & 3 & 7 \\
DME SumMin500 & 0 & 21 & 0 & 8 & 3 & 12 \\
\end{tabular}

\begin{tabular}{cccccccc}
**Scoring Technique** & **nSn** & **nSp** & **sSn** & **nPPV** & **sPPV** & **nPC** & **nCC** \\
PMS SumMin & 0.2586 & 0.9164 & 0.3483 & 0.3752 & 0.9997 & 0.1561 & 0.1843 \\
DME SumMin & 0.1638 & 0.9464 & 0.2332 & 0.3623 & 0.9994 & 0.1122 & 0.1385 \\
BestDME SumMin & 0.1715 & 0.9377 & 0.2419 & 0.3366 & 0.9993 & 0.1122 & 0.1280 \\
PMS SumMinD & 0.2880 & 0.9163 & 0.3695 & 0.3951 & 0.9996 & 0.1727 & 0.2100 \\
DME SumMinD & 0.1936 & 0.9420 & 0.2696 & 0.3715 & 0.9995 & 0.1245 & 0.1566 \\
BestDMESumMinD & 0.1863 & 0.9346 & 0.2626 & 0.3495 & 0.9993 & 0.1220 & 0.1409 \\
PMS SumMin500 & 0.2322 & 0.8961 & 0.3117 & 0.3809 & 0.9778 & 0.1476 & 0.1674 \\
PMS SumMinD500 & 0.2349 & 0.8959 & 0.3160 & 0.3842 & 1.0000 & 0.1487 & 0.1687 \\
DME SumMin500 & 0.1048 & 0.9302 & 0.1485 & 0.2802 & 0.8224 & 0.0747 & 0.0748 \\
\end{tabular}

5: Best performers

6: Average of all datasets for Best Results

