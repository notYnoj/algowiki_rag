## 3 Proposed Methods

### 3.1 AiSAQ-in-Filtering

Label handling procedure of Filtered-DiskANN can be easily ported to AiSAQ. However, such naive portation spoils the main advantages of AiSAQ, almost-zero DRAM usage and fast index switch, because its label data should be stored on DRAM (Figure 4). One straightforward solution is writing (compressed) label data along with edge information in the storage, the same as PQ vectors in AiSAQ. This cause increased SSD footprint. Although AiSAQ has larger SSD-resident index sizes than DiskANN due to PQ vector duplication, this straightforward approach will lead to much larger footprint since label information size will be larger than a PQ vector. There may be ideas to compress label data, however, larger index size than AiSAQ will be inevitable.

To address this issue, we propose a novel continuous label filtering search named AiSAQ-in-Filtering exploiting a new quantization technique shown below. This acheives high search accuracy in single-label search with almost-zero DRAM footprint and fast index switch time.

### 3.2 Label-inclusive Product Quantization (LiPQ)

As a key technique of AiSAQ-in-Filtering, we present Label-inclusive Product Quantization (LiPQ) which encodes vector and label data into combined PQ representation. In LiPQ which encodes an object to _M_ subvectors (or _M_ bytes), a label vector is also split into _M_ subvectors. The same subvectors **_v_**_<sub>im</sub>_, **_a_**_<sub>im</sub>_ of a data vector and label vector as the same object and position make pair. Then, They are clustered and quantized by almost the same way as normal PQ, except fusion distance \(d_\mathrm{F}(\cdot,\cdot)\) is used as the distance metric.

Figure 5 shows an example of LiPQ with _m_=2 and _b_=4 (2 bits). A 4-dimensional vector **_v_**_<sub>i</sub>_ and a 6-dimensinoal label **_a_**_<sub>i</sub>_ are split into 2 subvectors, which have 2 and 3 dimensions respectively. These procedure means objects are clustered in a space considering both of vector and label. Since objects are clustered in units of vector and label pairs, the PQ vector results in the same size as vector-only quantization.

We use a binary label vector **_a_**_<sub>i</sub>_={0,1}_<sup>L</sup>_ to express the object. If an object **_o_**_<sub>i</sub>_ has label _l<sub>j</sub>_, the corresponding element of its label vector _a<sub>ij</sub>_=1, otherwise 0. To obey the constraint of PQ described<tbc>

\begin{tabular}{ccccc}
 & Vectors and edges & PQ vectors & Filtering support and strategy & Labels \\
DiskANN & **SSD** & DRAM & - & - \\
AiSAQ & **SSD** & **SSD** & - & - \\
Filtered-DiskANN & **SSD** & DRAM & boolean & DRAM \\
AiSAQ-in-Filtering (ours) & **SSD** & **SSD** & continuous & **SSD** \\
\end{tabular}

v1
v11
v12
v13
v14
v2
v21
v22
v23
v24
VN
VN1
VN2
VN3
VN4
k-means
b
a
(v11, v12)
b
C2b
C1a
a
(c1a1, C1a2)
C1b
(v13, v14)
C2a
d
C2d
C1d
= (c2d3, C2d4)
C1c
C2c
C
d
C

Vectors
Labels
Vectors
Labels
PQ
LiPQ
PQ vectors
Labels
PQ vectors
DRAM
Storage

v1
v11
v12
v13
v14
a1
a11
a12
a13
a14
a15
a16
v2
v21
v22
v23
v24
a2
a21
a22
a23
a24
a25
a26
VN
VN1
VN2
VN3
VN4
AN
AN1
AN2
AN3
AN4
a2N
AN6
k-means by Fusion Distance
a
(v11, v12)
b
b
C2b
C1a
a
(v13, v14)
C1b
(a14, a15, a16)
C2a
d
C2d
C1d
C2c
C
d
C

** 1: Comparison of our proposal and existing methods**

**Figure 3: A toy example of 2-bit product quantization**

**Figure 4: Vector and Label placement on Filtered-DiskANN (left) vs AiSAQ-in-Filtering (right)**

**Figure 5: A toy example of 2-bit LiPQ**

