### A.1 Part Removal and Duplication

Because PointGT decouples geometry and appearance through a canonical UV mapping, it also supports editing operations that change the object’s topology, while keeping the edited texture correctly attached to the modified geometry. We demonstrate this on the Blossom scene with two operations. Figure 10 shows _part removal_: petals are sequentially detached from the flower (top to bottom). The learned UV mapping (left, visualized as a checkerboard with one color per chart) and the rendered result together with its 2D texture map (right) stay consistent throughout; since appearance is decoupled, the geometry can be retextured at the same time, and we switch the applied texture across the sequence. Figure 11 shows _part duplication_, where the duplicated geometry is rendered under two different texture edits, with the texture remaining correctly mapped onto the duplicated parts through the canonical UV mapping.

UV mapping
Rendering and texture map
Step 1
Step 2
Step 3

**Fig.10: Part removal** on the Blossom scene. From top to bottom, petals are sequentially removed. _UV mapping_: checkerboard visualization of the learned charts on the deforming geometry. _Rendering and texture map_: the rendered result (left) and its 2D texture map (right); the applied texture is switched across the sequence to show that the remaining geometry stays editable.

