import numpy as np
import matplotlib.pyplot as plt
import tifffile
import seaborn as sns

# Example data, replace it with your actual image data
img_values = tifffile.imread(r"LC08_L1TP_031032_20220804_20220817_02_T1_NDVI_adj_Filtered.tif")
class_values = tifffile.imread("LC2022_Filtered.tif")
class_indices = np.unique(class_values) # Random class indices (0 to 4)
colors = sns.color_palette("husl", len(class_indices))
# Flatten the images to 1D arrays
flat_img_values = np.asarray(img_values).flatten()
flat_class_indices = np.asarray(class_values).flatten()

# Create a scatter plot
plt.figure(figsize=(8, 12))

# Plot each point with a color corresponding to its class
for i in range(len(class_indices)):
    classValue = class_indices[i]
    if classValue==0:
        continue
    color = colors[i]
    class_points = flat_img_values[flat_class_indices == classValue]
    xVals = [classValue] * len(class_points)
    plt.scatter(xVals, class_points, color=color, label=f'ID_{classValue}',s=2)

# Customize the plot
plt.title('NDVI Values vs. Class Index after NxN filtering.')
plt.xlabel('Class Index')
plt.ylabel('Pixel Values')
plt.legend()
plt.savefig("NDVI_Vs_ClassIndex_Cleaned.png")

plt.close()
print("")
