<tbc>was obtained (for the one million sample size).

e) The _randSet_ & _randSet_ model generates search branches at a very high speed. For _n_=1000, the average time to obtain the composition is 0.001372 seconds. The average length of the compositions is 967. Accordingly, for _n_=10<sup>6</sup>, the average time is 1.767318 seconds with an average length of the compositions is 999793.

f) Except for a small interval \(n\le 70\), when the _randSet_ & _randSet_ model in very rare cases can lead to a solution, in all other cases the solution ends with the formation of a negative composition, which cannot be completed.

Thus, the _randSet_ & _randSet_ algorithm has an important advantage - the high speed of forming the search branch, and a significant disadvantage, is that if the composition size exceeds a certain threshold value, then this algorithm leads to form a compositions that cannot be completed. To overcome this drawback, we stop the formation of the search branch when the threshold _baseLevel_<sub>2</sub> is reached.

12
n= 100
10
8
Relative frequency, %
6
4
2
0
65
70
75
80
85
90
95
100
105
Number of correctly placed queens

Figure 2: Histogram of various length compositions, formed on the basis of _randSet_ & _randSet_ model. (_n_=100, sample size =10<sup>6</sup>).

