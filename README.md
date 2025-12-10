# Factors Influencing Movie Success

## Contributors
- Lucas Washor (Lwashor02)
- Max Washor (Mwashor2)

## Summary

This project explores the factors that influence movie success by examining how different movie characteristics relate to worldwide box office revenue. We combined two datasets: one containing IMDb-style metadata about movies (such as genre, runtime, and user ratings) and another containing worldwide box office revenue data from 2000 to 2024. By merging these datasets, our goal was to better understand which features of movies appear to be associated with stronger financial performance and how these relationships change over time.

We were motivated by the idea that movie success is often discussed using both critical opinions (ratings and reviews) and financial outcomes (box office revenue), but these two measures do not always align. Some movies receive high critical praise but do not perform well financially, while others are commercial hits despite average ratings. This project gave us a way to examine that disconnect using real-world data and to explore whether any consistent patterns emerge when looking at thousands of movies across multiple decades.

Our main research questions remained consistent throughout the project. First, how do movie characteristics such as genre, runtime, and IMDb rating correlate with box office performance over time? Second, do certain genres or production features tend to perform better financially than others? Third, how closely do user ratings align with revenue, and can ratings alone explain commercial success? Finally, can we identify any broader trends across different years that might help explain shifts in movie revenue?

To answer these questions, we built a reproducible data workflow using Python. We began by cleaning each dataset individually to standardize formats, correct data types, remove missing values, and normalize movie titles. We then merged the datasets using a combination of cleaned movie titles and release years, which resulted in a final merged dataset of 2,095 movies with both metadata and revenue information. This allowed us to directly compare ratings, genres, and release years against worldwide revenue.

After producing the merged dataset, we generated several visualizations to explore the relationships within the data. These included a scatterplot of revenue versus IMDb rating, a bar chart showing median revenue by genre, and a line chart showing median revenue over time. Together, these visualizations helped us identify patterns and evaluate how different factors contribute to financial performance.

Overall, our findings suggest that movie success is influenced by multiple factors rather than any single variable. Higher IMDb ratings tend to be associated with higher revenue on average, but the relationship is weak and highly variable. Certain genres consistently show higher median revenue than others, which reflects differences in production budgets, audience size, and distribution scale. Revenue also varies significantly from year to year, likely reflecting shifts in industry trends, major franchise releases, and broader economic conditions. These results reinforce the idea that box office success is multi-dimensional and cannot be predicted by ratings or genre alone.

Beyond the findings themselves, this project also emphasized building a transparent and reproducible data workflow. By documenting each step of the cleaning, merging, and visualization process and automating the workflow with Python scripts, we ensured that our results can be independently reproduced and verified. This focus on reproducibility shaped how we organized our data, code, and documentation and reflects a core goal of the project.

## Data Profile

Our project uses two primary datasets that were combined into a single merged dataset for analysis. The first dataset, `movie_metadata.csv`, contains IMDb-style metadata for a large collection of movies. This dataset includes information such as movie titles, release years, genres, runtimes, IMDb user ratings, budgets, number of user votes, and several popularity indicators such as Facebook likes for actors and films. Each row represents one movie, and the most important fields for our analysis were the movie title (`movie_title`), release year (`title_year`), genres (`genres`), runtime (`duration`), and IMDb rating (`imdb_score`).

The second dataset, `enhanced_box_office_data(2000-2024)u.csv`, contains worldwide box office revenue information for movies released between 2000 and 2024. Key fields in this dataset include the movie title (`Release Group`), the release year (`Year`), and worldwide revenue (`$Worldwide`). We treated worldwide revenue as our main measure of commercial success. Because this dataset only covers movies from 2000–2024, our final merged dataset is effectively limited to that same time window.

To integrate the two datasets, we standardized the movie titles in both files by converting them to lowercase and trimming extra whitespace, creating a new field called `title_clean`. We then merged the datasets using `title_clean` and `year`. Before merging, we also dropped rows that were missing critical fields such as title, year, or revenue. After cleaning and merging, the final processed dataset contained 2,095 movies with both metadata and revenue information. This merged dataset is saved as `data/processed/movies_merged.csv` and serves as the main input for our analysis and visualizations.

