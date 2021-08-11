import numpy as np
from sklearn.datasets import load_iris
from icecream import ic
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from sklearn.svm import LinearSVC, SVC
from sklearn.neighbors import KNeighborsClassifier  #, KNeighborsRegressor     # 분류면 KNeighborsClassifier, 회귀면 KNeighborsRegressor
from sklearn.linear_model import LogisticRegression     # *** LogisticRegression : 분류모델 임!!!!!!!!!!!!!!!!!(이름에 Regression이 들어간다고 회귀모델 아님!!!!!!!!!!!!!!)
from sklearn.tree import DecisionTreeClassifier     # 의사결정나무
from sklearn.ensemble import RandomForestClassifier # DecisionTree의 앙상블 모델 : 숲(Foreset)
import warnings
warnings.filterwarnings('ignore')
from sklearn.metrics import accuracy_score

### 실습  m07최적의 파라미터 값으로 모델 구성

datasets = load_iris()
print(datasets.DESCR)
print(datasets.feature_names)

# 1. 데이터
x = datasets.data
y = datasets.target
ic(x.shape, y.shape)  # (150, 4), (150,)->(150, 3)
ic(y)   # (0,0,0, ... ,1,1,1, ... ,2,2,2, ...)

from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV         # GridSearchCV : 체로 걸러서 찾겠다, CV(cross_val_score)까지 하겠다!!
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, shuffle=True, random_state=66)
n_split = 5
kfold = KFold(n_splits=n_split, shuffle=True, random_state=66)     # n_splits=5   5등분하겠다!  ->   값도 5(n)개로 나옴

parameters = [    # 딕셔너리 형태
    {"C":[1, 10, 100, 1000], "kernel":["linear"]},
    {"C":[1, 10, 100], "kernel":['rbf'], "gamma":[0.001, 0.0001]},
    {"C":[1, 10, 100, 1000], "kernel":["sigmoid"], "gamma":[0.001, 0.0001]}
    ]

# 2. 모델(머신러닝에서는 정의만 해주면 됨)  GridSearchCV로 모델(SVC) 감싸줌
model = SVC(C=1, kernel='linear')


# 3. 훈련(cross_val_score 은 fit과 score가 포함되어 있음)
model.fit(x_train, y_train)


# 4. 평가(evaluate 대신 score 사용함!!), 예측
# print("최적의 매개변수 :", model.best_estimator_)
# print("best_score :", model.best_score_)



print("model.score :", model.score(x_test, y_test))

y_predict = model.predict(x_test)
print("accuracy_score :", accuracy_score(y_test, y_predict))

'''
최적의 매개변수 : SVC(C=1, kernel='linear')
best_score : 0.9714285714285715     - cv(train, test 데이터)
model.score : 0.9555555555555556    - acc(test 데이터)
accuracy_score : 0.9555555555555556 - acc(test 데이터)

최적의 매개변수를 모델에 사용
model.score : 0.9555555555555556
accuracy_score : 0.9555555555555556
'''
