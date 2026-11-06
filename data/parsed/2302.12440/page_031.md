### BMS observation.

One natural extension is to replace BSC observation noise with a Binary Memoryless Symmetric channel (BMS). That is, for every noisy comparison, the probability of error is chosen (independently) from a distribution _W_ on \([0,\frac{1}{2}]\), and this probability is returned together with the comparison result. In this case our guess is that

\((1\pm o(1))\left(\frac{1}{\mathbb{E}_{p\sim W}[I(p)]}+\frac{1}{\mathbb{E}_{p\sim W}[(1-2p)log\frac{1-p}{p}]}\right)nlogn\)

noisy comparisons should be necessary and sufficient. When _W_ is supported on \([\epsilon,1/2-\epsilon]\) for some constant \(\epsilon>0\) independent of _n_, we expect it to be easier to adapt our proofs to BMS, whereas in the general case, issues described in the Varying _p_ discussion above can occur.

## References

