import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
from keras import optimizers
from keras.layers.normalization import BatchNormalization
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from keras.utils.np_utils import to_categorical
import re
import pickle
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('D:/Code/Python Code/HSA Project/SentimentAnalysis/testDataMedium.csv', encoding = "ISO-8859-1")
# Keeping only the neccessary columns
data = data[['SentimentText','Sentiment']]
#0 = negative; 1 = positive; 2 = neutral
#data = data[data.Sentiment != 2]
data['SentimentText'] = data['SentimentText'].apply(lambda x: x.lower())
data['SentimentText'] = data['SentimentText'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))

print('Positive: ' + str(data[ data['Sentiment'] == 1].size))
print('Negative: ' + str(data[ data['Sentiment'] == 0].size))

for idx,row in data.iterrows():
    row[0] = row[0].replace('rt',' ')
    
max_fatures = 2000
tokenizer = Tokenizer(nb_words = max_fatures, split=' ')
tokenizer.fit_on_texts(data['SentimentText'].values)
X = tokenizer.texts_to_sequences(data['SentimentText'].values)
X = pad_sequences(X)
print('***************')
#print(X)
#Normalise the data?
#X = preprocessing.normalize(X)		why pos and neg give high numbers???????????????????????????
#print(X)


#compose the LSTM Network
embed_dim = 128
lstm_out = 196

model = Sequential()
model.add(Embedding(max_fatures, embed_dim, input_length = X.shape[1]))#Turns positive integers (indexes) into dense vectors of fixed size. eg. [[4], [20]] -> [[0.25, 0.1], [0.6, -0.2]]
# max_fatures - the largest integer (i.e. word index) in the input should be no larger than 999 (vocabulary size).
#embed_dim - Dimension of the dense embedding.
model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
#add layers
#model.add(Dense(lstm_out,activation='relu'))#model will output arrays of shape (*, 2)# after the first layer, you don't need to specify the size of the input anymore.
#model.add(Dense(lstm_out,activation='relu'))
model.add(Dense(2,activation='softmax'))#model will output arrays of shape (*, 2)
#model.add(BatchNormalization())
rmsprop = optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0)
model.compile(loss = 'categorical_crossentropy', optimizer = rmsprop, metrics = ['accuracy'])
print(model.summary())


#Here I declare the train and test dataset.
Y = pd.get_dummies(data['Sentiment']).values
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.33, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)

#Here we train the Network.
batch_size = 32
model.fit(X_train, Y_train, nb_epoch = 7, batch_size=batch_size, verbose = 2)# 0 = silent, 1 = progress bar, 2 = one line per epoch.

# save the model to disk
filename = 'D:/Code/Python Code/HSA Project/SentimentAnalysis/model10epoch.h5'
model.save(filename) 

#Extracting a validation set, and measuring score and accuracy.
validation_size = 200
X_validate = X_test[-validation_size:]
Y_validate = Y_test[-validation_size:]
X_test = X_test[:-validation_size]
Y_test = Y_test[:-validation_size]
score,acc = model.evaluate(X_test, Y_test, verbose = 2, batch_size = batch_size)
print("score: %.2f" % (score))
print("acc: %.2f" % (acc))


#Finally measuring the number of correct guesses.
pos_cnt, neg_cnt, pos_correct, neg_correct = 0, 0, 0, 0
for x in range(len(X_validate)):
    
    result = model.predict(X_validate[x].reshape(1,X_test.shape[1]),batch_size=1,verbose = 2)[0]
   
    if np.argmax(result) == np.argmax(Y_validate[x]):
        if np.argmax(Y_validate[x]) == 0:
            neg_correct += 1
        else:
            pos_correct += 1
       
    if np.argmax(Y_validate[x]) == 0:
        neg_cnt += 1
    else:
        pos_cnt += 1



print("pos_acc", pos_correct/pos_cnt*100, "%")
print("neg_acc", neg_correct/neg_cnt*100, "%")


















