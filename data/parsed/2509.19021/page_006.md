## 5.2 Theoretical Analysis and Performance Prediction

Modelling the theoretical operational cost on a large input with skewed data:

### Parameters:

- _n_ (input size): 10<sup>6</sup> (1,000,000)<tbc>

- _k_ (maximum value): \(9\times 10^{18}\) (the approximate max value for a 64-bit integer)<tbc>

**-** Assuming 1% distribution of elements among each log group after the first log group.

For these parameters, the number of rounds required is _R_=4, calculated from \(\lfloor log_{10^6}(10^{18})\rfloor+1=4\). We assume a skewed dataset where maximum of 97% of the elements are lesser than _n_, giving a partition proportion _p_=0.97, which is the best case for our partitioning logic (assuming 1% of input size in each log distribution).

#### Cost of Comparison-Based Sort (`Introsort`):

The lower bound for comparison- based sorting is \(T_\mathrm{comp}=\Omega(n\mathrm{log}n)\), calculating on which gives us the following number of operations:

\(T_\mathrm{comp}\approx n\mathrm{log}_2n=10^6\times log_2(10^6)\approx 10^6\times 19.93=19,930,000\text{operations}.\)

#### Cost of BNRS:

The cost is fixed, as the algorithm processes all _n_ elements in each of _R_ rounds.

\(T_\mathrm{BNRS}=R\times n=4\times 10^6=4\times 1,000,000=4,000,000\text{operations}.\)

#### Cost of SP-LSD:

Total cost of operation assuming skewed distribution case

\(T_{\mathrm{SP}\mathrm{-LSD}}=\underbrace{1,000,000}_{\mathrm{Round}1(\mathrm{Sort})}+\underbrace{(1,030,000+60,000)}_{\mathrm{Rounds}2-3(\mathrm{Partition+Sort})}+\underbrace{30,000}_{\mathrm{Round}4(\mathrm{Sort})}\)<br>
\(=2,120,000\text{operations}.\)

This analysis demonstrates that the BNRS to be theoretically five times faster than an optimal comparison-based sort and the SP-LSD optimization then further provides a two times improvement over BNRS. The cumulative effect is a predicted ten times performance advantage for SP-LSD over standard comparison-based sorting.

## 5.3 Round Feasibility Crossover

The efficacy of SP-LSD is not uniform across execution; it is architecturally confined to the intermediate rounds. By analyzing the execution stages and theoretical modelling, we observe that:

**-** **Stage 1 (Initialization):** Incurs a fixed cost (\(\alpha N\)) identical to BNRS. No pruning is possible here as the full dataset must be read to establish the first digit’s order.

