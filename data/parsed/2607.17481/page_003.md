<tbc>Proposition 1 (Soundness). _For every_ \(\mathcal{S}\subseteq\mathcal{U}\)_, the induced profile is a sound upper pan-profile: every finite cell equals the exact z- normalized distance to the valid neighbor it stores, and_ \(P_m^\mathcal{S}[i]\ge P_m[i]\) _for every cell._

Proof. A finite cell equals d_<sub>m</sub>(i,j_) for some evaluated triple \((m,i,j)\in\mathcal{S}\). Every triple of **U** satisfies \(j-i\ge excl\), so the stored neighbor is valid. \(P_m^\mathcal{S}[i]\) is a minimum over a subset of the neighbors defining _P<sub>m</sub>_\[_i_\], so it cannot be smaller than _P<sub>m</sub>_\[_i_\]. □

Panache computes \((\hat{P},\hat{I})=(P^\mathcal{S},I^\mathcal{S})\) for an evaluated set assembled in one pass,

\(\mathcal{S}=\mathcal{S}_\mathrm{stream}\cup\mathcal{S}_\mathrm{hot}\cup\mathcal{S}_\mathrm{local},\)

where S<sub>stream</sub> is generated during the streaming pass (§3.1-3.5) and S<sub>hot</sub> and S<sub>local</sub> are added by the emit stage (§3.6). Proposition 1 separates correctness from coverage. Written values are correct for any choice of S; the remaining design question is which pairs to evaluate.

Every such choice must fit within a budget fixed before the stream starts. Per arriving sample and indexed length (§3.3), that budget is _O(K_) for the spectral state, _O(BK_) for the signature, and at most _R_ candidate inspections (_K_: retained spectral width, §3.2; _B_: signature bits, §3.4; _R_: verification budget, §3.4). The sections below describe the mechanisms that keep this budget effective as _n_ grows. Anchor lengths cover the length interval (§3.3), occupancy control keeps the hash directory bounded (§3.4), and exclusion-zone batching parallelizes the stream while keeping the output identical to serial processing (§3.5). Emit-time completion evaluates the oversized hash classes and the motif neighborhoods at non-anchor lengths, completing the evaluated set S (§3.6). Algorithms 1 and 2 (appendix) list the update and emit procedures. Figure 2 illustrates each stage on an ECG5000 motif pair (_i_=3925, _j_=7564, _m_=20), and its panels are referenced throughout the section.

## 3.1 Windows on a Stream

An offline PMP computation holds the full series, so a window is identified by where it starts. The algorithm picks a start position and reads the _m_ samples to its right. A stream allows no such choice. Samples arrive one at a time, and a window can be used only once its last sample has arrived, so the latest published sample decides which windows exist. Windows on a stream are therefore indexed by their right endpoints. Let \(\tau\) be the index of the most recently published sample. A length-_m_ window with start _q_ completes at \(\tau=q+m-1\), the moment its last sample arrives. Until then its mean, its variance, its non-DC spectrum, and its distance to any other window do not exist. When sample \(\tau\) is published, exactly one new window completes at every length \(m\le\tau+1\), namely \(T_{\tau-m+1,m}\).

For each _anchor length_ \(a\in A\subseteq[m_\mathrm{min},m_\mathrm{max}]\), the subset chosen in §3.3, Panache maintains one sliding window. The length-_a_ window completes for the first time at \(\tau=a-1\), and every later sample slides it to the start \(q=\tau-a+1\) (Figure 2A). Recomputing the window at every slide would read all _a_ samples for a one-position change. Instead, Panache maintains an online running state (§3.2). At each slide the oldest sample leaves on the left and the newest enters on the right, the state is corrected for exactly those two samples at cost _O(K_), and the same state is carried through the<tbc>

<tbc>entire series. The raw samples are retained, so the exact distance of any pair of completed windows can be computed at any later time.

A sample does not belong to one length. Take lengths 2 and 3 on a stream _t_<sub>0</sub>_,t_<sub>1</sub>_,t_<sub>2</sub>_,..._. When _t_<sub>1</sub> arrives, the first length-2 window (_t_<sub>0</sub>_,t_<sub>1</sub>) completes. When _t_<sub>2</sub> arrives, that window slides to (_t_<sub>1</sub>_,t_<sub>2</sub>), and the first length-3 window (_t_<sub>0</sub>_,t_<sub>1</sub>_,t_<sub>2</sub>) completes. When _t_<sub>3</sub> arrives, both windows slide at once, to (_t_<sub>2</sub>_,t_<sub>3</sub>) and (_t_<sub>1</sub>_,t_<sub>2</sub>_,t_<sub>3</sub>). The arriving sample _t_<sub>3</sub> enters both windows, while each window drops a different sample. Every later arrival behaves the same way. Panache holds one running state per anchor length, each published sample advances all of them together, at _O(K_) per length and _O_(|_A|K_) in total.

## 3.2 Normalized Spectral Features

Each sliding window’s state has three jobs. It must be updated at every slide, provide the signature under which similar windows collide, and yield the Parseval bound that rejects colliding pairs. The normalized non-DC Fourier coefficients do all three.

For a window _T<sub>i,m</sub>_, define the DFT coefficients<tbc>

\(X_{i,m,k}=\sum_{r=0}^{m-1}t_{i+r}e^{-2\pi ikr/m}.\)

<tbc>The coefficient _X_<sub>_i,m,_0</sub> is proportional to the window mean; the coefficients with _k\>_0 describe variation around that mean level. At an indexed length, Panache retains the scaled prefix \(F_{i,m}=(X_{i,m,1},\dots,X_{i,m,K^\prime})/\sigma_{i,m}\), zero-padded to the shared width _K_-1, where

\(K'=\mathrm{min}\big(K-1,\lceil m/2\rceil-1\big)\)

is the number of independent non-DC coefficients at length _m_: by conjugate symmetry bin _k_ and bin _m-k_ are mirror images, and for \(k\ge m\) the index aliases back onto the mean, so only bins \(1\le k\le K'\) carry new shape information (for even _m_ the Nyquist bin _m/_2 is omitted). Real and imaginary parts are kept; the DC coefficient is not stored.

Lemma 1 (AC invariance). _Let_ \(\hat{X}_{i,m,k}\) _be the DFT coefficient of the z-normalized window Z<sub>i,m</sub>. For every_ \(1\le k\le m-1\), \(\hat{X}_{i,m,k}=X_{i,m,k}/\sigma_{i,m}\).

Proof. Centering subtracts \(\mu_{i,m}G_{k,m}\) from coefficient _k_, where \(G_{k,m}=\sum_{r=0}^{m-1}e^{-2\pi ikr/m}\). This geometric sum is zero for \(k\unknown=0(\mathrm{mod}m)\). Scaling by \(\sigma_{i,m}^{-1}\) scales the remaining coefficients. □

The stored vector _F<sub>i,m</sub>_ therefore equals the leading \(K'\) independent bins of the non-DC spectrum of the z-normalized window (Figure 2A), the remaining entries zero. Mean subtraction affects only the DC bin, and the division by the standard deviation scales all bins uniformly.

_Online update._ A slide changes the window only at its ends. The departing sample leaves, the arriving sample enters, and every retained sample keeps its value while its position inside the window drops by one. This is the fact the sliding DFT exploits. A DFT coefficient is a sum of samples, each weighted by a phase factor \(e^{-2\pi ikr/m}\) that depends on its position _r_. When every position drops by one, every phase factor is multiplied by the same fixed rotation \(e^{2\pi ik/m}\). One multiplication of the coefficient therefore re-phases<tbc>

