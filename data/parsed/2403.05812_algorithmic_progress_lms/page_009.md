<tbc>with the increased emphasis on scaling large language models over the last few years, particularly since the introduction of GPT-2 in 2019 (Radford et al. 2019), relative to fundamental algorithmic or architectural changes.<sup>6</sup>Figure 5 illustrates a stylized version of this perspective, depicting a sharp increase in physical compute scaling around 2018-2019, followed by a return to previous compute scaling growth rates.

There are other potential explanations - for example, it is possible that the transformer architecture was a pivotal innovation (see section 3.3), and subsequent algorithmic advances have been less significant in comparison. Alternatively, this observation could also be explained by a secular decline in the rate of algorithmic innovation. However, we find these two explanations less compelling than the results of Figure 4, where the rate of algorithmic progress does not clearly decrease after the release of the transformer (e.g. with a 2018 cutoff). If anything, the rate _increases_ slightly, contrary to what both of these explanations predict.

## 3.3 The significance of the transformer architecture

Since its introduction in 2017 (Vaswani et al. 2017), the transformer architecture has become the dominant algorithmic architecture in language modeling, forming the base of multiple notable systems. The transformer has also been widely adopted in vision models, and there is a rich existing literature that has evaluated the merits of the transformer architecture against other architectures in vision.

We attempt to quantify the contribution of the transformer architecture in terms of the "compute-equivalent gain" over other architectures in our dataset (LSTMs, RNNs, state space models, among others). This is akin to the approach outlined in Davidson et al. 2023--in this context, the compute-equivalent gain is the amount by which training compute must be scaled to improve benchmark performance as the same amount as the introduction of the transformer. For example, Hernandez and T. Brown 2020 find that a transformer (2017) achieves the same performance as a Seq2Seq (2014) model on the WMT-14-EN-FR benchmark, with \(61\times\) less compute.

To capture the improvement represented by the transformer, we modify our core model as follows:

\(L=\left\{\begin{array}{ c c }
\sigma(\gamma_T)\left(\frac{A}{N_\mathrm{eff}^{\alpha_\mathrm{year}}}+\frac{B}{D_\mathrm{eff}^{\beta_\mathrm{data}}}\right), & \text{if transformer}, \\
\frac{A}{N_\mathrm{eff}^{\alpha_\mathrm{year}}}+\frac{B}{D_\mathrm{eff}^{\beta_\mathrm{data}}}, & \text{otherwise}.
\end{array}\right.\) (7)

where \(\sigma:\mathbb{R}\rightarrow(0,1)\) is the sigmoid function, given by \(\sigma(x)=1/(1+e^{-x})\). \(\gamma_T\) is a constant and all other terms have the same meaning as in the original model.<sup>7</sup> The key intuition is that the transformer could enable us to use compute (or perhaps data) more efficiently than the architectures that precede it.

<sup>6</sup>We can provide further support for this interpretation by considering the average growth in compute between pairs of systems in  1. This turns out to be higher for later pairs of systems that we consider: e.g. between the Transformer and GPT-3 there was an average annual growth rate of 9%, compared to an average growth rate of 2% between the 2012 RNN and GPT-2. <sup>7</sup>The sigmoid is introduced to make it easier to fit the model by improving optimizer stability.

\begin{tabular}{ccccc}
 & Parameter & Data & Parameter & Data \\
 & scaling & scaling & efficiency & efficiency \\
RNN (2012) \(\rightarrow\) LSTM (2016) & 12.7% & 46.5% & 4.9% & 35.9% \\
RNN (2012) \(\rightarrow\) Transformer (2018) & 40.8% & 26.3% & 3.7% & 29.2% \\
RNN (2012) \(\rightarrow\) GPT-2 (2019) & 42.9% & 32.5% & 2.8% & 21.8% \\
RNN (2012) \(\rightarrow\) GPT-3 (2021) & 48.6% & 32.4% & 2.1% & 16.8% \\
RNN (2012) \(\rightarrow\) Gopher (2021) & 48.4% & 29.8% & 2.5% & 19.3% \\
LSTM (2016) \(\rightarrow\) Transformer (2018) & 79.3% & 0.0% & 2.7% & 18.1% \\
LSTM (2016) \(\rightarrow\) GPT-2 (2019) & 65.8% & 21.2% & 1.7% & 11.3% \\
LSTM (2016) \(\rightarrow\) GPT-3 (2021) & 64.1% & 25.2% & 1.4% & 9.3% \\
LSTM (2016) \(\rightarrow\) Gopher (2021) & 63.2% & 22.3% & 1.9% & 12.6% \\
Transformer (2018) \(\rightarrow\) GPT-2 (2019) & 48.7% & 46.3% & 0.6% & 4.3% \\
Transformer (2018) \(\rightarrow\) GPT-3 (2021) & 56.8% & 35.9% & 0.8% & 6.4% \\
Transformer (2018) \(\rightarrow\) Gopher (2021) & 56.1% & 31.1% & 1.5% & 11.3% \\
\end{tabular}

1: Attribution of progress to pre-training algorithmic progress and compute scaling between model pairs based on Shapley decomposition in linear space. Numbers may not all add up to 100% due to rounding. The Transformer here is by Baevski and Auli 2018 (the earliest decoder-only transformer we have in our dataset), who modify the original transformer architecture by Vaswani et al. 2017 to be decoder-only.

