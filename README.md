<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sales Forecasting App | Meesam Raza</title>
    <!-- Google Fonts & Font Awesome -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #e9edf2 100%);
            color: #1e293b;
            line-height: 1.5;
        }

        .container {
            max-width: 1280px;
            margin: 0 auto;
            padding: 2rem 1.5rem;
        }

        /* Header / Hero */
        .hero {
            text-align: center;
            margin-bottom: 3rem;
        }

        .badge-group {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 0.75rem;
            margin-bottom: 1.5rem;
        }

        .badge {
            background: white;
            padding: 0.4rem 1rem;
            border-radius: 40px;
            font-size: 0.85rem;
            font-weight: 500;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: transform 0.2s;
        }
        .badge i { font-size: 1rem; }
        .badge:hover { transform: translateY(-2px); }

        h1 {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(135deg, #1E3A8A, #3B82F6);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin-bottom: 1rem;
        }

        .tagline {
            font-size: 1.2rem;
            color: #334155;
            max-width: 700px;
            margin: 0 auto 1.5rem;
        }

        .cta-buttons {
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 0.75rem 1.8rem;
            border-radius: 50px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.3s;
        }
        .btn-primary {
            background: #1E3A8A;
            color: white;
            box-shadow: 0 4px 12px rgba(30,58,138,0.3);
        }
        .btn-primary:hover {
            background: #2563EB;
            transform: scale(1.02);
        }
        .btn-outline {
            border: 2px solid #1E3A8A;
            color: #1E3A8A;
            background: transparent;
        }
        .btn-outline:hover {
            background: #1E3A8A;
            color: white;
        }

        /* cards */
        .card {
            background: white;
            border-radius: 28px;
            padding: 1.8rem;
            margin-bottom: 2rem;
            box-shadow: 0 20px 35px -12px rgba(0,0,0,0.08);
            transition: all 0.2s;
        }

        .section-title {
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            border-left: 5px solid #3B82F6;
            padding-left: 1rem;
        }

        .grid-2 {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.8rem;
        }

        .metric-card {
            background: #f8fafc;
            border-radius: 24px;
            padding: 1.5rem;
            text-align: center;
            border: 1px solid #e2e8f0;
        }
        .metric-value {
            font-size: 2.2rem;
            font-weight: 800;
            color: #0f172a;
        }

        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 0.8rem;
            margin-top: 1rem;
        }
        .tech-item {
            background: #eef2ff;
            padding: 0.4rem 1rem;
            border-radius: 40px;
            font-size: 0.85rem;
            font-weight: 500;
        }

        pre {
            background: #0f172a;
            color: #e2e8f0;
            padding: 1rem;
            border-radius: 16px;
            overflow-x: auto;
            font-size: 0.85rem;
            margin: 1rem 0;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }
        th {
            background: #f1f5f9;
            font-weight: 600;
        }

        .footer {
            text-align: center;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #cbd5e1;
            color: #475569;
        }

        @media (max-width: 640px) {
            .container { padding: 1.5rem; }
            h1 { font-size: 2rem; }
        }
    </style>
