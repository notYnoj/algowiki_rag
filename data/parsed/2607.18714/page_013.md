in \(\mathrm{L}_\gamma\). For each entry B<sub>ij</sub>, we store the estimate of the distance between vertex \(\mathrm{i}\in\mathrm{V}\) and vertex \(\mathrm{j}\in\mathrm{L}_\gamma\) that we updated in Algorithm 5. We then compute C=B⋆B<sup>T</sup> using Theorem 3.11. Note that C provides a \((1+\varepsilon)\) approximation of B⋆B<sup>T</sup>. We update the estimates for all vertex pairs using C, if required. This completes the description of Algorithm 4. We now analyze the running time and the approximation guarantee of our algorithm.

## 4.2.1 Running Time

Fix a value of \(\gamma\). We first analyze the running time of \(\mathrm{UPDATEFROM}(\mathrm{z},\gamma)\). Since the size of \(\mathrm{G}(\gamma)\) is \(\tilde{\mathrm{O}}(\mathrm{n}\gamma)\), the running time of \(\mathrm{UPDATEFROM}(\mathrm{z},\gamma)\) is \(\tilde{\mathrm{O}}(\mathrm{n}\gamma)\). The set \(\mathrm{L}_\gamma\) contains \(\tilde{\mathrm{O}}(\frac{\mathrm{n}}{\gamma})\) vertices, so all invocations of UPDATEFROM together take \(\tilde{\mathrm{O}}(\mathrm{n}^2)\) time.

Next, we compute the distance product B⋆B<sup>T</sup>. The sizes of B and B<sup>T</sup> are \(\mathrm{n}\times\tilde{\mathrm{O}}(\frac{\mathrm{n}}{\gamma})\) and \(\tilde{\mathrm{O}}(\frac{\mathrm{n}}{\gamma})\times\mathrm{n}\) respectively. Since \(\gamma\ge\mathrm{n}^{0.875}\), we have \(\frac{\mathrm{n}}{\gamma}\le\mathrm{n}^{0.125}\). Using Theorem 3.11, we compute C in time \(\tilde{\mathrm{O}}(\frac{\mathrm{n}^{\omega(0.125)}}{\varepsilon})\). We then update the estimates for all vertex pairs using C, if required. This step takes O(n<sup>2</sup>) time.

Thus, the running time for a fixed \(\gamma\) equals \(\tilde{\mathrm{O}}(\mathrm{n}^2+\frac{\mathrm{n}^{\omega(0.125)}}{\varepsilon})\). The while loop repeats at most logn times, so the total running time remains:<tbc>

\(\tilde{\mathrm{O}}\left(\mathrm{n}^2+\frac{\mathrm{n}^{\omega(0.125)}}{\varepsilon}\right)\)

<tbc>Using \[Cop82, Wil14\], \(\omega(0.125)=2\). Thus, we get:<tbc>

\(=\tilde{\mathrm{O}}\left(\frac{\mathrm{n}^2}{\varepsilon}\right)\)

<tbc>Setting \(\varepsilon=0.5\), we get:

\(=\tilde{\mathrm{O}}(\mathrm{n}^2)\)

We now analyze the approximation guarantees of the algorithm.

## 4.2.2 Approximation Ratio

We start with the following definition:

**Definition 4.5.** _Let_ \(\mathrm{TRUECLOSE}(\mathrm{p}_s)=\{\mathrm{y}||\mathrm{p}_s\mathrm{y}|\le 2c+1\}\)

Informally, TRUELOSE(p<sub>s</sub>) denotes the _actual_ (not estimated) set of all vertices at distance at most 2_c_+1 from p<sub>s</sub>. We cannot compute TRUELOSE(p<sub>s</sub>) as we do not know the exact distance between vertices in the graph. However, we claim that a vertex in ESTIMATEDCLOSE(p<sub>s</sub>) must also lie in TRUELOSE(p<sub>s</sub>).

**Lemma 4.6.** _If_ \(\mathrm{y}\in\mathrm{ESTIMATEDCLOSE}(\mathrm{p}_s)\)_, then_ \(\mathrm{y}\in\mathrm{TRUECLOSE}(\mathrm{p}_s)\)_. Thus,_ \(|\mathrm{TRUECLOSE}(\mathrm{p}_s)|\ge|\mathrm{ESTIMATEDCLOSE}(\mathrm{p}_s)|\).

_Proof._ Since ESTIMATEDCLOSE(p<sub>s</sub>) is based on estimates that can only be larger than the actual distances, \(\mathrm{est}(\mathrm{p}_s,\mathrm{y})\le 2c+1\) implies \(|\mathrm{p}_s\mathrm{y}|\le 2c+1\). Thus, if \(\mathrm{y}\in\mathrm{ESTIMATEDCLOSE}(\mathrm{p}_s)\), then \(\mathrm{y}\in\mathrm{TRUECLOSE}(\mathrm{p}_s)\).

Using the above lemma, since |ESTIMATEDCLOSE(p<sub>s</sub>)|_\>_n<sup>0.875</sup>, even |TRUELOSE(p<sub>s</sub>)|_\>_n<sup>0.875</sup>. The set TRUELOSE(p<sub>s</sub>) is fixed. If we sample vertices of suitable size at random, we are guaranteed to hit a vertex in TRUELOSE(p<sub>s</sub>) with high probability.

