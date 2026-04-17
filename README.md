# 💰 Sales Forecasting Web Application

[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-yellow)](https://huggingface.co/spaces/meesamraza/sales_model)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://huggingface.co/spaces/meesamraza/sales_model)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

An interactive **Sales Forecasting Application** that predicts sales amounts with ~80% accuracy using a Linear Regression model. Built with Streamlit and deployed on Hugging Face Spaces.

## 🚀 Live Demo

Try the app live: **[Sales Forecasting App on Hugging Face Spaces](https://huggingface.co/spaces/meesamraza/sales_model)**

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| **Training R² Score** | 0.8072 (80.72%) |
| **Test R² Score** | 0.7607 (76.07%) |
| **RMSE** | $1,021.98 |

## 🔍 Key Features

- **Real-time Predictions** - Instant sales forecasts based on input parameters
- **Interactive UI** - User-friendly Streamlit interface with intuitive controls
- **Feature Impact Analysis** - Visualize which factors most influence sales
- **Confidence Indicator** - Real-time model confidence scoring
- **Responsive Design** - Works seamlessly on desktop and mobile devices

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| **Frontend** | Streamlit |
| **ML Model** | scikit-learn (Linear Regression) |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly |
| **Deployment** | Hugging Face Spaces |
| **Language** | Python 3.10 |

## 📁 Project Structure
sales-forecasting-app/
├── app.py # Streamlit web application
├── sales project.ipynb # Jupyter notebook with EDA & model training
├── sales_forecasting_model.pkl # Trained Linear Regression model
├── sales_scaler.pkl # StandardScaler for feature normalization
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration for deployment
├── .dockerignore # Docker ignore file
└── README.md # Project documentation


## 📝 Data Preprocessing

The model was trained on **2,823 sales records** with the following preprocessing steps:

- ✅ Handled missing values in STATE and TERRITORY columns using mode imputation
- ✅ Removed unnecessary columns (PHONE, ADDRESSLINE, CONTACT details, etc.)
- ✅ Selected 5 key features with highest correlation to sales:
  - PRICEEACH - Price per unit
  - MSRP - Manufacturer's Suggested Retail Price
  - QUANTITYORDERED - Number of units ordered
  - ORDERNUMBER - Order identification number
  - YEAR_ID - Year of the order

## 🤖 Model Selection

Linear Regression was chosen after comparing multiple algorithms due to:

- **High Interpretability** - Easy to understand feature impacts
- **Fast Inference Time** - Real-time predictions with minimal latency
- **Strong Baseline Performance** - 76% test R² score
- **Simplicity** - Minimal computational resources required

## 🚀 Local Installation & Usage

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Step 1: Clone the Repository


git clone https://github.com/meesamraza/sales-forecasting-app.git
cd sales-forecasting-app

##Common Issues & Solutions
Issue	Solution
ModuleNotFoundError	Run pip install -r requirements.txt
Model file not found	Ensure sales_forecasting_model.pkl is in the root directory
Port already in use	Run streamlit run app.py --server.port 8502
Hugging Face build fails	Check Python version compatibility (use 3.10 or 3.11)

##📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Connect with Me
https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
https://img.shields.io/badge/Hugging%2520Face-F9D9EE?style=for-the-badge&logo=huggingface&logoColor=black

##🙏 Acknowledgments
Dataset provided for educational purposes

Built with Streamlit - the fastest way to build data apps

Deployed on Hugging Face Spaces - free ML app hosting
