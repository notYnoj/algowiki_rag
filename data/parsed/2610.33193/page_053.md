\(=log\frac{n!}{\prod_{b\in\{0,1\}^m}c_b!}.\)

Due to the linearity of expectation, the total expected heat released during sorting is exactly:

\(\sum_{c\in\mathbb{Z}_{\ge 0}^{\{0,1\}^m}}Pr_{x\sim\mathcal{D}}\left[C(x)=c\right]log\frac{n!}{\prod_{b\in\{0,1\}^m}c_b!}.\) (14)

Since the drop in entropy (13) exactly matches the expected heat released (14) by our circuit, we can conclude that the circuit entropy production is zero.

## 7 Conclusion

In this paper we posit that the concepts of entropy production and heat release provide a principled foundation for understanding inherent energy costs of computations. We introduce a thermodynamic logic circuit model in which gates (e.g., Boolean logic gates or comparator gates) are augmented with heat functions, which determine a circuit’s entropy flow and entropy production with respect to a given input distribution. We show that in general, determining optimal heat functions is computationally intractable. In contrast, we show that for specific problems (i.e. sorting) our model can be used both to analyze the thermodynamic costs of existing circuits and to design new circuits that are thermodynamically efficient.

There are many directions for future work. Our analysis of Batcher’s odd-even mergesort on bits uses a set of gate heat functions that scales with the circuit size; what are the penalties for using only a constant number of distinct heat functions for this problem? How can we analyze heat dissipation of circuits in other problem domains, such as graph algorithms? What are good general design principles for energy-efficient computation?

Theorem 6.1 shows a zero EP circuit for bit-compaction, the problem of sorting 1-bit keys with _m_-bit payloads, using _O(n_log_n_) depth (as long as log_m_ is _O(n_)). Can we design a zero EP compaction circuit with polylog(_n_) depth? This rules out erasing key bits one at a time as we do, which requires \(\Omega(n)\) depth.<sup>43</sup> Is it possible to show a lower bound of \(\Omega(n)\) depth for the clean compaction problem, arguing that zero EP erasure with constant arity gates must do so sequentially?

Another limitation of our technique to do compaction in Theorem 6.1 is that we require \(\Omega(n^2)\) erasure gates. This is necessary given our specific erasure technique: we get the circuit to a point where it has the intended output (compacted key-payload records), as well as the uncompacted keys \(b\in\{0,1\}^n\), and we erase each key bit one at a time. There are \(\Omega(n^2)\) conditional probabilities that are possible for each bit to be a 1 across all stages during this process, necessitating \(\Omega(n^2)\) erasure gates. However, this does not rule out a more sophisticated way to erase the bits in which we do not encounter so many different conditional probabilities. Perhaps some efficient reversible circuit computation could be done on _b_ to transform it into a different bit string \(b'\) of length _O(n_), such that while erasing the bits of \(b'\) in order, each bit would only have one of, say, _O_(log_n_) different (possibly position-dependent) probabilities. In this case _O(n_log_n_) total erasure gates would suffice to erase all bits.

Suppose the number of erasure gates could be reduced to _O(n_polylog(_n_)), or if \(m\gg n\) so that the _O(n_<sup>2</sup>) erasure gates are negligible. (To simplify discussion below assume _m=O_(1), so that<tbc>

<sup>43</sup>It is even worse for our circuit, \(\Theta(nlogn)\), due to requiring \(\Theta(logn)\) depth per bit to route it through a \(\Theta(log(n))\)-layer demultiplexer to the erasure gate with appropriate heat function.

