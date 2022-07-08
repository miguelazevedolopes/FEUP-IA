## Requirements

Before running the program you must install the following packages:

- xgboost

You can install them using the following command:

```
pip install package_name
```

In the first run it is needed to uncomment the *nltk.download('stopwords')* line (5th line).

You also need to make sure that the src folder and the docs folder have the same relative path. If not, the program
cannot read the .csv datasets.

## Run the program

Execute "python3 nlp.py" on the src folder.

## Use the program

Depending on the functions uncommented, the program runs any of these 7 classifiers:

- Naïve Bayes;
- Decision Tree;
- Random Forest;
- SVC;
- Perceptron;
- Logistic Regression;
- XGB

To see each classifier, simply run the program, each time with only one of these classifiers uncommented.