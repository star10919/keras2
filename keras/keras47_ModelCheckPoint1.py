import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from icecream import ic
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

### ES의 단점 : patience까지 밀려남 을 보완하기 위하여 ModelCheckPoint사용 - model.fit에서 함

#1. 데이터
datasets = load_diabetes()

x = datasets.data
y = datasets.target

ic(x.shape, y.shape)  # (442, 10)  (442,)

ic(datasets.feature_names)   
#['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
ic(datasets.DESCR)

ic(x[:30])
ic(np.min(y), np.max(y))

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, shuffle=True, random_state=9)
# x_train, x_val, y_train, y_val = train_test_split(x_test, y_test, train_size=0.8, shuffle=True, random_state=9)

#1-2. x 데이터 전처리
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
# x_val = scaler.transform(x_val)


#2. 모델구성(validation)
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
model = Sequential()
model.add(Dense(128, input_shape=(10,), activation='relu'))  #relu : 음수값은 0, 양수만 제대로 잡음
# model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(64, activation='relu'))
# model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1))

# 컴파일 x, fit x 모델 - 가중치 정해지지 않음(only model만 저장됨)
# model = load_model('./_save/keras46_1_save_model_1.h5')   # Total params: 8,865

# 컴파일 o, fit o 모델 - 가중치 정해짐(값 계속 똑같음)
# model = load_model('./_save/keras46_1_save_model_2.h5')   # Total params: 8,865



# model.save('./_save/keras46_1_save_model_1.h5')
# model.save_weights('./_save/keras46_1_save_weight_1.h5')

# model = load_model('./_save/keras46_1_save_weight_1.h5')
# model = load_model('./_save/keras46_1_save_weight_2.h5')


model.summary()

# model.load_weights()

# #3. 컴파일(ES), 훈련
model.compile(loss='mse', optimizer='adam')

from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
es = EarlyStopping(monitor='val_loss', patience=3, mode='min', verbose=1)
cp = ModelCheckpoint(monitor='val_loss', save_best_only=True, mode='auto', filepath='./_save/ModelCheckPoint/keras47_MCP.hdf5')

import time
start = time.time()
model.fit(x_train, y_train, epochs=100, batch_size=10, validation_split=0.7, verbose=1, callbacks=[es, cp])
end = time.time() - start

model.save('./_save/ModelCheckPoint/keras47_model_save.h5')

#4. 평가, 예측(mse, r2)
loss = model.evaluate(x_test, y_test)
print("걸린시간 :", end)
ic(loss)

y_predict = model.predict(x_test)
r2 = r2_score(y_test, y_predict)
ic(r2)


# 과제 0.62까지 올려라!
'''
결과값
ic| loss: 2092.216552734375
ic| r2: 0.6214054692239842

*x 전처리
걸린시간 : 3.319180727005005
ic| loss: 1291.806396484375
ic| r2: 0.7662427290354967

*load model
걸린시간 : 3.487668037414551
ic| loss: 1371.6661376953125
ic| r2: 0.7517918267211269
'''