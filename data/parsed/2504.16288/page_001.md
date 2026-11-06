Linear Time Subsequence and Supersequence Regex Matching

**Abstract**

It is well-known that checking whether a given string _w_ matches a given regular expression _r_ can be done in quadratic time \(O(|w|\cdot|r|)\) and that this cannot be improved to a truly subquadratic running time of \(O((|w|\cdot|r|)^{1-\epsilon})\) assuming the strong exponential time hypothesis (SETH). We study the related problem that asks whether _w_ has a _subsequence_ that matches _r_, and we show that surprisingly this task admits an algorithm that runs in linear time, i.e., in _O_(|_w_|+|_r_|). We further show that the same holds if we ask for a supersequence instead of a subsequence. Moreover, we show that the _quantitative_ problems of computing a longest subsequence or shortest supersequence of _w_ that matches _r_ can be solved with the same complexity as the classical longest common subsequence or shortest common supersequence problems, i.e., in \(O(|w|\cdot|r|)\), and conditionally not in \(O((|w|\cdot|r|)^{1-\epsilon})\).

By contrast, if instead of subsequences or supersequences we consider other string relations like the infix, prefix, left-extension, or extension relations, then all the corresponding problems (both quantitative and non-quantitative) have the same complexity as classical regex matching, i.e., they can also be solved in \(O(|w|\cdot|r|)\), but not in \(O((|w|\cdot|r|)^{1-\epsilon})\) assuming SETH.

We last study the complexity of the _universal_ problem that asks if _all_ subsequences (or supersequences, infixes, prefixes, left-extensions or extensions) of an input string satisfy a given regular expression. For these problems, we show polynomial upper bounds (along with matching conditional lower bounds) for the infix and prefix relations, but PSPACE-completeness for the extension, left-extension and supersequence relations, and coNP-completeness for the subsequence relation.

## 1 Introduction

Regular expressions (also called regex) were first introduced by Kleene in 1956 [Kle56] as a theoretical concept and quickly found their way into practice with the classical construction by Thompson [Tho68]. Nowadays, they are a standard tool for text processing and data retrieval tasks, and they constitute computational primitives in virtually all modern programming languages (see the

Antoine Amarilli<sup>1</sup>, Bartłomiej Dudek<sup>2</sup>, Florin Manea<sup>3</sup>, Tina Ringleb<sup>3</sup>, and Markus L. Schmid<sup>4</sup>

<sup>1</sup>Univ. Lille, Inria, CNRS, Centrale Lille, UMR 9189 CRIStAL, F-59000 Lille, France, `a3nm@a3nm.net`

<sup>2</sup>University of Wrocław, Institute of Computer Science, Joliot-Curie 15, PL-50-383 Wrocław, Poland, `bartlomiej.dudek@cs.uni.wroc.pl`

<sup>3</sup>University of Göttingen, Institute for Computer Science and CIDAS, D-37077 Göttingen, Germany, `{florin.manea, tina.ringleb}@cs.uni-goettingen.de`

<sup>4</sup>Humboldt-Universität zu Berlin, Unter den Linden 6, D-10099, Berlin, Germany, `MLSchmid@MLSchmid.de`

June 15, 2026

arXiv:2504.1628v3 [cs.DS] 12 Jun 2026

