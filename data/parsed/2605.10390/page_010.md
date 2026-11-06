is needed which eliminates round trips to memory storage required during pre-processing, achieving a 3x improvement in bandwidth efficiency over state-of-the-art Bonsai on 16KB-32GB data sets as shown in Figure 10. Optimizing the count variable width _w<sub>c</sub>_ based on the reduction of subtree size with increasing merge tree depth improves bandwidth efficiency and data compression.

FractalSortCPU is useful for sorting data streaming scenarios, and implementation on CPU enables both significant performance improvements and greater accessibility due to lower adoption costs. Together with the FPGA implementation [54], the FractalSort family provides bandwidth-efficient sorting across heterogeneous platforms. Future work will involve exploration of the GPU platform for higher parallelism and data access rates and exploration of novel high-precision sorting optimizations.

## REFERENCES

[1] B. G. R. R. B. and P. S. Yu, "CellSort: High Performance Sorting on the Cell Processor." In: _Proc. VLDB_ (2007), pp. 1286–1297.

[2] R. M. J. T. G. Alonso, "Sorting networks on FPGAs." In: _VLDB_ 21 (2012), pp. 1–23. https://doi.org/10.1007/s00778-011-0232-z.

[3] S. J. S. X. R. Arvind, "Terabyte sort on FPGA-accelerated flash storage." In: _International Symposium on Field-Programmable Custom Computing Machines (FCCM)_ (2017).

[4] S. J. S. X. S. Arvind, "Terabyte Sort on FPGA-Accelerated Flash Storage." In: _Proceedings of the 25th IEEE International Symposium on Field-Programmable Custom Computing Machines (FCCM)_ (2017).

[5] F. Berthelot, F. Nouvel, and D. Houzet, "Partial and dynamic reconfiguration of FPGAs: a top down design methodology for an automatic implementation." In: _Proceedings 20th IEEE International Parallel Distributed Processing Symposium_ (2006), 4 pp. DOI: 10.1109/IPDPS.2006.1639466.

[6] M. C. D. B. R. B. Bordawekar, "PARADIS: An efficient parallel algorithm for in-place radix sort." In: _Very Large Data Bases (VLDB)_ (2015).

[7] M. A. R. X. C. L. Y. H. D. L. J. Bradley, "Spark SQL: Relational data processing in spark." In: _International Conference on Management of Data_ (2015). URL: https://sortbenchmark.org/.

[8] L. Canese et al., "A Novel Digital Equalizer Based on RF Sampling Beyond GHz." In: _IEEE Access_ 12 (2024), pp. 92560–92572. DOI: 10.1109/ACCESS.2024.3422802.

[9] J. Chhugani et al., "Efficient implementation of sorting on multi-core SIMD CPU architecture." In: _Proceedings of the VLDB Endowment_ 1(2) (2008), pp. 1313–1324.

[10] N. S. W. Q. V. A. M. C. J. Cong, "Bonsai: High-Performance Adaptive Merge Tree Sorting." In: _ACM/IEEE 47th Annual International Symposium on Computer Architecture (ISCA)_ (2020).

[11] W. Q. L. G. M. C. J. Cong, "FANS: FPGA-accelerated near-storage sorting." In: _Proceedings of the 29th IEEE International Symposium on Field-Programmable Custom Computing Machines (FCCM)_ (2021).

[12] W. Q. L. G. Z. F. M. C. J. Cong, "TopSort: A High-Performance Two-Phase Sorting Accelerator Optimized on HBM-based FPGAs." In: _IEEE 30th Annual International Symposium on Field-Programmable Custom Computing Machines (FCCM)_ (2022). DOI: https://doi.org/10. 1109/FCCM53951.2022.9786209.

[13] J. Dean and S. Ghemawat, "MapReduce: Simplified Data Processing on Large Clusters." In: _Communications of the ACM_ 51(1) (Jan. 2008), pp. 107–113. DOI: 10.1145/1327452.1327492. URL: https://doi.org/10. 1145/1327452.1327492.

[14] A. Dutta and M. Saha, "Contrasting Parallelized with Sequential Sorting." In: _2022 IEEE 7th International Conference on Recent Advances and Innovations in Engineering (ICRAIE)_. Vol. 7. 2022, pp. 256–259. DOI: 10.1109/ICRAIE56454.2022.10054300.

[15] G. Graefe, "Implementing sorting in database systems." In: _ACM Computing Surveys_ 38(3) (Sept. 2006), 10–es. DOI: 10.1145/1132960.1132964. URL: https://doi.org/10.1145/1132960. 1132964.

[16] J. Gray, "Sort Benchmark Home Page." (2023). URL: https:// sortbenchmark.org/.

