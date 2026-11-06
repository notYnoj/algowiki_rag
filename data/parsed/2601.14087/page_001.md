# ’1’-bit Count-based Sorting Unit to Reduce Link Power in DNN Accelerators

Ruichi Han, Yizhi Chen, Tong Lei, Jordi Altayo Gonzalez, Ahmed Hemani

Department of Electronics and Embedded Systems, KTH Royal Institute of Technology, Stockholm, Sweden

{ruichi, yizhic, tonglei, jordiag, hemani}@kth.se

**_Abstract_--Interconnect power consumption remains a bottleneck in Deep Neural Network (DNN) accelerators. While ordering data based on ’1’-bit counts can mitigate this via reduced switching activity, practical hardware sorting implementations remain underexplored. This work proposes the hardware implementation of a comparison-free sorting unit optimized for Convolutional Neural Networks (CNN). By leveraging approximate computing to group population counts into coarse-grained buckets, our design achieves hardware area reductions while preserving the link power benefits of data reordering. Our approximate sorting unit achieves up to 35.4% area reduction while maintaining 19.50% BT reduction compared to 20.42% of precise implementation.**

**_Index Terms_--’1’-bit count-based sorting, Approximate computing, Bit transition reduction, Link power**

### I. INTRODUCTION

Deep neural network (DNN) accelerators are essential for modern computing [1] [2]. While DNN accelerators perform many arithmetic operations, recent works show that data movement dominates power consumption [3] [4] [5].

On-chip interconnects and NoC fabrics consume a growing share of chip power as models and parallelism scale, particularly in data-intensive workloads [1] [5]. Within NoC-based architectures, physical links account for a significant portion of the energy budget [4] [5]. As dynamic power is fundamentally driven by the switching activity on links, where each bit transition (BT) incurs capacitive charging costs, reducing BT is an effective lever to improve accelerator efficiency [3] [4].

Various BT reduction encoding schemes have been developed to suppress interface switching activity [2] [6]. Standard encoding algorithms often fail to adapt to the unique traffic patterns of neural computing [1] [4] [5] [6]. Recent studies exploit accumulation order-insensitivity, utilizing ’1’-bit count or population count (popcount) sorting to minimize switching activity [7]. However, these largely theoretical proposals lack practical hardware evaluations to justify the the sorting mechanism’s area and power overhead [1] [7].

To our knowledge, this is the first hardware implementation of a popcount sorting unit for DNNs with approximate sorting. For terminological consistency, though both terms are equivalent, "popcount" denotes the hardware unit, while ’’1’- bit count" for non-hardware discussion. We summarize our contributions as follows:

1) **Hardware Implementation**: Distinct from simulation- based prior work, we present a hardware implementation<tbc>

<tbc>of comparison-free popcount sorting and compare with other popcount sorting implementations.

2) **Approximate computing optimization**: We not only implement the accurate sorting unit, but also extend it with approximate sorting to reduce the area cost.

3) **Comprehensive power analysis**: We analyze ordering’s impact on both link power and computational unit power through post-layout power analysis.

4) **DNN layer’s workload**: We evaluate our design under a convolution and pooling workload, adopting the same configuration from LeNet’s first two layers.

**The rest of this paper is organized as follows:** Section II reviews related work. Section III describes our comparison- free sorting unit architecture and approximate computing techniques. Section IV presents our experiment setup and results. Section V concludes the paper.

### II. RELATED WORK

The rising power consumption of on-chip interconnects in DNN accelerators drives the need for strategies that minimize dynamic switching costs on links [5]. Encoding techniques such as those employed in Eyeriss v2 minimize BT during data transmission through signal-level transformations [8]. However, such encoding approaches introduce encoding/decoding overhead that impacts overall hardware efficiency [9].

DNN accumulation operations exhibit order-insensitivity, enabling data reordering strategies to reduce switching activity [4]. Chen _et al._ [7] demonstrated that ’1’-bit count based ordering reduces link BT but incurs non-trivial hardware overhead. This motivates our focus on minimizing sorting unit area while preserving power benefits [3].

Traditional sorting networks like Batcher’s Bitonic [10] are comparator-heavy. Constant-time approaches like the Competition Sorter Network (CSN) [11] [12] improve speed but require 80% more logic elements. Comparison-free architectures offer a more area-efficient foundation by eliminating explicit comparator logic. AdbelHafeez _et al._ [13] proposed a linear- time sorter mapping inputs into hardware-friendly structures, yielding low buffering and minimal complexity. Subsequent refinements include FSM integration for control [14] and bidirectional data-paths to reduce latency [15]. OnSort [16] addressed scalability using sparse-aware metadata filters.