From a legal and ethical perspective, both datasets originate from third-party sources that compile publicly available IMDb and box office data. We do not claim ownership over the original data. The data does not include direct personal identifiers; instead, it contains information about films, reviews, and financial outcomes. However, the datasets reflect industry-level and platform-level biases. For example, movies that are independently produced, international, or digitally released may be underrepresented. We document these limitations as part of our project’s transparency goals.

For reproducibility, the raw input datasets are stored in `data/raw/`, while the cleaned and merged output is stored in `data/processed/`. Our processed dataset is also uploaded to Box so that others can reproduce our analysis without needing to manually download the raw files.

Both datasets were obtained from Kaggle rather than directly from the original data providers (such as IMDb or box office aggregators) due to ease of access and standardized formatting. Kaggle was used as a secondary distribution platform that hosts curated versions of publicly available data. While redistribution of raw Kaggle datasets is restricted by their platform terms, our project only shares a derived processed dataset for academic use. We acknowledge that the original data licensing ultimately governs reuse and that Kaggle acts as a hosting intermediary rather than the primary data owner.

We also designed the project’s file structure and version control strategy to support long-term reproducibility. All raw data files were stored in the data/raw/ directory and left unmodified to ensure that no preprocessing steps alter the integrity of the original inputs. Cleaned and merged datasets were saved separately in data/processed/ to create a clear lineage of transformations. This separation prevents accidental overwriting and makes it easy for others to retrace the workflow from start to finish. In addition, the use of GitHub allowed us to track changes in our code and documentation over time, maintain transparency regarding updates or corrections, and provide a centralized space for collaborators to review the workflow. This structured organization supports both internal reproducibility and external verification of our methods.

## Data Quality

Several data quality issues were present in both original datasets and required careful handling before merging. In the IMDb-style metadata dataset, some movies were missing release years, runtimes, or IMDb ratings. Rows that were missing a title or release year were dropped because those fields are required for merging. In addition, numeric columns such as runtime, year, and rating needed to be explicitly cast to appropriate data types to ensure consistent analysis.

In the box office dataset, some records contained missing or zero values for worldwide revenue. Because revenue is our primary outcome variable, rows without valid revenue values were removed. This filtering step reduces the total number of movies but ensures that the remaining records represent legitimate financial outcomes rather than placeholders or incomplete entries.

One of the largest data quality challenges involved matching movie titles between the two datasets. Titles were often formatted differently across sources due to punctuation, capitalization, or small naming variations. To address this, we created a cleaned version of the movie title (`title_clean`) in both datasets by stripping whitespace and converting all text to lowercase. We then merged using both `title_clean` and release year. This approach improved matching accuracy but still may exclude some valid matches where titles differ more substantially.

Beyond the technical problems like mismatched or inconsistent titles, the datasets also come with broader sources of bias that can shape our results. The IMDb-style metadata tends to overrepresent movies that generate a lot of online activity, which usually means Hollywood releases or films with large fan communities. Smaller independent films, many international titles, and movies with limited theatrical runs often show up far less or not at all. The box office dataset has similar gaps because it mainly includes films with publicly reported revenue, so movies that go straight to streaming or have very small releases may be missing. These gaps can tilt the dataset toward higher-budget, mainstream productions, which may inflate what looks “typical” in terms of revenue and limit how representative our genre comparisons are. IMDb ratings themselves can also reflect demographic biases in who chooses to rate certain movies, which may influence average scores.

These data quality issues affect how we should interpret the patterns we see. Since the merged dataset mostly includes widely released and financially successful films, our conclusions apply more to commercial, mainstream movies than to the full range of films produced each year. Missing revenue data and the absence of streaming-only titles mean that some recent industry changes may not be captured. The process of matching titles can also lead to losing some valid entries, which reduces the sample size and may create small shifts in comparisons across years. In the future, a stronger workflow could include fuzzy matching techniques, pulling metadata from APIs, or incorporating different data sources to limit these problems. Even with these limitations, the dataset remains broad enough to provide useful insights into general trends in movie performance.

