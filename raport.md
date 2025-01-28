# Image colorization

## Problem description
The image colorization problem is a challenging and fascinating task in computer vision, where the goal is to transform a grayscale (black-and-white) image into a fully colored one. This task is particularly challenging because it is an ill-posed problem, as there are many possible colorizations for a single grayscale image. 

## Used architecture
The architecture used in this project is a version of the U-Net architecture. The U-Net architecture is a convolutional neural network that consists of a contracting path, which captures context, and an expansive path, which enables precise localization. The architecture also has skip connections, which allow the network to use features from the contracting path in the expansive path. The U-Net architecture has been widely used in image segmentation tasks and has been shown to be effective in many applications.

In our porject we used U-Net architecture imported from segmentation_models_pytorch library. As an encoder we took ResNet18 trained on ImageNet dataset. 


<img src="pictures\model.png" width="500" height="500" style="display: block; margin-left: auto; margin-right: auto;">
<img src="pictures\model_desc.png" width="500" height="500" style="display: block; margin-left: auto; margin-right: auto;">

## Dataset



## Results


## table with completed requirements
| Requirement | Number of points |
| --- | --- |
| Problem colorization | 1 |
| pre-trained model on the different problem (transfer-learning) | 1 |
| Evaluation on a set with at least 10000 photos | 1 |
| our own dataset | 1 |
| Hyperparameter tuning or estimation | 1 |
| Data augmentation | 1 |
| docker/ docker compose | 1 |
| REST API | 1 |
| DVC | 2 |
| --- | --- |
| sum: | 10 |

### Github repository
[Link to repository](https://github.com/shhhQuiettt/image-colorization)