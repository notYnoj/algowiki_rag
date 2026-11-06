# Hourglass Sorting: A novel parallel sorting algorithm and its implementation

Daniel Báscones, Borja Morcillo

**_Abstract_--Sorting is one of the fundamental problems in computer science. Playing a role in many processes, it has a lower complexity bound imposed by O(_n_log_n_) when executing on a sequential machine. This limit can be brought down to sub- linear times thanks to parallelization techniques that increase the number of comparisons done in parallel. This, however, increases the cost of implementation, which limits the application of such techniques. Moreover, as the size of the arrays increases, a bottleneck arises in moving the vast quantities of data required at the input, and generated at the output of such sorter. This might impose time requirements much stricter than those of the sorting itself. In this paper, a novel parallel sorter is proposed for the specific case where the input is parallel, but the output is serial. The design is then implemented and verified on an FPGA within the context of a quantum LDPC decoder. A latency of log_n_ is achieved for the output of the first element, after which the rest stream out for a total sorting time of _n_+log_n_. Contrary to other parallel sorting methods, clock speed does not degrade with _n_, and resources scale linearly with input size.

**_Index Terms_--Sorting, FPGA, parallelization**

## I. INTRODUCTION

ORTING algorithms are at the core of many of the processes that take part in computing. Appearing in databases, scheduling, data analytics, networking, recommendation systems, computational biology and, more recently, computer graphics or AI. Consequently, they are one of the most researched families of algorithms, and often the first to be studied in any basic algorithms course.

The formal proof that outlines the minimum \(\mathcal{O}(n\cdot log(n))\) complexity of sorting was published by D. Knuth [1], along with a collection of algorithms that reach that bound. Merge sort (attributed to John von Neumann in 1945; however lacking formal publication), heap sort [2], and radix sort [3] (which appeared prior to modern computers being available) are some examples. Quicksort [4], which only ensures an _average_ complexity of \(\mathcal{O}(n\cdot log(n))\) is -perhaps surprisingly- the most used, due to its simplicity and in-place sorting capabilities.

As time progressed, and data sets enlarged, the need for faster sorting was fulfilled by going parallel. The first sorting networks [5] were able to sort an array in O(log<sup>2</sup>(_n_)) time using \(\mathcal{O}(n\cdot log^2(n))\) resources. These were eventually refined [6] to O(log(_n_)) complexity and \(\mathcal{O}(n\cdot log(n))\) resources at the cost of a higher constant, which, unfortunately, made them impractical for most cases. Finally, it was proven that, given a CREW PRAM (Concurrent Read Exclusive Write Parallel Random Access Machine) architecture, a parallel merge sort

algorithm [7] can sort an array in O(log(_n_)) time using just O(_n_) processors.

In practice, hardware-accelerated sorting networks [8] are used when the problem is small and speed is critical. Parallel sorting techniques [9] for larger datasets usually work on general-purpose hardware: they partition, sort, and merge the arrays using sequential sorting and clever data interleaving.

There is, however, a gap in the case that faster than \(\mathcal{O}(n\cdot log(n))\) sorting is needed for large datasets: Hardware accelerated sorting networks become unfeasible due to resource use, and parallel techniques on general purpose hardware might not be sufficiently fast. Efforts have been made in bridging this gap, and two techniques shine above others: 1) Iterate over a small sorting network [10]. This reduces hardware use by a factor of log(_n_), increasing latency to linear time. 2) Trade off time and space complexity by selecting the input/output width and streaming data in chunks [11]. Further explored by [12], both exploit that only a fixed amount of data _w_ is processed in parallel, reducing hardware complexity, and increasing processing time, by a factor of _n/w_.

All of these algorithms (either serial or parallel) share a common characteristic: a fixed size _w_ for _both_ the input and output. However, it is not always that the processing is symmetrical. For certain applications, we might be interested in asymmetrical SIPO (Serial-In Parallel-Out) or PISO (Parallel- In Serial-Out) schemes. A SIPO scheme with incremental sorting capabilities is presented in [11] with an application in statistical signal processing, leveraging the fact that a single datum arrives per cycle to achieve O(1) sorting time. While PISO schemes have not been found directly in the literature, any PIPO (Parallel In Parallel Out) algorithm (such as sorting networks) can be adapted by placing a shift-register at its output. The cost (in hardware) would thus be slightly more than the original, at least \(\mathcal{O}(n\cdot log(n))\) considering the smallest sorting networks [6].

In this work, we propose a novel sorting method for the PISO scheme, that has O(_n_) hardware complexity, and is able to output its first sorted datum in O(log(_n_)) time. Furthermore, its clock cycle is independent of the input array size (a property not all sorting accelerators exhibit, that hinders many when scaling up), making it highly scalable. This method has been implemented in an FPGA, and is currently used in a BP-OSD (Belief Propagation - Ordered Statistics Decoder) [13] implementation as the intermediate step for ordering the outputs of BP.

**NOTE:** Throughout this paper, it is assumed for simplicity that ascending sorting (lowest first) is performed. All of the designs, however, can be adapted to descending order trivially.

Authors are with the Department of Computer Architecture and Auto- matics, Universidad Complutense de Madrid, Madrid, Spain. e-mail: (dani- basc@ucm.es).

