each data set. Here, we have focused on the largest data set, 1MV4ME. Results for all data sets are shown in Fig. 14 (b).

For Ho-ICA, Fig. 10 reveals a speedup of at least **48.32%** as we increased the number of partitions and the numbers of mappers/reducers from 8 to 16. Subsequently, a speedup of at least **43.49%** was observed when further increasing them from 16 to 32. Finally, a speedup of at least **34.41%** was noticed when further increasing them from 32 to 64. However, the speedup achieved was not linear; doubling the mappers and reducers does not halve the time taken. As the number of partitions increases, the overhead of writing more files and shuffling comes into effect.

This observed speedup can be attributed to the more partitions of the graphs, processed by an increased number of processors in parallel. Smaller-sized partitions contribute to a reduced computational load on each processor, leading to higher speedup. However, the diminishing speedup suggests that increasing the number of partitions does not continuously improve performance. Higher number of partitions allows more instances to belong to multiple partitions, increasing the potential for inter-partition duplication. This leads to redundant work in different processors. Moreover, excessively small input splits can negatively impact Hadoop performance, introducing overhead related to task setup, communication, and coordination. Conversely, overly large input splits can result in an uneven distribution of processing workload among nodes, leading to inefficient resource utilization. Hence, determining the optimal number of input splits is crucial for optimizing Hadoop job performance. If the objective is to maximize efficiency, employing 16 Mappers/Reducers appears to be the most effective choice as it provides the best speedup. However, in case there is surplus processing power available, 64 Mappers/Reducers still yield a respectable speedup of around 30% while taking the least amount of time.

2) Effect of Layer Distribution: As evident from Figure 10, layer distribution does not significantly impact the efficiency of Ho-ICA. This behavior stems from the algorithm’s implementation, where all layers are processed within the same Map/Reduce job, enabling effective load balancing and ensuring uniform load distribution among processors.

## D. Response Time and Scalability: Real-World Graphs

We have also employed real-world graphs to demonstrate scalability and speedup as the characteristics of a real-world graph

may be quite different from that of a synthetically generated graph. Two real-world data sets - Amazon and LiveJournal - were used with sizes of 0.74MV2.6ME and 4.9MV69ME, respectively. These data sets were partitioned into 8, 16, 32, and 64 partitions, and experiments were performed using same number of mappers and reducers for each.

**Amazon (0.74MV2.6ME)**: The speed in Figure 11, is very similar to the speed up seen for synthetic graphs. Across distributions, we observe speedups of at least **42.26%**, **40.01%** and **33.15%** going from 8 to 16, 16 to 32, and 32 to 64 mappers/reducers, respectively.

As the focus of this paper is on the composition algorithm, its correctness, and implementation using Map/Reduce, Figure 12 shows only the composition time for the Amazon data set. Note that there were no embedded substructures as this is a real-world data set. From Figure 12, it can be seen that composition takes most time in iteration 1 and is almost flat for other iterations. This is because, in iteration 1, **all** edges are composed whereas in subsequent iterations, only _top-beam_ substructures are composed.

On the other hand, in Figure 13 the same composition time is displayed for the synthetic data set 1MV4ME. As this data set has an embedded substructure of size 5, iterations 3

HoICA 50-50 HoICA 70-30 HoICA 90-10 49.99% 200 49.99% 180 68.92% 160 49.1% 44.5% 140 44.5% 120 100 44.2% 39.1% Time in secs 80 43.49% 34.41% 60 35.02% 40 20 0
8MBR 16M16R 32M32R 64M64R Approach and Distributions

HoICA 50-50 HoICA 70-30 HoICA 90-10 49.99% 40 43.41% 35 41.00% 30 42.50% 41.00% 25 41.03% 34.74% Time in secs 20 33.15% 15 40.01% 23.9% 10 5
0 8MBR 16M16R 32M32R 64M64R Approach and Distributions

Total Map Time Total Reduce Time Total Time 5.00 4.50 4.00 3.50 3.00 2.50 TIME IN SECS 2.00 1.50 1.00 0.50 0.00 ITERATION 1 ITERATION 2 ITERATION 3 ITERATION 4

Total Map Time Total Reduce Time Total Time 18.00 16.00 15.51 14.00 13.36 12.00 11.90 10.00 9.87 TIME IN SECS 8.00 7.30 6.00 4.87 4.00 4.56 4.56 2.00 2.74 2.09 2.15 0.00 0.90 ITERATION 1 ITERATION 2 ITERATION 3 ITERATION 4

Fig. 10: Speedup Analysis: 1MV4ME Data Set

Fig. 11: Speedup Analysis: Amazon Data Set

Fig. 12: Composition Job for Amazon Data Set

Fig. 13: Composition Job for 1MV4ME Data Set

