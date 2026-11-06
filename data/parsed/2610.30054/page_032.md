In fact, more abstractly, one may take such \(\phi\) in the asymptotic spectrum \(\Delta_\mathbb{F}\) and use \(\mathrm{max}_{\phi\in\Delta_\mathbb{F}}\phi(\langle 2,2,2\rangle)=2^{\omega_\mathbb{F}}\); that is, if \(\omega_\mathbb{F}=9/4\), then there is a \(\phi\in\Delta_\mathbb{F}\) such that \(\phi(\langle 2,2,2\rangle)=2^{9/4}\), and then \(\phi(\langle n,n,n\rangle)=n^{9/4}\) by basic powering arguments.

We do not know how to obtain such a degeneration monotone \(\phi\); instead, we will restrict ourselves to only work with the semiring of formal expression F and the restricted operational preorder \(\unknown\) on F. We will then construct functions \(F_\theta^\star\) on F that are \(\unknown\)-monotone (they are in fact in the asymptotic spectrum of \((\mathcal{F},\unknown)\)). These functions \(F_\theta^\star\) are constructed in a way that they obstruct all \(\langle n,n,n\rangle\unknown\langle r\rangle\) that can lead to \(\omega_\mathbb{F}<9/4\) (and similarly for the rectangular bounds). This "operational barrier" result is Theorem 5.4.

The challenge lies in constructing the functions \(F_\theta^\star\) as above, which we do in Section 5.4, and prove their monotonicity in Section 5.6 and Section 5.7.

This construction also gives a test for usefulness of different sets of degeneration ingredients to obtain better bounds on \(\omega_\mathbb{F}\): adding them to \(\unknown\) keeps the barrier whenever the functions \(F_\theta^\star\) remain monotone. This we state in Proposition 5.7.

## 5.1 Symmetric notation P_<sub>x,y,z</sub>_ for permuted polynomial multiplication

For convenience in this section, we will use a more symmetric notation for polynomial multiplication tensors and their permutations, \(\pi\cdot\mathsf{P}_{a,b}\). To see how this is natural, recall

\(\mathsf{P}_{a,b}=\sum_{i=1}^a\sum_{j=1}^be_i\otimes e_j\otimes e_{i+j-1}.\)

The terms are of the form \(e_i\otimes e_j\otimes e_k\) with \(i\in[a]\), \(j\in[b]\), \(k\in[a+b-1]\) such that _i+j-k_=1. Replacing _k_ by _a+b-k_ turns the condition _i+j-k_=1 into _i+j+k=a+b_+1=_M_+2, where _M=a+b_-1 is the largest of the three leg dimensions of P_<sub>a,b</sub>_. This definition is more symmetric and is what we use in the following:

**Definition 5.1.** A triple (_x,y,z_) of real numbers \(x,y,z\ge 1\) is _admissible_ if<tbc>

\(x+y+z=2\mathrm{max}(x,y,z)+1,\)

<tbc>that is, if its largest entry is the sum of the other two minus 1. For an admissible triple of integers, with _M_=max(_x,y,z_), let

\(\mathsf{P}_{x,y,z}:=\sum_{\alpha,\beta,\gamma} e_\alpha\otimes e_\beta\otimes e_\gamma\in\mathbb{F}^x\otimes\mathbb{F}^y\otimes\mathbb{F}^z,\)

where the sum is over all \(\alpha\in[x]\), \(\beta\in[y]\) and \(\gamma\in[z]\) with \(\alpha+\beta+\gamma=M+2\).

By the discussion before, we have \(\mathsf{P}_{a,b,a+b-1}\cong\mathsf{P}_{a,b}\). We see directly that permuting the legs of P_<sub>x,y,z</sub>_ permutes _x_, _y_ and _z_. For example, \((23)\cdot\mathsf{P}_{a,b}\cong\mathsf{P}_{a,a+b-1,b}\). Up to isomorphism, the tensors P_<sub>x,y,z</sub>_ for admissible triples (_x,y,z_) of integers are exactly the tensors \(\pi\cdot\mathsf{P}_{a,b}\) for \(\pi\in\mathfrak{S}_3\) and integers \(a,b\ge 1\). We will thus from now on work with P_<sub>x,y,z</sub>_ instead of \(\pi\cdot\mathsf{P}_{a,b}\).

## 5.2 Set F of formal combinations of tensors

We will work with formal combinations of tensors. This will enable us to be very precise about the degeneration ingredients, isomorphisms and combination rules that we allow to apply, by means of a formal preorder that we will define in the next subsection.

We will use formal operations \(\oplus\), \(\otimes\), and also \(\oplus_1,\oplus_2,\oplus_3\), which will represent partial direct sums in the three directions.

