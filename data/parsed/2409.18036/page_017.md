<tbc>PSS query instances, the total space consumption of the adapters is bounded by _O(n_<sub>0</sub>). Recall that _n_<sub>0</sub> is the size of the item set _S_ when the HALT structure is constructed, and _n_ is the _current_ size of _S_. Without loss of generality, we assume that \(n_0/2\le n\le 2n_0\). If this is not the case, we can rebuild the HALT structure on the current _S_ to make this assumption hold. More details about global rebuilding and de-amortization are discussed in Section **??**.

Recall that in the three-level hierarchy, at Level-1, the next-level item set _Y<sub>j</sub>_ of each group _G<sub>S</sub>(j_) in BG-Str(_S_) contains at most log<sub>2</sub>_n_<sub>0</sub> items; and at Level-2, the next-level item set _Z<sub>k</sub>_ of each group _G<sub>Y<sub>j</sub></sub>(k_) in BG-Str(_Y<sub>j</sub>_) has size at most log<sub>2</sub>log<sub>2</sub>_n_<sub>0</sub>. Furthermore, at Level-3, each item _v<sub>i</sub>_ in the item set _V<sub>k</sub>_ in the final-level instance corresponds to a non-empty bucket, _B<sub>Z<sub>k</sub></sub>(i_), of items in _Z<sub>k</sub>_, where each item \(z\in Z_k\) corresponds to a bucket in group _G<sub>Y<sub>j</sub></sub>(k_). Thus, we have \(|V_k|\le|Z_k|\le m\), where _m_=log<sub>2</sub>log<sub>2</sub>_n_<sub>0</sub>. And the weight of each item \(v_i\in V_k\) is \(w(v_i)=2^{i+1}\cdot|B_{Z_k}(i)|\le 2^{i+1}\cdot m\).

**A Simple but Space-Inefficient Adapter Implementation.** Define _m_=log<sub>2</sub>log<sub>2</sub>_n_<sub>0</sub>. Consider the final-level instance on _Z<sub>k</sub>_ as aforementioned. A simple implementation of an adapter is to maintain an array A of length _L_, where _L_ is number of possible bucket indices of the items in _Z<sub>k</sub>_, and for \(i\in[0,L-1]\), A\[_i_\] stores the size of (possibly empty) bucket _B<sub>Z<sub>k</sub></sub>(i_). Moreover, as \(|Z_k|\le m\), each bucket size must be an integer in \[0_,m_\].

<u>_The Query Algorithm for a Final-Level Instance_</u>. Given a PSS query with parameters \((0,W_S(\alpha,\beta))\) on <o>_V<sub>k</sub>_</o>, the following query algorithm aims to return a PSS result \(T\subseteq Z_k\) with parameters \((0,W_S(\alpha,\beta))\).

**QueryFinalLevel(** BG-Str(_Z<sub>k</sub>),_ \((0,W_S(\alpha,\beta))\) **).**

\(\bullet\) compute the _largest_ possible index _i_<sub>1</sub> of bucket _B<sub>Z<sub>k</sub></sub>(i_<sub>1</sub>) such that \(\frac{2^{i_1+1}}{W_S(\alpha,\beta)}\le\frac{2}{m^2}\);<tbc>

\(\bullet\) compute the _smallest_ possible index _i_<sub>2</sub> of bucket _B<sub>Z<sub>k</sub></sub>(i_<sub>2</sub>) such that \(\frac{2^{i_2}}{W_S(\alpha,\beta)}\ge 1\);<tbc>

\(\bullet\) \(T_1\leftarrow\) QueryInsignificant(BG-Str(_Z<sub>k</sub>),_ \((0,W_S(\alpha,\beta)),i_1\)) // Algorithm 2;<tbc>

\(\bullet\) \(T_2\leftarrow\) QueryCertain(BG-Str(_Z<sub>k</sub>),_ \((0,W_S(\alpha,\beta)),i_2\)) // Algorithm 3;<tbc>

\(\bullet\) process all the remaining buckets _B<sub>Z<sub>k</sub></sub>(i_) with index \(i\in[i_1+1,i_2-1]\):<tbc>

- collect all the bucket sizes in A\[_i_<sub>1</sub>+1_,i_<sub>2</sub>-1\] as an input configuration \(\vec{c}\) for the 4S problem; specif ically, recall that the _j_<sup>th</sup> item in the 4S problem is selected with probability \(p_j=min\left\{1,\frac{2^{j+1}\cdot\vec{c}[j]}{m^2}\right\}\), where \(\vec{c}[j]=|B_{Z_k}(j+i_1)|\);<tbc>

- use the lookup table T to obtain a subset sampling result _r_<sub>3</sub> for the 4S problem with input configuration \(\vec{c}\); note that _r_<sub>3</sub> is a bit string of length (_i_<sub>2</sub>-_i_<sub>1</sub>-1), where the _j_<sup>th</sup> bit in _r_<sub>3</sub> being 1 indicates the bucket with index (_j+i_<sub>1</sub>) is selected;<tbc>

- initialize an empty set \(T'_3\);<tbc>

- for each index \(j\in\{1,2,\dots,i_2-i_1-1\}\) such that _r_<sub>3</sub>\[_j_\]=1, add the item \(v\in V_k\) corresponding bucket _B<sub>Z<sub>k</sub></sub>(j+i_<sub>1</sub>) to \(T'_3\) with probability \(\frac{min\left\{1,\frac{w(v)}{W_S(\alpha,\beta)}\right\}}{p_j}\) ;<tbc>

- \(T_3\leftarrow\) ExtractItems(BG-Str(_Z<sub>k</sub>),_ \(T'_3\), \((0,W_S(\alpha,\beta))\) // Algorithm 5<tbc>

\(\bullet\) return \(T=T_1\cup T_2\cup T_3\);

Lemma 4.15. _The configuration_ \(\vec{c}\) _is a legal 4S problem input defined for the lookup table_ T .

Proof. From the above query algorithm, \(\vec{c}\) contains exactly _i_<sub>2</sub>-1-(_i_<sub>1</sub>+1)+1=_i_<sub>2</sub>-_i_<sub>1</sub>-1 integers. Observe that all the buckets with indices in the range \[_i_<sub>1</sub>+1_,i_<sub>2</sub>-1\] must correspond to a power-of-two probability in the range \([\frac{1}{m^2},1]\). Therefore, there are at most \(\lceil 2log_2m\rceil\in O(logm)=O(loglogn_0)\) possible buckets. And hence, \(\vec{c}\) contains exactly \(K\in O(loglogn_0)\) integers. Moreover, each integer is indeed a bucket size which is in the range \[0_,m_\]. Therefore, \(\vec{c}\) is a legal input configuration to the 4S problem. □

Lemma 4.16 (Correctness). _T is a correct PSS result on Z<sub>k</sub> with parameters_ \((0,W_S(\alpha,\beta))\).

