
# Automated Web Scraping & Data Analysis Pipeline

A Python project that scrapes book information from
[Books to Scrape](https://books.toscrape.com/), saves the
results to CSV, and analyzes the collected data using pandas.

## Features

- Extracts book titles, ratings, prices, and stock status.
- Saves scraped data to a CSV file.
- Converts prices and ratings into numeric values.
- Filters five-star books by price and stock status.
- Sorts books by title, rating, and price.
- Separates scraping, CSV storage, and analysis into modules.

## Project Structure

```text
automated-web-scraping-pipeline/
├── handlers/
│   ├── __init__.py
│   └── csv_handler.py
├── scraped_data/
│   └── all_books_output.csv
├── main.py
├── analyze_books.py
├── requirements.txt
├── .gitignore
└── README.md
```

The `scraped_data` folder and CSV are generated when the scraper runs.

## Technologies

- Python
- Requests
- BeautifulSoup
- pandas
- CSV

## Installation

Install the dependencies in your Python environment:

```bash
pip install -r requirements.txt
```

## How to Run

### Step 1: Scrape the books

Run `main.py`.

The scraper collects book information and creates:

`scraped_data/all_books_output.csv`

### Step 2: Analyze the results

Run `analyze_books.py`.

The analyzer displays:

- Three most expensive books
- Five-star books under £20
- Five-star books in stock
- Titles sorted alphabetically
- Highest-rated books
- Highest-priced books
- Affordable five-star books in stock

## Data Fields

| Field | Description |
|---|---|
| Title | Book title |
| Rating | Rating from One to Five |
| Price | Book price |
| Stock | Stock availability |

## Notes

This project uses Books to Scrape, a demonstration website
intended for scraping practice.

Generated CSV files are excluded from Git by default.
A small sample dataset can be added to the repository if
you want to demonstrate the output.
