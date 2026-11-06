set of semantic masks as test data. The diffusion models are conditioned on these masks to generate a set of 256 images, which are then segmented with the CNN.  6 reports the accuracy of these

segmentations; a higher accuracy indicates that the features better reflect the training data (real MVTec anomalies).

The throughput and latency of the three methods are compared in  7. SD has the highest computation time of the three methods.





Fig. 20. High-resolution (2048×4096) conditional generation example.

Fig. 21. High-resolution conditional generation examples. _Note that the puzzle model was trained from a single image (see Fig. 14)_

