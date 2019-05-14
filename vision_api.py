import io
import os
import re


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Set Google API authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "INSERT_FULL_KEY_FILE_PATH"

# ---------------------------------------------------------------------
# Retrieve labels for a single image 

# Instantiates a client
client = vision.ImageAnnotatorClient()

# # The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'INSERT_FULL_FILE_PATH')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# # Performs label detection on the image file
response = client.label_detection(image=image)
tags = response.label_annotations


# Compiling regex pattern to capture just the filename and not the whole path.
p = re.compile('(images/(.*)\.)')
m = p.search(file_name)


print('OBJECT:')
print(m.group(2))
print('----------------------------------')
print('TAGS:')
for tag in tags:
    print(tag.description)

