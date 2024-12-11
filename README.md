# Exploratory Data Analysis using Python's SweetViz library

Comprehensive framework for performing exploratory data analysis (EDA) using Python's SweetViz library. With features like dataset loading, customizable splits, and dynamic report generation via an interactive Streamlit app, it enables seamless insights into data comparisons and target analysis.

## 📑 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Data Description](#️-data-description)
- [Documentation](#-documentation)

## ✨ Features

- 📊 Detailed visualizations of data distributions
- 📈 Comparison of multiple datasets
- 📉 Identification of missing values and duplicates
- 📋 Summary statistics for numerical and categorical features
- 📊 Correlation analysis
- 📑 Exportable HTML reports

## 🔧 Prerequisites

- Python 3.10.15
- SweetViz library
- Web browser for viewing HTML reports

## 📥 Installation

1. Clone the repository:
```bash
git clone https://github.com/PreProd-Internship/DIY-Python-SweetViz
```

2. Create and activate a virtual environment (recommended). If using Conda:
```bash
conda create -n env_name python==3.10.15 -y
conda activate env_name
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Start the Streamlit application:
```bash
streamlit run source/app.py
```

2. Access the web interface at `http://localhost:8501`

3. Upload your CSV dataset and generate the EDA reports!

## 📁 Project Structure

```
DIY-Python-SweetViz/
    ├── data/
    │   └── retail_data.csv
    ├── source/
    │   ├── app.py
    │   ├── report.py
    │   └── split.py
    ├── .gitignore
    ├── LearnWithPrompts.md
    ├── README.md
    └── requirements.txt
```

## 🗃️ Data Description

### retail_data.csv

A mock dataset generated using [Mockaroo](https://mockaroo.com/) for learning purposes. The `retail_data.csv` file contains customer purchase data. Each row represents a single transaction with columns like

- `Username`,
- `Gender`,
- `PhoneNumber`,
- `ProductID`,
- `SatisfactionRating`, and so on.

> *Note: `SatisfactionRating` is the target variable (`target_column`) in this dataset.*

## 📚 Documentation

For detailed information about the project, please refer to:
- [SweetViz](https://pypi.org/project/sweetviz/) - SweetViz library's documentation
- [LearnWithPrompts.md](LearnWithPrompts.md) - Use your favourite LLM to learn more about SweetViz