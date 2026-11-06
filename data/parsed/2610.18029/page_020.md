The reduction is highly dependent on the specific vertex colouring, rather than just the number of colours required. Therefore, the efficacy of the hybrid reduction is no longer deterministic and will fluctuate with the exact colourings obtained. Indeed, as the instance sizes grows, the number of different colourings giving the same weight often grows very quickly too, decreasing the chance of finding one that will yield a powerful reduction. Nonetheless, even with sampling 3 different colourings, we see a impact in our problem sizes. Furthermore, recall the purpose of this reduction: it is to remove vertices that we do not belong in any putative clique. Therefore, extra effort here does not lead to increased postprocessing, and is worth it in order to reduce the computational requirements of the much-harder problem of enumerating all cliques on the resulting graph. In a similar vein to our overall argument, we do not necessarily see this preprocessing to be useful for every input, but simply, where this reduction is effective, it is very fruitful and will allow us to tackle much larger problem sizes than before.

For our complete hybrid classical-quantum preprocessing pipeline, we see the following reductions in problem sizes:

This reduction shrinks the graph to a much smaller instance. To illustrate its utility, the set of 350 samples was reduced to 64 vertices entirely classically, we can now reduce this to simply a 5-qubit complete (complement) graph:

Original D-Wave Reduction
400
300
Number of Vertices
200
100
0
100
200
300
400
500
600
700
800
Number of Samples

Original D-Wave Reduction
1750
1500
1250
Number of Edges
1000
750
500
250
0
100
200
300
400
500
600
700
800
Number of Samples

(a) Vertices

(b) Edges

Figure 9: The reduction of number of graph vertices and edges for SARS-CoV-2 samples between the original postprocessing and D-Wave reductions.

