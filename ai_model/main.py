# train_model.py
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import MeanAbsoluteError

# Load and prepare data
df = pd.read_csv(
    r"E:\eng_yousef\4fourth_year_power\2st term\GraduationProject\code\ourAIModle\GA_results.csv"
)

x = df[['PL', 'PF']].values
y = df[['Kw_bar','Ta','Tb','k1_bar','K2','T1','T2','T3','T4']].values

scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()
X_scaled = scaler_X.fit_transform(x)
y_scaled = scaler_y.fit_transform(y)

#################################
# Save scalers for future use
import joblib
joblib.dump(scaler_X, "scaler_X.save")
joblib.dump(scaler_y, "scaler_y.save")
##############################

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.15, random_state=42)

# Build and compile model
model = Sequential([
    Dense(64, activation='tanh', input_shape=(2,)),
    Dense(64, activation='tanh'),
    Dense(64, activation='tanh'),
    Dense(9, activation='linear')
])
##########################################
# change it to make file work 
model.compile(
    optimizer='adam',
    loss=MeanSquaredError(),
    metrics=[MeanAbsoluteError()]
)
#################################

# Train model
early_stop = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)
history = model.fit(X_train, y_train, validation_split=0.1, epochs=500, batch_size=16, callbacks=[early_stop], verbose=1)

######################################
# Save model
model.save("controller_model.h5")
print("Model saved as 'controller_model.h5'")
#######################################

# Evaluate model
loss, mae = model.evaluate(X_test, y_test)
print(f"\nTest MSE: {loss:.5f}")
print(f"Test MAE: {mae:.5f}")


