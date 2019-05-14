from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read text file or enter words directly as a string
# text = open(path.join(d, 'INSERT_FILENAME.txt')).read()
text = "ENTER WORDS FOR PROCESSING INTO WORDCLOUD"

# read the mask image
circle_mask = np.array(Image.open(path.join(d, "circle_mask.png")))


wc = WordCloud(background_color="white", max_words=2000, mask=circle_mask,
               contour_width=3, contour_color='black')

# generate word cloud
wc.generate(text)

# save wordcloud as a png file
wc.to_file(path.join(d, "INSERT_NEW_FILENAME.png"))

# show before storing to file
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(circle_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
# plt.show()