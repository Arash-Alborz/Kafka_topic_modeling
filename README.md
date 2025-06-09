# Kafka Topic Modeling

This project applies **Latent Dirichlet Allocation (LDA)** to a curated corpus of Franz Kafka’s fictional works (in the original German). Using unsupervised machine learning, the system identifies latent thematic structures across Kafka’s texts, visualizes topic distributions, and explores semantic coherence within his narrative universe.

---

## Project Structure

```
kafka_topic_modeling/
├── data/
│   ├── raw_chunks/                 # Text chunks (input)
│   ├── kafka_metadata.csv         # Metadata: titles, years, word counts, etc.
│
├── results/
│   ├── visualizations/            # Saved figures and plots
│   ├── csv_outputs/               # topic distributions, keywords, etc.
│
├── notebooks/
│   ├── 01_preprocessing.ipynb     # Cleaning & lemmatization
│   ├── 02_topic_modeling.ipynb    # Vectorization + LDA
│   ├── 03_topic_inspection.ipynb  # Visualizations & analysis
│   └── 04_metadata_analysis.ipynb # (optional) Timeline/topic correlation
│
├── config.py                      # Paths and model settings
├── environment.yml                # Reproducible conda environment
└── README.md                      # You're here!
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
   Preprocess and lemmatize the text chunks using spaCy. Saves cleaned text and filenames as `cleaned_chunks.csv`.

2. `02_topic_modeling.ipynb`  
   Loads the cleaned data, performs vectorization, trains the LDA model, saves the topic-word and document-topic distributions to CSV, and prints topic keywords.

3. `03_topic_inspection.ipynb`  
   Analyzes and visualizes the topic distributions. Includes sample visualizations, dominant topic counts, topic overlap, and similarity plots.

4. `04_metadata_analysis.ipynb` *(optional)*  
   Integrates topic distribution with metadata (e.g., year, title, genre) to perform chronological and genre-based topic analysis.

Ensure that all notebooks access paths and parameters consistently via the `config.py` file.

Make sure all required data (`data/raw_chunks/`, `kafka_metadata.csv`) is present.

---

## Features

- Topic modeling with `scikit-learn`’s LDA
- SpaCy-based preprocessing (`de_core_news_sm`)
- Visualization of:
  - Dominant topic distribution
  - Topic entropy & sparsity
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
- `spaCy` (lemmatization)
- `scikit-learn` (LDA modeling)
- `matplotlib`, `seaborn`, `pandas`, `pyLDAvis`
- `wordcloud`, `nltk`

---

## Author: Arash Alborz

## License

This repository is for academic and educational purposes only.