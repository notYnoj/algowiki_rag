### 1.2.4 Quorum Planted Motif Search (qPMS)

A generalized version of the PMS Problem namely Quorum Planted Motif Search (qPMS) problem. The qPMS problem is to find all the motifs that have motif instances present in _q_ out of the _n_ input sequences. This version captures the nature of motifs more precisely than the PMS problem because in practice some motifs may not have motif instances in all of the input sequences. qPMS algorithms can be used to find DNA motifs and protein motifs as well as transcription factor binding sites.

### 1.2.5 Formal Definitions of qPMS

**Definition 1** A string _x=x_[1]_...x[l_] of length _l_ is called an _l_-mer.

**Definition 2** Given two strings _x=x_[1]_...x[l_] and _s=s_[1]_...s[m_] with _l\<m_ we say \(x\epsilon_ls\) if there exists \(1\le i\le l-m+1\) such that _x[j_]=_s[l-m_+1] for every \(1\le j\le l\). We also say that _x_ is an _l_-mer in _s_.

**Definition 3** Given two strings _x=x_[1]_...x[l_] and _y=y_[1]_...y[l_] of equal length, the Hamming distance between _x_ and _y_ denoted by _d<sub>H</sub>(x,y_) is the number of mismatches between them. In other words, \(d_H(x,y)=\Sigma_{1\le i\le l}I_i\), where _I<sub>i</sub>_ is the indicator at position _i_. _I<sub>i</sub>_=1 if \(x[i]\neq y[i]\) and _I<sub>i</sub>_=0 otherwise.

**Definition 4** Given two strings _x_ and _s_ with |_x|\<|s_|, the Hamming distance between _x_ and _s_, denoted by _d<sub>H</sub>(x,s_) is \(min_{y\epsilon_{|x|}s}d_H(x,y)\).

**Definition 5** Given a set of _n_ strings _s_<sub>1</sub>_,...,s<sub>n</sub>_ of length _m_ each, a string _M_ of length _l_ is called an (_l,d,q_)-motif of the strings if there are at least _q_ out of the _n_ strings such that the Hamming distance between each one of them and _M_ is no more than _d_.

**Definition qPMS** Given _n_ input strings _s_<sub>1</sub>_,...,s<sub>n</sub>_ of length _m_ each, three integer parameters _l_, _d_ and _q_, find all the (_l,d,q_)-motifs of the input strings. The PMS problem is a special case of the qPMS problem when _q=n_.

## 1.3 Literature Review

During the last two decades various types of PMS algorithm has been proposed in the literature. There are mainly two types of algorithms for PMS problem. They are _exact_ and _approximate_ algorithms. An exact algorithm always finds all the (_l,d_)-motifs present in the input sequences. While, an approximate algorithm may not find all the motifs.

