#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud
from stop_words import get_stop_words

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'D:/Code/Python Code/HSA Project/wordCloud/allMensTweetsCleanedNoHT.txt')).read()

stop_words = get_stop_words('english')
my_list = ([
"thank", "great",
"rt", "and", "let", "dru", "dandrufffree", "lachi", 
"flies", "sunday",  "ravi", "amp", "arun", "lil", 
"come", "just", "nah", "know", "care",
"taken", "one", "nice",  "go", "ok", "flexfriday", "see",
"flip", "real", "big", "back", "time",
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
# Generate a word cloud image
wordcloud = WordCloud(stopwords = my_stop_words).generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
#wordcloud = WordCloud(max_font_size=40).generate(text)
#plt.figure()
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()















