2. NSSG<sup>9</sup>: Navigating SSG is an approximation of SSG with very low index cost, which is also current state-of-the-art algorithm. Also, NSSG is an improvement version of NSG.<tbc>

3. KGraph<sup>10</sup>: KGraph directly uses KNNG as the search index with a large value of K.<tbc>

4. DPG<sup>11</sup>: Diversified Proximity Graph selects neighbors by maximizing average pairwise angle from KNNG and adds reverse edges.<tbc>

5. FALCONN<sup>12</sup> is a library with algorithms for ANNS, which are based on Locality-Sensitive Hashing (LSH).<tbc>

6. Faiss<sup>13</sup>: Faiss is a product quantization based algorithm released by Facebook. We used the IVF-PQ implementation for comparison.<tbc>

7. TBSG<sup>14</sup>: Tree-based Search Graph is the algorithm proposed by this paper.

All of the algorithms are implemented in C++, compiled by g++ with "O3" option. All the experiments are carried out on a machine with i7-10700K CPU @3.80GHZ\*16 and 32 GB memory. We evaluate the search performance with a single thread and index performance with 16 threads.

## 4. Result and Analysis

### 4.1. Search Performance

We perform 1, 10, 100-NN queries with all the algorithms on four datasets, where 1, 10, 100 are the size of groundtruth per query. For graph-based methods, we adopt Algorithm 1 for query and increase the result pool size to get<tbc>

<sup>9</sup>https://github.com/ZJULearning/SSG <sup>10</sup>https://github.com/aaalgo/kgraph <sup>11</sup>https://github.com/DBWangGroupUNSW/nns\_benchmark <sup>12</sup>https://github.com/FALCONN-LIB/FALCONN <sup>13</sup>https://github.com/facebookresearch/faiss <sup>14</sup>https://github.com/Fanxbin/TBSG

