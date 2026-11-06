_Proof of Theorem 1._ The exact checks establish admissibility of the supplied rational witness. Apply Proposition 1 using the positive lower endpoint in (20). The strict gap permits the choice of \(\varepsilon\) in Section 2.4, proving the _O(n_<sup>2.37115924</sup>) arithmetic bound. A matrix multiplication algorithm over Q remains valid after extending scalars, giving the asserted consequence for characteristic-zero extensions.

### 4.2 Reproduction and scope

The ancillary directory contains the witness in `witness.json` and the checker in `verify.py` and `rigorous\_interval.py`. The recorded result is `expected\_result.json`; documentation is included alongside these files. With Python 3.10 or later, the verification command is

`python3 verify.py witness.json --target 2.37115924 \`

`--out result.json`

The checker uses only the standard library. It requires no package installation, model, remote service, credentials, or network access. The exact witness bytes have SHA-256 digest

`87f5e7a8c722ca05464920c99c64083e5fa`

`8235d1822720278e5a058485532ff`

where the two lines are concatenated. The package also includes file-level checksums. A regenerated result can be compared with the recorded rational endpoints; elapsed time and diagnostic output are not part of the mathematical certificate.

This is a computer-assisted proof relying on the cited tensor theorem and the supplied finite arithmetic calculation. The verifier is auditable source code, rather than a proof-assistant formalization of the full tensor theorem. Verification reproduces the bound from the final witness. It does not replay the numerical optimization trajectory, whose last continuation inherits an earlier point and multipliers. The optimization libraries used to discover the point are therefore unnecessary for verifying it.

## 5 Discussion

The certified construction improves the asymptotic arithmetic complexity of matrix multiplication within the established combination-loss framework. Its algorithmic content is the rational recursive extraction plan, which fixes the allocation of tensor constituents and the tradeoff between retained multiplicity and matrix size. The exact certificate turns that plan into a theorem about matrix multiplication.

The computational methodology addresses three coupled difficulties: weak gradients from rare recursive occurrences, a retained exponent controlled by competing minima, and entropy penalties that must survive rational export. Mass-dependent conditioning, a low-dimensional bottleneck<tbc>

\begin{tabular}{ccc}
Quantity & Lower endpoint & Upper endpoint \\
\(\widehat{E}\) & 8.1061402482833692887887 & 8.1061402482833692887888 \\
_M_ & 6.0530304732690271387406 & 6.0530304732690271387407 \\
_C_ & 22.4588393764608328595357 & 22.4588393764608328595358 \\
\(\widehat{\Omega}\) & 2.3711592385931075066123 & 2.3711592385931075066124 \\
\end{tabular}

2: Outward enclosures obtained from the rational witness.

