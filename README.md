# 📊 Data Science Job Market Analyzer

A Python-based data analysis and interactive dashboard project that explores Data Science job postings to identify **hiring trends, job titles, locations, companies, salaries, industries, company ratings, and in-demand technical skills**.

The project uses **Pandas, NumPy, Matplotlib, Seaborn, WordCloud, and Streamlit** to perform data cleaning, exploratory data analysis, visualization, and interactive job-market analysis.

---

##  Project Overview

The **Data Science Job Market Analyzer** analyzes a dataset of Data Science job postings and converts raw job-market data into meaningful visual insights.

The project follows an end-to-end workflow:

**Raw Job Data → Data Cleaning → Exploratory Data Analysis → Feature Analysis → Visualization → Interactive Streamlit Dashboard**

The Streamlit dashboard allows users to filter job postings by **location** and explore different aspects of the job market.

---

## 🎯 Objectives

* Analyze Data Science job postings.
* Identify the most common Data Science job titles.
* Find locations with the highest number of job postings.
* Identify companies hiring Data Science professionals.
* Analyze company ratings and company sizes.
* Explore industries and sectors hiring Data Scientists.
* Analyze salary estimates.
* Identify commonly demanded technical skills.
* Visualize job-market patterns through charts.
* Provide an interactive dashboard for exploring the cleaned dataset.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* WordCloud
* Streamlit

### Development Tools

* Jupyter Notebook
* VS Code
* Git / GitHub

---

## 📁 Project Structure

```text
Data Science Job Market Analyzer/
│
├── app.py
├── DataScienceJobMarketAnalyzer.ipynb
├── DataScientist.csv
├── cleaned_jobs.csv
├── cleaned_datascience_jobs.csv
└── README.md
```

### File Description

| File                                 | Description                                                                             |
| ------------------------------------ | --------------------------------------------------------------------------------------- |
| `app.py`                             | Streamlit application for the interactive dashboard                                     |
| `DataScienceJobMarketAnalyzer.ipynb` | Data cleaning, exploratory analysis, skill analysis, salary analysis and visualizations |
| `DataScientist.csv`                  | Original job-posting dataset                                                            |
| `cleaned_jobs.csv`                   | Intermediate cleaned dataset                                                            |
| `cleaned_datascience_jobs.csv`       | Dataset used by the Streamlit dashboard                                                 |

---

## 🔍 Data Analysis Performed

### 1. Data Cleaning

The project performs preprocessing operations including:

* Dataset inspection
* Missing-value analysis
* Duplicate detection
* Duplicate removal
* Removal of unnecessary columns
* Salary data cleaning
* Conversion of salary values into numerical values

---

### 2. Job Title Analysis

The project identifies the **top 10 most frequently occurring job titles** in the dataset.

---

### 3. Hiring Location Analysis

The project analyzes job postings by location to identify the locations with the highest number of opportunities.

---

### 4. Company Analysis

The project analyzes:

* Top hiring companies
* Company ratings
* Company size
* Ownership type
* Revenue distribution

---

### 5. Industry and Sector Analysis

The project examines the industries and sectors represented in the job postings and identifies the most frequently occurring categories.

---

### 6. Technical Skill Analysis

The project searches job descriptions for commonly requested Data Science and technology skills, including:

* Python
* SQL
* R
* Excel
* Tableau
* Power BI
* AWS
* Azure
* Spark
* Hadoop
* TensorFlow
* PyTorch
* Machine Learning
* Deep Learning
* Statistics
* Pandas
* NumPy
* Scikit-learn

The results are used to identify the skills appearing most frequently in the job descriptions.

---

### 7. Job Description Word Cloud

A WordCloud is generated from the job descriptions to provide a visual representation of frequently occurring terms.

---

### 8. Salary Analysis

Salary estimates are processed to calculate:

* Minimum salary
* Maximum salary
* Average salary

The project also analyzes:

* Average salary distribution
* Average salary by job title
* Average salary by location

---

### 9. Correlation Analysis

A correlation heatmap is generated using numerical columns in the dataset to explore relationships between numerical variables.

---

## 📊 Interactive Streamlit Dashboard

The project includes an interactive dashboard built with **Streamlit**.

The dashboard provides:

* Total job postings
* Average company rating
* Total companies
* Average salary
* Top job titles
* Top hiring locations
* Top hiring companies
* Company rating distribution
* Company size distribution
* Top industries
* Dataset preview

### Location Filter

Users can select a location from the sidebar to filter the dashboard and analyze job postings for the selected location.

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Open the Project Folder

```bash
cd "Data Science Job Market Analyzer"
```

### 3. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn streamlit wordcloud
```

### 4. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 Key Features

* ✅ Data cleaning and preprocessing
* ✅ Exploratory Data Analysis
* ✅ Job title analysis
* ✅ Hiring location analysis
* ✅ Company analysis
* ✅ Industry and sector analysis
* ✅ Technical skill analysis
* ✅ Salary analysis
* ✅ WordCloud visualization
* ✅ Correlation analysis
* ✅ Interactive Streamlit dashboard
* ✅ Location-based filtering

---

## 📚 Skills Demonstrated

This project demonstrates practical experience with:

* Python programming
* Pandas
* NumPy
* Data cleaning
* Exploratory Data Analysis
* Data visualization
* Statistical analysis
* Data processing
* Streamlit application development
* Dashboard development
* Working with CSV datasets
* Technical skill extraction from job descriptions

---

## 🔮 Future Improvements

Possible future enhancements include:

* Adding more recent job-posting datasets
* Adding additional dashboard filters
* Adding interactive salary comparisons
* Adding job-title search functionality
* Adding skill-based job filtering
* Adding geographic visualizations
* Adding automated dataset updates
* Deploying the dashboard online

---

## 👩‍💻 Author

**Nalluri Sai Pragathi**

B.Tech Computer Science and Engineering

