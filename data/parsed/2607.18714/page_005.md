<tbc>Since the algorithm checks all candidate pairs x and y, it will eventually process the specific iteration where x=p<sub>s</sub> and y=p<sub>t</sub>. Consider this specific pair (p<sub>s</sub>,p<sub>t</sub>). Because our algorithm takes the minimum over all pairs, checking the specific pair (p<sub>s</sub>,p<sub>t</sub>) gives us an upper bound on est(s,t):<tbc>

\(\mathrm{est}(\mathrm{s},\mathrm{t})\le\mathrm{est}(\mathrm{s},\mathrm{p}_\mathrm{s})+\mathrm{est}(\mathrm{p}_\mathrm{s},\mathrm{p}_\mathrm{t})+\mathrm{est}(\mathrm{p}_\mathrm{t},\mathrm{t})\)

<tbc>Later in our paper, we will show that we can find the exact distance between s and all the vertices in ball<sub>A</sub>(s) quickly. Thus, est(s,p<sub>s</sub>)=|sp<sub>s</sub>|. Similarly, est(t,p<sub>t</sub>)=|p<sub>t</sub>t|. Thus, we get:<tbc>

\(=|\mathrm{sp}_\mathrm{s}|+\mathrm{est}(\mathrm{p}_\mathrm{s},\mathrm{p}_\mathrm{t})+|\mathrm{p}_\mathrm{t}\mathrm{t}|\)

<tbc>By Theorem 2.1, \(\mathrm{est}(\mathrm{p}_\mathrm{s},\mathrm{p}_\mathrm{t})\le 2|\mathrm{p}_\mathrm{s}\mathrm{p}_\mathrm{t}|+1\). Thus, we get:<tbc>

\(\le|\mathrm{sp}_\mathrm{s}|+(2|\mathrm{p}_\mathrm{s}\mathrm{p}_\mathrm{t}|+1)+|\mathrm{p}_\mathrm{t}\mathrm{t}|\)<br>
\(=(|\mathrm{sp}_\mathrm{s}|+|\mathrm{p}_\mathrm{s}\mathrm{p}_\mathrm{t}|+|\mathrm{p}_\mathrm{t}\mathrm{t}|)+|\mathrm{p}_\mathrm{s}\mathrm{p}_\mathrm{t}|+1\)

<tbc>Since p<sub>s</sub> and p<sub>t</sub> lie exactly on the shortest st path, |sp<sub>s</sub>|+|p<sub>s</sub>p<sub>t</sub>|+|p<sub>t</sub>t|=|st|. Using Theorem 2.6, \(|\mathrm{p}_\mathrm{s}\mathrm{p}_\mathrm{t}|\le\mathrm{c}\). Thus, we get:

\(\le|\mathrm{st}|+\mathrm{c}+1\) (1)

Thus, we get a constant additive approximation of the st path. Let us now look at the running time of our algorithm. Using Theorem 2.3, |cluster<sub>A</sub>(x)|,|cluster<sub>A</sub>(y)|=\(\tilde{\mathcal{O}}(\mathrm{n}^{0.05})\). Thus, the running time of our algorithm is bounded by:

\(\sum_{\mathrm{x},\mathrm{y}}\sum_{\mathrm{s}\in\mathrm{cluster}_\mathrm{A}(\mathrm{x}),\mathrm{t}\in\mathrm{cluster}_\mathrm{A}(\mathrm{y})}\mathrm{O}(1)=\sum_{\mathrm{x},\mathrm{y}}\tilde{\mathcal{O}}(\mathrm{n}^{0.05}\times\mathrm{n}^{0.05})=\tilde{\mathcal{O}}(\mathrm{n}^{2.1})\)

Algorithm 1 processes all pairs x and y, resulting in an undesirable \(\tilde{\mathcal{O}}(\mathrm{n}^{2.1})\) running time. But do we really need to check all pairs? By Theorem 2.6, we know that our target vertices p<sub>s</sub> and p<sub>t</sub> are at most a distance c apart. Unfortunately, our current algorithm blindly pairs vertices that are arbitrarily far from each other. But what if, for a given x, we only check candidates y that are close to it? We define the following set to restrict our search space.

**Definition 2.7.** _For each_ \(\mathrm{x}\in\mathrm{V}\)_, we compute a set_ ESTIMATEDCLOSE(x) _defined as follows:_

\(\mathrm{ESTIMATEDCLOSE}(\mathrm{x})=\{\mathrm{y}|\mathrm{est}(\mathrm{x},\mathrm{y})\le 2\mathrm{c}+1\}\)

Using Theorem 2.6, \(|\mathrm{p}_\mathrm{s}\mathrm{p}_\mathrm{t}|\le\mathrm{c}\). Since we have pre-calculated a (2,1)-APSP, \(\mathrm{est}(\mathrm{p}_\mathrm{s},\mathrm{p}_\mathrm{t})\le 2\mathrm{c}+1\). Thus, ESTIMATEDCLOSE(p<sub>s</sub>) contains p<sub>t</sub>.

We now modify Algorithm 1: instead of pairing x with every vertex in the graph, we pair it only with vertices in ESTIMATEDCLOSE(x). This modification improves the running time when ESTIMATEDCLOSE(x) is small. Unfortunately, if |ESTIMATEDCLOSE(x)|=O(n), then the algorithm still performs as poorly as Algorithm 1. But what if we use the size of ESTIMATEDCLOSE(x) to our advantage? We now present our final insight. For each candidate vertex x, we divide the algorithm into two cases based on size of ESTIMATEDCLOSE(x):

1. **Sparse Case:** \(|\mathrm{ESTIMATEDCLOSE}(\mathrm{x})|\le\mathrm{n}^{0.875}\)<tbc>

<tbc>In this case, we use a modified version of Algorithm 1. We only pair x with vertices \(\mathrm{y}\in\mathrm{ESTIMATEDCLOSE}(\mathrm{x})\). Since the size of ESTIMATEDCLOSE(x) is bounded, the number of pairs processed for a given x reduces to O(n<sup>0.875</sup>). Across all sparse vertices, this takes time:<tbc>

