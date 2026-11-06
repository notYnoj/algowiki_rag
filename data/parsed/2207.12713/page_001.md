# Implementing the Comparison-Based External Sort

**Abstract.** In the age of big data, sorting is an indispensable operation for DBMSes and similar systems. Having data sorted can help produce query plans with significantly lower run times. It also can provide other benefits like having non-blocking operators which will produce data steadily (without bursts), or operators with reduced memory footprint. Sorting may be required on any step of query processing, i.e., be it source data or intermediate results. At the same time, the data to be sorted may not fit into main memory. In this case, an external sort operator, which writes intermediate results to disk, should be used.

In this paper we consider an external sort operator of the comparison- based sort type. We discuss its implementation and describe related design decisions. Our aim is to study the impact on performance of a data structure used on the merge step. For this, we have experimentally evaluated three data structures implemented inside a DBMS. Results have shown that it is worthwhile to make an effort to implement an efficient data structure for run merging, even on modern commodity computers which are usually disk-bound. Moreover, we demonstrated that using a loser tree is a more efficient approach than both the naive approach and the heap-based one.

**Keywords:** Query Engines · Query Processing · External Sort.

### 1 Introduction

Sorting is a very important operation in any data processing system. For example, in DBMSes leveraging sorted data may allow efficient implementation of operators [27] such as sort-merge join, which is one of the most popular approaches to join two tables larger than available memory in a reasonable time. Another example is performing aggregation over data sorted on aggregation attributes. In this case, it is possible to implement a non-blocking aggregation operator, i.e., an operator which can start producing results without having to read all input records.

<sup>2</sup> This paper was accepted to MegaData@ADBIS’22.

Michael Polyntsov<sup>1,2[0000-0001-7356-2504]</sup>, Valentin Grigorev<sup>2[0000-0003-4235-3712]</sup>, Kirill Smirnov<sup>1,2[0000-0003-4727-3455]</sup>, and George Chernishev<sup>1,2[0000-0002-4265-9642]</sup>

<sup>1</sup> Saint-Petersburg State University, Russia <sup>2</sup> PosDB Team {`polyntsov.m,valentin.d.grigorev,kirill.k.smirnov,chernishev`}`@gmail.com

