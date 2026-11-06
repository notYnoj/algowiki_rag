<tbc>reversible Turing machine using _O(t_) time and _O(s_) space; the current best results asymptotically increase at least one of them \[Vit05\], and there is an oracle relative to which this is necessary \[FA17\].

In this paper we start to investigate how stochastic thermodynamics can help untangle these issues.

## 1.2 Beyond logical reversibility: Stochastic thermodynamics

Bennett’s approach of requiring logical reversibility of every computational step is in one sense a very ambitious way to minimize energy costs by pushing the so-called _Landauer cost_ of executing logically irreversible operations to 0, simply by removing all such operations. Li and Vitányi \[LV96\] investigated how it is possible to trade time and space for ‘energy’ by limiting the number of logically irreversible steps in a computation. Demaine, Lynch, Mirano, and Tyagi \[DLMT16\] built on this idea and proposed a generalization of logical reversibility they call _semi-reversible computing_, in which irreversible operations \(f:D\rightarrow R\) are permitted and assumed to cost log \(\frac{|D|}{|R|}\) bits of energy to execute (this being the natural generalization of the Landauer cost of 1 bit when |_D_|=2 and |_R_|=1, assuming a uniform distribution on _D_). The total energy cost (by this definition) is then treated as a complexity measure to be minimized.

However, the more modern field of _stochastic thermodynamics_ \[VdBE15, Sei25\] has generalized our understanding of the interaction of entropy and fundamental energy use in physical devices, beyond the overly simplistic assumption that each bit erasure costs _k_Tln2 energy. It has been argued \[WKL<sup>+</sup>24\] that stochastic thermodynamics can be fruitfully applied to computational complexity to better understand the relationship between fundamental thermodynamic costs and other traditional complexity measures such as time and space.

We now review _entropy production_, a basic concept from modern stochastic thermodynamics that lets us study the fundamental limits of energetic costs even for logically irreversible computation. As applied to the study of computation, we propose entropy production as a computational complexity measure/cost to be minimized. This is already the measure of interest for such systems in the physics community (i.e. \[Wol19a, PP21, WKL<sup>+</sup>24, Sei25\]). We then analyze these costs in a particular circuit model, noting that our approach can be extended in a natural way to other models of computation.

We provide our full definitions in Section 2 and give a semi-formal summary of the underlying concepts here. Briefly, the generalization of the Second Law of thermodynamics most central to our purpose is the equation

\(\mathsf{EP}=\mathsf{Q}-(\mathcal{S}(\mathcal{D}_0)-\mathcal{S}(\mathcal{D}_1)).\) (1)

Equation (1) appears later in Definition 2.24 with notation specialized to the study of the thermodynamics of circuits. The terms EP and Q respectively mean _entropy production_ and _entropy flow_. However, throughout this paper we focus on the case of a single (thermal) reservoir. That leads us to use the term _heat released_ for Q. Furthermore, given our choice of units such that _k_Tln2=1, we can equate information in bits with equal units of heat; we discuss these terms below.

To begin, we focus on the term S(D<sub>0</sub>)-S(D<sub>1</sub>) in Eq. (1). D<sub>0</sub> represents the probability distribution on states of a physical device<sup>7</sup> prior to executing a (possibly logically irreversible) step,<tbc>

<sup>7</sup>The stochastic thermodynamic perspective can be viewed as an "intrinsically distributional" complexity measure because it defines costs that are fundamentally tied to a distribution over inputs. In other words, there is not in general a sensible notion of "worst-case entropy production" defined as \(max_{x\in\{0,1\}^n}\mathsf{EP}(x)\), as is typical for definitions

