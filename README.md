# Water Quality Prediction Project

## Overview
This project predicts water quality using machine learning to help identify safe drinking water sources. It analyzes key water parameters and classifies water as safe or unsafe for consumption.

## 🛠Features
- **Data Analysis**: Examines 9 water quality parameters like pH, hardness, and chloramines
- **Machine Learning**: Predicts water safety with 88% accuracy
- **User-Friendly**: Simple interface to check water safety

## Dataset
Uses the **Water Quality** dataset containing:
- 3,276 water samples
- 9 measurement features
- Safety labels (0 = unsafe, 1 = safe)

## 🔬 Features

| Feature             | Description                          |
|---------------------|--------------------------------------|
| pH                  | pH value of water                    |
| Hardness            | Hardness of water                    |
| Solids              | Total dissolved solids               |
| Chloramines         | Amount of chloramines                |
| Sulfate             | Sulfate concentration                |
| Conductivity        | Electrical conductivity              |
| Organic_carbon      | Organic carbon content               |
| Trihalomethanes     | Trihalomethanes level                |
| Turbidity           | Turbidity level                      |

## Models Tested
1. **Random Forest** (Best performance - 88% accuracy)
2. Logistic Regression
3. Decision Tree
4. Support Vector Machine

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/water-quality-prediction.git
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the prediction:
   ```python
   python predict_quality.py
   ```

## 📂 Project Structure
```
water-quality-prediction/
├── data/                   # Dataset files
├── models/                 # Saved ML models
├── notebooks/              # Jupyter notebooks
├── src/                    # Source code
│   ├── train.py            # Training script
│   └── predict.py          # Prediction script
├── requirements.txt        # Dependencies
└── README.md               # This file
```

## How to Contribute
1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## 📜 License
MIT License - Free for educational and research use

## Contact
For questions, email: sumitrathore45528@gmail.com

---

**Note**: This project is for educational purposes only. Always consult water quality experts for real-world applications.