</head>
<body>
<div class="container">
    <!-- Hero -->
    <div class="hero">
        <div class="badge-group">
            <span class="badge"><i class="fab fa-python"></i> Python 3.10</span>
            <span class="badge"><i class="fas fa-chart-line"></i> Linear Regression</span>
            <span class="badge"><i class="fas fa-cloud-upload-alt"></i> Hugging Face Spaces</span>
            <span class="badge"><i class="fab fa-stream"></i> Streamlit</span>
        </div>
        <h1>💰 Sales Forecasting Web Application</h1>
        <p class="tagline">Predict sales amounts with ~80% accuracy — interactive ML app powered by scikit-learn, Streamlit & deployed on Hugging Face.</p>
        <div class="cta-buttons">
            <a href="https://huggingface.co/spaces/meesamraza/sales_model" target="_blank" class="btn btn-primary"><i class="fas fa-rocket"></i> Live Demo</a>
            <a href="https://github.com/meesamraza/sales-forecasting-app" target="_blank" class="btn btn-outline"><i class="fab fa-github"></i> GitHub Repo</a>
            <a href="https://www.linkedin.com/posts/meesam-raza-295701354_datascience-machinelearning-python-ugcPost-7450857056275718144-SIrP" target="_blank" class="btn btn-outline"><i class="fab fa-linkedin"></i> LinkedIn Post</a>
        </div>
    </div>

    <!-- Model Performance -->
    <div class="card">
        <div class="section-title">📊 Model Performance</div>
        <div class="grid-2">
            <div class="metric-card"><div class="metric-value">80.72%</div><div>Training R² Score</div></div>
            <div class="metric-card"><div class="metric-value">76.07%</div><div>Test R² Score</div></div>
            <div class="metric-card"><div class="metric-value">$1,021.98</div><div>RMSE (Test)</div></div>
            <div class="metric-card"><div class="metric-value">2,823</div><div>Sales Records</div></div>
        </div>
    </div>

    <!-- Key Features & Tech Stack -->
    <div class="grid-2">
        <div class="card">
            <div class="section-title" style="border-left-color:#10b981;">🔍 Key Features</div>
            <ul style="list-style: none; padding-left: 0;">
                <li style="margin-bottom: 12px;"><i class="fas fa-bolt" style="color:#3B82F6; width: 28px;"></i> Real-time predictions</li>
                <li style="margin-bottom: 12px;"><i class="fas fa-sliders-h" style="color:#3B82F6; width: 28px;"></i> Interactive UI with intuitive controls</li>
                <li style="margin-bottom: 12px;"><i class="fas fa-chart-bar" style="color:#3B82F6; width: 28px;"></i> Feature impact visualization (Plotly)</li>
                <li style="margin-bottom: 12px;"><i class="fas fa-percent" style="color:#3B82F6; width: 28px;"></i> Confidence indicator & dynamic insights</li>
                <li><i class="fas fa-mobile-alt" style="color:#3B82F6; width: 28px;"></i> Fully responsive design</li>
            </ul>
        </div>
        <div class="card">
            <div class="section-title" style="border-left-color:#f59e0b;">🛠️ Tech Stack</div>
            <div class="tech-stack">
                <span class="tech-item"><i class="fab fa-python"></i> Python 3.10</span>
                <span class="tech-item"><i class="fas fa-chart-simple"></i> Pandas / NumPy</span>
                <span class="tech-item"><i class="fas fa-brain"></i> scikit-learn</span>
                <span class="tech-item"><i class="fab fa-stream"></i> Streamlit</span>
                <span class="tech-item"><i class="fas fa-chart-line"></i> Plotly</span>
                <span class="tech-item"><i class="fas fa-database"></i> Joblib</span>
                <span class="tech-item"><i class="fas fa-cloud"></i> Hugging Face Spaces</span>
            </div>
            <div style="margin-top: 1.5rem;">
                <p><strong>🧠 Model:</strong> Linear Regression (high interpretability, fast inference)</p>
                <p><strong>📈 Preprocessing:</strong> StandardScaler, mode imputation, feature selection via correlation.</p>
            </div>
        </div>
    </div>

    <!-- Project structure + preprocessing -->
    <div class="card">
        <div class="section-title">📁 Project Structure & Data Pipeline</div>
        <div style="display: flex; flex-wrap: wrap; gap: 2rem;">
            <div style="flex: 1;">
                <pre style="background:#1e293b; color:#cbd5e6;">
sales-forecasting-app/
├── app.py                     # Streamlit frontend
├── sales project.ipynb        # EDA + model training
├── sales_forecasting_model.pkl
├── sales_scaler.pkl
├── requirements.txt
├── Dockerfile
└── README.md
                </pre>
            </div>
            <div style="flex: 1;">
                <ul style="margin-top: 0;">
                    <li>✅ Cleaned 2,823 sales records</li>
                    <li>✅ Handled missing values (STATE, TERRITORY)</li>
                    <li>✅ Removed low-correlation columns (phone, address, etc.)</li>
                    <li>✅ Selected 5 core features: PRICEEACH, MSRP, QUANTITYORDERED, ORDERNUMBER, YEAR_ID</li>
                </ul>
                <p style="margin-top: 1rem;"><strong>💡 Feature impact direction:</strong> Price & Quantity have highest positive coefficients → directly boost sales prediction.</p>
            </div>
        </div>
    </div>

    <!-- Local Installation & deployment -->
    <div class="card">
        <div class="section-title">🚀 Local Installation / Quick Start</div>
        <pre><code>git clone https://github.com/meesamraza/sales-forecasting-app.git
