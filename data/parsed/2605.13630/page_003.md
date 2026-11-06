<tbc>the learned update rule of the automaton. After a number of evolution steps, the loss is computed using a pretrained VGG discriminator together with a Sliced Wasserstein Loss (SWL) [16]. The learnable weights of the network are then updated via backpropagation.

The base training strategy relies on a pool of seeds and intermediate states corresponding to the different textures in the training set. At each training epoch, a random batch is sampled from this pool and passed through the automaton. To stabilize training and prevent texture degradation during long NCA evolution sequences, the lowest-scoring batch sample associated with a given texture is replaced by the seed state of that texture at each epoch. This replacement is performed in a cyclical manner across textures, following the strategy described in [13].

## 2.2. Regeneration of a damaged texture

In order to enable the NCA to regenerate a partially obscured or corrupted texture (a damaged texture), several modifications to the base training procedure are required. A damaged texture refers to an input where certain regions are missing, occluded, or contain noise, and the NCA’s task is to infer and reconstruct the original, complete texture based on the intact surrounding information. In the following, we describe the necessary changes introduced for this texture regeneration process.

It is worth noting that no adaptation of the training strategy is required for a single-texture automaton, as the pooling strategy inherently enables regeneration and stabilization of the pattern shortly after it is damaged. However, for an NCA trained for multi-texture synthesis, additional alterations to the training procedure are necessary to ensure correct texture regeneration. Without these modifications, when a damaged input is propagated through the NCA, the automaton tends to generate patches corresponding to different textures rather than regenerating the target texture.

To achieve the desired behavior, several adjustments to the original algorithm are introduced. Inspired by the approach in [17] and building upon the pooling strategy proposed in [13], we modify the batch sampling process from the pool as follows: in addition to replacing a high-scoring state (in terms of loss), we also damage the two lowest-scoring states. Here, damaging refers to randomizing the state vectors of cells contained within a circular region of radius 15 to 25 pixels.

The adapted training procedure is summarized in Algorithm 1, which presents a modified version of the pooling algorithm introduced in [13]. The optimal adapted training strategy for multi-texture generation relies on a pool with seeds that are equally divided among the textures. This pool is initialized in line 1 of Algorithm 1, based on the _pool\_size_ parameter. The seed of a texture consists of all cells initialized, as described previously, with 0 in all channels except for the genome channels, which are initialized with the bi-<tbc>

<tbc>**Algorithm 1** Regeneration-adapted training for multi-texture architecture

**Require:** The _pool\_size_ of _nca_ states, the _number\_of\_epochs_, the _batch\_size_. **Ensure:** The trained _nca_, the final pool. 1: \(pool\leftarrow init\text{\_pool}(pool\text{\_}size)\) 2: \(nca\leftarrow init\text{\_}nca\text{\_}params()\) 3: **for** \(iteration\in range(0,number\text{\_}of\text{\_}epochs)\) **do** 4: \(batch\leftarrow\) random pick _batch\_size_ elements from _pool_ 5: \(\triangleright\) states and corresponding genome indices 6: \(gr\leftarrow iteration\%n\text{\_}genomes\) 7: **if** exists _gr<sub>r</sub>_ genome in _batch_ **then** 8: \(worst_gr\leftarrow highest\text{\_}loss\text{\_}state\text{\_}of\text{\_}genome(batch,gr)\) 9: **else** 10: \(worst_gr\leftarrow highest\text{\_}los\text{\_}state(batch)\) 11: \(ig\leftarrow index\text{\_}of\text{\_}element\text{\_}with\text{\_}highest\text{\_}loss(batch)\) 12: **end if** 13: \(batch[worst_gr].x\leftarrow seed\text{\_}of\text{\_}genome(h,w,gr)\) 14: \(x_1,x_2\leftarrow lowest\text{\_}2\text{\_}losses(batch)\) 15: \(damage\text{\_}texture\text{\_}from\text{\_}batch(batch[x_1])\) 16: \(damage\text{\_}texture\text{\_}from\text{\_}batch(batch[x_2])\) 17: \(num\text{\_}steps\leftarrow random(64,90)\) 18: **for** \(i\in range(0,num\text{\_}steps)\) **do** 19: \(batch.x\leftarrow nca(batch.x)\) 20: **end for** 21: \(loss\leftarrow compute\text{\_}loss(batch.x,target\text{\_}images(batch.y))\) 22: apply _nca_ weights backpropagation 23: \(pool\leftarrow\) put updated individuals of _batch_ back in the pool 24: **end for** 25: **return** _nca_

nary representation of the index of the corresponding texture. After initializing the NCA parameters (line 2), the training process is started by the _for-loop_ in line 3.

For each training iteration, a batch of samples is selected from the pool (line 4), and a genome index _gr<sub>r</sub>_ is considered (line 5). During batch selection, the highest-scoring sample in the pool corresponding to genome _gr<sub>r</sub>_ (selected in line 6) is replaced (lines 7-13) with a seed having the same initial genome coding. As can be observed from line 6, genome replacements are cycled across iterations. This strategy prevents samples corresponding to more difficult textures from being replaced more frequently than others.

In lines 14-16, the two lowest-scoring samples from the batch are damaged.

The NCA is then evolved for a random number of steps (lines 17-20), the loss is computed (line 21), and backpropagation is performed to adjust the weights of the learnable convolutional layers (line 22). Finally, the pool is updated with the new individuals (line 23).

When the NCA is trained according to Algorithm 1, it can be used for inference on damaged textures of the same type as those included in the training set.

## 2.3. Grafting

An important extension of our NCA is the ability to perform texture grafting between textures drawn from the training set. Grafting refers to the process of joining two organisms so that<tbc>

