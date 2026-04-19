
# Spam Email & SMS Classifier (ML Project)

## About the Project

Nowadays, we get a lot of unwanted emails and messages, so detecting spam is very important. In this project, I built a Machine Learning model that can classify messages as **Spam** or **Ham (not spam)**.

This is an end-to-end project where I worked on everything—from cleaning the data and applying NLP techniques to training models and finally deploying it using Streamlit.

## Features

* User can enter any email or message and check if it’s spam or not
* Text preprocessing like removing punctuation, stopwords, etc.
* Model is trained in a way that focuses more on **precision** so that important messages are not marked as spam


## Tech Stack

* Python
* pandas, numpy
* nltk (for text processing)
* scikit-learn (for ML models)
* matplotlib, seaborn (for visualization)
* streamlit (for web app)

## Workflow

1. Cleaned the dataset and converted labels (spam = 1, ham = 0)
2. Did basic EDA to understand the data
3. Used TF-IDF to convert text into numerical form
4. Trained different models like:

   * Naive Bayes
   * Logistic Regression
   * SVM
5. After tuning, SVM gave the best results with around **98% accuracy** and **99% precision**
