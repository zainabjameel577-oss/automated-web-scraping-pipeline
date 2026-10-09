import requests
from bs4 import BeautifulSoup
from handlers.csv_handler import save_books_to_csv

book_data = []
page_num = 1

while True:
    url = f"http://books.toscrape.com/catalogue/page-{page_num}.html"
    print(f"Scraping page {page_num}...")

    response = requests.get(url)

    # Stop the loop if we hit a page that doesn't exist
    if response.status_code != 200:
        print("Reached the end of the pages!")
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.find('h3').find('a')['title'].strip()
        rating = book.find('p', class_='star-rating').get('class')[1]
        price = book.find('p', class_='price_color').text.strip().replace('Â', '')
        raw_stock = book.find('p', class_='instock').text.split()
        stock_availability = f"{raw_stock[0]} {raw_stock[1]}"

        book_data.append({
            'Title': title,
            'Rating': rating,
            'Price': price,
            'Stock': stock_availability
        })

    page_num += 1

    save_books_to_csv(book_data)