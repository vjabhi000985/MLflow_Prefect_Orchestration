import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.neighbors import KNeighborsClassifier

from sklearn.pipeline import Pipeline
from sklearn import metrics
from prefect import task, flow

@task
def load_data(file_path):
    """
    Load data from a CSV file.
    """
    return pd.read_csv(file_path)

@task
def split_inputs_output(data, inputs, output):
    """
    Split features and target variables.
    """
    data = data.dropna(subset=[inputs])
    X = data[inputs]
    y = data[output]
    return X, y


@task
def split_train_test(X, y, test_size=0.2, random_state=42):
    """
    Split data into train and test sets.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

@task
def preprocess_data(X_train, X_test, y_train, y_test):
    """
    Preprocess the data.
    """
    vocab = CountVectorizer()
    X_train_preprocess = vocab.fit_transform(X_train)
    X_test_preprocess = vocab.transform(X_test)
    return X_train_preprocess, X_test_preprocess, y_train, y_test


@task
def train_model(X_train_preprocess, y_train,hyperparameters):
    """
    Training the machine learning model.
    """
    clf = KNeighborsClassifier(metric='cosine', **hyperparameters)
    clf.fit(X_train_preprocess, y_train)
    return clf

@task
def evaluate_model(model, X_train_preprocess, y_train, X_test_preprocess, y_test):
    """
    Evaluating the model.
    """
    y_train_pred = model.predict(X_train_preprocess)
    y_test_pred = model.predict(X_test_preprocess)

    train_score = metrics.accuracy_score(y_train, y_train_pred)
    test_score = metrics.accuracy_score(y_test, y_test_pred)
    
    return train_score, test_score

# Workflow

@flow(name="KNN Training Flow")
def workflow():
    DATA_PATH = "C:/Users/vjavi/Desktop/my_flask_projects/MLflow_Prefect_Orchestration/dataset/my_data.csv"
    INPUTS = 'Review text'
    OUTPUT = 'Sentiment'
    HYPERPARAMETERS = {
    'n_neighbors': 3,
    'p': 3
    }

    # Load data
    badmintion = load_data(DATA_PATH)

    # Identify Inputs and Output
    X, y = split_inputs_output(badmintion, INPUTS, OUTPUT)

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = split_train_test(X, y)

    # Preprocess the data
    X_train_preprocess, X_test_preprocess, y_train, y_test = preprocess_data(X_train, X_test, y_train, y_test)

    # Build a model
    model = train_model(X_train_preprocess, y_train, HYPERPARAMETERS)
    
    # Evaluation
    train_score, test_score = evaluate_model(model, X_train_preprocess, y_train, X_test_preprocess, y_test)
    
    print("Train Score:", train_score)
    print("Test Score:", test_score)

if __name__ == "__main__":
    workflow()