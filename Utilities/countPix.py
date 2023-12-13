import tifffile
import glob

tiffList = glob.glob("*.tif")
for tiff in tiffList:
    pixArray = tifffile.imread(tiff)
    rows, cols = pixArray.shape
    pixelCount = 0
    for i in range(0,cols-1):
        for j in range (0,rows-1):
            if (pixArray[j,i]>0):
                pixelCount+=1
    print(f"Non zero pixels in {tiff} = {pixelCount}/{rows*cols}")