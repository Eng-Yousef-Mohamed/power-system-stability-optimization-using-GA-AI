# Power System Stabilization via Genetic Algorithm and AI

This project combines MATLAB-based simulation and optimization using Genetic Algorithms (GA) with a Python-based AI model to enhance the dynamic stability of power systems.

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
