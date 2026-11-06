## 4.1 Spectral points, asymptotic spectrum duality, and basic properties

In this subsection we will define Strassen’s asymptotic spectrum, whose elements are called spectral points, and state the properties that we will use, including the asymptotic spectrum duality theorem. Strassen introduced these to study the asymptotic restriction of tensors, and in particular the exponent of matrix multiplication \[Str88\]. For background, see the survey of Wigderson and Zuiddam \[WZ26\].

**Definition 4.1** (Strassen \[Str88, Section 3\])**.** A _spectral point_ is a map \(\phi:\mathcal{S}_\mathbb{F}\rightarrow\mathbb{R}_{\ge 0}\) such that \(\phi(\langle 1\rangle)=1\) and, for all tensors _S_ and _T_ over F, we have \(\phi(S\oplus T)=\phi(S)+\phi(T)\) and \(\phi(S\otimes T)=\phi(S)\phi(T)\), and if \(T\le S\), then \(\phi(T)\le\phi(S)\). The _asymptotic spectrum_ of tensors over F is the set \(\Delta_\mathbb{F}\) of spectral points.

For the upper bounds on \(\omega_\mathbb{F}\) and \(\omega_\mathbb{F}(a,b,c)\), we will not need to know what the spectral points are beyond their abstract definition! Spectral points have been constructed explicitly, but it is not known whether these constructions give all of the asymptotic spectrum \[Str91, CVZ23, SDW26\].

The simplest spectral points are the flattening ranks R<sub>(1)</sub>, R<sub>(2)</sub> and R<sub>(3)</sub> of Section 2.2, since the rank of matrices is normalised, additive, multiplicative and monotone under restriction. They are the only explicit spectral points that we will use, in examples and to show that some of the bounds are attained.

From the definition it readily follows that spectral points lower bound the matrix multiplication exponent: for every \(\phi\in\Delta_\mathbb{F}\) we have \(log\phi(\langle 2,2,2\rangle)\le\omega_\mathbb{F}\). Strassen proved that these spectral point lower bounds are complete:

**Theorem 4.2** (Strassen \[Str88, Theorem 3.8 and Proposition 4.2\])**.** _We have_

\(max_{\phi\in\Delta_\mathbb{F}}log\phi(\langle 2,2,2\rangle)=\omega_\mathbb{F}.\)

To upper bound \(\omega_\mathbb{F}\) it thus suffices to upper bound \(\phi(\langle 2,2,2\rangle)\) for every \(\phi\in\Delta_\mathbb{F}\). This we will do by taking the degenerations constructed in Section 3, applying the spectral points to them, and optimising over these inequalities to upper bound the value of \(\phi(\langle 2,2,2\rangle)\). In Section 5 we will show that no combination of these degenerations by the combination rules gives a better bound.

The values of a spectral point \(\phi\) at the tensors \(\langle 1,1,2\rangle\), \(\langle 2,1,1\rangle\) and \(\langle 1,2,1\rangle\) will play a central role. The following are the basic properties of spectral points that we will need. For a given \(\pi\in\mathfrak{S}_3\), we define the permutation \(\phi_\pi\) of \(\phi\) as

\(\phi_\pi(T):=\phi(\pi\cdot T).\) (4.1)

**Lemma 4.3** (Strassen \[Str87, Proposition 5.10\], \[Str88, Theorem 3.1 and Proposition 4.3\])**.** _Let_ \(\phi\in\Delta_\mathbb{F}\).

(i) _For all tensors S and T over_ F _with_ \(T\triangleleft S\)_, we have_ \(\phi(T)\le\phi(S)\).<tbc>

(ii) _For every integer_ \(n\ge 0\)_, we have_ \(\phi(\langle n\rangle)=n\).<tbc>

(iii) _For every nonzero tensor T over_ F_, we have_ \(\phi(T)\ge 1\).<tbc>

(iv) _The values_ \(\phi(\langle 1,1,2\rangle)\), \(\phi(\langle 2,1,1\rangle)\) _and_ \(\phi(\langle 1,2,1\rangle)\) _lie in the interval_ \[1,2\]_, and for all integers_ \(n_1,n_2,n_3\ge 1\),<tbc>

<tbc>\(\phi(\langle n_1,n_2,n_3\rangle)=\phi(\langle 2,1,1\rangle)^{logn_1}\phi(\langle 1,2,1\rangle)^{logn_2}\phi(\langle 1,1,2\rangle)^{logn_3}.\)<tbc>

<tbc>_In particular,_ \(\phi(\langle m,m,m\rangle)=\phi(\langle 2,2,2\rangle)^{logn}\) _for every integer_ \(m\ge 1\).<tbc>

