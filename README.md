# Farmland_Detection_and_Categorization
## Objective 1: Preprocessing
## Objective 2: Crop vs no crop
## Objective 3: Crop categorization
- `Crop_classification.ipynb` is the Jupyter notebook to build the model. 
- `input/objective_2_crop_classification.zip` is the dataset used for the model. Each image is a sample image of a crop area with the top 3 label in its name. **Please extract this before running the model**. You may not be able to view it directly because it is a BrightnessTemp map with normalized value. 
    + Unfortunately, due to Github size limit, I cannot upload it directly. [Link](https://uofnelincoln-my.sharepoint.com/:u:/g/personal/qnguyen16_unl_edu/EeP1VMgU0HxGh4ea2xB7PJoB0zz_piamE_PjgyJoFSaCGQ?e=MFb3jO) to the dataset 
- `result/objective2` contains the results of objective 2 such as training history and metrics vs epochs (top1 + top3 accuracy, F1 score, and loss) of validation and loss 
- `src/crop_classification_utilities.py`: contains utilities function to print graphs from training history.
## Objective 4: Growth length
