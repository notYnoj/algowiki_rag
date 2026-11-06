In the second case the bound exceeds the lower bound _a+b_ by (_c(a+b_)-_ab_)<sup>2</sup>/(4_abc_), since (_ab+bc+ca_)<sup>2</sup>-4_abc(a+b_)=(_c(a+b_)-_ab_)<sup>2</sup>. For example, \(\omega_\mathbb{F}(6,3,2)=9\). For _a=b=c_=1, Theorem 1.2 gives \(\omega_\mathbb{F}\le 9/4\) again, and for the shapes (1_,k,_1) it gives the following bounds.

**Corollary 4.17.** _For every real number_ \(k\ge 0\),

\(\omega_\mathbb{F}(1,k,1)\le\left\{\begin{array}{ c c }
2 & \text{\textit{if}}0\le k\le 1/2, \\
1+k+\frac{1}{4k} & \text{\textit{if}}k\ge 1/2.
\end{array}\right.\)

_In particular,_ \(\alpha_\mathbb{F}\ge 1/2\) _and_ \(\omega_\mathbb{F}(1,2,1)\le 25/8\).

_Proof._ Since \(\omega_\mathbb{F}(a,b,c)\) does not depend on the order of _a_, _b_ and _c_, Theorem 1.2 applies to (1,1_,k_) if \(k\le 1\) and to (_k,_1,1) if \(k\ge 1\). If \(k\le 1/2\), its first case applies, since \(2k\le 1\), and gives \(\omega_\mathbb{F}(1,k,1)=2\), so \(\alpha_\mathbb{F}\ge 1/2\). Otherwise its second case applies, and gives

\(\omega_\mathbb{F}(1,k,1)\le\frac{(1+2k)^2}{4k}=1+k+\frac{1}{4k},\)

which is 25/8 for _k_=2.

By Corollary 4.17, we have \(\alpha_\mathbb{F}\ge 1/2\), \(\omega_\mathbb{F}(1,0.709,1)<2.0617\) and \(\omega_\mathbb{F}(1,2,1)\le 25/8\). These bounds improve the bounds \(\alpha_\mathbb{C}>0.465\) and \(\omega_\mathbb{C}(1,0.709,1)<2.092\) of OpenAI, which hold in characteristic zero, the second also outside a finite set of positive characteristics \[Ope26b\]. They also improve the bounds from the laser method: \(\alpha_\mathbb{F}>0.321334\) of Vassilevska Williams, Xu, Xu and Zhou \[WXXZ24\], and \(\omega_\mathbb{F}(1,2,1)\le 3.250035\) of Alman, Duan, Vassilevska Williams, Xu, Xu and Zhou \[ADW<sup>+</sup>25\]. Figure 1 (right) compares them with those of the laser method.

Figure 1 uses that \(\omega_\mathbb{F}\) is subadditive, homogeneous and convex, which follows from taking tensor products and rescaling (Lotti and Romani \[LR83, Section 1\]). So the lower convex hull of upper bounds on \(\omega_\mathbb{F}(1,k,1)\) is also an upper bound, and for all real numbers \(0<b\le 1\) and \(c\ge 0\),

\(\omega_\mathbb{F}(1,b,c)\le\omega_\mathbb{F}(1-b,0,0)+\omega_\mathbb{F}(b,b,c)=1-b+b\omega_\mathbb{F}(1,c/b,1).\)

The bound of Theorem 1.2 is homogeneous of degree one in (_a,b,c_), so its values with \(a=1\ge b\ge c\) determine it. Figure 1 (left) shows these values as a surface.

## 5 Operational barrier

In this section we will prove that no combination of the ingredients (D0)-(D4) by the rules (C1)-(C4) improves the bounds of Theorem 1.2.

To do this, we will define a semiring F of formal combinations of the polynomial multiplication tensors and their permutations, under \(\oplus\), \(\otimes\) and the partial direct sums \(\oplus_i\) (which are not semiring operations, and are only allowed under the natural leg dimension constraint). By "formal combinations" here we mean that we do not a priori identify restriction equivalent or isomorphic tensors. Instead, we define a special preorder \(\unknown\) on F which only encodes the degeneration ingredients (D0)-(D4) and combination rules (C1)-(C4) that we use in the proofs of Theorem 1.2. Thus any degeneration construction from those ingredients and rules can be written in the preorder \(\unknown\).

To prove no degenerations \(\langle n,n,n\rangle\unknown\langle r\rangle\) give log_r/_log_n\<_9/4, the natural approach would be to find a degeneration monotone function \(\phi\) that obstructs \(\langle n,n,n\rangle\unknown\langle r\rangle\) in the sense that \(\phi(\langle n,n,n\rangle)>\phi(\langle r\rangle)\) whenever log_r/_log_n\<_9/4.

