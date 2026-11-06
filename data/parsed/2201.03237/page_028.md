<tbc>Therefore, there is<tbc>

\(\frac{\int_0^{\pi-\frac{\varphi}{2}}\mathrm{sin}^{d-2}\theta_1d\theta_1}{\int_0^\pi\mathrm{sin}^{d-2}\theta_1d\theta_1}\ge\frac{\int_0^{\pi-\frac{\varphi}{2}}\mathrm{sin}^{d-4}\theta_1d\theta_1}{\int_0^\pi\mathrm{sin}^{d-4}\theta_1d\theta_1}\)

\(\ge\left\{\begin{array}{ c c c }
1-\frac{\varphi}{2\pi},d & \text{\textit{is}} & \text{\textit{even}} \\
\frac{1+\mathrm{cos}\frac{\varphi}{2}}{2},d & \text{\textit{is}} & \text{\textit{odd}}
\end{array}\right.\)

<tbc>because \(\frac{1+\mathrm{cos}\frac{\varphi}{2}}{2}\ge 1-\frac{\varphi}{2\pi}\), there is

\(Prob\ge 1-\frac{\varphi}{2\pi}\)

## 6.2. parameter

Here we list the value of parameters used for construction of indices. It is worth mentioning that the DPG is constructed based on KGraph and we cancel the addition of the reverse edges in Glove and Crawl.

1. Sift We use _k_=100_,mp_=0.53_,m_=50 for TBSG, \(l=100,r=50,\alpha=60^\circ,m=10\) for NSSG, _M_=25_,efconstruction_=600 for HNSW,\(K=100,L=100,S=10,R=100,I=12\) for KGraph, _L_<sub>2</sub>=30 for DPG, _num\_hash\_tables_=50_,num\_hash\_bits_=18 for FALCONN, IVF4096, PQ64+64 for Faiss.<tbc>

2. Gist We use _k_=200_,mp_=0.515_,m_=70 for TBSG,\(l=500,r=70,\alpha=60^\circ,m=10\) for NSSG, _M_=35_,efconstruction_=800 for HNSW, \(K=400,L=400,S=15,R=100,I=12\) for KGraph, _L_<sub>2</sub>=40 for DPG, _num\_hash\_tables_=50_,num\_hash\_bits_=18 for FALCONN, IVF4096, PQ240+240 for Faiss.<tbc>

3. Glove We use _k_=300_,mp_=0.53_,m_=80 for TBSG, \(l=500,r=50,\alpha=60^\circ,m=10\) for NSSG, _M_=40_,efconstruction_=2500 for HNSW, _K_=400_,L_=420_,S_=20_,R_=200_,I_=12 for KGraph, _L_<sub>2</sub>=200 for DPG, _num<sub>h</sub>ash<sub>t</sub>ables_=50_,num\_hash\_bits_=18 for FALCONN,_num\_hash\_tables_=50_,num\_hash\_bits_=18 for FALCONN, IVF4096, PQ50+50 for Faiss.<tbc>

