# PROJECT TITLE: MARKETING CAMPAIGN PERFORMANCE INSIGHTS

# 1) IMPORT REQUIRED LIBRARIES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# 2) LOAD THE DATASET

# 2.1) Load the dataset from the provided URL
url = "https://raw.githubusercontent.com/ArchanaInsights/Datasets/main/marketing_campaign.csv"

df = pd.read_csv(url)

print("\n========== DATASET LOADED SUCCESSFULLY ==========\n")
print(df.head())


# 3) BASIC DATA EXPLORATION

print("\n========== FIRST 5 ROWS ==========\n")
print(df.head())

print("\n========== NUMBER OF ROWS AND COLUMNS ==========\n")
print(df.shape)

print("\n========== COLUMN NAMES ==========\n")
print(df.columns)

print("\n========== DATA TYPES ==========\n")
print(df.dtypes)

print("\n========== DATASET INFORMATION ==========\n")
df.info()

print("\n========== DESCRIPTIVE STATISTICS ==========\n")
print(df.describe())


# 4) UNIQUE VALUES AND CATEGORY COUNTS

# 4.1) Check for unique values in key columns
print("\n========== UNIQUE CAMPAIGN IDs ==========\n")
print(df['Campaign_ID'].nunique())

print("\n========== UNIQUE LOCATIONS ==========\n")
print(df['Location'].unique())

print("\n========== UNIQUE CUSTOMER SEGMENTS ==========\n")
print(df['Customer_Segment'].unique())

print("\n========== CAMPAIGN TYPE COUNTS ==========\n")
print(df['Campaign_Type'].value_counts())

# 4.2) Handle Channel_Used / Channels_Used column name difference
if 'Channel_Used' in df.columns:
    channel_column = 'Channel_Used'
elif 'Channels_Used' in df.columns:
    channel_column = 'Channels_Used'
else:
    raise KeyError("Channel_Used or Channels_Used column not found.")

print("\n========== CHANNEL COUNTS ==========\n")
print(df[channel_column].value_counts())


# 5) DATA PREPARATION

# 5.1) Create a copy of the original dataset
df_clean = df.copy()

# 5.2) Convert Date column into datetime format
df_clean['Date'] = pd.to_datetime(
    df_clean['Date'],
    format='%d-%m-%Y',  # Explicit format matching '01-01-2023'
    errors='coerce'
)

# 5.3) Clean and convert Duration (extract numbers from text strings)
df_clean['Duration'] = df_clean['Duration'].astype(str).str.extract(r'(\d+)')[0]

# 5.4)Convert all required numerical columns into numeric format
numeric_columns = [
    'Duration',
    'Conversion_Rate',
    'Acquisition_Cost',
    'ROI',
    'Clicks',
    'Impressions',
    'Engagement_Score'
]

for col in numeric_columns:
    df_clean[col] = pd.to_numeric(
        df_clean[col],
        errors='coerce'
    )

# 5.5) Remove rows where Date is missing
df_clean = df_clean.dropna(subset=['Date'])

# 5.6) Fill missing numerical values using median
for col in numeric_columns:
    median_value = df_clean[col].median()
    if pd.notna(median_value):
        df_clean[col] = df_clean[col].fillna(median_value)

# 5.7) Fill missing categorical values using mode
categorical_columns = df_clean.select_dtypes(
    include=['object', 'category', 'string']
).columns

for col in categorical_columns:
    if df_clean[col].isnull().any():
        mode_value = df_clean[col].mode()
        if not mode_value.empty:
            df_clean[col] = df_clean[col].fillna(mode_value[0])
        else:
            df_clean[col] = df_clean[col].fillna("Unknown")

print("\n========== DATA CLEANING COMPLETED ==========\n")
print(df_clean.isnull().sum())

print("\nCleaned Dataset Shape:")
print(df_clean.shape)


# 6) CAMPAIGN PERFORMANCE ANALYSIS

# 6.1) SCATTER PLOT - ACQUISITION COST VS ROI
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df_clean,
    x='Acquisition_Cost',
    y='ROI',
    hue='Campaign_Type'
)

plt.title('Acquisition Cost vs ROI')
plt.xlabel('Acquisition Cost')
plt.ylabel('Return on Investment (ROI)')
plt.tight_layout()
plt.show()

# 6.2) BAR CHART - AVERAGE CONVERSION RATE BY CHANNEL
plt.figure(figsize=(12, 6))

sns.barplot(
    data=df_clean,
    x=channel_column,
    y='Conversion_Rate',
    hue='Campaign_Type',
    errorbar=None
)

