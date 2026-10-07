#Importing Required Library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

#Loading_Dataset
df  = pd.read_csv(r"C:\Users\prash\OneDrive\Documents\PERSONAL LIBRARY\Programming\GitHub\Hotel_Booking\hotel_bookings.csv")

#Exploratory Data Analysis & Data Cleaning
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'],dayfirst=True)
print(df.info())
print(df.describe(include = 'object'))
for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print(('-'*50))

#CheckingMissing Values
print(df.isnull().sum())
df.drop(["company","agent"],axis = 1, inplace = True)
df.dropna(inplace = True)

#Checking Missing Values again
print(df.isnull().sum())

#Summary Statistics
print(df.describe())

#outliers
numeric_cols = df.select_dtypes(include=['int64','float64']).columns
print(numeric_cols)

#Calculating Outliers
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q2 = df[col].quantile(0.75)

    IQR = Q2 - Q1 

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q2 + 1.5 * IQR

    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"{col}:{len(outliers)} outliers")

#Outliers Summary 
outliers_summary = []
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q2 = df[col].quantile(0.75)

    IQR = Q2 - Q1 

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q2 + 1.5 * IQR
    outlier_count = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()

    outliers_percentage = (outlier_count / len(df)) * 100
    outliers_summary.append({
        'Column':col,
        'Q1': Q1,
        'Q2': Q2,
        'IQR': IQR,
        'Lower Bound': lower_bound,
        'Upper Bound': upper_bound,
        'Outlier Count': outlier_count,
        'Outlier %': outliers_percentage
    })
outlier_df = pd.DataFrame(outliers_summary)
outlier_df.sort_values(by='Outlier Count',ascending=False)

#Checking the value distribution of count-based variables

check_cols = [
    'adults',
    'children',
    'babies',
    'stays_in_weekend_nights',
    'stays_in_week_nights',
    'booking_changes',
    'previous_cancellations',
    'previous_bookings_not_canceled',
    'days_in_waiting_list',
    'required_car_parking_spaces',
    'total_of_special_requests'
]

for col in check_cols:
    print(f"{col}")
    print(df[col].value_counts().sort_index())

###Visualizing Outliers using Boxplots
outlier_cols = [
    'lead_time',
    'stays_in_weekend_nights',
    'stays_in_week_nights',
    'previous_cancellations',
    'previous_bookings_not_canceled',
    'booking_changes',
    'days_in_waiting_list',
    'adr',
    'total_of_special_requests']
for col in outlier_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col])
    plt.title('Boxplot of {col}')
    plt.xlabel(col)
    plt.tight_layout()
    # plt.show()

# Distribution Analysis
for col in outlier_cols:
    plt.figure(figsize=(8, 4))
    
    sns.histplot(df[col], kde=True)
    
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    
    plt.tight_layout()
    # plt.show()

print("ADR Statistics")
print(df['adr'].describe())
print("Highest ADR values:")
print(df[['hotel', 'adults', 'children', 'babies', 'adr']].sort_values('adr', ascending=False).head(20))

print("Negative ADR records:")
print(df[df['adr'] < 0][['hotel', 'adults', 'children', 'babies', 'adr']])

print("Number of zero ADR records:")
print((df['adr'] == 0).sum())

#extreme lead_time
print("Highest Lead Time values:")
print(df[['hotel', 'lead_time', 'is_canceled', 'customer_type']]
    .sort_values('lead_time', ascending=False).head(20))

#Required Car Parking
df[df['required_car_parking_spaces'] >= 3][['hotel', 'adults', 'children', 'required_car_parking_spaces']]

#ADR
print("ADR")
print(df[df['adr'] < 0])

df = df[df['adr'] >= 0]
print(df['adr'].describe())

# Extreme adults check
print(df[df['adults'] > 6][['hotel', 'adults', 'children', 'babies', 'adr']])

# Extreme ADR
print(df[df['adr'] >= 500].T)

# Negative ADR
print(df[df['adr'] < 0].T)

