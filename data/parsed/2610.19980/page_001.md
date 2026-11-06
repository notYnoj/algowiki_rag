# Towards Learning-Guided Discovery of Extremal Geometric Constructions: A PatternBoost Study

### Abstract

Extremal constructions play a central role in the design and analysis of algorithms. Integrality-gap instances expose the limitations of relaxations, while hard configurations reveal the structural sources of computational difficulty. Such constructions, however, are still typically discovered by expert researchers through a slow and largely manual process. This paper investigates how machine learning can accelerate their discovery and thereby support algorithm design and analysis. We build on PatternBoost, a recent framework that alternates local search with generation from a trained transformer and has shown promise in finding mathematical constructions. We use its Explorer implementation to investigate three problems: integrality gaps for maximum independent set of rectangles, integrality gaps for stabbing unit squares with axis-parallel lines, and hard instances for recursive guillotine cutting. By exploring a range of representations of candidate constructions, the local search operations used to modify them, and the surrogate model used to rank candidates before exact verification, we carefully adapt the framework to these combinatorial geometry problems.

While naive representations and search strategies fail to find non-trivial instances, our tailored adaptation discovers numerous non-trivial constructions. For stabbing unit squares, the method reaches a gap of 20/13≈1.54, which improves on the best known lower bound of 3/2 in the literature. Purely automated search converges rapidly and then plateaus, prompting the question of what is required to push the bound higher still. We find that the diversity of the initial instance set plays an important role. With modest expert

input in the form of a structured staircase construction, the system reaches an improved integrality gap of 14/9≈1.555. These results demonstrate that machine learning and domain expertise can be combined to discover new extremal constructions that advance algorithmic lower-bound evidence.

### 1 Introduction

Extremal constructions are a central driver of progress in algorithm design and analysis. An integrality-gap instance exposes the limits of a relaxation by separating its value from the true optimum; a hard configuration reveals why a class of algorithms cannot go further. Such constructions identify the structural obstacles that any successful algorithm must overcome, and they often become the starting point for new theory. For computational geometry problems, progress has repeatedly depended on a single carefully crafted construction. Yet these constructions are still usually found by expert researchers through a slow, manual, and problem-specific process.

This paper asks whether machine learning can accelerate the discovery of such extremal objects. We build on PatternBoost [11], a recent framework that alternates local search with generation from a transformer trained on high-scoring candidates, using its Explorer implementation [3]. Applying this framework to combinatorial geometry is far from automatic. Candidate objects have rich geometric structure, and a single combinatorial object has many coordinate encodings, since translating, reflecting, rotating, or slightly perturbing it without changing which objects overlap leaves the objective unchanged. The true objective itself often requires solving a difficult optimization problem; and the learner only succeeds if the representation exposes the relevant combinatorial signal. We therefore redesign the three components that determine the effectiveness of the search: the representation of candidate objects, the local search operations, and the surrogate model used to rank candidates before exact verification.

We study three problems that capture different

<sup>1</sup>School of Computer Science, University College Dublin, Ireland <sup>2</sup>Quinn School of Business, University College Dublin, Ireland <sup>3</sup>Indraprastha Institute of Information Technology Delhi, India <sup>4</sup>New York University Abu Dhabi, UAE <sup>5</sup>Computer Science Program, New York University Abu Dhabi, UAE <sup>6</sup>Center for Interdisciplinary Data Science & AI (CIDSAI), NYU Abu Dhabi, UAE

Deepak Ajwani,<sup>1</sup> Paula Carroll,<sup>2</sup> Rishikesh Gajjala,<sup>4</sup> Ananta Manoranjan,<sup>4</sup> Ryan O’Connor,<sup>1</sup> Rajiv Raman,<sup>3</sup> Saurabh Ray,<sup>5,6</sup> and Aimen Taha<sup>2</sup>

arXiv:2610.19980v1 [cs.CG] 14 Oct 2026

