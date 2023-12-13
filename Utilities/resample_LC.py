from PIL import Image

# Open the original image
original_image_path = "LC2022.tif"
original_image = Image.open(original_image_path)

# Split the bands of the image
bands = original_image.split()

# Select the first band (index 0)
first_band = bands[0]


# Get the original dimensions
original_width, original_height = original_image.size

# Calculate the new dimensions (1/3 of the original size)
new_width = original_width // 9
new_height = original_height // 9

# Resize and resample the image
resized_image = first_band.resize((new_width, new_height), Image.NEAREST)
new_image = Image.merge('L', [resized_image])
# Save the resized image
new_image.save("resampledLC2022.tif")
