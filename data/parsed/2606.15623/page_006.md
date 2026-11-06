<tbc>**Algorithm 1** Surprise-Guided MergeSort (SGS)

Require: Items X, VLM annotator A, human oracle O, budget _B/_round, rounds _T_<br>
\(\bar{v}\leftarrow\mathcal{A}.\text{scoreAll}(\mathcal{X});\pi_0\leftarrow\text{argsort}(\bar{v})\)<br>
\(\alpha\leftarrow\text{Calibrate}(\mathcal{A},\mathcal{O},n_\text{cal})\)<br>
Initialize Elo **R** via Eq. (4)<br>
if \(\alpha<0.70\) then<br>
   Fallback: run Active Elo for all T rounds; return<br>
end if<br>
\(\mathcal{M}\leftarrow\text{MergeSortScheduler}(n,\pi_0)\)<br>
for t=1 to T do<br>
   if M.isComplete() then<br>
**Fallback:**<br>
refine<br>
remaining<br>
budget<br>
with<br>
Active<br>
Elo<br>
;<br>
break<br>
   end if<br>
\(\mathcal{C}_\text{unk}\leftarrow\{(i,j)\in\mathcal{M}.\text{getCandidates}():\text{unknown}\}\)<br>
   for \((i,j)\in\mathcal{C}_\text{unk}\) do<br>
\(S(i,j)\leftarrow\text{SurpriseScore}(i,j,\mathcal{A},\mathbf{R})\triangleright\)<br>
Eq. (8)<br>
   end for<br>
   Sort C<sub>unk</sub> by S descending; allocate top-_B_ to H, rest to I<br>
   for \((i,j)\in\mathcal{H}\) do<br>
\(y_{ij}\leftarrow\mathcal{O}(i,j)\)<br>
;<br>
update<br>
**R**<br>
,<br>
M<br>
   end for<br>
   for \((i,j)\in\mathcal{I}\) (up to C<sub>t</sub>; C<sub>t</sub> via Eq. (9)) do<br>
\(\hat{y}_{ij}\leftarrow\text{InferFromElo}(\mathbf{R},i,j)\)<br>
;<br>
update<br>
M<br>
   end for<br>
   M.completePass(**R**)<br>
Recalibrate A from accumulated human labels (optional)<br>
end for<br>
return<br>
M.getRanking()

### Adaptive fallback.

Warm-starting is always performed, but the MergeSort backbone is only used when the calibration agreement is sufficiently high. If \(\alpha<0.70\), SGS abandons MergeSort and switches to Active Elo for all remaining rounds. This prevents a poor pre-order from inducing cascading errors in later merge passes.

## 3.4 Transitivity-Aware MergeSort Scheduler

When \(\alpha\ge 0.70\), SGS initializes a bottom-up MergeSort scheduler from the VLM order \(\pi_0\). At each pass, only cross-run boundary pairs are considered, preserving the _O(n_log_n_) structure while avoiding global pair enumeration. The scheduler maintains a directed set K of reliable outcomes obtained from human labels or admitted inference, and skips pairs implied by the transitive closure of K. During pass completion, known relations are respected first; unresolved pairs are decided by Elo only when the rating gap is large (default \(|R_i-R_j|\ge 60\)), otherwise by the inherited run order. Transitivity is propagated only from reliable edges, not from weak VLM defaults.

