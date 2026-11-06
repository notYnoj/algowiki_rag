<tbc>efficiently derive \(\mathrm{dist}_d\left(\mathbf{T}_a,\mathbf{T}_b\right)\forall d\in[1,D]\). The condition of line 15 is initially based on _d<sub>low</sub>_ and gradually increases every time the lowest dimensionality has its motif confirmed. This approach allows to return solutions for each motif dimensionality as soon as their error probabilities satisfy the required quality, inheriting the anytime property.

## 7 EXPERIMENTS

This section aims at answering the following questions:

\(\bullet\) How does our algorithm compare with the state-of-the-art?<tbc>

\(\bullet\) How do parameters _K_, _L_, _r_ and \(\delta\) influence the performance?<tbc>

\(\bullet\) How does the algorithm scale with respect to the input size?<tbc>

\(\bullet\) Is the algorithm able to find motifs in high dimensional noisy time series?

### Baselines.

Our algorithm is compared to Mstump \[23\], the state- of-the-art implementation for the multidimensional matrix profile. We stress that Mstump is an _exact_ algorithm that computes more information than just the motifs: for instance it can be used to detect discords. Our aim is to investigate the gains that can be attained when only motifs are sought, and when a small failure probability is accepted. Alongside, we consider the Extended Motif Discovery (EMD) algorithm \[37\], reimplemented in \[22\], and the Random Projection (RP) algorithm \[29\], reimplemented by us, for comparisons with approximate approaches. We refer to our algorithm as MOMENTI, which stands for MOtifs in MultidimEnsoNal TIMeries. All algorithms were subject to a global timeout of 4 hours per execution for datasets under the million points, and 24 hours for larger datasets.

### Experimental Setup.

The evaluation was carried out on a machine with a 8 core Intel Xeon W-2245 @ 3.90 GHz equipped with 128 GB of memory.

### Datasets.

All the experiments are run on the following real datasets from different domains, whose details can be found in  2.

\(\bullet\) Potentials is a record of skin potentials \[16\];<tbc>

\(\bullet\) Evaporator is data from a four-stage evaporator to reduce the water content from products \[17\];<tbc>

\(\bullet\) Ruth, the Mel-spectrogram of the song _Running Up That Hill_ by Kate Bush, extracted with the following parameters: 32-Mel scale filters, 46 milliseconds short time Fourier transform window and 23 milliseconds hop;<tbc>

\(\bullet\) Weather is representing the hourly climate data near Monash University, in Australia, for about 10 years \[19\];<tbc>

\(\bullet\) Whales is obtained from data of an underwater passive acoustic network and is a 10 minute recording of humpback whales vocalizations \[32\];<tbc>

\(\bullet\) Quake is a waveform from the Observatories and Research Facilities for European Seismology (ORFEUS) during the 2014 Aegean Sea earthquake \[28\];<tbc>

\(\bullet\) El\_load includes cleaned electrical consumption data in Watts for 20 households at aggregate and appliance level \[31\];<tbc>

\(\bullet\) LTMM contains 3-day 3D accelerometer recordings of elder community residents, used to study gait, stability, and fall risk \[20, 21\].

The choice of the reference motif dimensionality _d_ for each dataset is guided by the additional information available. Specifically, for Potentials, Evaporator and Weather we use metadata information for the expected dimensionality of the pattern. For Ruth and Whales, we follow previous work on audio data to find, respectively, the drum pattern of the song and whale harmonization \[41\]. Finally, El\_load, Quake and LtMM were chosen based on the domain information.

Furthermore, we characterize each dataset by the _contrast c_<sub>_d,_1|_n_</sub> of its top _d_-dimensional motif, as per Definition 5.1. Datasets with a small contrast are expected to be more difficult, i.e. require more time to find the top motif. For instance El\_load is expected to be more difficult compared to Weather, since the latter has a pair of subsequences that repeat the same shape at a distance that is significantly smaller than the _n_-th closest pair.

### Default parameter values.

MOMENTI will have its parameters set to default unless otherwise indicated. The failure probability is set at \(\delta=0.01\), the maximum hash length is set to _K=_8, while the maximum number of repetitions is set to _L=_200. _r_ is automatically estimated using the heuristic introduced in Section 6.1.

### 7.1 Finding the top motif

In this first experiment, the task is to find the top motif at a given dimensionality _d_ (as per  2). For each dataset we report the total running time of the baselines Mstump, EMD and RP in the last three columns, whereas for our approach we report both the total time and the time required to set up the index. All times are in<tbc>

\begin{tabular}{cccccc}
dataset & n & D & window & _d_ & _c_<sub>_d,_1|_n_</sub> \\
potentials & 2 500 & 8 & 50 & 8 & 6.11 \\
evaporator & 7 000 & 5 & 75 & 2 & 2.60 \\
RUTH & 14 859 & 32 & 500 & 4 & 3.24 \\
weather & 100 057 & 8 & 5000 & 2 & 2.43 \\
whales & 450 001 & 32 & 300 & 6 & 1.22<sup>∗</sup> \\
quake & 6 440 998 & 32 & 100 & 4 & 1.65<sup>∗</sup> \\
electrical\_load & 6 960 008 & 10 & 1000 & 5 & 1.91<sup>∗</sup> \\
LTMM & 25 132 289 & 6 & 200 & 3 & 5.31<sup>∗</sup> \\
\multicolumn{6}{c}{<sup>∗</sup> obtained through random sampling.} \\
\end{tabular}

\begin{tabular}{cccccc}
dataset & \multicolumn{2}{c}{MOMENTI} & MSTUMP & EMD & RP \\
 & Index build & Total & & & \\
potentials & 0.11 & 0.51 & 3.65 & 4.80 & 3.20 \\
evaporator & 0.16 & 0.55 & 4.45 & 12.95 & 6.78 \\
RUTH & 2.91 & 8.10 & 84.04 & 1.5h & 2.3h \\
weather & 15.04 & 33.37 & 1035.73 & - & 1.2h \\
whales & 60.67 & 2.2 h & (2.7 days) & - & - \\
quake & 175.3 & 3.6 h & (7.2 days) & - & - \\
el\_load & 180.2 & 2.8 h & (8.4 days) & - & - \\
LTMM & 240.6 & 15.6 h & (11.8 days) & - & - \\
\end{tabular}

** 2: Information about the evaluation datasets.**

** 3: Time required to find the** _d_**-dimensional top motif, for fixed** _d_**, averaged over 9 runs. Values in parentheses are estimates.**

