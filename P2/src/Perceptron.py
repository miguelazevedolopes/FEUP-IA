from sklearn.linear_model import Perceptron
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
import numpy as np
from sklearn.model_selection import PredefinedSplit
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#67% pure
def Percep(X, y, X_test, y_test):
    print("\n\n  ________________________________ ")
    print("\n Perceptron:\n")

    clf = Perceptron()

    # TODO: SPLIT TRAIN DATASET IN TRAIN/TEST 70/30

    X_train, X_trainTest, y_train, y_trainTest = train_test_split(X, y, test_size=0.3, random_state=0)

    train_indices = np.full((len(X_train),), -1, dtype=int)
    print("len train indices: ", len(train_indices))

    test_indices = np.full((len(X_trainTest),), 0, dtype=int)
    print("len test indices: ", len(test_indices))

    test_fold = np.append(train_indices, test_indices)

    pdfsplt = PredefinedSplit(test_fold)

    print(pdfsplt.get_n_splits())

    param_grid = {"alpha": [0.005, 0.01, 0.05]}

    grid = GridSearchCV(clf, param_grid, cv=pdfsplt)

    print("Len x: ", len(X))
    print("Len x_test: ", len(X_test))

    grid.fit(X, y)

    print("best parameters: ", grid.best_params_) #0.005 - 96,6%

    print("Best score: ", grid.best_score_)

    y_pred = grid.predict(X_test)

    # confusion matrix
    labels = ["anger", "fear", "joy"]
    cm = confusion_matrix(y_test, y_pred)
    cmd_obj = ConfusionMatrixDisplay(cm, display_labels=labels)
    cmd_obj.plot()
    cmd_obj.ax_.set(
        title='Confusion Matrix (Perceptron)',
        xlabel='Predicted Emotion',
        ylabel='Actual Emotion')
    print("Confusion matrix:")
    plt.show()

    # accuracy
    print("\nAccuracy:")
    print(accuracy_score(y_test, y_pred))

    # precision
    print("\nPrecision:")
    print(precision_score(y_test, y_pred, average=None))  # TODO: We have multiple average options

    # recall
    print("\nRecall:")
    print(recall_score(y_test, y_pred, average=None))  # TODO: We have multiple average options

    # f1
    print("\nf1:")
    print(f1_score(y_test, y_pred, average=None))  # TODO: We have multiple average options

    #clf = SVC()
    #scores = cross_val_score(clf, X, y, cv=10)

    #print(scores)
    #print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))