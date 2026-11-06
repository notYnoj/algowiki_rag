<tbc>There are two classes of sorting operators -- internal (in-memory) and external (disk-based) sorts. The former assumes that all data fits into main memory and the latter has to write intermediates to disk. Recent research mostly focuses on an in-memory type because of a surge of interest that in-memory processing currently experiences [12, 22, 25]. Such systems try to avoid external sorting, since it significantly degrades performance. Despite all this, disk-based systems are still in use<sup>3</sup> and research in this area is relevant.

Thus, efficient implementation of the sorting operator is crucial for the performance of a DBMS as a whole. Such implementation heavily depends on the amount of an engineering effort put into the source code, which is specific for each particular system. For example, it may include adjusting implementation to various system parameters (e.g. disk block size, cache line size, etc.) and writing efficient code in general. However, some high-level techniques can be reused between systems, and thus they are of scientific interest. For example, such techniques as key normalization or record surrogate usage are discussed in Graefe’s survey [9].

In this paper we study the implementation of efficient external sorting in a disk-based column-store. Aside from the aforementioned application, in column- stores, external sort has another important one: it addresses the out-of-order probing problem [1]. The particular research focus of this paper is the impact of data structure choice on the performance of the comparison-based external sort. This data structure is used during run merging and allows to reduce the number of comparisons. More specifically we pose two following research questions: 1) is it beneficial to use a specialized data structure on the merge step in a contemporary environment (commodity PCs), and 2) which kind is the best.

To answer them, we have implemented an external sort operator inside PosDB [3, 4], a distributed column-store engine. In the operator’s core, we have devised three approaches to implementing the merge: naive (comparing all to all), a loser tree, and a binary heap.

To validate the quality of our implementation we first compare it with PostgreSQL’s external sort. Then we evaluate these three data structures by comparing them with each other using a synthetic and a real dataset.

The paper is organized as follows. In Section 2 we provide a concise introduction into external sorting. Then, in Section 3 we discuss the related work and provide a motivation for our study. Next, in Section 4 we describe the proposed approaches and their implementation. In Section 5 we explain conducted experiments and their results. Finally, we conclude this paper with Section 8.

## 2 Background

Sorting, because of its importance, has been studied very extensively. Sorting algorithms fall into two categories: external and in-memory (or internal [13]) sorting. In this paper we will focus on external sorting. An external sorting

<sup>3</sup> As of July 2022, disk-based systems PostgreSQL and MySQL were in the top-5 most used according to DB-Engines Ranking (`https://db-engines.com/en/ranking`).

