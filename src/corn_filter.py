import os
import tifffile
import numpy as np

# Specify the paths to your CDL and NDVI folders
cdl_folder = 'LandCover/'
ndvi_folder_base = 'NDVI/'
output_folder_corn = 'Corn/'
output_folder_corn_ndvi = 'Output/'

# Define the range of years
years_range = range(2013, 2023)

# Iterate over CDL years
for year in years_range:
    cdl_filename = f'LC{year}_Filtered.tif'
    cdl_path = os.path.join(cdl_folder, cdl_filename)
    output_path_corn_file = os.path.join(output_folder_corn, cdl_filename.replace("_Filtered.tif", "_Corn.tif"))

    # Load CDL image
    cdl_data = tifffile.imread(cdl_path)

    # Identify the code for corn (replace 1 with the actual code)
    corn_code = 1

    # Create a binary mask for corn
    corn_mask = (cdl_data == corn_code)

    # Save the corn mask as a new image using tifffile
    tifffile.imwrite(output_path_corn_file, corn_mask.astype(np.uint8))

    # Construct the path for NDVI folder for the corresponding year
    ndvi_folder_year = os.path.join(ndvi_folder_base, str(year))

    # Check if the NDVI folder for the corresponding year exists
    if os.path.exists(ndvi_folder_year):
        # Construct the path for the corresponding year in output_folder_corn_ndvi
        output_folder_corn_ndvi_year = os.path.join(output_folder_corn_ndvi, str(year))

        # Check if the output folder for the corresponding year exists, if not, create it
        if not os.path.exists(output_folder_corn_ndvi_year):
            os.makedirs(output_folder_corn_ndvi_year)

        # Iterate over NDVI files in the corresponding folder
        for ndvi_filename in os.listdir(ndvi_folder_year):
            if ndvi_filename.endswith(".tif"):
                # Construct the paths for NDVI files
                ndvi_path = os.path.join(ndvi_folder_year, ndvi_filename)
                
                # Extract the NDVI file name without the extension
                ndvi_name_without_extension = os.path.splitext(ndvi_filename)[0]
                
                # Construct the output path for corn NDVI file in the respective year folder
                output_path_corn_ndvi_file = os.path.join(output_folder_corn_ndvi_year, f'{ndvi_name_without_extension}_Corn_NDVI.tif')

                # Load NDVI image
                ndvi_data = tifffile.imread(ndvi_path)

                # Apply the corn mask to NDVI data
                corn_ndvi = np.where(corn_mask, ndvi_data, 0)  # Set non-corn pixels to 0

                # Save the result as a new NDVI image using tifffile
                tifffile.imwrite(output_path_corn_ndvi_file, corn_ndvi)
    else:
        print(f"No NDVI folder found for the year {year}.")