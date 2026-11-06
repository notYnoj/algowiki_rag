<tbc>as noise in the reconstruction space \[15\]. Thus, allowing delay-coordinate maps to combine delays of fast and slow frequencies may improve the embedding quality.

In other situations, while the system itself may not involve multi-scale dynamics, the measurement apparatus may sample the system at non-uniformly-spaced intervals, especially when considering mobile sensors or event-based rather than time- based sensing. Sauer \[16\], for example, proposed an event- based "interspike interval" detection mechanism, which, rather than measuring a system at set time intervals, initiates a measurement based on the state of the system. Huke et al. \[17\] established theoretical results on the conditions needed for delay-coordinates using such a mechanism to be embeddings and extended it to time-based observation functions in general.

A central challenge with delay-coordinate maps with unevenly-spaced delays is that, unlike delay-coordinate maps with evenly-spaced delays that have only two parameters to optimize (namely, the number of delays \(\ell\) and the time delay \(\tau\)), maps of non-uniform delays must optimize over \(\ell\) distinct delay parameters \(\{\tau_k\}_{k=1}^\ell\). The optimization problem is combinatorially complex, making such maps unwieldy and/or intractable. However, a number of works have developed algorithms to address this and make such mappings relevant \[15\], \[18\], \[19\].

It is the purpose of this paper to provide an extension to the stable linear Takens’ embedding for linear systems developed by Yap and Rozell \[6\] to the case of delay- coordinate maps of non-uniform delays. In Section II, we provide the relevant background for stable linear time-delay embeddings. In Section III, we establish the main theoretical results for delay-coordinate maps with unevenly-spaced delays, beginning with a description of the connection between Fourier Vandermonde matrices and linear delay-coordinate maps with evenly-spaced delays. To extend the stable linear Takens’ embedding to the non-uniform sampling setting, it is necessary to consider a form of generalized Vandermonde matrices that involve non-integer and unevenly-spaced powers and that have more lags than points considered. Just as typical Vandermonde matrices require a distinct set of points and a distinct set of consecutive, evenly-spaced integer powers to be full rank-which translate to relatively reasonable assumptions that the underlying frequencies in a given signal are not duplicated and are sampled at evenly-spaced time intervals, so too would it be reasonable to assume that, if a signal has distinct frequencies and is measured at distinct but not evenly- spaced time instants, then the generalized Vandermonde matrix modeling it ought to be full rank with probability one. To verify the claim, we provide conditions under which such<tbc>

Phase Portrait (Original State Space)
Time Series (Original State Space)
Time-Delay Embedding (Delay-Coordinate Space)
x(t - 2T)
x(t - T)
x(t)
x(t - T)
x(t - 2T)
A (Uniformly-Spaced Delays)
x(t)
x(t - 2T)
x(t - T)
x(t)
x(t)
t
Phase Portrait (Original State Space)
Time Series (Original State Space)
Time-Delay Embedding (Delay-Coordinate Space)
x(t - T2)
x(t - T2)
x(t - T1)
x(t)
x(t - T2)
x(t - T1)
x(t - T2)
x(t - T2)
x(t)
x(t - T2)
x(t - T1)
x(t)
x(t)
x(t)
t
x(t)

Fig. 1. An undamped harmonic oscillator \(\mathaccent\unknown{x}(t)+\omega x(t)=0\) with solutions \(x(t)=cos(\omega t)\) and \(v(t)=-\omega sin(\omega t)\) is a class A(1) system (see Definition 1). For this setting, \(\omega=2\pi\). For _x(t_) being the observed state variable (with the observation function being \(h:[x(t),v(t)]\rightarrow x(t)\), i.e. measuring only the position and not velocity), we plot the position versus normalized velocity phase portraits, the time series for the position function, and the _x(t_)-based time-delay embeddings using \(\ell=3\) delays, depicted for (A) the case of uniformly-spaced delays in the delay-coordinate map with \(\tau=0.13(x(t),x(t-\tau),x(t-2\tau))\), and (B) the case of the non-uniformly-spaced delays with \(\tau_1=0.08\) and \(\tau_2=0.34(x(t),x(t-\tau_1),x(t-\tau_2))\). The delay-coordinate maps preserve the topological and differential structure of the attractor in the reconstruction space, ensuring the original signal is recoverable, but differ from each other based on the choice of time delays.

