### Exact max flow.

If we have an algorithm computing \(\epsilon\)-approximate max flow (here \(\epsilon=1/2\kappa\)), then we can use a folklore reduction to get the exact max flow: iteratively compute approximate max flows on the residual graph. In \(\widetilde{O}\left(1/\epsilon\right)\) iterations the optimal flow value of the residual graph will be decreased to 1/poly(_n_). Notice that we can also apply the standard rounding algorithm (for example, see \[Coh95, §5\]) if we want to get an integer flow of the max flow value.

The algorithm uses \(\widetilde{O}\left(\kappa\right)\) calls to the approximate max flow algorithm, which corresponds to \(\widetilde{O}\left(\kappa\right)\) calls to \(\mathcal{A},\mathcal{A}'\), and additional \(\widetilde{O}\left(\kappa\cdot\mathrm{poly}(h)\cdot\left(m+m'\right)\right)\) work and \(\widetilde{O}\left(\kappa\cdot\mathrm{poly}(h)\right)\) depth.

## Acknowledgments

AB is supported by Sloan Fellowship, Google Research Fellowship, NSF Grant 1942010, and Charles S. Baylis endowment at NYU.

HF is supported by the National Science Foundation Graduate Research Fellowship Program under Grant No. DGE2140739.

BH is partially funded by the Ministry of Education and Science of Bulgaria’s support for INSAIT as part of the Bulgarian National Roadmap for Research Infrastructure and through the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program (ERC grant agreement 949272).

GH is supported in part by National Science Foundation grant NSF CCF-2153680.

GL is supported by the National Science Foundation Graduate Research Fellowship Program under Grant No. DGE2140739.

MP is supported by grant no. 200021 204787 of the Swiss National Science Foundation.

SP is supported by NSF Grant CCF-2221980.

TS is supported by Sloan Fellowship, NSF Grant CCF-2238138, and partially funded by the Ministry of Education and Science of Bulgaria’s support for INSAIT, Sofia University "St. Kliment Ohridski" as part of the Bulgarian National Roadmap for Research Infrastructure.

## References

