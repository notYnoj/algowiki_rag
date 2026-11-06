## A Tightened Boundary Analysis

In this Appendix, we provide the complete analysis of directional mergesort<sup>++</sup>.

### A.1 Directional Merging Savings

This subsection analyzes the correctness of the directional merge for all possible run configurations in directional mergesort<sup>+1</sup>, managed by the _backward condition_ on line 15 of Algorithm 2. As directional merge savings only apply to boundary nodes where the run contains an entire half and extends into the opposite half (Subcase B), we will only consider such situations. We otherwise count no directional merging savings and any merge direction is valid. We begin by considering non-decreasing runs relative to a boundary node _v_ with left child _L_ and right child _R_:

• **Case i (Prefix):** A non-decreasing run fully contains _L_ so _a_<sub>1</sub>=`true`. As the end of the non-decreasing run is in _R_, it cannot be pure non-decreasing (as the end of a non- decreasing run is decreasing) hence _b_<sub>1</sub>=`false`. Then, the backward condition evaluates to \(b_1\vee\neg(b_2\vee a_1)=\mathtt{false}\vee\neg(b_2\vee\mathtt{true})=\mathtt{false}\), so the algorithm chooses MergeFw.<tbc>

• **Case ii (Suffix):** The run fully contains _R_, and extends leftwards into _L_. Then _b_<sub>1</sub>=`true`, ensuring the backward condition evaluates to `true`. The algorithm calls MergeBw.

As discussed in Section 2, these are the correct merge directions that generate directional merging savings for non-decreasing runs. We apply a mirrored argument for strictly decreasing runs:

• **Case i (Prefix):** The decreasing run fully contains _L_ (_a_<sub>2</sub>=`true`) and extends rightwards into _R_, so _b_<sub>2</sub>=`false` (as _R_ contains the end of a decreasing run which is non-decreasing). The analysis splits into two further cases:

- **Subcase X (**|_L|\>_1**):** As a sequence strictly longer than 1 element cannot be both non- decreasing and decreasing simultaneously, _a_<sub>2</sub>=`true` implies _a_<sub>1</sub>=`false`. Hence, the backward condition evaluates to \(b_1\vee\neg(b_2\vee a_1)=b_1\vee\neg(\mathtt{false}\vee\mathtt{false})=b_1\vee\mathtt{true}=\mathtt{true}\) so the algorithm chooses MergeBw. The merge then exhausts all elements in _L_ before selecting any run elements from _R_ (as established in Section 4.1).<tbc>

**-** **Subcase Y (**|_L_|=1**):** Merging occurs only when |_R_|=2 (and _m_=|_L_|+|_R_|=3), as |_R_|=1 is handled by base cases. We are interested only when the decreasing prefix has size 2, spanning 1 element in _L_ and 1 in _R_ (\(k_1>k_2\le k_3\)) as a 1-element run falls under Subcase C and a 3-element run bypasses the merge entirely. Because |_L_|=1, the base case returns _a_<sub>1</sub>=`true` and the backward condition \(b_1\vee\neg(b_2\vee a_1)\) simplifies to _b_<sub>1</sub>, leaving the merge direction unknown. Nevertheless, merging _m_=3 elements requires at most _m_-1=2 comparisons regardless of whether MergeBw or MergeFw is called. The worst-case analysis of Lemma 16 charges at least 2 comparisons in this scenario: 1 to the run containing _k_<sub>1</sub>_k_<sub>2</sub> in Subcase B (or 2 at upper levels) and 1 to _k_<sub>3</sub> in Subcase A (or upper levels); the upper bound remains valid regardless of merge direction.<tbc>

• **Case ii (Suffix):** The decreasing run fully contains _R_ (_b_<sub>2</sub>=`true`) and extends leftwards into _L_. Because \(r-\ell\le 2\) is handled by base cases, we deduce \(r-\ell\ge 3\), and \(|R|=\lceil(r-\ell)/2\rceil\ge 2\) according to the index partitioning logic of the algorithm. Because a sequence of size 2 or greater cannot be both non-decreasing and decreasing simultaneously, _b_<sub>2</sub>=`true` implies _b_<sub>1</sub>=`false`. The backward condition then evaluates to \(b_1\vee\neg(b_2\vee a_1)=\mathtt{false}\vee\neg(\mathtt{true}\vee a_1)=\mathtt{false}\), thus the else branch executes correctly utilizing MergeFw to exhaust _R_ first.

Hence, the directional merging logic of Algorithm 2 successfully captures directional savings for decreasing runs where applicable, ensuring the comparison charging (in Lemma 16) remains valid.<tbc>

