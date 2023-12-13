
import numpy as np
from osgeo import gdal
import glob
import pandas as pd

def saveCSV(yearName):
    yearName = yearName.split("\\")[-1]
    dfData = pd.DataFrame()
    ndviList = glob.glob(f"J:\\ProjectComputerVision\\ProcessedData\\ComputerVisionProject\\NDVI\\{yearName}\\*.tif")
    thermalList = glob.glob(f"J:\\ProjectComputerVision\ProcessedData\\ComputerVisionProject\\BrightnessTemp\\{yearName}\\*.tif")
    for ndvi in ndviList:
        fileName = ndvi.split("\\")[-1].replace(".tif", "").split("_")[3]+"_ndvi"
        dfData[fileName] = gdal.Open(ndvi).ReadAsArray().flatten().tolist()

    for thermal in thermalList:
        fileName = thermal.split("\\")[-1].replace(".tif", "").split("_")[3]+"_temp"
        dfData[fileName] = gdal.Open(ndvi).ReadAsArray().flatten().tolist()

    crop_labels = gdal.Open(f"J:\\ProjectComputerVision\\ProcessedData\\ComputerVisionProject\\LandCover\\LC{yearName}_Filtered.tif").ReadAsArray().flatten().tolist()
    dfData["ClassName"] = crop_labels
    dfData["ClassName"] = dfData["ClassName"].replace(0,pd.NA)
    dfData = dfData.dropna()
    dfData.to_csv(f"OutputCombo{yearName}.csv", index=False)

folders = glob.glob(f"J:\\ProjectComputerVision\\ProcessedData\\ComputerVisionProject\\NDVI\\*")
for folder in folders:
    saveCSV(folder)

