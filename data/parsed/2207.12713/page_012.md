<tbc>for 40 iterations was taken with a confidence interval of 95%. The results of the first experiment are shown in Fig. 4. PostgreSQL sorts 231 runs with 150MB of `work\_mem` a bit slower than the naive approach, but it sorts 84 runs considerably faster. There could be several reasons for this: PostgreSQL implements prereading for a better disk access pattern, plus it sorts \(\langle\)key prefix, pointer\(\rangle\) pairs, which is more efficient [9,16] than pointer sorting.

Due to the space constraints, the results of the second experiment are shown in Fig. 4 as well. It is easy to see that the naive approach is the worst, binary heap is the second, and loser tree is the best one out of the considered three.

In the third experiment we compared the performance of the implemented algorithms using the `trip\_data` table of the TripData dataset. Unlike the previous experiment, this one uses real data. The table has approximately 128 million rows (over 20 GBs). We used a simple query of the same kind as the one in the first experiment:

1 **SELECT** medallion, hack\_license, vendor\_id, rate\_code,

2 store\_and\_fwd\_flag, pickup\_datetime, dropoff\_datetime,

3 passenger\_count, trip\_time\_in\_secs, trip\_distance,

4 pickup\_longitude, pickup\_latitude, dropoff\_longitude,

5 dropoff\_latitude

6 **FROM** trip\_data

7 **ORDER BY** trip\_time\_in\_secs

The number of runs was set to 80. The query plan is similar to the one in the first experiment, and is also shown in Fig. 3.

The results of the third experiment are presented in Fig. 5. The naive approach is predictably much slower than the other two. Similarly to the previous experiments, loser tree shows better performance than binary heap.

Based on the obtained results, we can answer the research questions given in the abstract as follows: 1) using a specialized data structure at the merge step

700K
PostgreSQL, 231 run, work_mem=150MB
Naive, 84 runs, 150MB
Binary heap, 84 runs, 150MB
650K
Loser tree, 84 runs, 150MB
PostgreSQL, 84 runs, work_mem=413MB
600K
Time, ms
550K
I
500K
I
450K
400K
Fig. 4: PostgreSQL comparison (exp 1), evaluation on synthetic data (exp 2).
Fig. 5: evaluation on real data (exp 3), TripData dataset.

1200K
Naive, 84 runs, 150MB Binary heap, 84 runs, 150MB Loser tree, 84 runs, 150MB
1100K
1000K
Time, ms
900K
800K
700K
600K

