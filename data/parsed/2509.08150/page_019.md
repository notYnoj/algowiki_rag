Although we assumed a simplified, exhaustive (_O(n_<sup>2</sup>)) comparison scenario, this speedup is significant in practice. Fig.6 demonstrates the empirical speedup due to kv-cache. RadixAttention in SGLang is particularly helpful for VAs whose queries share large prefixes.

## G Additional Results

The rest of the pages contain additional tables and figures.

Amazon Reviews, kwicksort-nocache
0.35
better
kwick
kwicksort_nocache
4
32
0.30
4
32
0.25
0.20
kendall tau
0.15
0.10
0.05
1.7
0.00
1.7
101
102

Figure 6: The speed-accuracy pareto front (log_x_-axis: the runtime per query, _y_-axis: kendall-\(\tau\) score) of sorting tasks over various Qwen3 model sizes (1.7B, 4B, 32B), comparing the effect of kv-cache reuse in KwickSort (with symmetrization, \(\theta=16\)). Disabling kv-cache reuse causes a significant runtime increase.

