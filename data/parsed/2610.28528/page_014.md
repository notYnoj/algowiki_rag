<tbc>For three hard instances, classical post-processing discovered independent sets strictly larger than any in the seed pool, and on one of them, `L12\_seed829`, it reached the certified optimum and recovered its entire 18-configuration manifold. All 15511 improved solutions passed independence, maximality, and target-cardinality validation. Because a local search from the same seeds reaches the same sizes on two of the three, the improvements show what recombination can extract from near- optimal seeds rather than an advantage specific to cluster updates.

The practical consequence is that solution counts and diversity metrics reported directly from quantum hardware understand what a run has determined, by a median factor of 14 on this dataset and by up to four orders of magnitude in the extreme case. For any application whose figure of merit is the number or diversity of optimal configurations rather than a single best solution, the quantity worth reporting is the post-processed count, since the recovery costs seconds to minutes of laptop time per instance. Because the cluster exchange mechanism is not specific to MIS, the same measurement can be made for any problem whose solutions admit a binary encoding and a well-defined overlap structure, which is where we expect this accounting to matter next.

## ACKNOWLEDGMENTS

AJO would like to thank Graham Enos for his careful review of this manuscript. HGK would like to thank Jon Machta for insightful conversations on cluster updates and thanks Mark Lundgaard, Rasmus Munk, Nicolai Nørregaard, and Eric Vildgaard for inspiring the work. MJAS would like to thank Sri Elaprolu for his leadership and support. This work received no external funding.

The authors acknowledge the use of AI tools to assist with code generation, data analysis, and drafting and editing parts of the manuscript text. The manuscript was written and reviewed in depth by the authors, who take full responsibility for its content.

## DATA AND CODE AVAILABILITY

The quantum-hardware measurement records, problem instances, and reference values analyzed in this work are those distributed with Ref. [7] and are publicly available at Ref. [17].

