
import requests
from bs4 import BeautifulSoup
from handlers.csv_handler import save_books_to_csv


BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

book_data = []
page_num = 1


with requests.Session() as session:
    while True:
        url = BASE_URL.format(page_num)
        print(f"Scraping page {page_num}...")

        try:

            response = session.get(url, timeout=15)


            if response.status_code == 404:
                print("Reached the end of the pages!")
                break

            response.raise_for_status()

        except requests.RequestException as error:
            print(f"Could not scrape {url}: {error}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        if not books:
            print("No book listings found. Stopping scraper.")
            break

        for book in books:
            # ADDED: Check that expected HTML elements exist before reading them.
            title_tag = book.find("h3")
            link_tag = title_tag.find("a") if title_tag else None
            rating_tag = book.find("p", class_="star-rating")
            price_tag = book.find("p", class_="price_color")
            stock_tag = book.find("p", class_="instock")

            if not all([link_tag, rating_tag, price_tag, stock_tag]):
                print("Skipping a book with missing information.")
                continue

            title = link_tag.get("title", "").strip()

            # FIXED: Extract the rating safely from the CSS classes.
            rating_classes = rating_tag.get("class", [])
            rating = (
                rating_classes[1]
                if len(rating_classes) > 1
                else ""
            )

            price = price_tag.get_text(strip=True).replace("Â", "")

            # FIXED: Normalize stock text, such as "In stock (22 available)".
            raw_stock = stock_tag.get_text(" ", strip=True).split()
            stock_availability = " ".join(raw_stock[:2])

            book_data.append({
                "Title": title,
                "Rating": rating,
                "Price": price,
                "Stock": stock_availability
            })

        page_num += 1

# FIXED: Save once after scraping finishes, not after every page.
save_books_to_csv(book_data)

print(f"Scraping finished. Total books collected: {len(book_data)}")
