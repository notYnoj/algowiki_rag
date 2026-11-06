# Surprise-Guided MergeSort

<tbc>SGS achieves the best average \(\tau\times 100\) while adding up to a 47% edge multiplier; controlled diagnostics show that these inferred edges are useful but imperfect, and that the method degrades toward warm-started Active Elo when the VLM prior is globally unreliable.

The empirical picture is domain-dependent: SGS is strongest when VLM pre-ordering is directionally informative, especially for perceptual IQA, while graph-based methods remain preferable on some semantic-similarity tasks. Future work should replace the binary agreement gate with soft or per-round fallback, learn surprise weights from calibration data, and validate the method with real annotators.

#### Acknowledgments

This work was supported by the National Research Foundation of Korea (NRF) grants funded by the Ministry of Science and ICT (MSIT) (RS-2024-00338048, RS-2024-00455720, RS-2026-25487796); a grant of the Korea Health Technology R&D Project through the Korea Health Industry Development Institute (KHIDI), funded by the Ministry of Health & Welfare (RS-2025-02220534); the Technology Innovation Program (or Industrial Strategic Technology Development Program - Biotechnology) (RS-2025-13002970) funded by the Ministry of Trade Industry & Energy (MOTIE, Korea); the National Institute of Health (NIH) research project (2026-ER0901-00, 2026-ER0904-00); the Advanced GPU Utilization Support Program and the High-Performance Computing Support project (RQT-25-070083), both funded by MSIT; Hankuk University of Foreign Studies Research Fund of 2026; the Culture, Sports and Tourism R&D Program through KOCCA funded by MCST (RS-2024-00332210); the Artificial Intelligence Graduate School Program, Hanyang University (RS- 2020-II201373); the AI Seoul Tech Research Support Program of the Seoul Future Foundation; and the Artificial Intelligence Semiconductor Support Program (IITP-2025-RS-2023-00253914), supervised by IITP and funded by the Korean government.

### References

