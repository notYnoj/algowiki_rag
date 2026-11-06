### 5.5 Space-Bounded Algorithm via Subset-Sum

We obtain another space-bounded algorithm for ESS by replacing the polynomial-space Subset-Sum algorithm used in Theorem 4.4 with a space-bounded Subset-Sum algorithm. Specifically, we use the faster of the time-space tradeoff algorithm for Subset Sum due to \[3\] and the polynomial-space algorithm of \[5, 11\].

**Lemma 5.13** (\[3, 5, 11\])**.** _Define_ \(\rho(i)=1+i(i+1)/2\) _for integers_ \(i\ge 1\)_. For every constant_ \(\alpha\in(0,1/2]\)_, let_ \(i_\alpha\) _be the integer such that_ \(\frac{1}{\rho(i_\alpha+1)}<\alpha\le\frac{1}{\rho(i_\alpha)}\)_, and define_

\(\tau_\mathrm{subset}(\alpha)=\mathrm{min}\left\{1-\frac{1}{i_\alpha+1}-\frac{\rho(i_\alpha)-2}{i_\alpha+1}\alpha,0.86\right\}.\) (13)

_We also define_ \(\tau_\mathrm{subset}(0)=0.86\)_. Then there is a Monte Carlo algorithm for Subset-Sum that runs in_ \(O^*(2^{\tau_\mathrm{subset}(\alpha)n})\) _time and uses_ \(O^*(2^{\alpha n})\) _space._

We use Lemma 5.13 to obtain the following theorem.

**Theorem 5.14.** _Let_ \(\ell'\) _be the minimum solution ratio. For every constant_ \(\alpha\in[0,1/2]\)_, there is a Monte Carlo algorithm for ESS that runs in_ \(O^*(2^{(H(\ell^\prime)+\tau_\mathrm{subset}(\alpha)\ell^\prime)n})\) _time and uses_ \(O^*(2^{\alpha n})\) _space._

_Proof._ We replace the _O_<sup>∗</sup>(2<sup>0.86_n_</sup>)-time polynomial-space Subset-Sum algorithm used in the proof of Theorem 4.4 with the Subset-Sum algorithm from Lemma 5.13, which runs in \(O^*(2^{\tau_\mathrm{subset}(\alpha)n})\) time and uses \(O^*(2^{\alpha n})\) space. Since the rest of the algorithm and its analysis remain unchanged, this replacement gives the claimed time and space bounds.

## Acknowledgements

The authors used Mathematica for numerical evaluations. The authors also used ChatGPT for grammar correction and language polishing. All AI-assisted text was reviewed by the authors, who assume full responsibility for the content of the paper.

## References

\[1\] Jonathan Allcock, Yassine Hamoudi, Antoine Joux, Felix Klingelhöfer, and Miklos Santha. "Classical and Quantum Algorithms for Variants of Subset-Sum via Dynamic Programming". In: _30th Annual European Symposium on Algorithms (ESA 2022)_. Ed. by Shiri Chechik, Gonzalo Navarro, Eva Rotenberg, and Grzegorz Herman. Vol. 244. Leibniz International Proceedings in Informatics (LIPIcs). Dagstuhl, Germany: Schloss Dagstuhl - Leibniz-Zentrum für Informatik, 2022, 6:1–6:18. isbn: 978-3-95977-247-1. doi: `10.4230/LIPIcs.ESA.2022.6`.

\[2\] Giannis Alonistiotis, Antonis Antonopoulos, Nikolaos Melissinos, Aris Pagourtzis, Stavros Petsalakis, and Manolis Vasilakis. "Approximating subset sum ratio via partition computations: G. Alonistiotis et al." In: _Acta Informatica_ 61.2 (2024), pp. 101–113. doi: `10.1007/s00236- 023-00451-7`.

\[3\] Per Austrin, Petteri Kaski, Mikko Koivisto, and Jussi Määttä. "Space–Time Tradeoffs for Subset Sum: An Improved Worst Case Algorithm". In: _40th International Colloquium on Automata, Languages, and Programming (ICALP 2013)_. Ed. by Fedor V. Fomin, Rūsinņš Freivalds, Marta Kwiatkowska, and David Peleg. Berlin, Heidelberg: Springer Berlin Heidelberg, 2013, pp. 45–56. isbn: 978-3-642-39206-1. doi: `10.1007/978-3-642-39206-1\_5`.