[17] E. S. H. A. Jacobsen, "A memory bandwidth-efficient hybrid radix sort on GPUs." In: _International Conference on Management of Data (SIGMOD)_ (2017). DOI: https://doi.org/10.1145/3035918.3064043.

[18] D. Koch and J. Torresen, "FPGASSort: A high performance sorting architecture exploiting run-time reconfiguration on FPGAs for large problem sorting." In: _Proceedings of the 19th ACM/SIGDA International Symposium on Field-Programmable Gate Arrays_ (2011), pp. 45–54.

[19] C. G. Z. B. P. Laskov, "FPGA vs. Multi-core CPUs vs. GPUs: Hands-On Experience with a Sorting Application." In: _Lecture Notes in Computer Science_ 6310 (2017), pp. 105–117.

[20] X. Luo et al., "A Memory-Disaggregated Radix Tree." In: _ACM Transactions on Storage_ 20(3) (June 2024). DOI: 10.1145/3664289. URL: https://doi.org/10.1145/3664289.

[21] T. Maltenberger et al., "Evaluating multi-GPU sorting with modern interconnects." In: _Proceedings of the 2022 International Conference on Management of Data_ (2022), pp. 1795–1809.

[22] D. Merrill and A. Grimshaw, "High Performance and Scalable Radix Sorting: A Case Study of Implementing Dynamic Parallelism for GPU Computing." In: _Parallel Processing Letters_ 21(02) (2011), pp. 245– 272. DOI: 10.1142/S0129626411000187. URL: https://doi.org/10.1142/ S0129626411000187.

[23] H. C. S. M. M. F. P. Milder, "FPGA-Accelerated Samplesort for Large Data Sets." In: _Proceedings of the 28th ACM/SIGDA International Symposium on Field-Programmable Gate Arrays (FPGA)_ (2020).

[24] P. Papaphilippou, C. Brooks, and W. Luk, "Fi:MS: Fast lightweight merge sorter." In: _2018 International Conference on Field- Programmable Technology (FPT)_. IEEE, 2018, pp. 78–85.

[25] N. Satish, M. Harris, and M. Garland, "Designing efficient sorting algorithms for manycore GPUs." In: _2009 IEEE International Symposium on Parallel & Distributed Processing_. IEEE, 2009, pp. 1–10.

[26] N. Satish et al., "Fast sort on CPUs and GPUs: a case for bandwidth oblivious SIMD sort." In: _Proceedings of the 2010 ACM SIGMOD International Conference on Management of Data_ (2010), pp. 351–362.

[27] M. El-Sharkawy et al., "Re-configurable parallel Feed-Forward Neural Network implementation using FPGA." In: _Integration_ 97 (2024), p. 102176. DOI: https://doi.org/10.1016/j.vlsi.2024.102176.

[28] T. Usui, T. Van Chu, and K. Kise, "A cost-effective and scalable merge sorter tree on FPGAs." In: _2016 Fourth International Symposium on Computing and Networking (CANDAR)_. IEEE, 2016, pp. 47–56.

[29] C. Zhang, R. Chen, and V. Prasanna, "High throughput large scale sorting on a CPU-FPGA heterogeneous platform." In: _2016 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)_. IEEE, 2016, pp. 148–155.

[30] M. Zuluaga, P. Milder, and M. Püschel, "Streaming Sorting Networks." In: 21(4) (May 2016). DOI: 10.1145/2854150. URL: https://doi.org/10. 1145/2854150.

[31] S. Asano, T. Maruyama, and Y. Yamaguchi, "Performance comparison of FPGA, GPU and CPU in image processing." In: _2009 International Conference on Field Programmable Logic and Applications (FPL)_ (2009), pp. 126–131. DOI: https://doi.org/10.1109/FPL.2009.5272532.

[32] D. E. Knuth, _The Art of Computer Programming, Volume 3: Sorting and Searching_, 2nd ed. Addison-Wesley, 1998.

[33] T. Bingmann, S. Sanders, and J. Singler, "Parallel string sample sort," _ACM Journal of Experimental Algorithmics_, vol. 23, no. 1, pp. 1–23, 2018.

[34] G. E. Blelloch, C. E. Leiserson, B. M. Maggs, C. G. Plaxton, S. J. Smith, and M. Zagha, "A comparison of sorting algorithms for the connection machine CM-2," in _Proceedings of the 3rd ACM Symposium on Parallel Algorithms and Architectures_, 1991, pp. 3–16.

[35] P. Sanders and J. L. Träff, "Parallel sorting in message-passing systems," in _Proceedings of the IEEE International Parallel and Distributed Processing Symposium_, 1997, pp. 1–10.

[36] F. Dehne, A. Fabri, and A. Rau-Chaplin, "Scalable parallel geometric algorithms for coarse grained multicomputers," in _Proceedings of the IEEE Symposium on Parallel and Distributed Processing_, 1996, pp. 298–305.

