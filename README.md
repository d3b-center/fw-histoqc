# Histoqc

HistoQC is an open-source quality control tool for digital pathology slides.
#**Requirements**

Tested with Python 3.7 and 3.8 Note: the DockerFile installs Python 3.8, so if your goal is reproducibility you may want to take this into account

Requires:

openslide
And the following additional python package:
python-openslide
matplotlib
numpy
scipy
skimage
sklearn
pytest (optional)
You can likely install the python requirements using something like (note python 3+ requirement):

pip3 install -r requirements.txt

The library versions have been pegged to the current validated ones. Later versions are likely to work but may not allow for cross-site/version reproducibility (typically a bad thing in quality control).

Openslide binaries will have to be installed separately as per individual o/s instructions

The most basic docker image can be created with the included (7-line) Dockerfile.

**Basic Usage**