Another major quality issue is the extreme skew in box office revenue. A small number of blockbuster films earn very large revenue values, while most films earn far less. This skew makes average revenue misleading in many cases, so our visualizations focus on medians rather than means when comparing revenue across genres and over time. We chose this approach to reduce the influence of extreme outliers while still representing overall trends.

Finally, the merged dataset is not a complete record of all movies produced between 2000 and 2024. It only includes films that appear in both the IMDb metadata dataset and the box office dataset. As a result, smaller independent films, limited international releases, and movies without reported revenue are underrepresented. We document this as an important limitation of our analysis.

## Findings

Using the merged dataset of 2,095 movies, we explored three main relationships: revenue versus IMDb rating, median revenue by genre, and median revenue over time. The scatterplot of revenue versus IMDb rating shows a weak positive relationship. On average, higher-rated movies tend to earn more revenue, but the spread is very wide. There are many movies with moderate ratings that perform extremely well financially, as well as some highly rated films that generate relatively low revenue. This suggests that ratings alone are not a strong predictor of box office success.

When examining revenue by genre, we used the first listed genre for each movie as its primary category. We found that certain genres typically associated with large-scale productions, such as action and adventure-style categories, tend to have the highest median revenue. Genres associated with smaller productions, such as drama and comedy, generally show lower median revenue. This aligns with expectations about production budgets, target audiences, and distribution scale.

The time-series visualization of median revenue by year shows that revenue fluctuates substantially over time. Some years feature noticeably higher median revenue, likely corresponding to strong franchise releases or particularly successful movie lineups. Because we used nominal revenue values, some of this trend may also reflect inflation and changes in global movie markets rather than only differences in movie quality or popularity.

Overall, the findings indicate that movie success is multi-dimensional. Genre clearly plays a role in financial outcomes, and ratings are loosely associated with revenue, but neither variable alone explains box office performance. Release timing and broader industry trends also appear to strongly influence revenue outcomes.

## Future Work

There are several ways this project could be expanded in future work. One major improvement would be adjusting box office revenue for inflation. All revenue values in our current analysis are nominal, which means that year-to-year comparisons are affected by changes in ticket prices and overall economic conditions. Applying inflation-adjusted revenue would allow for more meaningful comparisons across time.

Future work could also explore more advanced modeling approaches. Instead of relying only on visual comparisons, a regression-based model could be built using features such as runtime, budget, genre, and IMDb ratings to predict revenue. This would allow us to quantify the relative importance of different features more precisely.

Another possible extension would involve including more international data or streaming-related performance metrics. Many modern movies generate significant revenue from streaming platforms rather than traditional box office releases. Incorporating streaming viewership data would provide a more complete picture of movie success in the modern media environment.

Finally, future versions of this project could explore more granular genre categories, franchise effects, or the role of major actors and directors. Features such as cast popularity and prior box office performance could help explain why certain movies outperform others even when their ratings are similar.

## Reproducing

To reproduce this project from scratch, follow these steps:

1. Clone the project repository from GitHub.
2. Ensure you have Python installed (version 3.9+ recommended).
3. Install required dependencies:
   ```bash
   pip install pandas matplotlib

The full Python environment used for this project is recorded in `pip_freeze.txt`, and core dependencies are listed in `requirements.txt`.


## Contribution Statement

Lucas Washor did most of the technical implementation of the project, including data cleaning, dataset integration, creation of visualization scripts, and execution of the full reproducible workflow. Max Washor primarily focused on the written components of the project, including the data quality assessment, findings interpretation, and future work discussion. Both collaborators contributed to each other’s main focus of the project whenever needed, and both contributed to project planning, review, and final edits.


## References

IMDb-style Movie Metadata Dataset. Kaggle.

Enhanced Box Office Revenue Dataset (2000–2024). Kaggle.

McKinney, W. (2010). Data Structures for Statistical Computing in Python. Proceedings of the 9th Python in Science Conference.

Hunter, J. D. (2007). Matplotlib: A 2D Graphics Environment. Computing in Science & Engineering.


## Box Data Access

The processed merged dataset (`movies_merged.csv`) is available via Box at the following link:

[https://uofi.box.com/s/6to6nvbej27rltilcwix99cnwn8c2bhk]

After downloading, place the file into the `data/processed/` directory before running the visualization scripts.

