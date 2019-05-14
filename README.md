# Human vs. Machine

This is a final project for the Pratt Institute course Programming for Cultural Heritage.

At the outset of a keyword tagging project for a museum collection, a question that repeatedly came up during research was artificial intelligence tagging (sometimes referred to as computer vision) compared to human tagging. Larger museums who have tested out computer vision technology currently available have often chosen to go with people for keyword tagging because of the varying levels of accuracy. This project started out as a way to simply compare those human keyword tags to keyword tags provided by the Google Cloud Vision API. It has since developed into a series of scripts and a workflow for making this comparison and creating a visual representation of the resulting data sets. The human keyword data for this particular project came from The Metropolitan Museum of Art's open access initiative. All images used to produce the final report are avaialble for download on The Met's collection website. The workflow outlined below is intended to be adjusted and reused as a template for other museums to analyze their own keyword tags against the Google Cloud Vision API. 

Workflow:

1) Retrieved a .csv file of The Met's <a href="https://github.com/metmuseum/openaccess/blob/master/MetObjects.csv" target="_blank">open access</a> data.

2) Setup Google Cloud Vision API using available <a href="https://cloud.google.com/vision/docs/libraries#client-libraries-usage-python" target="_blank">documentation</a>.

3) Downloaded images from The Met <a href="https://www.metmuseum.org/art/collection" target="_blank">collection</a>.

4) Batch processed the downloaded images through the Vision API. Exported to JSON.

5) Used <a href="https://github.com/paulbrodersen/matplotlib_venn_wordcloud" target="_blank">matplotlib_venn_wordcloud</a> to make a venn diagram displaying the human tagged keywords compared to the ai tagged keywords.

6) Venn diagrams could not be created for those objects that did not have any matching keywords between the two datasets. Used <a href="https://github.com/amueller/word_cloud" target="_blank">word_cloud</a> to make two separate wordclouds comparing the human keywords to the ai keywords.

NOTE: The Google Cloud Vision API key used to create the examples is not included in this repository. In the scripts you will see a note to 'INSERT KEY HERE'. 