df = df[df['adr'] >= 0]

#UNIVARIATE ANALYSIS

# Booking Cancellation Distribution
print(df['is_canceled'].value_counts())

sns.countplot(x='is_canceled', data=df)
plt.title('Booking Cancellation Distribution')
plt.xlabel('Cancellation Status')
plt.ylabel('Number of Bookings')
plt.show()

cancellation_percentage = df['is_canceled'].value_counts(normalize=True) * 100
print(cancellation_percentage.round(2))

#Hotel Type Distribution
print(df['hotel'].value_counts())
sns.countplot(x='hotel', data=df)
plt.title('Hotel Type Distribution')
plt.xlabel('Hotel Type')
plt.ylabel('Number of Bookings')
plt.show()

# Lead Time Distribution

print(df['lead_time'].describe())
plt.figure(figsize=(10, 5))
sns.histplot(df['lead_time'], bins=50, kde=True)
plt.title('Lead Time Distribution')
plt.xlabel('Lead Time (Days)')
plt.ylabel('Number of Bookings')
plt.show()

# ADR(Average Daily Rate) Distribution

print(df['adr'].describe())
plt.figure(figsize=(10, 5))
sns.histplot(df['adr'], bins=50, kde=True)
plt.title('ADR Distribution')
plt.xlabel('Average Daily Rate (ADR)')
plt.ylabel('Number of Bookings')
plt.show()

# ADR Boxplot
plt.figure(figsize=(10, 4))
sns.boxplot(x=df['adr'])
plt.title('ADR Boxplot')
plt.xlabel('Average Daily Rate')
plt.show()

# Hotel Booking Distribution

hotel_counts = df['hotel'].value_counts()
print(hotel_counts)
plt.figure(figsize=(8, 5))
sns.countplot(x='hotel', data=df)
plt.title('Booking Distribution by Hotel Type')
plt.xlabel('Hotel Type')
plt.ylabel('Number of Bookings')
plt.show()

hotel_percentage = df['hotel'].value_counts(normalize=True) * 100
print("Hotel Booking Percentage:")
print(hotel_percentage.round(2))

# Monthly Booking Distribution
months = ['January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December']
monthly_bookings = (df['arrival_date_month'].value_counts().reindex(months))
print(monthly_bookings)

plt.figure(figsize=(12, 5))
sns.barplot(x=monthly_bookings.index, y=monthly_bookings.values)

plt.title('Monthly Booking Distribution')
plt.xlabel('Arrival Month')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=45)
plt.show()

# Market Segment Analysis

market_segment_counts = df['market_segment'].value_counts()
print(market_segment_counts)

market_segment_percentage = (df['market_segment'].value_counts(normalize=True) * 100)
print("Market Segment Percentage:")
print(market_segment_percentage.round(2))

#plot
plt.figure(figsize=(10, 5))

sns.countplot(x='market_segment',data=df,order=df['market_segment'].value_counts().index)
plt.title('Booking Distribution by Market Segment')
plt.xlabel('Market Segment')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=30)
plt.show()

# Distribution Channel Analysis
channel_counts = df['distribution_channel'].value_counts()
print(channel_counts)

channel_percentage = (df['distribution_channel'].value_counts(normalize=True) * 100)
print("Distribution Channel Percentage:")
print(channel_percentage.round(2))

plt.figure(figsize=(9, 5))

sns.countplot(x='distribution_channel',data=df,
    order=df['distribution_channel'].value_counts().index)
plt.title('Booking Distribution by Distribution Channel')
plt.xlabel('Distribution Channel')
plt.ylabel('Number of Bookings')
plt.show()


#BIVARIATE ANALYSIS


# Cancellation by Hotel Type
hotel_cancellation = pd.crosstab(
    df['hotel'],
    df['is_canceled'])
print(hotel_cancellation)

hotel_cancellation_rate = (
    df.groupby('hotel')['is_canceled']
    .mean() * 100)
print("Cancellation Rate by Hotel:")
print(hotel_cancellation_rate.round(2))

