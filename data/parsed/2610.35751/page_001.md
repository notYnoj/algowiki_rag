# ACTIVE: A Dynamic Pareto-Frontier-Based Unified Index for Dual-Vector Query

### ABSTRACT

Existing approximate nearest neighbor search (ANNS) methods generally assume that each entity has a single vector. In many real-world applications, however, an entity is associated with more than one vector, and queries may jointly consider two attributes. With different queries assigning different weights to each attribute, Pareto-frontier-based indices provide an effective solution for dual- vector retrieval by connecting to approximate nearest neighbors under all possible query preferences. However, existing Pareto- frontier-based approaches suffer from substantial inefficiencies in both index construction and dynamic updates, limiting their practical applicability.

To address these issues, we propose ACTIVE , a dynamic Pareto- frontier-based DVQ index that supports efficient construction and updates while maintaining high retrieval performance under varying query preferences. It employs angle-constrained active-range computation and connectivity-loss-driven adaptive repair strategies to accelerate node insertion and deletion, respectively. Extensive experiments show that, at comparable (or slightly below) search accuracy, ACTIVE improves insertion throughput by 1.20-1.43\(\times\) over DEG, and deletion throughput by 1.64-2.06\(\times\) over neighbor- reconnection-based repair and by 22.64-39.51\(\times\) over reinsertion- based repair.

### 1 INTRODUCTION

Approximate nearest neighbor search (ANNS) over high- dimensional vectors has been widely adopted in applications such as recommendation systems [12, 34, 42, 43] and information retrieval [4, 33, 55, 65]. In these applications, the unstructured attributes of an entity, such as image, text, or audio, are embedded into vectors, and objects whose vectors are close (similar) to the query vector are retrieved. Traditional ANNS primarily focuses on single-vector retrieval [9, 16, 19, 22, 23, 30, 50, 59], i.e., entities are searched based on only _one_ unstructured (vectorized) attribute.

However, many real-world retrieval tasks require jointly considering more than one vectorized attribute [5, 11, 32, 38, 39, 46, 48], with query-specific preferences assigned to each attribute. In this paper, we focus on dual-vector retrieval with exactly two attribute vectors, which is common in applications with complementary modalities, such as image-text of products on e-commerce platforms [20, 48, 61], spatial-textual data of posts on social platforms [11], and video-text of videos on short-video platforms [32, 61]. Given a query with two vectors, the distance between the query and an

object is the weighted sum of their distances on the two vectors, where the query-specific preference determines the weight of each attribute distance. As query preferences vary, the distance between the same pair of entities changes accordingly, making efficient and accurate ANN retrieval particularly challenging. Furthermore, real- world datasets are inherently dynamic, with entities continuously being inserted and deleted. Such dynamic updates pose significant challenges to efficient index-based retrieval methods.

**Example 1:** In product search on e-commerce platforms, consider two users who upload images of a smartphone and provide textual descriptions, such as "a smartphone with long battery life and excellent photography". The first user aims to retrieve a smartphone that visually resembles the uploaded image, whereas the second user prioritizes the specific performance attribute. Accordingly, the first user assigns a larger weight to the image-vector distance, while the second user assigns a larger weight to the textual- vector distance when computing similarity based on the image and textual embeddings. Even when the two users provide the same phone image and textual description, different preferences can lead to different retrieval results. Meanwhile, vendors continuously update product listings due to inventory changes, ensuring accurate retrieval results for users. This makes the dynamic updating of dual- vector data indispensable. Thus, the DVQ problem requires efficient and accurate retrieval under arbitrary query preferences while also supporting efficient dynamic updates. \(\sqcap\sqcup\)

**Motivation.** Existing DVQ approaches [48, 49, 61, 63] mainly build graph-based ANNS indices over dual-vector data to enable efficient retrieval. However, they cannot simultaneously achieve high retrieval accuracy and high update efficiency. In general, these approaches can be divided into two categories.

<u>1)Preference-specific multi-indices</u>. These approaches [48, 49, 63] build single-vector indices by fixing the query preference in advance. A representative solution is multi-index retrieval (MR) [48, 63], which builds a separate index for each attribute vector. It searches

MR (+ Wolverine++) DEG (+ FreshDiskANN) ACTIVE 1.00 0.97 1.5k 0.95 0.96 1.0k Recall 10@10 Recall 10@10 0.95 0.90 0.5k 0
2 4
6 8
0 2
4 6
8 10 0
2 4
6 8
10 Batches Batches (a) Search in DVQ indices (b) Recall stability (c) Update throughput

Shengyuan Lin<br> Northeastern Univ., China<br> linsy5847@gmail.com

Shufeng Gong<br> Northeastern Univ., China<br> gongsf@mail.neu.edu.cn

Zheng Wang<br> Northeastern Univ., China<br> wangzheng29a@163.com

Feng Yao<br> Northeastern Univ., China<br> yaofeng@stumail.neu.edu.cn

Shifu Li<br> Huawei Tec. Co., Ltd<br> lishifu@huawei.com

Yanfeng Zhang<br> Northeastern Univ., China<br> zhangyf@mail.neu.edu.cn

Ge Yu<br> Northeastern Univ., China<br> yuge@mail.neu.edu.cn

arXiv:2610.35751v1 [cs.DB] 26 Oct 2026

**Figure 1: Performance of DVQ indices under static search and dynamic updates on the OpenImage dataset, where "MR" denotes multi-index retrieval.**

