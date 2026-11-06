<tbc>zero-error randomized) fine-grained reduction from CNF-SAT or OV to 3SUM, APSP, or Exact Triangle. In fact, our algorithm shows that if there were a deterministic fine-grained reduction from CNF-SAT or OV to 3SUM, APSP, or Exact Triangle, then SETH (and not merely NSETH) is false.

Interestingly, the issues posed by co-nondeterminism disappear in the Merlin-Arthur world where randomization is allowed. CNF-SAT \[Wil16\], 3SUM, and APSP \[ACJ<sup>+</sup>22\] all have vastly improved Merlin-Arthur protocols: the verification time for CNF-SAT (indeed for counting its satisfying assignments) is 2<sup>_n/_2</sup>poly(_n_), for 3SUM it is \(\tilde{O}(n)\), and for APSP it is \(\tilde{O}(n^2)\).

While we obtain a polynomial improvement for 3SUM, we are unable to do so for _k_-SUM for \(k\ge 4\). 3SUM reduces to _k_-SUM, but no reduction in the other direction is known, and although _k_-SUM reduces to exact-weight subgraph problems \[AL13, ALW14\], whose _n<sup>k</sup>_ baseline we improve (Section 5.3), those reductions can only give _k_-SUM algorithms far slower than the \(n^{\lceil k/2\rceil}\) baseline. The same holds for _k_-XOR for \(k\ge 4\) and for the 3SUM-Indexing conjecture \[GKLP17, KP19, GGH<sup>+</sup>20\]. Ultimately, we believe that one good reason for the lack of progress on \(k\ge 4\) is that _k_-SUM for \(k\ge 4\) is not known to have fine-grained self-reductions. This has been a major obstacle in designing reductions from _k_-SUM and is also a major obstacle in designing algorithms for it. (The same goes for _k_-XOR for \(k\ge 4\).)

## Combinatorial algorithms.

The new algorithms are algebraic and potentially impractical in their current form: the constants hidden in the \(O(\cdot)\) are enormous, and the exponents can likely be improved. One might ask whether there are practical or "combinatorial" algorithms for these problems, similar to how one talks about combinatorial Boolean Matrix Multiplication (BMM). The known algorithms for combinatorial BMM, including the Four Russians \[ADKF70\], the _n_<sup>3</sup>/polylog_n_ bounds of \[BW09, Cha15, Yu18\], and the recent \(n^3/2^{\Omega((\mathrm{log}n)^{1/7})}\) bound of Abboud, Fischer, Kelley, Lovett, and Meka \[AFK<sup>+</sup>24\], save only a subpolynomial factor, and no truly subcubic combinatorial algorithm is known. We do not know whether such algorithms exist. Most FGC reductions are combinatorial, so one could refocus the hypotheses to be about combinatorial algorithms \[VW10, VW18, AV14\].

## Other parameter regimes.

Even without considering combinatorial algorithms, one might also ask whether All-Edges Sparse Triangle can be solved faster in every regime of how large the three parts are. Our technique (due to the identity we use) needs the middle part to have at most _n_<sup>0.12</sup> vertices, whereas prior reductions have focused on different regimes.

For instance, the balanced sparse case of All-Edges Sparse Triangle introduced by Pˇatra ̧cu \[Pˇat10\] has as input a tripartite graph with roughly equal parts and _m_ edges overall. Most known fine-grained reductions produce such balanced instances and give conditional lower bounds of _m_<sup>4/3-_o_(1)</sup>.

Another case of interest is where the tripartite graph has two parts of size _n_ and one part of size \(\sqrt{n}\) and _O(n_<sup>3/2</sup>) edges overall. Solving this version in \(O(n^{2-\varepsilon})\) time, even only for triangle detection (and not even for the all-edge version), would have consequences for girth approximation in undirected unweighted graphs \[RV12\].

## Even faster algorithms.

Our focus in this paper is to give the simplest presentation of our new algorithm for thin matrix products, and show how known reductions to All-Edges Sparse Triangle combine with this to give all the polynomial speedups mentioned above. In particular, over the course of this project, with Claude we generated some algorithms whose exponents<tbc>

