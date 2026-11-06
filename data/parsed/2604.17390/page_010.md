<tbc>MESA is particularly suitable when the damaged inscription is part of a larger text containing intact regions that can serve as exemplars, or when a dataset of inscriptions in the same or a similar style is available. In contrast, Deep Image Prior is more appropriate when only a single inscription image is available and its intact regions are insufficient to provide effective data for our multi-exemplar strategy.

By comparison, DRUNET, DnCNN, and ESRGAN require either (i) a real-world dataset with images before and after damage--which is rarely available for ancient inscriptions--or (ii) a synthetic dataset capable of accurately reproducing, on other well-preserved inscriptions, the type of damage present in the degraded input. Moreover, each of these methods is better suited to specific types of degradation. DRUNET is more effective for human- induced damage such as scratches, which are common on ancient inscriptions, whereas DnCNN is best suited for reducing noise caused by environmental factors. ESRGAN, originally designed for image super-resolution, is preferable when high-resolution restoration is required in ruined regions. Nonetheless, our experiments show that ESRGAN performs comparably well even when the output resolution is constrained to match that of the input image.

1 summarizes the training strategy for each method along with a brief description.







(a) Dataset A

(b) Dataset B

(c) Dataset C

Fig. 5. Tesseract [19] letter widths detection. Each rectangle captures some letters and we divide each width by the number of letters detected within it to define an average width of letters inside it.

