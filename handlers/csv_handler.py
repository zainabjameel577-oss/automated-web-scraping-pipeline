import os
import csv


def save_books_to_csv(book_data, folder_name="scraped_data", file_name="all_books_output.csv"):
    """Handles creating the directory and writing book data to a CSV file."""
    os.makedirs(folder_name, exist_ok=True)
    file_path = os.path.join(folder_name, file_name)

    fieldnames = ['Title', 'Rating', 'Price', 'Stock']

    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(book_data)

    print(f"Successfully saved {len(book_data)} books to {file_path}!")