# ⚡ Power System Stability Optimization using Genetic Algorithm & AI

This project focuses on improving power system stability using an AI-based prediction model, trained using data generated from Genetic Algorithm (GA) optimization in MATLAB.

---

## 📁 Project Structure

```plaintext
power-system-stability-optimization/
├── matlab_ga_model/             # MATLAB GA optimization script
│   └── optimize_controller.m
│
├── dataset_generation/          # Loops through PL/PF values and runs GA
│   └── generate_dataset_loop.m
│
├── data/
│   └── GA_results.csv           # Generated dataset (PL, PF → Optimal Params)
│
├── ai_model/                    # Python AI model
│   ├── main.py                  # Training + inference entry point
│   ├── use_model.py             # Predict parameters from new inputs
│   ├── model/
│   │   ├── controller_model.h5  # Trained Keras model
│   │   ├── scaler_X.save        # Input scaler
│   │   └── scaler_y.save        # Output scaler
│
├── docs/
│   └── thesis_summary.md        # Graduation project summary (optional)
└── README.md                    # Project documentation
```

## ⚙️ MATLAB: GA-Based Controller Optimization

- Optimizes 9 controller parameters: `Kw̄, Ta, Tb, k1̄, K2, T1, T2, T3, T4`
- Uses PM and GM margins as fitness criteria
- Simulates the effect of these parameters on system stability
- Generates a dataset under different Load (PL) and Power Factor (PF) conditions

📁 Folder: `matlab_ga_model/`

## 📊 Dataset Generation

- The script runs GA under varying PL and PF values
- Results are saved in `GA_results.csv`
- Used to train AI model

📁 Folder: `dataset_generation/`

## 🤖 Python AI Model

- Trained using the GA-generated dataset
- Predicts optimal controller parameters given new `PL` and `PF`
- Built with TensorFlow/Keras and scikit-learn

📁 Folder: `ai_model/`

## 📁 Dataset

- File: `data/GA_results.csv`

## 📌 How to Use

### MATLAB (GA Optimization)
1. Open `optimize_controller.m`
2. Run the script in MATLAB
3. View eigenvalues and response plots

### Python (AI Inference)
```bash
cd ai_model/
pip install -r ../requirements.txt
python main.py
