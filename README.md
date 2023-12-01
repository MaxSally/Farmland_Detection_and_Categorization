# Farmland_Detection_and_Categorization
1. Objective 1: Preprocessing
2. Objective 2: Crop vs no crop
3. Objective 3: Crop categorization
- `Crop_classification.ipynb` is the Jupyter notebook to build the model. 
- `input/objective_2_crop_classification.zip` is the dataset used for the model. Each image is a sample image of a crop area with the top 3 label in its name. **Please extract this before running the model**. You may not be able to view it directly because it is a BrightnessTemp map with normalized value. 
- `result/objective2` contains the results of objective 2 such as training history and metrics vs epochs (top1 + top3 accuracy, F1 score, and loss) of validation and loss 
- `src/crop_classification_utilities.py`: contains utilities function to print graphs from training history.
4. Objective 4: Growth length
