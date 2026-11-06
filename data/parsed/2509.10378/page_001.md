# Matrix-free Neural Preconditioner for the Dirac Operator in Lattice Gauge Theory<sup>∗</sup>

YIXUAN SUN and SRINIVAS ESWAR, Argonne National Laboratory, USA YIN LIN, Massachusetts Institute of Technology, USA WILLIAM DETMOLD and PHIALA SHANAHAN, Massachusetts Institute of Technology & The NSF AI Institute for Artificial Intelligence and Fundamental Interactions, USA YANG LIU and XIAOYE LI, Lawrance Berkeley National Laboratory, USA PRASANNA BALAPRAKASH, Oak Ridge National Laboratory, USA

Linear systems arise in generating samples and in calculating observables in lattice quantum chromodynamics (QCD). Solving the Hermitian positive definite systems, which are sparse but ill-conditioned, involves using iterative methods, such as Conjugate Gradient (CG), which are time-consuming and computationally expensive. Preconditioners can effectively accelerate this process, with the state-of-the-art being multigrid preconditioners. However, constructing useful preconditioners can be challenging, adding additional computational overhead, especially in large linear systems. We propose a framework, leveraging operator learning techniques, to construct linear maps as effective preconditioners. The method in this work does _not_ rely on explicit matrices from either the original linear systems or the produced preconditioners, allowing efficient model training and application in the CG solver. In the context of the Schwinger model (_U_(1) gauge theory in 1+1 spacetime dimensions with two degenerate-mass fermions), this preconditioning scheme effectively decreases the condition number of the linear systems and approximately halves the number of iterations required for convergence in relevant parameter ranges. We further demonstrate the framework learns a general mapping dependent on the lattice structure which leads to zero-shot learning ability for the Dirac operators constructed from gauge field configurations of different sizes.

CCS Concepts: • Applied computing \(\rightarrow\) Physics; • Computing methodologies \(\rightarrow\) Neural networks.

Additional Key Words and Phrases: preconditioners, neural operator, lattice gauge theory

**ACM Reference Format:**

Yixuan Sun, Srinivas Eswar, Yin Lin, William Detmold, Phiala Shanahan, Yang Liu, Xiaoye Li, and Prasanna Balaprakash. 2026. Matrix-free Neural Preconditioner for the Dirac Operator in Lattice Gauge Theory. _ACM Trans. AI Sci._ 1, 1 (August 2026), 22 pages.

<sup>∗</sup>Preprint No. MIT-CTP/5915, INT-PUB-25-022 Authors’ Contact Information: Yixuan Sun , yixuan.sun@anl.gov; Srinivas Eswar, seswar@anl.gov, Argonne National Laboratory, Lemont, Illinois, USA; Yin Lin, yin01@mit.edu, Massachusetts Institute of Technology, Lemont, Illinois, USA; William Detmold, wdetmold@mit.edu; Phiala Shanahan, pshana@mit.edu, Massachusetts Institute of Technology & The NSF AI Institute for Artificial Intelligence and Fundamental Interactions, Cambridge, Massachusetts, USA; Yang Liu, liuyangzhuan@lbl.gov; Xiaoye Li, xsli@lbl.gov, Lawrance Berkeley National Laboratory, Berkeley, California, USA; Prasanna Balaprakash, pbalapra@ornl.gov, Oak Ridge National Laboratory, Oak Ridge, Tennessee, USA. © 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM. This is the author’s version of the work. It is posted here for your personal use. Not for redistribution. The definitive Version of Record was published in _ACM Transactions on AI for Science._

arXiv:2509.10378v2 [hep-lat] 9 Aug 2026

