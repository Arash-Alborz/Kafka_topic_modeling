# Kafka Topic Modeling

This project applies **Latent Dirichlet Allocation (LDA)** to a curated corpus of Franz Kafka’s fictional works and diaries (in the original German). Using unsupervised machine learning, the system identifies latent thematic structures across Kafka’s texts, visualizes topic distributions, and explores semantic coherence within his narrative universe.

---

## Project Structure

```
kafka_topic_modeling/
├── data/
│   ├── raw_chunks/                # text chunks (input - not cleaned)
│   ├── kafka_metadata.csv         # chunk titles, years, word counts, etc.
│
├── results/
│   ├── visualizations/
│   ├── csv_outputs/
│
├── notebooks/
│   ├── data_analysis.ipynb     # cleaning & tokenization
│   ├── 01_preprocessing.ipynb
│   ├── 02_topic_modeling.ipynb    # vectorization + LDA
│   ├── 03_topic_inspection.ipynb  # visualizations & analysis for evaluating the topics
│   └── 04_interpretation.ipynb    # 
│
├── config.py                      # paths and model settings (model parameters)
├── environment.yml                # conda environment
└── README.md
```

---

## Setup (Conda)

### 1. Clone the Repository

```bash
git clone https://github.com/Arash-Alborz/kafka-topic-modeling.git
cd kafka-topic-modeling
```

### 2. Create the Environment
Recommending conda environment

```bash
conda env create -f environment.yml
```

### 3. Activate the Environment

```bash
conda activate kafka_topic_modeling
```

---

## Usage

All notebooks are organized and numbered in a logical workflow. To begin, open the `.ipynb` files in **VSCode** with the appropriate conda environment activated.

### Configuration

Before running any notebooks, make sure to execute the `config.py` file once. This script defines all relevant project paths and modeling parameters (e.g., number of topics, vectorization thresholds). It also ensures that all required output directories (for saving results and visualizations) are automatically created.

```bash
python config.py
```

You only need to run this once per setup to ensure proper path handling and output folder creation.

### Notebook Order

1. `01_preprocessing.ipynb`  
   Preprocess and tokenizes the text chunks using spaCy. Saves cleaned text and filenames as `cleaned_chunks.csv`.

2. `02_topic_modeling.ipynb`  
   Loads the cleaned data, performs vectorization, trains the LDA model, saves the topic-word and document-topic distributions to CSV, and prints topic keywords.

3. `03_topic_inspection.ipynb`  
   Analyzes and visualizes the topic distributions (used for evaluating the topics).

4. `04_interpretation.ipynb` 
   Integrates topic distribution with metadata (year and genre) to perform chronological and type-based topic analysis (fiction vs. diaries).

Ensure that all notebooks access paths and parameters consistently via the `config.py` file.
Run `config.py` once before running other notebooks.
Make sure all required data (`data/raw_chunks/`, `kafka_metadata.csv`) is present.

---

## Features

- Topic modeling with `scikit-learn`’s LDA
- SpaCy-based preprocessing (`de_core_news_sm`)
- Visualization of:
  - Dominant topic distribution
  - Topic sparsity
  - Temporal trends
  - Topic similarity (cosine heatmap)
- Reproducible pipeline with CSV + PNG output

---

## Reproducibility

All output CSV files and plots are automatically saved in the `results/` folder. If you add new chunks or retrain the model, simply re-run the notebooks.

---

## Data Source

The texts were obtained from [Projekt Gutenberg-DE](https://www.projekt-gutenberg.org) and manually chunked. Only Kafka’s original German texts were used to preserve semantic nuance.

---

## Tools & Libraries

- Python 3.10 (via Conda)
- `spaCy` (lemmatization + tokenization)
- `scikit-learn` (LDA modeling)
- `matplotlib`, `seaborn`, `pandas`, `pyLDAvis`
- `wordcloud`, `nltk`

---

## Author: Arash Alborz

## License

This repository is for academic and educational purposes only.