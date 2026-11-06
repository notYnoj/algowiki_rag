complexity, a residual certificate, a support-completeness theorem, and a sampling efficiency. We formulated the method on Riemannian cross sections, showed that conformal coordinates make the stiffness matrix metric-independent in two dimensions, obtained measurement filters from the isometries of the cross section, and bounded the effect of geometric perturbations through the Lie derivative of the metric. Numerical results for elliptic, lens-shaped, and curved ducts confirm the guarantees and show strong compression in a Fourier basis. Experiments on trapped-ion and superconducting processors confirm the measurement convention, the parity selection rule, and the replacement-noise picture.

The analysis and the examples also identify the conditions under which quantum Krylov-state sampling can be expected to offer a benefit. (1) The source and the solution must have different mode structures, so that a selection from the source fails. (2) The essential set must not be identifiable by an inexpensive classical procedure such as residual-greedy selection. (3) The outcome law must be nearly flat on the essential set, so that the sampling efficiency is not small. (4) The hardware noise must be small enough that the samples do not fill the admissible space with modes of negligible solution weight. The elliptic duct and the curved vessels satisfy condition (1). Condition (2) fails in all examples studied here, and condition (4) fails in the present hardware experiments. Problems that satisfy all four conditions remain to be identified.

## Acknowledgments

This work was supported by Korea National Research Foundation (NRF) grants No. RS-2026-25612745 and RS-2025-00519428, ICT R&D program of IITP-2023-2021-0-01810, RS-2023-00225385, RS- 2025-25464788, AFOSR grant FA2386-22-1-4052, Cleveland Clinic Quantum Innovation Catalyzer Program and Amazon Web Services. We acknowledge the use of IBM Quantum services for this work. The views expressed are those of the authors, and do not reflect the official policy or position of IBM or the IBM Quantum team. This work was also supported by the National Quantum Laboratory at Maryland (QLab). We acknowledge IonQ for providing quantum computing resources for this work. The views expressed are those of the authors, and do not reflect the official policy or position of IonQ. The authors used the AI assistants ChatGPT (OpenAI) and Claude (Anthropic) to help draft and edit the manuscript, to check the mathematical derivations, and to write numerical and analysis scripts. The authors reviewed and verified all results and take full responsibility for the content of this article.

## Author contributions

D.A. conceived the work, developed the theory and the algorithms, carried out the numerical studies, and wrote the first draft of the manuscript. B.P. carried out the hardware implementation. Both authors reviewed and edited the manuscript.

## Data availability

The derivations are given in the text and the appendices. The raw hardware counts, the submitted circuits, the calibration data, the job identifiers, the source data of s 10 and 11 and Figs. 3 and 4, and the scripts that reproduce the numerical and hardware results are available from the corresponding author upon reasonable request.

## Competing interests

D.A. is the founder of Singularity Quantum Inc. and holds an equity interest in the company; the authors declare no other competing interests.

