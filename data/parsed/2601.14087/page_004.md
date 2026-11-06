<tbc>The switching power of the transmission registers is extracted as a proxy for link power, referred to as link-related power. As shown in Fig. 7, ACC-PSU reduces link-related power by 18.27% and link BT by 20.42%, while APP-PSU achieves 16.48% and 19.50%, respectively.

Although APP-PSU yields slightly smaller power savings than ACC-PSU, its power overhead is only 1.43 mW compared to ACC-PSU’s 2.28 mW, corresponding to a 37.3% reduction.

### C. Discussion and limitation

**1. BT Reduction Effectiveness** Our proposed APP-PSU achieves a 19.50% BT reduction in links compared with the non-optimized baseline, retaining 95.5% of the 20.42% BT reduction provided by ACC-PSU.

**2. Hardware Efficiency of APP-PSU** APP-PSU reduces link-related power by 16.48%, corresponding to 90.2% of the link-power savings achieved by ACC-PSU. At the same time, it lowers area overhead by 35.4% and power overhead by 37.3%, resulting in a substantially lower hardware cost.

**3. End-to-end power and hop count** Our simplified platform uses only single-hop traversal for each packet, achieving a 16.48% link-power reduction with a 1.43 mW overhead. Our methods should achieve scalably greater savings with more hops in a full-scale accelerator with longer, multi-hop interconnects, as BT reduction benefits accumulate at each router-to-router transmission. Since this study focuses on the sorting unit, the platform serves as an illustrative example.

**4. Limitation** As future work, we plan to extend the analysis from a single convolution layer to more complex neural networks, such as ResNets and Transformers and to evaluate BT reduction and power saving over multi-hop paths within an accelerator platform with a detailed NoC implementation.

## V. CONCLUSION

We present the hardware implementation of a popcount sorting unit for partial LeNet. By introducing approximate computing to simplify logic, both area and power are reduced. Post-layout analysis in 22 nm technology demonstrates that our APP-PSU achieves 35.4% area reduction and 37.3% power reduction compared to the accurate baseline, while maintaining 95.5% BT reduction efficiency (19.5% vs 20.4%). Post- layout power analysis with back-annotated switching activity confirms 16.48% link-related power savings and 4.58% PE power reduction. Future work will scale to larger models (e.g., ResNets, Transformers) and integrate our method into complete NoC-based platforms to quantify end-to-end benefits<tbc>

## REFERENCES