plt.title('Average Conversion Rate by Channel and Campaign Type')
plt.xlabel('Channel Used')
plt.ylabel('Average Conversion Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6.3) BOX PLOT - ENGAGEMENT SCORE BY CAMPAIGN TYPE
plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df_clean,
    x='Campaign_Type',
    y='Engagement_Score'
)

plt.title('Engagement Score by Campaign Type')
plt.xlabel('Campaign Type')
plt.ylabel('Engagement Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 6.4) BAR CHART - AVERAGE ROI BY COMPANY
company_roi = df_clean.groupby(
    'Company'
)['ROI'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=company_roi.index,
    y=company_roi.values,
    errorbar=None
)

plt.title('Average ROI by Company')
plt.xlabel('Company')
plt.ylabel('Average ROI')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6.5) HEATMAP - ENGAGEMENT SCORE AND CONVERSION RATE
correlation_data = df_clean[
    ['Engagement_Score', 'Conversion_Rate']
]

correlation = correlation_data.corr()

plt.figure(figsize=(7, 5))

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Correlation: Engagement Score and Conversion Rate')
plt.tight_layout()
plt.show()



# 7) CUSTOMER SEGMENTATION ANALYSIS

# 7.1) COUNT PLOT - TARGET AUDIENCE DISTRIBUTION
plt.figure(figsize=(12, 6))

sns.countplot(
    data=df_clean,
    x='Target_Audience',
    order=df_clean['Target_Audience'].value_counts().index
)

plt.title('Distribution of Target Audience')
plt.xlabel('Target Audience')
plt.ylabel('Number of Campaigns')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7.2) BAR CHART - CUSTOMER SEGMENT CONVERSION RATE BY LANGUAGE
segment_language = df_clean.groupby(
    ['Language', 'Customer_Segment']
)['Conversion_Rate'].mean().reset_index()

plt.figure(figsize=(14, 7))

sns.barplot(
    data=segment_language,
    x='Language',
    y='Conversion_Rate',
    hue='Customer_Segment',
    errorbar=None
)

plt.title('Average Conversion Rate by Customer Segment and Language')
plt.xlabel('Language')
plt.ylabel('Average Conversion Rate')
plt.xticks(rotation=45)
plt.legend(
    title='Customer Segment',
    bbox_to_anchor=(1.02, 1),
    loc='upper left'
)
plt.tight_layout()
plt.show()

# 7.3) Identify the highest-converting segment for each language
best_segments = segment_language.loc[
    segment_language.groupby('Language')['Conversion_Rate'].idxmax()
]

print("\n========== BEST CUSTOMER SEGMENT BY LANGUAGE ==========\n")
print(best_segments)


# 7.4) BOX PLOT - ACQUISITION COST BY CUSTOMER SEGMENT
plt.figure(figsize=(14, 7))

sns.boxplot(
    data=df_clean,
    x='Customer_Segment',
    y='Acquisition_Cost',
    hue=channel_column
)

plt.title('Acquisition Cost by Customer Segment and Channel')
plt.xlabel('Customer Segment')
plt.ylabel('Acquisition Cost')
plt.xticks(rotation=45)
plt.legend(
    title='Channel Used',
    bbox_to_anchor=(1.02, 1),
    loc='upper left'
)
plt.tight_layout()
plt.show()


# 7.5) BAR CHART - AVERAGE CONVERSION RATE BY LANGUAGE
language_conversion = df_clean.groupby(
    'Language'
)['Conversion_Rate'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=language_conversion.index,
    y=language_conversion.values,
    errorbar=None
)

