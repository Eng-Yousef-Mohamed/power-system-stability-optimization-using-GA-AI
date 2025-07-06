# use_model.py

import numpy as np
from tensorflow.keras.models import load_model
import joblib

######################################
# Load saved model and scalers
model = load_model("model/controller_model.h5")
scaler_X = joblib.load("model/scaler_X.save")
scaler_y = joblib.load("model/scaler_y.save")
###################################

# Predict from input
pl_input = 0.75
pf_input = 0.95
sample_input = np.array([[pl_input, pf_input]])
sample_scaled = scaler_X.transform(sample_input)
pred_scaled = model.predict(sample_scaled)
pred = scaler_y.inverse_transform(pred_scaled)

# Print results in MATLAB format
labels = ['Kw_bar', 'Ta', 'Tb', 'k1_bar', 'K2', 'T1', 'T2', 'T3', 'T4']
print(f"\n%% Predicted controller parameters for PL={pl_input*100:.0f}%, PF={pf_input:.2f}")
for name, val in zip(labels, pred[0]):
    print(f"{name:<8} = {val:.8f};")

# Optional: print as vector
print("\npredicted = [", end="")
for i, val in enumerate(pred[0]):
    sep = " " if i < len(pred[0]) - 1 else ""
    print(f"{val:.8f}{sep}", end="")
print("];")
