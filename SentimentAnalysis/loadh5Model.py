#from keras.models import load_model
#loaded_model = load_model('model.h5')

#result = loaded_model.score(X_test, Y_test)
#print(result)
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np
import re
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical

from keras.models import load_model

import warnings
warnings.filterwarnings("ignore")

# load model from single file
model = load_model('D:/Code/Python Code/HSA Project/SentimentAnalysis/model1000003Lrs.h5')




data = pd.read_csv('D:/Code/Python Code/HSA Project/SentimentAnalysis/testDataShort.csv', encoding = "ISO-8859-1")
# Keeping only the neccessary columns
#data = data[['SentimentText']]
#0 = negative; 1 = positive; 2 = neutral
#data = data[data.Sentiment != 2]
data['SentimentText'] = data['SentimentText'].apply(lambda x: x.lower())
data['SentimentText'] = data['SentimentText'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))


#for idx,row in data.iterrows():
#    row[0] = row[0].replace('rt',' ')
    
max_fatures = 2000
tokenizer = Tokenizer(nb_words=max_fatures, split=' ')
tokenizer.fit_on_texts(data['SentimentText'].values)
X = tokenizer.texts_to_sequences(data['SentimentText'].values)
X = pad_sequences(X)
#X = X.shape[2]
#print(X.shape)
#print('*******************')


#compose the LSTM Network
embed_dim = 128
lstm_out = 196

model = Sequential()
model.add(Embedding(max_fatures, embed_dim, input_length = X.shape[1]))
model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
#add layers
model.add(Dense(lstm_out,activation='relu'))#model will output arrays of shape (*, 2)# after the first layer, you don't need to specify# the size of the input anymore:
model.add(Dense(lstm_out,activation='relu'))#model will output arrays of shape (*, 2)
model.add(Dense(2,activation='softmax'))#model will output arrays of shape (*, 2)

model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics = ['accuracy'])
#print(model.summary())



# make predictions
yhat = model.predict(np.array(X))
print(yhat)












