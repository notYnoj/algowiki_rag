Given that test perplexity on these datasets has persisted as a standard measure of language modeling performance in the literature, we expect that differences in perplexity will broadly reflect genuine underlying differences in model capabilities.

## E.3 Dataset Size & Epochs

In reporting training dataset size, we generally record the size of pre-training datasets as well fine-tuning datasets if the model in question has been fine-tuned. The number of epochs is usually sourced from the papers which describe the language model in question, but if not provided, we estimate it via

\(\text{num\_epochs}=\frac{\text{context\_length\_tokens\cdot batch\_size\cdot training\_steps}}{\text{pretrain\_tokens}}.\)

We adjust our epoch and dataset size calculations accordingly for models like GPT-Neo and Pythia, which report the effective number of tokens seen in training.

## E.4 Parameter Size

We use the reported parameter size value if it is stated in the paper. We impute the parameter size from the previous models for papers that do not specify parameter size but follow known, state-of-the-art models. Otherwise, we rely on other papers referring to the model’s parameter size or manually compute parameters for certain RNN and LSTM models based on provided details about the model architecture (e.g. the number and size of hidden layers).

## E.5 Inclusion and exclusion criteria

We exclude several models in the dataset from the analysis based on whether they meet any of the following primary criteria: (1) use of a retrieval mechanism, (2) use of model compression or pruning, (3) use of neural architecture search, (4) use of teacher-learner or knowledge distillation mechanisms, (5) use of cache models. These models are excluded because we expect these models to exhibit significantly different scaling behaviors from other models we analyze. In particular, they can substantially change the ratio of parameters and data that would "optimally" minimize loss given some compute budget.

\begin{tabular}{cc}
Variation source & Significance \\
Training set & Early models in our dataset are often exclusively trained on the benchmark training set before evaluation, whereas later models are generally pretrained on a larger pretraining dataset. Since the majority of our dataset involves the latter type of model, we expect this effect to be minor. The direction of this effect is somewhat ambiguous: the training set data is likely ‘closer’ to the test distribution relative to other internet text-corpuses, so not training on the relevant training distribution could yield lower performance at fixed budgets. \\
 & A further subtlety is that large text corpuses often, but not always, contain Wikipedia data. Pretraining on such distributions could yield larger gains than otherwise, which could be attributed to algorithmic progress. A small number of existing results illustrate this effect. For example, in a 1.3B GPT-3 reimplementation, including Wikipedia and other high-quality data in fixed-size pretraining reduced WikiText perplexity from 8.27 to 5.59 (Gao, Biderman, et al. 2020,  3). In our dataset, this effect is likely to show up as a small number of models receiving worse-than-otherwise perplexities in WikiText, around the time of the transition to large-scale pretraining but before inclusion of Wikipedia data became common. This is true of GPT-2, for example. \\
Word vs sub-word tokenization & Changing to a sub-word vocabulary can reduce perplexity substantially in an otherwise unchanged architecture, for example by ∼30% in a pre-GPT-2 LSTM (C. Wang, M. Li, and Smola 2019). In our dataset this is likely to show up as a one-time change, potentially exaggerating the algorithmic improvement in language models around GPT onwards. \\
Preprocessing and runtime adaptation & Different preprocessing of data can affect results significantly. For example, inverting word-level tokenization artifacts in WikiText-103 improved perplexity by ∼10% (Radford et al. 2019). Runtime adaptation sometimes has similarly large effects (Alon et al. 2022). We expect that these sources of variation mostly act as noise in our dataset, although if these improved over time, they might inflate estimates of algorithmic efficiency. \\
Stride length & The move to larger models led to evaluations using larger stride for lower computational cost. This can increase perplexity, but only on the order of ∼10% at realistic settings (Hugging Face 2023). We believe this should act as another source of variation, but without a strong influence on our overall findings. \\
\end{tabular}

4: Sources of variation and their significance in language modelling evaluations.

