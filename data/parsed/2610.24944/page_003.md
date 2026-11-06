## 2 Research Setting

### 2.1 Problems and Evidence

We study research tasks with a reference result, an explicit budget and outputs that can be checked. A curator supplies the question and source material; the agent chooses the methods and experiments. To compare the agent’s output with the reference, we specify an evaluation rule, called a _ruler_. The ruler defines the submission format, feasibility conditions, objective, normalization and comparison value.<sup>1</sup>

The agent submits the information required to check its claim. For a packing task, it supplies coordinates and orientations. For an optimization bound, it may supply a dual vector or another certificate. For a proof task, it supplies witnesses and an argument explaining why the checked objects establish the stated claim.

For a minimization problem, we write \(V(x)\in\{0,1\}\) for the verifier’s feasibility decision, _f(x_) for the objective and _b_ for the reference value. We define the improvement as \(\Delta(x)=b-f(x)\). We also specify a positive _gain floor_ \(\delta>0\), the smallest improvement that the task counts as meaningful.<sup>2</sup> Épi accepts an improvement when

\(V(x)=1,\Delta(x)\ge\delta.\) (1)

For maximization, we instead define \(\Delta(x)=f(x)-b\). The positive floor excludes ties and admits an improvement exactly equal to the threshold. If a task imposes no minimum gain (\(\delta=0\)), we instead require \(\Delta(x)>0\). We fix the feasibility tolerances and gain floor before the investigation. The verifier uses the tolerances to check constraints, while Épi uses the floor to decide whether the improvement counts. For a rigorous numerical bound, we additionally require exact arithmetic or outward rounding that controls the numerical error.

We establish a new record by verifying feasibility and improvement over the best established result for the same problem and normalization. Each final artifact retains its comparison value, source and any rounding convention. For a theorem, the proof connects the verified objects to the full stated claim.

### 2.2 Campaigns and Sessions

We call a complete investigation a _campaign_. A campaign may contain several agent sessions and concurrent experiments. Each session gives the agent a bounded context in which to inspect evidence, modify code and choose its next action. Épi stores the research state outside that context and keeps experiments running across session boundaries. A later session retrieves the saved state and resumes the investigation.

The curator may provide a published construction as the initial reference. The agent can consult the literature, implement alternative methods and select experiments within the campaign’s budget. We keep model weights fixed in the campaigns reported here. The agent adapts its methods through experimental feedback, retrieved memory and independent review.

## 3 The Épi Research Loop

Figure 1 shows Épi’s research loop. The agent conducts experiments in verifiable environments and improves its methods through branching, hierarchical memory and independent review. We describe the evolving environments and the mechanisms supporting the agent’s self-improvement below.

### 3.1 Evolving Research Environments

Comparing research methods requires a common objective and consistent validity checks. We establish these before search by checking that the scorer reproduces the reference result, testing input validation and fixing<tbc>

<sup>1</sup>A reported benchmark score alone does not specify feasibility conventions, normalization or input validation. These choices determine whether two values measure the same quantity on valid objects. We introduce the ruler to make them explicit before search. <sup>2</sup>Counting every positive score change as progress can include differences due to reporting precision or routine post-processing. We derive the floor from the objective’s granularity and known transformations, and record its rationale with the task. For an integer objective with unit granularity, a floor of one admits a one-unit improvement.



