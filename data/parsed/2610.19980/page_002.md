<tbc>forms of extremal construction in combinatorial geometry. For the maximum independent set of rectangles, we seek instances where a natural relaxation substantially overestimates the size of the largest pairwise disjoint subfamily of rectangles. For stabbing unit squares with axis-parallel lines, we seek configurations where the fractional stabbing number is significantly smaller than the minimum number of horizontal and vertical lines needed to stab all squares. For recursive guillotine cutting, we seek configurations that are difficult for algorithms restricted to recursively partitioning the instance by guillotine cuts.

A direct application of the pipeline fails. Naive representations and generic local search rediscover only trivial constructions or stall at the smallest, easiest gap instances. After tailoring the pipeline to the geometry and combinatorics of the problems, however, the system discovers non-trivial constructions for all three problems. For unit-square stabbing, the fully automated system reaches a gap of 20/13≈1.54, exceeding the best known lower bound of 3/2 for the problem. For MISR and guillotine cutting, the constructions found (3/2 and 1/3) do not improve on the best known bounds (Section 3); for these two problems the contribution lies in the method and its analysis rather than in new extremal objects.

Our experiments show that this success depends on co-design. We systematically vary the representation, local search, and surrogate components across the three problems, and independently verify every reported construction. No single component is sufficient on its own, and the best construction is rare in the design space: for each problem, only one of the 27 configurations we tried reaches its best value, so obtaining it demands careful exploration of the component choices.

Pure automation, however, has a clear limit. The search improves rapidly and then plateaus well before its time budget is spent, and simply running it longer does not move it further. Analyzing the learning dynamics, we find that the plateau is one of reachability: within a fixed search setup the automated loop cannot leave the region it starts in. This leads to a human-in-the-loop strategy: use domain expertise not to hand-design the final construction, but to recast the problem in a structured formulation in which the extremal obstruction is close to native. For unit-square stabbing this is a staircase construction that lifts a one-dimensional family of intervals to unit squares by products. With this modest expert input, the unit-square stabbing gap increases further to a certified value of 14/9≈1.555, _improving on the best known lower bound of_ 3/2 _by a wider margin still._

These results support a broader view of machine<tbc>

<tbc>learning as a partner in algorithm engineering. The role of the model is not to replace mathematical insight, but to amplify it: exploring large construction spaces, identifying promising patterns, and allowing expert guidance to be applied where it is most valuable.

In summary, we contribute:

1. an adaptation of PatternBoost, through its Explorer implementation, to extremal construction discovery in combinatorial geometry. The adaptation includes problem-specific representations, local search operations, and surrogate models. This turns a pipeline that finds only trivial instances into one that discovers exactly verified constructions, including a 20/13≈1.54 integrality gap for unit- square stabbing that improves on the best known lower bound of 3/2;<tbc>

2. a systematic ablation study across three pipeline components and three target problems, with independent verification of every certificate, showing that representation, search, and surrogate ranking must be co-designed: for each problem, only one of the 27 configurations reaches its best value; and<tbc>

3. an analysis of the plateau reached by purely automated search, together with a human-in-the-loop strategy based on an expert-structured staircase construction. This strategy raises the unit-square stabbing gap further to 14/9≈1.555, exceeding the prior best known lower bound and demonstrating productive collaboration between machine learning and domain expertise.

The remainder of the paper is organized as follows. Section 2 surveys model-guided construction search, machine learning for combinatorial optimization, and instance-hardness methods. Section 3 defines the three problems and their exact objectives. Section 4 describes the PatternBoost/Explorer framework. Section 5 explores the design space of components and presents the constructions found, including the unit-square result that beats the best known bound. Section 6 reports the human-in-the-loop staircase construction. Section 7 concludes and outlines future directions, and Section 8 covers reproducibility.

## 2 Related work

### 2.1 Model-guided construction discovery

A growing body of work uses machine learning to search for explicit mathematical constructions. Wagner showed that a reinforcement-learning method, the deep cross-entropy method, can produce explicit constructions and counterexamples to conjectures in extremal<tbc>

