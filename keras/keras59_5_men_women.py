### 실습1. - men women 데이터로 모델링을 구성할 것!

### 실습2. - 본인 사진으로 predict 하시오! D 드라이브 안에 본인 사진 넣고, 내가 여자 몇%인지 acc -수치 넣는 거는 찾아서/ 결과값 스크린샷으로 만들어서 메일보내기

import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

## ImageDataGenerator로 데이터 증폭시키기
train_datagen = ImageDataGenerator(
    rescale=1./255,
    horizontal_flip=True,
    vertical_flip=True,
    width_shift_range=0.1,
    height_shift_range=0.1,
    rotation_range=5,
    zoom_range=1.2,
    shear_range=0.7,
    fill_mode='nearest',
    )

# ImageDataGenerator로 데이터 증폭시키기 - test는 증폭시키지 않음
test_datagen = ImageDataGenerator(rescale=1./255)





## 이미지 x, y로 불러오기
xy_train = train_datagen.flow_from_directory(# x와 y가 동시에 생성됨
    '../data/men_women',      # 이미지가 있는 폴더 지정이 아닌 상위 폴더(동일한 급의 라벨이 모여있는 폴더까지)로 지정   # train(ad/normal)
    target_size=(150, 150),     # 임의대로 크기 조정
    batch_size=200,               # y 하나의 개수
    class_mode='binary',        # 이상이 있다-라벨 / 이상이 없다-라벨 : 이진분류
    shuffle=False               # 셔플 디폴트 : 트루
)
# Found 160 images belonging to 2 classes.


xy_test = test_datagen.flow_from_directory(
    '../data/men_women',      
    target_size=(150, 150),     
    batch_size=200,       
    class_mode='binary'         
)
# Found 120 images belonging to 2 classes.




# ## 프린트
# # print(xy_train)
# # <tensorflow.python.keras.preprocessing.image.DirectoryIterator object at 0x000001CE349F8550>

# # print(xy_train[0])          # x값, y값
# print(xy_train[0][0])       # x값
# print(xy_train[0][1])       # y값
# # print(xy_train[0][2])     # 없음                       
# print(xy_train[0][0].shape, xy_train[0][1].shape)       # (160, 150, 150, 3) (160,)
# print(xy_test[0][0].shape, xy_test[0][1].shape)       # (120, 150, 150, 3) (120,)


# # print(xy_train[31][1])      # 마지막 배치 y
# # print(xy_train[1][1])    # 없음 - [0][0] [0][1]에 다 몰아 넣었기 때문에

# # print(type(xy_train))           # <class 'tensorflow.python.keras.preprocessing.image.DirectoryIterator'>
# # print(type(xy_train[0]))        # <class 'tuple'>
# # print(type(xy_train[0][0]))     # <class 'numpy.ndarray'>
# # print(type(xy_train[0][1]))     # <class 'numpy.ndarray'>


# np.save('./_save/_npy/k59_3_train_x.npy', arr=xy_train[0][0])
# np.save('./_save/_npy/k59_3_train_y.npy', arr=xy_train[0][1])
# np.save('./_save/_npy/k59_3_test_x.npy', arr=xy_test[0][0])
# np.save('./_save/_npy/k59_3_test_y.npy', arr=xy_test[0][1])

