<tbc>content observed by distant cameras, the grid resolution is too coarse for nearby cameras. This limitation results in a degradation of both rendering quality and efficiency.

**Physical-based Rendering or Fluids.** Our method does not model fine-grained lighting effects such as shadowing and specular reflection of a certain lighting environment, which can be improved by introducing material and lighting estimation in future works. Due to the reliance on the mesh scaffold, we cannot represent objects that fail during reconstruction (e.g., smoke or liquid).

## 6 CONCLUSION

We have proposed a novel and versatile mesh-based neural representation, which achieves high-fidelity and efficient volume rendering and flexible geometry and texture editing that is fully compatible with a mesh-based workflow, and also supports convenient semantic-guided editing. Specifically, we encode the neural radiance field into a mesh scaffold, where each mesh vertex maintains learnable geometry, texture, semantic code and modification color value for its neighboring local space.

## ACKNOWLEDGMENT

This work was supported by NSF of China (No. 62441222), Key R&D Program of Zhejiang Province (No. 2023C01039), Ant Group.

## REFERENCES

