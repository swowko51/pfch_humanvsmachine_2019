# API: The Met
# No key required

import requests

# r = requests.get('https://collectionapi.metmuseum.org')
# print('The request code was:',r.status_code)
# print('Here is the text of the webpage:',r.text)

# Finding object ID using the search
# r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/search?q=dish-depicting-two-birds-among-flowering-plants')
# print(r.status_code)
# print(r.text)

# Using the Object ID from the search to get all metadata for the object, including tags.
r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/451490')
print(r.text)

# Parse out just the Object ID, Title, Tags