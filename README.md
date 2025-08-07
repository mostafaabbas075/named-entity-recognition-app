```
# 🧠 News Entity Explorer

A Named Entity Recognition (NER) project for extracting and visualizing entities (like people, organizations, locations, etc.) from news articles using SpaCy.  
The app supports both rule-based and model-based NER, with an interactive Streamlit interface.

## 📌 Features
- Parse and prepare the CoNLL 2003 dataset.
- Rule-based NER extraction (simple heuristics).
- Model-based NER using two SpaCy models:
  - `en_core_web_sm`
  - `en_core_web_md`
- Compare and visualize extracted entities using SpaCy’s `displacy`.
- Switch between models via user-friendly Streamlit interface.

## 🚀 How to Run

### 1. Install requirements
Make sure you have Python 3.8+ and install dependencies:

```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install streamlit spacy pandas
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
```

### 2. Run the Streamlit app

```bash
streamlit run ner_app.py
```

## 📁 Files Included

- `ner_app.py` → The Streamlit interface
- ❗ The models `en_core_web_sm` and `en_core_web_md` were downloaded and used locally for this project but are **not included** in the repo due to their size.  
  You can download them using the following commands:

```bash
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
```



## 📂 Dataset

- ✅ Google Drive (Notebooks + Dataset):
  [🔗 Click to Open](https://drive.google.com/drive/folders/1dDb19w5Vdm7gy_hWMccJNAtJfeqrW3Co?usp=drive_link)

- 📦 Original CoNLL2003 dataset from Kaggle:
  [🔗 Kaggle Dataset](https://www.kaggle.com/datasets/juliangarratt/conll2003-dataset)

## 🛠️ Rule-Based NER Logic

Simple pattern matching based on capitalization and known location terms.

Example:
```python
if word.istitle() and len(word) > 2:
    # Possible entity
```

## ✍️ Author  
Mostafa Abbas Saleh  
AI Student | NLP Practitioner

## 🙏 Acknowledgment  
Thanks to **Elevvo** for the valuable internship experience and professional training.
```
