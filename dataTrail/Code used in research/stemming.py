from nltk.stem import PorterStemmer

documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]
			 
porter = PorterStemmer()
documents = [[porter.stem(word) for word in sentence.split(" ")] for sentence in documents]
for x in range(len(documents)):
    print (documents[x]),