## 7.4 Crossover Calculations for Different Datatypes

- Datatype - Int (32-bit): Max value is \(2^{31}-1\approx 2.147\times 10^9\)<tbc>

**-** Datatype - Long Long (64-bit): Max value is \(2^{63}-1\approx 9.223\times 10^{18}\)

Assuming _k<sub>max</sub>_ to be the maximum possible value for the largest common datatype (64-bit unsigned integer), we can find the crossover point for _n_ as given below:<br>
\(k_{max}\le n^{log_2n}\). That is, \(n^{log_2n}\ge 2^{63}-1\).<br>
Taking log<sub>10</sub> of both sides, we get \(log_{10}(n^{log_2n})\ge log_{10}(2^{63}-1)\). This implies, \((log_2n)\cdot(log_{10}n)\ge 18.9648\). Since \(log_2n=\frac{log_{10}n}{log_{10}2}\) , we get \(\left(\frac{log_{10}n}{log_{10}2}\right)\cdot(log_{10}n)\ge 18.9648\). From this we get, \(\frac{(log_{10}n)^2}{0.30103}\ge 18.9648\). That is, \((log_{10}n)^2\ge 5.7081\Longrightarrow log_{10}n\ge\approx 2.3891\). This implies, \(n\ge 10^{2.3891}=n\ge 245.004\). Therefore, we get, _n\>_245<br>
This is the theoretical crossover point which implies that when sorting an array containing the maximum possible 64-bit integer value, BNRS algorithm is guaranteed to be theoretically faster than any comparison-based sorting algorithm for average case once the input size surpasses 245 elements.

## 7.5 Algorithms - SP-LSD and Demonstration of SP-LSD

We present some details below for understanding Algorithms 1 and 2.

- Algorithm 2 (Counting-Sort-by-Digit) is a helper function that calls Counting Sort as a subroutine for sorting a portion of the array, here called for the active region.<tbc>

- Algorithm 1 (SP-LSD-Sort) breaks down the sorting process into 3 distinct stages determined by the rounds, total number of rounds is calculated by \(R\leftarrow\lfloor log_n(max\text{\_}val)\rfloor+1\) (see line 9 of Algorithm 1). The first stage applies sorting to the entire input, the second stage runs the core optimization by partitioning the array into ’sorted’ and ’active’ regions using _first\_active_ iterator to mark the active region, \(div\leftarrow n^{r-1}\) (see line 17 of Algorithm 1) where _r_ is iterated value from 2 to _R_-1, Stable-Partition is called from _first\_active_ to the ’past-the-end’ iterator. The final stage is the round _R_-1, where Counting Sort is called for the remaining active region.

We now present two examples where the second example is a bad case for a poor input.

## 7.6 Example1: Demonstration of SP-LSD

**Input:** _A_=\[4,1,620,124,3\], Base (_n_): 5, Max Value (_k_): 620, Rounds Needed: \(\lfloor log_5(620)\rfloor+1=4\).

_Initial State_ The array is in its original unsorted state. `first\_active\_idx = 0`.

\begin{tabular}{cccc}
0 & 1 & 2 & 3 & 4 \\
4 & 1 & 620 & 124 & 3 \\
\end{tabular}

