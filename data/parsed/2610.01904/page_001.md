# On the Impact of Coordinate Descent for Multi-Angle QAOA in the Independent Set Graph Problem

**Abstract**

Constrained combinatorial optimisation provides a mathematical framework for modelling a wide range of practical decision making problems, including energy network operation, financial portfolio optimisation, logistics, routing, and resource allocation. This paper studies parameter optimisation for the multi angle quantum approximate optimisation algorithm (maQAOA) applied to the maximum independent set problem, a canonical constrained graph based optimisation task. We propose a coordinate wise training framework for maQAOA that updates one variational parameter at a time by solving a sequence of one dimensional optimisation subproblems. For each selected coordinate, the method reconstructs the objective dependence on that parameter and moves directly to the parameter value that minimizes the training objective, or equivalently maximises the corresponding expected solution quality. While demonstrated specifically on maQAOA, the underlying theoretical principle, that the expectation value with respect to a given parameter can be analytically expressed as a finite Fourier series, is broadly applicable to general tasks solved via parameterised quantum circuits. Empirical evaluations on connected Erdős Rényi graph benchmarks demonstrate that this analytic approach significantly reduces the computational training cost required to reach target approximation ratios and yields superior convergence reliability compared to standard gradient based, stochastic, and derivative free baselines.

### 1 Introduction

**Background and Motivation.** The earliest practically useful quantum processors are expected to operate in the noisy intermediate scale quantum (NISQ) regime [Preskill, 2018]. In this regime, limited qubit counts, finite coherence times, and imperfect gate fidelities restrict the size and depth of executable circuits. Overcoming these hardware limitations to solve hard combinatorial optimisation problems remains a central goal in quantum computing and algorithms. These hardware constraints have motivated hybrid methods combining quantum and classical computation, in which the quantum processor is used to prepare and measure parameterised quantum states, while a classical routine performs the outer loop optimisation. Variational quantum algorithms (VQAs) are a central example of this paradigm: a parameterised quantum circuit (PQC) is evaluated on a quantum processing unit, and its parameters are updated by a classical optimiser using objective values derived from measurements [Cerezo et al., 2021, McClean et al., 2016].

Among VQAs, the quantum approximate optimisation algorithm (QAOA) is a prominent framework that leverages PQCs to solve combinatorial optimisation problems [Farhi et al., 2014, Blekos et al.,<tbc>

<sup>∗</sup>Joongheon Kim is the corresponding author. This research was supported by IITP (Institute for Information & Communications Technology Planning & Evaluation) funded by MSIT (Ministry of Science and ICT), Korea, (RS-2024-00439803, SW Star Lab) for Quantum AI Empowered Second-Life Platform Technology. 40th Conference on Neural Information Processing Systems (NeurIPS 2026). Workshop: SaTQuML: Secure and Trustworthy Quantum Machine Learning.

**Daeyeun Kim**<br> Korea University<br> Seoul, Republic of Korea<br> dk725@korea.ac.kr

**Seungcheol Oh**<br> Korea University<br> Seoul, Republic of Korea<br> seungoh@korea.ac.kr

**Joongheon Kim**<sup>∗</sup> Korea University Seoul, Republic of Korea<br> **joongheon@korea.ac.kr**

