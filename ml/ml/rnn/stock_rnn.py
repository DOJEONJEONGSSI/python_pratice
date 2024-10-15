import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import joblib
from tensorflow.python.keras.backend import reshape

# 데이터 로드 및 스케일링
df = pd.read_excel("./AAPL_2010-01-01_2024-10-10.xlsx", engine='openpyxl')
print(df.describe())
scaler = MinMaxScaler(feature_range=(0, 1))
# 정규화 0 ~ 1 사이의 값으로
df['Close'] = scaler.fit_transform(df['Close'].values.reshape(-1, 1))
joblib.dump(scaler, 'scaler.save')   # 나중에 사용하기 위해 저장

# 시퀀스 데이터 생성 x: 1~50일  y: 51
seq_len = 50
data_len = len(df['Close'].values)
all_len = seq_len + 1
sequence = []
for i in range(data_len - all_len):
    sequence.append(df['Close'][i : i + all_len])
ndarry_seq = np.array(sequence)
print(ndarry_seq)

# 학습 및 테스트 데이터 분리
train_size = int(round(ndarry_seq.shape[0] * 0.9))
train_data = ndarry_seq[:train_size, :]
test_data = ndarry_seq[train_size:, :]

x_train = train_data[:, :-1]
y_train = train_data[:, -1]
x_test = test_data[:, :-1]
y_test = test_data[:, -1]

# 오류 수정: np.reshape를 올바르게 사용
x_train_reshape = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test_reshape = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# RNN 모델 생성
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape=(seq_len, 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(1, activation='linear'))
model.compile(loss='mse', optimizer='adam')

# 오류 수정: model.fit()의 괄호 닫기
model.fit(x_train_reshape, y_train, validation_data=(x_test_reshape, y_test), batch_size=50, epochs=50)

# 모델 저장
model.save("AAPL.h5")

# 시각화
pred = model.predict(x_test_reshape)
plt.plot(y_test, label='true')
plt.plot(pred, label='pred')
plt.legend()
plt.show()