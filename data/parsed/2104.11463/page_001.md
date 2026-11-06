# Decision Tree Learning in CEGIS-Based Termination Analysis

Satoshi Kura<sup>1,2</sup>, Hiroshi Unno<sup>3,4</sup>, and Ichiro Hasuo<sup>1,2</sup>

<sup>1</sup> National Institute of Informatics, Tokyo, Japan

<sup>2</sup> The Graduate University for Advanced Studies (SOKENDAI), Kanagawa, Japan

<sup>3</sup> University of Tsukuba, Ibaraki, Japan

<sup>4</sup> RIKEN AIP, Tokyo, Japan

**Abstract.** We present a novel decision tree-based synthesis algorithm of ranking functions for verifying program termination. Our algorithm is integrated into the workflow of CounterExample Guided Inductive Synthesis (CEGIS). CEGIS is an iterative learning model where, at each iteration, (1) a synthesizer synthesizes a candidate solution from the current examples, and (2) a validator accepts the candidate solution if it is correct, or rejects it providing counterexamples as part of the next examples. Our main novelty is in the design of a synthesizer: building on top of a usual decision tree learning algorithm, our algorithm detects _cycles_ in a set of example transitions and uses them for refining decision trees. We have implemented the proposed method and obtained promising experimental results on existing benchmark sets of (non-)termination verification problems that require synthesis of piecewise-defined lexicographic affine ranking functions.

### 1 Introduction

_Termination Verification by Ranking Functions and CEGIS_ Termination verification is a fundamental but challenging problem in program analysis. Termination verification usually involves some well-foundedness arguments. Among them are those methods which synthesize _ranking functions_ [16]: a ranking function assigns a natural number (or an ordinal, more generally) to each program state, in such a way that the assigned values strictly decrease along transition. Existence of such a ranking function witnesses termination, where well-foundedness of the set of natural numbers (or ordinals) is crucially used.

We study synthesis of ranking functions by CounterExample Guided Inductive Synthesis (CEGIS) [28]. CEGIS is an iterative learning model in which a synthesizer and a validator interact to find solutions for given constraints. At each iteration, (1) a synthesizer tries to find a candidate solution from the current examples, and (2) a validator accepts the candidate solution if it is correct, or rejects it providing counterexamples. These counterexamples are then used as part of the next examples (Fig. 1).

Functional
Artifac
Avg
Evaluated
reliable
reusable

