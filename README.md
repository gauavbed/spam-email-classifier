

# Spam Email & SMS Classifier

## Project Overview

In this project, I built a Machine Learning model that can classify emails or SMS messages as **Spam** or **Ham (not spam)**.

With the increasing number of unwanted messages, spam detection has become an important problem. Through this project, I implemented a complete ML pipeline starting from data cleaning and preprocessing to model building and deployment using Streamlit.

## Features

* User can enter any message and check whether it is spam or not
* Automatic text preprocessing (lowercasing, removing punctuation and stopwords, etc.)
* Model is optimized for **high precision** to avoid marking important messages as spam
* Simple and easy-to-use web interface

## Technologies Used

* Python
* pandas, numpy
* nltk (for text preprocessing)
* scikit-learn (for model building)
* matplotlib, seaborn (for visualization)
* streamlit (for deployment)

  
## Workflow

1. **Data Cleaning**

   * Handled missing values
   * Encoded labels (spam = 1, ham = 0)

2. **Exploratory Data Analysis (EDA)**

   * Analyzed word frequency
   * Compared spam and ham messages

3. **Text Preprocessing**

   * Converted text to lowercase
   * Tokenization
   * Removed stopwords
   * Applied lemmatization

4. **Feature Engineering**

   * Used TF-IDF vectorization to convert text into numerical form

5. **Model Training**

   * Trained multiple models:

     * Naive Bayes
     * Logistic Regression
     * Support Vector Machine (SVM)

6. **Model Selection**

   * SVM performed the best
   * Achieved around **98% accuracy** and **99% precision**
   

## How to Run the Project

bash id="a7d92x"
git clone https://github.com/your-username/spam-email-classifier.git
cd spam-email-classifier
pip install -r requirements.txt
streamlit run app.py

If you want, I can also make a **short version (for resume projects)** or help you answer **interview questions based on this project** 👍
