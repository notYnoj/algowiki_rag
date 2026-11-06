In this paper, we extend the work introduced in [13] by enabling the regeneration of any texture included in the training set, as well as seamless grafting between any pair of textures the automaton was trained on. These capabilities are made possible by the genomic information encoded within the cells of the NCA.

## 2. MATERIALS AND METHODS

### 2.1. Previous work

The fundamental architecture of the NCA employed for texture synthesis is extensively detailed in [13] and will thus be concisely reviewed herein for contextual clarity. The textures used for training and inference are selected from the Describable Textures Dataset [14], as well as from the Vis-Tex database [15].

The NCA corresponding to an image or texture is defined on a two-dimensional grid, where each cell represents a single pixel. The automaton introduced in [13] consists of an input grid, a perception stage, and an update stage. The perception stage comprises four fixed filters: a horizontal Sobel filter, a vertical Sobel filter, a Laplacian filter, and a 3 × 3 identity filter. These filters are applied to the input to extract local features, such as edges and gradients, which are important for capturing texture characteristics. The output of this filtering stage is a multi-channel feature map in which the responses of all filters applied to the multi-channel input are stacked.This is followed by two convolutional layers that learn the update rule and perform the state update.

The convolutional layers employ 1 × 1 kernels in order to faithfully model the local behavior of an NCA rule, where the state of each cell is influenced only by its immediate neighbors through the perception features. Specifically, the first convolutional layer processes the aggregated perception features, followed by a ReLU activation function. The second convolutional layer then outputs the proposed change for each cell’s state. The number of filters nf in these convolutional<tbc>

<tbc>layers determines the dimensionality of the hidden state and the complexity of the learned update rule. A schematic representation of a single evolution step of the NCA is shown in Fig. 1.

Each cell of the automaton is an _n_-dimensional vector, in which the first 3 channels correspond to the RGB color of the associated pixel, the last _ng_ channels encode the genome, and the remaining _n −ng −_3 channels are hidden channels used exclusively during training. The number of genome channels is determined by the number of textures used for training, which is chosen to be a power of 2. Specifically, an NCA with _ng_ genome channels can generate 2_ng_ distinct textures.

The training of the NCA is performed as follows. All channels of all cells in the initial NCA grid are initialized to 0, except for the genome channels, which are initialized according to the genome of the target texture. For example, considering 8 textures, as shown in Fig. 2, the number of genome channels is 3, and each texture is assigned a genome given by the binary representation of its texture index.

At each evolution step, the perception stage convolves the input grid with each of the 4 fixed filters and concatenates the resulting feature maps for each cell. These perception values form the input to the convolutional layers, which implement<tbc>

Input
Filtering
NN for the Update rule
Output
Laplace pass output
Sobel, pass output
Srochastic update
Sobel, pass output
Identity pass output
ReLU
Conv2d
P2AucC
NCA at timestamp t
n filters 1 x 1
ns filters 1 x 1
NCA at timestamp t + 1

(0,0,0)
(0,0,1)
(0,1,0)
(0,1,1)
(1,0,0)
(1,0,1)
(1,1,0)
(1,1,1)

**Fig. 1**. Schematic of a single NCA evolution step from timestamp _t_ to _t_ + 1.

**Fig. 2**. Example of textures for the training of the automaton. On top of each texture is the corresponding genome.

