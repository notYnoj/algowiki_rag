<tbc>factual world data inquiry stage is fixed to five, and the sample size for running candidate algorithms is fixed to 20.

We define the user-specified ranking budget _B_ as the maximum monetary cost the optimizer may spend to rank the input items. The cost of each access path is estimated from its required LLM API calls using the corresponding model’s API pricing, and the optimizer considers only paths whose estimated cost is within _B_. We evaluate the optimizer across a range of _B_ values to study the resulting quality-cost tradeoff. In the LLM-as-Judge optimizer,<tbc>

<tbc>the evaluation phase employs the identical backbone model used for the initial sorting. Utilizing the same model facilitates an internal reflection mechanism: the judge can seamlessly re-evaluate the candidate rankings for subtle errors and iteratively refine its assessments to maximize final accuracy. For the self-consistency optimizer, we measure candidate quality by comparing outputs to a derived aggregation through RRF \[10\]. The final output is the RRF fusion of the rankings produced by the top budget-feasible candidates by proxy agreement.

\begin{tabular}{ccccccccc}
\multirow{2}{*}{Dataset} & \multirow{2}{*}{Model} & \multicolumn{5}{c}{Top-3 Best Standalone Algorithms} & \multicolumn{2}{c}{Optimizer Best} \\
 & & 1st Alg & Acc. & 2nd Alg & Acc. & 3rd Alg & Acc. & Judge & Self-Cons. \\
\multirow{3}{*}{World} & Llama-3.1 70B & point\_search & 0.982 & point & 0.975 & ext\_point\_search & 0.969 & **0.982** & **0.982** \\
 & GPT-5 mini & point\_search & 0.996 & point & 0.996 & quick\_3 & 0.990 & **0.996** & **0.996** \\
 & Haiku-4.5 & point\_search & 0.98 & ext\_bubble\_4 & 0.98 & quick\_3 & 0.98 & **0.98** & **0.98** \\
\multirow{3}{*}{Sembench} & Llama-3.1 70B & ext\_merge\_4 & 0.919 & quick\_3 & 0.909 & quick & 0.909 & **0.926** & **0.927** \\
 & GPT-5 mini & ext\_merge\_4 & 0.922 & quick & 0.918 & quick\_3 & 0.918 & **0.929** & **0.922** \\
 & Haiku-4.5 & quick\_3 & 0.922 & quick & 0.920 & ext\_merge\_4 & 0.919 & **0.926** & **0.922** \\
\multirow{3}{*}{DL20} & Llama-3.1 70B & ext\_merge\_4 & 0.685 & quick\_3 & 0.684 & quick & 0.681 & **0.695** & **0.697** \\
 & GPT-5 mini & ext\_bubble\_4 & 0.691 & ext\_merge\_4 & 0.687 & quick\_3 & 0.682 & 0.690 & **0.695** \\
 & Haiku-4.5 & ext\_merge\_4 & 0.717 & ext\_bubble\_4 & 0.704 & quick & 0.700 & 0.707 & **0.720** \\
\multirow{3}{*}{NfCorpus} & Llama-3.1 70B & quick & 0.570 & quick\_3 & 0.540 & ext\_merge\_4 & 0.480 & 0.512 & **0.628** \\
 & GPT-5 mini & ext\_bubble\_4 & 0.651 & quick\_3 & 0.604 & quick & 0.601 & 0.579 & **0.673** \\
 & Haiku-4.5 & ext\_merge\_4 & 0.651 & ext\_bubble\_4 & 0.638 & quick\_3 & 0.572 & 0.607 & 0.638 \\
\multirow{3}{*}{HellaSwag} & Llama-3.1 70B & quick\_3 & 0.799 & ext\_bubble\_4 & 0.781 & quick & 0.779 & 0.796 & 0.793 \\
 & GPT-5 mini & ext\_bubble\_4 & 0.818 & quick & 0.809 & ext\_merge\_4 & 0.799 & 0.804 & 0.811 \\
 & Haiku-4.5 & quick\_3 & 0.820 & quick & 0.817 & ext\_merge\_4 & 0.786 & 0.806 & 0.813 \\
\end{tabular}

