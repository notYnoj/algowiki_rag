<tbc>measure pair informativeness within comparison graphs. These methods assume every selected pair requires human input. SGS differs by additionally classifying each candidate as human-required or transitivity-resolvable based on its surprise score.

### 2.4 Position Bias in LLM Comparisons

LLMs and VLMs exhibit systematic position bias in pairwise comparison tasks \[22,25\], where the order in which items are presented affects the output. The flip test--querying both orderings (_A,B_) and (_B,A_)--is a standard mitigation. We incorporate a calibrated version of the flip test as one component of our Surprise Score, converting position-bias-cancelled confidence into a continuous uncertainty signal.

## 3 Method

### 3.1 Problem Setup

Let X={_x_<sub>1</sub>_,...,x<sub>n</sub>_} be a set of items with unknown latent scores \(\{s_i\}_{i=1}^n\). The goal is to recover a ranking \(\hat{\mathcal{R}}\) that is maximally consistent with the ground-truth ordering while minimizing the number of _human_ pairwise judgments. We assume access to two complementary supervision channels: (i) a noisy VLM-based scorer that can assign pointwise scores to individual items and produce noisy pairwise preferences, and (ii) a reliable human oracle that returns the comparison outcome \(y_{ij}\in\{0,1\}\) for a queried pair (_i,j_).

Our design principle is to use the VLM as a _question prioritizer_ rather than as an annotator replacement. Accordingly, the VLM is used to (a) construct an initial coarse ordering, (b) estimate which comparisons are ambiguous, and (c) support low-risk automatic resolution. Human effort is reserved for comparisons whose ambiguity is high enough that automatic resolution is likely to be unreliable.

### 3.2 Method Overview

SGS first calibrates the VLM against a small set of human comparisons and uses the resulting agreement to warm-start an Elo state. When agreement is sufficient, a bottom-up MergeSort scheduler proposes local cross-run candidate pairs, which are scored by a composite surprise metric. High-surprise pairs are sent to humans, while low-surprise pairs are resolved only under a capped automatic-resolution policy; otherwise, the method falls back to Active Elo. Algorithm 1 summarizes the procedure.

### 3.3 Round-0 Calibration, Pre-Scoring, and Warm Start

_Calibration._ We first draw _n_<sub>cal</sub> unique random pairs and query both the VLM and the human oracle. Let \(\tilde{y}_{ij}\) denote the VLM decision and _y<sub>ij</sub>_ the human

