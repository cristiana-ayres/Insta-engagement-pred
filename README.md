# Instagram's Engagement Prediction with Machine Learning | Logistic Regression

Mid Project, in collaboration with Renjith Maniyanipurathu | Ironhack Data Analytics Bootcamp. October-November 2022.

## Overview and Project Definition

The project's intent is to leverage and improve the skills in Machine Learning.

1. MVP:

- Research, collect and analyse experimental data of a topic of interest
- Enrich data, through Web Scraping
- Main Goal: Collect between 30 and 100 observations, and between 5 and 10 features per observation.
- Define which Model/Algorithm best apply for the choosen scenario | Statistical and EDA techniques
- Develop an end-to-end analysis 
- Present results, accordingly, clearly and engangily
- Add-on: Supplement analysis with visual intuiton and highlight insights that the data seems to support | Using Data Visualization, with useful and easy-interpretable plots

2. Requirements:

- Understand what kind of research and analysis had been already done in that area and what kind of interesting remain topics could be still analysed and questioned.
- Choose wisely the source and the universe of datapoints that should provide us the observations and features, considering restrictions such as time, cost and access. 

## Project Process

- Used tools: 
- Programming in Python
- Selenium and Beautiful Soup for acquiring instagram data
- Pandas and Numpy libraries for data analysis 
- Matploblib and Seaborn libraries for Data Visualization
- Tableau for Data Visualization and Dashboard view
- Streamlit library for interactive demonstration

## Step 1: Gathering data

- Through WebScraping, we were able to generate a list of the top 100 most followed celebrities and influencers in Brazil. According to our analysis intention, we decided to restrict the content in national influencers (discarding the international celebrities), and also focus on influencers.
- This step also consisted in collect manually some relevant data of influencers that were inside our universe of interest, but out of the webscraped list.
- The final content had 43 observations with their features.
- WebScraping Source: https://starngage.com/app/global/influencer/ranking/brazil 

## Step 2: Preprocessing data: Data Cleansing, Feature Engineering and Feature Selection

- After analyse the data, trying to find the best relationships or connections between the factor, we were able to decide which Model would be appropriate and how we would develop it. 

## Step 3: Modeling using Logistic Regression

![](https://github.com/cristiana-ayres/Insta-engagement-pred/blob/main/Pictures/logistic_regression.jpg)

## Step 4: Interpreting Results

- Tableau | To interpret and generate some insights, such as observing outliers, how gender can influence on their behaviour on social media, what kind of post are preferred according to thei gender or total followers numbers.
- Streamlit | With a platform created with Streamlit, we were able to generate a interactive webpage where it is possible to predict through real numbers (choosing an Instagram account) what would be the kind of Engagement Activity: High or Low, based on our Logistic Regression model. 

## Data Visualization Analysis and some Insights | Tableau

![](https://github.com/cristiana-ayres/Insta-engagement-pred/blob/main/Pictures/tableau_dashboard_overview.JPG)

![](https://github.com/cristiana-ayres/Insta-engagement-pred/blob/main/Pictures/female_tableau.JPG)

![](https://github.com/cristiana-ayres/Insta-engagement-pred/blob/main/Pictures/male_tableau.JPG)

Source: https://public.tableau.com/app/profile/cristiana.ayres/viz/Project6-Instagram/Instagram

## Demonstration using Streamlit 

<p align="center" width="100%">
  <img width="130%" src="https://github.com/cristiana-ayres/Insta-engagement-pred/blob/main/Pictures/insta_streamlit_gif.gif"/>
</p>