plt.title('Average Conversion Rate by Language')
plt.xlabel('Language')
plt.ylabel('Average Conversion Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 8) CHANNEL EFFECTIVENESS ANALYSIS

# 8.1) BAR CHART - ENGAGEMENT SCORE BY CHANNEL
plt.figure(figsize=(12, 6))

sns.barplot(
    data=df_clean,
    x=channel_column,
    y='Engagement_Score',
    hue='Campaign_Type',
    errorbar=None
)

plt.title('Engagement Score by Channel and Campaign Type')
plt.xlabel('Channel Used')
plt.ylabel('Average Engagement Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 8.2) PIE CHART - TOTAL ROI BY CHANNEL
channel_roi = df_clean.groupby(
    channel_column
)['ROI'].sum()

plt.figure(figsize=(9, 9))

plt.pie(
    channel_roi,
    labels=channel_roi.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Distribution of Total ROI by Channel')
plt.show()

# 8.3) SCATTER PLOT - CLICKS VS IMPRESSIONS BY CHANNEL
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df_clean,
    x='Impressions',
    y='Clicks',
    hue=channel_column
)

plt.title('Clicks vs Impressions by Channel')
plt.xlabel('Impressions')
plt.ylabel('Clicks')
plt.tight_layout()
plt.show()

# 9) TIME-BASED ANALYSIS

# 9.1) HISTOGRAM - CAMPAIGN DURATION DISTRIBUTION
plt.figure(figsize=(10, 6))

plt.hist(
    df_clean['Duration'].dropna(),  # Drop any leftover NaNs
    bins=20,
    edgecolor='black'
)

plt.title('Distribution of Campaign Duration')
plt.xlabel('Duration (Days)')
plt.ylabel('Number of Campaigns')
plt.tight_layout()
plt.show()

# 9.2) LINE CHART - CONVERSION RATE OVER DATE BY COMPANY
company_date = df_clean.groupby(
    ['Date', 'Company']
)['Conversion_Rate'].mean().reset_index()

plt.figure(figsize=(14, 7))

sns.lineplot(
    data=company_date,
    x='Date',
    y='Conversion_Rate',
    hue='Company',
    marker='o'
)

plt.title('Conversion Rate Over Time by Company')
plt.xlabel('Date')
plt.ylabel('Average Conversion Rate')
plt.xticks(rotation=45)
plt.legend(
    title='Company',
    bbox_to_anchor=(1.02, 1),
    loc='upper left'
)
plt.tight_layout()
plt.show()

# 9.3) LINE CHART - ENGAGEMENT SCORE OVER DATE
date_engagement = df_clean.groupby(
    'Date'
)['Engagement_Score'].mean().reset_index()

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=date_engagement,
    x='Date',
    y='Engagement_Score',
    marker='o'
)

plt.title('Engagement Score Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Average Engagement Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 10) GEOGRAPHICAL ANALYSIS

# 10.1) BAR CHART - ACQUISITION COST BY LOCATION
location_cost = df_clean.groupby(
    'Location'
)['Acquisition_Cost'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=location_cost.index,
    y=location_cost.values,
    errorbar=None
)

plt.title('Average Acquisition Cost by Location')
plt.xlabel('Location')
plt.ylabel('Average Acquisition Cost')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nLocation with Highest Average Acquisition Cost:")
print(location_cost.idxmax())

# 10.2) BAR CHART - CONVERSION RATE BY LOCATION
location_conversion = df_clean.groupby(
    ['Location', 'Target_Audience']
)['Conversion_Rate'].mean().reset_index()

plt.figure(figsize=(14, 7))

sns.barplot(
    data=location_conversion,
    x='Location',
    y='Conversion_Rate',
    hue='Target_Audience',
    errorbar=None
)

plt.title('Conversion Rate by Location and Target Audience')
plt.xlabel('Location')
plt.ylabel('Average Conversion Rate')
plt.xticks(rotation=45)
plt.legend(
    title='Target Audience',
    bbox_to_anchor=(1.02, 1),
    loc='upper left'
)
plt.tight_layout()
plt.show()

# 10.3) PIE CHART - PROPORTION OF ROI BY LOCATION
location_roi = df_clean.groupby(
    'Location'
)['ROI'].sum()

plt.figure(figsize=(9, 9))

plt.pie(
    location_roi,
    labels=location_roi.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Proportion of Total ROI by Location')
plt.show()


# 11) KEY PERFORMANCE FINDINGS

print("\n==============================================")
print("       MARKETING CAMPAIGN ANALYSIS REPORT")
print("==============================================")

print("\nTotal Number of Campaigns:")
print(len(df_clean))

print("\nNumber of Unique Campaigns:")
print(df_clean['Campaign_ID'].nunique())

print("\nAverage Conversion Rate:")
print(round(df_clean['Conversion_Rate'].mean(), 2))

print("\nAverage Acquisition Cost:")
print(round(df_clean['Acquisition_Cost'].mean(), 2))

print("\nAverage ROI:")
print(round(df_clean['ROI'].mean(), 2))

print("\nAverage Engagement Score:")
print(round(df_clean['Engagement_Score'].mean(), 2))

print("\nCampaign Type with Highest Average ROI:")
print(
    df_clean.groupby('Campaign_Type')['ROI']
    .mean().idxmax()
)

print("\nCompany with Highest Average ROI:")
print(
    df_clean.groupby('Company')['ROI']
    .mean().idxmax()
)

print("\nChannel with Highest Average Conversion Rate:")
print(
    df_clean.groupby(channel_column)['Conversion_Rate']
    .mean().idxmax()
)

print("\nLocation with Highest Average Acquisition Cost:")
print(
    df_clean.groupby('Location')['Acquisition_Cost']
    .mean().idxmax()
)

print("\nCustomer Segment with Highest Average Conversion Rate:")
print(
    df_clean.groupby('Customer_Segment')['Conversion_Rate']
    .mean().idxmax()
)