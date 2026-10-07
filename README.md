# 🏨 Hotel Booking Cancellation & Revenue Risk Analysis

> **End-to-end hotel analytics project using Python, Pandas, EDA, and Power BI to identify cancellation drivers, quantify revenue exposure, and develop actionable revenue-management strategies.**

## 📌 Business Problem

Hotel cancellations create uncertainty around occupancy, staffing, inventory planning, and expected revenue.

This project analyzes **118,000+ hotel reservation records** to understand:

* Why customers cancel bookings
* Which booking characteristics are associated with higher cancellation risk
* How lead time affects cancellation behavior
* How deposit policies influence booking reliability
* How pricing and customer engagement relate to cancellations
* The potential revenue exposure associated with cancelled reservations

---

## 🎯 Project Objectives

The analysis focuses on four key areas:

1. **Cancellation Analysis** — identify major drivers of booking cancellations.
2. **Customer & Booking Behavior** — analyze lead time, customer type, distribution channels, and booking characteristics.
3. **Revenue Risk** — quantify the financial exposure associated with cancelled reservations.
4. **Business Recommendations** — translate analytical findings into practical revenue-management actions.

---

## 📊 Project Snapshot

| Metric                |    Value |
| --------------------- | -------: |
| Reservations Analyzed |    118K+ |
| Cancellation Rate     |   37.14% |
| Revenue Exposure      |  $25.91M |
| Primary Analysis Tool |   Python |
| BI / Dashboard Tool   | Power BI |

---

## 🛠️ Tech Stack

| Area                  | Tools               |
| --------------------- | ------------------- |
| Programming           | Python              |
| Data Analysis         | Pandas              |
| Visualization         | Matplotlib, Seaborn |
| Data Cleaning         | Pandas              |
| Exploratory Analysis  | EDA                 |
| Business Intelligence | Power BI            |
| Reporting             | Power BI / Python   |
| Documentation         | Markdown            |

---

## 🔄 End-to-End Analytics Workflow

```text
Raw Hotel Booking Data
        ↓
Data Cleaning & Validation
        ↓
Missing-Value Treatment
        ↓
Feature Preparation
        ↓
Exploratory Data Analysis
        ↓
Cancellation Risk Analysis
        ↓
Revenue Exposure Analysis
        ↓
Business Insights
        ↓
Revenue Management Recommendations
```

---

## 🧹 Data Cleaning & Preparation

The dataset was prepared for analysis by:

* Handling missing values across relevant fields
* Investigating pricing anomalies
* Identifying negative ADR values
* Converting date-related columns into appropriate datetime formats
* Creating analytical segments for cancellation analysis
* Validating booking and cancellation-related fields

---

## 🔍 Key Analytical Questions

### Booking Behavior

* Does booking lead time influence cancellation probability?
* Which customer segments show higher cancellation rates?
* Which distribution channels generate more cancellations?
* How does hotel type affect cancellation behavior?

### Pricing & Revenue

* Is ADR associated with cancellation behavior?
* Which booking segments represent the highest revenue exposure?
* How can cancellation patterns support better revenue planning?

### Customer Engagement

* Do special requests indicate stronger booking commitment?
* How do previous booking behaviors relate to cancellation risk?

---

## 📈 Key Business Insights

### 1. High Cancellation Exposure

The analysis identified a **37.14% cancellation rate across 118K+ reservations**, representing approximately **$25.91M in revenue exposure**.

**Business implication:**
Cancellation management should be treated as a revenue-management problem rather than simply an operational metric.

### 2. Lead-Time Sensitivity

Bookings made more than **90 days in advance** showed a higher tendency to cancel compared with shorter-lead bookings.

**Business implication:**
Long-lead reservations can be incorporated into cancellation-risk monitoring and overbooking decisions.

### 3. Deposit Policy Matters

Cancellation behavior varied substantially across deposit types.

**Business implication:**
Booking commitment mechanisms and cancellation policies can influence reservation reliability.

### 4. Customer Engagement Signal

