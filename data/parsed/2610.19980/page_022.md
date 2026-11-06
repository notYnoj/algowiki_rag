\begin{tabular}{ccc}
Limitation & Evidence and consequence & Leverage \\
Closed representation
families & All 9 symmetry-crossover guillotine configurations finish at 1/6, and 9 MISR
configurations across several component paths finish at 4/3. Search cannot
reach a structure its representation and repair cannot express. & Very high \\
Weak exact-witness
feedback & Exact primal, dual, stabbing, and cut-tree witnesses are not turned into
move-level feedback; learned-model samples yield only 0, 1, 1 strict records. & Very high \\
Archive collapse and
model restart & Median duplicate-slot fractions reach 42.6%, 36.1%, 22.6%; each event fits a
fresh three-epoch model, so features do not accumulate. & Very high \\
No composition mechanism & Best certificates have only 12, 20, 9 objects; no operator combines two
certified blocks while preserving the ratio. & Very high \\
Discrete exact objectives & Small changes usually leave the ratio unchanged; the next useful change
needs several coordinated objects, explaining 64-98% plateaus. & High \\
Proposal-repair mismatch & Repair guarantees validity but can undo a coordinated proposal; high
valid-sample rates coexist with little exact progress. & High \\
Syntactic serialization & The model sees serialized coordinates, not canonical graphs, incidences,
duals, or cut trees, so capacity is spent relearning equivalent encodings. & Med.-high \\
\end{tabular}

\begin{tabular}{ccc}
\multicolumn{3}{c}{**Unit-square (unit\_square\_stab\_certificate\_v1): Guillotine (guillotine\_certificate\_v1):**} \\
**squares** & **\[\[x,y\], ...\]** & **rectangles** **\[\[x1,x2,y1,y2\], ...\]** \\
**critical\_lines** & **{vertical:\[...\],** & **n** & **number of rectangles** \\
 & **horizontal:\[...\]}** & **saved** & **max preserved by optimal** \\
 & **tau\_int** & **integer optimum (tau)** & **recursive cutting** \\
 & **tau\_lp** & **set-cover LP opt (tau\*)** & **destroyed** & **n - saved** \\
 & **score** & **tau\_int / tau\_lp** & **score** & **destroyed / n** \\
 & **integer\_lines** & **\["v3","h5", ...\]** & **dp\_states** & **number of DP states** \\
 & **solver\_status** & **"optimal"** & **optimal\_strategy** & **recursive cut tree {...}** \\
 & **certificate\_hash** & **"..."** & **solver\_status** & **"optimal"** \\
 & **certificate\_hash** & **"..."** & \\
\end{tabular}

7: Prioritized limitations supported by the evidence across all runs. "Leverage" estimates how strongly
fixing the limitation could change the reachable constructions, not how easy the fix is.

