Lower Bounds for External Memory Integer Sorting via Network Coding

**Abstract**

Sorting extremely large datasets is a frequently occuring task in practice. These datasets are usually much larger than the computer’s main memory; thus external memory sorting algorithms, first introduced by Aggarwal and Vitter [2] (1988), are often used. The complexity of comparison based external memory sorting has been understood for decades by now, however the situation remains elusive if we assume the keys to be sorted are integers. In internal memory, one can sort a set of _n_ integer keys of \(\Theta(lgn)\) bits each in _O(n_) time using the classic Radix Sort algorithm, however in external memory, there are no faster integer sorting algorithms known than the simple comparison based ones. Whether such algorithms exist has remained a central open problem in external memory algorithms for more than three decades.

In this paper, we present a _tight_ conditional lower bound on the complexity of external memory sorting of integers. Our lower bound is based on a famous conjecture in network coding by Li and Li [15], who conjectured that network coding cannot help anything beyond the standard multicommodity flow rate in undirected graphs.

The only previous work connecting the Li and Li conjecture to lower bounds for algorithms is due to Adler et al. [1]. Adler et al. indeed obtain relatively simple lower bounds for _oblivious_ algorithms (the memory access pattern is fixed and independent of the input data). Unfortunately obliviousness is a strong limitations, especially for integer sorting: we show that the Li and Li conjecture implies an \(\Omega(nlgn)\) lower bound for internal memory _oblivious_ sorting when the keys are \(\Theta(lgn)\) bits. This is in sharp contrast to the classic (non-oblivious) Radix Sort algorithm. Indeed going beyond obliviousness is highly non-trivial; we need to introduce several new methods and involved techniques, which are of their own interest, to obtain our tight lower bound for external memory integer sorting.

<sup>∗</sup>{`farhadi, hajiagha`}`@cs.umd.edu`. Supported in part by NSF CAREER award CCF-1053605, NSF AF:Medium grant CCF-1161365, NSF BIGDATA grant IIS-1546108, NSF SPX grant CCF-1822738, UMD AI in Business and Society Seed Grant and UMD Year of Data Science Program Grant. <sup>†</sup>`larsen@cs.au.dk`. Supported by a Villum Young Investigator Grant and an AUFF Starting Grant. <sup>‡</sup>`runting@gmail.com`. Supported in part by NSF under grant number CCF1822805.

Alireza Farhadi <sup>∗</sup> University of Maryland College Park, MD

MohammadTaghi Hajiaghayi <sup>∗</sup> University of Maryland College Park, MD

Kasper Green Larsen <sup>†</sup> Aarhus University Denmark

Elaine Shi<sup>‡</sup> Cornell University Ithaca, NY

