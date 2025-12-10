import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def load_data():
    imdb_path = RAW_DIR / "imdb_movies.csv"      # TODO: change to your actual filename
    box_office_path = RAW_DIR / "box_office.csv" # TODO: change to your actual filename

    imdb = pd.read_csv(imdb_path)
    box = pd.read_csv(box_office_path)
    return imdb, box

def clean_imdb(imdb: pd.DataFrame) -> pd.DataFrame:
    # TODO: update column names to match your dataset
    imdb = imdb.copy()
    imdb = imdb.rename(columns={
        "title": "title",       # or "movie_title"
        "year": "year",         # or "title_year"
        "genres": "genres",
        "duration": "runtime",
        "imdb_score": "rating"  # or your rating column
    })

    imdb = imdb.dropna(subset=["title", "year"])
    imdb["year"] = imdb["year"].astype(int)

    imdb["title_clean"] = (
        imdb["title"].astype(str).str.strip().str.lower()
    )

    return imdb

def clean_box_office(box: pd.DataFrame) -> pd.DataFrame:
    # TODO: update column names to match your dataset
    box = box.copy()
    box = box.rename(columns={
        "title": "title",
        "year": "year",
        "worldwide_gross": "revenue"  # or "revenue" / "box_office"
    })

    box = box.dropna(subset=["title", "year", "revenue"])
    box["year"] = box["year"].astype(int)

    box["title_clean"] = (
        box["title"].astype(str).str.strip().str.lower()
    )

    # Remove negative or nonsense revenue
    box = box[box["revenue"] > 0]

    return box

def merge_datasets(imdb: pd.DataFrame, box: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        imdb,
        box[["title_clean", "year", "revenue"]],
        on=["title_clean", "year"],
        how="inner",
        suffixes=("_imdb", "_box")
    )

    return merged

def main():
    imdb, box = load_data()
    imdb_clean = clean_imdb(imdb)
    box_clean = clean_box_office(box)
    merged = merge_datasets(imdb_clean, box_clean)

    out_path = PROCESSED_DIR / "movies_merged.csv"
    merged.to_csv(out_path, index=False)
    print(f"Saved merged dataset to {out_path}")
    print(f"Rows in merged dataset: {len(merged)}")

if __name__ == "__main__":
    main()

