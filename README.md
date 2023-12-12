# Farmland_Detection_and_Categorization
## Objective 1: Preprocessing
## Objective 2: Crop vs no crop
- `src/DataPreprocessing.ipynb` is Jupyter Notebook to preprocess input data.
- `input/objective_2_crop_vs_no_crop` contains a sample to input images used to train UNet.
- `src/UNetTrain.ipynb` is to build the UNet model.
## Objective 3: Crop categorization
- `Crop_classification.ipynb` is the Jupyter notebook to build the model. 
- `input/objective_2_crop_classification` is the dataset used for the model. Each image is a sample image of a crop area with the top 3 labels in its name. Because the image encodes BrightnessTemp with the normalized value of a region, the image, when viewed under a typical image viewer, may appear strange. 
    + The dataset in this repository is only a small sample of the actual dataset. Please use the link here to get entire dataset and put them in this directory for training. [Link](https://uofnelincoln-my.sharepoint.com/:u:/g/personal/qnguyen16_unl_edu/EeP1VMgU0HxGh4ea2xB7PJoB0zz_piamE_PjgyJoFSaCGQ?e=MFb3jO) to the dataset 
- `result/objective2` contains the results of objective 2 such as training history and metrics vs epochs (top1 + top3 accuracy, F1 score, and loss) of validation and loss 
- `src/crop_classification_utilities.py`: contains utilities function to print graphs from training history.
## Objective 4: Growth length
