import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
VIZ_DIR = ROOT / "visualizations"
VIZ_DIR.mkdir(parents=True, exist_ok=True)

def load_data():
    path = PROCESSED_DIR / "movies_merged.csv"
    return pd.read_csv(path)

def plot_revenue_vs_rating(df):
    plt.figure(figsize=(6, 4))
    plt.scatter(df["rating"], df["revenue"], alpha=0.3)
    plt.xlabel("IMDb rating")
    plt.ylabel("Worldwide revenue")
    plt.title("Revenue vs. Rating")
    plt.tight_layout()
    plt.savefig(VIZ_DIR / "revenue_vs_rating.png")
    plt.close()

def plot_revenue_by_genre(df):
    temp = df.copy()
    temp["main_genre"] = temp["genres"].astype(str).str.split("|").str[0]

    genre_rev = (
        temp.groupby("main_genre")["revenue"]
        .median()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(8, 4))
    genre_rev.plot(kind="bar")
    plt.ylabel("Median revenue")
    plt.title("Top 10 Genres by Median Revenue")
    plt.tight_layout()
    plt.savefig(VIZ_DIR / "revenue_by_genre.png")
    plt.close()

def plot_revenue_over_time(df):
    yearly = df.groupby("year")["revenue"].median()

    plt.figure(figsize=(8, 4))
    yearly.plot()
    plt.xlabel("Year")
    plt.ylabel("Median revenue")
    plt.title("Median Revenue Over Time")
    plt.tight_layout()
    plt.savefig(VIZ_DIR / "revenue_over_time.png")
    plt.close()

def main():
    df = load_data()
    plot_revenue_vs_rating(df)
    plot_revenue_by_genre(df)
    plot_revenue_over_time(df)
    print(f"Saved plots in {VIZ_DIR}")

if __name__ == "__main__":
    main()

