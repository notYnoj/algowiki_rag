### 3 Filter, filter, sort, scan

Our first serious embellishment to SA-scan aims to avoid sorting the full set of subpattern occurrences by filtering out some of the candidate positions that cannot possibly lead to matches. Specifically, we allocate a bitvector _F_ of _n/b_ bits initially all set to 0. We refer to _b_ as the _block size_ of the filter. Logically, each bit represents a block of _b_ contiguous positions in the input text, with the _i_th bit corresponding to the positions _ib..i(b_+1)-1. In describing the use of the filter we assume two subpatterns _p_<sub>1</sub> and _p_<sub>2</sub> (with occurrences in SA\[_s_<sub>1</sub>_..e_<sub>1</sub>\] and SA\[_s_<sub>2</sub>_..e_<sub>2</sub>\], respectively), but the technique is easy to generalize for _k\>_2.

Having allocated _F_, we scan the interval SA\[_s_<sub>1</sub>_..e_<sub>1</sub>\] containing the occurrences of subpattern _p_<sub>1</sub> and for each element _i=SA\[j_\] encountered, we set bits \(F[(i+\delta)/b..(i+\Delta)/b]\) to 1 to indicate that an occurrence of _p_<sub>2</sub> in any of the corresponding blocks of the input is a potential match. During the scan we also copy elements of the interval to an array _A_<sub>1</sub> of size _m_<sub>1</sub>=_e_<sub>1</sub>-_s_<sub>1</sub>+1. We then scan the interval SA\[_s_<sub>2</sub>_..e_<sub>2</sub>\] containing the occurrences of the second subpattern and for each position _i_ encountered we check _F\[i/b_\]. If _F\[i/b_\]=0 then _i_ cannot possibly be part of a match and can be discarded. Otherwise (_F\[i/b_\]=1) we add _i_ to a vector _A_<sub>2</sub> of candidates. We then sort _A_<sub>1</sub> and _A_<sub>2</sub> and intersect them with respect to the gap constraints, the same as in the original SA-scan algorithm. The hope is that |_A_<sub>2</sub>| is much less than _e_<sub>2</sub>-_s_<sub>2</sub>+1, and so the time spent sorting prior to intersection will be reduced.

There are two straightforward refinements to this approach. The first is to make the initial scan not necessarily over SA\[_s_<sub>1</sub>_..e_<sub>1</sub>\], but instead over the smaller of intervals SA\[_s_<sub>1</sub>_..e_<sub>1</sub>\] and SA\[_s_<sub>2</sub>_..e_<sub>2</sub>\]. The only difference is that if the interval for

CC
Kernel
Para
Proteins
1M
100k
Query time [us]
10k
1k
Radix sort
std::sort
Radix sort
std::sort
Radix sort
std::sort
Radix sort
std::sort

Fig.2: Time to search a 2GiB subset of the Common Crawl web collection (`commoncrawl.org`). for 20 VLG patterns (_k_=2, \(\delta_i,\Delta_i=\langle 100,110\rangle\)), composed of very frequent subpatterns drawn from the 200 most common substrings of length 3 in the collection.

