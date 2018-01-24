from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.feature_extraction import text 
from stop_words import get_stop_words
import os

dirPath = os.path.dirname(os.path.realpath(__file__)) 
filePath = dirPath + "\\CleanedTweets\\cristianoronaldoCleaned.txt"
documents = open(filePath, encoding = "utf8")


stop_words = get_stop_words('english')
#stop_words = stop_words.union(["rt", "and", "let", "dru", "dandrufffree", "lachi", "flies", "sunday",  "ravi", "amp", "pooja", "debasmita", "chris", "martin", "arun", "lil", "robski", "brodie", "brady", "dele", "namma", "dru"])
my_list = (["rt", "and", "let", "dru", "dandrufffree", "lachi", "flies", "sunday",  "ravi", "amp", "pooja", "debasmita", "chris", "martin", "arun", "lil", "robski", "brodie", "brady", "dele", "namma", "dru"])

my_stop_words = list(set().union(stop_words, my_list))

vectorizer = TfidfVectorizer(analyzer = u'word', max_df=0.95, lowercase = True, stop_words = my_stop_words, max_features = 15000)
X = vectorizer.fit_transform(documents)
 
true_k = 5
kmeans = KMeans(n_clusters=true_k, init='k-means++', max_iter=1000, n_init=10, random_state=3426).fit(X)


 
print("Top terms per cluster:")
order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]: #this is the number of words in each cluster
        print('%s' % terms[ind].encode("utf-8")),
   

 