plt.figure(figsize=(8, 5))
sns.barplot(
    x=hotel_cancellation_rate.index,
    y=hotel_cancellation_rate.values)

plt.title('Cancellation Rate by Hotel Type')
plt.xlabel('Hotel Type')
plt.ylabel('Cancellation Rate (%)')
plt.show()

# Cancellation Rate by Market Segment
segment_cancellation = (
    df.groupby('market_segment')['is_canceled'].mean() * 100)
segment_cancellation = segment_cancellation.sort_values(ascending=False)
print("Cancellation Rate by Market Segment:")
print(segment_cancellation.round(2))

plt.figure(figsize=(10, 5))
sns.barplot(x=segment_cancellation.index,y=segment_cancellation.values)
plt.title('Cancellation Rate by Market Segment')
plt.xlabel('Market Segment')
plt.ylabel('Cancellation Rate (%)')
plt.xticks(rotation=30)
plt.show()

# Lead Time Groups

df['lead_time_group'] = pd.cut(
    df['lead_time'],
    bins=[-1, 7, 30, 90, 180, 365, 1000],
    labels=[
        '0-7 days',
        '8-30 days',
        '31-90 days',
        '91-180 days',
        '181-365 days',
        '365+ days'])
print(df['lead_time_group'].value_counts().sort_index())

# Cancellation Rate by Lead Time Group

lead_time_cancellation = (df.groupby('lead_time_group', observed=False)['is_canceled'].mean() * 100)
print("Cancellation Rate by Lead Time Group:")
print(lead_time_cancellation.round(2))

# ADR by Hotel Type

adr_by_hotel = (
    df.groupby('hotel')['adr']
    .agg(['mean', 'median'])
    .round(2))
print(adr_by_hotel)

plt.figure(figsize=(8, 5))
sns.barplot(
    x=adr_by_hotel.index,
    y=adr_by_hotel['mean'])
plt.title('Average ADR by Hotel Type')
plt.xlabel('Hotel Type')
plt.ylabel('Average Daily Rate')
plt.show()

# Cancellation Rate by Customer Type

customer_cancellation = (
    df.groupby('customer_type')['is_canceled']
    .mean() * 100)

customer_cancellation = customer_cancellation.sort_values(
    ascending=False)
print("Cancellation Rate by Customer Type:")
print(customer_cancellation.round(2))

plt.figure(figsize=(9, 5))

sns.barplot(
    x=customer_cancellation.index,
    y=customer_cancellation.values)

plt.title('Cancellation Rate by Customer Type')
plt.xlabel('Customer Type')
plt.ylabel('Cancellation Rate (%)')
plt.xticks(rotation=20)
plt.show()

# Cancellation Rate by Deposit Type

deposit_cancellation = (df.groupby('deposit_type')['is_canceled'].mean() * 100)
deposit_cancellation = deposit_cancellation.sort_values(ascending=False)

print("Cancellation Rate by Deposit Type:")
print(deposit_cancellation.round(2))

plt.figure(figsize=(9, 5))

sns.barplot(
    x=deposit_cancellation.index,
    y=deposit_cancellation.values
)

plt.title('Cancellation Rate by Deposit Type')
plt.xlabel('Deposit Type')
plt.ylabel('Cancellation Rate (%)')
plt.xticks(rotation=20)
plt.show()

# Cancellation Rate by Number of Special Requests

special_request_cancellation = (
    df.groupby('total_of_special_requests')['is_canceled']
    .mean() * 100
)

print("Cancellation Rate by Special Requests:")
print(special_request_cancellation.round(2))

plt.figure(figsize=(9, 5))

sns.barplot(
    x=special_request_cancellation.index,
    y=special_request_cancellation.values
)

plt.title('Cancellation Rate by Number of Special Requests')
plt.xlabel('Number of Special Requests')
plt.ylabel('Cancellation Rate (%)')
plt.show()

# Monthly Booking Trend

months = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]

monthly_bookings = (
    df['arrival_date_month']
    .value_counts()
    .reindex(months)
)

