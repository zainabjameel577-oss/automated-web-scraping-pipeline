import pandas as pd

def print_book_table(df_subset):
    """Helper function to print pandas subsets cleanly in a structured format."""
    for _, row in df_subset.iterrows():
        # Truncate long titles to 40 characters and left-align them, and include stock status
        print(f"Title: {row['Title'][:40]:<42} | Rating: {row['Rating']:<6} | Price: £{row['Clean_Price']:<6} | Stock: {row['Stock']}")
    print("-" * 110)

def analyze_books(file_path = "scraped_data/all_books_output.csv"):
    df = pd.read_csv(file_path)
    print(f"Successfully loaded {len(df)} books for analysis!\n")
    df['Clean_Price'] = df['Price'].str.replace('£', '').astype(float)

    rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    df['Numeric_Rating'] = df['Rating'].map(rating_map)
    df['Stock'] = df['Stock'].str.strip()

    print(f"\n------------3 Most expensive books-----------")
    expensive_books = df.sort_values(by = 'Clean_Price', ascending=False).head(3)
    print_book_table(expensive_books)

    print(f"\n------------books under 20 but five star ratings-----------")
    cheap_but_five = df[(df['Numeric_Rating'] == 'five') & (df['Clean_Price'] < 20)]
    print_book_table(cheap_but_five)

    print(f"\n------------books in stock and five star ratings-----------")
    stocked_and_five = df[(df['Numeric_Rating'] == 'five') & (df['Clean_Price'] > 20)]

    print(f"\n------------Sorted by names-----------")
    sorted_by_names = df.sort_values(by = 'Title', ascending = False).head()
    print_book_table(sorted_by_names)

    print(f"\n------------Sorted by Ratings-----------")
    sorted_by_ratings = df.sort_values(by = 'Rating', ascending = False).head()
    print_book_table(sorted_by_ratings)

    print(f"\n------------Sorted by Price-----------")
    sorted_by_price = df.sort_values(by = 'Clean_Price', ascending = False).head()
    print_book_table(sorted_by_price)

    print("\n------------ Mild-Priced, 5-Star, In-Stock Books ------------")
    mild_five_star_in_stock = df.loc[
        (df['Numeric_Rating'] == 5) &
        (df['Stock'] == 'In stock') &
        (df['Clean_Price'] < 20)
        ].head(7)
    print_book_table(mild_five_star_in_stock)

if __name__ == "__main__":
    analyze_books()





