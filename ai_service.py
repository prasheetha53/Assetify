from flask import Flask, jsonify, request
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.externals import joblib
from sklearn.preprocessing import MinMaxScaler
from utils import load_dataset  # Import the utility function

app = Flask(__name__)

# Load trained model and scaler
model_path = 'models/turbofan_model.pkl'
scaler_path = 'models/minmax_scaler.pkl'
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Perform data analysis and generate reports
def generate_reports():
    df = load_dataset()

    # Example report: Distribution of operational settings
    plt.figure(figsize=(10, 6))
    sns.histplot(df.iloc[:, 0], bins=20, kde=True, color='blue')
    plt.title('Distribution of Operational Setting 1')
    plt.xlabel('Operational Setting 1')
    plt.ylabel('Count')
    plt.savefig('reports/operational_setting_1_distribution.png')
    plt.close()

    # Example report: RUL distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df.iloc[:, -1], bins=20, kde=True, color='green')
    plt.title('Distribution of Remaining Useful Life (RUL)')
    plt.xlabel('RUL')
    plt.ylabel('Count')
    plt.savefig('reports/rul_distribution.png')
    plt.close()

    # Save reports to a specific directory
    reports_dir = 'reports'
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    print("Reports generated successfully!")

# Endpoint for predicting using the model
@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = data['features']
        
        # Preprocess features using the saved scaler
        features_scaled = scaler.transform([features])[0]

        # Predict using the model
        prediction = model.predict([features_scaled])[0]

        return jsonify({'prediction': prediction}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to generate reports
@app.route('/api/generate_reports', methods=['GET'])
def generate_reports_route():
    try:
        generate_reports()
        reports_dir = 'reports'
        report_files = os.listdir(reports_dir)
        return jsonify({'message': 'Reports generated successfully!', 'reports': report_files}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to generate specific reports
@app.route('/api/generate_report/<report_type>', methods=['GET'])
def generate_specific_report(report_type):
    try:
        if report_type == 'operational_setting':
            # Generate operational setting report
            generate_operational_setting_report()
            report_file = 'operational_setting_distribution.png'
        elif report_type == 'rul':
            # Generate RUL report
            generate_rul_report()
            report_file = 'rul_distribution.png'
        else:
            return jsonify({'error': 'Invalid report type.'}), 400

        return jsonify({'message': f'Report {report_file} generated successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_operational_setting_report():
    df = load_dataset()
    plt.figure(figsize=(10, 6))
    sns.histplot(df.iloc[:, 0], bins=20, kde=True, color='blue')
    plt.title('Distribution of Operational Setting 1')
    plt.xlabel('Operational Setting 1')
    plt.ylabel('Count')
    plt.savefig('reports/operational_setting_distribution.png')
    plt.close()

def generate_rul_report():
    df = load_dataset()
    plt.figure(figsize=(10, 6))
    sns.histplot(df.iloc[:, -1], bins=20, kde=True, color='green')
    plt.title('Distribution of Remaining Useful Life (RUL)')
    plt.xlabel('RUL')
    plt.ylabel('Count')
    plt.savefig('reports/rul_distribution.png')
    plt.close()

if __name__ == '__main__':
    app.run(debug=True)
