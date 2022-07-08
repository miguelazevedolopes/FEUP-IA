from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

def getPath(path, file):
    lst = path.split("\\")
    lst = path.split("\\")
    lst.remove('src')
    lst.append('docs')
    lst.append(file)
    return lst

def showWrdCld(lst):
    wordcloud = WordCloud().generate(" ".join(lst))

    plt.figure()
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


def getStopWords():
    stop_words = list(set(stopwords.words('english')))
    filter = "'t"
    for word in stop_words:
        if filter in word:
            stop_words.remove(word)

    stop_words.remove("no")
    stop_words.remove("not")
    stop_words.append("amp")

    return set(stop_words)
