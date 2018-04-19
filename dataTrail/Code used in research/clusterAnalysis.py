from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.feature_extraction import text 
from stop_words import get_stop_words
from scipy.cluster.hierarchy import dendrogram, linkage
import os

dirPath = os.path.dirname(os.path.realpath(__file__)) 
filePath = dirPath + "\\CleanedTweets\\allMensTweetsCleanedNoHT.txt"

documents = open(filePath, encoding = "utf8")

stop_words = get_stop_words('english')

my_list = ([
"easter","xx",
"san","juan",
"leo","decided",
"rt", "and", "let", "dru", "dandrufffree", "lachi", 
"flies", "sunday",  "ravi", "amp", "arun", "lil", 
"come", "just", "nah", "know", "care",
"taken", "one", "nice",  "go", "ok", "flexfriday", "see",
"950", "915", "saw", "need","cr7","250", "already",
"en", "de", "el","la", "muy",
"find","now",
"mean", "doesn", "ain","take", "made","thoughts",
"relly", "rj", "yeah",
"flip", "real", "big", "back", "time",
"feliz", "zo", 
"ive", "ur", "fav", "fave", "even", "get", "day", "sir", "yes", "comes",  
"now", "new", "man", "yet", "lock", "fantasy", "fax",  "getting",
"goes", "fart", "farther", "can", "keep", "don", "well", 
"much", "seems", "us", "like", "five", "fc", "will",
"going", "far", "give", "zoom", "always", "another",
"keeps", "soon", "re", "lol", "wireless", "space", "last,"
"looking", "make", "thing", "please", "aww", "awee", "everything",
"youuuu", "youuu", "rahul", "extravagant", "extremely", "extra", "finally",
"zverev", "put", "putting",  "two", "zouk", "theyre", "met", "lot", "looks", "em", 
"lisbon", "portugal", "got", "im", "lets", "fa", "fab", "orrrrrr", "boxes", "days", "way", "couldnt",
"zne",  "eye", "24", "almost", "ct", "et", "de", "la", "120", "31", "ppl", "next", "25", "dont", "lots", "whos",
"chris", "martin", "pooja", "debasmita", "robski", "brodie", "brady", "gareth", "southgate", "kyrie", "irving", "jimmy", "billy", "stephen", "curry",
"Annie", "Leibovitz", "prarthna", "thombare", "zoey", "faye", "nelson", "mandela", "cassius", "isco", "kroos", "carmelo", "anthony",
"dele", "namma", "dru"])

my_stop_words = list(set().union(stop_words, my_list))

#vectorizer = TfidfVectorizer(analyzer = u'word', max_df=0.3, lowercase = True, stop_words = my_stop_words, max_features = 15000, ngram_range = ( 1, 4 ))
vectorizer = TfidfVectorizer(analyzer = u'word',  min_df =2, max_df=0.95, lowercase = True, stop_words = my_stop_words, max_features = 20000)
#min_df is used for removing terms that appear too infrequently. 
#min_df = 5 means "ignore terms that appear in less than 5 documents".
#min_df = 0.01 means "ignore terms that appear in less than 1% of the documents".
#max_df is used for removing terms that appear too frequently, also known as "corpus-specific stop words". For example:
#max_df = 0.50 means "ignore terms that appear in more than 50% of the documents".

X = vectorizer.fit_transform(documents)


true_k = 5 # this is the number of clusters
kmeans = KMeans(n_clusters=true_k, init='k-means++', max_iter=300, n_init=10, random_state=1000).fit(X)#3426
#Number of time the k-means algorithm will be run with different centroid seeds. 
#The final results will be the best output of n_init consecutive runs in terms of inertia.
#Maximum number of iterations of the k-means algorithm for a single run
#If int, random_state is the seed used by the random number generator;


 
print("Top terms per cluster:")
order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :6]: #this is the number of words in each cluster
        print('%s' % terms[ind].encode("utf-8")),
   


 
 