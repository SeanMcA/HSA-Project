import pandas
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import adjusted_rand_score


filePath = "D:/Code/Python Code/TestingTextClusterAnalysis/allMensEnglishTweetscleanedInProgress.txt"
documents = open(filePath, encoding = "utf8") 
vectorizer = TfidfVectorizer(stop_words='english')
Y = vectorizer.fit_transform(documents)

Nc = range(1, 100)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]
score
pl.plot(Nc,score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')
pl.show()