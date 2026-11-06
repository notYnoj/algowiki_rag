<tbc>compute is required to attain some fixed level of performance over time? That is, we might say that an algorithm or architecture is two times better than another one if it achieves the same result on a benchmark with half the compute.

In this paper, we quantify pre-training algorithmic improvements by following the approach first presented by Erdil and Besiroglu (2022) in computer vision. Note that this is distinct from algorithmic progress in general, since we are not considering "post-training enhancements", such as chain-of-thought prompting, improvements to fine-tuning techniques, or the integration of search-based methods, which can significantly improve the performance of already-trained models on downstream tasks (e.g. programming or solving mathematics problems) (Davidson et al. 2023).

To this end, we produce a dataset of over 200 language models that have been evaluated, by others and by ourselves, on a range of popular language modeling datasets. We then use this data to estimate the rate of algorithmic progress. The language modeling datasets we focus on are Wikipedia (WikiText-103 and WikiText-2 (Merity et al. 2016)) as well as Penn Treebank (Taylor, Marcus, and Santorini 2003). We focus on evaluations on these datasets because these represent high-quality text data that have been used for many years to evaluate language models. Focusing on established benchmarks used throughout the development of neural language models provides continuity to compare models old and new.

## 1.1 Previous work

Studies across computer science, including linear programming, SAT solving, game playing, and deep learning, reveal algorithmic advances to be a vital driver of improved performance over time, on par with hardware improvements following Moore’s law. Algorithmic innovations enable solutions of larger problem instances, expand the scope of tractable problem classes, and reduce data and/or computation required to achieve fixed performance thresholds. Estimated rates of algorithmic progress vary substantially across domains and problem sizes, but often correspond to effectively doubling available compute resources for a task every 1-2 years (see Figure 1). However, progress is heterogeneous, with some domains stagnating while others improve rapidly.

## 1.1.1 Algorithmic progress in computer science

There is a small but growing literature on progress in software and algorithms for common computer science problems. Bixby 2012 reviews linear programming (LP) algorithm developments from 1985-1995 focusing on techniques to efficiently solve large problems. Increased computing power enabled the implementation of more advanced algorithms and the solution of larger models. They compare solution times using different versions of the CPLEX solver, indicating speedups of over 1000\(\times\) were achieved between 1988 and 1995. The paper concludes that advances in algorithms have been as important as hardware improvements in enabling solutions of much larger linear programs, opening up new domains of application.

Effective compute doubling time (months)
Our result
Reported estimate range
Moore's law doubling time
100
50
1K
Koch et al., 2022
20
Fichte et al., 2020
Bixby, 2002
Hernandez and Brown, 2020
Erdil et al., forthcoming
10
Dorner, 2021
1M
5
Our result
1B
Dorner, 2021
Erdil and Besiroglu, 2022
Sherry and Thompson, 2021
Dorner, 2021
2
Large language models
Linear Programs
SAT Solvers
Computer Vision
Stockfish (Computer chess)
Atari (Deep RL)
Avg of 57 textbook algorithms
State-based control (Deep RL)
Pixel-based control (Deep RL)
Domain

Figure 1: Estimates of effective compute doubling from algorithmic improvements across different domains. Blue dots represent central estimates or ranges; blue triangles correspond to doubling times for problems at different sizes (ranging from 1K to 1B); purple dashed line corresponds to the 2-year doubling time associated with Moore’s law. Koch et al. 2022 estimate range spans estimates for integer and mixed-integer linear programming.

