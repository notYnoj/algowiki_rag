<tbc>coordinates on one branch and change the contact pattern on another. It can compare both methods before allocating more compute.

**Hierarchical memory.** Drawing on work on human and agent memory (Atkinson and Shiffrin, 1968; Packer et al., 2023; Park et al., 2023), Épi uses hierarchical memory to accumulate and reuse research experience. Short-term memory supports the current investigation, while long-term memory retains experience for subsequent research. As illustrated in Figure 1, memory records include research context, lessons that capture reusable findings, and dead ends that document unproductive approaches and why they were abandoned. The agent retrieves these records to guide its next experiment and updates them as new evidence becomes available.

Épi stores code, artifacts and detailed research notes in a persistent filesystem and keeps retrievable lessons and dead ends in a memory store outside the model context. At a session boundary, the agent records its findings and a handover note identifying the current state and next steps. A subsequent session receives relevant memory records and can open the referenced files as needed. This supplies a bounded working context without replaying the full history of earlier sessions.

**Independent review.** The agent that develops a method also chooses which evidence to examine, giving its assessment a limited perspective. Prior work on self-correction motivates adding feedback from outside the agent’s own reasoning process (Huang et al., 2024); research on reward hacking further motivates checking whether a score increase reflects the intended task (Denison et al., 2024). Épi combines a separate review of research progress with artifact verification under the fixed ruler.

Épi supplies a review model with the score trajectory, attempted approaches, retrieved findings, comparison baseline and resource use. The reviewer assesses what the evidence supports and whether the agent’s interpretation of progress is justified. Épi records this assessment for subsequent sessions, and the agent uses it when selecting further experiments or revisiting a branch. We use a different model for an independent review and record the reviewer’s identity. The reviewer evaluates the research direction; the isolated verifier checks the candidate’s validity and gain.

**Research transparency.** Épi records alternative implementations, their experimental outcomes, and the assessments used to guide subsequent work. These records allow researchers to compare branches, inspect the evidence associated with a methodological change, and revisit the implementation on which a conclusion depends. Lessons summarize reusable findings, while references to code and experimental artifacts let researchers examine the evidence behind those summaries.

**Execution support.** We use Breadboard as Épi’s execution infrastructure. Breadboard provides isolated experimental environments, supports long-running jobs across model sessions and stores research history, including code, branch states and experimental outputs. It also runs the fixed verifier and preserves the state needed to recover and continue an investigation. The agent uses these services to execute experiments, inspect results and resume its research across sessions.

## 4 Experimental Results

### 4.1 Setup and Counting

We ran Épi over a few days using OpenAI frontier models (GPT-5.6 Sol and GPT-6-Astra). Computational budgets were set per problem. Published methods and constructions supplied starting points for several campaigns, including the packing case in Section 5.1. Each comparison uses the same task and evaluation convention for the reference and final artifact. All record comparisons are based on literature and registry references available as of September 16, 2026.

The current collection contains **120 record-setting results: 20 numerical bound records across 12 families** and **100 construction records across eight families**. A separate Tuza theorem extension brings the report to 21 families in total and is excluded from the record count.



