<tbc>ures in texture and pose reconstruction when G<sub>CNN</sub> is omitted.

**Two-Stage Fusion Network (**G<sub>**fuse**</sub>**)** This network fuses local view-dependent features with global contextual information in a two-stage MLP process. Removing this fusion step and directly feeding hierarchical features into the decoder dramatically worsens performance (PSNR: -16.27 dB, SSIM: -0.360, LPIPS: +0.374), indicating its crucial role in integrating detailed local and global context. Visual outputs without this fusion module exhibit severe deficiencies in both structure and texture (Figure 5).

## 6 . Conclusion

We presented NGP-SR, a generalizable super-resolution framework for Neural Radiance Fields that reconstructs high-resolution views directly from low-resolution multi- view inputs. By combining hierarchical spatial-texture encoding, camera-aware feature integration, and global feature fusion, NGP-SR produces detail-preserving and view- consistent reconstructions. Experiments on Blender, LLFF, and DTU show that NGP-SR outperforms state-of-the-art methods, especially in challenging low-resolution settings where standard NeRF and 3DGS backbones struggle. Our framework generalizes well to unseen scenes without per- scene retraining, and ablation studies confirm the importance of each component. Our approach reconstructs high- frequency details from LR inputs, without any generative models or high-frequency cues, high-frequency signals may be challengable despite visually sharp reconstructions. Future work will extend NGP-SR to high-frequency signals, dynamic scenes and explore lighter encodings for real-time deployment.

## References

