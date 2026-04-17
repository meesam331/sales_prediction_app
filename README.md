##Behind the Scenes: Building a Sales Forecasting Model

I recently completed a sales forecasting project that demonstrates the end-to-end ML workflow:

📝 Data Preprocessing:
• Cleaned 2,823 sales records
• Handled missing values in STATE and TERRITORY columns
• Selected 5 key features with highest correlation to sales

🤖 Model Selection:
After comparing multiple algorithms, Linear Regression was chosen for its:
• High interpretability
• Fast inference time
• Strong baseline performance (76% test R²)

🌐 Deployment:
The model is deployed on Hugging Face Spaces using Streamlit, making it accessible to non-technical users.

Check out the complete implementation below!

#MachineLearning #DataScience #Python #MLOps
