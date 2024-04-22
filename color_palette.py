import os
import csv
import colorgram

# Function to extract color palette and proportions
def extract_color_palette(image_path, num_colors):
    colors = colorgram.extract(image_path, num_colors)
    color_palette = []
    for color in colors:
        rgb = color.rgb
        proportion = color.proportion
        color_palette.append({'rgb': rgb, 'proportion': proportion})
    return color_palette

# Folder containing images
images_folder = "website_screenshots"

# Output CSV file
output_csv = "color_palette.csv"

# Dictionary to store results by filename
results_dict = {}

# Iterate through images in the folder
for filename in os.listdir(images_folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        image_path = os.path.join(images_folder, filename)
        # Extract color palette and proportions
        color_palette = extract_color_palette(image_path, 6)  # Extract 6 colors
        # Check if filename already exists in results_dict
        if filename in results_dict:
            # If it exists, extend the existing color palette
            results_dict[filename].extend(color_palette)
        else:
            # If it doesn't exist, add a new entry
            results_dict[filename] = color_palette

# Write results to CSV
with open(output_csv, mode='w', newline='') as csvfile:
    fieldnames = ['filename', 'color_rgb', 'color_proportion']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate through results_dict
    for filename, colors in results_dict.items():
        writer.writerow({'filename': filename, 'color_rgb': colors, 'color_proportion': 1.0})

print("Color palette extraction completed. Results saved to:", output_csv)
