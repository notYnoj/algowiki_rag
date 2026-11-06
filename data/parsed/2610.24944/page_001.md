# Épi: Towards a Persistent, Self-Improving Agent for Autonomous Research

**Yue Huang**<sup>1,2</sup> **Zhangchen Xu**<sup>1,3</sup> **Xiaonan Luo**<sup>1,2</sup> **Zheyuan Liu**<sup>1,2</sup> **Lichi Li**<sup>1</sup>

**Yiping Wang**<sup>3</sup> **Peiyang Song**<sup>7</sup> **Eric Gabriel Ramos**<sup>4</sup> **Enze Xie**<sup>6</sup> **Olexandr Isayev**<sup>7</sup>

**Paul Liang**<sup>8</sup> **Nouha Dziri**<sup>9</sup> **Huan Sun**<sup>10</sup> **Jianfeng Gao**<sup>11</sup> **Ying Liu**<sup>5</sup> **Misha Sra**<sup>12</sup>

**Xiangliang Zhang**<sup>2</sup> **Alex Pentland**<sup>8,13</sup> **Zichen Chen**<sup>1,12,13</sup>

**Abstract**

We present Épi, an autonomous research agent that sustains investigations across model sessions and evolves its methods through accumulated experience. Épi combines persistent research history, hierarchical memory, branching and independent review to maintain research continuity, learn from experiments, and explore and revisit alternative approaches. Its experiments run across session boundaries, and a fixed verifier evaluates their outputs. Épi produced 120 record-setting results, comprising 20 numerical bound records across 12 families and 100 construction records across eight families. These include an approximately 84-fold narrower interval for the _n_-queens constant and a more than 3.6-million-fold narrower rigorous interval for the quartic Feigenbaum attractor dimension. Exact dual certificates establish that the Cohn–Elkies linear-programming bound cannot be sharp in dimensions 10 and 11. Beyond numerical improvements, Épi gives a computer-assisted proof of Tuza’s conjecture for split graphs with an eight-vertex clique part and at most three triangle-active neighborhood types, with arbitrary multiplicities. We extend this research process to algorithmic coding with Épi-turbo, a lightweight configuration that develops executable solvers for tasks including vehicle routing, scheduling and production planning. On 30 FrontierOR tasks, Épi-turbo achieves a 5.4% higher total benchmark score than x at 64% of its model cost, using the same underlying model and reasoning effort. Épi is designed to support human understanding by connecting computational results to explicit methods and mathematical arguments that researchers can examine and build upon.

### 1 Introduction

Autonomous research agents must conduct experiments, interpret results and revise their methods over many interactions. FunSearch and AlphaEvolve demonstrate how agents can combine code generation with executable evaluation to discover new programs and constructions (Romera-Paredes et al., 2024; Novikov et al., 2025). The AI Scientist-v2 extends automation to an experimental workflow (Yamada et al., 2025). When an investigation requires more work than one model session can support, however, the agent must manage three additional challenges.

**First, maintaining research continuity. Experiments and research decisions span multiple model sessions.** To continue an investigation, the agent needs access to running jobs, code, intermediate results and reasons for earlier decisions. Kosmos maintains a shared research state, InternAgent-1.5 organizes long-horizon memory, and ScienceFlow archives recoverable execution states (Mitchener et al., 2025; Feng et al., 2026; Zhao et al., 2026). These mechanisms preserve information across steps. As the history grows, the agent must also select what a bounded model context needs: the current experimental state, relevant lessons and reasons



1 Bake AI 2 University of Notre Dame 3 W University of Washington 4
Stevens Institute of Technology 5
Scale AI 6 NVIDIA 7 CMU Carnegie Mellon University 8 MIT 9 Cohere Labs 10 The Ohio State University 11 Microsoft UCSB UC Santa Barbara 13 Stanford University Technical Report October 2026



Blog Results on GitHub

arXiv:2610.24944v1 [cs.CL] 18 Oct 2026

