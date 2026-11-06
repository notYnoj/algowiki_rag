# Nearly Optimal Fixed-Confidence Best-Arm Identification with 1-Bit Feedback

**Abstract**

We study fixed-confidence best-arm identification under strict 1-bit feedback constraints. At each round, the learner selects an arm and a query set, and receives only a single bit indicating whether the sampled reward belongs to that set. We consider a distribution-free finite-variance setting with arm-wise localization, where direct empirical mean estimation is no longer available and clipping becomes unavoidable. We first formulate a time-uniform 1-bit mean-estimation primitive based on randomized threshold queries and a clipped tail-integral identity. We then embed this primitive into candidate-challenger best-arm identification algorithms. A fixed- clipping algorithm gives a simple anytime \((\epsilon,\delta)\)-PAC guarantee, while a phased adaptive-clipping algorithm matches the clipping level to the current resolution and yields a gap-adaptive sample complexity. We also prove a _K_-arm worst-case information-theoretic lower bound showing that the logarithmic penalty caused by finite-variance 1-bit feedback is intrinsic. This bound matches the leading dependence of the phased algorithm up to lower-order loglog factors.

### 1 Introduction

Fixed-confidence best-arm identification (BAI) is the problem of identifying an optimal, or near- optimal, arm with high probability while using as few samples as possible [6, 14, 8]. Classical formulations assume that each pull reveals the reward value itself, so that empirical means and confidence intervals can be formed directly. In this paper, we study BAI under strict _1-bit_ feedback constraints: at each round, the learner selects an arm and a query set, and receives only a single bit indicating whether the sampled reward belongs to that set. Two concrete applications instantiate the threshold-query subclass of this model.

Uplink-constrained sensing. A controller selects one of _K_ sensing locations or configurations. A fresh scalar measurement \(X_{k,t}\sim\nu_k\) is compared locally with a programmed threshold _q<sub>t</sub>_, and the device sends only \(Y_t=\mathbf{1}\{X_{k,t}\ge q_t\}\). The controller seeks a location whose mean pollutant concentration or diagnostic score is within \(\varepsilon\) of the largest, with confidence \(1-\delta\), before prioritizing an inspection or deploying an expensive high-resolution monitor. Quantized scalar sensing motivates this response mechanism [23]; adaptive arm selection and fixed-confidence identification are our specialization.

Posted pricing. A seller selects a buyer population _k_, posts a price _q<sub>t</sub>_ to a fresh buyer with hidden valuation \(X_{k,t}\sim\nu_k\), and observes only the purchase bit \(Y_t=\mathbf{1}\{X_{k,t}\ge q_t\}\). This is the accept/reject mechanism of posted-price auctions [17]. Screening _K_ populations for an \(\varepsilon\)-optimal mean valuation gives a threshold-query BAI problem. The objective here is mean valuation; revenue maximization is a different objective.

<sup>∗</sup>Corresponding author: `hoang.taduy@hust.edu.vn`.

**Khang Luong**<sup>1,2</sup> **Dinh Thai Son**<sup>1</sup> **Hoang Ta**<sup>1∗</sup> **Hung The Tran**<sup>2</sup> **Tuan Quang Dam**<sup>1</sup>

<sup>1</sup>Hanoi University of Science and Technology

<sup>2</sup>Quantum AI & Cyber Security Institute, FPT Corporation

