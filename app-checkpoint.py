import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------
# Page Configuration
# ----------------------------------------
st.set_page_config(
    page_title="Data Science Job Market Analyzer",
    page_icon="📊",
    layout="wide"
)

# ----------------------------------------
# Load Dataset
# ----------------------------------------
df = pd.read_csv("cleaned_datascience_jobs.csv")

# ----------------------------------------
# Sidebar
# ----------------------------------------
st.sidebar.title("📌 Filters")

locations = ["All"] + sorted(df["Location"].dropna().unique().tolist())

selected_location = st.sidebar.selectbox(
    "Select Location",
    locations
)

if selected_location == "All":
    filtered_df = df
else:
    filtered_df = df[df["Location"] == selected_location]

# ----------------------------------------
# Title
# ----------------------------------------
st.title("📊 Data Science Job Market Analyzer")
st.markdown(
    "Analyze hiring trends, salaries, companies, locations and other insights from Data Science job postings."
)

# ----------------------------------------
# Dashboard Metrics
# ----------------------------------------
st.subheader("📈 Dashboard Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Job Postings", len(filtered_df))

with col2:
    avg_rating = round(filtered_df["Rating"].mean(), 2)
    st.metric("Average Company Rating", avg_rating)

with col3:
    st.metric("Total Companies", filtered_df["Company Name"].nunique())

with col4:
    avg_salary = round(filtered_df["Average Salary"].mean(), 1)
    st.metric("Average Salary (K USD)", avg_salary)

with col1:
    st.metric("Total Job Postings", len(filtered_df))

with col2:
    avg_rating = round(filtered_df["Rating"].mean(), 2)
    st.metric("Average Company Rating", avg_rating)

with col3:
    st.metric("Total Companies", filtered_df["Company Name"].nunique())

st.divider()

# ----------------------------------------
# Top Job Titles
# ----------------------------------------
st.subheader("📊 Top 10 Job Titles")

job_titles = filtered_df["Job Title"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10,5))
job_titles.plot(kind="bar", ax=ax)
plt.xticks(rotation=45)
plt.ylabel("Job Count")

st.pyplot(fig)

st.divider()

# ----------------------------------------
# Top Locations
# ----------------------------------------
st.subheader("📍 Top Hiring Locations")

locations_chart = filtered_df["Location"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10,5))
locations_chart.plot(kind="bar", ax=ax)
plt.xticks(rotation=45)
plt.ylabel("Job Count")

st.pyplot(fig)

st.divider()

# ----------------------------------------
# Top Hiring Companies
# ----------------------------------------
st.subheader("🏢 Top Hiring Companies")

companies = filtered_df["Company Name"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10,5))
companies.plot(kind="bar", ax=ax)
plt.xticks(rotation=90)
plt.ylabel("Job Count")

st.pyplot(fig)

st.divider()

# ----------------------------------------
# Company Ratings
# ----------------------------------------
st.subheader("⭐ Company Ratings Distribution")

fig, ax = plt.subplots(figsize=(10,5))

filtered_df["Rating"].plot(
    kind="hist",
    bins=20,
    ax=ax
)

plt.xlabel("Rating")

st.pyplot(fig)

st.divider()

# ----------------------------------------
# Company Size
# ----------------------------------------
st.subheader("🏢 Company Size Distribution")

company_size = filtered_df["Size"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10,5))

company_size.plot(kind="bar", ax=ax)

plt.xticks(rotation=45)

st.pyplot(fig)

st.divider()

# ----------------------------------------
# Industry Distribution
# ----------------------------------------
st.subheader("🏭 Top Industries")

industry = filtered_df["Industry"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10,5))

industry.plot(kind="bar", ax=ax)

plt.xticks(rotation=45)

st.pyplot(fig)

st.divider()

# ----------------------------------------
# Dataset Preview
# ----------------------------------------
st.subheader("📄 Dataset Preview")

st.dataframe(filtered_df)

st.divider()

# ----------------------------------------
# Footer
# ----------------------------------------
st.markdown("---")
st.markdown(
    "**Developed as a Data Science Job Market Analyzer Project using Python, Pandas, Matplotlib and Streamlit.**"
)