Bookings containing special requests demonstrated lower cancellation propensity.

**Business implication:**
Higher customer engagement may provide a useful behavioral signal when identifying booking reliability.

### 5. Pricing Behavior

Changes in Average Daily Rate (ADR), particularly around higher-demand periods, were associated with changes in cancellation behavior and potential rebooking activity.

**Business implication:**
Pricing and cancellation analytics should be evaluated together when managing revenue risk.

---

## 💡 Business Recommendations

### 🔹 1. Implement Cancellation-Risk Monitoring

Create booking-risk segments based on:

* Lead time
* Deposit type
* Customer type
* Distribution channel
* ADR
* Previous booking behavior

This allows revenue teams to identify higher-risk reservations before arrival.

### 🔹 2. Develop Dynamic Overbooking Rules

Use historical cancellation patterns to establish data-driven overbooking thresholds while maintaining acceptable service risk.

### 🔹 3. Introduce Tiered Cancellation Policies

Consider different cancellation terms based on booking lead time, deposit type, and reservation characteristics.

### 🔹 4. Improve Pre-Arrival Engagement

Use:

* Automated reminders
* Digital check-in
* Guest preference collection
* Pre-arrival communication

to strengthen customer engagement and reduce avoidable cancellations.

### 🔹 5. Combine Pricing & Cancellation Analytics

Monitor ADR changes alongside cancellation behavior to understand potential revenue risks and rebooking opportunities.

---

## 📊 Dashboard

The project includes a Power BI dashboard for exploring hotel booking and cancellation patterns.

Key analytical areas include:

* Cancellation KPIs
* Booking trends
* Lead-time analysis
* Customer segmentation
* Deposit-type analysis
* ADR analysis
* Revenue exposure
* Cancellation-risk patterns

**Power BI file:** `Hotel_Bookings.pbix`

---

## 🧠 What This Project Demonstrates

### Python & EDA

* Data cleaning
* Missing-value analysis
* Feature preparation
* Exploratory data analysis
* Behavioral segmentation
* Statistical exploration
* Business-oriented visualization

### Business Analytics

* KPI analysis
* Revenue-risk analysis
* Customer behavior analysis
* Root-cause exploration
* Business recommendations

### Power BI

* Interactive dashboards
* KPI visualization
* Trend analysis
* Segment analysis
* Business storytelling

---

## 📂 Project Structure

```text
hotel-cancellation-revenue-analysis/
│
├── data/
│   ├── hotel_bookings.csv
│   └── hotel_bookings_cleaned.csv
│
├── python/
│   └── Hotel_Booking.py
│
├── powerbi/
│   └── Hotel_Bookings.pbix
│
├── report/
│   └── Hotel_Booking_Cancellation_Analysis_Report.docx
│
├── screenshots/
│   ├── dashboard-overview.png
│   ├── cancellation-analysis.png
│   ├── lead-time-analysis.png
│   ├── revenue-analysis.png
│   └── key-insights.png
│
├── requirements.txt
└── README.md
```

> **Note:** Create these folders and move the existing files into them before using this structure. Keep the README synchronized with the actual repository structure.

---

## 🚀 Business Value

This project demonstrates how raw hotel booking data can be transformed into actionable business intelligence.

The analysis can help hospitality teams:

* Improve occupancy forecasting
* Identify high-risk reservations
* Reduce cancellation-related revenue uncertainty
* Improve overbooking decisions
* Optimize cancellation policies
* Understand customer booking behavior
* Support data-driven revenue management

---

## 👤 Author

**Prashant Marathe**

B.Tech — Artificial Intelligence & Data Science

**Target Roles:** Data Analyst | BI Analyst | Business Analyst

📍 Pune, Maharashtra, India

* [LinkedIn](https://www.linkedin.com/in/prashantmarathe17)
* [Portfolio](https://prashant-marathe.framer.website/)
* [GitHub](https://github.com/MarathePrashant)
* Email: [p04747391@gmail.com](mailto:p04747391@gmail.com)
