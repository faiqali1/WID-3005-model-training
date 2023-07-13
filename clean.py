import os
import numpy as np
import pandas as pd
from PIL import Image

dataset_dir = './data'
image_width = 256
image_height = 256

image_arrays = []
labels = []

for filename in os.listdir(dataset_dir):
    image_path = os.path.join(dataset_dir, filename)
    # Assuming the label is part of the filename before the extension
    label = filename.split('.')[0]

    # Load and resize the image using PIL
    image = Image.open(image_path).resize((image_width, image_height))

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Append the image array and label to the lists
    image_arrays.append(image_array)
    labels.append(label)

data = {
    'image data': image_arrays,
    'label': labels
}

df = pd.DataFrame(data)

df.to_csv('cleaned_data.csv', index=False)
