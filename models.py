import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

def load_data(file_path='datasets/train_FD001.txt'):
    # Load dataset
    df = pd.read_csv(file_path, sep=' ', header=None)
    df.drop(df.columns[[26, 27]], axis=1, inplace=True)  # Remove columns with no variance
    return df

def preprocess_data(df):
    # Split features and target
    X = df.iloc[:, 2:-1].values  # Assuming columns 2 to second-to-last are features
    y = df.iloc[:, -1].values   # Assuming last column is target (RUL)
    
    # Scale features
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Save the scaler for later use
    joblib.dump(scaler, 'models/minmax_scaler.pkl')
    
    return X_scaled, y

def load_model(model_path='models/turbofan_model.pkl'):
    # Load trained model from disk
    model = joblib.load(model_path)
    return model

def predict_rul(model, data):
    # Load the scaler
    scaler = joblib.load('models/minmax_scaler.pkl')
    # Scale the data
    data_scaled = scaler.transform(data)
    # Perform prediction using the loaded model
    prediction = model.predict(data_scaled)
    return prediction
