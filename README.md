# 🏨 Hotel Booking Cancellation & Revenue Risk Diagnostics

[![Python](https://img.shields.io/badge/Python-EDA%20%26%20Pandas-3776AB?style=flat-square\&logo=python)](#)
[![Seaborn](https://img.shields.io/badge/Seaborn-Data_Visualization-4c72b0?style=flat-square)](#)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)](#)

## 📌 Executive Summary & Business Problem

High booking cancellation rates can create challenges for hospitality businesses by reducing occupancy predictability, affecting staffing and resource planning, and increasing revenue uncertainty.

This project analyzes **118,000+ hotel reservation records** to identify the key factors associated with booking cancellations and evaluate how booking behavior, lead time, customer characteristics, pricing, and distribution channels influence cancellation risk.

## 🛠️ Data Pipeline & Technical Approach

* **Data Cleaning & Preparation:** Handled missing values across agent, company, and country fields, identified pricing anomalies such as negative ADR values, and converted date-related fields into appropriate datetime formats.
* **Behavioral Cohort Analysis:** Segmented booking cancellation behavior across lead-time groups, customer types, distribution channels, deposit types, and hotel categories.
* **Risk Analysis:** Examined relationships between cancellations, Average Daily Rate (ADR), lead time, room allocation changes, previous bookings, and special requests.
* **Exploratory Data Analysis:** Used Pandas, Matplotlib, and Seaborn to identify cancellation patterns, customer behavior, seasonal trends, and potential revenue risks.

## 📂 Project Structure

```text
├── data/               # Raw and transformed hotel booking datasets
├── notebooks/          # Jupyter Notebook covering data cleaning and EDA
├── visuals/            # Cancellation trends and analytical visualizations
└── README.md           # Business impact, methodology, and key insights
```

## 📊 Key Business Insights

* **Lead-Time Sensitivity:** Bookings made **more than 90 days in advance showed a significantly higher cancellation tendency** compared with short-lead bookings, highlighting lead time as an important cancellation-risk indicator.
* **Deposit Policy Impact:** Cancellation behavior varied substantially across deposit types, indicating that booking commitment and payment policies can influence reservation reliability.
* **Pricing Volatility:** Changes in Average Daily Rate (ADR), particularly during periods of higher demand, were associated with changes in cancellation behavior and potential rebooking activity.
* **Special Requests:** Guests who made special requests demonstrated **lower cancellation propensity**, suggesting that greater guest engagement may be associated with stronger booking commitment.

## 💡 Strategic Business Recommendations

* **Dynamic Overbooking Strategy:** Use historical cancellation patterns and lead-time segments to establish data-driven overbooking thresholds while maintaining acceptable service-risk levels.
* **Tiered Cancellation Policies:** Introduce progressive cancellation fees based on booking lead time and reservation characteristics rather than applying a single policy across all bookings.
* **Pre-Arrival Guest Engagement:** Use automated reminders, digital check-in options, and preference surveys before arrival to increase guest engagement and reduce avoidable cancellations.
* **Cancellation Risk Monitoring:** Develop a booking-risk segmentation model to identify high-risk reservations and support proactive revenue and occupancy management.

## 🚀 How to Explore This Project

1. **Review the EDA Notebook:** Open `/notebooks` to explore the complete data-cleaning process, exploratory analysis, feature preparation, and analytical workflow.
2. **Review the Visualizations:** Open `/visuals` to examine cancellation trends, booking behavior, pricing patterns, and other key analytical findings.

## 👤 Author

**Prashant Marathe**

* **LinkedIn:** https://www.linkedin.com/in/prashantmarathe17
* **Portfolio:** https://prashant-marathe.framer.website/
* **Email:** [p04747391@gmail.com](mailto:p04747391@gmail.com)
* **Location:** Pune, Maharashtra, India
