
from pathlib import Path
import pandas as pd


def print_book_table(df_subset):
    """Print book information in a readable format."""

    if df_subset.empty:
        print("No books matched this filter.")
        print("-" * 110)
        return

    for _, row in df_subset.iterrows():
        title = str(row["Title"])[:40]

        print(
            f"Title: {title:<42} | "
            f"Rating: {str(row['Rating']):<6} | "
            f"Price: £{row['Clean_Price']:<6.2f} | "
            f"Stock: {row['Stock']}"
        )

    print("-" * 110)


def analyze_books(file_path="scraped_data/all_books_output.csv"):

    if not Path(file_path).exists():
        print(f"CSV file not found: {file_path}")
        print("Run main.py first to generate the CSV.")
        return

    df = pd.read_csv(file_path)

    print(f"Successfully loaded {len(df)} books for analysis!\n")

    required_columns = {"Title", "Rating", "Price", "Stock"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        print(f"Missing columns: {', '.join(sorted(missing_columns))}")
        return

    df["Clean_Price"] = pd.to_numeric(
        df["Price"]
        .astype(str)
        .str.replace("£", "", regex=False)
        .str.replace("Â", "", regex=False)
        .str.strip(),
        errors="coerce"
    )

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    df["Numeric_Rating"] = df["Rating"].map(rating_map)

    df["Stock"] = (
        df["Stock"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    print("\n------------ 3 Most Expensive Books ------------")

    expensive_books = df.sort_values(
        by="Clean_Price",
        ascending=False
    ).head(3)

    print_book_table(expensive_books)

    print("\n------------ Five-Star Books Under £20 ------------")

    cheap_but_five = df[
        (df["Numeric_Rating"] == 5) &
        (df["Clean_Price"] < 20)
    ]

    print_book_table(cheap_but_five)

    print("\n------------ Five-Star Books In Stock ------------")

    stocked_and_five = df[
        (df["Numeric_Rating"] == 5) &
        (df["Stock"] == "in stock")
    ]

    print_book_table(stocked_and_five)


    print("\n------------ Titles Sorted A-Z ------------")


    sorted_by_names = df.sort_values(
        by="Title",
        ascending=True
    ).head()

    print_book_table(sorted_by_names)


    print("\n------------ Highest-Rated Books ------------")


    sorted_by_ratings = df.sort_values(
        by=["Numeric_Rating", "Title"],
        ascending=[False, True]
    ).head()

    print_book_table(sorted_by_ratings)


    print("\n------------ Highest-Priced Books ------------")

    sorted_by_price = df.sort_values(
        by="Clean_Price",
        ascending=False
    ).head()

    print_book_table(sorted_by_price)


    print("\n------------ Affordable, Five-Star, In-Stock Books ------------")

    mild_five_star_in_stock = df.loc[
        (df["Numeric_Rating"] == 5) &
        (df["Stock"] == "in stock") &
        (df["Clean_Price"] < 20)
    ].head(7)

    print_book_table(mild_five_star_in_stock)


if __name__ == "__main__":
    analyze_books()