print("Monthly Bookings:")
print(monthly_bookings)

plt.figure(figsize=(12, 5))

sns.lineplot(
    x=monthly_bookings.index,
    y=monthly_bookings.values,
    marker='o'
)

plt.title('Monthly Booking Trend')
plt.xlabel('Arrival Month')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Monthly Cancellation Rate

monthly_cancellation = (
    df.groupby('arrival_date_month')['is_canceled']
    .mean() * 100
)

monthly_cancellation = monthly_cancellation.reindex(months)

print("Monthly Cancellation Rate:")
print(monthly_cancellation.round(2))

plt.figure(figsize=(12, 5))

sns.lineplot(
    x=monthly_cancellation.index,
    y=monthly_cancellation.values,
    marker='o'
)

plt.title('Monthly Cancellation Rate')
plt.xlabel('Arrival Month')
plt.ylabel('Cancellation Rate (%)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Monthly ADR Trend

monthly_adr = (
    df.groupby('arrival_date_month')['adr']
    .mean()
    .reindex(months)
)

print("Monthly Average ADR:")
print(monthly_adr.round(2))

plt.figure(figsize=(12, 5))

sns.lineplot(
    x=monthly_adr.index,
    y=monthly_adr.values,
    marker='o'
)

plt.title('Monthly ADR Trend')
plt.xlabel('Arrival Month')
plt.ylabel('Average Daily Rate')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Correlation Analysis

numeric_cols = [
    'is_canceled',
    'lead_time',
    'stays_in_weekend_nights',
    'stays_in_week_nights',
    'adults',
    'children',
    'babies',
    'is_repeated_guest',
    'previous_cancellations',
    'previous_bookings_not_canceled',
    'booking_changes',
    'days_in_waiting_list',
    'adr',
    'required_car_parking_spaces',
    'total_of_special_requests'
]

corr = df[numeric_cols].corr()

print("Correlation with Cancellation:")
print(corr['is_canceled'].sort_values(ascending=False).round(2))

# Step 8 — Correlation Analysis

numeric_cols = [
    'is_canceled',
    'lead_time',
    'stays_in_weekend_nights',
    'stays_in_week_nights',
    'adults',
    'children',
    'babies',
    'is_repeated_guest',
    'previous_cancellations',
    'previous_bookings_not_canceled',
    'booking_changes',
    'days_in_waiting_list',
    'adr',
    'required_car_parking_spaces',
    'total_of_special_requests'
]

corr = df[numeric_cols].corr()

print("Correlation with Cancellation:")
print(corr['is_canceled'].sort_values(ascending=False).round(2))

plt.figure(figsize=(12, 8))

sns.heatmap(
    corr,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    center=0
)

plt.title('Correlation Matrix')
plt.show()

print(corr['is_canceled'].sort_values(ascending=False).round(2))

# Step 9 — Key Business Insights

insights = {
    'Metric': [
        'Total Bookings',
        'Cancellation Rate',
        'Non-Cancellation Rate',
        'Most Booked Hotel',
        'Average Lead Time',
        'Median Lead Time',
        'Average ADR',
        'Median ADR'
    ],
    
    'Value': [
        len(df),
        round(df['is_canceled'].mean() * 100, 2),
        round((1 - df['is_canceled'].mean()) * 100, 2),
        df['hotel'].value_counts().idxmax(),
        round(df['lead_time'].mean(), 2),
        round(df['lead_time'].median(), 2),
        round(df['adr'].mean(), 2),
        round(df['adr'].median(), 2)
    ]
}

insights_df = pd.DataFrame(insights)

print("\nKey Business Insights:")
print(insights_df)

print("Final Dataset Shape:")
print(df.shape)

print("\nFinal Columns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df.to_csv(
    r"C:\Users\prash\OneDrive\Documents\PERSONAL LIBRARY\Programming\GitHub\Hotel_Booking\hotel_bookings_cleaned.csv",
    index=False)

print("Cleaned dataset saved successfully.")
