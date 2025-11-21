# Milestone 3 – Interim Status Report  
**Project:** Factors Influencing Movie Success  
**Team:** Lucas Washor (Lwashor02), Max Washor (Mwashor2)

---

## 1. Overview

Our project looks at how different movie characteristics relate to box office success. We are combining two datasets:
one with IMDb-style information about movies (genre, runtime, ratings, etc.) and another dataset with box office revenue from 2000–2024.
By merging these two sources, we want to see which factors actually seem connected to financial performance and whether certain trends appear across time.

Our research questions from the project plan are still the same:

1. How have movie characteristics (genre, runtime, ratings) correlated with box office performance over time?
2. Do specific genres or production features tend to do better in certain years or decades?
3. How do user ratings compare to box office results?
4. Can we identify any patterns that might help predict revenue?

This report explains what we’ve completed so far, what’s still in progress, updates to our timeline, and any changes to our original plan.

---

## 2. Progress Update by Task

Below is an update on each major task from our project plan.

---

### **2.1 Data Acquisition – Status: Completed**

**What we’ve done:**

- We downloaded the IMDb dataset and the Box Office dataset from Kaggle.
- We are adding both raw files to our GitHub repository as part of this milestone.
- We quickly reviewed each dataset to understand what columns they have and what years they cover.

These files are now ready for cleaning and integration.

---

### **2.2 Data Cleaning – Status: In Progress**

**What we’ve done so far:**

- Loaded both datasets into Python and looked at the basic structure.
- Cleaned some initial issues such as:
  - Converting numeric columns to the correct types.
  - Lowercasing and trimming movie titles for consistency.
  - Filtering out rows with missing or invalid year information.
- Started looking at extreme outliers in revenue and ratings.

**What still needs to be done:**

- Need to actually finish cleaning missing values (especially revenue).
- We need to ecide how to handle duplicated or inconsistent movie titles.
- Create finalized “clean” versions of both datasets before merging.

---

### **2.3 Data Integration – Status: In Progress**

**What we’ve done so far:**

- We tried an initial merge using movie title + release year.
- We found that some titles don’t match exactly between datasets (punctuation, extra words, etc.).
- We created a first version of a merged dataset using exact matches only.

**Next steps:**

- We have to decide whether to keep only exact matches or apply simple normalization before merging.
- We also need to check how many movies are lost during the merge and whether it affects our analysis.
- Finalize and document the merging approach.

---

### **2.4 Interim Status Report – Status: Completed**

- Built this StatusReport.md file.
- Collected progress updates from both team members.
- Documented what tasks are done, in progress, and still ahead.
- Prepared the repository so that everything done so far is pushed and organized.

---

### **2.5 Analysis and Visualization – Status: Not Started (Early Exploration Only)**

**Early steps completed:**

- Created a few basic exploratory charts (revenue distributions, rating distributions) just to understand the data.

**Main work still ahead:**

- Investigate relationships between:
  - Genre and revenue
  - Runtime and revenue
  - Ratings and revenue
- Look at changes across years or decades.
- Create visuals like:
  - Scatterplots of rating vs. revenue
  - Bar charts of revenue by genre
  - Trend lines for revenue over time

We can actually start this stuff in full once the merge is finalized.

---

### **2.6 Workflow Automation – Status: Not Started**

**Plan:**

- Create:
  - A simple Python “run-all” script
- Automate steps:
  1. Clean data  
  2. Merge data  
  3. Run analysis  
  4. Produce final visualizations  

The goal is to make the project reproducible from start to finish.

---

### **2.7 Final Report & Documentation – Status: Not Started**

This will happen at the end of the project when we've completed every step neccesary. We will include:

- A summary of our cleaning and merging steps
- The key findings from our analysis
- Visualizations with explanations
- Limitations and future questions
- Updated README instructions

---

## 3. Updated Timeline

| Task | Original Dates | Status | Updated Completion |
|------|----------------|--------|--------------------|
| Data Acquisition | Oct 16–22 | Completed | Done |
| Data Cleaning | Oct 23–29 | In Progress | Expected to finish soon |
| Data Integration | Oct 30–Nov 6 | In Progress | Expected soon after cleaning |
| Interim Status Report | Nov 7–11 | Completed | Done |
| Analysis & Visualization | Nov 12–24 | Not Started/Early | Will begin once merge is finalized |
| Workflow Automation | Nov 25–Dec 1 | Not Started | Expected early December |
| Final Report & Documentation | Dec 2–8 | Not Started | Will complete before final deadline |
| Final Project Submission | Dec 10 | Not Started | On schedule |

---

## 4. Changes to the Project Plan

So far, most of our project plan has stayed the same, but a few small adjustments were necessary:

- **Merging the datasets is trickier than expected.**  
  Because there are title differences, it means we may lose some movies if we only keep exact matches. So, we are trying to find a balance between accuracy and also keeping enough data.
  
- **Predictive modeling may be optional.**  
  If time allows, we’ll build a simple prediction model, but the main focus will just be on analysis and visual trends.


No major changes to research questions or datasets so far.

---

## 5. Challenges and Things We’re Still Figuring Out

- **Matching movie titles**  
  Some movies appear slightly differently in each dataset, so we need to choose a good matching strategy.

- **Outliers in revenue**  
  Box office revenue is very skewed, so we have to find the best way to deal with that. We might use a log transformation for analysis or find a different method to have an efficient and interpretable analysis.

- **Year coverage**  
  The IMDb dataset covers more years than the box office dataset, so our merged data will mainly focus on 2000–2024.

- **Inflation adjustment**  
  Adjusting revenue for inflation is ideal but we also think it may be too big to include in this project’s scope.

---

## 6. Contribution Summary (Each Team Member Writes Their Own)

### **6.1 Lucas Washor (Lwashor02)**  
For this milestone, I worked mainly on acquiring the datasets and beginning the cleaning process. I downloaded the datasets, added them to our repo, and wrote the first cleaning scripts to standardize formats and inspect missing values. I also helped write and organize this status report.



---

_End of Status Report_
