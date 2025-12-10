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
