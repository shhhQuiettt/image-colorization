# Image colorization

## Authors
- [Krzysztof Skrobała](https://github.com/shhhQuiettt)
- [Wojciech Bogacz](https://github.com/wojbog)


## Problem description
The image colorization problem is a challenging and fascinating task in computer vision, where the goal is to transform a grayscale image into a fully colored one. This task is particularly challenging because it is an ill-posed problem, as there are many possible colorizations for a single grayscale image. 

## Used architecture
The architecture used in this project is a version of the U-Net architecture. The U-Net architecture is a convolutional neural network that consists of a contracting path, which captures context, and an expansive path, which enables precise localization. The architecture also has skip connections, which allow the network to use features from the contracting path in the expansive path. The U-Net architecture has been widely used in image segmentation tasks and has been shown to be effective in many applications.

In our porject we used U-Net architecture imported from segmentation_models_pytorch library. As an encoder we took ResNet18 trained on ImageNet dataset. 


<img src="pictures\model.png" width="500" height="500" style="margin-left: 110px; margin-right: auto;">
<img src="pictures\model_desc.png" width="500" height="500" style="margin-left: auto; margin-right: auto;">

## Dataset
[Dataset](https://www.kaggle.com/datasets/alessiocorrado99/animals10)

The dataset contains about 28K medium quality animal images belonging to 10 categories: dog, cat, horse, spyder, butterfly, chicken, sheep, cow, squirrel, elephant.

In a data preprocessing we croped images to size 224x224 and to increase diversity as an augumentation process we applied Random horizontal fip and random rotation up to 15 degree. Both operations were apply under 0.3 probabillity.   

## Training and Results
We grouped our data set into batches and in each batch there are 128 images with size 224x224.

The training consisted of three parts:
1. Training only decoder with moderate learning rate
2. Training only decoder with small learning rate
3. Training the whole network 

The **early stopping** was implemented, and the model with the best validation loss is taken to the next stage 

In the first part of the training we used our model with the following parameters: learing rate: **0.01**, loss function: **MAE**, optimizer: **Adam** and patience for early stopping: **6**

The following graph shows loss function for validation and training set:

<img src="pictures\loss_1.png" width="500" height="500" style="display: block; margin-left: auto; margin-right: auto;">

Validation loss decreases steadly. Nice!


The results from the model after first part of the training presents as follows:



<img src="pictures\pred_1_1.png"  style="display: block; margin-left: auto; margin-right: auto;">
<img src="pictures\pred_1_2.png"  style="display: block; margin-left: auto; margin-right: auto;">
<img src="pictures\pred_1_3.png"  style="display: block; margin-left: auto; margin-right: auto;">


In the next stage we decreased learning rate and set to: **0.001**. The rest of the parameters remained unchanged.

<img src="pictures\loss_2.png" width="500" height="500" style="display: block; margin-left: auto; margin-right: auto;">

Unfortunately reducing learning rate didn't improve the model :(

<img src="pictures\pred_2_1.png"  style="display: block; margin-left: auto; margin-right: auto;">
<img src="pictures\pred_2_2.png"  style="display: block; margin-left: auto; margin-right: auto;">
<img src="pictures\pred_2_3.png"  style="display: block; margin-left: auto; margin-right: auto;">


In the last part of the training we unlocked the encoder part of the model. The results present as follows:

<img src="pictures\loss_3.png" width="500" height="500" style="display: block; margin-left: auto; margin-right: auto;">

<img src="pictures\pred_3_1.png"  style="display: block; margin-left: auto; margin-right: auto;">
<img src="pictures\pred_3_2.png"  style="display: block; margin-left: auto; margin-right: auto;">
<img src="pictures\pred_3_3.png"  style="display: block; margin-left: auto; margin-right: auto;">

We see that the last stage doesn't show much improvement. In fact we see classical example of **overfiting**, because training loss decreases while validation loss doesn't improve.

The training process can be found in jupiter notebook: train_model.ipynb

## Prediction API

We implemented simple REST API configured in the docker environment. The `code` is in the `server` folder.

## Table with completed requirements
| Requirement | Number of points |
| --- | --- |
| Problem colorization | 1 |
| pre-trained model on the different problem (transfer-learning) | 1 |
|additional model | 1 |
| Evaluation on a set with at least 10000 photos | 1 |
| partialy our own dataset | 1 |
| Hyperparameter tuning or estimation | 1 |
| Data augmentation | 1 |
| docker/ docker compose | 1 |
| REST API | 1 |
| DVC | 2 |
| --- | --- |
| sum: | 11 |

