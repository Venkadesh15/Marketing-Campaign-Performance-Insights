# 📊 Marketing Campaign Performance Insights

## 📌 Project Overview

This project focuses on analyzing marketing campaign performance using Python and its powerful data analysis and visualization libraries.

The analysis explores campaign effectiveness, Return on Investment (ROI), conversion rates, customer segmentation, channel performance, engagement scores, time-based trends, and geographical insights to understand marketing performance.

## 🎯 Project Objectives

- Analyze marketing campaign performance and effectiveness.
- Evaluate ROI, acquisition cost, and conversion rates.
- Understand customer segments and target audience distribution.
- Compare marketing channel effectiveness.
- Identify campaign engagement trends over time.
- Analyze geographical campaign performance.
- Generate meaningful business insights through data visualization.

## 🛠️ Technologies & Tools Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Programming Language |
| 🔢 NumPy | Numerical Operations |
| 🐼 Pandas | Data Manipulation and Analysis |
| 📊 Matplotlib | Data Visualization |
| 🎨 Seaborn | Statistical Data Visualization |
| 💻 VS Code | Development Environment |

## 📂 Dataset Information

**Dataset:** Marketing Campaign Dataset

**Source:** GitHub – ArchanaInsights

🔗 [Download / View Dataset](https://raw.githubusercontent.com/ArchanaInsights/Datasets/main/marketing_campaign.csv)

The dataset contains marketing campaign information related to:

- Campaign ID
- Company
- Campaign Type
- Target Audience
- Duration
- Channel Used
- Conversion Rate
- Acquisition Cost
- ROI
- Location
- Language
- Customer Segment
- Engagement Score
- Clicks
- Impressions
- Date

## 🔍 Project Workflow

### 1️⃣ Import Required Libraries

- Import NumPy and Pandas.
- Import Matplotlib and Seaborn.
- Configure the visualization theme.

### 2️⃣ Load the Dataset

- Load the marketing campaign dataset using Pandas.
- Display the first five records.
- Verify successful dataset loading.

### 3️⃣ Basic Data Exploration

- Explore dataset dimensions.
- Display column names and data types.
- Understand dataset information.
- Generate descriptive statistics.

### 4️⃣ Unique Values & Category Analysis

- Identify unique campaign IDs.
- Explore unique locations and customer segments.
- Calculate campaign type frequency.
- Analyze marketing channel distribution.

### 5️⃣ Data Preparation & Cleaning

- Create a copy of the original dataset.
- Convert Date into datetime format.
- Extract numerical values from Duration.
- Convert numerical columns into appropriate data types.
- Remove rows with missing dates.
- Handle missing numerical values using median.
- Handle missing categorical values using mode.

### 6️⃣ Campaign Performance Analysis

- 📍 Scatter Plot – Acquisition Cost vs ROI.
- 📊 Bar Chart – Average Conversion Rate by Channel.
- 📦 Box Plot – Engagement Score by Campaign Type.
- 🏢 Bar Chart – Average ROI by Company.
- 🔥 Heatmap – Engagement Score and Conversion Rate Correlation.

### 7️⃣ Customer Segmentation Analysis

- 📊 Count Plot – Target Audience Distribution.
- 📈 Bar Chart – Conversion Rate by Customer Segment and Language.
- 🏆 Identify the highest-converting customer segment for each language.
- 📦 Box Plot – Acquisition Cost by Customer Segment and Channel.
- 📊 Bar Chart – Average Conversion Rate by Language.

### 8️⃣ Channel Effectiveness Analysis

- 📊 Bar Chart – Engagement Score by Channel and Campaign Type.
- 🥧 Pie Chart – Total ROI Distribution by Channel.
- 📍 Scatter Plot – Clicks vs Impressions by Channel.

### 9️⃣ Time-Based Analysis

- 📊 Histogram – Campaign Duration Distribution.
- 📈 Line Chart – Conversion Rate Over Time by Company.
- 📉 Line Chart – Engagement Score Trend Over Time.

### 🔟 Geographical Analysis

- 📊 Bar Chart – Average Acquisition Cost by Location.
- 📈 Bar Chart – Conversion Rate by Location and Target Audience.
- 🥧 Pie Chart – Total ROI Distribution by Location.
- 🏆 Identify the location with the highest average acquisition cost.

### 1️⃣1️⃣ Key Performance Findings

Generate a summary report containing:

- Total number of campaigns.
- Number of unique campaigns.
- Average conversion rate.
- Average acquisition cost.
- Average ROI.
- Average engagement score.
- Campaign type with the highest average ROI.
- Company with the highest average ROI.
- Channel with the highest average conversion rate.
- Location with the highest average acquisition cost.
- Customer segment with the highest average conversion rate.

## 📊 Key Analysis Areas

| Analysis | Business Purpose |
|---|---|
| Campaign Performance | Evaluate campaign effectiveness |
| ROI Analysis | Understand marketing returns |
| Customer Segmentation | Identify valuable customer groups |
| Channel Effectiveness | Compare marketing channels |
| Time-Based Analysis | Understand performance trends |
| Geographical Analysis | Compare performance across locations |

## ⚙️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Marketing-Campaign-Performance-Insights.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Marketing-Campaign-Performance-Insights
```

### Step 3: Install Required Libraries

```bash
py -m pip install numpy pandas matplotlib seaborn
```

### Step 4: Run the Python File

```bash
py "Marketing Campaign Performance Insights.py"
```

## 📁 Project Structure

```text
Marketing-Campaign-Performance-Insights/
│
├── Marketing Campaign Performance Insights.py
├── README.md
└── requirements.txt
```

## 📦 Requirements

Create a `requirements.txt` file:

```text
numpy
pandas
matplotlib
seaborn
```

Install all dependencies:

```bash
py -m pip install -r requirements.txt
```
