Justification: The results are averaged over 1000 to 5000 independent Monte Carlo runs. Figure 1 and Figure 2 reports standard deviations of the plotted quantities, while Appendix F.2 compares dispersion of signed estimates. Empirical error rates of the tuned BAI implementations are distinguished from the theoretical PAC guarantees in Appendix F.3.

Guidelines:

• The answer [N/A] means that the paper does not include experiments.

• The authors should answer [Yes] if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that support the main claims of the paper.

• The factors of variability that the error bars are capturing should be clearly stated (for example, train/test split, initialization, random drawing of some parameter, or overall run with given experimental conditions).

• The method for calculating the error bars should be explained (closed form formula, call to a library function, bootstrap, etc.)

• The assumptions made should be given (e.g., Normally distributed errors).

• It should be clear whether the error bar is the standard deviation or the standard error of the mean.

• It is OK to report 1-sigma error bars, but one should state it. The authors should preferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesis of Normality of errors is not verified.

• For asymmetric distributions, the authors should be careful not to show in tables or figures symmetric error bars that would yield results that are out of range (e.g., negative error rates).

• If error bars are reported in tables or plots, the authors should explain in the text how they were calculated and reference the corresponding figures or tables in the text.

8. Experiments compute resources

Question: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproduce the experiments?

Answer: [Yes]

Justification: Appendix F explicitly details the compute resources (Intel Core Ultra 9 285K CPU, 128 GB RAM) and the execution times for both the estimator experiment (40 minutes) and the BAI experiments (10 hours each).

Guidelines:

• The answer [N/A] means that the paper does not include experiments.

• The paper should indicate the type of compute workers CPU or GPU, internal cluster, or cloud provider, including relevant memory and storage.

• The paper should provide the amount of compute required for each of the individual experimental runs as well as estimate the total compute.

• The paper should disclose whether the full research project required more compute than the experiments reported in the paper (e.g., preliminary or failed experiments that didn’t make it into the paper).

9.  of ethics

Question: Does the research conducted in the paper conform, in every respect, with the NeurIPS  of Ethics https://neurips.cc/public/EthicsGuidelines?

Answer: [Yes]

Justification: The research focuses on foundational theoretical and algorithmic machine learning methodology (Sections 2 to 4), which fully conforms to the NeurIPS  of Ethics.

Guidelines:

• The answer [N/A] means that the authors have not reviewed the NeurIPS  of Ethics.

