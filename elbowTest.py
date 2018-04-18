import pandas
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import adjusted_rand_score
from stop_words import get_stop_words

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

filePath = "D:/Code/Python Code/HSA Project/CleanedTweets/allWomensTweetsCleanedNoHT.txt"
documents = open(filePath, encoding = "utf8") 
vectorizer = TfidfVectorizer(min_df =2, max_df=0.6, lowercase = True, stop_words = my_stop_words, max_features = 500000)
Y = vectorizer.fit_transform(documents)

Nc = range(1, 10)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]
score
pl.plot(Nc,score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')
pl.show()