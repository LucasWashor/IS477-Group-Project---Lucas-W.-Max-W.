# Overview

The first thing we wanted to do was find a good dataset. We both agreed that we want this project to not only be useful and showcase the abilities we learned in this class, but to also be interesting and fun to do. In the past, we both agreed that we seem to use similar datasets (often about sports) and wanted to focus on another shared interest. We watch a good amount of movies so we decided that doing a project about movies and learning how different factors influenced their success would be super insightful. In this project we will specifically be looking at how characteristics like genre, runtime, ratings, and production details, influence box office performance over time. We identified 2 strong and detailed datasets that look helpful for us to answer these questions. By merging a dataset with IMDB movies with a dataset about Movies in the box office we can create one combined dataset that includes multiple decades and includes both audience ratings as well as financial success. This type of study will help us understand how there were most likely certain historical correlations and trends that affected commercial success, and what they were. We hope that by developing these predictive models we might be able to leverage the IMDb ratings and certain movie characteristics to try and forecast their box office performance. By carrying out this study, we want to be able to look at which factors actually had an existent role in affecting the total revenue, viewer ratings, etc. It will also be interesting to see how they changed over the course of time depending on economic factors, cultural trends, etc. Ultimately, this project provides a richer, data-driven understanding of what drives movie success in both historical and predictive contexts.


# Research Question(s)
**Purpose:** These questions are designed to explore both historical trends and predictive insights. By examining correlations, genre-specific patterns, audience versus financial reception, and predictive relationships, we can gain a deeper understanding of the factors that contribute to movie success.


1. How have movie characteristics (genre, runtime, rating) correlated with box office performance over time? (we have a general estimate of things in mind, like the most recent epidemic Covid, or maybe when the US was having economic trouble)
2. Do specific genres or production characteristics tend to perform better in certain decades?
(this is rather researchable, but looking at the evidence can help prove theories true or false)
3. How do audience ratings (IMDb) compare to financial success (box office revenue)?
4. Can we identify patterns or predictive relationships between IMDb data and box office results?

# Team
**Team Members:**
- **Lucas Washor (Lwashor02)** : Will focus on data acquisition, cleaning, and documentation.
- **Max Washor (Mwashor2)** : WIll focus on data integration, analysis, and visualization.

# Datasets
We will integrate two distinct, trustworthy datasets with different formats and access methods:

1.**IMDB 5000 Movie Dataset**
source(https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset)

2. **Movies Box office Dataset (2000-2024)**
source(https://www.kaggle.com/datasets/aditya126/movies-box-office-dataset-2000-2024?utm_source=chatgpt.com)

**Integration Plan:**  
Our plan is for the datasets to be merged using a common field such as movie title and release year. After that we can perform any sort of cleaning necessary to handle title mismatches and duplicates. Once integrated, we then will analyze the dataset to find relationships between movie attributes and revenue trends.

# Timeline

Oct 16–22 [Data Acquisition]:  Download IMDb and box office datasets; document metadata and licenses. (Lucas focused)
Oct 23–29 [Data Cleaning]:  Clean missing values, normalize titles, and handle outliers in revenue/rating data. (Lucas focused)
Oct 30–Nov 6 [Data Integration]:  Merge datasets and validate joins using Python (Pandas). (Max focused)
Nov 7–11 [Interim Status Report]: Submit progress report to GitHub with updated findings and timeline. (Both)
Nov 12–24 [Analysis and Visualization]: Explore relationships across decades, generate summary statistics and graphs. (Max focused)
Nov 25–Dec 1 [Workflow Automation]: Create reproducible workflow (Snakemake or Run-All script). (Both)
Dec 2–8 [Final Report and Documentation]: Finalize README.md with results, citations, and metadata. (Both)
Dec 10 [Final Project Submission]: Push release and share Box folder link. | Both |

# Constraints
- Some datasets may have licensing restrictions or require scraping/cleaning due to formatting inconsistencies.
- Matching titles across datasets may cause alignment challenges due to different naming conventions and release years.
- Box office data from the past may be incomplete, estimated, or not adjusted for inflation, which could affect accuracy.
- External factors (cultural trends, economic conditions, etc.) may influence results in ways not captured by the datasets.


# Gaps
- We are still determining the best combination and merging strategy of IMDb and box office datasets to cover all years.
- We will need to find the best method to handle inflation-adjusted revenue to compare revenues across time.
- We may need guidance (from professor or additional research) on workflow automation, preprocessing pipelines, and reproducibility documentation format.
