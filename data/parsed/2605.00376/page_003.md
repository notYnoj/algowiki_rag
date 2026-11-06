This paper is organized as follows. In Section 2, we introduce the fundamental concepts used throughout the paper. Section 3 details the construction of the MDS array codes used in this work. Next, Section 4 presents decoding algorithms for MDS array codes capable of correcting up to two symbol errors, together with a simplification for the two-error case when Vandermonde matrices are employed. In Subsection 4.1, these algorithms are further examined in the context of correcting three symbol errors. Finally, Section 5 summarizes the main results and discusses directions for future research.

## 2. Initial Concepts

A **linear code** _C_ is a _K_-dimension subspace of \(\mathbb{F}_q^N\), where F_<sub>q</sub>_ is a finite field with _q_ elements. We describe the code _C_ through the parameters \[_N,K,D_\], where _N_ is the code length, _K_ is the dimension and _D_ is the minimum Hamming distance. For a linear code _C_ we can calculate a bound to the number of codewords, which is given by the following theorem.

**Theorem 2.1.** _\[15\](Singleton Bound) If C is a linear code_ \[_N,K,D_\] _over_ F_<sub>q</sub> then the maximum number of possible codewords is q<sup>K</sup> and the Singleton bound says that_

\(q^K\le q^{N-D+1},\) (2.1)

_or equivalently_

\(D\le N-K+1.\) (2.2)

A code in which equality is achieved on (2.2) is called a **maximum distance separable - MDS** code, which means that no code of length _N_ and minimum distance _D_ has more codewords than an MDS code with the same parameters.

Now, if we take _b\>_0 as a positive integer such that _b_ divides _K_ and _N_, then we can construct a **linear array code** _C_ over \(\mathbb{F}_q^b\), with parameters \[_n,k,d_\], where _k=K/b,n=N/b_ and the minimum distance _d_ is calculated considering the code over \(\mathbb{F}_q^b\). Such codes can be specified by their parity-check matrix _H_ of dimension \((n-k)b\times nb\), generating codewords of length _nb_, where each block of _b_ symbols is regarded as an element of \(\mathbb{F}_q^b\). In this setting, the error model corresponds to errors affecting entire symbols over \(\mathbb{F}_q^b\), rather than errors in individual scalar components. The Singleton bound is still valid in linear array codes, that is, \(d\le n-k+1\). And if equality is achieved we have an **MDS linear array code**.

Next, we present some concepts that will be used in the construction of MDS array codes and in the decoding algorithms developed in this work. Let F_<sub>q<sup>b</sup></sub>_ be the extension field of F_<sub>q</sub>_ of degree _b_, and let \(\alpha\in\mathbb{F}_{q^b}\) be a primitive element, that is, a root of a primitive polynomial \(p(x)\in\mathbb{F}_q[x]\). Throughout the paper, we identify F_<sub>q<sup>b</sup></sub>_ with \(\mathbb{F}_q^b\) as a vector space over F_<sub>q</sub>_ via a fixed basis, so that each symbol over F_<sub>q<sup>b</sup></sub>_ is represented as a block of _b_ components over F_<sub>q</sub>_. We denote by \(M_{m\times n}(\mathbb{F}_q)\) the space of \(m\times n\) matrices with entries in F_<sub>q</sub>_.

**Definition 2.1.** A matrix \(A\in M_{m\times n}(\mathbb{F}_q)\) is called **superregular** if every square submatrix of _A_ is nonsingular, that is, all its determinants are nonzero.

**Definition 2.2.** A matrix \(A\in M_{mb\times nb}(\mathbb{F}_q)\) is said to be a **superregular** _b_**-block matrix** if every square submatrix of _A_ formed by full \(b\times b\) blocks is nonsingular over F_<sub>q</sub>_.

In the context of coding theory, superregular matrices with entries in the finite field F_<sub>q</sub>_ can be used to generate linear codes and linear array codes with good distance properties.

**Proposition 2.1.** _\[19\] Let C be a linear code_ \[_N,K,D_\] _over a finite field_ F_<sub>q</sub>. The following conditions are equivalent to C being MDS:_

(_1)_ _Every set of N-K columns of a H parity-check matrix of C is linearly independent._<tbc>

(_2)_ _Every set of K columns of a generator matrix of_ C _is linearly independent._<tbc>

