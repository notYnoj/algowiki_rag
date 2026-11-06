# Verified DRAM Address Mapping Reverse Engineering with Threshold Sweep

Hewen Zhang<br> _University of California, Irvine_<br> Irvine, USA<br> hewenz1@uci.edu

Ian G Harris

_University of California, Irvine_ Irvine, USA<br> iharris@uci.edu

**_Abstract_--We propose an end-to-end software pipeline for solving and validating DRAM address mapping functions on embedded LPDDR5 systems, and we instantiate it on embedded platforms. Starting from a large latency dataset of address pairs, the pipeline first builds a latency histogram and then performs a threshold sweep to obtain candidate same-bank address pairs. For each threshold, we apply a Knock-Knock- style [9] linear-constraint solver to recover candidate bank masks. Final bank masks are calculated using GF(2) reduced row echelon form (RREF). To verify correctness, we implement two verification stages, group verification and single function verification, inspired by prior work. Group verification checks whether bank partitions induced by the recovered masks agree with observed timing behavior. Single function verification removes one addressing function at a time and measures the resulting change in verification pass rate. Unlike approaches that return only a single inferred mapping, our workflow systematically records, for each candidate threshold, the solved bank masks and validation metrics. This pipeline supports more robust selection of bank masks on ARM-based embedded devices and provides an efficient method for reverse engineering DRAM address mapping functions and subsequent Rowhammer analysis.**

### I. INTRODUCTION

Dynamic random-access memory (DRAM) is a core memory technology used by modern computing systems. Kim et al. [7] first systematically revealed DRAM disturbance errors in commodity devices, showing that repeatedly activating a DRAM row can induce bit flips in adjacent rows, which makes Rowhammer a serious security threat. Subsequent work has demonstrated Rowhammer attacks across a wide range of platforms and threat models, including commodity desktops, cloud and cross-VM settings, mobile ARM devices, browsers via JavaScript, and newer CPU ecosystems such as AMD Zen and RISC-V [3], [4], [5], [10], [13].

To efficiently trigger Rowhammer bit flips, it is important to understand the DRAM address mapping function, which determines how physical addresses are mapped to DRAM locations. These mapping functions enable an attacker to select addresses required for effective hammering, and prior work has shown that better recovered mappings can substantially improve the success of double-sided Rowhammer experiments [8], [11], [12]. However, these functions are typically undocumented and vendor-specific, forcing researchers to reverse engineer them from externally observable behavior [8], [13]. A recent work is Knock-Knock, which departs from the exhaustive search by formulating bank masks recovery in linear-algebraic terms and<tbc>

<tbc>replacing mask enumeration with a nullspace-based algorithm [9].

Despite this progress, there are still some limitations. Prior work still focuses mainly on desktop and server-class Intel/AMD systems, while fewer works target embedded platforms especially ARM-based systems with LPDDR5 memory. Moreover, many works report recovered DRAM address mapping functions, but systematic software-only verification of whether the functions are complete and correct is limited. Recent work highlights this issue and introduces systematic methods to reliably verify DRAM address mapping functions and individual function components, which provides a more rigorous foundation for evaluating the reverse engineering methods [2].

This paper makes the following contributions:

\(\bullet\) To the best of our knowledge, this is the first work to systematically study DRAM address mapping reverse engineering and verification on an embedded LPDDR5 platform in the context of Rowhammer analysis.

\(\bullet\) We propose a software-only end-to-end automatic pipeline involving latency measurements, reverse engineering, and verification processes without prior knowledge of DRAM hierarchy.

\(\bullet\) We instantiate the pipeline on two ARM-based embedded platforms with different memory generations, Jetson Orin Nano with LPDDR5 memory and Raspberry Pi 4B with LPDDR4 memory, showing that the approach is effective beyond a single device or DRAM configuration.

\(\bullet\) Our pipeline recovers DRAM address mapping functions that are strongly supported by verification. On both platforms, the final solutions achieve pass rates close to 100% in group verification, and on Jetson Orin Nano the recovered masks are further supported by single function verification results that closely match the expected behavior.

### II. BACKGROUND

#### A. DRAM Organization

Modern DRAM systems are organized hierarchically. At the system level, a memory controller maps physical addresses to a tuple of DRAM components, typically including channel, rank, bank group, bank, row, and column [1]. Each DRAM bank contains a row buffer that temporarily stores<tbc>

