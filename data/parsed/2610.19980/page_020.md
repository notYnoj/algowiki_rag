<tbc>bar, replace a rectangle, or nudge an endpoint, keeping a nonworsening candidate under a nonseparability key; this second stage is what makes it more than random packing noise. `witness\_breaking` first finds an easy witness, a guillotine-separable subset of majority size (enumerated for small _n_, sampled otherwise), and then tries to destroy that separation by extending a rectangle across a projection gap or inserting a thin bridging rectangle, alongside bar replacement, cut blockers, and motif copies, again followed by guided nonseparability trials. It is an adversarial neighborhood that acts on a concrete weakness of the current packing. `symmetry\_ crossover\_hillclimb` applies the shared 25-proposal portfolio - one-step shifts, relocations that preserve a rectangle’s width and height, exchanges of two rectangles’ vertical intervals, and global symmetries - to<tbc>

<tbc>disjoint packings, repairing each proposal to interior- disjointness and scoring it exactly. Acceptance is gated first by a nontriviality requirement of at least two destroyed rectangles and then by the exact number destroyed, and no exact-downhill step is ever accepted. In practice this shared exact-nonworsening rule does not transfer to guillotine hardness: starting from an easily separable packing, none of its nonworsening local moves reaches a harder one, so every guillotine configuration using it stalls at the trivial 1/6 value (Section 5).

_Surrogates._ `first\_cut\_obstruction` scores by how many rectangles the cheapest progressing first cut must cross, that is, how hard it is to make even the first guillotine slice, with small bonuses for a first cut that leaves two comparably sized sides and for a packing whose horizontal and vertical spans are similar. It is<tbc>

Misr: component-slice convergence around the best final configuration
Vary representation
Vary local search
Vary surrogate
local search-sequence pair pivot
representation-triangle free rect
representation-triangle free rect
local search-sequence pair pivot
surrogate-exact tp gap pressure
surrogate-exact tp gap pressure
1.560
1.560
1.560
1.405
1.405
1.405
Best exact score so far
1.250
1.250
1.250
1.095
1.095
1.095
0.940
0.940
0
2089
4178
6266
8355
0
1597
3194
4790
6387
0
1642
3284
4925
6567
Cumulative transformer-training epochs
Cumulative transformer-training epochs
Cumulative transformer-training epochs
fixed symmetry rectangles
program coeffi pivot
exact tp gap pressure
quadratic program rectangles
sequence pair pivot
graph conflict proxy
triangle free rect
symmetry crossover hillclimb
triangle free exact gap pressure

Guillotine: component-slice convergence around the best final configuration
Vary representation
Vary local search
Vary surrogate
local search-witness breaking
representation-rect direct disjoint
representation-rect direct disjoint
local search-witness breaking
surrogate-depth limited dp
surrogate-depth limited dp
0.358
0.358
0.358
0.294
0.294
0.294
Best exact score so far
0.229
0.229
0.229
0.165
0.165
0.165
0.100
0.100
0.100
0
838
1676
2513
3351
0
838
1676
2513
3351
0
920
1840
2761
3681
Cumulative transformer-training epochs
Cumulative transformer-training epochs
Cumulative transformer-training epochs
fixed symmetry packing
packing resize
depth limited dp
rect direct disjoint
symmetry crossover hillclimb
first cut obstruction
recursive obstruction grammar
witness breaking
k subset nonseparability

Figure 8: Component-slice convergence for MISR, plotting the best exact integrality gap \(\alpha^*/\alpha\) found so far. From left to right the panels vary the representation, the local-search operation, and the surrogate.

Figure 9: Component-slice convergence for guillotine hardness, plotting the best exact destroyed fraction 1-save_/n_ found so far. From left to right the panels vary the representation, the local-search operation, and the surrogate.