cd sales-forecasting-app
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py</code></pre>
        <p>🌐 <strong>Deploy on Hugging Face:</strong> Create new Space → choose Streamlit SDK → upload files → add Dockerfile (Python 3.10) → done. Your app will be live.</p>
        <div class="badge-group" style="justify-content: flex-start; margin-top: 1rem;">
            <span class="badge"><i class="fas fa-check-circle"></i> Python 3.10+ required</span>
            <span class="badge"><i class="fas fa-docker"></i> Docker ready</span>
        </div>
    </div>

    <!-- Feature impact table + screenshot placeholder -->
    <div class="card">
        <div class="section-title">📈 Feature Influence (Linear Regression Coefficients)</div>
        <table>
            <thead>
                <tr><th>Feature</th><th>Impact Direction</th><th>Interpretation</th></tr>
            </thead>
            <tbody>
                <tr><td>💰 Price Each</td><td>Strong Positive</td><td>Higher price per unit → higher total sales</td></tr>
                <tr><td>🏷️ MSRP</td><td>Positive</td><td>Correlates with premium positioning</td></tr>
                <tr><td>📦 Quantity Ordered</td><td>Strong Positive</td><td>More units → proportionally higher sales</td></tr>
                <tr><td>🔢 Order Number</td><td>Neutral</td><td>Minimal effect (mostly identifier)</td></tr>
                <tr><td>📅 Year ID</td><td>Slight Positive</td><td>Upward sales trend over years</td></tr>
            </tbody>
        </table>
        <div style="background: #f1f5f9; border-radius: 20px; padding: 1rem; text-align: center; margin-top: 1.5rem;">
            <i class="fas fa-image" style="font-size: 2rem; color:#64748b;"></i>
            <p style="margin-top: 8px;">📸 <strong>App Preview:</strong> Interactive sliders, live prediction card, and feature impact bar chart (Plotly).</p>
            <small>(Replace with actual screenshot URL if desired)</small>
        </div>
    </div>

    <!-- Troubleshooting + License -->
    <div class="grid-2">
        <div class="card">
            <div class="section-title">🔧 Troubleshooting</div>
            <ul>
                <li><strong>ModuleNotFoundError:</strong> run <code>pip install -r requirements.txt</code></li>
                <li><strong>Model file missing:</strong> ensure <code>.pkl</code> files are in root</li>
                <li><strong>Port conflict:</strong> <code>streamlit run app.py --server.port 8502</code></li>
                <li><strong>Hugging Face build fails:</strong> use Python 3.10/3.11 in Dockerfile</li>
            </ul>
        </div>
        <div class="card">
            <div class="section-title">📄 License & Connect</div>
            <p>MIT License — free to use, modify, and distribute.</p>
            <div style="display: flex; gap: 1rem; margin: 1rem 0;">
                <a href="https://www.linkedin.com/in/meesam-raza-295701354/" target="_blank" style="color:#0A66C2;"><i class="fab fa-linkedin fa-2x"></i></a>
                <a href="https://github.com/meesamraza" target="_blank" style="color:#181717;"><i class="fab fa-github fa-2x"></i></a>
                <a href="https://huggingface.co/meesamraza" target="_blank" style="color:#FFD21E;"><i class="fas fa-smile-wink fa-2x"></i></a>
            </div>
            <p>⭐ If you like this project, give it a star on GitHub and share it with your network!</p>
        </div>
    </div>

    <div class="footer">
        <p>Built with <i class="fas fa-heart" style="color:#ef4444;"></i> by Meesam Raza | Streamlit · scikit-learn · Hugging Face Spaces</p>
        <p><strong>Live Demo:</strong> <a href="https://huggingface.co/spaces/meesamraza/sales_model" target="_blank">https://huggingface.co/spaces/meesamraza/sales_model</a></p>
    </div>
</div>
</body>
</html>
