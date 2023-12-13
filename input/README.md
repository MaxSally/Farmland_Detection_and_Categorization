# ComputerVisionProject
 
### Two screenshots in the root folder are for one year of land cover image overlayed on the top of NDVI image. 
All images are resampled to smaller size (resampled 9x9 pixel as 1 pixel).
If the classified image had same values in 9x9 window, then that pixel is populated as same value, otherwise that pixel is set as NaN.
## Folders here contains:
1. Classified crops 2013 - 2022.
2. NDVI images for each year resampled at matching lower resolution.
3. Surface appearent temprature matching image size of classified images.
4. Utilities: Resample==> It contains post processing tasks like resampling TIFF's to lower resolution based on all pixels having same value, else the output is zero.
5. Utilities: ScatterPlotVsClasses ==> To generate the Land Cover classes Vs NDVI pixel sacatter plots (before and after filterning).
6. automatic_mask_generator_SAM PDF & IPYNB ==> To create image segmentation using the upoaded TIFF file (Note: Large file can't be uploaded here). It runs of Google Colab.

