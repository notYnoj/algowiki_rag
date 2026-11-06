# The Thermodynamic Complexity of Circuits<sup>∗</sup>

Anne Condon<sup>†</sup><sup>1</sup>, David Doty<sup>‡</sup><sup>2</sup>, Niels Kornerup<sup>§</sup><sup>3</sup>, David Soloveichik\(^\unknown^{4}\), and David Wolpert<sup>‖</sup><sup>5</sup>

<sup>1</sup>University of British Columbia

<sup>2</sup>University of California, Davis

<sup>3</sup>Sandia National Laboratories

<sup>4</sup>University of Texas, Austin

<sup>5</sup>Santa Fe Institute, New Mexico; Complexity Science Hub, Vienna; Arizona State University, Arizona; International Center for Theoretical Physics, Trieste

**Abstract**

When any physical system executes a logically irreversible (non-injective) step of a computation, the excess heat released over the so-called Landauer limit is an energetic cost that cannot be recovered. In modern computers this cost vastly dwarfs the Landauer limit. Modern stochastic thermodynamics refers to this cost as the "entropy production" and has derived some very powerful lower bounds on its value, which strictly strengthen the second law of thermodynamics. Here we introduce a model of circuits using _heat functions_ and investigate its entropy production, deriving new results on the thermodynamic complexity of circuits.

In our model, the circuits compute _cleanly_, erasing their inputs and all intermediate values. We first show that computing the optimal heat functions for gates in a given circuit (the gates that minimize total entropy production) when the circuit’s input is uniformly random is PP-complete. We also show that multiplicative approximation of those heat functions is NP-hard, but additive approximation admits a polynomial-time randomized algorithm. We give tight bounds for entropy production for certain specific families of circuits (on uniformly distributed inputs): an _n_-ary AND tree of depth _O_(log_n_) requires \(\Omega(n)\) circuit entropy production, while a serial chain achieves _O_(1), showing an energy-depth tradeoff. The Batcher odd-even mergesort network on _n_ bits has \(\Theta(n)\) entropy production, asymptotically less than its \(\Theta(nlog^2n)\) gate count. On random permutations of distinct integers its entropy production is \(\Theta(nlog^2n)\), asymptotically exceeding the Landauer cost of sorting; but preceding it with Leighton and Plaxton’s almost-sorting network reduces the total heat released to _O(n_log_n_). Finally, we show that a clean sorting circuit (not a sorting network) can sort _n_ values with zero circuit entropy production over any exchangeable input distribution. Our framework also yields streamlined proofs of known results in stochastic thermodynamics on mismatch cost and modularity cost.

<sup>∗</sup>A preliminary version of this paper appeared in chapter 6 of Niels Kornerup’s PhD thesis [Kor25]. This version substantially improves, corrects, and builds on the results in that chapter. <sup>†</sup>Condon was supported by an NSERC Discovery grant. <sup>‡</sup>Doty was supported by NSF awards 2329909 and 2211793 and DoE award DE-SC0024467. <sup>§</sup>Kornerup was supported by the LDRD Program at Sandia National Laboratories. Sandia is managed and operated by NTESS under DOE NNSA contract DE-NA0003525. \(^\unknown\)Soloveichik was supported by a Schmidt Sciences Polymath award. <sup>‖</sup>Wolpert was supported by NSF award 2626044.

