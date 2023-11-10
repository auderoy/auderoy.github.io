- [View on Google Drive](https://drive.google.com/drive/folders/19LlSZPHSBr38YvoHUiRmO_9do4jt-lCX?usp=sharing)
- [View live website](https://alexdseo.github.io/Visualization-App-on-World-Events/)

# Workflow

## 1. Preprocess images

`image_preprocessing.ipynb`
- Requires: 
	- Pillow: `pip3 install PyMuPDF Pillow`
- Input: `data` (see Google Drive for all files; sample on GitHub)
- Output: `data_resized` (see Google Drive for all files; sample on GitHub)

## 2. Extract text with Optical Character Recognition

`text_extraction.ipynb`
- Requires:
	- Pillow: `pip3 install PyMuPDF Pillow`
	- PyTesseract: `pip install pytesseract`
	- Tesseract: `brew install tesseract`
- Input: `data_resized` (see Google Drive for all files; sample on GitHub)
- Output: `raw_text` (see Google Drive for all files; sample on GitHub)

## 3. Process text

`text_processing.ipynb`
- Input: `raw_text` (see Google Drive for all files; sample on GitHub)
- Output: `cleaned_text` (see Google Drive for all files; sample on GitHub)

### 4. Name Entities Recognition and analysis

- Run Named Entity Recognition on GPU: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com//github/alexdseo/Visualization-App-on-World-Events/blob/master/NER.ipynb)
	- Input: `cleaned_text` (see Google Drive for all files; sample on GitHub)
	- Output: charts in Notebook and on website

### 5. Geolocation

- Run Geoparsing on GPU: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com//github/alexdseo/Visualization-App-on-World-Events/blob/master/geoparsing.ipynb)
	- Input: `cleaned_text` (see Google Drive for all files; sample on GitHub)
	- Output: `geoparse.csv`
- Run Dynamic Mapping on GPU: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com//github/alexdseo/Visualization-App-on-World-Events/blob/master/dynamic_maps.ipynb)
	- Requires Mapbox API token
	- Input: `geoparse_clean.csv`
	- Output: world map and Ukraine map in Notebook and on website

### 6. Web page

[See our live website here and interact with our maps!](https://alexdseo.github.io/Visualization-App-on-World-Events)
	- [View GitHub repo](https://github.com/alexdseo/Visualization-App-on-World-Events)