[SSSV25] Raghuvansh Saxena, Noah G. Singer, Madhu Sudan, and Santhoshini Velusamy. "Streaming Algorithms via Local Algorithms for Maximum Directed Cut". In: _Proceedings of the 2025 Annual ACM-SIAM Symposium on Discrete Algorithms_. SODA 2025 (Jan. 12–15, 2025). Society for Industrial and Applied Mathematics, 2025, pp. 3392–3408. doi: `10.1137/1.9781611978322. 111`.

[STV25] Noah G. Singer, Madhur Tulsiani, and Santhoshini Velusamy. _Sketching Approximations and LP Approximations for Finite CSPs Are Related_. Sept. 23, 2025. arXiv: `2509.17926 [cs]`.

[STV26] Noah Singer, Madhur Tulsiani, and Santhoshini Velusamy. _Optimal Single-Pass Streaming Lower Bounds for Approximating CSPs_. Apr. 9, 2026. arXiv: `2604.08731 [cs]`.

[SV26a] Amatya Sharma and Santhoshini Velusamy. "Characterizing Streaming Decidability of CSPs via Non-Redundancy". In: _34th Annual European Symposium on Algorithms (ESA 2026)_. Ed. by Philip Bille, Seth Pettie, and Sabine Storandt. Vol. 388. Leibniz International Proceedings in Informatics (LIPIcs). Dagstuhl, Germany: Schloss Dagstuhl – Leibniz-Zentrum für Informatik, 2026, 131:1–131:20. isbn: 978-3-95977-445-1. doi: `10.4230/LIPIcs.ESA.2026.131`. url: `https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.131`.

[SV26b] Amatya Sharma and Santhoshini Velusamy. "Non-Redundancy of Low-Arity Symmetric Boolean CSPs". In: _CoRR_ abs/2605.14007 (2026). doi: `10.48550/ARXIV.2605.14007`. arXiv: `2605. 14007`. url: `https://doi.org/10.48550/arXiv.2605.14007`.

[Vel25] Santhoshini Velusamy. _Near-Optimal Streaming Approximation for Max-DICUT in Sublinear Space Using Two Passes_. Dec. 22, 2025. arXiv: `2512.19521 [cs]`.

[Vu24] Hoa T Vu. "Revisiting maximum satisfiability and related problems in data streams". In: _Theoretical Computer Science_ 982 (2024), p. 114271.

[Zhu20] Dmitriy Zhuk. "A proof of the CSP dichotomy conjecture". In: _Journal of the ACM (JACM)_ 67.5 (2020), pp. 1–78.

## A Literals and Non-Constant-Satisfiable CSPs

In this section, we show how our general CSPs core characterization recovers the two earlier results of Sharma and Velusamy [SV26a]. We first consider CSPs with literals and show that passing their shift/sign-closed language to the core does not change non-redundancy. We then show that a positive Boolean constraint language is a core exactly when it is not constant-satisfiable.

A _constraint language_ \(\Gamma\) is a fixed finite set of relations over the same domain. A map on the domain is an endomorphism of \(\Gamma\) if it preserves every relation in \(\Gamma\), and \(\Gamma\) is a core if every such endomorphism is an automorphism. As for one relation, we obtain core(\(\Gamma\)) by choosing an endomorphism \(\rho\) with minimum image and restricting every relation to that image.

Without loss of generality, we claim that the core reduction and the satisfiability arguments also work for a fixed finite constraint language. In the core reduction, each arriving _S_-constraint, for \(S\in\Gamma\), is replaced by the \(\rho(S)\)-constraint on the same scope. The satisfiability hard-pinning construction may similarly use constraints from any relation in \(\Gamma\). We will use this extension below without further comment.

### A.1 Literal CSPs as a special case

We first show that our general CSPs core characterization recovers the previous characterization for CSPs with literals. In the literal model, the domain is _D_=Z_<sub>q</sub>_, and every constraint may apply an arbitrary additive shift to each coordinate. For any relation \(S\subseteq D^\ell\) and any \(\lambda\in D^\ell\), write \(S^\lambda(x):=S(x+\lambda)\). Thus, for a relation \(R\subseteq D^k\), its _shift closure_ is<tbc>

\(\Gamma_R^\mathrm{lit}:=\{R^\lambda:\lambda\in D^k\}.\)

