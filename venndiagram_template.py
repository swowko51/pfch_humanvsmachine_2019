from PIL import Image
from matplotlib_venn_wordcloud import venn2_wordcloud
import matplotlib.pyplot as plt

# If none of the words in the strings match a visualization will not be created. 
# AttributeError: 'NoneType' object has no attribute 'set_text'
api = "ENTER WORDS FROM VISION API RESULTS"
csv = "ENTER WORDS FROM MET CSV"

# tokenize words (approximately at least):
sets = []
for string in [api, csv]:

    # get a word list
    words = string.split(' ')

    # remove non alphanumeric characters
    words = [''.join(ch for ch in word if ch.isalnum()) for word in words]

    # convert to all lower case
    words = [word.lower() for word in words]

    sets.append(set(words))

# generate venn diagram
venn2_wordcloud(sets, set_labels=['Machine', 'Human'])
# plt.show()


# Save venn diagram as a png file
plt.savefig('INSERT_NEW_FILENAME.png')