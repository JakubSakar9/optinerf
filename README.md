# OptiNeRF: An extension of the MultiNeRF codebase with the addition of depth supervision

This repository was directly derived from the [MultiNeRF repository](https://github.com/google-research/multinerf), which Google Research published as a Code Release for Mip-NeRF 360, Ref-NeRF, and RawNeRF. The functionality that was added in this project is the option of depth supervised training for mip-NeRF when using adequate depth images for each viewpoint. The code was tested on three datasets which can be found in a [Google Drive directory](https://drive.google.com/drive/folders/1CvObrtawHvlLIk1IRxcQiaQAqaa1BW9_?usp=share_link).

## New configuration options

Here is the list of all configuration options that were not present in the original [MultiNeRF repository](https://github.com/google-research/multinerf)

## New configuration files

All of these files are stored in the **/config** directory

- **use_depth_supervision** - A bool that enables the depth supervision loss function. It can only be used for the mip-NeRF method; using for other methods such as mip-NeRF 360 or Ref-NeRF was not tested and may lead to undefined behaviour. Set to false by default.
- **depth_supervision_loss_mult** - A float that defines the multiplier used for the depth supervision loss function. Set to 0.1 by default.
- **depth_decay** - A float that defines how much will the value of the depth supervision loss multiplier decrease in time. Its name is slightly misleading as the rate is computed as one minus this value. The depth supervision loss function multiplier is multiplied by the decay rate for each iteration, so the value of this parameter is usually relatively small. Set to 0.0 by default, tested only for the value of 1e-3.
- **depth_loss_type** - A string that describes the depth supervision loss function type. The type of the loss function can be one of the following:
  - **ds** - Loss function that was proposed in the [DS-NeRF](https://github.com/dunbar12138/DSNeRF) paper which was based on KL divergence
  - **kl** - Loss function that was directly derived from the definition of KL divergence.
  - **mse** - Another loss function taken from [DS-NeRF](https://github.com/dunbar12138/DSNeRF). Used by default and whenever any other string is used as the parameter value.
- **efficient_sampling** - A bool that was created to enable a planned feature of efficient sampling near the input depth values. However, this feature was left unfinished, so setting this parameter to true will lead to undefined behavior. Set to false by default.

## Additional files

The following section contains additional files used during dataset preparation but are not part of the project and need to be run independently. All of these files are stored in the **/scripts** directory.

- **show_depthmap.ipynb**
- **depth_loss.ipynb**
- **transform_depth.py**
- **generate_cropped.ipynb**
- **pose_utils.py**, **colmap_read_model.py** - Files that were copied from the [LLFF repository](https://github.com/Fyusion/LLFF) and modified to produce pose bound for used datasets.

## References

- Mildenhall, B., Verbin, D., Srinivasan, P. P., Hedman, P., Martin-Brualla, R., & Barron, J. T. (2022, October 13). MultiNeRF: A Code Release for Mip-NeRF 360, Ref-NeRF, and RawNeRF. GitHub.
https://github.com/google-research/multinerf
- Mildenhall, B., Srinivasan, P. P., Ortiz-Canyon, R., Kalantari, N. K., Ramamoorthi, R., Ng, R., & Kar, A. (2021, January 21). Local Light Field Fusion. GitHub. https://github.com/Fyusion/LLFF
- Deng, K., Liu, A., Zhu, J. Y., & Ramanan, D. (2023, January 19). Depth-
supervised NeRF: Fewer Views and Faster Training for Free. GitHub.
https://github.com/dunbar12138/DSNeRF#depth-supervised-ner
f-fewer-views-and-faster-training-for-free
