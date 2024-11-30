# Customer Engagement and Product Feedback Analysis

## Project Overview

This project is an **operational intelligence report** whose goal is to analyze customer engagement and their feedback to derive actionable insights and optimize future marketing strategies. By processing and analyzing customer data, particularly customer reviews, the project aims to uncover patterns and trends that can inform targeted marketing campaigns, improve customer satisfaction, and drive business growth. This analysis combines data cleaning, text segmentation, data modeling, and visualization to create a comprehensive overview of customer sentiment and engagement.

## Workflow

The project is structured into four main stages:

### 1. **Data Cleaning and Transformation**
   - **Tool**: SQL Server
   - **Description**: Raw customer engagement data is cleaned and transformed using SQL queries to ensure it's structured and ready for analysis. This stage includes tasks such as handling missing data, filtering irrelevant information, and creating necessary data relationships.

### 2. **Data Segmentation**
   - **Tools**: Python (Pandas, NLTK, pyodbc)
   - **Description**: Customer reviews are extracted from SQL Server and processed in Python using `pyodbc` for database connectivity. Natural Language Processing (NLP) techniques, including text segmentation and sentiment analysis, are applied using the `NLTK` library to understand customer feedback and sentiment.

### 3. **Data Modeling and Dashboard Creation**
   - **Tool**: Power BI
   - **Description**: The processed data is imported into Power BI, where a data model is created. DAX (Data Analysis Expressions) is used to build "Date" table and calculate necessary measures. Interactive dashboards are created to visualize insights, including customer engagement trends, sentiment over time, and key demographic information.

### 4. **Analysis and Presentation**
   - **Tool**: PowerPoint
   - **Description**: The findings from the analysis are compiled into a PowerPoint presentation to clearly communicate insights. The presentation includes visualizations, analysis of customer engagement trends, and recommendations for optimizing future marketing strategies.

## Tools and Technologies Used

- **Python**:
  - **Pandas**: Data manipulation and analysis
  - **NLTK**: Natural Language Processing (NLP) for text segmentation and sentiment analysis
  - **pyodbc**: Connecting Python to SQL Server for data retrieval
- **SQL Server**: Database management system for data storage and transformation
- **Power BI**: Data visualization tool for building dashboards and reports
- **PowerPoint**: Presentation software for summarizing findings and creating reports
