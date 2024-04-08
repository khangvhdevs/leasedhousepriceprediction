from joblib import load
import pandas as pd
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
dummies_data = data_dummies = pd.read_csv('data_dummies.csv')
loaded_model = load('linear_regression_model.joblib')
scaler.fit(dummies_data)

def Predict_price(district, square):
    new_input = pd.DataFrame({'acreage': [square], 'district': [district]})
    district_enconder = 'district_'+district
    # One-hot encode the district feature
    new_input_dummies = pd.get_dummies(new_input, drop_first=True)
    new_input_dummies
    # Ensure the columns are consistent with the training data
    # Add missing district columns if necessary
    missing_cols = set(dummies_data.columns) - set(new_input_dummies.columns)
    for col in missing_cols:
        new_input_dummies[col] = 0
    new_input_dummies[district_enconder] = 1
    # Reorder the columns to match the order of the training data
    new_input_dummies = new_input_dummies[dummies_data.columns]
    new_input_dummies = scaler.transform(new_input_dummies)
    # Predict using the trained model
    Y_pred = loaded_model.predict(new_input_dummies)
    predicted_price = round(Y_pred[0], 2)
    return predicted_price