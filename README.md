# Flywheel gear that implements Histoqc

HistoQC is an open-source quality control tool for digital pathology slides.

HistoQC utilizes a configuration file to define the processing pipeline. By default the gear uses a built-in H&E pipeline (config_v2.1.ini). Users can input their own configuration file to the gear if they wish to run other processes.

## **Requirements**:
- openslide
- python-openslide
- matplotlib
- numpy
- scipy
- skimage
- sklearn

Runs on Python 3.8.

**Required inputs:**
Input image

**Optional inputs:**
Config file (.ini)

## **Local Gear Testing**
1. Clone repo to local machine
2. Copy a pathology file to the same directory (e.g., "HandE.svs")
3. Build the docker container
```
docker build -t chop.flywheel.io/histoqc:[version#] ./
Note: To convert to different architecture (example: linux/amd64):
docker buildx build --platform linux/amd64 -t chop.flywheel.io/histoqc:[version#] ./
```
4. Run gear locally
```
fw-beta gear config --new
fw-beta gear config --input input_image=HandE.svs
fw-beta gear config --input api-key=[your-api-key]
fw-beta gear run
```

##  **Citation**

"HistoQC: An Open-Source Quality Control Tool for Digital Pathology Slides", Janowczyk A., Zuo R., Gilmore H., Feldman M., Madabhushi A., JCO Clinical Cancer Informatics, 2019

“Assessment of a computerized quantitative quality control tool for kidney whole slide image biopsies”, Chen Y., Zee J., Smith A., Jayapandian C., Hodgin J., Howell D., Palmer M., Thomas D., Cassol C., Farris A., Perkinson K., Madabhushi A., Barisoni L., Janowczyk A., Journal of Pathology, 2020

