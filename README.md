
# Automated Web Scraping & Data Analysis Pipeline

A modular Python-based data engineering pipeline that automatically extracts, cleans, and analyzes structured e-commerce data from [Books to Scrape](http://books.toscrape.com/).

The project follows clean coding standards, separating raw HTML data extraction from tabular data analysis and terminal presentation.

---

## 📌 Features

* **Targeted Web Extraction:** Uses `BeautifulSoup4` with direct class targeting (`.instock`) and normalized text parsing (`.split()`) to extract titles, stock statuses, prices, and ratings clean of HTML noise.
* **Data Processing & Storage:** Converts raw extracted data into structured `pandas` DataFrames and exports clean CSV datasets.
* **Numeric Mapping & Filtering:** Maps textual ratings (`One` through `Five`) into numerical values for complex mathematical querying (e.g., filtering 5-star books under specific price thresholds).
* **Structured Terminal Output:** Uses custom f-string padding and alignment to render clean, tabular terminal views without raw, unformatted outputs.
* **Modular Architecture:** Built following DRY (*Don't Repeat Yourself*) principles with separated concerns (`main.py` for extraction, `analyzer.py` for analytical processing, and dedicated handler modules).

---

## 📁 Repository Structure

```text
automated-web-scraping-pipeline/
│
├── handlers/
│   ├── __init__.py
│   └── csv_handler.py        # Dataset export and filesystem logic
│
├── scraped_data/
│   └── all_books_output.csv  # Output dataset (generated upon execution)
│
├── analyze_books.py          # Data analysis, transformation, and custom table display
├── main.py                   # Main scraper orchestration entry point
├── .gitignore                # Excludes virtual environments and temporary configuration
└── README.md                 # Project documentation

```

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x
* **Scraping & Parsing:** `BeautifulSoup4`, `requests`
* **Data Manipulation & Analysis:** `pandas`

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone [https://github.com/zainabjameel577-oss/automated-web-scraping-pipeline.git](https://github.com/zainabjameel577-oss/automated-web-scraping-pipeline.git)
cd automated-web-scraping-pipeline

```

### 2. Install Dependencies

```bash
pip install pandas beautifulsoup4 requests

```

### 3. Run the Scraper

Generate the dataset from the live target site:

```bash
python main.py

```

### 4. Run the Data Analyzer

Perform data transformations, clean price conversions, and output filtered subsets:

```bash
python analyze_books.py

```

---

## 📊 Sample Output Format

When running the analysis pipeline, output tables are dynamically aligned in the terminal:

```text
Title: A Light in the Attic                     | Rating: Three  | Price: £51.77 | Stock: In stock
Title: Tipping the Velvet                       | Rating: One    | Price: £53.74 | Stock: In stock
--------------------------------------------------------------------------------------------------------------

```

---

## 🛡️ Best Practices Applied

* **Robust Data Cleaning:** String stripping and whitespace normalization occur during the initial scrape to avoid dirty imports down the line.
* **Safe Column Formatting:** Numerical parsing handles currency symbol removal smoothly for mathematical operations (`.loc[]` filtering).
* **Git Hygiene:** Unnecessary IDE metadata (`.idea/`) and output data logs are managed cleanly via `.gitignore`.

```

```