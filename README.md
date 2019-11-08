# Client Project: Identifying Major Electrical Disturbances in the U.S. Using Social Media Posts

Author: [Creighton Ashton](https://www.linkedin.com/in/creightonashton/), [Meroe Yadollahi](https://www.linkedin.com/in/meroe-yadollahi/), [Jack Wang](https://www.linkedin.com/in/jackweijiawang/)

---

## Problem Statement: 

The traditional method to spot a power outage/electrical disturbance is to check the live feeds provided by major utility companies or the satellite data that capture the extent of light emitted at night. We will build a tool that identifies the major electrical disturbances using social media posts. Unlike the traditional methods, our tool will identify major electrical disturbances more timely.

---

## Executive Summary

The goal of this project is to develop a tool that will scan twitter for certain posts containing power outage keywords and build a classification model in order to predict which areas are most likely to be suffering from a power outage. The power outage data will be collected on [the U.S. Department of Energy website](https://www.oe.netl.doe.gov/OE417_annual_summary.aspx), the weather data will be collected on [National Oceanic and Atmospheric Administration](https://www.ncdc.noaa.gov/data-access/severe-weather), and we will scrape historical twitter posts on [Twitter](https://twitter.com) to form our twitter data. We will build different types of classification models and select the best model based on the recall score, F1 score, accuracy score of the models.

---

## Software Requirements

Codes are written in Jupyter Notebook with Python language. Users are recommended to know Python libraries including `Numpy`, `Pandas`, classification models in `Scikit-learn`, visualization with `matplotlib`, and the knowledge of supervised machine learning.

---

## Content (Jupyter Notebooks)

User should follow the below order to read through our work, all notebooks have description for each step:

### 1. Data Collection

As mentioned in executive summary, we collected our data on [the U.S. Department of Energy website](https://www.oe.netl.doe.gov/OE417_annual_summary.aspx), [National Oceanic and Atmospheric Administration](https://www.ncdc.noaa.gov/data-access/severe-weather), and we scraped posts on [Twitter](https://twitter.com) by using twitter scraper. Our main focus is the power outage data and the twitter data because we built our model based on these two data. The weather data we collected is for EDA purpose. The inutition is our findings from power outage data. 

**Below are the Jupyter Notebook for Data Collection:**
- [Twitter_Scraper](./Code/Twitter_Scraper.ipynb)
- [Power Outage Data](./Code/power-outage-data.ipynb)
- [Weather Data](./Code/Weather_Data.ipynb)

### 2. Data Cleaning & Merging

We did the data cleaning by dropping missing values, checking data types, and dropping the columns/features we don't need. For twitter data, we cleaned it up by removing hyper links, words not making sense, and we have tried PorterStemmer.

**Below are the Jupyter Notebook for Data Collection:**
- [Cleaned Twitter Data](./Code/twitter_cleaning.ipynb)
- [Combining Data (power outage and twitter)](./Code/Combining_Data.ipynb)

### 3. EDA

EDA

**Below are the Jupyter Notebook for Data Collection:**
- [Twitter EDA](./Code/Twitter_EDA.ipynb)
- [Weather & Power Outage EDA](./Code/Weather_PowerOutage_EDA.ipynb)
- [Word2Vec](./Code/Word2Vec.ipynb)


### 4. Modeling & Pickle

**Below are the Jupyter Notebook for Data Collection:**
- [Modeling](./Code/Modeling.ipynb)
- [Pickle](./Code/Pickle.ipynb)

### 5. Final Product

**Below are the Jupyter Notebook for Data Collection:**
- [Final Product](./Code/App_development.ipynb)

---

## Conclusion

Our final classification model is not performing pretty well since it only has 64.36% F1 score and 63.13% recall score. However, it is understandable because we are limited by the number of data we have so we could not train our model effectively. The power outage data we have does not line up well with our twitter data because most of the posts on twitter are about local power outages, where our power outage data are major electrical power outages. We could not find useful local power outage historical data because most utility companies tend to not give out historical power outage datas, they only provide live feeds of power outage events. As a consequence, our model is more conservative when it is predicting the major electrical disturbances. 

To improve our model, we definitely need more data and also more detail of the power outage datas. Most of our power outage data only has location that is state-level, which gave us a hard time matching the twitter posts to the power outage event. Another thing we can work on is the keyword selection. We included "blackout" as one of the keywords we scrape from Twitter, which ends up giving us a lot of noises. For example, we have people who are drunk and "blackout".

---

## Sources

- [the U.S. Department of Energy](https://www.oe.netl.doe.gov/OE417_annual_summary.aspx)
- [National Oceanic and Atmospheric Administration](https://www.ncdc.noaa.gov/data-access/severe-weather)
- [Using word2vec to Analyze News Headlines and Predict Article Success](https://towardsdatascience.com/using-word2vec-to-analyze-news-headlines-and-predict-article-success-cdeda5f14751)
- [7 Techniques to Handle Imbalanced Data](https://www.kdnuggets.com/2017/06/7-techniques-handle-imbalanced-data.html)
- [twitterscraper](https://github.com/taspinar/twitterscraper)