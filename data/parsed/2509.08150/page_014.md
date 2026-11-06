## Appendix

## A (_n,k_)-Verbalized Algorithms

A verbalized algorithm that utilizes the PL reward model of an LLM by using it as a _k_-categorical oracle is called a (_n,k_)-_Verbalized Algorithm_. For brevity, we may refer to (_n,k_)-VAs as just _k_-VAs.

**Definition 2** ((_n,k_)-Verbalized Algorithms)**.** _Let_ \(A[\tau]\) _be an algorithm that solves_ \(T[\tau]\) _with an n-arg boolean oracle_ \(f[\tau]:\tau,\cdots,\tau\rightarrow 1..k\)_. A_ (_n,k_)-Verbalized Algorithm _instantiates f_\[str\] _as a multiple- choice-question (MCQ) query to an LLM._

### Symmetrization for (_n,k_)-VAs

Let \(\sigma\) be a permutation of _n_ inputs. An _n_-ary function _f_ is _permutation- invariant_ if \(\forall\sigma;f(\sigma(x))=f(x)\), and _permutation-equivariant_ if \(\forall\sigma;f(\sigma(x))=\sigma(f(x))\). For permutation- invariant oracles in (_n,k_)-VAs, we query them with _S_ shuffled inputs (hyperparameter \(S\le n!\)) presenting the arguments in a different order in the context, then average the output probability over the orderings. For permutation-equivariant oracles, the probability must be added toward the original element before the shuffling.

## B Sorting Dataset and Prompt Details

This section summarizes the dataset used for evaluating the sorting task. All verbalized sorting algorithms use the same query for the same dataset. Let `comparison\_prompt` be a comparison query prompt, specific to each dataset, listed in the following sections. When comparing strings `X` and `Y`, we query the LLM the following prompt, using the f-string notation in Python programming language:

`verbalized\_prompt = f"{comparison\_prompt}}nX:{X}}nY:{Y}"`

To guarantee that all baseline approaches (constraint-decoding baseline, autoregressive constraint-decoding baseline, I.i.d. scoring, autoregressive scoring) receive the same information as the verbalized sorting, we construct the prompts for these baselines from the same comparison query prompt used for verbalized sorting. Let `strings` be a list of strings to sort. For constraint-decoding baseline, we query the LLM as follows, with outputs constrained to string representations of numbers from 0 to |`strings`|:

`constraint\_decoding\_baseline\_prompt = (`

`f"Sort the following list in the increasing order of quality " +`

`f"that is compared in the following comparison criteria: ’{comparison\_prompt}’. " +`

`f"That is, for a pair X and Y, if the answer to the criteria is ’yes’, " +`

`f"X must appear after Y in the output list. " +`

`f"The elements in the list are numbered. " +`

`f"Answer the order using a comma-separated list of the numbers.\\n" +`

`"\\n".join([f"{i}: {s}" for i, s in enumerate(strings)])`

`)`

For scoring-based baseline, we query the LLM with output constrained to a regular expression `"[1-4]\\.[0-9]"` as follows:

`scoring\_prompt = (`

`"I want to sort several strings. " +`

`"Given two strings X and Y, " +`

`"my comparison criteria is as follows: ’" + comparison\_prompt + "’. " +`

`"Assign a score to X below so that for any pair of strings X and Y, " +`

`"if the answer to the comparison criteria above is yes, " +`

`"the score of X is greater than the score of Y. " +`

`"Each score must be between 1 and 5 with one decimal place, " +`

`"where the score 5 means that X will most certainly satisfy the comparison against other strings, " +`

`"and the score 1 means the opposite. " +`

`"For example, if we compare the height of mountains, score 5 will be assigned to the tallest mountains, " +`

`"and if we compare the quality of restaurants, score 1 implies that the food or the service is very bad. " +`

`"\\n" +`

`"X: " + X + "\\n"`

`)`

