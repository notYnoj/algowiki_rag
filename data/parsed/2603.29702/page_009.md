





Figure 4: Overfitting Issue With Naïve Sub-sampling Approach for ED

In all of the following figures, bold edges have weight 0, and the rest have weight 1.

(a) Suppose we sample the first and the third sub-intervals, setting weights in the second and the fourth sub-intervals to zero, we find a good path (dotted) with a weight of 2. Naïvely, since we sample half of the sub-intervals, we estimate that the actual best path between these vertices has a length of 2/(1/2)=4. However, this estimate can be inaccurate because we cannot distinguish between the following good and bad cases:

(b) Good Case: the optimal path (dotted) indeed has a length of 4, consistent with our estimate.

(c) Bad Case: The optimal path (bottom path) has a length of 5, which is longer than our estimate. Notice that this is the case even though the second and fourth sub-intervals have the same number of weight-0 edges as in the good case. In particular, even in the scenario when we sampled the even sub-intervals instead of the odd ones (and in many other scenarios), we would still arrive at the same overly-optimistic estimate. The key issue is that both the odd and even sub-intervals are consistent with some potentially good candidate paths (top path and bottom path, respectively), but there is no single good path that is consistent with both.

