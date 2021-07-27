from tensorflow.keras.datasets import fashion_mnist
import numpy as np
import matplotlib.pyplot as plt
from icecream import ic

### cnn -> dnn

#1. 데이터
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
# print(x_train.shape, y_train.shape)   # (60000, 28, 28) (60000,)
# print(x_test.shape, y_test.shape)     # (10000, 28, 28) (10000,)

x_train = x_train.reshape(60000, 28, 28)
x_test = x_test.reshape(10000, 28, 28)

ic(np.unique(y_train))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)

#1-2. 데이터 전처리
from sklearn.preprocessing import OneHotEncoder
onehot = OneHotEncoder()
onehot.fit(y_train)
y_train = onehot.transform(y_train).toarray()  # (60000, 10
y_test = onehot.transform(y_test).toarray()   # (10000, 10)
ic(y_train.shape, y_test.shape)


#2. 모델 구성
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten, LSTM, Conv1D
# model = Sequential()
# # dnn
# model.add(LSTM(128, activation='relu', input_shape=(28, 28), return_sequences=True))
# model.add(Conv1D(64, 2, activation='relu'))
# model.add(Flatten())
# model.add(Dense(128, activation='relu'))
# model.add(Dense(128, activation='relu'))
# model.add(Dense(64, activation='relu'))
# model.add(Dense(100, activation='relu'))
# model.add(Dense(128, activation='relu'))
# model.add(Dense(64, activation='relu'))
# model.add(Dense(32, activation='relu'))
# model.add(Dense(10, activation='softmax'))

# model.summary()


#3. 컴파일(ES), 훈련
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
# es = EarlyStopping(monitor='val_loss', patience=8, mode='min', verbose=1)
# cp = ModelCheckpoint(monitor='val_loss', mode='auto', save_best_only=True, filepath='./_save/ModelCheckPoint/keras48_7_MCP.hdf5')

# import time
# start = time.time()
# model.fit(x_train, y_train, epochs=1000, batch_size=512, validation_split=0.001, callbacks=[es, cp])
# end = time.time() - start

# model.save('./_save/ModelCheckPoint/keras48_7_model_save.h5')

# model = load_model('./_save/ModelCheckPoint/keras48_7_MCP.h5')          # save model
model = load_model('./_save/ModelCheckPoint/keras48_7_MCP.hdf5')        # checkpoint

#4. 평가, 예측
results = model.evaluate(x_test, y_test)
# print('걸린시간 :', end)
print('category :', results[0])
print('accuracy :', results[1])

'''
*cnn
category : 0.42756807804107666
accuracy : 0.91839998960495

*dnn
걸린시간 : 75.93847155570984
category : 0.3571701943874359
accuracy : 0.886900007724762

*LSTM
걸린시간 : 141.8664379119873
category : 1.4018232822418213
accuracy : 0.4546000063419342

*LSTM + Conv1D
걸린시간 : 162.72723007202148
category : 0.8386392593383789
accuracy : 0.6711999773979187

*save model
걸린시간 : 187.3428933620453
category : 0.5221372246742249
accuracy : 0.8061000108718872

*checkpoint
category : 0.5989198684692383
accuracy : 0.7785999774932861
'''