over-fits mildly (validation F1 on 200 patches 0.775 at epoch 49, 0.761 at 299), the 10 % layer does not (0.453 at epoch 49 before its schedule, 0.749 at 249, 0.745 at 299), so an early-stopped baseline could recover part of the 0.020; a 30-epoch baseline at 10 % (a tenth of the steps) was not run. The WS layer's 10 % run cost 1.6 h on an A100 (19 s per epoch, 300 epochs, the extraction of the predicted markers from epoch 100 included) and the baseline's 0.3 h, so the usual 5-10\(\times\) price of the WS layer holds here too.<tbc>

**-** **One seed, one subset draw.** The subsets are nested and shared by the two methods, which removes the subset draw from the paired differences but not from the absolute curves; a second draw and a second seed at 10 % (two jobs per method, 2 h each) would settle whether 0.020 is the typical margin or an upper draw, and a 5 % point (133 images) would say whether the gap keeps opening. The replicates were run the same day: see the addendum below.

**Addendum, 24 October 2026 (later the same day): the 10 % point replicated.** Four more runs at 10 %, two per method: a second training seed on the same 266 images (`--seed 1`, runs `dist\_bg\_p10\_s1` / `unet\_dist\_p10\_s1`) and the first seed on a second subset draw (`--subset-seed 1`, runs `dist\_bg\_ p10\_d1` / `unet\_dist\_p10\_d1`; a different 266 images of fold 1); layer runs on ruche, baselines on jacobian, same recipe and tuning as above. Results (F1 / PQ / AJI on fold 2; the full rows and intervals are in `data\_efficiency.md`):

The margin holds: +0.015 to +0.020 F1 and +0.011 to +0.015 PQ across the three seed / draw pairs, every interval clear of zero, with the WS layer at F1 0.765 in all four runs and the baseline at 0.745-0.749. The spread between replicates is 0.004 F1 for the baseline and 0.000 for the WS layer, so the 0.020 of the first pair was the upper end of a stable 0.017 \(\pm\) 0.003, not a lucky draw. The mechanism reads the same in every replicate: the baseline's fold-3 tuning picks threshold 0.5 each time and leaves 24 % of the nuclei unmarked, the WS layer's picks 0.2 and leaves 14-16 %; the segmentation of the matched nuclei is equal (SQ 0.811-0.815 against 0.812-0.817); the oracles with ground-truth markers are 0.839-0.842 for the WS layer against 0.812-0.817 for the watershed. The baseline's mild over-fitting under the held step count is not systematic either (validation F1 at epoch 49 \(\rightarrow\) 299: 0.775 \(\rightarrow\) 0.761, 0.750 \(\rightarrow\) 0.760, 0.774 \(\rightarrow\) 0.771), so early stopping would not close the gap. The conclusion of the section is unchanged and now rests on three pairs: at a tenth of the fold the structured layer is a small, reliable step ahead of the tuned watershed baseline; from a quarter on it is not.

## S Marker selection in the gradient path: candidate strengths trained through the solve

Added 24-25 October 2026 (side session; three training jobs on ruche's A100 partition, one of them stopped). Section 11.5 left the WS layer 0.001-0.008 F1 /

\begin{tabular}{ccccccccccccc}
10 % run & WS layer & \multicolumn{2}{c}{watershed baseline} & \multicolumn{2}{c}{WS layer - baseline F1 / PQ (paired)} & \multicolumn{2}{c}{unmarked nuclei, layer / baseline} & \multicolumn{2}{c}{} & \multicolumn{2}{c}{} & \multicolumn{2}{c}{} \\
seed 0, draw 0 & 0.765 / 0.620 / 0.635 & 0.745 / 0.605 / 0.620 & +0.020 \[+0.017, +0.023\] & / & +0.015 \[+0.013, +0.017\] & 13.9 % / & 24.5 % & & & & & \\
seed 1, draw 0 & 0.765 / 0.620 / 0.636 & 0.749 / 0.609 / 0.623 & +0.015 \[+0.012, +0.018\] & / & +0.011 \[+0.009, +0.014\] & 15.8 % / & 23.7 % & & & & & \\
seed 0, draw 1 & 0.765 / 0.624 / 0.633 & 0.749 / 0.612 / 0.624 & +0.017 \[+0.014, +0.020\] & / & +0.012 \[+0.010, +0.014\] & 15.0 % / & 24.4 % & & & & & \\
seed 0, draw 0, jacobian & 0.765 / 0.621 / 0.636 & - & - & - & - & - & - & 15.2 % / & - & & & \\
\end{tabular}

