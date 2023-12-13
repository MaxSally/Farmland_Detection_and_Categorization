import os
import numpy as np
import tifffile

def filter_ndvi_with_kc(ndvi_path, output_path_filtered, kc_range):
    # Load NDVI image
    ndvi_data = tifffile.imread(ndvi_path)

    # Convert NDVI to Kc using the formula Kc = 1.457 * NDVI - 0.1725
    kc_data = (1.457 * ndvi_data) - 0.1725

    # Create a mask for pixels within the specified Kc range
    kc_mask = np.logical_and(kc_data >= kc_range[0], kc_data <= kc_range[1])

    # Apply the mask to keep only pixels within the specified Kc range
    filtered_ndvi = np.where(kc_mask, ndvi_data, 0)  # Set non-matching pixels to 0

    # Save the filtered NDVI image
    tifffile.imwrite(output_path_filtered, filtered_ndvi)

# Example paths and parameters
input_folder = 'Predict/3 Late/'
output_folder = 'Kpredict/3 Late/'
kc_range_initial = (0.6-0.2, 0.6+0.2)

# Iterate over files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith("_NDVI.tif"):
        # Construct full paths
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".tif", "_Kc.tif"))

        # Apply the filter function
        filter_ndvi_with_kc(input_path, output_path, kc_range_initial)
