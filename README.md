# Farmland_Detection_and_Categorization 
CSCE 873: Computer Vision Project
## Objective 1: Preprocessing (Ashish)
- Two screenshots in the root folder are for one year of land cover image overlayed on the top of NDVI image. 
- All images are resampled to smaller size (resampled 9x9 pixel as 1 pixel).
    - If the classified image had same values in 9x9 window, then that pixel is populated as same value, otherwise that pixel is set as NaN.
- `input\` includes
    - Classified crops 2013 - 2022.
    - NDVI images for each year resampled at matching lower resolution.
    - Surface apparent temperature matching image size of classified images.
    - `Utilities: Resample`: Contain post processing tasks like resampling TIFF's to lower resolution based on all pixels having same value, else the output is zero.
    - `Utilities: ScatterPlotVsClasses`: Generate the Land Cover classes Vs NDVI pixel scatter plots (before and after filtering).
    - `automatic_mask_generator_SAM PDF & IPYNB`: Create image segmentation using the uploaded TIFF file (Note: Large file can't be uploaded here). It runs of Google Collab.
        - `automatic_mask_generator_SAM PDF`: Read the script as a PDF file.
## Objective 2: Crop vs no crop (Shubham)
- `src/DataPreprocessing.ipynb` is Jupyter Notebook to preprocess input data.
- `input/objective_2_crop_vs_no_crop` contains a sample to input images used to train UNet.
- `src/UNetTrain.ipynb` is to build the UNet model.
- `src/UNetTrain.ipynb` is to build the UNet model.
## Objective 3: Crop categorization (Max, Quan, MaxSally)
- `Crop_classification.ipynb` is the Jupyter notebook to build the model. 
- `input/objective_2_crop_classification` is the dataset used for the model. Each image is a sample image of a crop area with the top 3 labels in its name. Because the image encodes BrightnessTemp with the normalized value of a region, the image, when viewed under a typical image viewer, may appear strange. 
    + The dataset in this repository is only a small sample of the actual dataset. Please use the link here to get entire dataset and put them in this directory for training. [Link](https://uofnelincoln-my.sharepoint.com/:u:/g/personal/qnguyen16_unl_edu/EeP1VMgU0HxGh4ea2xB7PJoB0zz_piamE_PjgyJoFSaCGQ?e=MFb3jO) to the dataset 
- `result/objective2` contains the results of objective 2 such as training history and metrics vs epochs (top1 + top3 accuracy, F1 score, and loss) of validation and loss 
- `src/crop_classification_utilities.py`: contains utilities function to print graphs from training history.
## Objective 4: Growth length (Salem)
- Use `cropgrowth_predictor.ipynb` to train snd save the model.
- Trained model saved as `growth_stage_predictor.h5`.
- `cropgrowth_predictor-checkpoint.ipynb` can be used to observe how the current model was trained.
- `corn_filter.py` under code was used to filter non-corn areas out of the dataset.
- `Kc_filter.py` under code was used to filter out areas that do not match the appropriate corn growth stage obtained using Kc values and the Day of Year (DOY) the image was captured on.
