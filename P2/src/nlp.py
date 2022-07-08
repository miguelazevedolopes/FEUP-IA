import pandas as pd
import os
import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_val_score
from nltk.corpus.reader.knbc import test
import utils

import NaiveBayes
import DecisionTree
import RandomForest
import SVC
import LogisticRegression
import Perceptron
import XGBoost

if __name__ == "__main__":
    # This certifies that the path is always correct for someone running this program
    path = os.getcwd()
    lst = utils.getPath(path, 'Emotions.csv')
    lst2 = utils.getPath(path, 'Testingdata.csv')

    dataset = pd.read_csv("/".join(lst), encoding='cp1252')
    dataset.drop_duplicates(subset="Statement", keep='first', inplace=True)
    datasetTest = pd.read_csv("/".join(lst2), encoding='cp1252')
    datasetTest.drop_duplicates(subset="Statement", keep='first', inplace=True)

    dataset.info()

    # Check if everything looks alright
    # 3 emotions: fear, anger and joy
    print('\nFear count:\n')
    print((dataset['Emotion'] == 'fear').value_counts(normalize=True))
    dataset_fear = [(dataset['Emotion'] == 'fear')]
    print('\nAnger count:\n')
    print((dataset['Emotion'] == 'anger').value_counts(normalize=True))
    dataset_anger = [(dataset['Emotion'] == 'anger')]
    print('\nJoy count:\n')
    print((dataset['Emotion'] == 'joy').value_counts(normalize=True))
    dataset_joy = [(dataset['Emotion'] == 'joy')]

    #print(datasetTest)

    corpus = []
    ps = PorterStemmer()
    for index, row in dataset.iterrows():
        # replace asterisk for empty
        review = re.sub('\*', '', row['Statement'])
        # remove non alpha chars
        review = re.sub('[^a-zA-Z]', ' ', review)
        # to lower case
        review = review.lower()
        # split into tokens, apply stemming and remove stop words
        review = ' '.join([ps.stem(w) for w in review.split() if not w in utils.getStopWords()])
        corpus.append(review)

    stop_words = utils.getStopWords()
    for i in range(0, len(corpus)):
        review = corpus[i].split()
        review = [word for word in review if word not in stop_words]
        corpus[i] = ' '.join(review)

    #showWrdCld(corpus)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus).toarray()
    y = dataset['Emotion']

    # TODO: We probably want to customise stopwords set
    # TODO: Maybe would be interesting to remove asterisk and join both parts? Ex: fu*k -> fuk

    test_corpus = []
    for index, row in datasetTest.iterrows():
        # replace asterisk for empty
        review = re.sub('\*', '', row['Statement'])
        # remove non alpha chars
        review = re.sub('[^a-zA-Z]', ' ', review)
        # to lower case
        review = review.lower()
        # split into tokens, apply stemming and remove stop words
        review = ' '.join([ps.stem(w) for w in review.split() if not w in utils.getStopWords()])
        test_corpus.append(review)

    stop_words = utils.getStopWords()
    for i in range(0, len(test_corpus)):
        review = test_corpus[i].split()
        review = [word for word in review if word not in stop_words]
        test_corpus[i] = ' '.join(review)

    X_test = vectorizer.transform(test_corpus).toarray()
    y_test = datasetTest['Emotion']

    #NaiveBayes.NaiveBayes(X, y, X_test, y_test)

    #DecisionTree.DecisionTree(X, y, X_test, y_test)

    RandomForest.RandForest(X, y, X_test, y_test)

    #SVC.Svc(X, y, X_test, y_test)

    #LogisticRegression.LogRegr(X, y, X_test, y_test)

    #Perceptron.Percep(X, y, X_test, y_test)

    #XGBoost.xgb(X, y, X_test, y_test)


